.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. important:: v4.1.2 requires Elasticsearch v7.x. Please refer to :ref:`esupgrade` and ``Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to v4.1.2 if your Appliance's Elasticsearch is external.

.. important:: v3.6.0 or later required to upgrade to 4.1.2. Upgrading from v3.6.x to v4.x contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x a database backup is recommended due to MySQL version upgrade.

New Features
============

Agents: FIPS enabled packages installed when FIPS is enabled on target
  |morpheus| will now use FIPS enabled agent packages when FIPS is enabled.

  - The Agent install process will detect if FIPS is enabled on the target VM or Host, and then call the package `morpheus-node-fips` or `morpheus-vm-node-fips` instead of the non-FIPS compliant packages during the agent install process.
  - The Appliance repo will contain both non-FIPS and FIPS package versions.

Agent: SSL Verification of Agent Communications option added
  SSL Verification of Agent Communications can now be enforced.

  - ``Enable SSL Verification of Agent`` toggle added to ``/admin/settings#!appliance``
  - Enabling SSL Verification of Agent Communications requires a valid Certificate be installed on the Appliance.
    - If ``Enable SSL Verification of Agent`` is enabled and the Appliance has a valid 3rd party SSL Certificate and the verify peer is set on the Agent, the Agent can connect to the Appliance.
    - If ``Enable SSL Verification of Agent`` is enabled and the Appliance has a self-signed Certificate  (default), the Agent will not be able to connect to the Appliance.
    - SSL Verification of Agent Communications requires the node's Agent configuration to have ``morphd['verify_peer'] = true`` set in ``/etc/morpheus/morpheus-node.rb``.

Apps: Kubernetes: Spec-Based App: Parsing errors surfaced
  When provisioning Kubernetes Spec-Based Apps, syntax and/or parsing errors are now surfaced in the UI.
Appliance: Redis removed
  Redis has been removed for security enhancements. Redis is no longer installed or needed.
Appliance: Elasticsearch 7 upgrade
  4.1.2 installs and requires Elasticsearch v7.x.
   - For Appliances with the default local Elasticsearch, no action is required.
   - For existing Appliances using an external Elasticsearch Host, Cluster or Service, Elasticsearch v7.x upgrade is required.
   - New installations require any external Elasticsearch Host, Cluster or Service to be on Elasticsearch v7.x.
   - Elasticsearch v5.6 was the previous version used by |morpheus|. Please refer to Elasticsearch Upgrade Documentation for upgrade instructions.
  .. important:: Elasticsearch 7 is required for v4.1.2+. Running |morpheus| v4.1.2+ with Elasticsearch 5.x or 6.x is NOT supported."

Azure: CSP and EA price sync
  Azure EA (enterprise agreement) and CSP (Cloud Solution Provider) pricing support added.
   - ACCOUNT TYPE field added to Azure Cloud settings, with Standard, EA and CSP options.† The Account Type selection determines what prices are synced to |morpheus|. Standard is Default and the same prices synced in earlier versions.
   - To change an Azure Cloud Account Type from Standard to either CSP or EA pricing, in ``Infrastructure -> Clouds``, edit the target Azure Cloud. In the Details section, select Standard, CSP, or EA from the ACCOUNT TYPE dropdown. Select SAVE CHANGES. A new cloud sync will be triggered and the specified Account Type pricing will sync.
       .. note:: CSP and EA pricing sync is only available for Azure EA (Enterprise Agreement) and CSP (Cloud Solution Provider) subscriptions.

Azure: ARM templates: Custom naming of parameters for display
  Currently, the key in an Azure ARM template is used as the display name. See https://bertram.d.pr/13G6gf. Now, a user can specify 'fieldLabel' under the 'metadata' block for a parameter and that will be picked up and displayed as the label when provisioning.
Azure: ARM Spec Templates & Layouts
  ARM Spec Templates & Layouts
  - Users can now create an ARM layout type and then select a Spec Template created with an ARM template.
  - The options in the ARM template then appear in the instance wizard. Upon provision, |morpheus| will look through the template and create matching resource records in |morpheus| mapped to those created in Azure. - - - Post-provision, records will also be created for any additional indirect resources that are created during provisioning.
  - ARM Spec Templates support Local, Repository and URL Sources.
  - Spec Templates: /provisioning/library/resource-specs"

