Veeam
-----

Adding Veeam Integration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Backups -> Services`
#. Select :guilabel:`+ ADD`
#. Select Veeam
#. Fill in the following:

   Name
      Name of the Integration in |morpheus|
   Enabled
      Enable the Veeam integration
   Host
      IP or Hostname of the Veeam server.
   Port
      Port number configured to access the Veeam server
   Username
      Admin Username for Veeam
   Password
      Password for Username provided (encrypted in |morpheus|).
   Visibility
      Sets Multi-Tenant Visibility
        Private
          Only Available to the Tenant the Integration is added by
        Public´‰
          Available to Sub-Tenants (master tenant option only)

#. :guilabel:`SAVE`

.. IMPORTANT:: Once a Veeam Integration has been enabled, a ``VEEAM SERVER`` setting will be available in VMware and Hyper-V cloud settings (``Infrastructure -> Clouds -> Edit a Cloud``). To enabled backups on a Cloud, a Veeam Server must be selected in the ``VEEAM SERVER`` dropdown in the Cloud settings and saved. Failure to do so will result in blank ``Backup Repositories`` and ``Backup Job Templates`` options when configuring Veeam Backups during provisioning´´.
