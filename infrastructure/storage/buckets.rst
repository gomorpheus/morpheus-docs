Storage Buckets
---------------

Storage Buckets are for Backup, Archives, Deployment and Virtual Images storage targets. Buckets can be browsed and files and folders can be uploaded, downloaded or deleted from the Bucket section. Retention Policies can be set on Storage Buckets for files to be deleted or backed up to another bucket after a set amount of time.

Supported Bucket Types
^^^^^^^^^^^^^^^^^^^^^^

- Alibaba
- Amazon S3
- Azure
- Openstack Swift
- Rackspace CDN

Alibaba Buckets
^^^^^^^^^^^^^^^

To Add an Alibaba Storage Bucket:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the BUCKETS tab, Click the :guilabel:`+ ADD` button.
#. Select `Alibaba` from the dropdown list
#. From the NEW BUCKET Wizard input the following:

   NAME
     Name of the Bucket in |morpheus|.
   ACCESS KEY
    Alibaba Access Key
   SECRET KEY
    Alibaba Secret Key
   REGION
     Enter Alibaba Region for the Bucket
   BUCKET NAME
    Enter existing Alibaba Bucket name, or to add a new Bucket enter a new name and select `Create Bucket`.
   Create Bucket
    Enable if the Bucket entered in BUCKET NAME does not exist and needs to be created.
   Default Backup Target
    Sets this Bucket as the default backup target when creating Backups. If selected the option to update existing Backup configuration to use this Bucket will be presented.
   Archive Snapshots
    Enabled to export VM snapshots to this Bucket when creating VMware Backups, after which the snapshot will be removed from the target hypervisor.
   Default Deployment Archive Target
    Sets this bucket as the default storage target when uploading Deployment files in the `Deployments` section.
   Default Virtual Image Store
    Sets this bucket as the default storage target when uploading Virtual Images from the `Virtual Images` section, importing Images from Instance Actions, creating Images with the `Image Builder` and when creating new images from `Migrations`.

   RETENTION POLICY
    None
      Files in the Bucket will not be automatically deleted or backed up.
    Backup Old Files
      This option will backup files after a set amount of time and remove them from the bucket.
        DAYS OLD
          Files older than the set number of days will be automatically backed up to the selected Backup Bucket.
        BACKUP BUCKET
          Search for and select the Bucket the files will be backed up to.
    DELETE OLD FILES
      This option will delete files from this bucket after a set amount of days.
        DAYS OLD
          Files older than the set number of days will be automatically deleted from the Bucket.

#. Select :guilabel:`SAVE CHANGES`

The Bucket will be created and displayed in the Buckets tab.

- To browse, upload, download, or delete files from this Bucket, select the name of the Bucket.

- To edit the Bucket, select the edit icon or select the name of the Bucket and select :guilabel:`ACTIONS - EDIT`.

  .. WARNING:: Repointing a bucket that is in use may cause loss of file references. Ensure data is mirrored first.

- To delete a Bucket, select the trash icon or select the name of the Bucket and select :guilabel:`DELETE`.

  .. WARNING:: When deleting a Bucket, all Deployment Versions and Backups associated with the Bucket will be deleted.


Amazon S3 Buckets
^^^^^^^^^^^^^^^^^

