Backups
=======

In the |BacBac| section, currently-configured Backups can be viewed and managed, and new Instance, Host and Provider backups be configured. Backups must be tied to a Backup Job, which holds the retention count and the schedule on which the backup should automatically be run. You can create a new Job at the same time as the backup is created or you can create the job ahead of time and associate any new backups to the existing job.

.. NOTE:: Role permissions for Backups determine which backups will be accessible to the individual user.

Create an Instance Backup
-------------------------

To create Instance backup:

#. Navigate to |BacBac|
#. Click :guilabel:`+ ADD`
#. From the Create Backup Wizard select the radio button for Instance, then click :guilabel:`NEXT`
#. Input the following:

   Instance
    Select an Instance to backup from the typeahead menu
   Name
    Enter a name for the backup job being created

#. Click :guilabel:`NEXT`
#. Depending on the Instance Type selected in the previous step, enter additional details. These can include a specific container, backup type, database name, username and password, or a number of other things depending on the Instance Type
#. Configure the storage bucket and retention details:

   Storage
    Select a configured storage bucket as the backup target
   Backup Job Type
    Create a new backup job, add this backup to an existing job, or clone an existing job to handle this backup
   Job Name
    If creating a new job, enter a name for the job
   Retention Count
    If creating a new job, enter the number of backups which should be simultaneously retained
   Schedule
    If creating a new job, select an execution schedule of which to run the backup
   Synthetic Full
    When the backup is targeting an MVM Instance, check this box to schedule synthetic full backups in addition to the normal full and incremental backups
   Synthetic Full Schedule
    If synthetic full backups are enabled, select an execution schedule on which to run the synthetic full backups

#. Click :guilabel:`COMPLETE`.

.. NOTE:: On VMware Cloud types, |morpheus| will merge and consolidate the snapshots held against a VM before exporting the OVF to the storage location or share. This is so |morpheus| has a full and consistent copy of the VM state.

.. TIP:: To edit an existing backup, click on the hyperlinked name of the backup job from the list of backups at |BacBac|.

..
  Create Server Backup
  --------------------

  To create a server backup:

  #. Select the Backups link in the navigation bar.
  #. Select the Backups link in the sub navigation bar.
  #. Click Add Backup.
  #. From the Create Backup Wizard select the radio button Server, then click Next.
  #. Input the following:

     - Name of the backup job being created
     - Server
     - Type of backup you wish to create.

       - File
       - Directory
       - Mongo
       - MySQL
       - Postgres

  #. Click Next. Different options are presented based upon the type of backup being created.

     - File/Directory - input path for the backup.
     - Mongo/MySQL/Postgres - input 'Database IP Address/URL', 'Database Port', 'Database Username', 'Database Password', 'Database Name', and the option to select 'All Databases'.

  #. Click Next.
  #. Schedule the backup Days, Time, Storage Provider & Retention Count.
  #. Click Complete to save.