Backups: Tenant Backups Visibility added to Master Tenant
  Sub-Tenants Backups are now visible in the Master Tenant for Backups in Clouds owned by the Master Tenant and either shared Publicly or Private and assigned to a Sub-Tenant.

  - Tenant field added to Backup List ( /backups/list) and Backup Details ( /backups/show/{id}) pages.

Backups: (GB, 7 DAY TOTAL) added to SIZE OF BACKUPS widget.
  Title for "Size of backups" on /backups summary updated to make it clearer the values in the widget reflect the last 7 days and are in GB.
Convert To Managed: Instance Type list filtered by Role Permissions
  The Instance Types available to a user to select from during the Convert to Managed action are now filtered by the users Instance Type Access Role permissions.
Clusters: Create Cluster: Review Tab Enhancements
  The Review Tab in the Create Cluster wizard has been update with:
     - Added:
        VOLUME DETAILS, NETWORK DETAILS, SERVICE PLAN, POD CIDR, and LAYOUT
     - Removed:
        GROUP

Clouds: Type and Status filters added
  In the Clouds List page /infrastructure/clouds, Clouds can now be filtered by status (All/Enabled/Disabled) and/or by Cloud Type
Clouds: `Cloud Init/ Unattend` default Agent Install mode
  The default AGENT INSTALL MODE setting for new Clouds is now set to ``Cloud Init / Unattend (when available) ``

  - The setting for existing clouds will not be changed.
  - `SSH / WinRM / Gust Execution` was previously the default setting and ` Cloud Init / Unattend (when available)` needed to be set manually, which is the recommended Agent Install mode.

Instances: Warning message added for "Force Delete" option
  Checking "Force Delete" when deleting now displays a warning message "After force deleting you may need to remove the corresponding infrastructure manually", as force deletes can leave target resources up if |morpheus| is unable to validate their removal.
Identity Sources: SAML: Logout Redirect improvements
  Logout Redirect functionality improved for SAML Identity Source Integrations when the Logout Redirect URL is specified.
Identity Sources: SAML: Azure AD SAML Graph support
  Azure AD SAML now supports graph links in saml responses for Azure AD SAML, sent when the number of groups a user is a member exceeds 150.
Library: Option Types: Typeahead now returns value(s) only
  Typeahead Option Types now return value(s) only, like Select List Option Types. Previously [name:name, value:value] was returned.
Networks: Cloud List Filter
  Cloud Type Filter added to /infrastructure/networks
.. NSX Object Permissions
  All of the NSX network objects to be scoped to a group by default and have individual role permission for each nsx object.Owned by and only visible by default to that group. Permission to create each object type can be assigned via user roles NSX objects are: ?	Transport Zones ?	Logical Switches (VxLans) ?	DLR ?	Edge Services Gateway (Firewall, NAT, DHCP, VPN, Load Balancing) ?	Load Balancers ?	Security Groups"

Openstack: Backups: Storage Provider options added
  Openstack backup creation now allows for choosing a storage provider.

  - Openstack Backup/Restores works with Local disk types, Volume disk types and Multiple disks.
  - If 'Archive Snapshots' is set on the Storage Provider, backups will be offloaded from Openstack onto the specified storage provider.
  - If 'Archive Snapshots' is unchecked, backups will remain on Openstack.
  - Offloaded backups can still be restored to Openstack.
Openstack: Migrations
  Ability to migrate an Instance from an openstack-based cloud to any other openstack-based cloud

  .. note:: Migrations to OTC/Huawei will not be supported via the Migrations tool in |morpheus|. This capability will only be covered via instance clone

Openstack: Support for multiple Routers within the same network
  Support added for multiple Routers within the same network. Previously, only one Router could be created per Network.

Provisioning: Actions removed for Canceled or Denied Instances & Apps.
  On Instance and App detail pages, invalid Instance and Node Actions are no longer listed for Instances with a status of Canceled or Denied (Approval).
Policies: Message of the Day (MOTD) Policy Type
  Message of the Day"" Policy for displaying Alerts in |morpheus|.

  - Configurable as a pop-up or full-page notification with Info, Warning and Critical message types.
  - Includes new Role Permission: Admin: Message Of the Day - None/Full

Policies: Backup Targets
  Backup Targets Policy Type added. A master account can determine storage provider options for backups with Backup Targets policies.