To Add an Amazon S3 Storage Bucket:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the BUCKETS tab, Click the :guilabel:`+ ADD` button.
#. Select `Amazon S3` from the dropdown list
#. From the NEW BUCKET Wizard input the following:

   NAME
     Name of the Bucket in |morpheus|.
   ACCESS KEY
    AWS IAM Access Key
   SECRET KEY
    AWS IAM Secret Key
   BUCKET NAME
    Enter existing S3 Bucket name, or to add a new Bucket enter a new name and select `Create Bucket`.
   CREATE BUCKET
    Enable if the Bucket entered in BUCKET NAME does not exist and needs to be created. If enabled, select an AWS Region to create the Bucket in.
   ENDPOINT URL
    Optional endpoint URL if pointing to an object store other than amazon that mimics the Amazon S3 APIs.
   Default Backup Target
    Sets this Bucket as the default backup target when creating Backups. If selected the option to update existing Backup configuration to use this Bucket will be presented.
   Archive Snapshots
    Enabled to export VM snapshots to this Bucket when creating VMware Backups, after which the snapshot will be removed from the target hypervisor.
   Default Deployment Archive Target
    Sets this bucket as the default storage target when uploading Deployment files in the `Deployments` section.
   Default Virtual Image Store
    Sets this bucket as the default storage target when uploading Virtual Images from the `Virtual Images` section, importing Images from Instance Actions, creating Images with the `Image Builder` and when creating new images from `Migrations`.

   RETENTION POLICY
    None
      Files in the Bucket will not be automatically deleted or backed up.
    Backup Old Files
      This option will backup files after a set amount of time and remove them from the bucket.
        DAYS OLD
          Files older than the set number of days will be automatically backed up to the selected Backup Bucket.
        BACKUP BUCKET
          Search for and select the Bucket the files will be backed up to.
    DELETE OLD FILES
      This option will delete files from this bucket after a set amount of days.
        DAYS OLD
          Files older than the set number of days will be automatically deleted from the Bucket.

#. Select :guilabel:`SAVE CHANGES`

The Bucket will be created and displayed in the Buckets tab.

- To browse, upload, download, or delete files from this Bucket, select the name of the Bucket.

- To edit the Bucket, select the edit icon or select the name of the Bucket and select :guilabel:`ACTIONS - EDIT`.

  .. WARNING:: Repointing a bucket that is in use may cause loss of file references. Ensure data is mirrored first.

- To delete a Bucket, select the trash icon or select the name of the Bucket and select :guilabel:`DELETE`.

  .. WARNING:: When deleting a Bucket, all Deployment Versions and Backups associated with the Bucket will be deleted.


Azure Buckets
^^^^^^^^^^^^^

To Add an Azure Storage Bucket:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the BUCKETS tab, Click the :guilabel:`+ ADD` button.
#. Select `Azure` from the dropdown list
#. From the NEW BUCKET Wizard input the following:

   NAME
     Name of the Bucket in |morpheus|.
   STORAGE ACCOUNT
    Name of the Storage Account in Azure for the Bucket
   STORAGE KEY
    Storage Key provided from Azure
   SHARE NAME
    Enter existing Azure Storage Share name, or to add a new Share enter a new name and select `Create Bucket` below.
   CREATE BUCKET
    Enable if the Share entered in SHARE NAME does not exist and needs to be created.
   Default Backup Target
    Sets this bucket as the default backup target when creating Backups. If selected the option to update existing Backup configuration to use this Bucket will be presented.
   Archive Snapshots
    Enabled to export VM snapshots to this Bucket when creating VMware Backups, after which the snapshot will be removed from the target hypervisor.
   Default Deployment Archive Target
    Sets this Bucket as the default storage target when uploading Deployment files in the `Deployments` section.
   Default Virtual Image Store
    Sets this bucket as the default storage target when uploading Virtual Images from the `Virtual Images` section, importing Images from Instance Actions, creating Images with the `Image Builder` and when creating new images from `Migrations`.

   RETENTION POLICY
    None
      Files in the Bucket will not be automatically deleted or backed up.
    Backup Old Files
      This option will backup files after a set amount of time and remove them from the bucket.
        DAYS OLD
          Files older than the set number of days will be automatically backed up to the selected Backup Bucket.
        BACKUP BUCKET
          Search for and select the Bucket the files will be backed up to.
    DELETE OLD FILES
      This option will delete files from this bucket after a set amount of days.
        DAYS OLD
          Files older than the set number of days will be automatically deleted from the Bucket.

#. Select :guilabel:`SAVE CHANGES`

The Bucket will be created and displayed in the Buckets tab.

- To browse, upload, download, or delete files from this Bucket, select the name of the Bucket.

- To edit the Bucket, select the edit icon or select the name of the Bucket and select :guilabel:`ACTIONS - EDIT`.

  .. WARNING:: Repointing a bucket that is in use may cause loss of file references. Ensure data is mirrored first.

