.. _Release Notes:

*************************
|morphver| Release Notes
*************************

4.2.0 brings all of the new features and enhancements from the 4.1 Feature Branch to a LTS branch. Future versions of 4.2 will add additional capabilities, fixes, performance improvements and security enhancements to the existing feature set of 4.2.0, while net new Feature and changes to the platform will be added to the upcoming 4.3 Feature branch.

.. important:: |morphver| requires Elasticsearch v7.x. Please refer to :ref:`upgrading` and `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to |morphver| if your Appliance's Elasticsearch is external. As of 4.2.0, Ubuntu 14.04 is no longer supported, you must be running Ubuntu 16.04+.

.. important:: v3.6.0 or later required to upgrade to |morphver|. Upgrading from v3.6.x to v4.2.0 contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x, a database backup is recommended due to MySQL version upgrade.

.. important:: It is recommend to upgrade existing VM and Host Agents after upgrading to |morphver| for Automation tasks with large task outputs/results when executing over |morpheus| Agent Command Bus.

New Features
============

Tag Enforcement and Compliance Policy
-------------------------------------

New Tag Policy type with enforcement and compliance scanning added: `LINK <https://support.morpheusdata.com/s/article/How-to-work-with-cloud-tagging-policies?language=en_US>`_
 - A Tag Policy can be enforced both strictly (at provision time) as well as passively on supported clouds
 - A Tag Policy defines the relevant key to validate the presence of, as well as an optional Option List to validate valid values
 - Multiple Tag Policies can be combined to enforce a comprehensive Tag compliance program
 - Server detail pages show warnings if Tags are not compliant

.. note:: Tag Policy scanning and enforcement is currently supported only in Azure, Amazon, and VMware clouds.

.. image:: /images/administration/settings/policies/tagPolicy.jpeg
   :width: 60%

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
- CloudFormation: Improved conditional resource handling. When conditional resources fail to create when provisioning CloudFormation Instances or Apps, the resources are removed instead of remaining in |morpheus| as failed.
- Git and Github Integrations: HTTPS-only auth support added
- Tasks: Git integration now exists for Groovy Script and Python-type Automation Tasks
- Cloud-Init: Added support for hashing change passwords in target cloud-init data for any non-Ubuntu 14 based image (Ubuntu 14.04 restriction). This is dependent on Virtual Image OS type and version settings, ensure OS Type is accurately set.
- Removed a hard-coded message stating "You have logged out of |morpheus|." when users who were authenticated through a SAML integration logged out. This could cause confusion when using white-labeled |morpheus| Appliances.
- Removed a message stating "If supported by your identity provider and configuration, you have also been logged out of your identity provider" that appeared in some instances when logging out of |morpheus| through Identity Source authentication
- Fixed an issue where the HISTORY tab of an ARM Blueprint App detail page would only show deployment information if a VM resource was being deployed
- Creation of networks and routers are now asynchronous processes to improve performance and prevent modal timeout in some scenarios
- Updated |morpheus| installer to force a version of FreeRDP which is compatible with Guacd. CentOS/RHEL 7.7+ include FreeRDP 2.0 by default which is not compatible.
- Fixed an issue preventing a second router from being added to a |morpheus|-created Openstack network in certain scenarios
- Appliance: MySQL: Default value for ``max_allowed_packet`` set to ``5242880``
- Azure: ARM:  Added support for ``copyindex`` in the event template doesn't properly use ``copyIndex``
- NSX: Logical Switch creation: Given name is now appended onto end of Logical Switch/Network name
- Tasks: HTTP Task now does preemptive basic AUTH and parses variables in custom header values



API Enhancements
================

- API: ``Library - Cluster Layouts`` added
- API: ``Provisioning - Library`` updated
- API: ``Infrastructure - Network Routers`` added
- API: ``Infrastructure - Network Integrations`` added
- API: ``/servers`` and ``/servers/{server_id}`` calls now return the ``resourcePoolId`` and ``folderId`` properties for discovered VMware servers.
- API: Jobs: Point in Time (Date and Time) execution added.
  - ``dateTime`` scheduleMode added
  - ``dateTime`` | N | Date and Time to execute the job. Use UTC time in the format 2020-02-15T05:00:00Z. Required when scheduleMode is ``dateTime``.
- API: Clusters: Support for number of workers parameter added


.. API/CLI: instances update --created-by not working
.. API: Appliance Settings: cannot PUT json in the same format as GET returns for

.. CLI Enhancements
.. ================

.. Security Enhancements
.. =====================

