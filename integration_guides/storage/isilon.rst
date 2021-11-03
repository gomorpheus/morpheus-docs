Isilon
------

Add Dell EMC Isilon Storage Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. IMPORTANT:: Enable insecure mode on the NFS settings.  This allows non-root ports to be used.  Setting the insecure/privileged mode will require a restart of the Isilon nodes.

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the SERVERS tab, Click the :guilabel:`+ ADD` button.
#. From the ADD STORAGE SERVER wizard input the following:

   NAME
      Name of the Storage Server in |morpheus|
   TYPE
      Select `Dell EMC Isilon`
   URL
     URL Of Dell EMC Isilon Server
     Example : `https://192.168.190.202:8080`
   USERNAME
    Add your administrative user account.
   PASSWORD
    Add your administrative password.
   PROVISION USER
    Select Provision User
   PROVISION GROUP
    Select Provision Group
   ROOT PATH
    Enter Root Path
      Example : ``\``

#. Select :guilabel:`SAVE CHANGES`

The Dell EMC Isilon Storage Server will be added and displayed in the Buckets tab.

Buckets, Files Shares and Storage Groups will be synced in.

Add Dell EMC Isilon File Share
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
