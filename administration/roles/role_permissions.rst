Role Permissions
----------------

.. NOTE:: Permission options for sub-tenant user roles will only list options permitted by the Tenant role applied to the sub-tenant. Sub-Tenant user roles permissions cannot exceed permissions set by the overriding Tenant Role.

User Role Permission Sections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Features
  Controls User access level for UI sections and features in |morpheus|. The complete feature permissions grid is included below.
Groups
  Controls User access level for Groups. Groups are not a Multi-Tenant construct, only Groups created in the current Tenant will be visible.
Instance Types
  Controls User access level for Instance Types. Only Instance Types created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.
Blueprints
  Controls User access level for Blueprints during App provisioning. Only Blueprints created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.
Report Types
  Controls User access for each report type in the Reports section (|OpeRep|). The user must also have Operations: Reports access granted under the Feature permissions tab.
Personas
  Controls User access to |morpheus| Personas, at the time of this writing Users may be given access to the Standard (full |morpheus| experience), Virtual Desktop (VDI), or Service Catalog Personas
Catalog Item Types
  Controls User access to Catalog Item types within the Service Catalog Persona. Only Catalog Items created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.
VDI Pools
  Controls User access to VDI Pools which are currently configured (|TooVDI|) via the Virtual Desktops Persona view

Tenant Role Permission Sections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Features
  Controls Tenant access level for sections and features in |morpheus|. The complete feature permissions grid is included below.
Clouds
  Controls Tenant access level for Clouds. This list includes Clouds integrated from the Master Tenant and shared publicly. Tenants given this Tenant Role will have either Full, Read, or None access levels to a given Cloud. See the section below for more information on Cloud Access levels.
Instance Types
  Controls Tenant access level for Instance Types. Only Instance Types created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.
Blueprints
  Controls Tenant access level for Blueprints during App provisioning. Only Blueprints created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.
Report Types
  Controls Tenant access for each report type in the Reports section (|OpeRep|). The Tenant must also have Operations: Reports access granted under the Feature permissions tab.
Personas
  Controls Tenant access to |morpheus| Personas, at the time of this writing Users may be given access to the Standard (full |morpheus| experience) or Service Catalog Personas
Catalog Item Types
  Controls Tenant access to Catalog Item types within the Service Catalog Persona. Only Catalog Items created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.
VDI Pools
  Controls Tenant access to VDI Pools which are currently configured (|TooVDI|) via the Virtual Desktops Persona view

Cloud Access Levels
^^^^^^^^^^^^^^^^^^^

When creating or editing a Tenant Role, Master Tenant administrators can choose which publicly-visible Clouds to share with Tenants having the current Role. Access can be completely restricted or administrators can choose between Read and Full access.

Read Access
```````````

Master Tenant administrators can opt to give other Tenants read-level access to any integrated Clouds through the Tenant Role. A read-only Cloud allows the Master Tenant to assign resources for viewing by Subtenant users but not allow them to perform any actions or provision new Instances.

With read-level access, Subtenant users will have access to the Cloud detail page (|InfClo|). From the Summary subtab on the Cloud detail page, high-level information on Cloud resources are shown regardless of specific resources that have been shared with the Subtenant. Other metrics, such as costing, resource percentages (CPU, Memory, and Storage), VM counts and host counts will only be populated when servers in the Cloud have been assigned to the Tenant.

Full Access
```````````

With full access, Subtenant users also have access to the Cloud detail page (|InfClo| > Specific Cloud) and see the same level of detail as Subtenants with read-only rights. However, with full access, Subtenant users can also perform many actions including the addition of Clusters, Hosts, and VMs, changing networks, and more. This cloud will also be selectable as a provisioning target for Subtenant users when deploying Instances or Apps.

Feature Access Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^
Feature Access settings control permissions for sections and objects in |morpheus|. Permission options include:

None
  Hidden or inaccessible for user
Read
  User can view but cannot edit or create
Full
  User has full access
User
  User can access Objects they have created or own
Group
  User can access Objects assigned to or shared with Groups the User has access to
Remote Console: Provisioned
  Remote Console tab will only appear after instance is successfully provisioned.
Remote Console: Auto Login
  RDP and SSH only, controls if user is auto-logged in to Remote Console or presented with login prompt.
Role Mappings
  Gives User Access to Role Mappings config in ``/admin/roles`` for configuring Identity Source Role Mappings without providing Access to other Identity Source configuration settings.

