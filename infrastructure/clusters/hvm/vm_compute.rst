VM Compute Configuration
========================

vCPU Placement
--------------

vCPU Placement is a cluster-level feature that actively manages the physical CPU affinity of virtual machine vCPUs to optimize performance. The |morpheus| Agent periodically evaluates all running VMs on each host and adjusts their vCPU-to-physical-CPU bindings based on the host's NUMA and L3 cache topology.

This feature is especially important for workloads that are sensitive to cross-NUMA memory access latency or L3 cache contention.

Enabling vCPU Placement
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to :menuselection:`Infrastructure --> Clusters` and select the HVM cluster
#. Click :guilabel:`Edit`
#. In the **Options** section, locate the **Dynamic Placement Mode** field
#. Select the desired mode:

   .. list-table::
      :widths: 20 80
      :header-rows: 1

      * - Mode
        - Description
      * - Unmanaged
        - vCPU placement is not managed. The hypervisor's default scheduler handles CPU assignment. This is the default setting.
      * - Region
        - vCPUs for each VM are spread across all physical CPUs within a single NUMA/L3 cache region. This keeps the VM's vCPUs within the same memory locality boundary for optimal performance while allowing the hypervisor flexibility within that region. If a VM is too large to fit within a single region, it switches to pinned mode for that VM.
      * - Pinned
        - Each vCPU is pinned to a specific physical CPU core, chosen based on the least-utilized core available. This provides the most deterministic performance but reduces scheduler flexibility.

#. Click :guilabel:`Save`

How vCPU Placement Works
^^^^^^^^^^^^^^^^^^^^^^^^^

When enabled, the |morpheus| Agent on each host runs a periodic placement cycle:

#. The host's physical CPU topology is read (NUMA nodes, sockets, cores, and L3 cache groups)
#. All running VMs are enumerated and their current vCPU affinities inspected
#. For each VM:

   - If the VM has **guest vNUMA topology defined** (see `vNUMA Provisioning`_ below), vCPUs are pinned to the corresponding host NUMA node's physical CPUs. This takes priority over the cluster placement mode.
   - In **Region** mode: the least-utilized NUMA/L3 region is selected and all of the VM's vCPUs are given affinity to the CPUs in that region
   - In **Pinned** mode (or if the VM's vCPU count exceeds a single region's capacity): each vCPU is individually pinned to the least-utilized physical CPU

Excluded Cores
^^^^^^^^^^^^^^

Cores reserved for host-level functions (such as DPDK or dedicated I/O threads) can be excluded from vCPU placement. Excluded cores are specified in the cluster configuration and the placement manager will never assign VM vCPUs to these cores.

vNUMA Provisioning
------------------

vNUMA (virtual NUMA) exposes the host's NUMA topology to the guest operating system, allowing NUMA-aware workloads inside the VM to optimize their own memory allocation and thread placement. This is critical for "wide" VMs that span multiple physical CPU sockets, such as large database or HPC workloads.

When vNUMA is enabled, the VM's configuration includes a virtual NUMA topology that maps to the host's physical NUMA boundaries. The vCPU Placement Manager then automatically pins each vNUMA cell's vCPUs to the corresponding host NUMA node's physical CPUs.

Configuring vNUMA
^^^^^^^^^^^^^^^^^^

vNUMA is configured per-VM in the **Advanced Options** section during provisioning or reconfigure:

#. Navigate to the VM detail page
#. Click :guilabel:`Actions` > :guilabel:`Reconfigure` (or configure during provisioning)
#. In the **Advanced Options** section, locate the **vNUMA Mode** field
#. Select the desired mode:

   .. list-table::
      :widths: 20 80
      :header-rows: 1

      * - Mode
        - Description
      * - Off
        - No virtual NUMA topology is emitted in the VM configuration. The guest sees a flat CPU/memory layout. This is the default.
      * - Auto
        - |morpheus| automatically calculates the optimal vNUMA topology based on the host's physical NUMA layout and the VM's resource allocation. vNUMA cells are only generated when the VM is large enough to span a NUMA boundary (i.e., its cores or memory exceed what a single NUMA node can provide). If the VM fits within one NUMA node, no vNUMA is emitted.
      * - Manual
        - Uses a previously-synced or explicitly-stored NUMA cell configuration. This is automatically set when |morpheus| discovers an existing VM with vNUMA topology already configured.

#. Save the reconfiguration

.. NOTE:: Changing the vNUMA mode requires the VM to be powered off and its configuration to be regenerated.

How Auto Mode Calculates vNUMA Topology
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Auto mode, the system:

#. Reads the host's physical NUMA topology (number of nodes, CPUs per node, memory per node)
#. Determines whether the VM spans a NUMA boundary by comparing the VM's total cores and memory against a single NUMA node's capacity
#. If the VM fits within one node, no vNUMA cells are generated (flat topology is optimal)
#. If the VM spans nodes, calculates the number of vNUMA cells needed (capped at the host's total NUMA node count)
#. Distributes cores and memory evenly across cells

Synced VMs and Manual Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When |morpheus| discovers existing VMs on a host (brownfield import or inventory sync), it reads any existing vNUMA topology from the VM's configuration. If vNUMA cells are found:

- The vNUMA Mode is automatically set to **Manual**
- The cell configuration is stored and preserved across reconfigure operations
- The vCPU Placement Manager uses this topology to correctly pin vCPUs to the appropriate host NUMA nodes

Integration with vCPU Placement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

vNUMA and vCPU Placement work together:

- When a VM has vNUMA cells defined (Auto or Manual mode), the vCPU Placement Manager pins each cell's vCPUs to the physical CPUs of the corresponding host NUMA node
- This ensures that memory allocated by the guest on a given vNUMA node is physically local to the CPUs handling that workload
- VMs with vNUMA take priority over the cluster-level placement mode — the per-cell pinning is always applied regardless of whether the cluster is set to Region or Pinned
