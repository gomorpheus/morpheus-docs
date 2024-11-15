Clouds
======

Overview
--------

In |morpheus|, a Cloud represents a grouping of |clusters| (referred to as a "Private Cloud") or an integration with a VMware vCenter appliance. This section describes general information about the Clouds construct and UI pages for Clouds. See the VMware integration guide for more specific details on integrating with VMware and the features supported by |morpheus|.

.. rst-class:: hidden
  Supported Cloud Types
  ^^^^^^^^^^^^^^^^^^^^^

  * Alibaba Cloud
  * Amazon
  * Azure (Public)
  * Azure Stack (Private)
  * Canonical MaaS
  * Cloud Foundry
  * Dell (Cloud type for PXE and manually added Dell EMC Hosts)
  * DigitalOcean
  * Google Cloud
  * HPE (Cloud type for PXE and manually added HPE Hosts)
  * Huawei
  * Hyper-V
  * IBM Cloud
  * IBM Cloud Platform
  * Kubernetes
  * MacStadium
  * Morpheus (Generic Cloud type for PXE/Bare Metal and manually added Hosts)
  * Nutanix
  * Open Telekom Cloud
  * OpenStack
  * Oracle Public Cloud
  * Oracle VM
  * Platform 9
  * SCVMM
  * Supermicro (Cloud type for PXE and manually added Supermicro Hosts)
  * UCS
  * UpCloud
  * vCloud Air (OVH)
  * VMWare ESXi
  * VMware Fusion
  * VMWare on AWS
  * VMware vCenter
  * VMware vCloud Director
  * XenServer

  Information on each cloud type can be found in the :ref:`integration-guide` section.

Creating Clouds
---------------

Clouds can be added from |InfClo| or in |InfGro| > (selected Group) > Clouds. A more detailed guide to adding a VMware vCenter Cloud can be found in the vCenter integration guide. The other available Cloud type, known as Private Cloud, is a generic Cloud type that doesn't directly integrate with any other technology as the vCenter Cloud type does. Instead Private Cloud-type Clouds are used to house your |clusters|. Make as many Private Cloud-type Clouds as needed to organize your |clusters| properly.

Cloud Detail View
-----------------

The Cloud Detail view shows metrics on health, sync status, resource utilization statistics, and resource counts for hosts, virtual machines, or any other constructs under the umbrella of the selected Cloud.

From the Cloud list page, select the name of a Cloud to display that Cloud's detail page. You'll notice the following actions are available:

EDIT
  Edit the setup configuration of the Cloud.
REFRESH
  Force a sync with the Cloud.
DELETE
  Delete the Cloud from |morpheus|.

.. IMPORTANT:: All Instances, managed Hosts, and VMs associated with the Cloud must be removed prior to deleting a Cloud.

Cloud Detail Tabs
^^^^^^^^^^^^^^^^^

.. NOTE:: Not all tabs are available for all Cloud Types.

Clusters
  The Clusters tab displays clusters provisioned into the Cloud being viewed, including their status, type, name, layout, workers, and compute, memory, and storage stats. You can add a cluster by clicking :guilabel:`ADD CLUSTER`.
Hosts
  The Hosts tab displays available hosts in the Cloud and displays power, OS, name, type, cloud, IP address, nodes, disk space, memory, and status. You can add a resource by clicking :guilabel:`ADD RESOURCE`, add a hypervisor host by clicking :guilabel:`ADD HYPERVISOR`, or perform action an action by selecting one or more Hosts and clicking :guilabel:`ACTIONS`.
 VMs
  Displays an inventory of existing Instances in your Cloud configuration and provides details such as power, OS, name, type, cloud, IP address, nodes, disk space, memory, and status.
Bare Metal
  Setup PXE Boot in the Boot section to add bare metal servers. Once set up you can view information such as power, OS, name, type, cloud, IP address, nodes, disk space, memory, and status.
Security Groups
  The Security Groups tab displays a list of existing security groups in the cloud. You can add a security group to this cloud by clicking :guilabel:`EDIT SECURITY GROUPS`.
Networks
  Displays Networks synced or added to the Cloud, including their name, type, CIDR, pool, DHCP status, visibility and targeted Tenant.
Data Stores
  Displays Datastores synced or added to the Cloud, including their name, type, capacity, online status, visibility, and targeted Tenant.
Resources
  Displays Resource Pools synced from the Cloud, including their name, description, and targeted Tenant.

Deleting Clouds
---------------

To delete a Cloud:

#. Select the Infrastructure link in the navigation bar.
#. Select the Clouds link in the sub navigation bar.
#. Click the Delete icon of the cloud to delete.

.. IMPORTANT:: All Instances, managed Hosts and VMs must be removed prior to deleting a Cloud.

|

.. rst-class:: hidden
  .. include:: /infrastructure/clouds/profiles.rst
