Role Permissions
----------------

.. NOTE:: Permission options for sub-tenant user roles will only list options permitted by the Tenant role applied to the sub-tenant. Sub-Tenant user roles permissions cannot exceed permissions set by the overriding Tenant Role.

User Role Permission Sections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FEATURE ACCESS
  Controls Tenant and User access level for sections and features in morpheus.
GROUP ACCESS
  Controls User access level for Groups. (Groups are not Multi-Tenant.)
CLOUD ACCESS
  Controls Sub-Tenant access level for Master Tenant publicly visible Clouds.
INSTANCE TYPE User only has access to Objects they have created/own.
  Controls Tenant and User access level for Instance Types.
BLUEPRINT ACCESS

Feature Access Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^
Feature Access settings control permissions for sections and objects in morpheus. Permission options include:

None
  Hidden or inaccessible for user
Read
  User can view but cannot edit or create
Full
  User has full access
User
  User can access Objects they have created or own.
Group
  User can access Objects assigned to or shared with Groups the User has access to.
Remote Console: Provisioned
  Remote Console tab will only appear after instance is successfully provisioned.
Remote Console: Auto Login
  RDP and SSH only, controls if user is auto-logged in to Remote Console or presented with login prompt.
Role Mappings
  Gives User Access to Role Mappings config in ``/admin/roles`` for configuring Identity Source Role Mappings without providing Access to other Identity Source configuration settings.