- .. toggle-header:: :header: **Admin Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Admin: Ansible
        - None, Full
        - Allows or disallows the ability to edit existing Ansible integrations
        - Ansible integrations are shown on the Integrations list page (|AdmInt|). Users with access may view and edit them here.
        - This permission is recommended for those responsible for administering |morpheus|, including creating integrations with third-party technologies, specifically Ansible
        -
      * - Admin: Appliance Settings
        - None, Full
        - Allows or disallows access to the Appliance and License tabs in |AdmSet|
        - The Appliance tab in |AdmSet| is where |morpheus| administrators would configure the appliance URL, Tenant and User management, email, proxy, and currency settings. Additionally, defining which Clouds are available for integration within |morpheus| is done on this page. On the License tab information about the current |morpheus| license may be viewed and a new license may be applied when needed.
        - This permission is recommended to only be assigned to Roles utilized within the Master Tenant. Those responsible for configuring currency, email, and proxy settings for Cloud API access will need this permission.
        - This permission is recommended to be set to None on the Tenant Role to restrict this access for all Subtenant Users.
      * - Admin: Backup Settings
        - None, Full
        - Allows or disallows access to |AdmSetBac|. Master Tenant administrators have additional settings for appliance backups and defaults on this page.
        - The Backup Settings page is where users define the default |morpheus| backup bucket, backup schedule, and retention count. Additionally, if given to a Master Tenant user they will have the ability to enable scheduled backups, create backups, and backup appliance.
        - This permission is recommended for those responsible for enabling backups and setting default backup buckets within |morpheus|.
        -
      * - Admin: Clients
        - None, Full
        - Allows or disallows access to the Clients tab in global settings (|AdmSet|)
        - The Clients settings section is where API clients are created and edited. Default clients may have their validity and refresh periods edited but cannot be deleted. User-created API clients may be edited or deleted
        - This permission is recommended for those responsible for administering API access.
        -
      * - Admin: Distributed Workers
        - None, Full
        - Allows or disallows access to |AdmInt| > Distributed Workers Tab
        -
        -
        -
      * - Admin: Environment Settings
        - None, Full
        - Allows or disallows access to the Environments tab in |AdmSetPro|. When given to a Master Tenant user they may define the visibility of the environment to either private or public.  When given to a Subtenant user the environments are only visible to the subtenant (private).
        - The Environments tab is where named environments such as development or production are created and given a description as well as a code for use within the API. A display order and visibility is also set.
        - This permission is recommended for those responsible for defining environments that will be available to select at provision time whether they are the Master Tenant or Subtenant users.
        -
      * - Admin: Guidance Settings
        - None, Full
        - Allows or disallows access to the Guidance tab in |AdmSet|
        - The Guidance tab controls global thresholds for |morpheus| guidance recommendations
        - This permission is recommended for those responsible for cost and resource management
        -
      * - Admin: Health
        - None, Read
        - Determines access to the |AdmHea| page, including the |morpheus| Health and |morpheus| Logs tabs.
        - The Health pages provide an overview of |morpheus| health, notifications from integrations, and the current |morpheus|-ui log.
        - This permission is recommended for those responsible for administering and troubleshooting |morpheus|.
        - This permission is recommended to be set to None on the Tenant Role to restrict access for Subtenant users.
      * - Admin: Identity Source
        - None, Role Mappings, Full
        - Allows or disallows access to create, edit, or delete integrated Identity Sources associated with subtenants. The "Role Mappings" option allows the user to edit role mappings without seeing higher level details about the integration itself (such as server IP addresses and admin usernames).
        - The Identity Sources page associated with the selected Tenant allows for creating, editing, and removing of identity sources in addition to configuring role mapping between |morpheus| and the identity provider.
        - Full permission is recommended for those responsible for integrating |morpheus| with Identity Providers. Role Mapping permission is recommended for those responsible for Role Based Access Control (RBAC).
        - This permission is recommended to be set to None for any subtenant user roles via use of a Tenant Role unless they manage their own RBAC.
      * - Admin: Integrations
        - None, Read, Full
        - This allows or disallows full or read access to |AdmInt|.
        - The Administration Integrations tab is where many new or existing integration types can be configured. These include Chef, Puppet, Ansible, Salt Master, Ansible Tower, vRealize Orchestrator, Microsoft DNS, PowerDNS, Route 53, Git, GitHub, Docker, Jenkins, ServiceNow, Cherwell, Remedy, ACI, and Venafi.
        - This permission is recommended for those responsible for the integration between |morpheus| and integrated technologies.
        -
      * - Admin: License Settings
        - None, Full
        - Allows or disallows access to the Licenses tab in |AdmSetPro|. When given to a Master Tenant user they may define specific subtenants in which the licenses may be used.
        - The Licenses tab is where software licenses may be added for tracking in |morpheus|. |morpheus| may then be configured to apply these licenses on provision. Currently, only Windows license types are available.
        - This permission is recommended for those responsible for managing Windows licenses.
        -
      * - Admin: Log Settings
        - None, Full
        - Allows or disallows access to the |AdmSetLog|.
        - The Logs page is where logs are enabled. Syslog forwarding rules are also configured here.
        - This permission is recommended for those responsible for configuring |morpheus| log settings and integrations.
        - This permission is recommended to be set to None in the Tenant Role to restrict this access to Subtenant Users.
      * - Admin: Message of the day
        - None, Full
        - Allows or disallows access to create and edit Message of the Day policies in |AdmPol|
        - The Policies page is where policies are defined. When creating a policy, users can select "Message of the Day" from the TYPE dropdown with this permission set to Full.
        - This permission is recommended for those responsible for publishing the Message of the Day.
        - This permission is recommended to be set to None in the Tenant Role to restrict this access from Subtenant Users.
      * - Admin: Monitoring Settings
        - None, Full
        - Allows or disallows access to |AdmSetMon|
        - The monitoring settings page is where |morpheus| monitoring and monitoring integrations are configured.  Available integrations are AppDynamics, ServiceNow, and New Relic. Monitoring checks can be turned on or off, and availability time frame, check interval period, and reported availability precision are also configured on this page.
        - This permission is recommended for those responsible for configuring |morpheus| monitoring settings and integrations.
        - This permission is recommended to be set to None in the Tenant Role to restrict this access from Subtenant Users.
      * - Admin: Packages
        - None, Full
        - Allows or disallows access to the Packages tab on the Integrations page (|AdmInt|)
        - The Plugins tab is where custom library packages (mpg) are added.
        - This permission is recommended for those responsible for managing the Library.
        - This permission is recommended to be set to None in the Tenant Role to restrict this access from Subtenant Users.
      * - Admin: Plugins
        - None, Full
        - Allows or disallows access to the Plugins tab on the Integrations page (|AdmInt|)
        - The Plugins tab is where custom plugins are added to extend |morpheus| functionality.
        - This permission is recommended for those responsible for extending |morpheus| functionality through custom plugins.
        - This permission is recommended to be set to None in the Tenant Role to restrict this access from Subtenant Users.
      * - Admin: Policies
        - None, Read, Full
        - This setting determines the level of access to |AdmPol|. When given to a Master Tenant user the ability to define Global policies and associate them with one or many Subtenants is granted.  When given to a Subtenant user, a global policy applies only to their subtenant.
        - The Policies page is where policies are defined. On create, the type of policy is selected, a name, description, and scope are defined.
        - This permission is recommended for those responsible for configuring and managing policies either at the Master Tenant or Subtenant.
        -
      * - Admin: Profiles
        - none,read,full
        - Allows or disallows access to Profiles (|profileObjects|)
        - Profiles are where |profileTypes| profiles are created and managed.
        - This permission is recommended for those responsible for managing secrets and other metadata that needs to be accessed by provisioning and automation processes.
        -
      * - Admin: Provisioning Settings
        - None, Full
        - Allows or disallows access to the Settings tab of the |AdmSetPro| page.
        - The Settings tab is where global provisioning settings are configured. For Master Tenant users, these include allowing Cloud selection, allowing host selection, requiring environment selection, showing pricing, hiding datastore stats on selection, cross-Tenant naming policies, and reusing naming sequence numbers. For both Master Tenant and Subtenant users, defining the deploy archive store, cloud-init setting, the PXE boot root password, and default App Blueprint types are available.
        - This permission is recommended to only be assigned to roles utilized within the Master Tenant.
        -
      * - Admin: Roles
        - None, Read, Full
        - This setting determines access to the |AdmRol| page. When given to a Subtenant user, the ability to create user roles is granted.  When given to a Master Tenant user, the ability to create and manage Tenant and Multi-Tenant Users roles is also granted.
        - The Roles page is where roles are defined. On create, a name and description are defined. Once created, the Role is accessed and feature access, Group access, Instance Type access and Blueprint access may be configured.
        - This permission is recommended for those responsible for configuring Role Based Access Control (RBAC) either globally or within their Subtenant.
        -
      * - Admin: Service Plans
        - None, Read, Full
        - This setting determines access to |AdmPla|. When given to a Subtenant user, access to the Plans tab is granted. When given to a user in the Master Tenant, the Price Sets and Prices tabs are also available.
        - The Plans tab is where service plans are defined. On create, a name and code (for API) are defined, display order, provisioning type, storage, memory, core count and the price may be configured. Additionally, the actions menu will allow group access to be scoped.
        - This permission is recommended for those responsible for defining and managing pricing and applying plans.
        -
      * - Admin: Tenant
        - None, Read, Full
        - This setting determines access to the |AdmTen| page. With this permission, local users may be created or deleted within each Tenant. Critical Note: Granting this permission to Subtenant users will expose all Tenants and Tenant users to the Subtenant.
        - The Tenant page is where all Tenants may be viewed, edited, created, or even deleted.
        - This permission is recommended to only be assigned to Roles utilized within the Master Tenant who are responsible for the creation, configuration, and/or deletion of Subtenants.
        - It is recommended this setting be set to None on the Tenant Role to restrict access for Subtenant users.
      * - Admin: Tenant - Impersonate Users
        - None, Full
        - This setting allows or disallows access to impersonate users. This selection is located on the |AdmUse| page in the Actions menu. When set to Full, Impersonate selection is available.
        - This permission allows for users in the Master Tenant to impersonate users of the Master Tenant and Subtenants.
        - This permission is recommended to be assigned only to Roles utilized within the Master Tenant who are responsible for configuring RBAC or for supporting users.
        - It is recommended this setting be set to None on the Tenant Role to restrict access for Subtenant users.
      * - Admin: Users
        - None, Read, Full
        - This setting determines access to the |AdmUse| page (both Users and User Groups tabs). User Roles can also be set or edited when creating or editing a User on this page. Note: A Master Tenant user with the Admin: Tenants (Full) permission may also access and perform user management from the associated Tenant page.
        - The User tab is where all users may be viewed, edited, created, or even deleted. The User Groups tab is where User Groups may be viewed, edited, created, or even deleted. Within |morpheus|, a User Group may be selected during provisioning in order to add each group member's credentials to an Instance. When creating a User Group a name, description, server group (in Linux, name of the group to assign members), sudo access toggle, and a list of users are defined.
        - This permission is recommended for those responsible for managing users and RBAC.
        -
      * - Admin: Whitelabel Settings
        - None, Full
        - Allows or disallows access to the Whitelabel tab in |AdmSet|.
        - The Whitelabel tab is where custom Tenant logos, colors, and security banners may be configured.
        - This permission is recommended for those responsible for branding tenants, whether they are Master Tenant users or individual Subtenant users.
        -