Provisioning: System 'Existing' Instance Layouts removed.
  v4.1.2 no longer seeds the legacy and disabled "Existing" System Layout options.

  - The "Existing" layout options, used for adding non-inventoried/discovered hosts and vm's in older releases, no are longer supported/retired.
  - Existing Hosts, Virtual Machines and Bare Metal can be added in the Infrastructure -> Hosts section, or through Cloud Discovery.

Roles: Identity Sources: Roles Admin permission
  Role permission for Identity Sources allowing the user to only edit Role Mappings and no other settings of the Identity Source.
ServiceNow Plugin: App Provisioning
  Apps from Blueprints can now be provisioned from ServiceNow via the |morpheus| ServiceNow App. Blueprint section added to the ServiceNow Integration details page in |morpheus| for managing the Blueprints exposed in ServiceNow.
ServiceNow: Plugin Support added for vCD, Xen, and ESXi Cloud Types
  The |morpheus| ServiceNow Plugin now supports vCloud Director (vCD), Xen, and ESXi Cloud Types.
Security: opensaml updated
  Addressed ``CVE-2015-1796 - opensaml-2.6.4 - A``
Tenants: Logouts now redirect to subdomain login
  When logging out of a sub-tenant, users are now redirected to the Tenants login url, rather than the Master Tenant login url.
Tasks: Shell Task: KEY Field Added
  Keys can now be used on Shell Tasks when using Remote Execution Targets
Tasks: Remote Shell, Local Shell, SSH Script Tasks Merged into "Shell Script"
  With the addition of task execution targets, the fRemote Shell Script, Local Shell Script and SSH Script task types offered redundant functionality and have been have been merged into a single "Shell Script" task type.
Tasks: "WinRM Script" renamed "Powershell Script"
  The WinRM Script Task type has been renamed Powershell Script, as the Task Type supports Command Bus, Local and Guest Execution in addition to WinRM connections for executing Powershell Scripts.

  - Existing WinRM Script Tasks are not affected, this is only a label change.

UI: Alarm Icon with Alarm Count badge added to Global Header
  Alarm Icon added to Global Header that links to Operations: Health: Alarms.

  - Active Alarm Count displayed with Badge on Alarm Icon
  - 100 or more alarms will display as 99+
  - Alarm Icon links to Operations: Health: Alarms
  - Alarm Count Icon

VM "Dashboard" tab renamed "Summary"
  The "Dashboard" tab on Virtual Machine Detail pages (/infrastructure/servers/{id}) has been renamed to "Summary"
Virtual Images: "OCI" added to Image Type Filter for Oracle Cloud Images
Workflows Provision Phase support for Cluster/Host Provisioning
  In addition to Post-Provision phases, Provision phases now supported for Workflows executed during Cluster and Host Provisioning


.. - Value of cypher created from API/CLI is a key pair string instead of just the value


Fixes
-----

- Administration: Disabling a user account now clears user access token session
- Agent Installation: SSH validation when using cloud-init agent install mode timeout increased from 2 seconds to 60 seconds
- Ansible: Integration detail pages now display streaming output of workflow runs
- API: Added support for both ``resourcePoolId`` & ``vmwareResourcePoolId`` for specifying VMware Resource Pool.
- Apps: Fix for validation error not exposed when Group is not specified and Instance configuration is extended in App wizard
- AWS: Fix for Elastic IP assignment when ``None`` is selected and subnet does not default to assigning an EIP.
- AWS: Fix for synced AMI Image location for AMI's with the same name in two different AWS accounts, with an AWS cloud added for each account.
- Azure: Fix for Azure Discovered VM's usage records.

  .. note:: If inventory level is set to basic, Morpheus does not know the power state of discovered VMs. Usage records will only be created as Stopped in this case.

