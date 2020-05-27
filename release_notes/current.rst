.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading to |morpheus| |morphver|.

|morpheus| UI Updates
*********************

Highlights
==========

Full integration with **VMware NSX-T**

- Create and manage software-based virtual networks efficiently and programmatically
- Sync, edit, create, and manage transfer zones, distributed firewalls, edge gateways, load balancers and more

.. image:: /images/releases/421/nsxt.png

Full integration with **Unisys Stealth**

- Protects sensitive systems with identity-driven microsegmentation
- Sync, create, and manage roles and communities of interest (COIs)
- Assign Stealth configuration at provision time

.. image:: /images/releases/421/stealth.png

Keep more **Task** types under version control with expanded Git integration for automation

- Email Tasks, jRuby scripts, and shell scripts can now be kept under Git version control
- |morpheus| runs the current version of the script at execution time

.. image:: /images/releases/421/task.png

**Usability and navigation** improvements

- Advanced filtering for Instance, Host, VM, and Bare Metal server lists
- Create custom views for Instance, Host and VM lists and set them as your default view
- Refreshed default theme for improved visibility and enhanced contrast (does not affect whitelabeled appliances)
- Drag and drop columns in large list views to bring the most relevant information to the forefront

.. image:: /images/releases/421/advanced_filters.png

Enhanced existing **public and on-prem cloud** integrations

- Updated support for the latest version of Azure Kubernetes Service (AKS) and premium SSD tiers in Microsoft Azure cloud
- Expanded |morpheus| tagging policies to include Google Cloud Platform in addition to previously supported clouds
- Sync real-time pricing data from Oracle Cloud in addition to clouds that previously supported live pricing data
- Slice a single SCVMM cluster into a fully multi-tenant private cloud

All New Features
================

- Agent Compatibility: SUSE SLES 12 and 15, OpenSUSE Leap agent installation support
- Appliance Compatibility: Amazon Linux 2 appliance installation support
- Appliance Compatibility: RHEL 8 and CentOS 8 appliance installation support
- Appliance Compatibility: SUSE SLES 12 and 15, OpenSUSE Leap appliance installation support
- Apps: The App owner can now be edited in Provisioning > Apps > (Selected App) > :guilabel:`EDIT`
- Azure: Kubernetes AKS version updated to v1.15 (replaces 1.13)
- Azure: Premium SSD disk types are now supported
- Azure: Static IP address assignment now supported
- Blueprints: The Blueprint owner can now be edited or removed in Provisioning > Blueprints > :guilabel:`MORE` > Permissions
- Convert to Managed: Options Types are now supported when converting a resource to managed and selecting a custom layout with associated Option Types.
- Convert to Managed: Tags are now supported when converting an Instance to managed. Tag policy validation (if applicable) also applies
- Docker: System Docker version upgraded to 19.03.8
- Google: Static IP address assignment now supported
- Google: Tag compliance policies are now supported for Google clouds, including scanning of existing resources and banner display for non-compliant machines
- Identity Sources: SAML SSO and Azure AD SAML SSO now allow "Force Authn" in the Advanced Validation Options section of the create and edit Identity Source modals
- Layouts: Group Access Permissions added to Instance Type Layouts.
- Library: Amazon Linux 2 added to System Library for AWS Clouds
- Library: openSUSE 15.1 added to System Library for for Amazon, VMware, Nutanix, OpenStack, KVM, and Hyper-V Clouds
- Licenses: Version column added to the License list view in Administration > Provisioning > Licenses
- Morpheus UI: Advanced Filters added including Tag Name, Clusters, Instance Type, Resource Pool, and Plan filters on Instance, Host, VM and Bare Metal list views.
- Morpheus UI: Instance, Host, VM and Bare Metal list view columns can now be arranged via drag and drop
- Morpheus UI: New top level Status filters added to Instance, Host, VM and Bare Metal list views
- Morpheus UI: Updated default System Theme with refreshed Logo, Icons and Colors.
- Morpheus UI: Views added for Instance, Host and Virtual Machine list views
- Network: Stealth Security Service Integration added
- NSX: NSX-T Integration added
- OpenStack: Rocky, Stein, and Train added to Openstack Version options.
- Option Lists: New LDAP Option List type added
- Oracle Cloud: |morpheus| now syncs in pricing/costing data for Oracle Cloud Resources
- Oracle Cloud: Added support for new Regional-type subnets
- Oracle Cloud: Costing data added to Oracle Cloud summary tab, including current, estimated, historical and per service data.
- Provisioning: Retry attempts added to IP Pool address allocation when initial allocation fails
- Puppet: The |morpheus| Puppet integration now supports version 6+. Note: Puppet versions prior to 6 are no longer supported.
- Roles: "Reconfigure Servers" Feature Access permission added (Full or None). When set to None, Instance and Host Reconfigure Actions will not be available for applicable users
- SCVMM: Multiple |morpheus| SCVMM Clouds can now be pointed to the same SCVMM controller. Please note multiple Morpheus Appliances pointed to the same SCVMM controller is not yet supported.
- ServiceNow: |morpheus| plugin now certified and available on Orlando
- Settings: ``Disable SSH Password Authentication`` option added to Administration > Settings > Appliance
- Tasks: Email: Git Repository support added for Email Task content source
- Tasks: Email: Whitelabel support added for Email Task types
- Tasks: jRuby Script: Git Repository support added for jRuby Task script source
- Tasks: Powershell Script: Git Repository support added for Powershell Task script source
- Tasks: Python: Virtual environment are now used for Python Tasks. Note: ``virtualenv`` is required on all Appliance App nodes. ``pip install virtualenv``
- Tasks: Shell Script: Git Repository support added for Shell Task script source
- Users: Effective Role Permissions added to User detail pages to assist in determining effective permissions for a User with multiple roles
- Utilities: Maintenance Mode added. Maintenance Mode drains active sessions and queues to support auto-scale down of |morpheus| Appliance nodes. Note: System Administrator Role required to access ``admin/settings#!utilities``.
- Veeam: |morpheus| Veeam integration now supports Veeam version 10
- VMware: Removed "Customization Spec" provisioning option to prevent possible conflict with |morpheus| triggered Guest Customization
.. - Catalog: CentOS catalog items added for SCVMM, Hyper-V, and UpCloud Clouds