- .. toggle-header:: :header: **API Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - API: Billing
        - None, Read, Full
        - Allows or disallows access to invoices and projects via |morpheus| API/CLI.
        - The invoices API/CLI is used to generate bills and gather highly-granular costing data for supported Clouds. Read access allows list and get functions and Full allows access to post (refresh).
        - This permission is recommended for those responsible for generating invoices or projects.
        - It is recommended this setting be set to None on the Tenant Role to restrict access for Subtenant users.
      * - API: Execution Request
        - None, Full
        - Allows or disallows access to an API endpoint.
        - This endpoint allows users to execute scripts on Instances, containers, or hosts and then polls for a response.
        - This permission is recommended for those responsible for arbitrary API script execution.
        - It is recommended this setting be set to None on the Tenant Role to restrict access for Subtenant users.

- .. toggle-header:: :header: **Backups Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Backups
        - None, View, Read, User, Full
        - Determines access to the Backups secton of |morpheus| UI, including the Summary, Jobs, Backups, and History subpages. The "User" permission allows access only to backup objects the user owns.
        - The Summary subpage allows the user to see the number of configured backups, the success rate, recent failures, and the size of the backups, as well as, the upcoming and in-progress backups. The Jobs subpage is where backup jobs may be created, cloned, edited or deleted. On create, a name, code (for use within the API), retention count, and schedule are selected (Note: Selectable schedules are defined Execution Schedules which are created in the |LibAut|). On the backups subpage, a list of configured backups is provided and new backups may be created or on-demand backups may be executed. On create, the place where the target exists is selected (Instance, Host, or Provider), the source is selected and a name is defined as well as the selected execution schedule. On the History subpage both the backups and restores tabs are available. Names, statuses, start times, durations and size may be viewed.
        - This permission is recommended for those responsible for performing the backup and restoration of workloads.
        -
      * - Backups: Integrations
        - None, Read, Full
        - Determines access to the Backups > Integrations page.
        - From this page, backup integrations may be created, edited, or deleted. The page also provides the status of existing integrations. On create the integration product is selected and all associated connection and authentication information must be provided. Additionally, visibility is set to either public or private. Integrations available include Avamar, Commvault, Rubrik, Veeam, and Zerto.
        - This permission is recommended for those responsible for the integration between |morpheus| and backup technologies.
        - It is recommended this setting be set to None on the Tenant Role to restrict access for Subtenant users.

- .. toggle-header:: :header: **Catalog Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Catalog (Formerly Service Catalog: Catalog)
        - None, Full
        - Determines access to |ProCat| and Catalog in the Service Catalog Persona view
        - The Catalog page displays the complete list of Catalog Items that can be ordered from the Service Catalog
        - This permission is recommended for users who will order items from the Service Catalog
        -
      * - Catalog: Dashboard (Formerly Service Catalog: Dashboard)
        - None, Read
        - Determines access to |ProCatDas| and Dashboard in Service Catalog Persona view
        - The Catalog Dashboard contains featured Catalog Items, recently-ordered Catalog items and Inventory items. The Catalog Dashboard is the default landing page for the Service Catalog Persona view
        - This permission is recommended for users who will use the Service Catalog
        -
      * - Catalog: Inventory (Formerly Service Catalog: Inventory)
        - None, Full
        - Determines access to |ProCatDas| and Dashboard in Service Catalog Persona view
        - The Inventory is the complete list of user-owned items provisioned from the Service Catalog
        - This permission is recommended for users who will use the Service Catalog and need to be able to view details on the items they've provisioned from the Catalog
        -

