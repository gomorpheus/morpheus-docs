Nutanix
-------

Overview
^^^^^^^^

Nutanix simplifies datacenter infrastructure by integrating server and storage resources allowing applications to run at scale. |morpheus| provides and avenue to enhance the Nutanix resources to allow efficient and seamless deployment of applications as a virtual machine (VM) or as a container on a Docker host.

Features
^^^^^^^^

* Virtual Machine Provisioning
* Containers
* Backups / Snapshots
* Resources Groups
* Migrations
* Auto Scaling
* Load Balancing
* Remote Console
* Periodic Synchronization
* Lifecycle Management and Resize

|morpheus| can provide a single pane of glass and self-service portal for managing multiple Nutanix Clusters and allowing the seamless deployment of applications.

.. Note:: Prism Central is not currently supported as a Cloud endpoint target

Getting Started
^^^^^^^^^^^^^^^

To get started this a few prerequisites must first be met.  The Nutanix cluster should be provisioned and available on the network. |morpheus| will look login to the Nutanix cluster with the Nutanix admin credentials and is typically located at the https://fqdn:9440 url.

Adding a Nutanix Cloud
^^^^^^^^^^^^^^^^^^^^^^^

The Nutanix cluster should be available and responding to the https://fqdn:9440 url for authentication by |morpheus| .

NAME
  Name of the Cloud in |morpheus|
CODE 
  Unique code used for api/cli, automation and policies.
LOCATION
  Description field for adding notes on the cloud, such as location.
VISIBILITY
  For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
TENANT
  If Visibility is set to Private, select the Tenant the Cloud resources will assigned to.
ENABLED
  When disabled, automatic Cloud sync is paused and the Cloud will not be selectable for provisioning. 
AUTOMATICALLY POWER ON VMS
  When enabled, Morpheus will maintain the expected powered on state of managed VM's and power on any managed VM's in the cloud that have been shut down for unknown reasons (not powered off by |morpheus|) to ensure availability of services. 
  
  .. note:: When "AUTOMATICALLY POWER ON VMS" is enabled, the power state of managed VM's should be maintained in |morpheus|. This setting is not applicable to discovered/unmanaged resources.

API URL
  URL of the Nutanix Prism API, example: https://10.30.21.220:9440. Prism Central is not currently supported as a Cloud endpoint target
USERNAME
  Nutanix admin username
PASSWORD
  Nutanix admin password
Inventory Existing Instances
  If enabled, existing Virtual Machines will be inventoried and appear as unmanaged Virtual Machines in |morpheus| .

.. include:: /integration_guides/Clouds/advanced_options.rst

Service Plans
^^^^^^^^^^^^^

A default set of Service Plans are created in |morpheus| for the VMware provisioning engine. These Service Plans can be considered akin to AWS Flavors or Openstack Flavors. They provide a means to set predefined tiers on memory, storage, cores, and cpu. Price tables can also be applied to these so estimated cost per virtual machine can be tracked as well as pricing for customers. By default, these options are fixed sizes but can be configured for dynamic sizing. A service plan can be configured to allow a custom user entry for memory, storage, or cpu. To configure this, simply edit an existing Service Plan tied to Nutanix or create a new one. These all can be easily managed from the Admin | Service Plans & Pricing section.

Docker
^^^^^^

So far this document has covered how to add the Nutanix cloud integration and has enabled users the ability to provision virtual machine based instances via the Add Instance catalog in Provisioning. Another great feature provided by |morpheus| out of the box is the ability to use Docker containers and even support multiple containers per Docker host. To do this a Docker Host must first be provisioned into Nutanix (multiple are needed when dealing with horizontal scaling scenarios).

To provision a Docker Host, simply navigate to the Cloud detail page or Infrastructure > Clusters section. From there click :guilabel:`+ ADD CLUSTER` to add a Nutanix Docker Host. |morpheus| views a Docker host just like any other Hypervisor with the caveat being that it is used for running containerized images instead of virtualized ones. Once a Docker Host is successfully provisioned a green checkmark will appear to the right of the host marking it as available for use. In the event of a failure click into the relevant host that failed and an error explaining the failure will be displayed in red at the top.

Some common error scenarios include network connectivity. For a Docker Host to function properly, it must be able to resolve the |morpheus| appliance url which can be configured in Admin Settings. If it is unable to resolve and negotiate with the appliance than the agent installation will fail and provisioning instructions will not be able to be issued to the host.

Snapshots
^^^^^^^^^

|morpheus| allows the ability to create a snapshot of a Nutanix instance.  From the instance detail page, simply select ``Actions -> Create Snapshot`` to begin creation of a new Snapshot.  Existing snapshots can be viewed in the ``BACKUPS`` tab on the instance detail page.  Snapshots taken outside |morpheus| will be synced every five minutes.  To revert to a previous snapshot, click on the revert icon located on the right side of the Snapshot. Snapshots can be deleted by clicking on the trash can icon.

.. Note:: Access to Snapshots can be limited or removed entirely for specific user roles as needed. To edit a role's Snapshots permissions, go to ``|AdmRol| > (Your selected role) > Snapshots``. Users can be given Full, Read-only, or No access.
