Veeam
-----

Veeam is a backup and replication platform designed to work with popular on-prem cloud providers, including VMware, Microsoft Hyper-V, and vCloud Director. |morpheus| integrates with your existing Veeam appliance which can then be set as the preferred backup solution for any existing Clouds. From there, easily schedule backup routines during Instance provisioning and restore Instances when needed. This section discusses the process for integrating Veeam with |morpheus|, sharing a Veeam integration with multiple Tenants, setting backup during Instance provisioning, and restoring Instances from Veeam backup.

Features
^^^^^^^^

- Share one backup provider across multiple Tenants
- Apply Veeam integration as the default backup target for compatible clouds
- Select Veeam integrations as backup provider at Instance provision time
- Automate backups with |morpheus| Backup Jobs
- When needed, easily restore Instance backups

Adding Veeam Integration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Backups > Integrations`
#. Select :guilabel:`+ ADD`
#. Select Veeam
#. Fill in the following:

   Name
      Friendly name for the integration in |morpheus|
   Enabled
      When marked, this integration will be active and available for use
   API URL
      IP or Hostname of the Veeam Enterprise Manager, must be HTTPS for VEEAM 10
   Port
      Port number configured to access the Veeam server, must be 9398 for VEEAM 10
   Username
      Username for an admin service account in Veeam
   Password
      Password for Username provided (encrypted in |morpheus|)
   Visibility
      Sets Multi-Tenant Visibility
        Private
          Only available to the Tenant that added the integration
        Public
          Available to Subtenants (primary tenant option only)

#. Click :guilabel:`SAVE`

.. NOTE:: Veeam Backup Enterprise Manager must be installed in order to successfully integrate |morpheus| with Veeam.

.. IMPORTANT:: Once Veeam service has been integrated with |morpheus|, Veeam server(s) will be available to select as the backup provider for VMware, Hyper-V, and vCloud Director cloud integrations (Infrastructure > Clouds > Edit a compatible Cloud). To enable Veeam backups, select the appropriate Veeam server as the "backup provider" for your cloud integrations as needed. Failure to do so will result in blank ``Backup Repositories`` and ``Backup Job Templates`` options when configuring Veeam Backups during provisioning.

Set Veeam as Cloud Backup Target
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the initial integration is made, set this integration as the backup provider for as many supported Clouds as needed. Veeam integrations are supported as backup target for VMware, Hyper-V, and vCloud Director Clouds at this time.

#. Navigate to Infrastructure > Clouds
#. Select an existing VMware, Hyper-V, or vCD Cloud
#. Click :guilabel:`EDIT`
#. Expand the Advanced Options section
#. Under "Backup Provider", select the relevant Veeam integration
#. Click :guilabel:`SAVE CHANGES`

.. image:: /images/integration_guides/veeam/1setProvider.png

Configure Backup at Provision Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When provisioning an Instance into a Cloud where Veeam is set as the backup provider, Veeam will be selectable as the "Backup Type" on the Automation tab of the provisioning wizard. Expand the Backups section on this tab and enter the following:

- **Backup Type:** Select the desired Veeam backup type
- **Repository:** Select a repository synced from the Veeam backup provider associated with the Cloud
- **Managed Server:** Select a managed server associated with the backup server selected in the previous step
- **Backup Name:** A name for the backup in Morpheus, this field is pre-populated with the Instance name but can be overwritten
- **Backup Job Type:** Clone an existing backup job (Backups > Jobs) or add this backup to an existing job. A job contains a retention count and backup frequency schedule and can have as many Instances backing up under it as needed
- **Backup Job:** Select the job which will be cloned or have a backup added to it depending on your selection in the prior field
- **Job Name:** A name for the new cloned job (if you are cloning and not creating a new Backup Job)

.. image:: /images/integration_guides/veeam/2createBackup.png

Viewing Backups
^^^^^^^^^^^^^^^

After provisioning, users can review backup details from the Instance detail page (|ProIns| > Selected Instance > Backups tab). Additionally, backups can be configured here if this was not done during provision time by clicking :guilabel:`ADD BACKUP`. Users can also run one-off backups from this page by opening the ACTIONS menu and clicking Backup. Backups will still continue to run based on the schedule configured in their job but additional runs can be made on-demand this way.

Within the Backups section (Backups > Backups) users can also view all currently-configured backups and whether or not recent backup runs have succeeded.

.. image:: /images/integration_guides/veeam/3viewBackups.png

Restore an Instance from Veeam
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For Instances with current backups, the Backup Results section will be populated on the Instance detail page (|ProIns| > Selected Instance > Backup tab). If the Instance needs restored, simply click Actions (within the Backup Results area, not the main actions menu for the Instance itself) and then click Restore. The status icon at the top of the Instance detail page will turn green once this process is finished and the Instance will be fully restored from your selected backup.