- .. toggle-header:: :header: **Infrastructure Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Infrastructure: Boot
        - None, Read, Full
        - Determines access to the Integrations > Boot page, including the Mapping, Boot Menus, Answer Files, Images, and Discovered MAC Addresses tabs.
        - |morpheus| includes a PXE Server to provide for rapid bare metal provisioning. The Boot page is where users may add, edit, or delete answer files, as well as, manage their own images or use existing ones. Boot menus and mappings are also managed here and discovered MAC addresses are displayed.
        - This permission is recommend for those responsible for bare metal provisioning.
        -
      * - Infrastructure: Certificates
        - None, Read, Full
        - Determines access to the SSL Certificates tab on the Infrastructure > Keys & Certs page.
        - The SSL Certificates page is where certificates may be uploaded and managed. These certificates may then be used within |morpheus| when orchestrating load balancers.
        - This permission is recommended for personnel who will be orchestrating and provisioning load balancers.
        -
      * - Infrastructure: Clouds
        - None, Read, Group, Full
        - Determines access to the Infrastructure > Clouds page. The "Group" permission limits the Cloud list page (Infrastructure > Clouds) to show only Clouds in their assigned Groups.
        - The Cloud page is where new Clouds are integrated with |morpheus| and existing Cloud integrations are managed. This includes creating a code for use within the API, the location, visibility, tenant, whether or not it should be enabled, and if VMs should be automatically powered on. Additionally, Clouds may be integrated from the Clouds tab of a Group detail page.
        - This permission is recommended for those responsible for configuring RBAC as well as those responsible for |morpheus| Cloud Integrations.
        -
      * - Infrastructure: Clusters
        - None, Read, Group, Full
        - Determines access to the Infrastructure > Clusters page.
        - The Clusters page allows you to create and manage Kubernetes, Docker, and KVM Clusters, as well as Cloud-specific Kubernetes services such as EKS.
        - This permission is recommend for those creating and managing containers or container services.
        -
      * - Infrastructure: Compute
        - None, Read, Full
        - Determines access to the Infrastructure > Hosts page, including the Hosts, Virtual Machines, and Bare Metal tabs.
        - The Hosts page provides for viewing and managing hosts, virtual machines, and bare metal hosts. On the bare metal hosts page, hosts may come from PXE boot or may be manually added. On the Hosts page hypervisors and Docker hosts are displayed. The Virtual Machines page lists all VMs. On all three pages actions may be performed against machines. Additionally, views may be refined by altering the columns displayed and CSV/JSON exporting of lists is available.
        - This permission is recommend for those whom need to take action on machines and those responsible for bare metal provisioning.
        -
      * - Infrastructure: Credentials
        - None, Read, Full
        - Determines access to the Credentials tab in |InfTru|
        - The credentials tab allows you to create and manage credential sets stored internally and in external Cypher server integrations
        - This permission is recommended for those responsible for maintaining credentials
        -
      * - Infrastructure: Groups
        - None, Read, Full
        - Determines access to the Infrastructure > Groups page.
        - The Groups page is where |morpheus| Groups are created and given a code for use within the API. Additionally, the DNS service, CMDB, service registry, and config management may be selected. Existing Clouds/Hosts or new Clouds/Hosts are added to the Group and virtual or bare metal machines may be viewed.
        - This permission is recommended for those responsible for configuring Role Based Access Control (RBAC).
        -
      * - Infrastructure: Keypairs
        - None, Read, Full
        - Determines access to the Key Pairs tab on the Infrastructure > Keys & Certs page.
        - The Keypairs page allows for ease in accessing instances via SSH. On create a name, public key, private key, and passphrase are entered.
        - This permission is recommended for those whom utilize |morpheus| deployment and management of Linux Instances.
        -
      * - Infrastructure: Kubernetes Control
        - None, Full
        - Determines access to the Control tab on Kubernetes Cluster detail pages (Infrastructure > Clusters > Selected Kubernetes Cluster > Control Tab)
        - Run ``kubectl`` commands, apply templates, and run workloads on the Kubernetes Cluster
        - This permission is recommended for Kubernetes Cluster administrators
        -
      * - Infrastructure: Load Balancers
        - None, Read, Full
        - Determines access to the Infrastructure > Load Balancers page, including both the Load Balancers and Virtual Servers tabs.
        - The Load Balancers page is where new load balancer integrations may be configured. Additionally, existing integrations may be managed. The Virtual Servers page is where virtual servers are managed to include policies, pools, profiles, monitors, nodes, and rule scripts may be managed.
        - This permission is recommended for those responsible for integrating |morpheus| with load balancers as well as those responsible for managing virtual servers.
        -
      * - Infrastructure: Move Servers
        - None, Full
        - Determines access to the "Change Cloud" action on server detail pages (|InfCom| > Virtual Machines tab > Selected VM > Actions > Change Cloud)
        - Change Cloud allows server records to be migrated from one Cloud to another. Note that this is not a migration tool but simply allows for upkeep of records in |morpheus|.
        - This permission is recommended for appliance administrators. See other sections of |morpheus| documentation for more information on the use of this feature.
        -
      * - Infrastructure: Networks
        - None, Read, Group, Full
        - Determines access to the Infrastructure > Networks page, including the Networks, network groups, and integrations tabs. The "Group" permission setting allows access to objects shared to Groups associated with the user.
        - The Networks page is where networks are configured for DHCP or static IP assignment and existing networks are displayed. The Network Groups page is where networks are grouped to allow round robin provisioning among the group. The Integrations page is where IPAM, DNS, security, service registry, and virtual network tools are integrated. These include Cisco ACI, VMware NSX T and V, Infoblox, Bluecat, phpIPAM, SolarWinds, Stealth, Microsoft DNS, PowerDNS, and Route 53.
        - This permission is recommended for those responsible for integration with network technologies and the configuration and management of networks to be used during provisioning.
        -
      * - Infrastructure: Policies
        - None, Read, Full
        - Determines access to the Policies tabs on the Group and Cloud detail pages (Infrastructure > Groups > selected Group OR Infrastructure > Cloud > selected Cloud).
        - Policies can be created from this tab which are scoped to the Cloud or Group being viewed.
        - This permission is recommended for users who will need to set quotas which pertain specifically to Groups or Clouds the user has access to.
        -
      * - Infrastructure: Security Groups
        - None, Read, Full
        - Determines access to the Security Groups tab on the Infrastructure > Networks page.
        - The Security Groups page is where Security Groups (aka virtual firewalls) are defined.
        - This permission is recommended for those responsible for firewall configuration and management.
        -
      * - Infrastructure: State
        - None, Read, Full
        - Determines access to the power state toggle on the Infrastructure > Hosts page.
        - This toggle moves Hosts between a started and stopped state.
        - This permission is recommended for those responsible for managing Hosts.
        -
      * - Infrastructure: Storage
        - None, Read, Full
        - Determines access to the Infrastructure > Storage page, including the Buckets, File Shares, Volumes, Data Stores, and Servers tabs.
        - The Servers page is where storage integrations are configured. Integrations available include 3Par, AWS S3, Dell EMC ECS and Isilon, Huawei or Open Telekom OBS and Huawei, Open Telekom, OpenStack SFS. The Volumes page is where storage volumes may be created or viewed. The File Shares page is where File Shares of types CIFS, Dell EMC ECS or Isilon, local storage, and NFSv3 may be configured. The Buckets page is where storage buckets of type AWS S3, Alibaba, Azure, Open Telekom OBS, OpenStack Swift, Racspace CDN may be created. Storage buckets are used for Backup, Archives, and Virtual Images. The Data Store page is where permissions to data stores may be managed and new data stores are added.
        - This permission is recommended for those responsible for storage integrations and configurations.
        - This permission is recommended to be set to None on the Tenant Role to restrict access to Subtentant users.
      * - Infrastructure: Storage Browser
        - None, Read, Full
        - Determines file browsing access to buckets and file shares on the Buckets and File Shares tabs of the Infrastructure > Storage page.
        - The Storage Browser permission allows users who also have appropriate Infrastructure: Storage permission to browse, add files and folders, download, and delete from the buckets and file shares.
        - This permission is recommended for those who need to browse storage.
        -
      * - Infrastructure: Trust Integrations
        - None, Read, Full
        - Determines access to the Integrations tab of the Infrastructure > Keys & Certs page.
        - The Integrations tab is where new trust integrations can be configured. This includes Venafi.
        - This permission is recommended for those responsible for the integration between |morpheus| and Venafi.
        - This permission is recommended to be set to None on the Tenant Role to restrict access to Subtentant users.

