UCS Manager
-----------

Overview
^^^^^^^^

The |morpheus| UCS Manager Integration enables UCS M B and C Chassis Inventory, VM and Container Host Bare Metal Provisioning, PXE boot with IPMI, Storage Profile, SAN Connection Profile, Server Pool, BIOS Profile, Boot Profile, Maintenance Profile, UUID Pool and Disk Group Profile sync.

This integration automates the UCS capabilities described below; it is not a general UCS administration interface. Create and validate the required organizations, pools, policies, network paths, and installation sources in UCS Manager before relying on them from |morpheus|. The exact UCS privileges are determined by those objects and the organization's UCS security policy; use a dedicated account with sufficient read access for inventory and write access for Service Profile provisioning rather than assuming a built-in |morpheus| role.

Features
^^^^^^^^

- Validate and onboard a UCS Manager endpoint using an existing UCS organization or a new organization created for |morpheus|
- Synchronize organizations, chassis, blades, cartridges, cartridge servers, networks, boot and BIOS policies, maintenance policies, UUID pools, SAN connection policies, disk group policies, storage profiles, and server pools
- Provision bare-metal hosts with UCS Service Profiles and PXE boot mappings
- Onboard inventoried UCS servers for management and return managed servers to unmanaged inventory
- Import UCS faults as |morpheus| operation notifications associated with the matching zone, chassis, or server when a match is available
- Calculate UCS usage with the system **Custom UCS Price Set**, which contains memory, CPU, core, and storage component prices

Adding UCS Manager Cloud
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clouds``
#. Select :guilabel:`+ ADD`
#. Select **UCS MANAGER** from the Clouds list
#. Populate the following:

   .. include:: /integration_guides/Clouds/base_options.rst

   **Details**

    
   UCS MANAGER
      IP or hostname of UCS Manager
   USERNAME
      UCS Manager User
   PASSWORD
      UCS Manager Password
   ORGANIZATION
      * EXISTING (select)
      * NEW (create)
         * ORG NAME
            Enter name for the new Organization
   SERVER PREFIX
      String provisioned servers will be prefixed with
   DATA DISK MODE
      * LVM data disk
      * Single Disk
   DATA VOLUME
      Defaults to ``/dev/sdb``
      * Check to enable SOFTWARE RAID
   NET INTERFACE
      Defaults to eth0

#. Select :guilabel:`NEXT`
#. Select an existing or create a new Group to add the Cloud to. The Cloud can be added to additional Groups in a Groups `Clouds` tab.
#. Select :guilabel:`NEXT`
#. Review and then Select :guilabel:`COMPLETE`

After creation, |morpheus| tests connectivity and credentials. A successful refresh sets the Cloud status to OK and synchronizes the inventory listed above. Invalid credentials set an error status; an unreachable endpoint sets the Cloud offline. Use the Cloud refresh action after changing inventory in UCS Manager.

Bare-metal Provisioning and Lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Provisioning selects an available synchronized UCS server, creates or reuses a Service Profile template, creates PXE boot mappings for the selected image, and creates the UCS Service Profile. Before provisioning, confirm the selected organization, server pool, policies, MAC/UUID pools, PXE image, network path, and Kickstart source are available to the target server. A failure to create the Service Profile marks the server failed; review the provisioning process before retrying.

Synchronized unmanaged servers can be selected for |morpheus| management. Returning a managed UCS server to unmanaged inventory removes it from its |morpheus|-managed server pool, clears managed network addressing, and restores its UCS server inventory type. Confirm that no workload depends on the server before removing it from management.

Faults and Costing
^^^^^^^^^^^^^^^^^^

Each Cloud refresh imports active UCS faults into |morpheus| notifications, maps UCS severity and acknowledgement state, and associates a fault with a matching server or chassis when possible. Faults no longer returned by UCS are marked inactive. See :doc:`/operations/alarms` for notification and alarm handling.

UCS Clouds use the **Custom UCS Price Set** and its memory, CPU, core, and storage component prices. Configure component prices using the pricing guidance in :doc:`/administration/plans_pricing/prices` before relying on cost totals.

The integration does not replace UCS Manager for object creation outside the provisioning operations described here, UCS fault remediation, or Cisco-side recovery. If a refresh or Service Profile operation fails, preserve the failed process and UCS fault details and reconcile the UCS object state before retrying.
