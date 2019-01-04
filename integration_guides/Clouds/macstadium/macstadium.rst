Mac Stadium
-----------

Overview
^^^^^^^^^^

MacStadium is a provider of enterprise-class hosting solutions for Apple Mac infrastructure. It can be used to deploy a hosted private cloud for large-scale CI/CD or even a single Mac mini to test an iOS app. It allows virtualized Mac build machines

Features
^^^^^^^^^

* Virtual Machine Provisioning
* Backups / Snapshots
* Resource Groups
* Datastores and DRS Clusters
* Distributed Switches
* Datacenter / Cluster scoping
* Brownfield VM management and migration
* VMware to VMware migrations
* VMDK/OVF image conversion support
* Hypervisor Remote Console
* Periodic Synchronization
* Veeam Backup Integration
* Lifecycle Management and Resize

On top of all these features, |morpheus| also adds additional features to VMware that do not exist out of the box to make it easier to manage in multi tenant environments as well as hybrid cloud environments:

* Cloud-Init Support
* VHD to VMDK Image Conversion
* QCOW2 to VMDK Image Conversion
* Multitenancy resource allocation
* Virtual Image management (Blueprints)
* Auto-scaling and recovery

.. include:: /integration_guides/Clouds/vmware/getting_started.rst
.. include:: /integration_guides/Clouds/vmware/docker.rst
.. include:: /integration_guides/Clouds/vmware/multitenancy.rst
.. include:: /integration_guides/Clouds/vmware/advanced.rst
