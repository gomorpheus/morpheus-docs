Storage Management
^^^^^^^^^^^^^^^^^^

There are two types of storage that are available for an instance to consume. One is the local storage available on the compute server used to create an instance. The other is the remote storage (SAN), using the Alletra MP storage array.

 At present, there is no support for the management of the local storage throughHPE Morpheus. They are used to install the OS image, and any storage available beyond that is up to the user to configure and use. They cannot be managed fromHPE Morpheus.

 The remote storage is fully manageable. The user can create/update/delete volumes and manage their attachment to compute servers.

Boot Volume Selection
---------------------

During Instance Creation for Local Storage
  During Morpheus instance creation, the provisioning workflow will delete existing logical volumes,create a boot volume, and then identify the correct disk deviceusing the device’s unique identifier (UID).

 The boot volume is determined by matching the device UID found in the storage controller to the corresponding Linux device path.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Storage Device
     - Name
     - RAID Type
     - Identifiers.DurableNameFormat
     - Identifiers.DurableName
   * - HPE MegaRAID (MR216i-o) Storage Controller
     - BootVolume
     - RAID1
     - NAA
     - 600508B1001C40706B7600592D4A5C5A
   * - HPE NVMe SHIELD (NS204i) Boot Device
     - BootVolume
     - RAID1
     - EUI
     - 1234:5678:9ABC:DEF0

Finding the Device Path
 Once the device UID is known (from the storage controller), the provisioning script searches for the matching device in/dev/disk/by-id/

 The script looks for thefirst entry that contains the UID(or a stripped version of the UID). These entries arestable identifiersthat point to the actual Linux block device.

 Once a match is found, the script resolves the symbolic link to determine the real boot device path, which will be in the form:/dev/sdX

 This/dev/sdXpath is then used for OS installation.

Remote Storage
--------------

Remote storage enables lifecycle management of volumes on supportedHPE Alletra storage arrays(includingAlletra MPandAlletra 9000, where supported) and allows compute instances to attach to or detach from those volumes. These operations can be performed during instance provisioning or post-provisioning through the reconfigure workflow. The currently supported transport protocol isFibre Channel.

 To get started with using remote storage, first, the storage plugin for Alletra needs to be loaded, and a storage server added. This allows the user to specify the URL where the management interface of the storage array is available, along with the user credentials to manage the storage array.

 There is also a concept of a datastore, which is used to represent a container for a set of volumes. A datastore is associated with a storage server and also a resource pool. The resource pool is used to represent a site or a location, which is useful when storage HA is being used with datastores associated with different sites.

  AddingHPE AlletraStorage Integration
 You can add the Allertra Storage plugin JAR using the Upload plugin method.

Creating a Storage Server
^^^^^^^^^^^^^^^^^^^^^^^^^

  This procedure guides you through creating a storage server.


#. Log in to the
#. HPE
#. |morpheus| Enterprise Software web interface using your administrator credentials. 
#. Navigate to
#. Infrastructure
#. >
#. Storage
#. >
#. Servers.
#. Click the
#. Add.
#. Provide a
#. Name
#. , select
#. HPE 
#. Alletra Block Storage HVM
#. for type, specify the URL for the storage array, and the credentials. 
#. Click the
#. Save Changes
#. to create the storage server.

Results
 The added storage server appears under Servers.

Creating a Datastore
^^^^^^^^^^^^^^^^^^^^

  This procedure guides you through creating a Datastore. The datastore acts as a container for volumes and must be created before volumes can be created.


#. Log in to the
#. HPE
#. |morpheus| Enterprise Software web interface using your administrator credentials. 
#. Navigate to
#. Infrastructure
#. >
#. Storage
#. >
#. DataStores.
#. Click the
#. Add.
#. Provide a
#. Name
#. , select
#. HPE 
#. Alletra Block Storage Baremetal
#. for type, select your
#. cloud
#. , the
#. storage server
#. previously created,
#. FC
#. as the protocol type, and the
#. Resource Pool
#. that applies to this storage server. 
#. Click the
#. Save
#. to create the DataStore.

Results
 The added data store appears under Data Store.

Volume Management
-----------------

