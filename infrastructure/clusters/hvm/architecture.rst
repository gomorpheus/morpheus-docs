Architecture
============

Overview
--------

The HVM 1.3 cluster layout introduces a fundamentally new high-availability architecture for |morpheus| hypervisor clusters. The previous Pacemaker-based resource management has been replaced with the |morpheus| agent's QuorumCheckService, providing tighter integration with the |morpheus| platform and simplified operations.

Component Stack
^^^^^^^^^^^^^^^

The HVM 1.3 cluster relies on three core components:

- **Corosync**: Cluster membership and messaging layer
- **DLM (Distributed Lock Manager)**: Coordinates file locks for the HPE Clustered Datastore (GFS2) filesystem
- **Morpheus Agent (QuorumCheckService)**: Quorum decisions, failure detection, fencing, and recovery orchestration

Quorum Algorithm
----------------

The |morpheus| agent on each host runs a QuorumCheckService that continuously monitors cluster health and makes quorum decisions.

Peer Communication
^^^^^^^^^^^^^^^^^^

- Each host exposes a ``/quorum`` endpoint on port 7443
- Hosts ping each other every 20 seconds
- A node is considered unreachable after 60 seconds with no response
- Cross-verification: reachability is confirmed by a majority of same-site peers

Majority Calculation
^^^^^^^^^^^^^^^^^^^^

The quorum algorithm uses a simple majority formula:

.. code-block:: text

   neededForQuorum = (totalNodes / 2) + 1

Quorum States
^^^^^^^^^^^^^

Each node operates in one of three states:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - State
     - Description
   * - Quorum Achieved
     - A majority of cluster nodes are reachable. Normal operations continue.
   * - Quorum Lost
     - The node cannot reach a majority of peers. The node self-fences to protect data integrity.
   * - Fenced
     - The node has been fenced and is waiting for recovery.

Designated Coordinator
----------------------

The cluster elects a Designated Coordinator from among the reachable nodes. The coordinator is determined by the lowest hash of reachable host key hashes (sorted alphabetically). Only the coordinator is authorized to issue fencing operations.

Heartbeat Failover (MvmHeartbeatFailover)
------------------------------------------

The heartbeat failover mechanism monitors host health via shared storage and orchestrates VM recovery when a host fails.

Heartbeat Writes
^^^^^^^^^^^^^^^^

- Each host writes ``hb.properties`` to shared storage every 20 seconds
- The heartbeat file contains hostname, memory statistics, and timestamp
- VM XML definitions are written for all running VMs alongside the heartbeat

Failure Detection
^^^^^^^^^^^^^^^^^

- A host is considered offline after 140 seconds (7 missed heartbeat intervals)
- The Designated Coordinator assigns the failed host's VMs to surviving hosts based on available memory

Storage Structure
^^^^^^^^^^^^^^^^^

Heartbeat data is stored on the HPE Clustered Datastore (Shared LUN) at:

.. code-block:: text

   <datastore>/mvm-hb/<cluster_uuid>-2/<host_hash>/
     ├── hb.properties
     ├── *.xml          (VM definitions)
     └── recover/

APD (All Paths Down) Protection
--------------------------------

APD protection prevents split-brain data corruption when a host loses access to shared storage.

- After 6 consecutive failed heartbeat writes (~2 minutes), all non-pinned VMs on shared storage are shut down
- This prevents VMs from running with stale data while another host may be serving the same storage

Timing Constants
----------------

.. list-table::
   :widths: 40 30 30
   :header-rows: 1

   * - Parameter
     - Value
     - Description
   * - Ping interval
     - 20s
     - Frequency of quorum peer checks
   * - Quorum timeout
     - 60s
     - Time before a node is marked unreachable
   * - Heartbeat interval
     - 20s
     - Frequency of heartbeat writes to shared storage
   * - Heartbeat failure threshold
     - 140s (7 missed)
     - Time before a host is considered offline
   * - APD threshold
     - ~2 minutes (6 failed cycles)
     - Time before VMs shut down on storage loss
   * - Fence_ack cooldown
     - 60s
     - Cooldown period after a fence acknowledgement
   * - DLM fence_wait delay
     - Up to 30s
     - Maximum DLM delay waiting for fence resolution

Persistence Files
-----------------

The |morpheus| agent persists cluster state to the following files on each host:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - File Path
     - Purpose
   * - ``/opt/morpheus-node/.quorum-nodes``
     - Cluster member list
   * - ``/opt/morpheus-node/.hb``
     - Heartbeat job configuration
   * - ``/opt/morpheus-node/.mounts``
     - HPE Clustered Datastore (GFS2) mount list
