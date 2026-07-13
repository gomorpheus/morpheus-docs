Upgrading Clusters
==================

This section covers upgrade procedures for HVM clusters, including layout upgrades, appliance version upgrades, and agent package updates.

Layout 1.2 → 1.3 Upgrade
--------------------------

The HVM 1.3 layout replaces the Pacemaker-based high availability stack with the |morpheus| agent's QuorumCheckService. Clusters running layout 1.2 can be upgraded to 1.3.

What Changes
^^^^^^^^^^^^

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Component
     - Layout 1.2
     - Layout 1.3
   * - Quorum/HA management
     - Pacemaker + Corosync
     - |morpheus| Agent (QuorumCheckService) + Corosync
   * - Fencing
     - STONITH via Pacemaker
     - Agent-based fence_ack via DLM
   * - Resource management
     - Pacemaker resource agents
     - Agent-managed mounts and health checks
   * - Failure detection
     - Pacemaker node monitoring
     - Peer-to-peer quorum pinging + heartbeat writes
   * - Cluster commands
     - ``pcs`` CLI
     - ``corosync-quorumtool``, ``dlm_tool``, agent ``/quorum`` endpoint

.. IMPORTANT:: After upgrading to layout 1.3, ``pcs`` commands are no longer available or applicable. Use the diagnostic commands listed in :doc:`troubleshooting` for all cluster operations.

What Is Preserved
^^^^^^^^^^^^^^^^^^

- **Corosync** — Continues to provide cluster membership and messaging (shared between both layouts)
- **DLM** — Continues to coordinate filesystem locks (shared between both layouts)
- **HPE Clustered Datastores** — GFS2 filesystems remain mounted and operational
- **VMs** — All running VMs continue without interruption
- **iSCSI connectivity** — Storage paths are unaffected

Upgrade Process
^^^^^^^^^^^^^^^^

The layout upgrade is performed as part of a cluster update operation. During the upgrade:

#. Pacemaker services are disabled and removed
#. The |morpheus| agent's QuorumCheckService activates
#. Quorum info is sent to all agents
#. Agents begin peer-to-peer quorum pinging

Post-Upgrade: Corosync Authkey
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: For clusters upgraded from 1.2 to 1.3, the Corosync authkey may not be stored in Cypher (since 1.2 clusters managed authkey distribution via Pacemaker). |morpheus| automatically detects this condition and retroactively stores the authkey from an online host. This ensures that future add-worker operations can distribute the authkey to new hosts.

Rolling Cluster Updates
------------------------

HVM 1.3 clusters support rolling updates where each host is updated one at a time without cluster downtime.

Update Process (Per Host)
^^^^^^^^^^^^^^^^^^^^^^^^^^

For each host in the cluster, the rolling update performs:

#. **Agent upgrade** (if required) — If the host's agent version is below the minimum required version, the agent is upgraded first. |morpheus| waits for the agent to reconnect after the upgrade.

#. **Enter maintenance mode** — VMs are evacuated from the host via live migration (see :doc:`host_maintenance`). A Dynamic Placement lock is acquired to prevent resource scheduling from interfering.

#. **Execute update scripts** — Layout-defined scripts run on the host (package updates, configuration changes, etc.)

#. **Exit maintenance mode** — The host returns to normal operation and can receive VMs again. The Dynamic Placement lock is released.

#. **Proceed to next host** — The process repeats for the next host.

After all hosts complete the update phase:

6. **Post-update scripts** — Any scripts designated as ``postUpdate`` phase run on each host.

Failure Handling
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Scenario
     - Behavior
   * - Agent upgrade fails
     - Update stops for that host; error is reported
   * - Maintenance mode fails (insufficient capacity)
     - Update stops for that host; VMs remain in place
   * - Update script fails
     - Rollback scripts run on the failed host and all previously succeeded hosts
   * - Agent does not reconnect after upgrade
     - Update stops; timeout error is reported

