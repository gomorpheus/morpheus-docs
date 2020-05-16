.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: There are a number of important considerations to make before upgrading to |morpheus| version |morphver|. Please review our KnowledgeBase article on `upgrade considerations <https://support.morpheusdata.com/s/article/What-to-consider-before-upgrading-to-Morpheus-4-2-0?language=en_US>`_ and read the release notes below thoroughly.

|morpheus| UI Updates
*********************

New Features
============

Network Integration Enhancements
--------------------------------

- NSX: NSX-T Integration added

  - Create, manage, and sync NSX-T security groups and firewall rules
  - Create, manage, and sync NSX-T Transport Zones
  - Create, manage, and sync NSX-T Segments
  - Create, manage, and sync NSX-T Tier-0 Gateways
  - Create, manage, and sync NSX-T Tier-1 Gateways

- Stealth Integration added

Cloud Integrations Enhancements
-------------------------------

- Azure: Premium SSD disks can now be selected when provisioning or reconfiguring to add volumes
- Azure: Static IP addresses and IP pools can now be used with subnets, previously subnets were forced to DHCP
- Azure: Kubernetes AKS version 1.15 replaces 1.13
- Google: Tag compliance policies are now supported for Google clouds, including scanning of existing resources and banner display for non-compliant machines
- Google: Added the ability to set a statically-assigned DHCP addresses when provisioning
- Oracle Cloud: |morpheus| now syncs in pricing data for Oracle Cloud
- Oracle Cloud: Added support for new Regional-type subnet
- SCVMM: Multiple |morpheus| Clouds can now be pointed to the same SCVMM controller for easier distribution of resources
- OpenStack: Updated OS VERSION dropdown menu to include support for latest versions (Rocky, Stein, and Train) when adding or editing OpenStack clouds

Tasks and Workflows
-------------------

- Tasks: For email-type Tasks, added an option to remove the |morpheus| email template and render only email content contained in the "CONTENT" field of the Task
- Tasks: For email-type Tasks, added a Source field to optionally use templates stored in a Git repository or outside URL destination
- Tasks: Git repository integration now supported for Shell, Powershell, and jRuby Task types
- Tasks: Python Tasks now have support for virtual environments

UI Design Updates
-----------------

- Advanced Filtering: Potentially-large lists, such as Instances (Provisioning > Instances), Hosts (Infrastructure > Hosts > Hosts), and Virtual Machines (Infrastructure > Hosts > Virtual Machines) now have a group of advanced filters that can be activated when needed
- Custom Views: Many list view pages, such as Instances, Hosts, and Virtual Machines, allow custom views with user-selected output columns. Custom views can also be saved and set as the user's default
- Theme: New theme and styling for appliances which are not whitelabeled

Other Enhancements
------------------

- Agent Compatibility: SUSE SLES 12 and 15, OpenSUSE Leap agent installation support
- Appliance Compatibility: Amazon Linux 2 appliance installation support
- Appliance Compatibility: RHEL 8 and CentOS 8 appliance installation support
- Appliance Compatibility: SUSE SLES 12 and 15, OpenSUSE Leap appliance installation support
- Apps: The App owner can now be edited in Provisioning > Apps > (Selected App) > :guilabel:`EDIT`
- Blueprints: The Blueprint owner can now be edited or removed in Provisioning > Blueprints > :guilabel:`MORE` > Permissions
- Catalog: CentOS catalog items added for SCVMM, Hyper-V, and UpCloud Clouds
- Catalog: Amazon Linux 2 catalog items added
- Catalog: openSUSE 15.1 catalog items added for Amazon, VMware, Nutanix, OpenStack, KVM, and Hyper-V Clouds
- Convert to Managed: When converting an instance to managed and specifying a Layout tied to custom options (Option Types), the user is prompted with the same options as when provisioning a new Instance with that Layout. If Option Types are configured as required, this validation is also honored when converting to managed
- Convert to Managed: Added the option to apply tags when converting an Instance to managed. Tag policy validation (if applicable) also applies
- Docker: System Docker version upgraded to 19.03.8
- Identity Sources: SAML SSO and Azure AD SAML SSO now allow "Force Authn" in the Advanced Validation Options section of the create and edit identity source modals
- Layouts: Layouts can now be scoped to Groups making the list of available Groups at provision time much smaller in appliances that have many
- Licenses: Version column added to the License list view in Administration > Provisioning > Licenses
- Maintenance Mode: Drains active sessions and queues so an auto-scaling group can scale down. Can be enabled by System Administrators in Administration > Settings > Utilities > Toggle Maintenance Mode
- Option Lists: Option Lists can now be populated by LDAP queries
- Provisioning: |morpheus| will now retry some steps of the provisioning process when needed to prevent occasional node provisioning failure due to environmental factors when provisioning multiple Instances at once
- Puppet: |morpheus| integration now supports version 6+
- Roles: Added "Reconfigure Servers" permission (Full or None) to User Roles. When set to None, the user cannot resize or reconfigure from Instance or server detail pages
- Security: Set web security HTTP response headers for enhanced security
- ServiceNow: |morpheus| plugin now certified and available on Orlando
- Settings: Added the option to disable SSH password authentication in Administration > Settings > Appliance
- Users and Roles: Added view accessible from the User list view to see an individual User's effective Role permissions
- VMware vCenter: Removed "Customization Spec" provisioning option to prevent possible conflict with |morpheus|' own guest customization
- Veeam: |morpheus| Veeam integration now supports version 10

