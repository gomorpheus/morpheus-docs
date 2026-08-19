VMware Administrator Task Map for VM Essentials
================================================

This guide maps a practical core set of familiar VMware administration tasks to their HPE Morpheus VM Essentials workflows. It is a task map, not a feature-parity statement: vCenter inventory objects and |morpheus| Instances, Groups, Service Plans, and HVM cluster objects have different lifecycles and permission models. See :doc:`/provisioning/concepts/concepts` before converting existing workloads.

.. list-table:: Common brownfield tasks
   :header-rows: 1
   :widths: 22 24 22 32

   * - VMware intent
     - VM Essentials concept and navigation
     - Check first
     - Canonical procedure
   * - Add existing virtualization inventory
     - Add a VMware Cloud at :menuselection:`Infrastructure --> Clouds`; enable existing-Instance inventory when required
     - vCenter API URL, service account permissions, scope, and appliance-to-vCenter/ESXi connectivity
     - :doc:`/integration_guides/Clouds/vmware/vmware`
   * - Adopt an existing VM
     - Convert a discovered Virtual Machine to a managed Instance
     - The target Tenant, Group, Instance Type, Layout, operating system, credentials, and matching Plan
     - :doc:`/provisioning/instances/creating_instances`
   * - Deploy a VM from a template
     - Provision an Instance from an Instance Type/Layout and Virtual Image
     - Group/Cloud access, image preparation, network, datastore, and Service Plan
     - :doc:`/provisioning/instances/creating_instances`
   * - Control VM size
     - Select or create a Service Plan
     - Provision type, active state, CPU, memory, storage, and any cluster permission filter
     - :doc:`/administration/plans_pricing/plans`
   * - Control placement access
     - Scope Clouds, resource pools, datastores, networks, or HVM clusters to Groups
     - User role plus Group and resource permission intersections
     - :doc:`/getting_started/guides/groups_roles_perms`
   * - Connect VM networking
     - Select a provisionable Network; HVM layout 2.0 uses Virtual Switches beneath Networks
     - VLAN, MTU, upstream switch configuration, IP pool, and target-cluster access
     - :doc:`/infrastructure/networks/networks` and :doc:`/infrastructure/clusters/hvm/virtual_switches`
   * - Take or restore a snapshot
     - Use Instance or VM snapshot actions supported by the target provider
     - Provider support, datastore capacity, application consistency, and backup policy
     - :doc:`/provisioning/instances/managing_instances`
   * - Resize a VM
     - Reconfigure the Instance or VM and select an allowed Plan or supported custom values
     - Provider hot-add support, guest support, permissions, and required restart
     - :doc:`/provisioning/instances/managing_instances`
   * - Open a VM console
     - Open the console from the Instance or Virtual Machine detail page
     - Browser connectivity and the provider-specific console path
     - :doc:`/provisioning/instances/instance_details`
   * - Move a workload
     - Use a provider-supported migration action; migration is not equivalent to changing an Instance Group
     - Source/target compatibility, storage, networking, snapshots, and downtime requirements
     - :doc:`/infrastructure/servers/server_migration`
   * - Back up a workload
     - Configure a Backup integration and Backup Job rather than treating snapshots as backups
     - Provider/integration support, credentials, retention, and restore testing
     - :doc:`/backups/backups`

When no action appears, check the user's role, Group access, target resource permissions, and provider capabilities before assuming VM Essentials lacks an equivalent task.
