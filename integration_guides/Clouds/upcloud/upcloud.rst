UpCloud
-------

Overview
^^^^^^^^

UpCloud is a cloud hosting provider that offers both Linux and Windows virtual machines on their MAXIOPS infrastructure which is billed as I.A.A.S ( infrastructure-as-a-service ).
They have datacenters based in the UK, USA, Germany, Netherlands, Singapore and Finland. Servers can be created a lightning fast 45 seconds with their faster than SSD technology.

Features
^^^^^^^^

- Virtual Machine Provisioning
- Containers
- Backups / Snapshots
- Migrations
- Auto Scaling
- Load Balancing
- Remote Console
- Periodic Synchronization
- Lifecycle Management and Resize
- Inventory
- Cloudinit

Requirements
^^^^^^^^^^^^

An UpCloud User with API, Server and Storage permissions is required.

*To enable API access for a Main Account UpCloud User:*

#. Login to UpCloud
#. Select ``My Account -> User Accounts``
#. Select `Change` on the target user
#. Check the box for `API connections: Allow API connections from`
#. Under ``Access Permissions ->  Allow access to individual servers``, check the box for `User has control access to all servers`.
#. Under ``Access Permissions ->  Allow control access to individual storages``, check the box for `User has control access to all storages`
#. Save

*To Enable API, API, Server and Storage permissions for a SubAccount User:*

When creating or editing a Sub Account UpCloud user:

#. Check the box for `API connections: Allow API connections from`
#. Under ``Access Permissions ->  Allow access to individual servers``, check the box for `User has control access to all servers`.
#. Under ``Access Permissions ->  Allow control access to individual storages``, check the box for `User has control access to all storages`
#. Save

Adding an UpCloud Cloud
^^^^^^^^^^^^^^^^^^^^^^^

Configure
`````````

#. Navigate to ``Infrastructure -> Clouds``
#. Select :guilabel:`+ Create Cloud` Button
#. Select UpCloud from the Add Cloud modal
#. Select :guilabel:`NEXT`
#. Enter the following:

   .. include:: /integration_guides/Clouds/base_options.rst

   **Details**

   USERNAME
    UpCloud User Account Username
   PASSWORD
    UpCloud User Account Password
   ZONE
    Select UpCloud Datacenter to scope cloud to
   INVENTORY
    * *Off*: Existing UpCloud Servers will not be inventoried in |morpheus|
    * *Basic*: Existing Servers are Inventoried with Power state, Memory and Cores statistics synced.
    * *Full*: Existing Servers are Inventoried with Power state, Memory and Cores statistics, plus IP Addresses, Storage Info, and Console VNC Information.

   .. NOTE:: Full Inventory level recommended. Basic Inventory level can reduce Cloud Sync times when inventorying Datacenters with large amounts of servers. Credentials need to be added by editing the Virtual Machine in order to connect.

   The Cloud can now be added to a Group or configured with additional Advanced options.

   .. include:: /integration_guides/Clouds/advanced_options.rst

Group
`````

A Group must be specified or created for the new Cloud to be added to. Clouds can be added to additional Groups or removed from Groups after being created.

* *USE EXISTING*: Add the new Cloud to an exiting Group in |morpheus| .
* *CREATE NEW*: Creates a new Group in |morpheus| and adds the Cloud to the Group.

Review
``````

Confirm all settings are correct and select `COMPLETE`.

The UpCloud Cloud will be added, and |morpheus| will perform the initial cloud sync of:

* UpCloud Servers will added as Virtual Machines (if Inventory is enabled)
* UpCloud Templates (My Templates) will sync and be added to ```Provisioning -> Virtual Images``.

.. NOTE:: The Console tab will only appear for Inventoried Servers if Inventory Level is set to `Full`

Provisioning to UpCloud
^^^^^^^^^^^^^^^^^^^^^^^^

Instances and Apps can be created using the private Images synced from UpCloud or from the |morpheus| provided Image Catalog.

Provision a synced Image
^^^^^^^^^^^^^^^^^^^^^^^^

Images synced from UpCloud can be provisioned by using:

* The `UPCLOUD` Instance Type and selecting the Image from the Image dropdown in the configure section when provisioning and Instance, App, or creating an App Blueprint.
* Creating custom Library Instance Types and selecting a synced Image when creating a Node Type for the custom Instance Type.

.. IMPORTANT:: Synced images should be configured prior to provisioning by editing the Image in the `Provisioning -> Virtual Images` section.

Provision a |morpheus| provided UpCloud Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|morpheus| provides a number of pre-configured Images that are available in the default |morpheus| Catalog when provisioning and Instance, App, or creating an App Blueprint. UpCloud Images are included in the following Instance Types in the default |morpheus| catalog.

* ACTIVEMQ
* APACHE
* CASSANDRA
* DEBIAN
* ELASTICSEARCH
* GRAILS
* JAVA
* MONGO
* MYSQL
* NGINX
* PHP
* RABBITMQ
* REDIS
* OMCAT
* UBUNTU
* WINDOWS
* GRAILS
