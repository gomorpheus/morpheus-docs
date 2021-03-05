.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: This list includes improvements that were initially provided in version 4.2.5. Those feature items are marked with :superscript:`+`.

.. Small Update, omitting highlights this time
  .. include:: highlights.rst

New Features
============

- Amazon AWS Integration: Amazon cost explorer pricing has been brought back for integrations without a costing report configured

- .. toggle-header:: :header: **Azure Marketplace Images, Pricing, and VM Sizes Synced by Region**

    - Azure Marketplace images now synced by region rather than by Cloud :superscript:`+`
    - Azure pricing now synced by region and currency rather than Cloud :superscript:`+`
    - Azure VM sizes (Service Plans) now synced by region rather than Cloud :superscript:`+`

- .. toggle-header:: :header: **Multi-year Budgets with Custom Fiscal Year Periods**

    - Budgets based on a yearly interval can now start on a month other than January
    - Multi-year budgets, up to three years, are now supported

    .. image:: /images/operations/multiBudget.png
      :width: 50%

- NSX-V: Create and manage SNAT rules from the NAT tab of the Edge Gateway detail page of an NSX-V network integration
- Option Types: Custom help block text can now be displayed with any Option Type
- Security Scanning: Windows support added for SCAP security scans :superscript:`+`
- Security Scanning: Security Drift view section added to the Software tab on Virtual Machine Detail pages. When SCAP security scans are run, data related to changes in security posture compared to prior scans is displayed
- ServiceNow: Plugin version 3.0 now available on the ServiceNow store, see `integration guide <https://morpheusdata.com/wp-content/uploads/content/ServiceNow-Cloud-Management-Morpheus-CMP-1.pdf>`_ for new features and complete use instructions
- Tags: |morpheus| `naming variables <https://docs.morpheusdata.com/en/latest/troubleshooting/Variables_Examples.html?highlight=naming%20policy#pre-provision-vars>`_ can be used as tag values for Instances and VMs/servers at provision time
- Tenants: Account Name, Account Number and Customer Number values tracked on the Tenant are now resolveable from naming variables: ``${accountName}``, ``${accountNumber}``, and ``${customerNumber}``

- .. toggle-header:: :header: **UI and Usability Improvements**

    - Tokens in forgot/reset password email now expire after seven days :superscript:`+`
    - Network REF UUID now appears on the Network tab of the server detail page for bare metal hosts

- Virtual Images: A "FIPS Compliant Image?" checkbox has been added to the Add/Edit Virtual Image modal. When checked, |morpheus| will install the FIPS-compliant Agent package

|morpheus| API & CLI Improvements
=================================

- Dashboard: ``dashboard`` command added to give a high level overview of |morpheus| activities such as aggregate Instance usage data, monitoring alerts, backup event alerts, recent user activity, and more
- Hosts: Added ability to tag servers (hosts). These are automatically updated when Instance tags are updated but useful for tagging discovered servers (currently API only) :superscript:`+`
- Instances: Passing ``masked=true`` flag for tags masks the value of the tag :superscript:`+`

- .. toggle-header:: :header: **Invoices Tagging and Other Improvements**

    - Invoice tags can now be updated, added and removed through API/CLI
    - Lists of invoices can be filtered by tags (API only, for now)
    - Subtenant users now only see prices (not costs) for Instances provisioned to Clouds owned by the Master Tenant and assigned to the Subtenant when calling the Invoices API

- Metadata: Metadata tags now referred to as ``tags`` and labels now referred to as ``labels``, previously metadata tags were referred to as ``metadata`` and labels were referred to as ``tags`` :superscript:`+`
- Snapshots: Create and view snapshots :superscript:`+`

- .. toggle-header:: :header: **Virtual Image Volumes and Tagging Enhancements**

    - Associated ``volumes`` are returned with ``maxStorage`` viewable for each :superscript:`+`
    - Added ability to tag Virtual Images (currently API only) :superscript:`+`

Fixes
=====

