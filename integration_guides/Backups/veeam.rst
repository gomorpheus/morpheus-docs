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
      IP or Hostname of the Veeam server, must be HTTPS for VEEAM 10
   Port
      Port number configured to access the Veeam server, must be 9398 for VEEAM 10
   Username
      Admin Username for Veeam
   Password
      Password for Username provided (encrypted in |morpheus|).
   Visibility
      Sets Multi-Tenant Visibility
        Private
          Only Available to the Tenant the Integration is added by
        Public
          Available to Sub-Tenants (master tenant option only)

#. Click :guilabel:`SAVE`

.. NOTE:: Veeam Backup Enterprise Manager must be installed on the Veeam server in order to successfully integrate Morpheus with Veeam. In addition, |morpheus| does not currently support VEEAM backup job deletion. Jobs must be deleted from VEEAM directly but |morpheus| will disable the job as a best effort measure. This is due to a limitation in the VEEAM API.

.. IMPORTANT:: Once a Veeam Integration has been enabled, a ``VEEAM SERVER`` setting will be available in VMware and Hyper-V cloud settings (``Infrastructure -> Clouds -> Edit a Cloud``). To enable backups on a cloud, a Veeam server must be selected in the ``VEEAM SERVER`` dropdown of the cloud settings and saved. Failure to do so will result in blank ``Backup Repositories`` and ``Backup Job Templates`` options when configuring Veeam Backups during provisioning.
