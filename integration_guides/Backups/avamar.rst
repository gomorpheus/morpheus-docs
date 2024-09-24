Avamar
-------

|morpheus| integrates with an existing Avamar appliance which can then be set as the preferred backup solution for any compatible Clouds. From there, easily schedule backup routines during Instance provisioning and restore Instances when needed. This section discusses the process for integrating Avamar with Morpheus. Once the integration is complete, when editing or adding compatible Clouds, set the Avamar integration as the backup provider for the Cloud. At provision time, set Avamar backup configurations for the workload. When necessary, restore Instances from Avamar backup.

.. IMPORTANT:: Avamar API must be installed on Avamar server (not installed by default)

Features
^^^^^^^^

- Share one backup provider across multiple Tenants
- Apply Avamar integration as the default backup target for compatible Clouds
- Select Avamar integrations as backup provider at Instance provision time
- Automate backups with |morpheus| Backup Jobs
- When needed, easily restore Instance backups

Adding Avamar Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |BacInt|
#. Select :guilabel:`+ ADD`
#. Select Avamar
#. Fill in the following:

   Name
      Name for the Avamar integration in |morpheus|
   Enabled
      When checked, the integration is selectable as a backup provider for compatible Clouds
   Host
      IP or Hostname of the Avamar API server
   Port
      Port number configured to access the Avamar server
   Username
      Admin username for Avamar
   Password
      Password for the user provided. Choose to enter credentials locally or use a securely-stored credential set saved previously
   Tenant
     Avamar Tenant/Domain scoping for the integration
   Hypervisor
     Avamar Hypervisor scoping for the integration
   Visibility
      Sets Multi-Tenant Visibility
        Private
          Only available to the Tenant that adds the integration
        Public
          Available to Subtenants (|mastertenant| option only)

#. Click :guilabel:`SAVE`
