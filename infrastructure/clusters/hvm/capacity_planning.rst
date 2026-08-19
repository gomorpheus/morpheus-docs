Capacity Planning
=================

Proper capacity planning ensures an HVM cluster can handle workloads while maintaining the ability to tolerate host failures and perform maintenance operations.

Memory Math
-----------

Understanding how memory is allocated in an HVM cluster:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Component
     - Calculation
   * - Total physical memory
     - Installed RAM on the host
   * - System overhead (reserved)
     - 4 GB per host (reserved for OS, Corosync, DLM, agent, libvirt)
   * - Available for VMs
     - Total physical memory − 4 GB
   * - Computed max memory
     - Available memory reported by |morpheus| for VM placement

**Example:** A host with 128 GB RAM has ``128 − 4 = 124 GB`` available for VMs.

.. NOTE:: The 4 GB system reservation is set during host provisioning and accounts for the base operating system, cluster services (Corosync, DLM), the |morpheus| agent, libvirt overhead, and kernel buffers.

Memory Utilization Calculation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|morpheus| tracks memory at two levels:

- **Reserved memory** — Sum of all VM memory allocations on a host (what VMs *could* use at maximum)
- **Used memory** — Actual memory consumption reported by the host

The capacity system uses ``computedMaxMemory`` (total − reserved system overhead) as the denominator for utilization calculations.

Failover Capacity: N+1 Sizing
-------------------------------

N+1 sizing means that if any single host fails, the remaining hosts must have enough available memory to absorb all VMs from the failed host.

Formula
^^^^^^^

.. code-block:: text

   Required memory per host = Total VM memory / (N - 1)
   Available per host must exceed = Largest single host's VM load

Where N is the total number of hosts.

Sizing Examples
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 15 20 20 20 25
   :header-rows: 1

   * - Hosts
     - RAM Each
     - Available Each
     - Total Available
     - Usable with N+1
   * - 3
     - 128 GB
     - 124 GB
     - 372 GB
     - 248 GB (2 hosts worth)
   * - 5
     - 128 GB
     - 124 GB
     - 620 GB
     - 496 GB (4 hosts worth)
   * - 3
     - 256 GB
     - 252 GB
     - 756 GB
     - 504 GB (2 hosts worth)
   * - 5
     - 256 GB
     - 252 GB
     - 1260 GB
     - 1008 GB (4 hosts worth)

.. IMPORTANT:: With N+1 sizing, you should never allocate more than ``(N-1)/N`` of total cluster memory to VMs. For a 3-node cluster, this means keeping 33% of total capacity free. For a 5-node cluster, 20%.

Maintenance Capacity
^^^^^^^^^^^^^^^^^^^^^

Maintenance mode requires the same capacity headroom as failover — one host worth of memory must be available across remaining hosts to evacuate VMs during maintenance.

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Cluster Size
     - Max Usable Memory (N+1)
     - Reason
   * - 3 hosts
     - 66% of total available
     - 1 host's VMs must fit on remaining 2
   * - 4 hosts
     - 75% of total available
     - 1 host's VMs must fit on remaining 3
   * - 5 hosts
     - 80% of total available
     - 1 host's VMs must fit on remaining 4

.. NOTE:: |morpheus| enforces a 95% utilization cap on any single host during maintenance evacuation. Even if the cluster has aggregate capacity, no individual host will be loaded beyond 95%.

When to Add Hosts
------------------

Consider adding hosts to the cluster when:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Trigger
     - Description
   * - Memory utilization > 70% cluster-wide
     - Approaching the point where N+1 failover is at risk
   * - Cannot enter maintenance mode
     - Insufficient capacity to evacuate VMs indicates the cluster is too full
   * - Single host > 85% utilization
     - That host's VMs would overload remaining hosts on failure
   * - New workload requirements
     - Planned VM deployments would exceed available capacity
   * - Failover testing fails
     - Testing shows VMs cannot be redistributed after a simulated failure

.. WARNING:: Do not wait until the cluster is at capacity to add hosts. Adding hosts requires network connectivity and provisioning time. Plan ahead based on growth trends.

CPU Overcommit Considerations
------------------------------

Unlike memory, CPU can be safely overcommitted in most workloads:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Ratio
     - Use Case
   * - 1:1
     - Latency-sensitive workloads, real-time applications
   * - 2:1
     - General purpose workloads, typical enterprise applications
   * - 4:1
     - Development/test environments, low-utilization workloads
   * - 8:1+
     - Idle or bursty workloads (use with caution)

**Key differences from memory:**

- CPU overcommit does not risk data corruption (unlike memory overcommit)
- Over-committed CPUs result in increased scheduling latency, not failures
- Memory is a hard limit — if a VM's memory is overcommitted and fully utilized, the host may become unstable

.. NOTE:: |morpheus| does not overcommit memory by default. VM memory allocations are treated as reservations. Memory overcommit can be enabled per host — see :doc:`vm_placement` for details. CPU scheduling is managed by the Linux kernel's CFS scheduler with KVM's virtual CPU mappings.

Storage Capacity Planning
--------------------------

Plan storage capacity considering:

- **VM disk allocation** — Current storage usage plus growth projections
- **Heartbeat overhead** — Heartbeat files consume minimal space (~KB per host per datastore)
- **Snapshot space** — VM snapshots can consume significant temporary space
- **GFS2 journal overhead** — Each host requires a journal entry per datastore (typically 128 MB per journal)

Recommended free space threshold: **> 20%** on all HPE Clustered Datastores.

Prefer adding another datastore before an existing datastore reaches the threshold. If operational constraints require an in-place LUN/GFS2 increase, use the single canonical, Support-gated procedure in :doc:`storage_operations`; do not treat array expansion alone as filesystem growth.

For multiple shared file-based datastores, an HVM Datastore Group can select a member during provisioning and optionally rebalance eligible VM disks when a member exceeds the configured utilization threshold. See :doc:`storage_operations`.

Capacity Monitoring in |morpheus|
-----------------------------------

Track cluster capacity from the |morpheus| UI:

- **Cluster Summary:** ``Infrastructure > Clusters > [Cluster] > Summary`` shows aggregate memory, CPU, and storage utilization
- **Host Detail:** Individual host pages show per-host memory and CPU utilization
- **Datastore Detail:** ``Storage > Datastores > [Datastore]`` shows capacity and free space

Sizing Decision Matrix
-----------------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Requirement
     - Minimum
     - Recommendation
   * - Production HA
     - 3 hosts
     - 5 hosts (tolerates 2 failures)
   * - Memory per host
     - 32 GB
     - 128+ GB for meaningful VM density
   * - Failover capacity
     - N+1
     - N+1 with maintenance headroom
   * - Datastores
     - 1 shared
     - 2+ (heartbeat redundancy)
   * - Network
     - 1 path
     - Bonded/redundant network paths
