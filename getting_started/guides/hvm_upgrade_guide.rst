HVM Deployment Upgrade Guide
=============================

This guide provides a cohesive, end-to-end upgrade procedure for a complete HVM deployment. An HVM deployment consists of the |morpheus| Manager (appliance), one or more HVM clusters, the |morpheus| Agents on cluster hosts, and host-level packages. Each component has its own upgrade mechanism, but they must be performed in the correct order.

.. important:: Always review the release notes for your target version before starting. Some releases may have specific prerequisites or change the upgrade order.

Upgrade Order
--------------

The recommended upgrade sequence is:

.. list-table::
   :widths: 5 25 70
   :header-rows: 1

   * - Step
     - Component
     - Description
   * - 1
     - |morpheus| Manager
     - Upgrade the appliance software. HVM clusters remain self-sustaining during this operation.
   * - 2
     - HVM Cluster (Rolling Update)
     - Trigger the cluster update from the Manager UI. This upgrades agents, host packages, and layout scripts per host.
   * - 3
     - Post-Upgrade Verification
     - Confirm health across all layers: Manager, cluster quorum, agents, and VMs.

.. note:: In most cases, Step 2 (the rolling cluster update) automatically handles both agent upgrades and host package updates as part of its orchestrated process. You do not typically need to upgrade agents or packages independently.

Step 1: Upgrade the Morpheus Manager
--------------------------------------

The |morpheus| Manager appliance is upgraded first. HVM clusters operate autonomously during this window — quorum, heartbeat monitoring, and VM failover continue regardless of Manager availability.

**Procedure:**

#. **Back up the Manager database and configuration** before starting. See :doc:`/getting_started/guides/backup_restore`.

#. Follow the appropriate appliance upgrade procedure for your topology:

   - Single node: :doc:`/getting_started/maintenance/upgrades/single/singlenode`
   - 3-node HA: :doc:`/getting_started/maintenance/upgrades/3node/overview`
   - Full HA: :doc:`/getting_started/maintenance/upgrades/fullha/overview`

#. After the Manager is upgraded and accessible, verify:

   - The Manager UI is reachable and login succeeds
   - Navigate to ``Infrastructure > Clusters`` and confirm all clusters are visible
   - Agent connectivity: all hosts show recent ``lastAgentUpdate`` timestamps

.. tip:: The Manager upgrade does not require cluster maintenance mode. Clusters continue operating normally throughout the appliance upgrade window.

Step 2: Rolling Cluster Update
-------------------------------

Once the Manager is running the new version, trigger the cluster update. This is an orchestrated operation that processes each host sequentially:

**What the rolling update does per host:**

#. **Upgrades the Morpheus Agent** (if the host agent is below the required ``minAgentVersion`` for the update)
#. **Enters maintenance mode** — Live-migrates all VMs off the host
#. **Executes update scripts** — Applies host package updates, configuration changes, and layout-specific operations
#. **Exits maintenance mode** — Host returns to service and can receive VMs again
#. **Proceeds to next host**

After all hosts complete, any ``postUpdate`` scripts run across the cluster.

**Triggering the update:**

#. Navigate to ``Infrastructure > Clusters > [Your Cluster]``
#. If an update is available, the UI will indicate it. Select the update action.
#. Monitor progress in the cluster history/activity feed

**Prerequisites before starting:**

.. list-table::
   :widths: 5 95
   :header-rows: 0

   * - ☐
     - Cluster health: Quorum ACHIEVED, all nodes ONLINE, no fenced nodes
   * - ☐
     - N+1 capacity: remaining hosts can absorb workloads during per-host maintenance
   * - ☐
     - No pinned VMs blocking maintenance mode evacuation
   * - ☐
     - Shared storage healthy: all datastores PROVISIONED
   * - ☐
     - No other maintenance or Dynamic Placement operations in progress
   * - ☐
     - Network connectivity between all hosts verified (port 7443, SSH)

**Failure handling:**

If the update fails on any host:

- Rollback scripts execute on the failed host and all previously updated hosts
- The cluster returns to its pre-update state
- Review the error, resolve the underlying issue, and retry

