Clouds
======

Overview
--------

Clouds are integrations or connections to public, private, hybrid clouds, or bare metal servers. Clouds can belong to many groups and contain many hosts. The clouds view includes clouds status, statistics, tenant assignment, and provides the option to add, edit, delete new clouds. |morpheus| supports most Public Clouds and Private Clouds.

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
* HPE OneView
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

Clouds can be added from `Infrastructure > Clouds` or in `Infrastructure > Groups > (select Group) > Clouds`. Individual Guides for adding specific Cloud Types can be found in the :ref:`integration-guide` section.

Cloud Detail View
-----------------

The Cloud Detail view shows metrics on health, sync status, current month costs, average monthly costs, resource utilization statistics, and resource counts for Container Hosts, Hypervisors, Bare Metal, Virtual Machines, and Unmanaged resources.

.. image:: /images/infrastructure/clouds/clouddetailview.png

To view the Cloud List View, select the name of a Cloud to display the clouds Detail View.

EDIT
  Edit the setup configuration of the Cloud.
REFRESH
  Force a sync with the Cloud. Depending on the Cloud, choose to force a standard Cloud sync (occurs every five minutes by default) or a nightly sync. When syncing Costing data, |morpheus| will force a pull of costing data for your specified period. If opting to "rebuild" the costing data, |morpheus| will delete all costing data from the Cloud for that period and attempt to rebuild the data by calling the Cloud API.
DELETE
  Delete the Cloud from |morpheus|

.. IMPORTANT:: All Instances and managed Hosts and VM's associated with the Cloud must be removed prior to deleting a cloud.

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
Load Balancers
  The load balancers tab panel displays available load balancers in the cloud including the name, description, type, cloud and host. You can add a load balancer from this tab by clicking :guilabel:`ADD LOAD BALANCER`.
Networks
  Displays Networks synced or added to the Cloud, including their name, type, CIDR, pool, DHCP status, visibility and targeted Tenant.
Data Stores
  Displays Datastores synced or added to the Cloud, including their name, type, capacity, online status, visibility, and targeted Tenant.
Resources
  Displays Resource Pools synced from the Cloud, including their name, description, and targeted Tenant.
Policies
  Manages Policies enforced on the Cloud. Setting a policy on this tab is equal to creating a policy in |AdmPol| and scoping it to the selected Cloud.
Profiles
  Manages |profileTypes| Profiles that create custom object associated secrets and metadata that will automatically be mapped per Cloud selection during provisioning and automation.

Deleting Clouds
---------------

To delete a cloud:

#. Select the Infrastructure link in the navigation bar.
#. Select the Clouds link in the sub navigation bar.
#. Click the Delete icon of the cloud to delete.

.. IMPORTANT:: All Instances, managed Hosts and VMs must be removed prior to deleting a Cloud. To remove Instances, hosts and VMs from |morpheus| without deleting the Cloud resources they represent, select Delete on the host or VM, unselect "Remove Infrastructure", and select "Remove Associated Instances" if Instance are associated with the selected Hosts or VMs.

|

.. include:: /infrastructure/clouds/profiles.rst