- .. toggle-header:: :header: **Library Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Library: App Blueprints (Formerly Provisioning: Blueprints)
        - None, Read, Full
        - Determines access to the |LibBluApp| page.
        - The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of |morpheus| is available.
        - This permission is recommended for those responsible for defining |morpheus|-type Blueprints.
        -
      * - Library: Blueprints - ARM (Formerly Provisioning: Blueprints - ARM)
        - None, Provision, Full
        - Determines access to ARM-type Blueprints on the |LibBluApp| page. The "Provision" permission allows for provisioning Apps from ARM Blueprints without the ability to create or edit them.
        - The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of ARM is available.
        - This permission is recommended for those responsible for defining ARM blueprints.
        -
      * - Library: Blueprints - CloudFormation (Formerly Provisioning: Blueprints - CloudFormation)
        - None, Provision, Full
        - Determines access to CloudFormation-type Blueprints on the |LibBluApp| page. The "Provision" permission allows for provisioning Apps from CloudFormation Blueprints without the ability to create or edit them.
        - The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of CloudFormation is available.
        - This permission is recommended for those responsible for defining CloudFormation blueprints.
        -
      * - Library: Blueprints - Helm (Formerly Provisioning: Blueprints - Helm)
        - None, Provision, Full
        - Determines access to Helm-type Blueprints on the |LibBluApp| page. The "Provision" permission allows for provisioning Apps from Helm Blueprints without the ability to create or edit them.
        - The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of Helm is available.
        - This permission is recommended for those responsible for defining Helm blueprints.
        -
      * - Library: Blueprints - Kubernetes (Formerly Provisioning: Blueprints - Kubernetes)
        - None, Provision, Full
        - Determines access to Kubernetes-type Blueprints on the |LibBluApp| page. The "Provision" permission allows for provisioning Apps from Kubernetes Blueprints without the ability to create or edit them.
        - The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of Kubernetes is available.
        - This permission is recommended for those responsible for defining Kubernetes blueprints.
        -
      * - Library: Blueprint - Terraform (Formerly Provisioning: Blueprints - Terraform)
        - None, Provision, Full
        - Determines access to Terraform-type Blueprints on the |LibBluApp| page. The "Provision" permission allows for provisioning Apps from Terraform Blueprints without the ability to create or edit them.
        - The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of Terraform is available.
        - This permission is recommended for those responsible for defining Terraform blueprints.
        -
      * - Library: Catalog Items (Formerly Tools: Self Service)
        - None, Read, Full
        - Determines access to |LibBluCat|
        - |LibBluCat| allows administrators to configure Catalog Items for the Library Catalog and Self Service Persona users
        - This permission is recommended for those responsible for creating and managing Library Catalog Items.
        -
      * - Library: Instance Types (Formerly Provisioning: Library)
        - None, Read, Full
        - Determines access to the |LibBluIns|
        - |LibBluIns| is where Instance Types are created and maintained.
        - This permission is recommended for those responsible for managing the Instance Types.
        -
      * - Library: Integrations (Formerly Provisioning: Automation Integrations)
        - None, Read, Full
        - Determines access to |LibInt|.
        - |LibInt| is where Library Automation created and maintained.. These include Chef, Puppet, Ansible, Salt, Ansible Tower and vRealize Orchestrator.
        - This permission is recommended for those responsible for the integration between |morpheus| and integrated automation technologies.
        -
      * - Library: Options
        - None, Read, Full
        - Determines access to |LibOpt| - Inputs (Option Types) and Option Lists.
        -
        - This permission is recommended for those responsible for creating and managing Library Inputs (Option Types) and Option Lists.
        -
      * - Library: Scheduling - Execute (Formerly Provisioning: Scheduling - Execute)
        - None, Read, Full
        - Determines access to |LibAutExe|.
        - The Execute Scheduling is where time schedules for Jobs, including Task, Workflow, and Backup Jobs are created and managed.
        - This permission is recommended for those responsible to create and manage schedules to be selected when scheduling jobs.
        -
      * - Library: Scheduling - Power (Formerly Provisioning: Scheduling - Power)
        - None, Read, Full
        - Determines access to |LibAutPow|.
        - Power Scheduling is where startup and shutdown times are created, these schedules can be applied via policy or manaully.
        - This permission is recommended for those responsible to create and manage power schedules.
        -
      * - Library: Tasks (Formerly Provisioning: Tasks)
        - None, Read, Full
        - Determines access to |LibAutTas| and |LibAutWor|.
        - |LibAutTas| is where Tasks are created and managed. |LibAutWor| is where Workflows are created and managed. Workflows are used to execute one or many tasks during specified phases.
        - This permission is recommended for those responsible for creating provisioning and operational scripts.
        -
      * - Library: Tasks - Script Engines (Formerly Provisioning: Tasks - Script Engines)
        - None, Full
        - Determines access to advanced Task types include Groovy Script, Javascript, jRuby Script, and Python Script.
        - This permission adds the ability to create and manage Groovy, Javascript, jRuby and Python Task Types.
        - This permission is recommended for those responsible for Tasks containing advanced script capabilities.
        -
      * - Library: Templates
        - None, Read, Full
        - Determines access to |LibTem|
        - |LibTem| is where Spec Templates, File Templates, Script Templates and Security Packages are created and managed.
        - This permission is recommended for those responsible for creating and managing Spec Templates, File Templates, Script Templates and Security Packages.
        -
      * - Library: Thresholds (Formerly Provisioning: Thresholds)
        - None, Read, Full
        - Determines access to |LibAutSca|.
        - Scale Thresholds is where preconfigured settings for auto-scaling Instances are configured. When adding auto-scaling to an Instance, existing Scale Thresholds can be selected to define auto-scaling rules.
        - This permission is recommended for those responsible for defining auto-scaling for Instances.
        - This permission is recommended to be set to None or Read on the Tenant Role to restrict access for Subtenant users.
      * - Library: Virtual Images (Formerly Provisioning: Virtual Images)
        - None, Read, Full
        - Determines access to the |LibVir| page.
        - |LibVir| is where user and system Virtual Images are managed.
        - This permission is recommended for those who are responsible for image management.
        -

- .. toggle-header:: :header: **Lifecycle Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Environment Variables
        - None, User, Read, Full
        - Allows access to the Environments tab of the Instance detail page
        - Allows Instance environment variables to be edited. If set to "User" level only environment variables of Instances owned by the currently logged in user may be edited.
        - This permission is recommended for those needing management control over Instances
        -
      * - Power Control
        - None, User, Full
        - Allows access to power state controls for Instances and servers, including stopping, starting, restarting and suspending.
        - Allows the user to change the current power state of Instances and servers
        - This permission is recommended for those needing management control over Instances
        -
      * - Reconfigure
        - None, User, Full
        - Allows general access to Instance and server reconfigure (resize) feature. See additional reconfigure permissions below for more granular control over specific reconfigure functionality.
        - Allows general access to reconfigure features for Instances and servers. "User" level permission allows only Instances and servers owned by the currently logged in user to be reconfigured.
        - This permission is recommended for those needing management control over Instances
        -
      * - Reconfigure: Change Plan
        - None, User, Full
        - Allows the user to change the Instance service plan
        - When reconfiguring, the user may change the service plan associated with the Instance. "User" level permission allows only Instances owned by the currently logged in user to have their plans changed.
        - This permission is recommended for those needing management control over Instances
        -
      * - Reconfigure: Disk Add
        - None, User, Full
        - Allows the user to add disks to an Instance or server during reconfigure.
        - When reconfiguring, the user may add disks to the selected Instance or server. "User" level permission allows only Instances owned by the currently logged in user to have their disks changed.
        - This permission is recommended for those needing management control over Instances
        -
      * - Reconfigure: Disk Change Type
        - None, User, Full
        - Allows the user to change the datastore or volume type during reconfigure.
        - When reconfiguring, the user may update datastore or volume types. "User" level permission allows only Instances owned by the currently logged in user to have their disk types changed.
        - This permission is recommended for those needing management control over Instances
        -
      * - Reconfigure: Disk Modify
        - None, User, Full
        - Allows the user to modify an attached disk during reconfigure.
        - When reconfiguring, the user may modify disks attached to the Instance. "User" level permission allows only Instances owned by the currently logged in user to have their disks changed.
        - This permission is recommended for those needing management control over Instances
        -
      * - Reconfigure: Disk Remove
        - None, User, Full
        - Allows the user to remove disks or volumes during reconfigure.
        - When reconfiguring, the user may remove disks attached to the Instance or server. "User" level permission allows only Instances owned by the currently logged in user to have their disks removed.
        - This permission is recommended for those needing management control over Instances
        -
      * - Reconfigure: Network Add
        - None, User, Full
        - Allows the user to add a network adapter during reconfigure.
        - When reconfiguring, the user may add a network interface to the Instance or server. "User" level permission allows only Instances owned by the currently logged in user to have network interfaces added.
        - This permission is recommended for those needing management control over Instances
        -
      * - Reconfigure: Network Modify
        - None, User, Full
        - Allows the user to edit network adapters during reconfigure.
        - When reconfiguring, the user may edit network interfaces on the Instance or server. "User" level permission allows only Instances owned by the currently logged in user to have network interfaces modified.
        - This permission is recommended for those needing management control over Instances
        -
      * - Reconfigure: Network Remove
        - None, User, Full
        - Allows the user to remove network adapters during reconfigure.
        - When reconfiguring, the user may remove network interfaces on the Instance or server. "User" level permission allows only Instances owned by the currently logged in user to have network interfaces removed.
        - This permission is recommended for those needing management control over Instances
        -

- .. toggle-header:: :header: **Monitoring Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Monitoring
        - None, Read, User, Full
        - Determines level of access to the Monitoring section of |morpheus| UI, including the Status, Apps, Checks, Groups, Incidents, Contacts, and Alert Rules subpages. The "User" permission will allow access only to objects the user owns.
        - The Checks page is where automatically-created checks are customized or new checks are created. The Groups and Apps pages are where checks may be grouped. The Incidents page is where incidents are created upon Check failure. The Contacts page is where contacts may be added for notifications. The Alert Rules page is where notification are configured.
        - This permission is recommended for those responsible for monitoring applications, incidents, or configuring notifications.
        -
      * - Monitoring: Logs (Formerly Logs)
        - None, Read, User, Full
        - Determines level of access to the Logs section of |morpheus| UI. The "User" permission will allow access only to objects the user owns.
        - |MonLog| is where Instance and Server logs may be viewed (does not include |morpheus| Appliance logs from |AdmHeaMorLog|).
        - This permission is recommended for those who should have access to Instance and Server logs.
        - Setting permission to Full on the Tenant Role will give Subtenant users full access to all logs appliance-wide, including to workloads living in other Tenants, for any Subtenant users who also have Full permission on their User Role. It's recommended that you set this permission to User on the Tenant Role so that Subtenant users are not able to see logs for workloads other than their own.

