UCS Manager
-----------

Overview
^^^^^^^^

The |morpheus| UCS Manager Integration enables UCS M B and C Chassis Inventory, VM and Container Host Bare Metal Provisioning, PXE boot with IPMI, Storage Profile, SAN Connection Profile, Server Pool, BIOS Profile, Boot Profile, Maintenance Profile, UUID Pool and Disk Group Profile sync.

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
