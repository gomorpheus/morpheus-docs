.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. important:: |morphver| requires Elasticsearch v7.x. Please refer to :ref:`upgrading` and `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to |morphver| if your Appliance's Elasticsearch is external.

.. important:: v3.6.0 or later required to upgrade to |morphver|. Upgrading from v3.6.x to v4.2.0 contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x, a database backup is recommended due to MySQL version upgrade.

.. important:: It is recommend to upgrade existing VM and Host Agents after upgrading to |morphver| for Automation tasks with large task outputs/results when executing over |morpheus| Agent Command Bus.

New Features
============

Tag Enforcement and Compliance Policy
-------------------------------------

New Tag Policy Type with enforcement and compliance scanning added: `LINK <https://support.morpheusdata.com/s/article/How-to-work-with-cloud-tagging-policies?language=en_US>`_
 - A Tag Policy can be enforced both strictly (at provision time) as well as passively on supported clouds
 - A Tag Policy defines the relevant key to validate the presence of, as well as an optional Option List to validate valid values
 - Multiple Tag Policies can be combined to enforce a comprehensive Tag compliance program
 - Server detail pages show warnings if Tags are not compliant

.. note:: Tag Policy scanning and enforcement is currently supported only in Azure, Amazon, and VMware clouds.

.. image:: /images/administration/settings/policies/tagPolicy.jpeg
   :width: 60%

.. image:: /images/administration/settings/policies/tagComplianceWarning.jpeg
   :width: 80%

TAGS renamed to LABELS, METADATA renamed to TAGS
 In |morpheus| UI, TAGS have been renamed to LABELS and METADATA has been renamed to TAGS in all places where these fields appear, such as the Instance provisioning wizard, clone wizard, App wizard, Blueprint wizard, and perhaps other places. This change was made to align |morpheus| UI more closely with public cloud terminology.

.. note:: |morpheus| variables and API naming conventions have not been changed.

NSX Updates
-----------

- NSX Logical Router config : ``EXTERNAL NETWORK`` renamed to ``UPLINK NETWORK``
- Multi-network support added for Uplink and Internal Networks
- Uplink and Internal IP Addresses now specified per Network after adding via ``+``
- NSX Edge Gateway modal updated with Appliance, Interfaces, DNS Client and Routing configurations.
- NSX Firewall Rule modal updated with PROTOCOL specification.
- Status icons added to Logical Switch tab
- APPLICATION column added to Firewall tab
- :guilabel:`+ Create Rule` added to new ``v MORE`` dropdown per security group
- Group and Rule Icons added
- ``Appliance`` Config section added to NSX Logical Router creation
- Group permission added for new Networks and Edge Gateways/Routers
.. add link to network and group sections below

Role Permission Updates
-----------------------

Group Access level option added for Networks and Routers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*A user with ``Infrastructure: Networks: Group`` access permissions can:*

- Create shared Networks or assign to Group(s) the User has ``Full`` access to
- Manage Networks assigned to Group(s) the User has ``Full`` access to
- View and use Shared Networks (Group set to ``Shared`` in Network config)
- View Networks assigned to Group(s) the user has ``Read`` access to

*A user with ``Infrastructure: Network Routers: Group`` Access permissions can:*

- Create, Manage and use Routers assigned to Group(s) the user has ``Full`` access to
- View and use Shared Routers (Group set to ``Shared`` in Router config)
- View Routers assigned to Group(s) the user has ``Read`` access to

Feature Access permissions updates offer more granular access to Network Domains, Routers and Proxies:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Infrastructure: Network Domains (Access Levels: None/Read/Full)
- Infrastructure: Network IP Pools (Access Levels: None/Read/Full)
- Infrastructure: Network Proxies (Access Levels: None/Read/Full)
- Infrastructure: Network Routers (Access Levels: None/Read/Group/Full)
- Infrastructure: Networks (Access Levels: None/Read/Group/Full)

Added Network ``GROUP`` ownership setting: `LINK <https://support.morpheusdata.com/s/article/Working-with-Network-Group-ownership?language=en_US>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Available for Networks created in |morpheus|
- Relevant for users with ``Infrastructure: Networks: Group`` Role permissions
- If a Group is selected, only users with ``Infrastructure: Networks: Group`` Role Permission and Access to specified Group, or ``Infrastructure: Networks: Full`` Role Permission can Manage the Network.
- If "Shared" is selected, only users with ``Infrastructure: Networks: Full`` Role Permission can Manage the Network.

PXE Boot Menu section updates
-----------------------------

The PXE Boot Menu section in *Infrastructure > Boot > BOOT MENUS* has been updated for Boot Menu creation and management, the ability to set Root and Sub Menus, configure images, and answer file scoping: `LINK <https://docs.morpheusdata.com/en/4.2.0/infrastructure/pxeboot/pxeboot.html>`_

Boot Menu Creation with:

- Enabled flag
- Default Menu flag
- Root Menu Flag
- Boot Image scoping (optional)
- Answer File scoping (optional)
- Menu Content field
- Sub Menu(s) selection

System-seeded Boot Menus are displayed and user-created Boot Menus can be edited and deleted.

Jobs: Scheduled run-once executions
-----------------------------------

- Jobs can now be scheduled to execute once at a specified date and time: `LINK <https://docs.morpheusdata.com/en/4.2.0/provisioning/jobs/jobs.html#creating-jobs>`_

  .. image:: /images/provisioning/jobs/dateandtime_job.png
    :width: 60%