- To delete a Bucket, select the trash icon or select the name of the Bucket and select :guilabel:`DELETE`.

  .. WARNING:: When deleting a Bucket, all Deployment Versions and Backups associated with the Bucket will be deleted.


Dell ECS Buckets
^^^^^^^^^^^^^^^^

.. NOTE:: A Dell ECS Storage Server must be configured in `Infrastructure - Storage - Servers` prior to adding a Dell ECS Bucket.

To Add a Dell ECS Storage Bucket:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the BUCKETS tab, Click the :guilabel:`+ ADD` button.
#. Select `Dell ECS Bucket` from the dropdown list
#. From the NEW BUCKET Wizard input the following:

   NAME
     Name of the Bucket in |morpheus|.
   STORAGE SERVICE
     Select existing Dell ECS Storage Server (configured in `Infrastructure - Storage - Servers`)
   BUCKET NAME
     Enter a name for the new Dell ECS bucket.
   USER
    Dell ECS User
   SECRET KEY
    Dell ECS Secret key
   NAMESPACE
    Select Dell ECS Namespace for the Bucket
   STORAGE GROUP
    Select a Dell ECS Storage Group
   Default Backup Target
    Sets this bucket as the default backup target when creating Backups. If selected the option to update existing Backup configuration to use this Bucket will be presented.
   Archive Snapshots
    Enabled to export VM snapshots to this Bucket when creating VMware Backups, after which the snapshot will be removed from the target hypervisor.
   Default Deployment Archive Target
    Sets this Bucket as the default storage target when uploading Deployment files in the `Deployments` section.
   Default Virtual Image Store
    Sets this bucket as the default storage target when uploading Virtual Images from the `Virtual Images` section, importing Images from Instance Actions, creating Images with the `Image Builder` and when creating new images from `Migrations`.

   RETENTION POLICY
    None
      Files in the Bucket will not be automatically deleted or backed up.
    Backup Old Files
      This option will backup files after a set amount of time and remove them from the bucket.
        DAYS OLD
          Files older than the set number of days will be automatically backed up to the selected Backup Bucket.
        BACKUP BUCKET
          Search for and select the Bucket the files will be backed up to.
    DELETE OLD FILES
      This option will delete files from this bucket after a set amount of days.
        DAYS OLD
          Files older than the set number of days will be automatically deleted from the Bucket.

#. Select :guilabel:`SAVE CHANGES`

The Bucket will be created and displayed in the Buckets tab.

- To browse, upload, download, or delete files from this Bucket, select the name of the Bucket.

- To edit the Bucket, select the edit icon or select the name of the Bucket and select :guilabel:`ACTIONS - EDIT`.

  .. WARNING:: Repointing a bucket that is in use may cause loss of file references. Ensure data is mirrored first.

- To delete a Bucket, select the trash icon or select the name of the Bucket and select :guilabel:`DELETE`.

  .. WARNING:: When deleting a Bucket, all Deployment Versions and Backups associated with the Bucket will be deleted.

Openstack Swift Buckets
^^^^^^^^^^^^^^^^^^^^^^^

To Add an Azure Storage Bucket:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the BUCKETS tab, Click the :guilabel:`+ ADD` button.
#. Select `Openstack Swift` from the dropdown list
#. From the NEW BUCKET Wizard input the following:

   NAME
     Name of the Bucket in |morpheus|.
   USERNAME
    Openstack Swift Username
   API KEY
    Openstack Swift API Key
   BUCKET NAME
    Enter existing Openstack Swift Bucket name, or to add a new Bucket enter a new name and select `Create Bucket` below.
   IDENTITY URL
    Openstack Swift Identity URL
   Create Bucket
    Enable if the name entered in BUCKET NAME does not exist and needs to be created.
   Default Backup Target
    Sets this bucket as the default backup target when creating Backups. If selected the option to update existing Backup configuration to use this Bucket will be presented.
   Archive Snapshots
    Enabled to export VM snapshots to this Bucket when creating VMware Backups, after which the snapshot will be removed from the target hypervisor.
   Default Deployment Archive Target
    Sets this Bucket as the default storage target when uploading Deployment files in the `Deployments` section.
   Default Virtual Image Store
    Sets this bucket as the default storage target when uploading Virtual Images from the `Virtual Images` section, importing Images from Instance Actions, creating Images with the `Image Builder` and when creating new images from `Migrations`.

   RETENTION POLICY
    None
      Files in the Bucket will not be automatically deleted or backed up.
    Backup Old Files
      This option will backup files after a set amount of time and remove them from the bucket.
        DAYS OLD
          Files older than the set number of days will be automatically backed up to the selected Backup Bucket.
        BACKUP BUCKET
          Search for and select the Bucket the files will be backed up to.
    DELETE OLD FILES
      This option will delete files from this bucket after a set amount of days.
        DAYS OLD
          Files older than the set number of days will be automatically deleted from the Bucket.

