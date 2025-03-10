File Shares
-----------

File Shares are for Backup, Archives, Deployment and Virtual Images storage targets. File Shares can be browsed and files and folders can be uploaded, downloaded or deleted from the File Shares section. Retention Policies can be set on Storage File Shares for files to be deleted or backed up to another File Share after a set amount of time.

Supported File Share Types
^^^^^^^^^^^^^^^^^^^^^^^^^^

* Azure
* CIFS (Samba Windows File Sharing)
* Dell EMC ECS Share
* Dell EMC Isilon Share
* Local Storage
* NFSv3


Azure File Shares
^^^^^^^^^^^^^^^^^

To Add an Azure File Share:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the FILE SHARES tab, Click the :guilabel:`+ ADD` button.
#. Select `Azure` from the dropdown list
#. From the NEW FILE SHARE Wizard input the following:

   NAME
     Name for the file share in |morpheus|.
   STORAGE ACCOUNT
    Name of the Storage Account in Azure for the file share
   STORAGE KEY
    Storage Key provided from Azure
   SHARE NAME
    Enter existing Azure Storage Share name or, to add a new Share, enter a new name and mark the `Create Bucket` box below
   CREATE BUCKET
    Mark if the share entered in SHARE NAME does not exist and needs to be created
   DEFAULT BACKUP TARGET
    Sets this file share as the default backup target when creating Backups. If selected, the option to UPDATE EXISTING BACKUPS will appear. Mark to update existing backups to this file share
   DEFAULT DEPLOYMENT ARCHIVE TARGET
    Sets this file share as the default storage target when creating deployment archives
   DEFAULT VIRTUAL IMAGE STORE
    Sets this file share as the default storage target when uploading Virtual Images from the `Virtual Images` section or when importing Images from Instance Actions

   RETENTION POLICY
    None
      Files in the share will not be automatically deleted or backed up
    Backup Old Files
      This option will backup files after a set amount of time and remove them from the file share
        DAYS OLD
          Files older than the set number of days will be automatically backed up to the selected Backup target
        BACKUP BUCKET
          Search for and then select the desired backup bucket
    DELETE OLD FILES
      This option will delete files from this share after a set amount of days
        DAYS OLD
          Files older than the set number of days will be automatically deleted from the share

#. Select :guilabel:`SAVE CHANGES`

The file share will be created and displayed in the file shares tab.

- To browse, upload, download, or delete files from this file share, select the name of the share from the File Shares tab.

- To edit the file share, select the edit icon or select the name of the share and select :guilabel:`ACTIONS - EDIT`.

  .. WARNING:: Re-pointing a file share that is in use may cause loss of file references. Ensure data is mirrored first.

- To delete a file share, select the trash icon or select the name of the file share and click :guilabel:`DELETE`.

  .. WARNING:: When deleting a file share, all Deployment versions and Backups associated with the file share will be deleted.

CIFS File Shares
^^^^^^^^^^^^^^^^

To Add a CIFS File Share:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the FILE SHARES tab, Click the :guilabel:`+ ADD` button.
#. Select `CIFS (Samba Windows File Sharing)` from the dropdown list
#. From the NEW FILE SHARE Wizard input the following:

   NAME
     Name of the File Share in |morpheus|.
   HOST
     Enter host IP or resolvable hostname
      Example: ``192.168.200.210``
   USERNAME
    CIFS Share Username
   PASSWORD
    CIFS Share User Password
   SHARE PATH
    Enter CIFS Share Path
      Example: ``cifs``
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


Dell EMC ECS File Shares
^^^^^^^^^^^^^^^^^^^^^^^^

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


Dell EMC Isilon File Shares
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To Add a Dell EMC Isilon File Share:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the FILE SHARES tab, Click the :guilabel:`+ ADD` button.
#. Select `Dell EMC Isilon Share` from the dropdown list
#. From the NEW FILE SHARE Wizard input the following:

   NAME
     Name of the File Share in |morpheus|.
   STORAGE SERVICE
     Select existing Dell EMC Isilon Storage Server (configured in `Infrastructure - Storage - Servers`)
   SHARE PATH
     Enter Dell EMC Isilon Share Path
      Example: ``ecs-file-share-1``
   Volume Size
    Specify volume size for the File Share (in MB)
   Allowed IP's
    Specify IP Addresses to limit accessibility to the File Share
      Leave blank for open access
        Click the ``+`` symbol to the right of the first ALLOWED IPS field to add multiple IP's
   NAMESPACE
     Select Dell EMC Isilon Namespace (synced)
   STORAGE GROUP
    Select Dell EMC Isilon Storage Group (synced)
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


Local Storage File Shares
^^^^^^^^^^^^^^^^^^^^^^^^^

.. IMPORTANT:: Local Storage refers to local to the |morpheus| Appliance and the path must be owned by `morpheus-app`. Please be conscious of storage space. High Availability configurations require Local Storage File Shares paths to be shared storage paths between the font end |morpheus| Appliances.

.. NOTE:: To change the owner of a file path to be used as a Local Storage File Share, run ``chown morpheus-app.morpheus-app /path`` on the |morpheus| Appliance.

.. NOTE:: |morpheus| will validate path and ownership of the File Share Path.

To Add a Local Storage File Share:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the FILE SHARES tab, Click the :guilabel:`+ ADD` button.
#. Select `Local Storage Share` from the dropdown list
#. From the NEW FILE SHARE Wizard input the following:

   NAME
     Name of the File Share in |morpheus|.
   STORAGE PATH
     Enter the File Share path on the local |morpheus| Appliance.
      Example: ``/var/opt/morpheus/morpheus-ui/vms/virtual-images``

      .. IMPORTANT:: High Availability configurations require Local Storage File Shares paths to be shared storage paths between the font end |morpheus| Appliances.
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

NFSv3 File Shares
^^^^^^^^^^^^^^^^^

.. NOTE:: Configure access to the NFS folder on the NFS Provider prior to adding the NFSv3 File Share.

.. NOTE:: Upon save |morpheus| will create a persistent mount owned by ``morpheus-app.morpheus-app`` on the |morpheus| Appliance for the NFSv3 File Share. The |morpheus| appliance will require access to the following ports in order to mount the share: 111, 54302, 20048, 2049, 46666, 42955, 875. With some storage solutions, you may need to enable insecure, unprivileged ports, or allow non-root on the export before |morpheus| is able to successfully mount the share.

To Add a NFSv3 File Share:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the FILE SHARES tab, Click the :guilabel:`+ ADD` button.
#. Select `NFSv3` from the dropdown list
#. From the NEW FILE SHARE Wizard input the following:

   NAME
     Name of the File Share in |morpheus|.
   HOST
     Enter the File Share path on the local |morpheus| Appliance.
   EXPORT FOLDER
     Enter the NFSv3 Folder
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
