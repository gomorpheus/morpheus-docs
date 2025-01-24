Rubrik
-------

The embedded |morpheus| Rubrik Backup integration allows syncing, creation, and management of Rubrik Backups for vCenter Clouds. New Rubrik integrations are created in |BacInt| and, once created, can be set as the backup provider for existing vCenter Clouds. The latest versions of the Rubrik plugin support Rubrik CDM as well as Rubrik RSC (Rubrik Cloud Security). From a |morpheus| standpoint, the primary difference between the two is in how they are authenticated. CDM-based integrations are created with API key authentication whereas RSC-based integrations are created with a client ID and client secret. Once the integration is created, the feature set as used through |morpheus| is identical.

Features
^^^^^^^^

- Backup sync & association
- SLA Domain sync & selection
- Backup creation, deletion & restore
- Restore Backups over existing VMs
- Restore Backups as new Instances

Adding Rubrik Integration
^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: The Rubrik backup service is currently only supported on the VMware Cloud type.

#. Navigate to |BacInt|
#. Select :guilabel:`+ ADD`
#. Select Rubrik
#. Fill in the following:

   **Rubrik CDM Integration**

   Name
      A name for the integration in |morpheus|
   Enabled
      When marked, the integration is enabled for use as a backup provider for compatible Clouds
   Host
      IP or Hostname of the Rubrik API server
   Credentials
      Choose to manually enter authentication credentials and save them to a secure credential store for later use (api key), manually enter and not save them for later use (Local Credentials), or apply a previously-saved API key (select from list of existing credentials)
   API Token
      If manually entering credentials, this field will be visible. Enter the API key
   Visibility
      Sets Multi-Tenant Visibility
        Private
          Only Available to the Tenant the Integration is added by
        Public
          Available to Sub-Tenants (master tenant option only)

   **Rubrik RSC Integration**

   Name
      A name for the integration in |morpheus|
   Enabled
      When marked, the integration is enabled for use as a backup provider for compatible Clouds
   Host
      IP or Hostname of the Rubrik API server. Each Rubrik customer will have a unique host URL (for example: ``https://morpheusdata.my.rubrik.com``)
   Credentials
      Choose to manually enter authentication credentials and save them to a secure credential store for later use (client id and secret), manually enter and not save them for later use (Local Credentials), or apply a previously-saved API key (select from list of existing credentials)
   Client ID
      If manually entering credentials, this field will be visible. Enter the client ID for authentication. If needed, add a service account to obtain credentials (for example: ``https://morpheusdata.my.rubrik.com/service_accounts``). Keep in mind the service account will need to have sufficient privileges to interface with the Rubrik API to execute all |morpheus| functionality listed in the "Features" section above
   Client Secret
      If manually entering credentials, this field will be visible. Enter the client secret for authentication
   Visibility
      Sets Multi-Tenant Visibility
        Private
          Only Available to the Tenant the Integration is added by
        Public
          Available to Sub-Tenants (master tenant option only)

#. Click :guilabel:`SAVE`
