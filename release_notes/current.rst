.. _Release Notes:

************************
v|version| Release Notes
************************

.. important:: v4.1.2 requires Elasticsearch v7.x. Please refer to `Elasticseatch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to v4.1.2 if your Applaince's Elasticsearch is external.

.. important:: v3.6.0 or later required to upgrade to 4.1.2. Upgrading from v3.6.x to v4.x contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x a database backup is recommended due to MySQL version upgrade.

New Features
============

Agents: FIPS enabled packages installed when FIPS is enabled on target
  Morpheus will now use FIPS enabled agent packages when FIPS is enabled.

  - The Agent install process will detect if FIPS is enabled on the target VM or Host, and then call the package `morpheus-node-fips` or `morpheus-vm-node-fips` instead of the non-FIPS compliant packages during the agent install process.
  - The Appliance repo will contain both non-FIPS and FIPS package versions.

Agent: SSL Verification of Agent Communications option added
  SSL Verification of Agent Communications can now be enforced.

  - ``Enable SSL Verification of Agent`` toggle added to ``/admin/settings#!appliance``
  - Enabling SSL Verification of Agent Communications requires a valid Certificate be installed on the Appliance.
    - If ``Enable SSL Verification of Agent`` is enabled and the Appliance has a valid 3rd party SSL Certificate and the verify peer is set on the Agent, the Agent can connect to the Appliance.
    - If ``Enable SSL Verification of Agent`` is enabled and the Appliance has a self-signed Certificate  (default), the Agent will not be able to connect to the Appliance.
    - SSL Verification of Agent Communications requires the node's Agent configuraiton to have ``morphd['verify_peer'] = true`` set in ``/etc/morpheus/morpheus-node.rb``.

Apps: Kubernetes: Spec-Based App: Parsing errors surfaced
  When provisioning Kubernetes Spec-Based Apps, syntax and/or parsing errors are now surfaced in the UI.
Appliance: Redis removed
  Redis has been removed for security enhancements. Redis is no longer installed or needed.
Appliance: Elasticsearch 7 upgrade
  4.1.2 installs and requires Elasticsearch v7.x.
   - For Appliances with the default local Elasticsearch, no action is required.
   - For existing Appliances using an external Elasticsearch Host, Cluster or Service, Elasticsearch v7.x upgrade is required.
   - New installations require any external Elasticsearch Host, Cluster or Service to be on Elasticsearch v7.x.
   - Elasticsearch v5.6 was the previous version used by Morpheus. Please refer to Elasticsearch Upgrade Documentation for upgrade instructions.
  .. important:: Elasticsearch 7 is required for v4.1.2+. Running Morpheus v4.1.2+ with Elasticsearch 5.x or 6.x is NOT supported."

Azure: CSP and EA price sync
  Azure EA (enterprise agreement) and CSP (Cloud Solution Provider) pricing support added.
   - ACCOUNT TYPE field added to Azure Cloud settings, with Standard, EA and CSP options.† The Account Type selection determines what prices are synced to Morpheus. Standard is Default and the same prices synced in earlier versions.
   - To change an Azure Cloud Account Type from Standard to either CSP or EA pricing, in ``Infrastructure -> Clouds``, edit the target Azure Cloud. In the Details section, select Standard, CSP, or EA from the ACCOUNT TYPE dropdown. Select SAVE CHANGES. A new cloud sync will be triggered and the specified Account Type pricing will sync.
       .. note:: CSP and EA pricing sync is only available for Azure EA (Enterprise Agreement) and CSP (Cloud Solution Provider) subscriptions.

Azure: ARM templates: Custom naming of parameters for display
  Currently, the key in an Azure ARM template is used as the display name. See https://bertram.d.pr/13G6gf. Now, a user can specify 'fieldLabel' under the 'metadata' block for a parameter and that will be picked up and displayed as the label when provisioning.
Azure: ARM Spec Templates & Layouts
  ARM Spec Templates & Layouts
  - Users can now create an ARM layout type and then select a Spec Template created with an ARM template.
  - The options in the ARM template then appear in the instance wizard. Upon provision, Morpheus will look through the template and create matching resource records in Morpheus mapped to those created in Azure. - - - Post-provision, records will also be created for any additional indirect resources that are created during provisioning.
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
  Checking "Force Delete" when deleting now displays a warning message "After force deleting you may need to remove the corresponding infrastructure manually", as force deletes can leave target resources up if Morpheus is unable to validate their removal.
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

  .. note:: Migrations to OTC/Huawei will not be supported via the Migrations tool in Morpheus. This capability will only be covered via instance clone

Openstack: Support for multiple Routers within the same network
  Support added for multiple Routers within the same network. Previously, only one Router could be created per Network.

Provisioning: Actions removed for Canceled or Denied Instances & Apps.
  On Instance and App detail pages, invalid Instance and Node Actions are no longer listed for Instances with a status of Canceled or Denied (Approval).
Policies: Message of the Day (MOTD) Policy Type
  Message of the Day"" Policy for displaying Alerts in Morpheus.

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
  Apps from Blueprints can now be provisioned from ServiceNow via the Morpheus ServiceNow App. Blueprint section added to the ServiceNow Integration details page in Morpheus for managing the Blueprints exposed in ServiceNow.
ServiceNow: Plugin Support added for vCD, Xen, and ESXi Cloud Types
  The Morpheus ServiceNow Plugin now supports vCloud Director (vCD), Xen, and ESXi Cloud Types.
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
