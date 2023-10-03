Backing Up and Restoring |morpheus| Appliance
---------------------------------------------

|morpheus| includes built-in tools for backing up managed Instances as well as the appliance itself. Use this guide to configure a location and schedule for backing up your |morpheus| appliance. This guide also includes steps for restoring or migrating your appliance from the created backup. The steps are the same whether your appliance is deployed in a single node or distributed architecture.

The built-in |morpheus| appliance backup functionality backs up the MySql data. In addition to the database, it's advisable to back up your shared storage (at ``/var/opt/morpheus/morpheus-ui``) and the morpheus.rb configuration file.

.. note:: The destination |morpheus| appliance must be running the same version as that which the backup was taken from.

Create A Backup Job
^^^^^^^^^^^^^^^^^^^

A Backup Job in |morpheus| holds the schedule timing and retention count for automated backups. If you already have a Job configured, you can move on to the next section. By default, |morpheus| includes two execution schedules: Daily at Midnight and Weekly on Sunday at Midnight. If currently-existing options do not make sense for your backup needs, create a new execution schedule:

#. Navigate to |LibAut|
#. Click on the "Execute Scheduling" tab
#. Click :guilabel:`+ ADD`
#. Enter schedule timing using ``cron`` notation
#. Click :guilabel:`SAVE`

With the execution schedule created, we can move on to creating the Backup Job itself. A Backup Job includes both the backup retention count and an execution schedule (which we just created).

#. Navigate to Backups > Jobs
#. Click :guilabel:`+ ADD`
#. Name the Job, then configure the retention count and the schedule
#. Click :guilabel:`SAVE`

Integrate a Bucket or File Share
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When configuring a |morpheus| appliance backup, a storage location is selected. If you already have the destination bucket or file share integrated with |morpheus|, skip to the next section.

#. Navigate to Infrastructure > Storage
#. Click on the Buckets or File Shares tab depending on your chosen storage type
#. Click :guilabel:`+ ADD`
#. Select the appropriate bucket or file share type
#. Complete the required fields and click :guilabel:`SAVE CHANGES`

.. NOTE:: Additional guidance on integrating each of the supported bucket and file share types can be found elsewhere in |morpheus| documentation.

Configuring |morpheus| Appliance Backup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the groundwork laid in the previous sections, we're ready to enable and configure |morpheus| appliance backup.

#. Navigate to |AdmSetBac|
#. Slide the switch labeled "Backup Appliance"
#. Click :guilabel:`SAVE`

On saving this change, a text link labeled "Backup" will be activated which will take you directly to the automatically-generated appliance backup job. Click this link to continue.

#. Click :guilabel:`EDIT`
#. Enter a name for the appliance backup job
#. Select an integrated storage bucket or file share
#. Choose a pre-created backup job. If you do not have an existing backup job that fits, a retention count and schedule can be manually created in this modal. If you manually configure retention counts and schedules in addition to associating a Job, the Job values will override any manual settings.
#. Click :guilabel:`SAVE CHANGES`

At this point, your appliance will be automatically backed up on the schedule you chose and stored in the selected location. An appliance backup will store backup copies of the appliance MySQL database. Should you need to restore or migrate your database from backup, follow the steps in the next section of this guide.

Restoring an Appliance from Backup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Begin by ensuring the Morpheus UI service is stopped on all of the application servers:

.. code-block:: bash

 [root@app-server-new ~] morpheus-ctl stop morpheus-ui

To access the MySQL shell we will need the password for the Morpheus DB user. We can find this in the morpheus-secrets file:

.. code-block:: bash

 [root@app-server-old ~] cat /etc/morpheus/morpheus-secrets.json | grep morpheus_password
 "morpheus_password": "451e122cr5d122asw3de5e1b", <---- this one
 "morpheus_password": "9b5vdj4de5awf87d",

Make note of the first ``morpheus_password`` value as indicated above.

Copy the SQL database backup from the backup bucket or file share to an appliance node at ``/tmp/morpheus_backup.sql``. Then, you can import the MySQL dump into the target database using the embedded MySQL binaries, specifying the database host, and entering the password for the morpheus user when prompted:

.. code-block:: bash

  [root@app-server-new ~] /opt/morpheus/embedded/mysql/bin/mysql -u morpheus -h 127.0.0.1 morpheus -p < /tmp/morpheus_backup.sql
  Enter password:

The data from the old appliance is now replicated on the new appliance. Simply start the UI to complete the process:

.. code-block:: bash

  [root@app-server-new ~] morpheus-ctl start morpheus-ui
