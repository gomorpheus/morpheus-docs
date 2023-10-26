*******
Backups
*******

|morpheus| built-in Backup solution provides VM, Container, Host, Database, File, Directory, Volume and Storage Provider Backup, Snapshot and Replication capabilities. Backups can be automatically configured during provisioning or manually created at any time. Backup Jobs with custom Execution Schedules and retention counts can be created and used across all environments in conjunction with configured Storage Providers. Backups can be  restored over current Instances or as new Instances, and downloaded or deleted from |morpheus|.

|morpheus| also integrates with external services to automate availability with other providers.

Initial Backups Setup
=====================

Global Backup settings, Storage Providers and Execution Schedules should be configured prior to creating backups.

Global Backups Settings
-----------------------

|morpheus| Backups can be enabled under |AdmSetBac|.

Scheduled Backups
  When enabled, configured Backups will automatically run on the set Schedule. If disabled, backups need to be manually ran.
Create Backups
  When enabled, |morpheus| will automatically configure backup jobs for Instances.
Backup Appliance
  When enabled, a Backup will be created to backup the |morpheus| appliance database. Select the ``Backup`` text link to edit Appliance Backup Settings and view existing Appliance Backups.
Default Backup Storage Provider
  Storage Providers can be configured and managed in the `Infrastructure > Storage` section.
Default Backup Schedule
  Schedules can be configured and managed in the |LibAutPow|
Backup Retention Count
  Default maximum number of successful backups to retain.

Backup Schedules
----------------

Backup Execution Schedules can be configured and managed in |LibAutExe|. An execution schedule stores only the interval at which some execution should be run. To create a new backup job with this schedule, navigate to `Backups > Backups` and click "+ADD". In the final step of creating the backup job we are able to select any of our created execution schedules. The Default Backup Schedule set in |AdmSetBac| will be selected when creating a backup job and not specifying an execution schedule.


Configuring Backups during Provisioning
=======================================

When Backups are enabled, Backup options are presenting in the Automation tab of the Provisioning wizard.

.. NOTE:: The Backup options presented in the Automation tab can be disabled using a "Create Backup" policy. See :doc:`../administration/policies/policies`

BACKUP TYPE
  Select the type for the Backup. Backup Types displayed will be filtered by available options per selected Instance Layout.
BACKUP NAME
  Defaults to Instance name
BACKUP TARGET
  Select Storage Provider target for the Backup (when applicable).
BACKUP JOB TYPE
  Create New, Clone, or Add to existing Job
JOB Name
  Defaults to Instance name
RETENTION COUNT
  Maximum number of successful backups to retain.
BACKUP SCHEDULE
  Select the schedule the Backup Job will be executed.

Backup Types displayed will be filtered by available options per selected Instance Layout. Backup Job Types include:

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
.. include:: managing_backups.rst
