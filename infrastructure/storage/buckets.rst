Storage Buckets
---------------

Storage Buckets are for Backup, Archives, Deployment and Virtual Images storage targets. Buckets can be browsed and files and folders can be uploaded, downloaded or deleted from the Bucket section. Retention Policies can be set on Storage Buckets for files to be deleted or backed up to another bucket after a set amount of time.

Supported Bucket Types
^^^^^^^^^^^^^^^^^^^^^^

- Alibaba
- Amazon S3
- Azure
- Google Cloud Storage
- Openstack Swift
- Rackspace CDN
- Generic S3

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
          Search for and then select the Bucket the files will be backed up to.
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
          Search for and then select the Bucket the files will be backed up to.
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
          Search for and then select the Bucket the files will be backed up to.
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


Google Cloud Storage Buckets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: Google Cloud Storage Buckets are associated with an existing GCP Cloud integration. Ensure the GCP Cloud integration is pre-existing before attempting to create a new Google Cloud Storage Bucket. On the initial integration and subsequent cloud syncs, Google Cloud Storage Buckets are automatically onboarded and updated.

To add a Google Cloud Storage Bucket:

#. Select the Infrastructure link in the navigation bar
#. Select the Storage link in the sub-navigation bar
#. In the BUCKETS tab, Click the :guilabel:`+ ADD` button
#. Select `Google Cloud Storage` from the dropdown list
#. From the NEW BUCKET Wizard input the following:

   NAME
     A friendly name for the bucket in |morpheus|
   STORAGE SERVICE
     Select the GCP cloud integration this bucket should be created in
   PROJECT ID
     Select the Project to create the group under, Projects are a GCP-specific concept and are logical grouping for your resources. Select any existing project associated with your selected GCP cloud integration
   BUCKET NAME
     The name for the bucket resource on the GCP side
   LOCATION TYPE
     Select Region, Dual-Region, or Multi-Region. Buckets with a Region location type will be stored in one GCP region, such as "us-east1 (South Carolina)". Dual-Region and Multi-Region data is stored in two (or more, in the case of multi-region) GCP regions separated by a significant physical distance. Dual-Region and Multi-Region data is geo-redundant across the multiple selected regions
   LOCATION
     A selected GCP region (or regions, in the case of dual and multi-location data) where the data will be stored
   STORAGE CLASS
     Select Standard, Nearline, Coldline, or Archive. The appropriate storage class will depend on how frequently the bucket data is accessed and how long the type of data in the bucket is expected to be stored. More information on storage classes can be found in `GCP Documentation <https://cloud.google.com/storage/docs/storage-classes#descriptions>`_
   ACTIVE
     When marked, the bucket is available for use in |morpheus|
   DEFAULT BACKUP TARGET
     Sets the bucket as the default storage option when creating backups at provision time or in the Backups section of |morpheus|
   DEFAULT DEPLOYMENT ARCHIVE TARGET
     Sets this Bucket as the default storage target when uploading deployment files in the `Deployments` section
   DEFAULT VIRTUAL IMAGE STORE
     Sets this bucket as the default storage target when uploading virtual images from the `Virtual Images` section, importing images from Instance actions, creating images with the `Image Builder`, and when creating new images from `Migrations`
   RETENTION POLICY
     Select None and the files in this bucket will never be deleted or backed up by |morpheus|. When selecting 'Backup Old Files', |morpheus| will backup files into another selected bucket once they reach a certain number of days old. When selecting 'Delete Old Files', |morpheus| will delete any files that reach a certain number of days old

Dell EMC ECS Buckets
^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: A Dell EMC ECS Storage Server must be configured in `Infrastructure - Storage - Servers` prior to adding a Dell EMC ECS Bucket.

To Add a Dell EMC ECS Storage Bucket:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the BUCKETS tab, Click the :guilabel:`+ ADD` button.
#. Select `Dell EMC ECS Bucket` from the dropdown list
#. From the NEW BUCKET Wizard input the following:

   NAME
     Name of the Bucket in |morpheus|.
   STORAGE SERVICE
     Select existing Dell EMC ECS Storage Server (configured in `Infrastructure - Storage - Servers`)
   BUCKET NAME
     Enter a name for the new Dell EMC ECS bucket.
   USER
    Dell EMC ECS User
   SECRET KEY
    Dell EMC ECS Secret key
   NAMESPACE
    Select Dell EMC ECS Namespace for the Bucket
   STORAGE GROUP
    Select a Dell EMC ECS Storage Group
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
          Search for and then select the Bucket the files will be backed up to.
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
          Search for and then select the Bucket the files will be backed up to.
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
          Search for and then select the Bucket the files will be backed up to.
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