.. WARNING:: Only one cluster update operation can run at a time. Attempting to start a second update while one is in progress will be rejected.

Rollback Support
^^^^^^^^^^^^^^^^^

If the cluster layout defines rollback scripts, they are executed in reverse order on:

- The host where the failure occurred
- All hosts that previously completed the update phase successfully

This restores the cluster to its pre-update state.

Morpheus Appliance Upgrades
-----------------------------

When upgrading the |morpheus| appliance itself:

Pre-Upgrade Considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Active HVM clusters will continue to operate during the appliance upgrade (agents are self-sustaining)
- Quorum decisions are made by agents independently of the appliance
- Heartbeat writes continue regardless of appliance connectivity
- VM failover will still work during appliance downtime

.. NOTE:: The |morpheus| agent's QuorumCheckService operates autonomously. Cluster quorum, heartbeat monitoring, and failover continue even if the |morpheus| appliance is offline for maintenance.

Post-Upgrade Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

After upgrading the |morpheus| appliance:

#. Navigate to ``Infrastructure > Clusters``
#. Verify all clusters show their expected state
#. Check the Quorum panel for each cluster — confirm ACHIEVED status
#. Verify agent connectivity (all hosts show recent ``lastAgentUpdate``)

Agent Package Updates
-----------------------

The |morpheus| agent on each cluster host can be updated independently of cluster layout updates.

Automatic Agent Upgrades
^^^^^^^^^^^^^^^^^^^^^^^^^^

During rolling cluster updates, if a host's agent version is below the ``minAgentVersion`` required by the update definition, the agent is upgraded automatically before update scripts execute.

The automatic agent upgrade:

#. Triggers the agent upgrade on the host
#. Waits for the agent to disconnect and reconnect
#. Verifies the new agent version meets requirements
#. Proceeds with the update only after successful agent reconnection

Manual Agent Upgrades
^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: Manual agent upgrades are typically not required. The rolling cluster update process handles agent upgrades automatically when needed.

Pre-Upgrade Checklist
----------------------

Before performing any cluster upgrade:

.. list-table::
   :widths: 5 95
   :header-rows: 0

   * - ☐
     - Verify cluster health: Quorum ACHIEVED, all nodes ONLINE, no fenced nodes
   * - ☐
     - Confirm N+1 capacity: remaining hosts can absorb workloads during rolling maintenance
   * - ☐
     - Check for pinned VMs that may block maintenance mode
   * - ☐
     - Verify shared storage health: all datastores PROVISIONED, no withdrawn filesystems
   * - ☐
     - Take a backup of critical VM configurations
   * - ☐
     - Ensure no other maintenance or Dynamic Placement operations are in progress
   * - ☐
     - Verify network connectivity between all hosts (port 7443, SSH)
   * - ☐
     - Review the upgrade release notes for any known issues

Post-Upgrade Verification
--------------------------

After completing a cluster upgrade:

#. **Quorum health:**

   .. code-block:: bash

      curl -k https://localhost:7443/quorum

   Confirm quorum is ACHIEVED with all nodes ONLINE.

#. **Corosync membership:**

   .. code-block:: bash

      corosync-quorumtool -s

   Confirm ``Quorate: Yes`` and all expected nodes are listed.

#. **DLM status:**

   .. code-block:: bash

      dlm_tool status -v

   Confirm all nodes show ``member=1``.

#. **Datastore mounts:**

   .. code-block:: bash

      mount | grep gfs2

   Confirm all expected HPE Clustered Datastores are mounted.

#. **UI verification:**

   Navigate to ``Infrastructure > Clusters > [Cluster] > Summary > Quorum`` panel and confirm:

   - Quorum status: ACHIEVED
   - All nodes: ONLINE
   - Coordinator: assigned
   - Lockspaces: OK

#. **VM health:**

   Verify all VMs are running and accessible after the upgrade completes.