#. Select :guilabel:`SAVE CHANGES`

The Bucket will be created and displayed in the Buckets tab.

- To browse, upload, download, or delete files from this Bucket, select the name of the Bucket.

- To edit the Bucket, select the edit icon or select the name of the Bucket and select :guilabel:`ACTIONS - EDIT`.

  .. WARNING:: Repointing a bucket that is in use may cause loss of file references. Ensure data is mirrored first.

- To delete a Bucket, select the trash icon or select the name of the Bucket and select :guilabel:`DELETE`.

  .. WARNING:: When deleting a Bucket, all Deployment Versions and Backups associated with the Bucket will be deleted.


Rackspace CDN Buckets
^^^^^^^^^^^^^^^^^^^^^

To Add a Rackspace CDN Bucket:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the BUCKETS tab, Click the :guilabel:`+ ADD` button.
#. Select `Rackspace CDN` from the dropdown list
#. From the NEW BUCKET Wizard input the following:

   NAME
     Name of the Bucket in |morpheus|.
   USERNAME
    Rackspace CDN Username
   API KEY
    Rackspace CDN API Key
   REGION
    Enter Rackspace CDN Region
   BUCKET NAME
    Enter existing Rackspace CDN Bucket name, or to add a new Bucket enter a new name and select `Create Bucket` below.
   Create Bucket
    Enable if the name entered in BUCKET NAME does not exist and needs to be created.
   Default Backup Target
    Sets this bucket as the default backup target when creating Backups. If selected the option to update existing Backup configuration to use this Bucket will be presented.
   Archive Snapshots
    Enabled to export VM snapshots to this Bucket when creating VMware Backups, after which the snapshot will be removed from the target hypervisor.
   Default Deployment Archive Target
    Sets this Bucket as the default storage target when uploading Deployment files in the `Deployments` section.
   Default Virtual Image Store
    Sets this bucket as the default storage target when uploading Virtual Images from the `Virtual Images` section, importing Images from Instance Actions, creating Images with the `Image Builder` and when creating new images from `Migrations`.

   RETENTION POLICY
    None
      Files in the Bucket will not be automatically deleted or backed up.
    Backup Old Files
      This option will backup files after a set amount of time and remove them from the bucket.
        DAYS OLD
          Files older than the set number of days will be automatically backed up to the selected Backup Bucket.
        BACKUP BUCKET
          Search for and select the Bucket the files will be backed up to.
    DELETE OLD FILES
      This option will delete files from this bucket after a set amount of days.
        DAYS OLD
          Files older than the set number of days will be automatically deleted from the Bucket.

#. Select :guilabel:`SAVE CHANGES`

The Bucket will be created and displayed in the Buckets tab.

- To browse, upload, download, or delete files from this Bucket, select the name of the Bucket.

- To edit the Bucket, select the edit icon or select the name of the Bucket and select :guilabel:`ACTIONS - EDIT`.

  .. WARNING:: Repointing a bucket that is in use may cause loss of file references. Ensure data is mirrored first.

- To delete a Bucket, select the trash icon or select the name of the Bucket and select :guilabel:`DELETE`.

  .. WARNING:: When deleting a Bucket, all Deployment Versions and Backups associated with the Bucket will be deleted.