- Azure: Fix for validation of minimum root volume size requirement on Private Azure Images
- Budgets. Fix for displayed currency when USD is not specified
- Docker: Fix for inaccurate Used Memory stat on Docker Hosts with running Instances
- ESXi: Fix for updating Image Store on Cloud Configuration not saving, using previous Image Store.
- Infrastructure Clouds Actions menu
- Instances: Instance status now reflected as unknown if the VM has been deleted in the target Cloud
- Instances: Reconfigure: Fix for adding networks during a reconfigure to a sub-tenant instance using a master-tenant owned private service plan.
- Nutanix: Fix for default Plan selection when reconfiguring an Instance when scoped plan has been deactivated
- Openstack: Fix for Security group rules not being created when the destination is a Security group
- OpenStack: Fix for sync of Security Groups that have been renamed in Openstack after initial sync
- Password exposed during agent install through vmtools
- Plans & Pricing: Fix for Price Sets displaying default Resource Pool (if set) instead of saved Resource Pool.
- Policies: Shutdown and Expiration policies no longer allow negative values
- Provisioning: Fix for allowing customization of additional volume sizes when ``CUSTOMIZE ROOT VOLUME`` is unchecked in selected Service Plan
- Provisioning: Fix for Ansible Tower section not expanding to expose the validation message when a required field is empty.
- Provisioning: Fix for scenarios when Option Type requirement is not validated
- Provisioning: Price estimates in provisioning instance wizard now incorporate selected resource pool as a price parameter
- Provisioning: Validation added for Network Static IP fields
- Recent Activity: Fix for User Filter only listing first 25 Users
- Reports: Cloud Cost Reports now include subtenant costs when filtering by subtenant Cloud
- Reports: Fix for Group Inventory Summary report VM Count
- SAML: Fix for SAML Response signature validation when enabled
- ServiceNow: Unsupported Instance Types (Google) with typeahead fields removed from ServiceNow Integration EXPOSED LIBRARIES Library Item configuration.
- Solarwinds: Fix for hostname record update in Solarwinds when IP is reserved
- Tasks: PROCESS OUTPUT is no longer hidden after the last retry attempt on task history if automation task is 'RETRYABLE' and fails.
- Tenants: Fix for Confirmation emails during Tenant self-registration
- Tenants: Fix for Tenant deletion when a Storage Server still exists in the Tenant
- Tenants: Improved error handling for when assigning a managed VM to subtenant that does not have access to the associated Cloud
- Usage: Fix and additional jobs added to prevent discovered virtual machines from having both running & stopped usage records active.
- vCloud Director: Provisions now properly fail when there is a Guest Customizations failure
- vCloud Director: Support added for VCD 9.5 upload api's removal of support for Content-Length header
- VMware: Fix for Default Resource Pool specification propagating to sub-tenants
- VMware: Fix for duplicate storage controller ``controllerKey`` values
- Whitelabel: Fix for favicon not being displayed in Terms of Use or Privacy Policy pages
- Zerto: Fix for Replication Group sync
.. - [API] [UI] Sub tenant user cannot toggle feature using both API and UI for instance-types created by himself
.. - [API] Failed to create role using API, however UI is able create the same.
.. - [API] PUT /api/virtual-images is not disabling "installAgent" option for virtual images
.. - Add Instance to Apps doesn't appear in UI"
.. - Admin Integrations: Stealth - missing fields
.. - API: Discovered VMs - start not working
.. - API: Hosts: Convert to Managed: should return 404 not 200 when invalid server ID
.. - Backup archives produced on QA are corrupt or not complete.
.. - CLI: apps add: undefined method + for nil:nilClass error when not setting instance name
.. - CLI: blueprints add: @clouds_interface not defined error
.. - CLI: hosts run-workflow: failing with async error
.. - CLI: Hosts: issues
.. - CLI: networks & security-groups: add fails with resource group error
.. - Cluster Add Node: Manual - not working due to form issues
.. - Could not create NSX Edge Service Gateway on |morpheus| UI. Error "Resource pool 14 is not valid. Reconfigure NSX Edge appliance with valid resource pool or cluster and retry the operation." was shown in morpheus-ui log
.. - Create/Edit NSX Edge Gateway operation is failing due to missing null protector on router.zone
.. - NSX - cant create security rules
.. - NSX - Error creating Logical Switch
.. - NSX Integration Issues
.. - Openstack VM's console does not work
.. - OTC: Network/Router creation is missing SNAT and CIDR
.. - Policies: Delayed Removal: not working properly for app instances & expired instances
.. - Powered Off VMs should set instance to stopped
.. - ServiceNow plug-in: provisioning fails for DigitalOcean, Nutanix, & Oracle Cloud instance types
.. - ServiceNow plug-in: VCD: vApp field options not populating
.. - Static IP Assignment - Linux Images
.. - Unable to clone instances via the API/CLI
.. - vCloud Director: Hypervisor Console
.. - VIO: Instances within volumes are aborted during clone
