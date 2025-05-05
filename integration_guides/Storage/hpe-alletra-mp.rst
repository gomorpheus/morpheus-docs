HPE Alletra MP Storage
----------------------

Prerequisites
^^^^^^^^^^^^^

* All HPE Alletra MP Storage iSCSI ports are reachable from each of the cluster hosts
* The ``multipath.conf`` settings on each node should be configured as follows:

.. code-block:: bash

  defaults {
      find_multipaths yes
      user_friendly_names no
  }

Add HPE Alletra MP Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^

The first step is to create a storage server in |morpheus|. Once the storage server is added, you can create a datastore and provision Instances. Follow these steps to add a Storage Server:

#. Navigate to |InfSto|
#. In the "Servers" tab, Click the :guilabel:`+ ADD` button
#. From the ADD STORAGE SERVER wizard, input the following:

   NAME:
     Name of the storage server in |morpheus|
   TYPE:
     Select "HPE Alletra MP"
   URL:
     URL of HPE Alletra MP Storage (ex. ``https://storage-system.example.com`` or ``https://192.1.2.3:1234``)
   USERNAME:
      Add your administrative user account
   PASSWORD:
      Add your administrative user account password

#. Select :guilabel:`SAVE CHANGES`

.. image:: /images/infrastructure/Storage/hpe-alletra-mp/add-storage-server.png
  :width: 30%

The `Storage Server` will be added and displayed in the `Datastore` tab.

Create Datastore
^^^^^^^^^^^^^^^^

Add a `Datastore` to the `Storage Server`.

#. Navigate to |InfClu|
#. Click into the detail page for the cluster where datastore is to be created
#. Select the "Storage" tab
#. Under the "Data Stores" sub tab, Click :guilabel:`+ ADD`
#. From the ADD DATASTORE wizard, input the following:

   NAME:
     Name of the datastore in |morpheus|
   TYPE:
     Select "HPE Alletra MP"
   STORAGE SERVER:
     Select the Storage Server created using the steps in the previous section

#. Select :guilabel:`SAVE`

.. image:: /images/infrastructure/Storage/hpe-alletra-mp/create-datastore.png
  :width: 50%

The data store will be added and displayed in the "Datastore" tab. Confirm that its status is healthy.

Create Instance
^^^^^^^^^^^^^^^

Create an Instance with the Datastore.

#. Navigate to |ProIns|
#. In the `Instances` tab, Click the :guilabel:`+ ADD` button
#. From the ADD INSTANCE wizard input the following:

   - From the TYPE section: Select "|hvm|"
   - Click :guilabel:`NEXT`

     .. image:: /images/infrastructure/Storage/hpe-alletra-mp/create-instance-type.png
        :width: 50%

   - From the GROUP tab, input the following:

      GROUP:
        Select the Group for the Instance
      CLOUD:
        Select the Cloud for the Instance
      NAME:
        Name for the Instance in |morpheus|

   - Click :guilabel:`NEXT`

     .. image:: /images/infrastructure/Storage/hpe-alletra-mp/create-instance-group.png
        :width: 50%

   - From the CONFIGURE tab, input the following:

      LAYOUT:
        Select the Layout for the Instance
      PLAN:
        Select the Plan for the Instance
      RESOURCE POOL:
        Select the Resource Pool (Cluster) for the Instance
      VOLUMES:
        Add one or more Volumes to the Instance. Select the datastore created in the previous section
      NETWORK:
        Add Networks to the Instance
      IMAGE:
        Select the Image for the Instance
      HOST:
        Select the cluster host for the Instance

      Other configurations may be added as needed.

       .. image:: /images/infrastructure/Storage/hpe-alletra-mp/create-instance-configure.png
         :width: 50%

   - Click :guilabel:`NEXT`
   - Add Automation Tasks, if needed
   - Click :guilabel:`NEXT`
   - Review the Instance configuration
   - Click :guilabel:`COMPLETE`

    .. image:: /images/infrastructure/Storage/hpe-alletra-mp/create-instance-review.png
     :width: 50%

The Instance is now provisioned to the new datastore and is viewable within the Instances (|ProIns|) section.
