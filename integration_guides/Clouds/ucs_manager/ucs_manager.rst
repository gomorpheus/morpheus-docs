UCS Manager
-----------

Overview
^^^^^^^^

The |morpheus| UCS Manager Integration enables UCS M B and C Chassis Inventory, VM and Container Host Bare Metal Provisioning, PXE boot with IPMI, Storage Profile, SAN Connection Profile, Server Pool, BIOS Profile, Boot Profile, Maintenance Profile, UUID Pool and Disk Group Profile sync.

Adding UCS Manager Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure -> Clouds``
#. Select :guilabel:`+ ADD`
#. Select **UCS MANAGER** from the Clouds list
#. Populate the following:

   Name
    Name of the Cloud in |morpheus|
   Code
    Cloud Code for variables

   Location
    Description field for adding notes on the cloud, such as location.
   Visibility
     For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
   Tenant
     Select which Tenant to scope visibility to when Visibility is set to Private.
   Enabled
     Unchecking will disable the scheduled cloud-sync job
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