Volume life cycle management can be performed under theInfrastructure>Storage>Volumestab. It allows the user to perform create/resize/delete operations.

Adding Volume
^^^^^^^^^^^^^

  Perform the following procedure to create a new volume:


#. Navigate to
#. Infrastructure
#. >
#. Storage
#. >
#. Volumes.
#. Click the
#. Add
#. button. 
#. Select the
#. storage server
#. to create the volume in and click
#. Next.
#. Select the required volume type, unreplicated, CPP replicated, or APP replicated, and click
#. Next.
#. On the
#. Configure
#. screen, specify the volume name, size, datastore in which the volume needs to be created, shared/unshared. You can optionally specify the server/instance to export the volume, depending on whether it is unshared/shared. 
#. Click
#. Complete
#. to finish adding the volume.

Deleting Volume
^^^^^^^^^^^^^^^

  This procedure allows the users to delete a volume. A volume can be deleted only after it is detached from all the servers.


#. Navigate to
#. Infrastructure
#. >
#. Storage
#. >
#. Volumes.
#. Click the
#. Actions
#. pulldown on the right and select
#. Delete
#. for the volume to be deleted. 
#. Click the
#. Delete
#. on the confirmation screen.

Resizing Volume
^^^^^^^^^^^^^^^

  This procedure allows the user to resize a volume. Volume size can only be increased. A rescan is required on the server OS to see the increased size.


#. Navigate to
#. Infrastructure
#. >
#. Storage
#. >
#. Volumes.
#. Click the
#. Actions
#. pulldown on the right and select
#. Resize
#. for the volume to be deleted. 
#. Specify the new size and click
#. Resize.
Reconfiguring Volume
^^^^^^^^^^^^^^^^^^^^

  Reconfiguration allows the user to make changes to volumes consumed by a compute instance post-provisioning. This is achieved through theReconfigureaction on the instance.

 New volumes can be created and attached to the compute instance. These can be shared or unshared volumes. Any volume attached to the compute instance can be resized to increase the size of the volume. Any attached volume can be detached. However, volumes cannot be deleted from the Reconfigure action. Volumes can be deleted only from the infrastructure management section.

 All these operations work in the context of a compute instance and are not specific to a compute server within the instance.


#. Navigate to
#. Provision
#. >
#. Instance.
#. Click on the compute instance you want to reconfigure and access the details of the instance. 
#. Click on
#. Actions
#. and select
#. Reconfigure.
#. In the
#. Reconfigure
#. wizard, make the changes desired to add a new volume, resize an existing volume or click the trash icon to detach a volume from the instance.

 
#. Click on
#. Reconfigure.
Volume Consumption
------------------

Consumption of volume is typically done through compute instance provisioning, where the user can specify volumes to attach to, whether existing volumes or new volumes to be created. It can also be done using the reconfigure action.

  Instance Provisioning
 During instance provisioning, the user can specify volumes to be attached to the servers within the instance. There are various types of volumes user can specify.

Sharing
 Volumes can be shared or unshared (attached to a specific server only). Specifying a shared volume means a single volume is attached to all the servers within that instance. Specifying an unshared volume means a volume is created for each server within the instance and exported to the corresponding server.

Existing vs New
 The user can specify a new volume to be created or specify to attach to an existing volume. Existing volume is applicable only to shared volumes.

Replicated vs Unreplicated
 When creating new volumes, the user can specify that the volume is unreplicated or replicated. Depending on the storage array deployed and the HA configuration, replicated volumes can be specified as CPP (classic peer persistence) or APP (active peer persistence).

Using Volume
^^^^^^^^^^^^

 Perform the following to use the configured volume:      
#. Navigate to
#. Provisioning
#. >
#. Instances.
#. Click
#. Add.
#. After selecting the
#. HPE
#. BareMetal ILO server for type and specifying the cloud, group, and a name for the instance, click
#. Next
#. to advance to the
#. Configure
#. section. 
#. Click on the
#. +
#. sign next to Volumes to add a volume to this instance. 
#. Specify a name for the volume, desired size, volume type to indicate whether it is a replicated volume or not, the datastore to create it in, and whether it’s a shared volume.

