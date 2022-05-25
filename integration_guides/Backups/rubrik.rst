Rubrik
-------

The embedded |morpheus| Rubrik Backup integraiton allow syncing, creation and managemnet of Rubrik Backups for vCenter clouds. 

Features
^^^^^^^^

- Backup sync & associaiton
- Sla Domain sync & selection
- Backup creation, deletion & restore 
- Restore Backups over existing vm's
- Restore Backup as new

Adding Rubrik Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: The Rubrik backup service is currently only supported on the VMware cloud type.

#. Navigate to `Backups > Services`
#. Select :guilabel:`+ ADD`
#. Select Rubrik
#. Fill in the following:

   Name
      Name of the Integration in |morpheus|
   Enabled
      Enable the Integration
   Host
      IP or Hostname of the Rubrik api server.
   Username
      Admin Username for Rubrik
   Password
      Password for Username provided (encrypted in |morpheus|).
   Visibility
      Sets Multi-Tenant Visibility
        Private
          Only Available to the Tenant the Integration is added by
        Public
          Available to Sub-Tenants (master tenant option only)

#. :guilabel:`SAVE`


