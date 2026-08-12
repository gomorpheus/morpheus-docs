VMware vCenter
--------------

Overview
^^^^^^^^

VMware is a very common cloud integration choice supported by |morpheus| . They have provided a top notch virtualization solution and one might argue pioneered the virtualization space altogether. As such, many companies utilize this technology and all the features that come with it, so |morpheus| covers a broad feature set in vCenter.

Features
^^^^^^^^

* Virtual Machine Provisioning
* Backups / Snapshots
* Resource Groups
* Datastores and DRS Clusters
* Distributed Switches
* Affinity Groups
* Datacenter / Cluster scoping
* Brownfield VM management and migration
* VMware to VMware migrations
* VMDK/OVF image conversion support
* Hypervisor Remote Console
* Periodic Synchronization
* Veeam Backup Integration
* Lifecycle Management and Resize
* Metadata tag sync

For Windows 11 VMs with vTPM or other encrypted VMs, review the task-scoped **Cryptographic operations** guidance in `VMware Permissions`_ before enabling hypervisor console, clone, or migration workflows.

On top of all these features, |morpheus| also adds additional features to VMware that do not exist out of the box to make it easier to manage in multitenant environments as well as hybrid cloud environments:

* Cloud-Init Support
* VHD to VMDK Image Conversion
* QCOW2 to VMDK Image Conversion
* Multitenancy resource allocation
* Virtual Image management (Blueprints)
* Auto-scaling and recovery

VMware administrators adopting VM Essentials can use :doc:`/getting_started/guides/vmware_to_vme` to find the corresponding workflow for common inventory, provisioning, placement, networking, lifecycle, migration, console, and backup tasks.

.. include:: /integration_guides/Clouds/vmware/getting_started.rst
.. include:: /integration_guides/Clouds/vmware/docker.rst
.. include:: /integration_guides/Clouds/vmware/multitenancy.rst
.. include:: /integration_guides/Clouds/vmware/advanced.rst
.. include:: /integration_guides/Clouds/vmware/permissions.rst
.. include:: /integration_guides/Clouds/vmware/vmware_templates.rst