Fixes
=====

- Openstack: Fix for generic error message when Openstack quote is exceeded during provisioning. |morpheus| now displays Quota exceeded message with statistics in provisioning wizards.
- Openstack: Fix for secondary network interface IP address not displaying in UI.

- Apps: Fixe for datastore selection changing when layout was changed to ``Auto Datastore`` in App Wizard
- NSX-V: Fixed issue where firewall functionality for NSX integration was not applicable for all NSX objects
- Automation: Fix for Post Provision Tasks executing prior to finalization of Provision phase Config Management Tasks (Salt Stack)
- Shutdown Policies: Fixed for Extension banners not being displayed on Instances already shutdown from an active Shutdown Policy.
- Networks UI: Fix for sorting Network By Service in Networks list view resulted in page error.
- Clone Wizard: Fix for incorrect layout version displaying when cloning instances from VIO to native openstack
- PXE: Added support for <%=%> variable syntax in custom Kickstart files
- AWS: Unsupported RAW image formats removed from provisioning options.
- Openstack: Fix for Octavia Loadbalancer ephemeral ports for containers not being created within the backend listeners
- Backups: "Backup Retention Count" renamed to "Default Retention Count" in /admin/backup-settings
- ARM Templates: Fix for ARM Templates with ARM schema '2019-04-01' parsed as invalid json when using repo source
- Apps: Fix for some Option Type dependencies not being honored
- IBM Cloud: Fix for Inventory issue when using Proxy
- vCloud Director: Fix for specified service version not being honored when created a Cloud
- Openstack: Service Plans that do not meet the selected Image's minimum storage requirements are not filtered in Provisioning Wizards
- Cloud Formation: Fix for Task or Workflow execution on CF Instances
- Docker: Fix for updating the url of a Docker Registry Integration

- Azure API Error Provisioning Error
- Incorrect Syntax Error when deploying Apps for Helm Blueprint types
- Workflows do not populate option types upon execution when workflows page is not touched for about a minute
- Instance Type/Blueprints Tenant Role control not Working
- Java exception in the log while parsing list of networks from SCVMM
- Console for SCVMM Clouds do not connect,  just hang at Attempt
- Allow colon in active directory group name
- Adding a Volume to Azure Private Image Error
- Security group rules with source "all" are silently lost when syncing to Openstack
- Instance log tab is showing unrelated log entries
- Virtual Image Location Inaccurate
- Instances that have been shut off still displaying utilized CPU
- IP address on virtual machine inventory report inaccurate or missing
- Default Domain Not Inherited By Linux Builds
- Sub-tenant expired logged in session is redirected to main appliance login url.
- Nutanix images not syncing into cloud in master tenancy
- HyperV - can't delete instance with backup result
- Unable to authenticate Active Directory users with subdomain UPN
- When resizing a VMware VM the max_cpu field is not updated.
- Morpheus is syncing Azure SKUs that are not available within the scoped region.
- AWS Security Rules
- UI enables existing NIC modification on reconfigure modal
- Openstack clouds: reconfigure option - network interface
- ARM Template deployment issue
- Actions - Reconfigure on xenserver cloud
- Zerto Paging Error
- Azure CSP Price Lists
- OVM images are not being grouped similar to VmWare images
- Azure: Support Premium SSD Disks
- API payloads are being exposed in workflow execution logs
- Cloud sync on SCVMM cloud discovers all VMs within all clouds when SCVMM cloud is scoped on cloud config.
- has_auto_scale not flagged for supported nutanix system layouts
- Fixed Convert to Managed Instance record issue when vm name not unique

.. Issues with SCVMM (great story title)

|morpheus| API Updates
**********************

API Enhancements
================

- Amazon: Increased pricing granularity available for individual servers including for compute, storage, memory, and network
- Azure: Increased pricing granularity available for individual servers including for compute, storage, memory, and network
- Azure: Static IP addresses and IP pools supported on Azure Subnets
- Invoices: Invoice line items are now exposed through the API
- Licenses: Improved API coverage of licenses (Administration > Provisioning > Licenses)
- Ping: API supports "GET /api/ping" endpoint to replace "GET /setup/check". The new endpoint returns the same information
- Prices: Prices can be filtered by platform type

API Fixes
=========

- API/CLI: Fixed Security Group 'canManage' Flag not consumable via API
- API/CLI: Fixed IndexOutOfBounds when updating price-set over API
- API/CLI: Fixed IndexOutOfBounds when updating price-set over API
- API/CLI: Fixed Adding subnet permissions through API call returns incorrect status
- API/CLI: Fixed CLI | Adding the vCD cloud type using the cli fails to add Cloud