- .. toggle-header:: :header: **Networks Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Networks: DHCP Relays
        - None, Read, Full
        - Determines access to the DHCP Relays in applicable network integrations
        - Allows DHCP Relays to be viewed, created and managed
        - This permission is recommended for those tasked with network management
        -
      * - Networks: DHCP Servers
        - None, Read, Full
        - Determines access to the DHCP Servers in applicable network integrations
        - Allows DHCP Servers to be viewed, created and managed
        - This permission is recommended for those tasked with network management
        -
      * - Networks: Domains
        - None, Read, Full
        - Determines access to the Domains tab on the |InfNet| page.
        - The Domains page is where network domains are managed. Domains are used for setting FQDNs, joining Windows Instances to domains, and creating A-Records with DNS integrations. On create the domain controller and credentials for domain join must be provided.
        - This permission is recommended for those responsible for |morpheus| DNS and domain-join integrations.
        -
      * - Networks: Firewalls
        - None, Read, Manage Rules, Full
        - Determines access to the Firewall tab on applicable network integrations detail pages. When the "Manage Rules" permission is given, users have read-only access to firewall groups and the ability to create and manage firewall rules on those groups
        - The Firewall tab is where network firewall groups and rules are viewed, created and managed
        - This permission is recommended for those tasked with network security management
        -
      * - Networks: Integration
        - None, Read, Full
        - Determines access to the Integrations tab on the Network list page (Infrastructure > Network)
        - The integrations tab is where network integrations can be viewed, added and managed. Additionally, the detail pages for network integrations are accessed here
        - This permission is recommended for those tasked with handling network integrations and their use within |morpheus|
        -
      * - Networks: IP Pools
        - None, Read, Full
        - Determines access to the IP Pools tab on the Network list page (Infrastructure > Network)
        - The IP Pools tab is where IP pools from various networks are displayed. Detail pages for IP pools can also be accessed here
        - This permission is recommended for those tasked with IP address management
        -
      * - Networks: Proxies
        - None, Read, Full
        - Determines access to the Proxies tab on the Infrastructure > Networks page.
        - The Infrastructure Networks Proxies page is where Proxy configurations are stored, which are available for use by the provisioning engines.
        - This permission is recommended for those responsible for configuring proxies to be used when provisioning.
        -
      * - Networks: Router DHCP Binding
        - None, Read, Full
        - Determines access to management of DHCP bindings
        -
        -
        -
      * - Networks: Router DHCP Pool
        - None, Read, Full
        - Determines access to the DHCP tab on the detail page for a Router associated with certain network integrations (Example: Infrastructure > Network > Integrations > Routers tab > selected router > DHCP tab)
        - The DHCP tab is where DHCP pools are viewed, created and managed
        - This permission is recommended for those responsible for DHCP pool management
        -
      * - Networks: Router DHCP Relay
        - None, Read, Full
        - Determines access to management of DHCP relays
        -
        -
        -
      * - Networks: Router Firewalls
        - None, Read, Full
        - Determines access to Firewall tabs on Router Detail pages (|InfNetRou| tab > Selected Router)
        - The Firewall tab is where firewall rules are viewed, created, and managed
        - This permission is recommended for those responsible for managing firewall rules
        -
      * - Networks: Router Interfaces
        - None, Read, Full
        - Determines access to Interfaces tabs on Router Detail pages (|InfNetRou| tab > Selected Router)
        - The Interface tab is where router interfaces can be viewed, created and managed
        - This permission is recommended for those responsible for network traffic flow
        -
      * - Networks: Router NAT
        - None, Read, Full
        - Determines access to the NAT tab on Router Detail pages (|InfNetRou| tab > Selected Router)
        - The NAT tab is where NAT rules are viewed, created, and managed
        - This permission is recommended for those responsible for network traffic flow
        -
      * - Networks: Router Redistribution
        - None, Read, Full
        - Determines access to Route Redistribution tabs on Router Detail pages (|InfNetRou| tab > Selected Router)
        - The Route Redistribution tab is where redistribution rules are viewed, created, and managed
        - This permission is recommended for those responsible for redistribution rules
        -
      * - Networks: Router Routes
        - None, Read, Full
        - Determines access to Routing tabs on Router Detail pages (|InfNetRou| tab > Selected Router)
        - The Routing tab is where routes are viewed, created, and managed
        - This permission is recommended for those responsible for network route management
        -
      * - Networks: Routers
        - None, Read, Group, Full
        - Determines access to the Routers tab on the Infrastructure > Networks page. The "Group" permission setting allows access to objects shared to Groups associated with the user.
        - The Routers page is where virtual routers are created and managed from Cloud and Network integrations.
        - This permission is recommended for those responsible for network management.
        -
      * - Networks: Server Groups
        - None, Read, Full
        - Determines access to
        -
        -
        -
      * - Networks: Static Routes
        - None, Read, Full
        - Determines access to the routing tab on a router detail page (/infrastructure/networks/routes)
        - The routers tab is where routes are created and managed
        - This permission is recommended for those responsible for network management
        -

- .. toggle-header:: :header: **Operations Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Operations: Activity
        - None, Read
        - Determines access to the Activity and History tabs on the Operations > Activity page.
        - The Activity page displays four types of recent activities: Provisioning, Alerts, Backups, and Permissions.
        - This permission is recommended for those responsible to monitor or view activities and their statuses within |morpheus|.
        -
      * - Operations: Alarms
        - None, Read, Full
        - Determines access to the Alarms tab in the Activity section (Operations > Health)
        - The Alarms tab is where alarms are listed and acknowledgement actions can be taken against them
        - This permission is recommended for those responsible for monitoring
        -
      * - Operations: Analytics
        - None, Read, Full
        - Determines access to the Operations > Analytics page.
        - The Analytics page gives administrators the ability to break down costs and usage, then filter the results by relevant delineations including Groups, Clouds, Tenants or even tag values.
        - This permission is recommended for those responsible for understanding utilization and costs.
        -
      * - Operations: Approvals
        - None, Read, Full
        - Determines access to the Operations > Approvals page.
        - When a Provision Approval-type Policy is enabled for a Group or Cloud, an approval request will be created on each relevant provision attempt. These approvals can be handled directly in |morpheus| or dealt with in ServiceNow with a properly-configured integration.
        - This permission is recommended for those responsible for approving, denying, or canceling approval requests.
        -
      * - Operations: Budgets
        - None, Read, Full
        - Determines access to the Operations > Budgets page.
        - The Budgets page is where budgets are created and applied to clouds, tenants, users, or groups.
        - This permission is recommended for those responsible for managing budgets.
        -
      * - Operations: Dashboard
        - None, Read
        - Determines access to the Operations > Dashboard page (default |morpheus| landing page).
        - The Dashboard page is a single pane of glass showing quick, easy-to-read performance and configuration information about the |morpheus| environment.
        - "Read" permission is recommended for all users. When set to None, Operations > Reports becomes the default landing page and attempts to go to the Dashboard will redirect users to their User Settings page.
        -
      * - Operations: Guidance
        - None, Read, Full
        - Determines access to the Operations > Guidance page.
        - The Guidance page shows recommendations for resource and cost-utilization optimization.
        - This permission is recommended for those responsible to optimize utilization and costs of Cloud-based resources.
        -
      * - Operations: Invoices
        - None, Read, Full
        - Determines access to the Invoices tab in Operations > Costing
        - The Invoices tab allows access to highly-granular historical costing data
        - This permission is recommended for those responsible for generating invoices and analyzing spend
        -
      * - Operations: Reports
        - None, Read, Full
        - Determines access to the Operations > Reports page.
        - The Reports page is where reports may be generated and exported into JSON or CSV format.
        - This permission is recommended for those responsible for account, infrastructure, provisioning, usage, and cost reports.
        -
      * - Operations: Usage
        - None, Read, Full
        - Determines access to the Usage tab on the Operations > Activity page.
        - The Usage tab shows billing information for Instances and hosts that have pricing configured on their Service Plans.
        - This permissions is recommended for those responsible for cost accounting.
        -
      * - Operations: Wiki
        - None, Read, Full
        - Determines access to the Operations > Wiki page.
        - The Wiki page allows easy UI, API and CLI access to information to be referenced or shared with others. Wiki pages encompass individual Clouds, Groups, Servers, Instances, Clusters, and other pages can be manually created. Wiki pages from resources are accessible from the Operations > Wiki page or within individual resource detail pages on their respective Wiki tabs.
        - This permission is recommend for those responsible for documentation and knowledge management.
        -