.. list-table:: **Feature Access Role Permission Options**
  :widths: auto
  :header-rows: 1

  * - Permission
    - None
    - Read
    - Full
    - User
    - Other
  * - Admin: Appliance Settings
    - ✔
    -
    - ✔
    -
    -
  * - Admin: Backup Settings
    - ✔
    - ✔
    - ✔
    -
    -
  * - Admin: Environment Settings
    - ✔
    -
    - ✔
    -
    -
  * - Admin: Identity Source
    - ✔
    -
    - ✔
    -
    - Role Mappings
  * - Admin: Integrations
    - ✔
    - ✔
    - ✔
    -
    -
  * - Admin: License Settings
    - ✔
    -
    - ✔
    -
    -
  * - Admin: Log Settings
    - ✔
    -
    - ✔
    -
    -
  * - Admin: Message of the day
    - ✔
    -
    - ✔
    -
    -
  * - Admin: Monitoring Settings
    - ✔
    -
    - ✔
    -
    -
  * - Admin: Policies
    - ✔
    - ✔
    - ✔
    -
    -
  * - Admin: Provisioning Settings
    - ✔
    -
    - ✔
    -
    -
  * - Admin: Roles
    - ✔
    - ✔
    - ✔
    -
    -
  * - Admin: Service Plans
    - ✔
    - ✔
    - ✔
    -
    -
  * - Admin: Tenant
    - ✔
    - ✔
    - ✔
    -
    -
  * - Admin: Tenant - Impersonate Users
    - ✔
    -
    - ✔
    -
    -
  * - Admin: Users
    - ✔
    - ✔
    - ✔
    -
    -
  * - Admin: Whitelabel Settings
    - ✔
    -
    - ✔
    -
    -
  * - API: Execution Request
    - ✔
    -
    - ✔
    -
    -
  * - Backups
    - ✔
    - ✔
    - ✔
    - ✔
    - View
  * - Backups: Integrations
    - ✔
    - ✔
    - ✔
    -
    -
  * - Backups: Services
    - ✔
    - ✔
    - ✔
    -
    -
  * - Billing:
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Boot
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Certificates
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Clouds
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Clusters
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Groups
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Hosts
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: KeyPairs
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Load Balancers
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Network Domains
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Network IP Pools
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Network Proxies
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Network Routers
    - ✔
    - ✔
    - ✔
    -
    - Group
  * - Infrastructure: Networks
    - ✔
    - ✔
    - ✔
    -
    - Group
  * - Infrastructure: Policies
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Security Groups
    - ✔
    -
    - ✔
    -
    -
  * - Infrastructure: State
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Storage
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Storage Browser
    - ✔
    - ✔
    - ✔
    -
    -
  * - Infrastructure: Trust Integrations
    - ✔
    - ✔
    - ✔
    -

    -
  * - Integrations: Ansible
    - ✔
    -
    - ✔
    -
    -
  * - Logs:
    - ✔
    - ✔
    - ✔
    - ✔
    -
  * - Monitoring:
    - ✔
    - ✔
    - ✔
    - ✔
    -
  * - Operations: Activity
    - ✔
    - ✔
    -
    -
    -
  * - Operations: Analytics
    - ✔
    - ✔
    - ✔
    -
    -
  * - Operations: Approvals
    - ✔
    - ✔
    - ✔
    -
    -
  * - Operations: Budgets
    - ✔
    - ✔
    - ✔
    -
    -
  * - Operations: Dashboard
    - ✔
    - ✔
    -
    -
    -
  * - Operations: Guidance
    - ✔
    - ✔
    - ✔
    -
    -
  * - Operations: Health
    - ✔
    - ✔
    -
    -
    -
  * - Operations: Reports
    - ✔
    - ✔
    - ✔
    -
    -
  * - Operations: Usage
    - ✔
    - ✔
    - ✔
    -
    -
  * - Operations: Wiki
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning Administrator
    - ✔
    -
    - ✔
    -
    -
  * - Provisioning: Advanced Node Type Option
    - ✔
    -
    - ✔
    -
    -
  * - Provisioning: Allow Force Delete:
    - ✔
    -
    - ✔
    -
    -
  * - Provisioning: Apps:
    - ✔
    - ✔
    - ✔
    - ✔
    -
  * - Provisioning: Automation Integrations
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Automation Services
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Blueprints
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Blueprints - ARM
    - ✔
    -
    - ✔
    -
    - Provision
  * - Provisioning: Blueprints - CloudFormation
    - ✔
    -
    - ✔
    -
    - Provision
  * - Provisioning: Blueprints - Helm
    - ✔
    -
    - ✔
    -
    - Provision
  * - Provisioning: Blueprints - Kubernetes
    - ✔
    -
    - ✔
    -
    - Provision
  * - Provisioning: Blueprints - Terraform
    - ✔
    -
    - ✔
    -
    - Provision
  * - Provisioning: Deployment Integrations
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Deployments
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Instances
    - ✔
    - ✔
    - ✔
    - ✔
    -
  * - Provisioning: Job Executions
    - ✔
    - ✔
    -
    -
    -
  * - Provisioning: Jobs
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Library
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Scheduling - Execute
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Scheduling - Power
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Service Mesh
    - ✔
    - ✔
    - ✔
    - ✔
    -
  * - Provisioning: Tasks
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Tasks - Script Engines
    - ✔
    -
    - ✔
    -
    -
  * - Provisioning: Thresholds
    - ✔
    - ✔
    - ✔
    -
    -
  * - Provisioning: Virtual Images
    - ✔
    - ✔
    - ✔
    -
    -
  * - Reconfigure Servers
    - ✔
    -
    - ✔
    -
    -
  * - Remote Console:
    - ✔
    -
    - ✔
    -
    - Provisioned
  * - Remote Console - Auto Login:
    -
    -
    -
    -
    - Yes/No
  * - Snapshots:
    - ✔
    - ✔
    - ✔
    -
    -
  * - Tools: Archives
    - ✔
    - ✔
    - ✔
    -
    -
  * - Tools: Cypher
    - ✔
    - ✔
    - ✔
    - ✔
    - Decrypted
  * - Tools: Image Builder
    - ✔
    - ✔
    - ✔
    -
    -
  * - Tools: Kubernetes  (Deprecated)
    - ✔
    - ✔
    - ✔
    - ✔
    -
  * - Tools: Migrations
    - ✔
    - ✔
    - ✔
    -
    -
