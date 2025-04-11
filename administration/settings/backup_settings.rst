Backup Settings
^^^^^^^^^^^^^^^

The Backup settings page allows you enable or disable scheduled backups, select a default backup bucket, and administer global settings related to backups. Changes to global settings only affect new backups going forward and do not affect existing backups.

.. NOTE:: Appliance backups are subject to a two-hour time limit to complete the backup. Automated backup attempts will be abandoned and will fail once this time limit is exceeded.

.. IMPORTANT:: Appliances with an HA architecture containing multiple app nodes must ensure all nodes can access stored backups. By default, if no "Default Backup Bucket" configuration is made, backups are stored in ``/var/opt/morpheus/bitcan``. If this path is local to the app nodes, all other app nodes would not be able to reach the backups. In such a case, one solution would be to create an NFS share for the ``bitcan`` directory for all app nodes. Another solution would be to make a "Default Backup Bucket" configuration selection, which all nodes would then use for backup storage and retrieval.

|morpheus| Backup Settings
``````````````````````````

Scheduled Backups
  Enable automatic scheduled backups for provisioned instances

Create Backups
  When enabled, |morpheus| will automatically configure instances for manual or scheduled backups

Backup Appliance
  When enabled, a backup will be created for the |morpheus| appliance database. Select the ``Backup`` text link to view or edit settings related to the appliance backup

Default Backup Bucket
  Select an existing bucket as the default for future backup runs. Click the ``Infrastructure Storage`` text link to add a new storage bucket to |morpheus| if needed

Default Backup Schedule
  Choose a default schedule interval for automated backups. The available selections in this dropdown menu are Execution Schedules defined in |LibAutExe|

Default Backup Retention
  Choose the default number of backups to be retained for automated Instance and appliance backup jobs

Default Synthetic Full Backup enabled
  When enabled, full synthetic backups will be on by default in addition to standard backups for supported workload types

Default Synthetic Full Backup Schedule
  Choose a default schedule interval for full synthetic backups. The available selections in this dropdown menu are Execution Schedules defined in |LibAutExe|
