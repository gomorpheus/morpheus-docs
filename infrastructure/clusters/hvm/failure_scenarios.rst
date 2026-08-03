Failure Scenarios
=================

This section documents the expected behavior and timelines for common failure scenarios in layout 1.3 and 2.0 HVM clusters.

Scenario 1: Single Host Failure
--------------------------------

A single host becomes unavailable due to hardware failure, OS crash, or power loss.

Timeline
^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Time
     - Event
   * - T+0s
     - Host stops responding to quorum pings
   * - T+60s
     - Node marked unreachable (3 missed ping intervals)
   * - T+60–90s
     - Designated Coordinator issues ``fence_ack`` for the failed node
   * - T+140s
     - Heartbeat failure threshold reached (7 missed intervals)
   * - T+140s+
     - Coordinator assigns failed host's VMs to surviving hosts by available memory

**Recovery:** Automatic. Fix the underlying host issue and the node will rejoin on reboot.

Scenario 2: Storage Partition (APD)
------------------------------------

A host loses all paths to shared storage while remaining network-reachable to other cluster nodes.

Timeline
^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Time
     - Event
   * - T+0s
     - Storage paths fail, heartbeat writes begin failing
   * - ~T+2min
     - 6 consecutive failed heartbeat write cycles
   * - ~T+2min
     - APD protection activates: all non-pinned VMs on shared storage are shut down

**Recovery:** Restore storage connectivity to the affected host, then restart VMs. Investigate the root cause of the storage path failure.

Scenario 3: Network Partition
------------------------------

A network failure splits the cluster into two groups that cannot communicate with each other.

Timeline
^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Time
     - Event
   * - T+0s
     - Network partition occurs
   * - T+60s
     - Nodes on each side detect unreachable peers
   * - T+60s
     - Majority side: retains quorum, continues operations
   * - T+60s
     - Minority side: loses quorum, self-fences
   * - Recovery
     - When network is restored, fenced nodes reboot and rejoin

**Recovery:** Fix the network issue. Fenced hosts will automatically recover via reboot.

Scenario 4: Stretch Cluster Site Failure
-----------------------------------------

An entire site becomes unavailable in a stretch cluster configuration.

Timeline
^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Time
     - Event
   * - T+0s
     - All nodes at one site become unreachable
   * - T+60s
     - Site failure detected (all non-witness nodes at site unreachable)
   * - T+60s
     - Surviving site checks witness reachability
   * - T+60s
     - Arbitration: alphabetically first site name wins
   * - T+60s
     - Winner adjusts Corosync votes, issues ``fence_ack``
   * - T+60s
     - Loser self-fences (stops DLM, Corosync)
   * - T+140s
     - VM failover begins for VMs from the failed site

**Recovery:** Automatic. After the failed site is restored, 3 consecutive healthy cycles (~3 minutes) must pass. Votes are restored, fenced nodes reboot and rejoin. Redistribute VMs across sites after recovery.

Scenario 5: Single Node Reboot
-------------------------------

A single node is rebooted (planned or unplanned).

Fast Reboot (<140 seconds)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the node returns before the heartbeat failure threshold:

- No VM failover occurs
- Node rejoins quorum automatically

Slow Reboot (>140 seconds)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the reboot takes longer than the heartbeat failure threshold:

- VMs are moved to surviving hosts
- On boot, the node enters recovery mode
- Agent re-establishes quorum membership

**Recovery:** Automatic. Node rejoins cluster on boot.

Scenario 6: Layout 1.2 to 1.3 Upgrade
---------------------------------------

Upgrading from HVM layout 1.2 (Pacemaker-based) to layout 1.3 (agent-based quorum).

Process
^^^^^^^

#. Pacemaker services are disabled and removed
#. The |morpheus| agent's QuorumCheckService takes over quorum and fencing responsibilities
#. Corosync and DLM continue to operate (these components are shared between both layouts)

Verification After Upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the following commands to confirm the upgrade completed successfully:

.. code-block:: bash

   corosync-quorumtool -s
   dlm_tool status -v
   curl -k https://localhost:7443/quorum

Confirm:

- Corosync shows ``Quorate: Yes``
- DLM shows all nodes with ``member=1``
- Agent ``/quorum`` endpoint returns healthy status with all nodes ONLINE

.. NOTE:: After upgrading, ``pcs`` commands are no longer available or applicable. Use the diagnostic commands listed in :doc:`troubleshooting` for all cluster operations.

Recovery Matrix
---------------

.. list-table::
   :widths: 25 20 55
   :header-rows: 1

   * - Scenario
     - Recovery Type
     - Action Required
   * - Single host failure
     - Automatic
     - Fix host issue; node rejoins on reboot
   * - Storage partition (APD)
     - Manual
     - Restore storage connectivity, restart VMs
   * - Network partition
     - Automatic
     - Fix network; fenced hosts auto-recover via reboot
   * - Stretch site failure
     - Automatic
     - Site restores; redistribute VMs after recovery
   * - DLM stuck
     - Automatic/Manual
     - Agent auto-issues ``fence_ack``; manual if agent fails
   * - GFS2 withdrawn
     - Manual
     - Unmount/remount or reboot affected host
