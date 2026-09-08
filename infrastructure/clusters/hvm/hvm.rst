HVM Clusters
============

HVM clusters provide KVM-based virtualization, centralized lifecycle management, workload placement, shared storage, monitoring, migration, and high availability. This guide covers every supported HVM cluster layout. Use the layout matrix to identify the operating system, networking model, and management tools that apply to a cluster.

.. toctree::
   :hidden:
   :maxdepth: 2

   architecture
   building_clusters
   managing_hosts
   host_maintenance
   virtual_switches
   hvm_networks
   vm_migration
   vm_placement
   host_vm_groups
   vm_compute
   vm_advanced_options
   /infrastructure/clusters/hardware-passthrough
   nvidia_vgpu
   guest_os_notes
   snapshots
   storage_operations
   upgrading
   monitoring
   alarms
   maximums
   capacity_planning
   two_node_clusters
   stretch_clusters
   console_keyboards
   troubleshooting
   failure_scenarios
   /infrastructure/clusters/mvm

Supported Layouts
-----------------

.. list-table::
   :widths: 15 20 25 20 20
   :header-rows: 1

   * - Layout
     - Host operating system
     - High availability
     - Host networking
     - Host management
   * - Legacy (1.2 and earlier)
     - Ubuntu 22.04
     - Pacemaker and Corosync
     - Open vSwitch (OVS)
     - Standard Linux and ``pcs`` commands
   * - 1.3
     - HVM OS/Ubuntu 24.04
     - |morpheus| Agent quorum, Corosync, and DLM
     - Open vSwitch (OVS)
     - Standard Linux commands
   * - 2.0
     - HVM OS 26.04
     - |morpheus| Agent quorum, Corosync, and DLM
     - Virtual Switches (Linux bridge)
     - ``hvmcli`` and standard Linux commands

.. important::

   Layout and HVM OS versions are separate from the |morpheus| Manager version. Confirm the cluster layout on the cluster detail page before following a layout-specific procedure.

How to Use This Guide
---------------------

Unless a section contains a layout notice, it applies to layouts 1.3 and 2.0. Legacy clusters remain supported, but their Pacemaker, Ceph, provisioning, and OVS differences are collected in :doc:`/infrastructure/clusters/mvm` to keep current workflows singular.

- For OVS networking on Legacy and layout 1.3 clusters, see :doc:`hvm_networks`.
- For layout 2.0 networking, see :doc:`virtual_switches`.
- For layout 2.0 host commands, see :doc:`/tools/hvmcli/hvmcli`.
- For NVIDIA SR-IOV vGPU profiles, Host preparation, Service Plans, and guest licensing, see :doc:`nvidia_vgpu`.
- For datastore creation, Datastore Groups, file browsing, maintenance, and capacity operations, see :doc:`storage_operations`.
- For VM snapshots and creating linked clone Virtual Images, see :doc:`snapshots`.
- For moving VMs between hosts or HVM clusters (Actions > Move), see :doc:`vm_migration`.
- For layout and HVM OS upgrades, start at :doc:`/getting_started/maintenance/upgrades/hvm_clusters`, then use :doc:`upgrading` for detailed cluster procedures.
- For two-Host GFS2 clusters that use a Distributed Worker witness and no Site Groups, see :doc:`two_node_clusters`.
- For multi-site stretch clusters that use Site Groups and a ``siteWitness``, see :doc:`stretch_clusters`.
- For the quorum vote model and Quorum panel differences between those topologies, see :doc:`architecture`.
