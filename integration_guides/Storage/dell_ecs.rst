Dell ECS
--------

Overview
^^^^^^^^

|morpheus| integrates with DELL EMC ECS via the ECS api. This allows Morpheus to talk directly to the ECS services.

When you add a ECS Server, |morpheus| will sync in the following.

- Storage Groups
- Buckets
- File shares

Users will be able to create the following times within ECS without direct access to the ECS console.

- Buckets
- File shares

Storage Servers
^^^^^^^^^^^^^^^

The first step in the Dell EMC ECS integration is to add a Dell EMC ECS Storage Server. Once added, Buckets, Files Shares and Storage Groups will be synced in and can be access and managed in |morpheus|.

Adding Dell EMC ECS Storage Server
..................................

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the SERVERS tab, Click the :guilabel:`+ ADD` button.
#. From the ADD STORAGE SERVER wizard input the following:

   NAME
      Name of the Storage Server in |morpheus|
   TYPE
      Select `Dell EMC ECS`
   URL
     URL Of DELL EMC ECS Server
     Example : `https://192.168.190.200:4443`

     .. TIP:: The port 4443 is the api port for ECS api. This may be different depending on your configuration

   USERNAME
    Add your administrative user account.
   PASSWORD
    Add your administrative password.
   S3 SERVICE URL (Optional)
    Add your S3 service url
    Example: http://192.168.190.220:9020

    .. NOTE:: S3 SERVICE URL is not required if you are not planning on using ECS S3.

#. Select :guilabel:`SAVE CHANGES`

The Dell EMC ECS Storage Server will be added and displayed in the Buckets tab.

Buckets, Files Shares and Storage Groups will be synced in.

Buckets
^^^^^^^

- **Buckets** will be listed in `Infrastructure - Storage - Buckets`

  - Buckets can be created and deleted with `Infrastructure - Storage` Role Permissions
  - Buckets can be browsed with `Infrastructure: Storage Browser` Role permissions
  - File and folders can be uploaded, downloaded and deleted with Full `Infrastructure: Storage Browser` Role permissions.

Adding Dell EMC ECS Buckets
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: A Dell ECS Storage Server must be configured in `Infrastructure - Storage - Servers` prior to adding a Dell ECS Bucket.

To Add a Dell ECS Storage Bucket:

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
     Enter a name for the new Dell ECS bucket.
   USER
    Your Dell EMC ECS S3 user account
   SECRET KEY
    Your Dell EMC ECS S3 Secret
      Example: jW+pFyAPtSS5FuEqKwt44xlpM/2
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
      This option will backup files after a set amount if time and remove them from the bucket.
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

Add Dell EMC ECS File Shares
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To Add a Dell EMC ECS File Share:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the FILE SHARES tab, Click the :guilabel:`+ ADD` button.
#. Select `Dell EMC ECS Share` from the dropdown list
#. From the NEW FILE SHARE Wizard input the following:

   NAME
     Name of the File Share in |morpheus|.
   STORAGE SERVICE
     Select existing Dell EMC ECS Storage Server (configured in `Infrastructure - Storage - Servers`)
   SHARE PATH
     Enter Dell EMC ECS Share Path
      Example: ``ecs-file-share-1``
   USER
    Dell EMC ECS User
   SECRET KEY
    Dell EMC ECS Secret key
   Volume Size
    Specify volume size for the File Share (in MB)
   Allowed IP's
    Specify IP Addresses to limit accessibility to the File Share
      Leave blank for open access
        Click the ``+`` symbol to the right of the first ALLOWED IPS field to add multiple IP's
   NAMESPACE
     Select Dell EMC ECS Namespace (synced)
   STORAGE GROUP
    Select Dell EMC ECS Storage Group (synced)
   Default Backup Target
    Sets this File Share as the default backup target when creating Backups. If selected the option to update existing Backup configuration to use this File Share will be presented.
   Archive Snapshots
    Enabled to export VM snapshots to this File Share when creating VMware Backups, after which the snapshot will be removed from the source Cloud.
   Default Deployment Archive Target
    Sets this File Share as the default storage target when uploading Deployment files in the `Deployments` section.
   Default Virtual Image Store
    Sets this File Share as the default storage target when uploading Virtual Images from the `Virtual Images` section, importing Images from Instance Actions, creating Images with the `Image Builder` and when creating new images from `Migrations`.

   RETENTION POLICY
    None
      Files in the File Share will not be automatically deleted or backed up.
    Backup Old Files
      This option will backup files after a set amount if time and remove them from the File Share.
        DAYS OLD
          Files older than the set number of days will be automatically backed up to the selected Backup File Share.
        BACKUP File Share
          Search for and select the File Share the files will be backed up to.
    DELETE OLD FILES
      This option will delete files from this File Share after a set amount of days.
        DAYS OLD
          Files older than the set number of days will be automatically deleted from the File Share.

#. Select :guilabel:`SAVE CHANGES`

The File Share will be created and displayed in the File Shares tab.

- To browse, upload, download, or delete files from this File Share, select the name of the File Share.

- To edit the File Share, select the edit icon or select the name of the File Share and select :guilabel:`ACTIONS - EDIT`.

  .. WARNING:: Repointing a File Share that is in use may cause loss of file references. Ensure data is mirrored first.

- To delete a File Share, select the trash icon or select the name of the File Share and select :guilabel:`DELETE`.

  .. WARNING:: When deleting a File Share, all Deployment Versions and Backups associated with the File Share will be deleted.
