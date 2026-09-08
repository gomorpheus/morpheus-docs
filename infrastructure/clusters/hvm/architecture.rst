Architecture
============

Overview
--------

Layouts 1.3 and 2.0 use the |morpheus| Agent's QuorumCheckService for high availability. This architecture replaces the Pacemaker-based resource management used by Legacy layouts, providing tighter integration with the |morpheus| platform and simplified operations.

.. note:: This page applies to layouts 1.3 and 2.0. For the Pacemaker architecture used by Legacy layouts, see :doc:`/infrastructure/clusters/mvm`.

Component Stack
^^^^^^^^^^^^^^^

Layouts 1.3 and 2.0 rely on three core components:

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
- On a two-node GFS2 cluster, both Hosts ping each other on TCP 7443 and must also reach the Distributed Worker URL. Do not apply same-site peer cross-verification to this topology.
- On a stretch cluster, reachability is confirmed by a majority of same-site peers. Site-level arbitration is documented in :doc:`stretch_clusters`.

Majority Calculation
^^^^^^^^^^^^^^^^^^^^

The quorum algorithm uses a simple majority formula:

.. code-block:: text

   neededForQuorum = (totalNodes / 2) + 1

``totalNodes`` counts every Agent quorum member. On a two-node GFS2 cluster that includes a Distributed Worker witness, there are three members and majority is 2 of 3.

Agent quorum is the operational authority for layouts 1.3 and 2.0. Corosync ``Quorate`` does not decide Agent quorum and may report ``No`` on a healthy two-node or stretch cluster. See :doc:`building_clusters` and :doc:`troubleshooting`.

Witness Topologies
^^^^^^^^^^^^^^^^^^

A Distributed Worker can provide a quorum-only vote for two supported GFS2 topologies. |morpheus| classifies the witness from Site Group presence, not from Host count. Agent quorum is sent only for layout 1.3 or later clusters that have at least one HPE Shared File System (GFS2) datastore.

.. list-table::
   :header-rows: 1
   :widths: 22 39 39

   * - 
     - Two-node GFS2
     - Stretch
   * - Compute Hosts
     - Two Hosts
     - Minimum 6 Hosts (3 per site); see :doc:`stretch_clusters`
   * - Site Groups
     - None
     - One Site Group per physical site
   * - Witness
     - One Distributed Worker, quorum-only
     - One Distributed Worker in a third location, quorum-only
   * - How |morpheus| classifies the witness
     - No Site Groups present
     - Site Groups present; the worker is assigned as ``siteWitness``
   * - Votes
     - 3 members; majority is 2
     - Site-level arbitration described in :doc:`stretch_clusters`
   * - Quorum panel
     - Witness row; no Sites row; flat Host table
     - Witness row; Sites row; Hosts grouped by site
   * - Activation
     - Layout 1.3 or later and at least one GFS2 datastore
     - Same GFS2 activation; add Site Groups after cluster create

.. warning:: Creating Site Groups on a two-node GFS2 cluster switches the witness classification to stretch ``siteWitness``. Do not add Site Groups to a two-node cluster. Use :doc:`two_node_clusters` for two Hosts with no Site Groups, and :doc:`stretch_clusters` only when Site Groups exist.

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