.. Exposed Passwords in Logs
.. .[Security Issue DE771] Session Cookies are not marked Secure
.. Java Vulnerable in Elastic search on 4.1.2 Can you provide a recommendation for remediation and ensure this is addressed in 4.2?
.. patch MySQL

Fixes
=====

- Security Groups: Fixed possibility of synced private security groups listing in subtenants
- vCloud Director: Fixed Cloud sync status showing ``OK`` when sync was not successful
- vCloud Director: Fixes scenario where plan size changes in vCD were not detected on next sync, potentially causing restart warning on reconfigure to not display
- vCloud Director: Fixed issue with volume deletes on discovered server syncing, preventing usage record updates.
- Oracle VM: Fixed issues with intermittent provision failures in HA environments due to appliance in-memory cloud-init ISO config
- Instances: Groups Filter: Fixed issue listing all Groups in filter choices when more 100+ Groups exist
- Openstack Clouds: Fixed default tenant assignment of synced Routers upon cloud creation when cloud is assigned to sub-tenant
- Azure: Fixed usage records not updating when Morpheus Agent fails to install
- VMware: Fixed issue with Datastore placement calculations and error surfacing when creating 2+ VMware Instance copies
- NSX: Fixed issue with Logical Switch and Edge Gateway Tenant assignment on Logical Switches and Edge Gateways created inside a Subtenant
- NSX: Fixed issue with NSX Edge Gateway creation related to invalid Resource Pool specification
- NSX: Fixed network creation on synced DLRs
- NSX: Fixed secondary network creation on created DLRs
- Automation: Execute Scheduling: Fixed issues with deletion of Execution Schedules
- Kubernetes: Fixed issue when provisioning Hosts with insufficient memory
- vCloud Director: Windows: Fixed Agent Installation Script injection into Guest OS Customizations when Domain Join is enabled
- OTC: Added image deletion for failed image import service uploads
- Azure: SQL DBaaS: Added support database names that include spaces
- Convert to Managed: Fixed issue with Tenant visibility on Library Layouts when "Support Convert to Managed" is enabled
- vCloud Director: Fix removal of vApp when deleting an Instance in |morpheus| that has been stopped in vCD and vApp is in partially running state
- Tenants: Fixed issue when deleting a Tenant with existing Power Schedules
- Workflows: Fixed issue with Workflows with multiple Options Types displaying when second Option Type has no default value
- Openstack: Synced Private Network's type now displayed as ``Private Network`` instead of ``VLAN``
- Openstack Clouds: Fixed associated Load Balancer visibility not updating when Cloud visibility is changed from Public to Private
- Cisco ACI: Fixed issue with deleting Cisco ACI integrations
- Reports: Cloud-specific Tenant costing analytics report values fix
- Python Tasks: Fix for Python Tasks script and output size constraints
- Backups: Local Time value now displayed for latest date/time on Backup detail pages
- Backups: Backup List: Fixed ``All`` Status filter value displayed as as ``Undefined``
- Tenant Registration: Email sign-in link now links to Tenant URL/subdomain instead of Master Tenant base URL
- Tenants: Fixed issue where existing ``reference_data`` would prevent Tenant deletion
- Amazon/AWS: Fixed issue with detected Plan changes updating VM records but not Instance records
- Windows Execution: Fixed potential issue in HA environments related to Windows Agent websocket session ID, .NET not being good at random, and Spring
- VMware: Fixed 'Import As Image' session timeouts when OVF export takes longer than 20 minutes
- Policies: Security Banner: Fixed issues with Security Banner display for Subtenant login URLs
- Xen: Resolved issue where volume size changes in Xen were only reflected on Virtual Machine records, not Instance and Container records
- Networks: Fixed issue with custom Network updates not saving when no Tenants exist


