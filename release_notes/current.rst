v4.1.0
======

.. important:: v3.6.0 or later required to upgrade to 4.1.0. Upgrading from v3.6.x to v4.x contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x a database backup is recommended due to MySQL version upgrade.

Highlights
----------

vRealize Orchestrator Integration (vRO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Syncs all available vRO workflows by category
- These workflows can also be chained easily into non-vRO workflows
- ``vRealize Orchestrator Workflow`` (vRO) Task Type added. Executes Workflow from any vRO integration. Parameter Body accepts JSON.

New Automation Task Types
^^^^^^^^^^^^^^^^^^^^^^^^^
- New ``Ansible Tower Job`` Task Type added. Executes a Job from any Ansible Tower integration with inventory, group, execution mode and target options.
- ``Email`` Task Type added. Sends email to specified address with defined subject and body upon successful workflow execution. Address, Subject and Body fields support variables, and body field supports html.
- ``vRealize Orchestrator Workflow`` (vRO) Task Type added. Executes Workflow from any vRO integration. Parameter Body accepts JSON.

Option Types & Lists Enhancements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- New ``Typeahead`` Option Type with multi-selection support. Presents an Option List in a typeahead field vs the dropdown selection list field in ``Select List`` types.
- New ``Morpheus API`` Option List type with Clouds, Groups, Instances, Instances Wiki, Servers and Servers Wiki object targets.
- New ``REQUEST SCRIPT`` field added to ``REST`` and ``Morpheus API`` option list settings. Create a js script to prepare the request. Return a data object as the body. The input data is provided as data and the result should be put on the global variable results.
- ``Select`` Option Type name changed to ``Select List``
- New ``DEPENDENT FIELD`` setting in ``Select List`` Option Types. Allows using results from a previous Option Type in a ``Select List`` Option List script. Data will reload when an associated dependent fields value is defined or changed.

Subnets
^^^^^^^
- Added `SUBNETS` tab to the network detail page in ``Infrastructure > Network > (Your specific Network)`` which allows subnets to be searched and edited.
- Subnets can now be created and edited on an Azure VNet from ``Infrastructure > Network``.
- Azure networks sync as subnets. Previously, subnets were synced as individual networks
- Network subnets can now be selected from the `Networks` dropdown list when provisioning an instance
- Group permissions can now be modified on subnets just like networks
- Subnet options are now respected just like networks in terms of visibility, group access, and defaults
- Subnets are now selectable when adding or editing a Network Group in ``Infrastructure > Network > NETWORK GROUPS``

Additional Changes and Improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Job executions can now be expanded to show process details in ``Provisioning > Automation > Executions``
- Individual tasks and scripts can now be run against hosts and virtual machines in ``Infrastructure > Hosts``. Previously workflows could be executed but not individual scripts or tasks.
- Clone system layouts in ``Provisioning > Library > CLUSTER LAYOUTS`` for use in custom layouts. Buttons to edit and delete existing custom layouts also appear alongside the clone button in the list view.
- Data Stores, History, and Logs tabs added to detail page for KVM clusters
- Setting to Reuse Sequence Numbers added to ``Administration > Provisioning``
- `VMWare on AWS` cloud type added to ``Infrastructure > Clouds``
- `User Data` field on images and clouds now supports YAML
- Kubernetes clusters can now be created in ``Infrastructure > Clusters > +ADD CLUSTER``
- Kubernetes blueprints can now be created in ``Provisioning > Blueprints``
- Metadata is now synced to vCenter to set tags on VMs. Existing tags are also inventoried into Morpheus as Metadata
- Static IP addresses can now be assigned on vCD cloud via Guest Customizations during instance provisioning
- `Morpheus Api` has been added as a type selection in Option Lists (``Provisioning > Library > OPTION LISTS``)
- ServiceNow integrations now allow for custom CMDB record mapping and give the user the ability to define the table that CMDB records are written to
- Listed datastores in wizards for SCVMM instances are now limited to those that make sense for the given host and resource pool rather than displaying all of them
- Listed datastore names for SCVMM instances (``Infrastructure > Clouds > DATASTORES``) are now prefixed with the host or cluster name for easier identification
- Amazon M5A and M5AD plans can now be selected when provisioning instances. In most cases, this requires a custom AMI due to this instance type not supporting Enhanced Networking (ENA)
- Stopped and started usage records are created appropriately for managed and unmanaged instances on each cloud sync when stopping or starting them outside of Morpheus
- `AUTOMATICALLY POWER ON VMS` checkbox added to add and edit cloud wizards (``Infrastructure > Clouds``). When checked, VMs will match the power state of the Morpheus instance
- Added support for Openstack Availability Zones
- Added Morpheus-provided catalog image for Ubuntu 18 on UpCloud

Fixes
-----
- Output results now appear correctly in the Execution Detail window in ``Provisioning > Automation > Executions``. Similarly, output results will also now appear correctly in the Execution Detail window in ``Provisioning > Jobs > Job Executions``.
- Fixed an issue where backups were not being created in some cases when integrating with Veeam 9.5
- Time period definitions within the specified dates are now honored in data calls to the Billing API
- Removing an instance or VM from Morpheus no longer removes serverExternalID and serverInternalID values from /api/billing records
- General improvements to Usage data
- Fixed an issue where the list of floating or elastic IP addresses available was not being immediately updated on some clouds when provisioning an instance and selecting an external IP pool for the floating IP pool
- Stopped and started usage records (``Operations > Activity > USAGE``) are no longer created when there is an error in calling the Azure API. In some cases this could cause interruptions in billing data.

.. API/CLI #Awaiting cli release
.. -------
.. API/CLI: Infrastructure > Clusters (Kubernetes) functionality added
.. API/CLI: Network Domain Records added
.. API/CLI: Network Pool IP management added
.. API/CLI: provision instances to docker & Kubernetes clusters

Service Version Compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When externalizing MySQL, Elasticsearch and/or RabbitMQ services, the following versions are compatible with Morpheus 4.1.0:

+---------------------------------------+----------------------+-----------------------------+
| **Service**                           |**Compatible Branch** | **4.1.0 Installed Version** |
+---------------------------------------+----------------------+-----------------------------+
| MySQL                                 | 5.7                  | 5.7.27                      |
+---------------------------------------+----------------------+-----------------------------+
| Elasticsearch: 5.6 (5.6.16 installed) | 5.6                  | 5.6.16                      |
+---------------------------------------+----------------------+-----------------------------+
| RabbitMQ: 3.7 (3.7.16 installed)      | 3.7                  | 3.7.16                      |
+---------------------------------------+----------------------+-----------------------------+

v4.0.0
======

Highlights
----------

Clusters & Kubernetes
^^^^^^^^^^^^^^^^^^^^^
New ``Infrastructure -> Clusters`` section
 - Cluster tab added to Cloud detail pages
 - Kubernetes Cluster provisioning
   - Rebuilt from the ground up, CNCF certified
 - Docker Cluster provisioning
   - New Clusters are automatically created for existing Docker Hosts
 - Amazon EKS Cluster provisioning
   - Kubernetes EKS 1.13 layout provided (note: Kubernetes Clusters can also be created in AWS EC2 using Kubernetes Cluster type)
 - KVM Cluster Provisioning
   - Spin up Morpheus KVM Clusters
Cluster List View
   - Create new Kubernetes, Morpheus Docker, and EKS clusters
   - Lists existing Clusters with Cluster Status, Cluster Type, Cluster Layout, Worker count, Cluster resource utilization stats, and actions including adding new worker nodes.
   - Edit, updated, disable, rename, and delete clusters
   - Cluster search field
Cluster Detail view
    - Cluster resource utilization statistics for compute, memory and storage
    - Total Cluster Costs (month to date)
    - Masters, Workers, Containers, Services, Jobs and Discovered containers stats
    - Summary, Namespaces, Masters, Workers, Services, Containers, Jobs, Volumes, Lobs, History and Wiki tabs
    - Easy access to Kubernetes API and Config via ``Actions``
    - Group, Tenant and Service Plan permissions per Cluster
    - Detailed Metadata and Status views for all Masters, Workers, Containers, Deployments and Pods (``i`` bubble)
    - Real-time process event history
New Blueprint Types
    - Kubernetes Blueprints
    - Helm Blueprints
Library: Spec Templates added
   - Kubernetes Spec, Helm Chart and Swarm Template Spec Template Types added
   - Kubernetes and Helm Spec Temples can be provisioned using the system Kubernetes Instance type, or added to Custom layouts
   - Code Repository, URL and Local sources supported
   - Terraform, ARM and CloudFormation Spec Template types also added
     - Allows provisioning of Terraform, ARM and CloudFormation templates as Instances
Library: Cluster Layouts added
   - Create your own Kubernetes, Docker, EKS and KVM Cluster Layouts using your own images and config

.. note:: Kubernetes Cluster provisioning is only supported in VMware, AWS, Azure, Openstack, Nutanix, vCloud Director, Xen, Google, IBM, Upcloud, Huawei, Digital Ocean, VMware Fusion, Hyper-V, and Open Telekom Cloud Cloud types

Automation Expansion
^^^^^^^^^^^^^^^^^^^^

Jobs
 - New ``Provisioning -> Jobs`` section with Jobs and Job Executions tabs
 - Task and Operational Workflow Job types
 - Execute Jobs on a schedule and/or manually.
 - Jobs can be associated with Instances, Servers, or have no |morpheus| resource association.
 - Job execution status, output and history in `Job Executions`` tab
Operational Workflows
 - New Workflow type: ``Operational Workflows``
   - Original Workflows renamed ``Provisioning Workflows``
 - Support Option Types for custom input during execution
 - Support Instance and Server execution contexts for resource config map support
 - Support executing on multiple Instances or Servers at once
 - Do not contain Phases for Tasks
 - Can be added to Jobs
Task Execution Targets and Contexts
 - Specify Local, Remote, or Resource for where a task will be executed from
 - Specify Instance, Server or no Context Type for resource config map support
 - Custom config option for adding custom config during execution (json)
- ``Run Task`` and ``Run Scripts`` added to Virtual Machines and Host Actions


Wiki
^^^^
- Main Wiki section is at ``Operations - Wiki``
- Wiki tabs are on Clouds, Groups, Instances, Hosts, VM's, Bare Metal, and Clusters.
- Additional Wiki Pages and Categories can be created from ``Operations - Wiki``.
- When a Wiki tab is populated, a Page is automatically added and accessible to ``Operations - Wiki``.
- Wiki's are per Tenant. There is no multi-tenant access to Wikis.
- The Wiki is accessible from the UI, CLI and API.
- RBAC controlled via the Operations: Wiki User and Tenant Role permission (None, Read and Full).
- Page updates contain Updated by User and Date stamps.
- Wiki pages can be searched from ``/operations/wiki`` or navigated from ``/operations/wiki-page/page-index``.

.. NOTE:: The Wiki replaces Notes. Notes are automatically migrated to corresponding Wiki pages when upgrading to 4.0.

Snapshots
^^^^^^^^^
- Snapshot action added for VMware and Nutanix Instances
- ``Create Snapshot`` added to Instance Actions
- Snapshots are listed in the ``Backups`` tab on Instance detail page (yes we get it, Snapshots are not Backups)
- Snapshot list shows Snapshot name, description, date created and status, and flags most current Snapshot
- Revert and delete actions per snapshot
- Brownfield sync of existing snapshots

Azure ARM Enhancements
^^^^^^^^^^^^^^^^^^^^^^
- Azure ARM deployment process output record from Azure now imported live into Morpheus, visible in App History tab
- Azure ARM deployments deployment records now retained in Azure
- Added 'Create new Resource Group' option for ARM deployments, to create a new RG per App deployment
- Azure ARM Templates API Version updated to latest

UI Navigation Updates
^^^^^^^^^^^^^^^^^^^^^
- ``Services`` section renamed to ``Tools``
- ``Migrations`` moved to Tools section
- ``Operations -> Usage`` moved to ``Operations -> Activity -> Usage``
- ``Operations -> Scheduling`` moved to ``Provisioning -> Automation -> Power Scheduling`` and ``Provisioning -> Automation -> Execute Scheduling``

SolarWinds
^^^^^^^^^^
- SolarWinds IPAM Integration added
- Network Pool sync. Network Pools can be set on networks in |morpheus| for automated IP allocation and record creation.
- Optional Network Pool allocation and record sync. ``Inventory Existing`` option syncs all individual ip's records and corresponding status. Inventory is not required for provisioning.
- Grid and list displays with IP record overlays and color coding for static, available, reserved and transient status.
- Manual IP Host record creation from Network Pool detail pages.

AWS Updates
^^^^^^^^^^^
- EKS Cluster integration added
- Security Groups can now be viewed and managed from Instance detail Network tab
- AWS GovCloud US East Region added

Role Permission Updates
^^^^^^^^^^^^^^^^^^^^^^^
- Infrastructure: Clusters (None, Read, Full)
- Operations: Wiki (None, Read, Full)
- Provisioning: Advanced Node Type Options (None, Full)
- Provisioning: Blueprints - Helm (None, Provision, Full)
- Provisioning: Blueprints - Kubernetes (None, Provision, Full)
- Provisioning: Instances (None, Read, User, Full)
- Provisioning: Job Executions (None, Read)
- Provisioning: Jobs (None, Read, Full)
- Provisioning: Scheduling - Execute (None, Read, Full)
- Provisioning: Scheduling - Power (None, Read, Full)
- Provisioning: Service Mesh (None, Read, User, Full)
- Snapshots (None, Read, Full)
- Tools: Archives (None, Read, Full)
- Tools: Cypher (None, Read, Full, Full Decrypted)
- Tools: Image Builder (None, Read, Full)
- Tools: Migrations (None, Read, Full)
