Upgrading Clusters
==================

This section is the detailed HVM cluster upgrade reference (layout transitions, rolling Host updates, Agent behavior on the Host, and verification). For the overall |morpheus| upgrade entry point—including Manager VM, HA app nodes, and when to return here for HVM—start at :doc:`/getting_started/maintenance/upgrading`.

Upgrade sequence
^^^^^^^^^^^^^^^^

Complete these steps in order. Layout and rolling cluster updates depend on a Manager that already includes the target release's update definitions.

#. **Upgrade the** |morpheus| **appliance (Manager)** — Required before you can offer or run layout updates. See :ref:`hvm-appliance-upgrade` below.
#. **Run the cluster layout or rolling update** — After the Manager is on the target version, perform the layout transition (for example 1.2 → 1.3) or a rolling host update from the cluster actions in the UI. See the sections that follow.
#. **Confirm agent and quorum health** — Host Agent upgrades that a layout update requires are handled automatically during the cluster update when needed; verify connectivity and Quorum afterward.

.. important:: A layout upgrade and an HVM OS update are separate operations. Layout 1.3 uses HVM OS/Ubuntu 24.04; layout 2.0 uses HVM OS 26.04. The supported layouts run in parallel. Do not change a cluster's layout or HVM OS outside a documented product workflow.

.. warning:: The rolling update described here is an orchestrated cluster operation that runs the update and rollback scripts supplied by the selected HVM layout. It is not approval to perform an arbitrary Ubuntu release upgrade, replace package sources, or run general-purpose base-OS upgrade commands on an HVM host. No supported in-place base-OS transition outside a released cluster update is documented. If the required target OS is not offered by a product workflow, stop and contact Support for an approved migration or host-replacement plan; do not derive one from generic Ubuntu guidance.

.. _hvm-appliance-upgrade:

Step 1: Morpheus Appliance Upgrade
----------------------------------

Upgrade the |morpheus| appliance **before** starting any HVM layout or rolling cluster update. The Manager release publishes the cluster update definitions and minimum Agent versions that the later steps consume. Do not attempt a layout update against an older Manager that does not yet offer that update.

How to upgrade the appliance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the Getting Started upgrade hub for your topology — that is the canonical package procedure:

:doc:`/getting_started/maintenance/upgrading`

**Primary path — HPE Morpheus Manager VM (Debian package):** Most HVM deployments use the HPE Morpheus Manager QCOW2 (or equivalent) on Ubuntu/Debian. Use the Debian / Ubuntu section of :ref:`singleUpgrade`:

.. code-block:: bash

   sudo morpheus-ctl stop morpheus-ui
   sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
   sudo morpheus-ctl reconfigure

**Other topologies:**

- **Single-node on your own guest OS** (``.deb`` or ``.rpm``): :ref:`singleUpgrade`
- **3-Node HA:** :doc:`/getting_started/maintenance/upgrades/3node/overview`
- **Full HA:** :doc:`/getting_started/maintenance/upgrades/fullha/overview`

A Getting Started summary of Manager-then-HVM order is also in :doc:`/getting_started/maintenance/upgrades/hvm_clusters`.

HVM behavior during the appliance upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While the Manager is offline for the package install and reconfigure:

- Active HVM clusters continue to operate (agents are self-sustaining)
- Quorum decisions are made by agents independently of the appliance
- Heartbeat writes continue regardless of appliance connectivity
- VM failover still works during appliance downtime

.. NOTE:: The |morpheus| agent's QuorumCheckService operates autonomously. Cluster quorum, heartbeat monitoring, and failover continue even if the |morpheus| appliance is offline for maintenance.

Post-upgrade verification (before layout updates)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the appliance upgrade completes and the UI is available:

#. Navigate to :menuselection:`Infrastructure --> Clusters`
#. Verify all clusters show their expected state
#. Check the Quorum panel for each cluster — confirm ACHIEVED status
#. Verify agent connectivity (all hosts show recent ``lastAgentUpdate``)

Only after this verification, proceed to a layout upgrade or rolling cluster update.

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

The layout upgrade is performed as part of a cluster update operation after the Manager is on a release that publishes the 1.2-to-1.3 update. During the upgrade:

.. IMPORTANT:: The released HVM 1.2-to-1.3 update definitions require |morpheus| Agent 3.2.7 or later on each Host. This minimum applies to this layout transition only; it is not a general Agent requirement for every VME Manager upgrade or every HVM update. The cluster update upgrades an older Host Agent before running the transition scripts and stops if the Agent cannot reconnect at the required version.

#. Pacemaker services are disabled and removed
#. The |morpheus| agent's QuorumCheckService activates
#. Quorum info is sent to all agents
#. Agents begin peer-to-peer quorum pinging

Post-Upgrade: Corosync Authkey
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: For clusters upgraded from 1.2 to 1.3, the Corosync authkey may not be stored in Cypher (since 1.2 clusters managed authkey distribution via Pacemaker). |morpheus| automatically detects this condition and retroactively stores the authkey from an online host. This ensures that future add-worker operations can distribute the authkey to new hosts.

Rolling Cluster Updates
------------------------

Layouts 1.3 and 2.0 support rolling updates where each host is updated one at a time without cluster downtime.

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

Agent Package Updates
-----------------------

The |morpheus| agent on each cluster host can be updated independently of cluster layout updates. Automatic upgrades run when a layout or rolling cluster update requires a minimum Agent version. Manual upgrades are the supported path after Manager patch (and many minor) releases that do not ship an HVM layout update, so Hosts receive Agent improvements such as quorum and health-check logic and telemetry.

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

Manual Host Agent upgrades **are** recommended when a Manager patch or minor release does not include an HVM layout or rolling cluster update. Layout-driven updates upgrade the Agent automatically only when ``minAgentVersion`` requires it. Patch releases often still ship Host Agent improvements—for example quorum and health-check logic, fencing behavior, and telemetry—that do not ride a layout change. After those Manager upgrades, trigger Agent upgrades on each HVM Host so the cluster picks up the new Agent package.

To upgrade from the UI:

#. Open the Host detail page (:menuselection:`Infrastructure --> Clusters --> [Cluster] --> Hosts`, or the Hosts list)
#. Expand :guilabel:`ACTIONS` and select :guilabel:`Upgrade Agent`
#. Wait for the Agent to disconnect and reconnect, then confirm the reported Agent version

Repeat for **every** HVM Host in the cluster. Alternatively, select :guilabel:`Download Agent Script`, connect to that Host over SSH, and run the downloaded script. Scripts are Host-specific; download and run the correct script on each Host.

.. NOTE:: When a rolling cluster or layout update is in progress and defines a ``minAgentVersion``, prefer letting that update upgrade the Agent automatically. Use manual :guilabel:`Upgrade Agent` for Manager releases that do not run a layout update, or when release notes call out a Host Agent upgrade.

After a Manager upgrade that does not include a layout update, check for available Host Agent upgrades before treating the environment as fully current. See also the Agent guidance in :doc:`/release_notes/lifecycle` and the release notes for the Manager version you installed.

Pre-Upgrade Checklist
----------------------

Before performing a cluster layout or rolling update:

.. list-table::
   :widths: 5 95
   :header-rows: 0

   * - ☐
     - Upgrade the |morpheus| appliance to the target Manager release and confirm the UI is healthy (see :ref:`hvm-appliance-upgrade`)
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