- Amazon: Fixed a potential backup and restore failure when using public images on "EC2 Instance" Instance type
- Activity: Fixed an issue where Activity History details were not shown when activating the expansion arrow
- Activity: Fixed loading issue with Activity History Details for some Activity types
- Administration: Monitoring Settings: Fixed an issue where the validation error for monitoring availability timeframe could cause a 500 error
- Amazon: Fixed Instance Status sync when not using |morpheus| Agent
- Analytics: Utilization vs. Cost dashboard showing prices in whole dollars
- Ansible Galaxy: Fixed group permission issue on folders created in Roles by Ansible Galaxy
- Ansible Tower: Fixed tower job sync issue causing existing tasks to not trigger job in Tower. Existing tasks should be edited and saved to rebind.
- Ansible: Fixed Inventory displaying containerid.domain for Instances that were converted to managed.
- API/CLI: Fixed ``--group parameter`` override when using json payload for Instance config --group parameter
- API/CLI: Fixed ``/monitoring/push`` 401 error
- API/CLI: Fixed error on ``GET /api/approvals/${id}`` / ``morpheus approvals get ${id}``
- API/CLI: Fixed issue with Morpheus Network Pool creation
- Apps: Fixed pressing `Enter` opening App Provision wizard when cursor focus is in App search field
- Apps: Fixed disk layout changes on App provisioning when selecting different layouts
- AWS: Fixed AWS Security Group ICMP rule creation
- Azure: Fixes File >2GB fails to upload to Azure-backed archive
- Azure: Fixed a potential backup and restore failure when using public images on "Microsoft Azure" Instance type
- Backups: Fixed Backup Job visibility issue for Tenants
- Backups: Fixed issue restoring a preserved backup to a new Instance after VM deletion
- Backups: Fixed issue with creating a new backup configuration from an Instance for external Backup providers and selecting "Create and Run"
- Blueprints: Fixed an issue where creating Blueprints using Azure Spec templates could hang with "Loading configuration"
- Blueprints: Fixed an issue related to hidden text fields not refreshing in Blueprints
- Commvault: Fixed an issue when restoring an Instance that has been backed up via Commvault and the Instance would stay in the restore state after the VM has been restored
- Git Integration: Successful connection validation added when creating Git repository integrations
- Google Cloud: Fixed an image sync issue where not all Windows 2019 images were available
- Infoblox: PTR records can now be automatically created during provisioning
- Instance Types: Fixed issues with environment prefixes on Instance Types with periods in their name
- Instances: ``unformatted_name`` and ``unformatted_host_name`` Field Types updates to LONGTEXT
- Instances: Fixed an issue where the list of Instances or hosts differs between the UI and API
- Instances: When editing an Instance, the cursor now focuses on NAME field instead of DESCRIPTION field
- Keys & Certs: Fixe an issue where the legacy Add Certificate modal could be displayed when no trust provider integration has been added
- Kubernetes: Fixed service endpoint configuration issue when going back a step in the wizard to change cloud selection during Cluster creation
- Networks: Fixed issue with Interface Label association when removing Interfaces during a reconfigure
- Networks: Fixed potential 500 errors in while accessing IP Pools with a  large set of used IPs
- Networks: Network Security Group ``externalId`` character limit expanded to 512
- New NSX-T segment created from morpheus defaults to the first TZ after creation
- NSX-T: Fixed an issue where distributed firewall rules were not displayed in order of priority
- NSX-T: Fixed an issue where the Routers tab could fail to load
- NSX-T: Reduced the amount of log chatter created by an NSX-T integration
- NSX-V: "Infrastructure: Network Router Firewalls" permission added addresses new Firewall DLR visibility and creation permissions
- NSX-V: Fixed distributed firewall rules not displayed in order of priority
- NSX-V: Fixed DLR Group scoping visibility issue
- NSX-V: Fixed load balancer member association with created pool during provisioning
- NSX-V: Fixed load balancer persistence info not updating when set to "None" after edit and save
- NSX-V: Fixed sync issue when cloning VM template while the provisioning Instance is expecting property "uuid"
- NSX: Added validation to SNX network deletion to prevent removal of associations when Network deletion does not succeed
- NSX: Fixed NSX Edge Logical Router (DLR) Firewall rules remote change sync
- NSX: If you attach an IP pool to an NSX-V network as a Subtenant, that IP pool is now visible from the Network Detail page
- Nutanix: Fixed Hypervisor stat sync
- Nutanix: Root disk Datastore is no longer selectable and defaults to the templates datastore as required by Nutanix
- OpenStack: Fixed an issue where public images in OpenStack were  not listed on provisioning
- Option Types: Checkbox option type values previously defaulted to NULL rather than OFF on initial load
- OTC: Fixed minimum disk size issue with local RAW images provisioned to OTC
- Policies: Fixed an issue where Approval policies could break and prevent VM deployment
- Policies: Fixed an issue with Router Quota policies
- Policies: Fixed and issue where warning emails were not received for expiring Instances
- Policies: Fixed Instances in Pending Removal State powering back on due to Power Schedules or Availability service
- Policies: When using multiple Naming Policies, Tenant-assigned Policies will take precedence over a Global policy
- Prices: Corrected potential pricing or billing discrepancies created by currency conversion inconsistencies
- Prices: Fixed l8n issue with South Africa English and decimal places
- Reconfigure: Fixed existing networks hiding on reconfigure when networks are not accessible from network Group Access permissions.
- Reports: "All" placeholder text removed from Tenant filter on Reports
- Roles: Fixed an issue where Global Access set to "None" on the Group Permissions tab was not working correctly
- Roles: Fixed Persona tab config not cloning when copying a Role
- Roles: Fixed an issue where users with "view" permission on "Backup" were shown delete options for failed executions
- SCAP Scans: Fixed a display issue for SCAP scan results
- Service Plans: Fixed an issue causing service plan names not to refresh after a reconfigure
- Storage: Fixed storage bucket duplication for public clouds
- Tags: Fixed ``Null`` Tags causing ``Provisioning > Instances`` to throw Permission Denied
- Tags: Tags created from Option Types with Export as Tag enabled can now be deleted
- Tasks: The ``help_block`` under the Additional Packages field on a Python Task now shows a correct syntax example
- UI error message doesn‚Äôt surface for the used NSX networks deletion
- UI: Fixed CSS issues related to language translation
- User role Network permission with Group should not provide access to All groups
- VCD: No reboot warning when adding IP
- vCloud Director: Fixed incorrect NIC index sent to vCD on reconfigure
- vCloud Director: Fixed an issue causing Virtual Images not to sync for vCD 10
- VMware: Fixed an issue where |morpheus| Agent install could fail on VMware instances when converting to managed
- VMware: Fixed an issue where the Docker Cluster Creation Module was not inheriting the VM template disk size
- VMware: Fixed bulk datastore assignment for Tenants
- Workflows: Fixed the output not displaying in Powershell tasks in the Post Provisioning phase of Workflows
- Workflows: Required fields in operational workflows are now being enforced
- Workflows: Fixed an issue causing filtering Workflows by the platform field not to work correctly
- Installer: ``guacd['yum-power-tools-repo-baseurl']`` morpheus.rb config override added to specify yum powertools repo url
- New Ansible Tower Task Modal | Missing Job Templates
  - Existing backup job not found
  - If role provision tasks are set to none the option list doesn't present

.. NOTE:: :superscript:`+` indicates items also released in v4.2.5

Appliance Updates
=================

- Support added for Installing |morpheus| on Ubuntu 20.04
- Java: Openjdk-jre updated to 8u275
- Appliance Logs: Default log rotation added for Nginx and Tomcat logs //add paths & files
- Installer: ``iptables_bach`` setup bash script moved from /tmp to /opt/morpheus/embedded/bin and renamed to iptables_morpheus.rules. Resolves reconfigure issue for systems with ``noexec`` set on ``/tmp``.
- Installer: FIPS mode supported now for Amazon Linux 2

Agent/Node Package Updates
==========================

- Java: openjdk and openjdk-jre updated to 8u275
- Node and VM Node package versions updated to 3.1.11
- FIPS mode supported now for Amazon Linux 2 
