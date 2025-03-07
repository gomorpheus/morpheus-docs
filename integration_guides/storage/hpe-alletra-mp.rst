HPE Alletra MP Storage
----------------------

Prerequisites
^^^^^^^^^^^^^

* All HPE Alletra MP Storage iSCSI ports are reachable from each of the cluster hosts.
* The `multipath.conf` settings on each node should be configured as follows

.. code-block:: markdown

    defaults {
        find_multipaths yes
        user_friendly_names no
    }

Add HPE Alletra MP Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^

The first step is to create a Storage Server in |morpheus|. Once the Storage Server is added, you can create a Datastore and provision Instances.
Follow these steps to add a Storage Server.

#. Select the `Infrastructure` link in the navigation bar.
#. Select the `Storage` link in the sub navigation bar.
#. In the `Servers` tab, Click the :guilabel:`+ ADD` button.
#. From the ADD STORAGE SERVER wizard, input the following:

   NAME:
     Name of the Storage Server in |morpheus|
   TYPE:
     Select `HPE Alletra MP`
   URL:
     URL of HPE Alletra MP Storage
     Examples : `https://storage-system.example.com`, `https://192.1.2.3:1234`
   USERNAME:
      Add your administrative user account.
   PASSWORD:
      Add your administrative password.

#. Select :guilabel:`SAVE CHANGES`

.. image:: /images/infrastructure/Storage/hpe-alletra-mp/add-storage-server.png

The `Storage Server` will be added and displayed in the `Datastore` tab.


Create Datastore
^^^^^^^^^^^^^^^^

Add a `Datastore` to the `Storage Server`.

#. Select the `Infrastructure` link in the navigation bar.
#. Select the `Clusters` link in the sub navigation bar.
#. Navigate to the Cluster where datastore is to be created.
#. Select the `Storage` tab.
#. Under the `Data Stores` sub tab, Click the :guilabel:`+ ADD` button.
#. From the ADD DATASTORE wizard, input the following:

   NAME:
     Name of the Datastore in |morpheus|
   TYPE:
     Select `HPE Alletra MP`
   STORAGE SERVER:
     Select the Storage Server created as a part of Add Storage Server.

#. Select :guilabel:`SAVE`

.. image:: /images/infrastructure/Storage/hpe-alletra-mp/create-datastore.png

The `Datastore` will be added and displayed in the `Datastore` tab and confirm that the status is marked as healthy.


Create Instance
^^^^^^^^^^^^^^^

Create an `Instance` with the Datastore.

#. Select the `Provisioning` link in the navigation bar.
#. Select the `Instances` link in the sub navigation bar.
#. In the `Instances` tab, Click the :guilabel:`+ ADD` button.
#. From the ADD INSTANCE wizard input the following:

   - From the TYPE section:
       Select `HPE VM`
   - Select :guilabel:`NEXT`

   .. image:: /images/infrastructure/Storage/hpe-alletra-mp/create-instance-type.png

   - From the GROUP section input the following:

      GROUP:
        Select the Group to add the Instance to
      CLOUD:
        Select the Cloud to add the Instance to
      NAME:
        Name of the Instance in |morpheus|

   - Select :guilabel:`NEXT`

   .. image:: /images/infrastructure/Storage/hpe-alletra-mp/create-instance-group.png

   - From the CONFIGURE section input the following:

      LAYOUT:
        Select the Layout to add the Instance to
      PLAN:
        Select the CPU Plan for the Instance
      RESOURCE POOL:
        Select the Resource Pool for the Instance
      VOLUMES:
        Add one or more Volumes to the Instance. Select the Datastore created in the Create Datastore section.
      NETWORK:
        Add Networks to the Instance
      IMAGE:
        Select the Image for the Instance
      HOST:
        Select the Host for the Instance

      Add additional configurations as needed

   .. image:: /images/infrastructure/Storage/hpe-alletra-mp/create-instance-configure.png

   - Select :guilabel:`NEXT`
   - Add Automation settings as needed
   - Select :guilabel:`NEXT`
   - Review the Instance configuration
   - Select :guilabel:`COMPLETE`

   .. image:: /images/infrastructure/Storage/hpe-alletra-mp/create-instance-review.png

The `Instance` will be provisioned and displayed in the `Instances` tab.

