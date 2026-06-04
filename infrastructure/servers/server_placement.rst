Server Placement
----------------

Overview
^^^^^^^^

Server Placement in |morpheus| controls which host, cluster, or resource pool a virtual machine is assigned to within a cloud. Placement configuration can be set during provisioning or updated post-provisioning to optimize resource utilization across the infrastructure.

Placement settings work in conjunction with cloud resource pool configurations and can be influenced by Host-VM Groups (affinity and anti-affinity rules).

Configuring Placement
^^^^^^^^^^^^^^^^^^^^^

During Provisioning
```````````````````

When provisioning a new instance, placement is configured in the **Configure** step:

CLOUD
  The target cloud determines available placement options.
RESOURCE POOL
  Select a resource pool or cluster. This defines the boundary within which the VM will be placed.
HOST
  (Optional) When manual host selection is enabled, a specific host can be chosen. If left as auto-select, |morpheus| or the hypervisor will determine optimal placement.

Updating Placement Post-Provisioning
`````````````````````````````````````

To change a server's placement after provisioning:

#. Navigate to the server detail page
#. Click :guilabel:`ACTIONS`
#. Select **Change Cloud** or **Placement**
#. Update the placement configuration:

   CLOUD
     The target cloud (for cross-cloud placement changes).
   RESOURCE POOL
     The destination resource pool or cluster.

#. Click :guilabel:`SAVE`

.. NOTE:: Changing placement may trigger a migration operation depending on the hypervisor. See :doc:`server_migration` for details on VM migration.

Automatic Placement
^^^^^^^^^^^^^^^^^^^

When no specific host is selected, |morpheus| works with the underlying hypervisor's placement engine:

- **VMware DRS** — When DRS is enabled, VMware handles optimal host placement within a cluster.
- **Nutanix ADS** — Acropolis Dynamic Scheduling distributes VMs across hosts.
- **KVM/MVM** — |morpheus| selects the host with the most available resources in the target pool.

Host-VM Group Integration
^^^^^^^^^^^^^^^^^^^^^^^^^

Server placement can be further controlled through Host-VM Groups, which define affinity and anti-affinity rules. See :doc:`/infrastructure/clusters/host_vm_groups` for details on configuring these rules.