Kubernetes Updates
------------------
- Brownfield Kubernetes Cluster Support, create a new Cluster (Infrastructure > Clusters) with "External Kubernetes Cluster" type to bring an existing Kubernetes cluster into Morpheus: `LINK <https://support.morpheusdata.com/s/article/How-to-add-existing?language=en_US>`_
- Azure AKS Integration
- Reconfigure Action now available for Kubernetes Instances
- Create Cluster wizard (`Infrastructure > Clusters > + ADD CLUSTER`) now allows users to specify the number of worker nodes or the number of hosts for Kubernetes Clusters or Docker/KVM clusters, respectively

  .. image:: /images/infrastructure/clusters/workers_cluster_wizard.png
    :width: 60%

SCVMM: Discovered VM IP Address Sync
------------------------------------

- SCVMM cloud discovery now syncs in IP addresses for discovered VMs.

  .. note:: Inventory Existing setting must be enabled on SCVMM Cloud config

Google Cloud Platform (GCP) Enhancements
----------------------------------------

- API Proxy values can now be set under Advanced Options for GCP clouds (when creating a new integration or editing an existing one) as is already possible for other clouds: `LINK <https://docs.morpheusdata.com/en/4.2.0/integration_guides/Clouds/google/google.html#advanced-options>`_

vCloud Director (vCD) Enhancements
----------------------------------

The vCloud Director API version can now be specified in vCD Cloud configurations in the API VERSION field

  - To override system API version, enter version in API VERSION field (for example: ``31.0``)

AWS Security Token Service (STS) to AssumeRole
----------------------------------------------

- Now supports security token service to AssumeRole by entering AWS role ARN value when editing or integrating a new Amazon cloud

.. image:: /images/integration_guides/clouds/aws_role_arn.png
  :width: 60%

Policy Enhancements
-------------------

Policies: Network Quotas
^^^^^^^^^^^^^^^^^^^^^^^^

Network Quota Policies limit the number of Networks that can be created within the Policy's scope

- Once the quota is reached, Users will not be able to create additional Networks within the applicable Policy enforcement scope
- Scopes include:

  - Global
  - Tenant
  - Group
  - Cloud
  - Role
  - User

Policies: Router Quotas
^^^^^^^^^^^^^^^^^^^^^^^

Router Quota Policies limit the number of Routers that can be created within the Policy's scope.

- Once the quota limit is reached, Users will not be able to create additional Routers within the applicable Policy enforcement scope
- Scopes include:

  - Global
  - Tenant
  - Group
  - Cloud
  - Role
  - User

Tag Enhancements
----------------

VMware: Tag Enhancements
^^^^^^^^^^^^^^^^^^^^^^^^

- Post-Provision Tag additions, updates, and/or removals in |morpheus| on VMware Instances are now synced into VMware

Azure: Tag Enhancements
^^^^^^^^^^^^^^^^^^^^^^^

- Post-Provision Tag additions, updates, and/or removals in |morpheus| on Azure Instances are now synced into Azure

Cloud Datacenter Expansion
--------------------------

- IBM Cloud: Frankfurt 4 & 5 Datacenters now supported
- Softlayer: Frankfurt 4 & 5 Datacenters now supported

System Image Catalog Improvements
---------------------------------

- Ubuntu 18.04 Node Types have been added for the following Clouds: Upcloud, Azure, DigitalOcean, IBM, Oracle Cloud, Open Telekom, SoftLayer, vCD, SCVMM, Alibaba, Hyper-V, ESXi

Other Enhancements
------------------

- Workflows with a visibility value of "Public" are now viewable and executable by Tenants: `LINK <https://docs.morpheusdata.com/en/4.2.0/provisioning/automation/automation.html#add-workflow>`_
- Approvals (`Operations > Approvals`) can be sorted by DATE CREATED
- Recent Activity Report now displays impersonated User info. The Recent Activity Report (Operations > Activity) now shows "User as Impersonated User" for activity records from an impersonated User. Impersonations were previously shown in the Dashboard Activity section, as well as the Audit Log and UI Logs. They are now shown in the Recent Activity Report as well.
- CloudFormation: Improved conditional resource handling. When Conditional Resources fail to create when provisioning CloudFormation Instances or Apps, the resources are removed instead of remaining in |morpheus| as failed.
- Git and Github Integrations: HTTPS only auth support added
- Tasks: Git integration now exists for Groovy Script-type Automation Tasks
- Cloud-Init: Added support for hashing change passwords in target cloud-init data for any non-Ubuntu 14 based image (Ubuntu 14.04 restriction). Note: Dependent on Virtual Image OS type and version settings; ensure OS Type is accurately set.
- Removed a hard-coded message stating "You have logged out of |morpheus|." when users who were authenticated through a SAML integration logged out. This could cause confusion when using white-labeled |morpheus| Appliances.
- Removed a message stating "If supported by your identity provider and configuration, you have also been logged out of your identity provider" that appeared in some instances when logging out of |morpheus| through Identity Source authentication
- Fixed an issue where the HISTORY tab of an ARM Blueprint App detail page would only show deployment information if a VM resource was being deployed
- Creation of networks and routers are now asynchronous processes to improve performance and prevent modal timeout in some scenarios
- Updated |morpheus| installer to force a version of FreeRDP which is compatible with Guacd. CentOS/RHEL 7.7+ include FreeRDP 2.0 by default which is not compatible.
- Fixed an issue preventing a second router from being added to a |morpheus|-created Openstack network in certain scenarios

API Enhancements
================

CLI Enhancements
================

Security Enhancements
=====================

Fixes
=====