.. ARM tags variable lookup bug
.. Plan X scoped to Tenant Y can be assigned to Tenant Z when assigning to discovered or updating existing compute_server records
.. CustomOptions.x typeahead vars not evaluating in prov wizard review pane
.. Network changes in Infrastructure -> Network doesnt work if there is no subtenant
.. Reports are only printing 1 page
.. Kubernetes Instance: Network - service mesh issues
.. Cluster Details: Kubernetes Volumes - error on delete
.. Kubernetes: Volumes - view modal doesn't load
.. Kubernetes Host: Reconfigure - not updating plan values
.. Cluster Add Node - naming issue with incrementing numbers
.. Cluster Details: Master/Workers - sort by name
.. Kubernetes Instance: Logs - not retrieving log data
.. Cluster Layouts: only displaying first 50 layouts (need pagination)
.. Cluster Provision: Combo - unable to provision
.. Cluster Layouts: issues with creating workers, node count, & priority
.. Cluster: Add Host - empty Cloud field
.. Kubernetes Instance: Catalog - Grails
.. Ansible Tower Task - not showing Errors
.. Kubernetes Cluster Layouts: workers shouldn't show up on Masters tab
.. Kubernetes Spec-Based App: delete doesn't complete
.. Cluster Add Host/Worker: cleanup field handling
.. Network modal - Improvements
.. Clusters: Delete - handle various options correctly
.. Kubernetes Instance: Add Node - not working
.. Kubernetes Spec-Based Apps: instance detail content issues
.. Cluster Provision: Kubernetes HA - load balancer selection doesnt work
.. Cluster Detail: cluster and host status issues
.. Kubernetes Instance: Catalog - Tomcat (deployments)
.. VCD - remove backup & clone actions
.. App Wizard: Review: CloudFormation: should display all Resources
.. Kubernetes Add Worker: should hide cluster related fields
.. Kubernetes: AKS/EKS - unable to delete cloud with sync'd in cluster
.. Kubernetes Instance: Service Mesh - not updating IP
.. API/CLI: Create Azure Subnet: failing with timeout, error
.. API: improve authorization validation
.. API: Network Pools/Domains/Proxies/Services: Create/Update syntax needs to be documented
.. API: Validation fails on certain app provisions
.. API: Provisioning > Library > Layouts: no signature of method error when updating version property
.. CLI: health alarms: not able to acknowledge unacknowledged alarms
.. Cloudformation InstanceType No Default Option
.. NSX-V - Firewall Issues
.. Policy: Router Quota - missing translation
.. Set default max_allowed_packet to 5M for MySQL
.. Subnets not being removed, no parent network
.. VMware: max_storage on instance and container not updated if associate compute_server volume size changes directly on cloud.
.. NSX-V: Sync Error
.. NSX-V: Transport Zone issues
.. NSX-V - do not log passwords
.. NSX-V: Firewall Group issues
.. NSX-V: Logical Switch issues
.. NSX-V: Logical Router issues
.. NSX-V: UI and Routing Issues
.. NSX-V: Firewall Rule issues
.. AWS CE: API error due to date range
.. Backup Jobs: duration for in-progress jobs inaccurate
.. Blueprint wiz & group access fields
.. Azure - Windows agent does not install when using ARM  Spec Template
.. Backups: cleanup on backup counts
.. Using a `$` in a MySQL alters password in config data
.. App Wizard: Policies: not bubbling up specific error on complete
.. Amazon ALB/ELB: issues with adding LBs
.. OTC/Huawei - surface provision failures
.. KVM instance showing healthy despite deleted VM
.. Backup status widget - wrong order
.. Image Builder - force hypervisor
.. ServiceNow: OracleVM - fail to provision
.. Kubernetes Blueprint from Spec: App Wizard: Review: should bubble up validation errors, Plan (Development Plan / Config) field not displaying
.. OTC Networks: type not consistent (private network or VLAN) across 3.6 and 4.0 versions
.. Nutanix Snapshots show up as 0kb
.. Amazon ALB: Scheme & VPC validation issues
.. Service Plans: can't save plan with manual type
.. Migrated Veeam Integration - can't delete
.. Network Router Detail: blank except for NSX firewall properties
.. Deleted Azure Plans sync new Plans, cause permission issues
.. String/label cleanup
.. SCVMM: Skip Agent Install being ignored on instance provisioning
.. ESXi VM Stop - log error
.. Amazon Servers: failing to delete because of server not empty error
.. Tenant Delete Error - Network Domain
.. Tenant Delete - doesnt work if Tenant has Operation Data (ie: amazon costing data)
.. Existing SAML sign-in error HTTP-Artifact
.. SQL Error in Logs
.. VM that wont delete
.. Google log spam
.. AWS: use root device mappings from AMI
.. Policies: "Auto-Approve Extensions" settings not saving
.. Router Details issues
.. SCVMM - dont provision to hypervisors that are offline
.. Network router wizard not filtering network service for selected router type
.. Disabling OTC / Huawei routers fails
.. Amazon costing service log error
.. ServiceNow: Docker Provisioning: not seeing docker hosts
.. Boot Menus for PXE are blank
.. Tenant Delete - can't delete with jobs/executions
.. A network read-only user should not be able to view the details of a network integration.
.. Logs: shouldn't log vSphere password
..
.. Kubernetes - exposed passwords in logs
.. Cloudformation Capability IAM Missing
