Avamar
-------

IMPORTANT: Avamar API must be installed on Avamar server (not installed by default)

Adding Avamar Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Backups > Services`
#. Select :guilabel:`+ ADD`
#. Select Avamar
#. Fill in the following:

   Name
      Name of the Integration in |morpheus|
   Enabled
      Enable the Integration
   Host
      IP or Hostname of the Avamar api server.
   Port
      Port number configured to access the Avamar server
   Username
      Admin Username for Avamar
   Password
      Password for Username provided (encrypted in |morpheus|).
   Tenant
     Avamar Tenant/Domain to scope Integration to
   Hypervisor
     Avamar Hypervisor to scope Integration to
   Visibility
      Sets Multi-Tenant Visibility
        Private
          Only Available to the Tenant the Integration is added by
        Public
          Available to Sub-Tenants (master tenant option only)

#. :guilabel:`SAVE`
