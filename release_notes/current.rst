v4.0.0
======

.. important:: v3.6.0 or later required to upgrade to 4.0.0. Upgrade steps have been changed. 4.0.0 contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to 4.0.0 Upgrade Requirements before upgrading, and BACKUP YOUR DATABASE before upgrade.

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

Other
^^^^^
- ``Download Agent Script`` added to VM Actions. Generates script for manual agent installs with appliance url and api key included
- Openstack-based Clouds - parallel provisioning added
- Instance/App Wizard: Service Ports and Dns Options merged
- Option for Cross-Tenant Naming Policies (sequence applies across tenants) added to ``Administration -> Provisioning``
- Migration wizard: new Ports component added
- vCloud Director: Network reconfigure added

.. important:: v3.6.0 or later required to upgrade to 4.0.0. Upgrade steps have been changed. 4.0.0 contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to 4.0.0 Upgrade Requirements before upgrading, and BACKUP YOUR DATABASE before upgrade.             
