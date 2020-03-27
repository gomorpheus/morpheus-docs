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

Other Enhancements
------------------

- Activty: Recent Activity Report now displays impersonated User info. The Recent Activity Report (Operations > Activity) now shows "User as Impersonated User" for activity records from an impersonated User. Impersonations were previously shown in the Dashboard Activity section, as well as the Audit Log and UI Logs. They are now shown in the Recent Activity Report as well.
- Appliance: MySQL: Default value for ``max_allowed_packet`` set to ``5242880``
- Approvals: Reversed default DATE CREATED sort order for Approvals in ``/operations/approvals``
- ARM: Added process output to history tab for non-VM resources
- Azure: ARM:  Added support for ``copyindex`` in the event template doesn't properly use ``copyIndex``
- Cloud-Init: Added support for hashing change passwords in target cloud-init data for any non-Ubuntu 14 based image (Ubuntu 14.04 restriction). This is dependent on Virtual Image OS type and version settings, ensure OS Type is accurately set.
- CloudFormation: Improved conditional resource handling. When conditional resources fail to create when provisioning CloudFormation Instances or Apps, the resources are removed instead of remaining in |morpheus| as failed.
- Console: Guacamole upgraded to v1.1.0 on Appliances running on CentOS/RHEL 7.x and Ubuntu 18.04 to add support for FreeRDP 2.0.
- Creation of networks and routers are now asynchronous processes to improve performance and prevent modal timeout in some scenarios
- Git and Github Integrations: HTTPS-only auth support added
- Google Cloud: API Proxy values can now be set under Advanced Options for GCP clouds (when creating a new integration or editing an existing one) as is already possible for other clouds: `LINK <https://docs.morpheusdata.com/en/4.2.0/integration_guides/Clouds/google/google.html#advanced-options>`_
- IBM Cloud: Frankfurt 4 & 5 Datacenters now supported
- NSX: Logical Switch creation: Given name is now appended onto end of Logical Switch/Network name
- Openstack: Added support for attaching multiple Routers to |morpheus|-created Openstack Networks
- Softlayer: Frankfurt 4 & 5 Datacenters now supported
- System Library: Ubuntu 18.04 Node Types have been added for the following Clouds: Upcloud, Azure, DigitalOcean, IBM, Oracle Cloud, Open Telekom, SoftLayer, vCD, SCVMM, Alibaba, Hyper-V, ESXi
- Tasks: Git integration now exists for Groovy Script-type Automation Tasks
- Workflows: Workflows with a visibility value of "Public" are now viewable and executable by Tenants: `LINK <https://docs.morpheusdata.com/en/4.2.0/provisioning/automation/automation.html#add-workflow>`_
.. - Removed a hard-coded message stating "You have logged out of |morpheus|." when users who were authenticated through a SAML integration logged out.
.. - Removed a message stating "If supported by your identity provider and configuration, you have also been logged out of your identity provider" that appeared in some instances when logging out of |morpheus| through Identity Source authentication

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

CLI Updates
===========

4.2.7
 Enhancements
  - New options --wrap and --all-fields for all list commands.
  - New option remote check --all that works just like remote check-all.
  - Updated command groups current to support --remote option.
4.2.4 - 4.2.6
 Fixes
  - Fixes for new invoices command.
4.2.3
 Enhancements
  - Updated command invoices to show more info and make --raw-data an option.
 Fixes
  - Fixed clouds add groups dropdown being limited to 25.
  - Fixed multiselect option types not working when passed in eg. --tenants "one, two"
4.2.2
 Enhancements
  - New command invoices
 Fixes
  - Fixed instances add requiring Library permission to fetch layout.
  - Fixed instances add requiring Clouds permission to fetch datastores.
  - Fixed instances add potential 500 error when retrieving datastores.

4.2.1
 Enhancements
  - New subcommand service-plans activate
 Fixes
  - Fixed 404 error when fetching layout seen when pointing at appliance versions older than 4.2. This change is to use /library instead of /libray/instance-types when for those resources.

4.2 - This release corresponds to the release of the Morpheus API version 4.2.
 Enhancements
  - New command network-routers
  - New option networks add --group
  - New options tasks add --source --url for task types that supporting file-content instead of script content. ie. Groovy and Python
  - Updated command tasks get with improved output format.
  - New command library-spec-templates
  - Updated commands library-option-types, library-option-lists by adding , library-scripts, and library-file-templates with prompting and standard option support.
  - New option library-instance-types add --option-types [x,y,z].
  - New option clusters add --worker-count N and clusters add-worker -n N
  - New option service-plans update --active.
  - Updated jobs add to support --schedule datetime --datetime DATE.
  - New option instances add --ports ARRAY and prompting for exposed ports.
 Fixes
  - Fixed tasks update --payload not being supported.
  - Fixed prices add and price-sets add prompts to match -O options
  - Fixed library-cluster-layouts add prompts to match -O options
  - Fixed cypher put not respecting --key and --value options

Fixes
=====