Fixes
=====

- ARM Templates: Fix for ARM Templates with ARM schema '2019-04-01' parsed as invalid json when using repo source
- AWS: Fixed synced Security Group Rule "Source" field value
- AWS: The Name value for synced Security Group Rules will now equal the source rules Description value if populated in AWS. If Description is not populate, Port Range will continue to be used for the Security Group Rule Name
- AWS: Unsupported RAW image formats removed from provisioning options.
- Active Directory: Fixed issue with User authentication when a Users domain suffix contains numbers
- Active Directory: Fixed issue with colons in active directory group names
- Apps: Fix for some Option Type dependencies not being honored
- Apps: Fixe for datastore selection changing when layout was changed to ``Auto Datastore`` in App Wizard
- Automation: Fix for Post Provision Tasks executing prior to finalization of Provision phase Config Management Tasks (Salt Stack)
- Azure: Added support for creating additional Volumes on Azure Private Images at provision time (Previously only supported on Reconfigure)
- Azure: Fixed "StandardSSD_LRS" API Version issue
- Azure: Fixed syncing of Service Plans that are not available in scoped Azure Region
- Backups: "Backup Retention Count" renamed to "Default Retention Count" in /admin/backup-settings
- Blueprints: Fixed incorrect Syntax error for Helm Blueprint types
- Clone Wizard: Fix for incorrect layout version displaying when cloning instances from VIO to native openstack
- Cloud Formation: Fix for Task or Workflow execution on CF Instances
- Convert to Managed: Fixed `Convert to Managed` Instance record creation issue when the source VM name matches existing Instance name (Instance Name uniqueness constraint).
- Docker: Fix for updating the url of a Docker Registry Integration
- Domains: Fixed Cloud Default Domain setting not applying to Domain Joins when Domain not set on Network
- HyperV: Fixed Instance deletion issue when Instance record has associated Backup Results
- IBM Cloud: Fix for Inventory issue when using Proxy
- Instances: Fixed existing Network Interface fields not set to Read-Only in Reconfigure modal
- Jobs:  Fixed Execution logs including associated Morpheus process logs
- Logs: Fixed rare condition where Instance Log tab would include unrelated log entries
- NSX-V: Fixed issue where firewall functionality for NSX integration was not applicable for all NSX objects
- Networks UI: Fix for sorting Network By Service in Networks list view resulted in page error.
- Nutanix Fixed partial Virtual Image sync when the same Nutanix cluster is added to Master Tenant and Subtenant Clouds
- Nutanix: Added auto-scaling support for system Nutanix Tomcat layouts
- Openstack clouds: Fixed creation of additional Network Interfaces during Reconfigure
- Openstack: Fix for Octavia Loadbalancer ephemeral ports for containers not being created within the backend listeners
- Openstack: Fix for generic error message when Openstack quote is exceeded during provisioning. |morpheus| now displays Quota exceeded message with statistics in provisioning wizards.
- Openstack: Fix for secondary network interface IP address not displaying in UI.
- Openstack: Fixed issue creating Security Group Rules with source "all"
- Openstack: Service Plans that do not meet the selected Image's minimum storage requirements are not filtered in Provisioning Wizards
- PXE: Added support for <%=%> variable syntax in custom Kickstart files
- Reports: Fixed Instance Inventory Summary report displaying deprecated ``max_cpu`` instead of ``max_cores``
- Reports: Virtual Machine Inventory Report: All IP Addresses are now shown on VM's with multiple IP Addresses.
- Reports: Virtual Machine Inventory Report: VM's that have been stopped now display 0% CPU utilization instead of last reported %. Note the updated CPU % can take up to 5 minutes to update.
- Roles: Fixed Tenant Role Instance Type and Blueprint Access propagation
- SCVMM: Fixed overzealous SCVMM discovery when |morpheus| SCVMM Cloud config is scoped to a single SCVMM Cloud.
- Shutdown Policies: Fixed for Extension banners not being displayed on Instances already shutdown from an active Shutdown Policy.
- Tenants: Fixed expired Subtenant ui session not redirecting to subtenant login url.
- VMware: Fixed synced Virtual Image Location record issue
- Wiki: Fixed \`code\` and \`\`\` code block \`\`\` syntax display
- Workflows: Fixed timeout issue with Option Types not loading when /automation/workflow page that has been open for several minutes
- Zerto: Fixed paging error on Replication Sites list views.
- vCloud Director: Fix for specified service version not being honored when created a Cloud

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
- Updated command ``invoices`` to show more info and make ``--raw-data`` an option.
- New command ``invoices``
- New subcommand service-plans activate

Fixes
^^^^^
- Fixed ``ping`` resulting in an error when used on older appliances. Now it falls back to use ``/api/setup/check`` instead of erroring.
- Fixed ``remote setup`` error and also improved error handling for ``setup --remote-url`` with an insecure url.
- Fixed error seen with ``instances import-snapshot``
- Fixed ``instances add`` payload duplicating plan.
- Grooming of help info for instances, apps and blueprints.
- Fixed ``--quiet`` option still printing a newline.
- Fixed issues with ``--remote-url`` option, it could cause errors or otherwise behave incorrectly.
- Fixed issue with instances add using the wrong version when specified with ``-O layout=ID`` instead of ``--layout ID``
- Fixed ``library-layouts get ID`` 404 error incorrectly saying ``'Instance Type not found'``
- Fixed ``clouds add`` not merging ``-O options`` into the payload
- Fixed ``invoices`` cost display issues
- Fixed ``apps add`` including ``-O networkInterface`` options when the blueprint has that field locked. This fixes potential serverside error ``'ip address required'``.
- Fixed users permissions error when using older appliance versions.
- Fixed ``apps add`` not using blueprint values for layout,plan,networks,volumes,etc.
- Fixed ``apps add`` not printing some error messages eg. ``'name must be unique'``.
- Fixed ``instances add --security-groups`` causing invalid argument error.
- Fixed ``instances add`` infinite name must be unique error when --no-prompt is used.
- Fixed passwd extraneous output ``'args is'``.
- Fixes for new invoices command.
- Fixed ``clouds add`` groups dropdown being limited to 25.
- Fixed multiselect option types not working when passed in eg. ``--tenants "one, two"``
- Fixed ``instances add`` requiring Library permission to fetch layout.
- Fixed ``instances add`` requiring Clouds permission to fetch datastores.
- Fixed ``instances add`` potential 500 error when retrieving datastores.
- Fixed 404 error when fetching layout seen when pointing at appliance versions older than 4.2. This change is to use ``/library`` instead of ``/library/instance-types`` when for those resources.
