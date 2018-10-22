Volumes
-------

Volumes sync or created in |morpheus| can be viewed in `Infrastructure- Storage - Volumes`. Volumes can be added for Storage Servers integrated with |morpheus| in the `Infrastructure- Storage - Servers` section.

Volumes Types
^^^^^^^^^^^^^

The available Volume Types list and filterable by are:

- 3Par Volume
- Alibaba Cloud SSD
- Alibaba Efficiency Disk
- Alibaba Cloud Disk
- AWS gp2
- AWS io1
- AWS sc1
- AWS st1
- Azure Volume
- Azure Disk
- Bluemix Disk
- Bluemix SAN
- Bluemix SAN
- CD ROM
- DO Disk
- ECS Block Storage
- ECS Object Storage
- ECS Shared File System
- Floppy Disk
- Google Standard
- HP Enclosure Disk
- Oracle iSCSI
- Isilon NFS Volume
- Nutanix IDE
- Nutanix SATA
- Nutanix SCSI
- Open Telekom Volume
- Openstack Disk
- Openstack Volume
- Oracle Block Volume
- Oracle Disk
- Oracle Virtual Volume
- SCVMM Datastore
- Softlayer Disk
- Softlayer SAN
- Softlayer SAN
- Disk
- UpCloud Disk
- UpCloud MaxIOPS
- NULL
- NULL
- VMWare Datastore
- VMWare Disk

CREATE VOLUME
^^^^^^^^^^^^^

At least one Storage Server Integration from `Infrastructure- Storage - Servers` is required to create volumes from `Infrastructure- Storage - Volumes`.

3par
....

To Add a 3Par Volume:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the VolumeS tab, Click the :guilabel:`+ ADD` button.
#. Select `3Par` from the dropdown list
#. From the CREATE VOLUME Wizard input the following:

   SELECT TYPE
    STORAGE SERVER
      Name of the 3par Storage Server added in `Infrastructure- Storage - Servers`
    GROUP
     Select Storage Group
    VOLUME TYPE
      3Par Volume
    Click NEXT
      Select :guilabel:`NEXT`
   CONFIGURE
    NAME
      Name of the Volume
    VOLUME SIZE
      Specify size of the Volume (in MB)

    PROVISION TYPE
      - FULL
      - TPVV
      - SNP
      - PEER
      - UNKNOWN
      - TDVV
    Click COMPLETE
         Select :guilabel:`COMPLETE`

Dell EMC ECS
............

To Add a Dell EMC ECS Volume:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the VolumeS tab, Click the :guilabel:`+ ADD` button.
#. Select `Dell EMC ECS` from the dropdown list
#. From the CREATE VOLUME Wizard input the following:

   SELECT TYPE
    STORAGE SERVER
       Name of the DELL EMC ECS Storage Server added in `Infrastructure- Storage - Servers`
    GROUP
      Select Storage Group
    VOLUME TYPE
       ECS Block Storage
       ECS Object Storage
       ECS Shared File System
    Click NEXT
       Select :guilabel:`NEXT`
   CONFIGURE
    NAME
       Name of the Volume
   Click COMPLETE
          Select :guilabel:`COMPLETE`


Dell EMC Isilon
...............

To Add a Dell EMC ECS Volume:

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the VolumeS tab, Click the :guilabel:`+ ADD` button.
#. Select `Dell EMC Isilon` from the dropdown list
#. From the CREATE VOLUME Wizard input the following:

   SELECT TYPE
    STORAGE SERVER
       Name of the Dell EMC Isilon Storage Server added in `Infrastructure- Storage - Servers`
    GROUP
      Select Storage Group
    VOLUME TYPE
      Isilon NFS Volume
    Click NEXT
       Select :guilabel:`NEXT`
   CONFIGURE
    NAME
     Name of the Volume
    ALLOWED IP's
      Specify IP Addresses to limit accessibility to the File Share
        Leave blank for open access
          Click the ``+`` symbol to the right of the first ALLOWED IPS field to add multiple IP's
    VOLUME SIZE
     Specify size of the Volume (in MB)
   Click COMPLETE
          Select :guilabel:`COMPLETE`