- Amazon/AWS: Fixed issue with detected Plan changes updating VM records but not Instance records
- Apps: App wizard validation fixes *
- ARM: Added support for ``"tags": "[variables('resourceTags')]``
- Automation: Execute Scheduling: Fixed issues with deletion of Execution Schedules
- Azure: Fixed usage records not updating when Morpheus Agent fails to install.
- Azure: SQL DBaaS: Added support Databases names that include spaces.
- Backups: Backup List: Fixed ``All`` Status filter value displayed as as ``Undefined``
- Backups: Local Time value now displayed for Latest date/time on Backup Detail
- Backups: Minor backend fix to ensure proper behavior when creating a backup ^
- Billing: Fixed an issue that caused datastore billing not to appear for managed vm's under specific conditions *
- Cisco ACI: Fixed issue with deleting Cisco ACI Integrations
- Convert to managed: Converted a variable data type from integer to long text which prevents an error in the ‘Convert to Managed’ process in certain scenarios *
- Convert to Managed: Fixed issue with Tenant visibility on Library Layouts when "Support Convert to managed" is enabled.
- EKS: Fixed Amazon EKS Service Plan seed issue when upgrading from v4.0.0 or prior *
- Instances: Groups Filter: Fixed issue listing all Groups in filter choices when more 100+ Groups exist.
- Kubernetes: Fixed issue when provisioning Hosts with insufficient memory
- Kubernetes: Service Mesh improvements
- Kubernetes: Fixed an issue preventing Kubernetes App Blueprint deployment ^
- Networks: Fixed error when editing Network Tenant access from the Networks list on the Cloud detail page *
- Networks: Fixed issue with Custom Network updates not saving when no Tenants exist
- NSX-V: Can now set default gateway (Logical Routers > Gateway) *
- NSX-V: Fixed an issue preventing the creation of firewall rules with source and destination *
- NSX-V: Fixed an issue where vNIC was not set on default routes for DLR and EDGE *
- NSX: Fixed issue with Logical Switch and Edge Gateway Tenant assignment on Logical Switches and Edge Gateways created inside a Subtenant.
- NSX: Fixed issue with NSX Edge Gateway creation related to invalid Resource Pool specification
- NSX: Fixed network creation on synced DLR's
- NSX: Fixed secondary network creation on created DLR's
- NSX: Updated NSX Network display names on the Instance provisioning wizard to make them prettier *
- Openstack Clouds:  Fixed associated Load Balancer visibility not updating when Cloud visibility is changed from Public to Private.
- Openstack Clouds: Fixed default tenant assignment of synced Routers upon cloud creation when cloud is assigned to sub-tenant.
- Openstack: Synced Private Networks' Type now displayed as ``Private Network`` instead of ``VLAN``
- Oracle VM: Fixed issues with intermittent provision failures in a HA environments due to appliance in-memory cloud-init ISO config.
- OTC: Added image deletion for failed image import service uploads.
- Policies: Security Banner: Fixed issues with Security Banner display for Subtenant Login URLs
- Provisioning: Fix for Typeahead Option Type variables not evaluating in Provisioning Wizard Review tab.
- Python Tasks: Fix for Python Tasks script and output size constraints
- Reports: Cloud-specific tenant costing analytics report values fix
- Reports: Updates for ``Print`` layout formatting
- Security Groups: Fixed possibility of synced private security groups listing in subtenants
- Tenant Registration: Email sign-in link now links to Tenant url/subdomain instead of Master Tenant base url.
- Tenants: Fixed issue when deleting a Tenant with existing Power Schedules
- Tenants: Fixed issues where existing ``reference_data`` would prevent Tenant deletion.
- vCloud Director: Fix removal of vApp when deleting an Instance in morpheus that has been stopped in vCD and vApp is in partially running state.
- vCloud Director: Fixed Cloud Sync Status showing ``OK`` when Cloud Sync was not successful
- vCloud Director: Fixed issue with volume deletes on discovered server syncing, preventing Usage Record updates.
- vCloud Director: Fixes scenario where plan size changes in vCD were not detected on next sync, potentially causing restart warning on reconfigure to not display.
- vCloud Director: Windows: Fixed Agent Installation Script injection into Guest OS Customizations when Domain Join is enabled
- VMware: Fixed 'Import As Image' session timeouts when ovf export takes longer than 20 minutes.
- VMware: Fixed issue with Datastore placement calculations and error surfacing when creating 2+ VMware Instance copies.
- Windows Execution: Fixed potential issue in HA Environments related to Windows Agent websocket session ID, .net not being good at random, and Spring.
- Workflows: Fixed issue with Workflows with Multiple Options Types displaying when 2nd Option Type has no default value.
- Xen: Resolved issue where volume size changes in Xen were only reflected on Virtual Machine records, not Instance and Container records.


CVEs Addressed
==============

- CVE-2019-17563 *
- CVE-2019-17569 *
- CVE-2020-1935 *
- CVE-2020-1938 *
- CVE-2019-20372 *

Services
========

- NGINX updated to 1.17.9
- Tomcat updated to 9.0.33

(* Found in v4.2.0-2; ^ Found in v4.2.0-3)
