v4.0.0
======

Highlights
----------

Clusters & Kubernetes
^^^^^^^^^^^^^^^^^^^^^
New ``Infrastructure -> Clusters`` section
 - Cluster tab added to Cloud detail pages
 - New Clusters are automatically created for existing Docker Hosts
 - Kubernetes Cluster provisioning
   - Rebuilt from ground up to allow custom layouts and services
 - Docker Cluster provisioning
 - Amazon EKS Cluster provisioning
Cluster List View
   - Create new Kubernetes, Morpheus Docker, and EKS clusters
   - Lists existing Clusters with Cluster Status, Cluster Type, Cluster Layout, Worker count, Cluster resource utilization stats, and actions including adding new worker nodes.
   - Edit, updated, disable, rename, and delete clusters
   - Cluster search field
Cluster Detail view
    - Cluster resource utilization statistics for compute, memory and storage
    - Total Cluster Costs (month do date)
    - Masters, Workers, Containers, Services, Jobs and Discovered stats
    - Summary, Namespaces, Masters, Workers, Services, Containers, Jobs, Volumes, Lobs, History and Wiki tabs
    - Easy access to Kubernetes API and Config
    - Group, Tenant and Service Plan permissions per Cluster
    - Detailed Metadata and Status views for all Masters, Workers, Containers, Deployments and Pods
    - Real-time process event history
- Kubernetes Blueprints
- Helm Blueprints
- Library Spec Templates
- Kubernetes Cluster provisioning is supported in VMware, AWS, Openstack, Nutanix, vCloud Director, Xen, Google, Softlayer, Huawei, Digital Ocean, Fusion, Hyper-v, Open Telekom Cloud cloud types


Automation Expansion
^^^^^^^^^^^^^^^^^^^^^
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
- Network Pool sync. Polls are set on networks in |morpheus| for automated IP allocation and record creation.
- Optional network pool allocation record sync. ``Inventory Existing`` option syncs all individual ip's records and status, not required for provisioning.
- Grid and list displays with ip record overlays and color coding for static, available, reserved and transient status
- Manual record creation

AWS Updates
^^^^^^^^^^^
- EKS Cluster creation added
- Security Groups can now be viewed and managed from Instance detail Network tab
- AWS GovCloud US East Region added

Other
^^^^^
- ``Download Agent Script`` added to VM Actions. Generates script for manual agent installs with appliance url and api key included
- Openstack-based Clouds - parallel provisioning added
- Instance/App Wizard: Service Ports and Dns Options merged
- Option for Cross-Tenant Naming Policies (sequence applies across tenants) added to ``Administration -> Provisioning``
- Migration wizard: new Ports component added
- vCloud Director: Network reconfigure added
