HVM 1.3 Clusters
=================

.. versionadded:: 9.0

The HVM 1.3 cluster layout introduces a new agent-based quorum system for |morpheus| hypervisor clusters. This layout replaces the previous Pacemaker-based high availability stack with the |morpheus| agent's QuorumCheckService, providing simplified cluster management, faster failure detection, and integrated fencing.

HVM 1.3 clusters utilize KVM-based virtualization with Corosync for cluster membership, DLM for distributed lock management, and the |morpheus| agent for quorum decisions, failure detection, and automated recovery.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   architecture
   building_clusters
   managing_hosts
   host_maintenance
   virtual_switches
   vm_migration
   vm_placement
   host_vm_groups
   vm_compute
   vm_advanced_options
   storage_operations
   upgrading
   monitoring
   capacity_planning
   stretch_clusters
   console_keyboards
   troubleshooting
   failure_scenarios