- .. toggle-header:: :header: **Projects Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Projects
        - None, Read, Full
        - Determines access to Projects through |morpheus| API
        - Projects are used to associate resources together and apply common tags to their invoices
        - This permission is recommended for those responsible for cost analysis and invoice reporting
        -

- .. toggle-header:: :header: **Provisioning Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Provisioning: Administrator
        - None, Full
        - When editing an Instance (|ProIns| > selected Instance > EDIT button), this permission determines access to changing the owner of an Instance.
        - Allows you to change the owning user of an Instance.
        - This permission is recommended for those responsible to ensure all instances are owned by appropriate personnel.
        -
      * - Provisioning: Advanced Node Type Options
        - None, Full
        - This allows or disallows access to the "Extra Options" field of the Node Types tab on the |Lib| page when the Node Type Technology value is set to "VMware".
        - When VMware technology type is selected for a new or existing Node Type (|LibBluNod|), the "Extra Options" field will be available in the VMware VM Options section. These allow defining advanced vmx-file parameters during provisioning.
        - This permission is recommended for those responsible for managing VMware Node Types (images).
        -
      * - Provisioning: Apps
        - None, Read, User, Full
        - Determines access to the |ProApp| page. The "User" permission will allow access to only object the user owns.
        - The Apps page allows Instances to be grouped and tiered logically into Apps. From this page, Apps can be deployed from existing Blueprints and Instances can be added to existing Apps. Security groups and environmental variables (Linux Only) may be added and edited. The App log, history, and monitoring tabs may be viewed.
        - This permission is recommended for those responsible for provisioning.
        -
      * - Provisioning: Code Deployments
        - None, Read, Full
        - Determines access to the Deployments tab on the |ProCod| page.
        - The Deployments page provides the ability to use git, fetch from a url, or upload a file to be utilized during the provisioning of an Instance or pushed to an existing Instance.
        - This permission is recommended for those responsible for providing and managing software.
        -
      * - Provisioning: Code Integrations
        - None, Read, Full
        - Determines access to the Integrations tab on the |ProCod| page.
        - From this page code integrations may be created, edited, or deleted. Integrations available include Git, Github, and Jenkins.
        - This permission is recommended for those responsible for the integration between |morpheus| and code repositories and services.
        -
      * - Provisioning: Code Repositories
        - None, List Files, Read, Full
        - Determines access to the Deployments tab on the |ProCod| page.
        - The Code Repositories contains the repositories integrated with |morpheus| allowing users to browse repositories folders and files and view file contents from any branch, trigger a refresh, and create tasks, scripts and templates directly from the repos.
        - This permission is recommended for those responsible for providing and managing software.
        -
      * - Provisioning: Execute Script
        - None, Full
        - Determines access to the Run Script and Apply Template selections from the Actions menu on an Instance detail page
        - These selections bring up a menu allowing the user to select a script and run it against the viewed Instance or select a template to write to the Instance
        - This permission is recommended for those running day two automations against existing Instances
        -
      * - Provisioning: Execute Task
        - None, Full
        - Determines access to the Run Task selection from the Actions menu on an Instance detail page
        - This selection brings up a menu allowing the user to select a Task and run it against the viewed Instance
        - This permission is recommended for those running day two automations against existing Instances
        -
      * - Provisioning: Execute Workflow
        - None, Full
        - Determines access to the Run Workflow selection from the Actions menu on an Instance detail page
        - This selection brings up a menu allowing the user to select a Workflow and run it against the viewed Instance
        - This permission is recommended for those running day two automations against existing Instances
        -
      * - Provisioning: Executions
        - None, Read
        - Determines access |ProExe|
        - |ProExe| is where Task, Workflow, and Security Scan execution output can be viewed
        - This permission is recommended for those who are responsible for managing or troubleshooting Task, Workflow, and Security Scan executions.
        -
      * - Provisioning: Import Image
        - None, Full
        - Determines access to the Import as Image and Clone to Image selections from the Actions menu on an Instance detail page
        - These selections allow users to create an image from an existing Instance or import the Instance as an image to a selected bucket
        - This permission is recommended for those responsible for managing the library of provisionable items
        -
      * - Provisioning: Instances: Add
        - None, Full
        - Gives access to create Instances. Without this permission the user cannot directly add Instances.
        - The "+ ADD" button will not be visible on the Instances List Page if permission is set to "None" and the user will not have access to Instance create API actions as well
        - This permission is recommended for any user who needs to be able to provision Instances
        -
      * - Provisioning: Instances: Clone
        - None, User, Full
        - Determines the presence of the "Clone" selection under the Actions menu on the Instance detail page and Instance clone API functionality
        - The "Clone" selection will not be available under the "Actions" menu on the Instance detail page if permission is set to "None" and the user will not have access to similar API actions. If permission is set to "User", only Instances owned by the currently logged in user may be cloned.
        - This permission is recommended for any user who needs to be able to manage Instances
        -
      * - Provisioning: Instances: Delete
        - None, User, Full
        - Determines the presence of the "Delete" button on the Instance detail page, delete bulk action on the Instances list page, and Instance delete API functionality
        - The "Delete" button will not be available on the Instance detail page and the delete action will not be available from the Instances list page if permission is set to "None" and the user will not have access to similar API actions. If permission is set to "User", only Instances owned by the currently logged in user may be deleted.
        - This permission is recommended for any user who needs to be able to manage Instances
        -
      * - Provisioning: Instances: Edit
        - None, User, Full
        - Gives access to the Edit Instances modal for existing Instances (and corresponding API functionality). This allows the user to edit an Instance display name, tags, or Input (custom option) values
        - The "EDIT" button will not be visible on the Instances List Page if permission is set to "None" and the user will not have access to Instance edit API actions. If permission is set to "User", only Instances owned by the currently logged in user may be edited.
        - This permission is recommended for any user who needs to be able to manage Instances
        -
      * - Provisioning: Instances: Force Delete
        - None, Full
        - Determines access to the force delete option when deleting Instances
        - The force delete option (checkbox) will not be available when deleting Instances if this permission is not given. Force deleting allows |morpheus| to delete an Instance object even when it is unable to confirm the delete happened in the target cloud. Occasionally, this may be necessary but improper use can cause orphaned objects.
        - This permission is recommended for any user who needs to be able to manage Instances
        -
      * - Provisioning: Instances: List
        - None, User, Full
        - Controls which Instances are listed on the Instances list page (|ProIns|). When set to "User", only Instances owned by the currently logged in user will be displayed.
        -
        - This permission is recommended for any user who needs to be able to manage Instances
        -
      * - Provisioning: Instances: Lock/Unlock
        - None, User, Full
        - Gives access to the lock/unlock actions on Instance detail pages (and corresponding API functionality). This allows the user to lock or unlock Instances which reduces the chances of accidental removal of important workloads.
        - The Lock/Unlock selections will not be visible in the Actions menu on the Instances List Page if permission is set to "None". If permission is set to "User", only Instances owned by the currently logged in user may be locked or unlocked.
        - This permission is recommended for any user who needs to be able to manage Instances
        -
      * - Provisioning: Instances: Remove From Control
        - None, User, Full
        - Gives access to deleting an Instance in |morpheus| only. The instance remains in the target cloud. This may only be done for brownfield workloads which were converted to managed |morpheus| Instances
        -
        - This permission is recommended for any user who needs to be able to manage Instances
        -
      * - Provisioning: Instances: Scale
        - None, User, Full
        - Gives access to the scale tab on Instance detail pages which allow configuration of automated scaling thresholds (and corresponding API functionality). This allows the user to control scaling thresholds and add/remove nodes from an Instance.
        - The Scale tab on the Instance detail pages will not be visible and the user will not be able to add/remove nodes from Instances if the permission is set to "None". If permission is set to "User", only Instances owned by the currently logged in user may be scaled.
        - This permission is recommended for any user who needs to be able to manage Instances
        -
      * - Provisioning: Instances: Settings
        - None, User, Read, Full
        - Gives access to configuration changes if the Instance supports dynamic settings templates
        -
        -
        -
      * - Provisioning: Job Executions
        - None, Read
        - Determines access to the Job Executions tab on the |ProJob| page.
        - The Job Executions page contains execution history of completed jobs, including any process outputs and error messages.
        - This permission is recommended for those who are responsible for managing or troubleshooting jobs.
        -
      * - Provisioning: Jobs
        - None, Read, Full
        - Determines access to the Jobs tab on the |ProJob| page.
        - The Jobs page is where jobs are scheduled for the execution of automation Tasks and Workflows against Instances or servers.
        - This permission is recommended for those responsible to schedule the exectution of Tasks or Workflows.
        -
      * - Provisioning: Remote Console
        - None, Provisioned, Full
        - Determines access to the console on a Host detail page (Infrastructure > Hosts > selected Host, VM, or Bare Metal resource > Console tab). The "Provisioned" permission gives access to the console only for resources the logged in user has provisioned.
        - Remote console access for Instances, hosts, virtual machines, and bare metal.
        - This permission is recommended for those who need console access for provisioned Cloud resources.
        -
      * - Provisioning: Remote Console Auto Login
        - No, Yes
        - This allows or disallows the ability to automatically log into the remote console.
        - |morpheus| will automatically log into the machine using the credentials defined on the VM or Host. The credentials are defined either from the virtual image used, added via cloud-init or VMware Tools using the global cloud-init settings (|AdmSetPro|), or the Linux or Windows settings defined in User Settings.
        - This permission is recommended when an organization utilizes |morpheus| to create user accounts on provisioned or managed machines, as well as, allow remote console access.
        -
      * - Provisioning: Service Mesh
        - None, Read, User, Full
        - Determines access to the Provisioning > Service Mesh page, including the Services and DNS tabs. The "User" permission will allow access only to objects the user owns.
        - The Service Mesh page displays container services and DNS information. A service mesh ensures fast and reliable communication between containerized application services.
        - This permission is recommended for those responsible for container management.
        -
      * - Provisioning: State
        - None, Read, Full
        - Determines access to the State tab for a Terraform Instance or App
        - The State tab is where `Terraform state management <https://docs.morpheusdata.com/en/latest/integration_guides/Automation/terraform.html#terraform-app-state-management>`_ is handled for Terraform Instances or Apps
        - This permission is recommended for those responsible for any Terraform-based workloads
        -

