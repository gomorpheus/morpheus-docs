Backing Up and Restoring |morpheus| Appliance
---------------------------------------------

|morpheus| includes built-in tools for backing up managed Instances as well as the appliance itself. Use this guide to configure a location and schedule for backing up your |morpheus| appliance. This guide also includes steps for restoring or migrating your appliance from the created backup. The steps are the same whether your appliance is deployed in a single node or distributed architecture.

The built-in |morpheus| appliance backup functionality backs up the MySQL data. It is not a complete Manager recovery set.

.. _vme-manager-recovery-set:

For Manager recovery, keep the following together and outside the Manager VM and its HVM host:

- A recently verified appliance database backup
- A filesystem-level backup of ``/var/opt/morpheus/morpheus-ui``, including ownership and permissions
- Protected copies of ``/etc/morpheus/morpheus.rb``, ``/etc/morpheus/morpheus-secrets.json``, certificates, and the deployment record (appliance version, hostname, IP, DNS, gateway, and storage mappings)

Protect the secrets file as credential material. Test recovery on the same appliance version and document the recovery point and recovery time achieved by the test.

.. note:: The destination |morpheus| appliance must be running the same version as that which the backup was taken from.

Create A Backup Job
^^^^^^^^^^^^^^^^^^^

A Backup Job in |morpheus| holds the schedule timing and retention count for automated backups. If you already have a Job configured, you can move on to the next section. By default, |morpheus| includes two execution schedules: Daily at Midnight and Weekly on Sunday at Midnight. If currently-existing options do not make sense for your backup needs, create a new execution schedule:

#. Navigate to :menuselection:`Library --> Automation`
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

.. _vme-manager-host-recovery:

VME Manager host-failure decision tree
``````````````````````````````````````

First isolate the failed HVM host so that it cannot run another copy of the Manager VM. Starting two copies with the same identity or disks can corrupt data and disrupt integrations. Then select the recovery path:

#. **The Manager VM and all of its disks are intact on storage accessible to another healthy host:** use the supported HVM VM registration, migration, or recovery workflow for the applicable cluster layout. This relocates the complete VM; it is not an appliance database restore. Preserve the VM identity, MAC addresses, and storage attachments. Start only one copy and validate it using the checklist below.
#. **The VM is unavailable, but the complete recovery set survives:** deploy a replacement Manager at the **same version as the backup**, preserve or deliberately update its DNS/IP identity, and contact HPE Support for the topology-specific database and appliance-file restore sequence. Do not attach the old and replacement Manager to production simultaneously.
#. **Only a database backup survives:** stop. A database backup does not contain all files, configuration, secrets, certificates, or uploaded assets needed to reproduce the appliance. Contact HPE Support to determine what can be recovered and which integrations and credentials must be rebuilt.
#. **No viable VM or recovery set survives:** deploy a new Manager and re-onboard resources under an HPE Support recovery plan. Do not copy database tables, edit appliance identity directly, or reuse unknown disks in an attempt to reconstruct the failed appliance.

Before any recovery, record the failed host and storage state, fence or power off the original host, protect surviving disks from writes, and take snapshots or storage-level copies where supported. Stop and contact HPE Support if host isolation is uncertain, a disk is inconsistent, the replacement version differs, the database topology is unknown, or DNS/certificate/identity changes are required.

After starting the recovered Manager, verify the appliance URL and certificate, administrator login, service health, database connectivity, UI assets and uploaded images, HVM cluster/host connectivity, inventory refresh, console access, integrations, automation credentials, and the next appliance backup. Do not discard the failed VM or recovery artifacts until this validation and an agreed rollback period are complete.

Begin by ensuring the Morpheus UI service is stopped on all of the application servers:

.. code-block:: bash

 [root@app-server-new ~] morpheus-ctl stop morpheus-ui

For an embedded database using the default generated credentials, retrieve the exact MySQL application-user key without printing unrelated secrets:

.. code-block:: bash

 [root@app-server-old ~] jq -r '.mysql.morpheus_password' /etc/morpheus/morpheus-secrets.json

For an external database or a customized database name, host, user, or password, use the effective ``mysql`` configuration in ``/etc/morpheus/morpheus.rb`` instead. Values in ``morpheus-secrets.json`` describe generated embedded-service secrets and must not be assumed to describe an external service.

Copy the SQL database backup from the backup bucket or file share to a secured location on an appliance node. The previously documented direct ``mysql`` restore command is not a supported general restore procedure: appliance dumps can contain database-level statements, and the correct connection target, privileges, schema name, topology sequence, and validation depend on the deployment. Contact HPE Support for the restore command and recovery plan for the source and target appliance versions and database topology. Do not start the UI until Support's restore validation is complete.

When the validated restore is complete, start the UI on each application server as directed by the recovery plan:

.. code-block:: bash

  [root@app-server-new ~] morpheus-ctl start morpheus-ui