|morpheus| CLI Updates
**********************

CLI Enhancements
================

Enhancements
^^^^^^^^^^^^
- Prompt for credentials by default, instead of erroring. This was the behavior a long time ago, and now it is once again.
- Improved output of ``remote list`` and ``remote get``
- Changed ``remote get`` to refresh status and version by default, can use option ``--offline`` to avoid this.
- Changed ``remote`` get to work like ``remote current`` when called with 0 arguments
- New subcommand ``remote version``.
- New subcommand ``remote view``.
- New command ``setup`` that works like remote setup
- New command ``ping`` that works like remote check
- New command ``activity`` that works like ``recent-activity``
- Deprecated ``recent-activity``
- Updated ``instances`` command renaming options ``--created-by`` to ``--owner``
- Updated ``apps`` command to show Owner.
- Updated ``blueprints`` command to support Owner.
- Updated ``blueprints`` and ``apps`` command to show more information.
- Updated ``invoices list -c CLOUD`` so that name can be passed instead of just id.
- New option ``apps update --owner``.
- Removed deprecated command ``instances update-notes``.
- New subcommand ``library-layouts update-permissions``.
- Changed the way role permission access values displayed, so they look more like a grid and full is green, while other values are cyan.
- New option ``workflows list --type``.
- New options ``--wrap`` and ``--all-fields`` for all list commands.
- New option ``remote check --all`` that works just like ``remote check-all``.
- New option ``curl -v``.
- Updated command ``groups current`` to support ``--remote`` option.
- Updated command ``apps add Environment`` prompt to be a select instead of text.
- Updated ``apps list`` and apps get to display Environment
- Changed No records found messages to be cyan instead of yellow.
- New option ``--can-manage`` for ``security-groups add/update``.
- Changed workflows get to just show ``TASK ID`` in the tasks list, and no longer display ``ID`` ('taskSetTaskId').
- Renamed ``'Tags'`` to ``'Labels'`` in instances get
- Renamed option ``--tags`` to ``--labels`` for instances add.
- Added options ``--labels`` and ``--metadata`` to ``instances add``
- Updated command ``users permissions`` and ``users get --all`` to show all access. requires api 4.2.1
- Updated command ``whitelabel-settings`` to support ``--account`` option. requires api 4.2.1
- New subcommand ``clouds refresh``. requires api 4.2.1
- New command ``guidance``. requires api 4.2.1
- Some of these enhancements require remote version 4.2.1 to behave properly.
- Updated command invoices to show more info and make ``--raw-data`` an option.
- New command ``invoices``
- New subcommand service-plans activate

Fixes
^^^^^
- Fixed ping resulting in an error when used on older appliances. Now it falls back to use ``/api/setup/check`` instead of erroring.
- Fixed remote setup error and also improved error handling for ``setup --remote-url`` with an insecure url.
- Fixed error seen with ``instances import-snapshot``
- Fixed instances add payload duplicating plan.
- Grooming of help info for instances, apps and blueprints.
- Fixed ``--quiet`` option still printing a newline.
- Fixed issues with ``--remote-url`` option, it could cause errors or otherwise behave incorrectly.
- Fixed issue with instances add using the wrong version when specified with ``-O layout=ID`` instead of ``--layout ID``
- Fix library-layouts get ID 404 error incorrectly saying ``'Instance Type not found'``
- Fix clouds add not merging ``-O options`` into the payload
- Fixed invoices cost display issues
- Fix apps add including ``-O networkInterface`` options when the blueprint has that field locked. This fixes potential serverside error ``'ip address required'``.
- Fix users permissions error when using older appliance versions.
- Fix apps add not using blueprint values for layout,plan,networks,volumes,etc.
- Fix apps add not printing some error messages eg. ``'name must be unique'``.
- Fix instances add ``--security-groups`` causing invalid argument error.
- Fix instances add infinite name must be unique error when --no-prompt is used.
- Fix passwd extraneous output ``'args is'``.
- Fixes for new invoices command.
- Fixed clouds add groups dropdown being limited to 25.
- Fixed multiselect option types not working when passed in eg. ``--tenants "one, two"``
- Fixed instances add requiring Library permission to fetch layout.
- Fixed instances add requiring Clouds permission to fetch datastores.
- Fixed instances add potential 500 error when retrieving datastores.
- Fixed 404 error when fetching layout seen when pointing at appliance versions older than 4.2. This change is to use ``/library`` instead of ``/library/instance-types`` when for those resources.

CVEs Addressed
==============

- CVE-2017-18640
- CVE-2019-12418

Service Version Changes
=======================

- ElasticSearch: Upgraded to 7.6.2 from 7.6.1
- Erlang: Upgraded to 22.3 from 22.0
- NGINX: Upgraded to 1.17.9 from 1.17.6
- OpenJDK JRE: Upgraded to 8u252 from 8u242
- OpenSSL: Upgraded to 1.0.2u from 1.0.2t
- RabbitMQ: Upgraded to 3.8.3 from 3.7.16
- Tomcat: Upgraded to 3.0.33 from 9.0.31
