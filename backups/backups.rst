*******
Backups
*******

The |morpheus| built-in Backup solution provides VM, Container, Host, Database, File, Directory, Volume and Storage Provider Backup, Snapshot and Replication capabilities. Backups can be automatically configured during provisioning or manually created at any time. Backup Jobs with custom Execution Schedules and retention counts can be created and used across all environments in conjunction with configured Storage Providers. Backups can be restored over current Instances or as new Instances, and downloaded or deleted from |morpheus|.

|morpheus| also integrates with external services to automate availability with other providers.

Initial Backups Setup
=====================

Global Backup settings (|AdmSetBac|), Storage Providers (|InfSto|) and Execution Schedules (|LibAutExe|) should be configured prior to creating backups. Global backup settings are where scheduled backups can be globally enabled or disabled and certain global backup default settings can be configured. Storage providers include local and remote configured storage locations that can be used as backup targets. Execution schedules are timed intervals at which individual automated backup jobs will run. See the next two sections for full details on global backup settings and configuring execution schedules. See |morpheus| UI `storage documentation <https://docs.morpheusdata.com/en/latest/infrastructure/storage/storage.html>`_ for more information about configuring local and remote storage targets and/or integrating with third party storage providers.

Global Backups Settings
-----------------------

|morpheus| Backups can be enabled under |AdmSetBac|.

Scheduled Backups
  When enabled, configured Backups will automatically run on their configured schedules. If disabled, backups need to be manually run.
Create Backups
  When enabled, |morpheus| will automatically configure backup jobs for Instances at provision time.
Backup Appliance
  When enabled, a Backup will be created to backup the |morpheus| appliance database. Select the ``Backup`` text link to edit the Appliance Backup Settings and view existing Appliance Backups.
Default Backup Bucket
  From this dropdown, select the default storage bucket to be used for future created Backups. If needed, new storage providers can be configured and managed in the |InfSto| section.
Default Backup Schedule
  From this dropdown, select a default execution schedule for future created Backups. If needed, new schedules can be configured in |LibAutExe|.
Backup Retention Count
  The default maximum number of successful backups to retain.
Default Synthetic Full Backup Enabled
  When enabled, supported workload types will have periodic full synthetic backups scheduled by default in addition to any typical backups (full backup followed by incremental backups) that may also be scheduled.
Default Synthetic Full Backups Schedule
  From this dropdown, select a default execution schedule for future full synthetic backups. In general, this should be at a longer internal than incremental backups that are also scheduled. If needed, new schedules can be configured in |LibAutExe|.

Execution Schedules
-------------------

Backup Execution Schedules can be configured and managed in |LibAutExe|. An execution schedule stores only the interval at which some execution should be run and they can apply to both backups and automation scripts. To create a new backup job with this schedule, navigate to `Backups > Backups` and click "+ADD". In the final step of creating the backup job we are able to select any of our created execution schedules. The Default Backup Schedule set in |AdmSetBac| will be selected when creating a backup job and not specifying an execution schedule.

Configuring Backups during Provisioning
=======================================

When Backups are enabled, Backup options are presented in the AUTOMATION tab of the provisioning wizard. Note that your default backup bucket and default backup schedule will be set according to your global backup settings as mentioned in the previous sections.

.. NOTE:: The Backup options presented in the Automation tab can be disabled using a "Create Backup" Policy. See :doc:`../administration/policies/policies`

BACKUP TYPE
  Select the type for the Backup. Backup Types displayed will be filtered by available options for the selected Instance Layout
BACKUP NAME
  Defaults to the Instance name
BACKUP TARGET
  Select the Storage Provider target for the Backup (when applicable)
BACKUP JOB TYPE
  Create a new job, clone an existing job, or Add to existing job
JOB NAME
  Defaults to the Instance name
RETENTION COUNT
  Maximum number of successful backups to retain
BACKUP SCHEDULE
  Select the schedule for the backup job from the list of existing execution schedules
SYNTHETIC FULL (Currently only available for KVM VM Snapshot-type backups, such as those used with HPE VM Instances. More Layout types are expected to support synthetic full backups in the future)
  When checked, an additional schedule is configured for the backup job during which a synthetic full backup will be taken. In general, this should be on a longer time period than that at which standard backups (full backup followed by incremental backups) are configured
SYNTHETIC FULL SCHEDULE
  Select the schedule for the backup job on which synthetic full backups should be taken

Backup Types displayed will be filtered by available options per selected Instance Layout.

.. rst-class:: hidden
  * File Backup
  * Directory Backup
  * MySQL
  * MongoDB
  * LVM Snapshot
  * LVM Image
  * LVM Migration
  * Windows Migration
  * Postgres
  * Tar Directory Backup
  * Amazon VM Snapshot
  * VMWare VM Snapshot
  * Fusion VM Snapshot
  * Xen VM Snapshot
  * Veeam VMWare VM Backup
  * Veeam Hyper-V VM Backup
  * Google VM Snapshot
  * Commvault File/Directory Backup
  * Azure VM Snapshot
  * Morpheus Appliance
  * Openstack VM Snapshot
  * DigitalOcean VM Snapshot
  * Nutanix VM Snapshot
  * Softlayer VM Snapshot
  * Hyper-V VM Snapshot
  * VMWare VM Snapshot
  * SCVMM VM Snapshot
  * UpCloud VM Snapshot
  * Bluemix VM Snapshot
  * Alibaba VM Snapshot
  * Oracle Cloud VM Snapshot
  * KVM VM Snapshot
  * Container Backup
  * VM Backup
  * Object Storage Backup


.. include:: summary.rst
.. include:: backups_sub.rst
