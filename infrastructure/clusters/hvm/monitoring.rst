Monitoring & Health Baselines
==============================

This section describes what a healthy layout 1.3 or 2.0 HVM cluster looks like, key metrics to monitor, and recommended alert thresholds.

What Healthy Looks Like
-------------------------

Quorum Panel (UI)
^^^^^^^^^^^^^^^^^^

Navigate to ``Infrastructure > Clusters > [Cluster] > Summary > Quorum`` to view the cluster health panel.

A healthy cluster displays:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Indicator
     - Expected Value
   * - Quorum Status
     - ACHIEVED
   * - Total Nodes
     - Matches your configured cluster size
   * - Reachable Nodes
     - Equals total nodes
   * - Online Nodes
     - All nodes show ONLINE member status
   * - Fenced Nodes
     - 0
   * - Down Hosts
     - Empty / None
   * - Designated Coordinator
     - One host assigned
   * - Lockspaces
     - OK (no waiting on fencing)
   * - Datastores
     - All PROVISIONED
   * - Witness (stretch clusters)
     - Connected

Agent Quorum Endpoint
^^^^^^^^^^^^^^^^^^^^^^

Query the agent's quorum status from any cluster host:

.. code-block:: bash

   curl -k https://localhost:7443/quorum

A healthy response includes:

- ``quorumAchieved: true``
- ``fenced: false``
- ``waitFencing: false``
- ``reachableNodes`` equals ``totalNodes``
- All nodes in the ``nodes`` array show as reachable
- ``corosyncActive: true``
- ``dlmActive: true``
- ``corosyncQuorate: true``

Corosync Health
^^^^^^^^^^^^^^^^

.. code-block:: bash

   corosync-quorumtool -s

Expected output includes:

- ``Quorate: Yes``
- ``Votes`` for each node equals 1
- ``Total votes`` matches the cluster size

DLM Health
^^^^^^^^^^^

.. code-block:: bash

   dlm_tool status -v

Expected output shows:

- All nodes with ``member=1``
- No nodes waiting on fencing

GFS2 Mounts
^^^^^^^^^^^^^

.. code-block:: bash

   mount | grep gfs2

All expected HPE Clustered Datastores should be mounted. Verify no filesystems are in a withdrawn state:

.. code-block:: bash

   cat /sys/fs/gfs2/*/withdraw

Expected output: ``0`` for all filesystems (``1`` indicates a withdrawn filesystem).

Key Metrics to Monitor
-----------------------

Host-Level Metrics
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Metric
     - Healthy Range
     - Concern Threshold
   * - Agent last update
     - Within 2 minutes
     - > 2 minutes indicates agent or network issue
   * - Host power state
     - ``on``
     - ``off`` or ``unknown`` requires investigation
   * - Memory utilization
     - < 85% of computed max
     - > 90% risks inability to evacuate during maintenance
   * - CPU utilization
     - Varies by workload
     - Sustained > 90% impacts VM performance
   * - Cluster member status
     - ``online``
     - ``offline``, ``fenced``, ``unclean`` require the layout-aware recovery in :doc:`troubleshooting`

Cluster-Level Metrics
^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Metric
     - Healthy Range
     - Concern Threshold
   * - Quorum status
     - ACHIEVED
     - LOST requires immediate attention
   * - Reachable nodes
     - Equals total nodes
     - Any difference indicates a node issue
   * - Heartbeat currency
     - All hosts writing within 20s interval
     - > 60s since last write indicates an issue
   * - DLM lockspaces
     - Active, no fencing waits
     - Wait fencing state blocks I/O operations
   * - Datastore status
     - All PROVISIONED
     - WARNING or FAILED requires investigation

Storage Metrics
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Metric
     - Healthy Range
     - Concern Threshold
   * - Datastore free space
     - > 20% free
     - < 15% risks provisioning failures
   * - GFS2 withdraw status
     - 0 (not withdrawn)
     - 1 requires unmount/remount or reboot
   * - iSCSI session status
     - Active on all hosts
     - Lost sessions trigger APD protection
   * - Multipath status
     - All paths active
     - Degraded paths risk APD on further failures

Integration with Morpheus Monitoring
--------------------------------------

Cluster Health Alarms
^^^^^^^^^^^^^^^^^^^^^^

|morpheus| automatically generates alarms for critical cluster events:

- **Multiple heartbeat datastores detected** — When more than one datastore is marked as heartbeat target, an alarm is raised and the system auto-selects one
- **Host removal failure** — When a host cannot be cleanly removed due to no available online hypervisors
- **Cluster member status changes** — Host transitions to offline, fenced, or unclean states

These alarms appear in ``Operations > Health > Alarms``.

Cluster Summary Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The cluster summary (``Infrastructure > Clusters > [Cluster] > Summary``) provides an at-a-glance view of:

- Total/used/reserved memory across all hosts
- CPU utilization
- Storage capacity and usage
- VM count
- Host status breakdown (online, maintenance, warning, offline)

Recommended Alert Thresholds
------------------------------

Configure the following monitoring alerts for proactive cluster management:

.. list-table::
   :widths: 30 25 45
   :header-rows: 1

   * - Alert
     - Threshold
     - Action
   * - Quorum lost
     - Immediate
     - Investigate host/network failures; potential data risk
   * - Node unreachable
     - > 60 seconds
     - Check host connectivity, agent status
   * - Host memory > 90%
     - Sustained 5 min
     - Consider migrating VMs or adding hosts
   * - Datastore free < 15%
     - Sustained
     - Add storage capacity or migrate VMs
   * - GFS2 withdrawn
     - Any occurrence
     - Unmount/remount or reboot affected host
   * - APD activated
     - Any occurrence
     - Investigate storage connectivity immediately
   * - DLM wait fencing
     - > 30 seconds
     - Check if agent is issuing fence_ack; manual intervention may be needed
   * - Agent last update > 5 min
     - Sustained
     - Agent may be down; check agent service on host

Log Monitoring
---------------

Key log files to monitor for cluster health:

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Log
     - What to Watch For
   * - ``/var/log/dlm_controld/dlm_controld.log``
     - Fence events, member changes, lockspace errors
   * - ``journalctl -u corosync``
     - Membership changes, quorum state transitions
   * - ``/var/log/kern.log``
     - GFS2 withdraw events, DLM kernel messages
   * - Agent logs
     - Quorum check results, heartbeat write failures, failover events

Expected Log Messages (Healthy)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During normal operation, you should see:

- Periodic quorum check messages (every 20 seconds)
- Heartbeat write confirmations
- DLM lockspace activity during storage I/O
- Corosync membership stable (no join/leave events)

Warning Log Messages
^^^^^^^^^^^^^^^^^^^^^

Investigate immediately if you see:

- ``gfs2: fsid=*: withdrawing``
- DLM fence wait messages
- Corosync membership changes (unexpected joins/leaves)
- Agent quorum state changes
- APD threshold reached messages