- .. toggle-header:: :header: **Security Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Security: Scanning
        - None, Read, Full
        - Determines access to the Security Packages tab on the Jobs list page (|ProJob|), Security Scanning type Jobs, and Security Subtab inside the Software tab on a server detail page where the results of security scans are viewed
        - Allows access to view, create, and run security scans on existing systems, as well as view the results of previously-run scans
        - This permission is recommended for those responsible for security compliance of existing systems
        -

- .. toggle-header:: :header: **Snapshots Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Snapshots
        - None, Read, Full
        - Determines access to the "Create Snapshot" function in the Actions menu on an Instance detail page (Provisoning > Instances > selected Instance).
        - If utilizing a VMware Cloud, the ability to create snapshots is available on the Instance detail page (Provisoning > Instances > selected Instance).
        - This permission is recommended for Instance owners who should be allowed to take snapshots.
        -

- .. toggle-header:: :header: **Tools Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Tools: Archives
        - None, Read, Full
        - Determines access to the Tools > Archives page.
        - Archives provides a way to store files and make them available for download by scripts and users. Archives are organized by buckets. Each bucket has a unique name that is used to identify it in URLs and Scripts.
        - This permission is recommended for those responsible for storage or scripts which will use the Archive.
        -
      * - Tools: Cypher
        - None, Read, User, Full, Full Decrypt
        - Determines access to the Tools > Cypher page. The "User" permission will allow access only to objects the user owns. The "Full Decrypt" permission will allow for decryption of secrets.
        - Secure key/value store. Cypher keys can be used in scripts.
        - Recommended for those who need to store or use security key value pairs.
        -
      * - Tools: Image Builder
        - None, Read, Full
        - Determines access to the Tools > Image Builder page, Image Builds, Boot Scripts, and Preseed Scripts tabs.
        - The |morpheus| Image Builder tool creates vmdk, qcow2, vhd and raw images. The Image Builder creates a blank VM in VMware, attaches an OS ISO, executes a boot script on the VM at startup via VNC, which calls a preseed script that runs the unattended OS installation and configuration. |morpheus| then executes an OVA export of the completed vmdk to the target storage provider and converts the image to all other specified formats.
        - Recommended for those who are responsible for image creation.
        -
      * - Tools: Kubernetes
        - None, Read, User, Full
        - Allows for the management of Kubernetes clusters via the API (may be deprecated in the near future).
        - Allows for the management of Kubernetes clusters via the API
        - This permission is recommended for those who need to manage Kubernetes clusters via the API.
        - It is recommended this permission is set to None on the Tenant Role to restrict access for Subtenant users.

- .. toggle-header:: :header: **Virtual Desktop Permission Options**

    .. list-table::
      :widths: auto
      :header-rows: 1

      * - Permission Name
        - Permission Options
        - Feature Access
        - Description
        - Recommendations
        - Tenant Role Recommendations
      * - Virtual Desktop: Copy/Paste
        - None, Full
        - Allows copy and paste access from the virtual desktop terminal
        - Enables the user to copy and paste values from a virtual desktop session into the paste buffer of their local computer
        -
        -
      * - Virtual Desktop: Local Printer
        - None, Full
        - Enables printing from a virtual desktop session to a locally installed printer
        -
        -
        -
      * - Tools: VDI Pools
        - None, Read, Full
        - Allows for the management of virtual desktop (VDI) pools.
        - Enables the user to access the VDI Pools section (TooVDI) and view existing pools (with "read" permission) or create and edit pools (with "full" permission). Related API functions are also granted with this feature permission.
        - This permission is recommended for those needing to manage VDI pools
        -