For full details on rolling updates, failure handling, and rollback, see :doc:`/infrastructure/clusters/hvm/upgrading`.

Layout Upgrades (1.2 → 1.3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If upgrading from layout 1.2 to 1.3, the rolling update additionally:

- Disables and removes Pacemaker services
- Activates the |morpheus| Agent QuorumCheckService
- Distributes quorum configuration to all agents

After this upgrade, ``pcs`` commands are no longer applicable. Use ``corosync-quorumtool`` and the agent ``/quorum`` endpoint for cluster operations.

.. important:: The 1.2-to-1.3 layout transition requires Agent 3.2.7 or later on each host. The rolling update upgrades older agents automatically before running transition scripts.

Agent Upgrades
^^^^^^^^^^^^^^^

Agent upgrades are handled automatically during the rolling cluster update when needed. Manual agent upgrades are typically not required.

If you need to verify agent versions outside of a cluster update:

- Navigate to ``Infrastructure > Clusters > [Cluster] > Hosts``
- Check the agent version reported for each host
- The cluster update will upgrade any agent below ``minAgentVersion`` before applying host updates

Host Package Updates
^^^^^^^^^^^^^^^^^^^^^

Host-level package updates (kernel, libraries, HVM OS packages) are applied by the update scripts during the rolling update. These are not arbitrary ``apt upgrade`` operations — they are curated package sets defined by the cluster layout and delivered through the update mechanism.

.. warning:: Do not run ``apt upgrade``, ``do-release-upgrade``, or modify package sources on HVM hosts outside of the documented cluster update process. Only the rolling update's layout-defined scripts are supported for host-level package changes.

Step 3: Post-Upgrade Verification
-----------------------------------

After both the Manager and cluster updates complete, verify the full stack:

**Manager verification:**

- UI accessible, all expected clouds and clusters visible
- Check ``Administration > Health`` for any service warnings

**Cluster verification:**

#. Quorum health:

   .. code-block:: bash

      curl -k https://localhost:7443/quorum

   Confirm quorum is ACHIEVED with all nodes ONLINE.

#. Corosync membership:

   .. code-block:: bash

      corosync-quorumtool -s

   Confirm ``Quorate: Yes`` and all expected nodes listed.

#. DLM status:

   .. code-block:: bash

      dlm_tool status -v

   Confirm all nodes show ``member=1``.

#. Datastore mounts:

   .. code-block:: bash

      mount | grep gfs2

   Confirm all HPE Clustered Datastores are mounted.

#. UI Quorum panel (``Infrastructure > Clusters > [Cluster] > Summary > Quorum``):

   - Quorum: ACHIEVED
   - All nodes: ONLINE
   - Coordinator: assigned
   - Lockspaces: OK

**VM verification:**

- All VMs running and accessible
- No unexpected VM migrations or restarts in the activity log

Troubleshooting
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Symptom
     - Action
   * - Cluster update won't start
     - Verify quorum is ACHIEVED and no other operations are in progress
   * - Agent won't reconnect after upgrade
     - Check network connectivity (port 7443) and agent service status on the host
   * - Maintenance mode fails
     - Insufficient capacity to evacuate VMs. Free resources or add hosts before retrying.
   * - VMs not migrating back after update
     - Verify Dynamic Placement is enabled and the host has exited maintenance mode
   * - Quorum not achieved post-update
     - Check Corosync membership and DLM status. See :doc:`/infrastructure/clusters/hvm/troubleshooting`

Related Documentation
----------------------

- :doc:`/getting_started/maintenance/upgrading` — Manager appliance upgrade procedures
- :doc:`/infrastructure/clusters/hvm/upgrading` — Detailed cluster update mechanics and layout transitions
- :doc:`/infrastructure/clusters/hvm/host_maintenance` — Host maintenance mode operations
- :doc:`/infrastructure/clusters/hvm/troubleshooting` — Cluster diagnostic commands
- :doc:`/getting_started/guides/backup_restore` — Backup and restore procedures
