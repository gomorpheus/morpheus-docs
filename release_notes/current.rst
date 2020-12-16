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

- .. toggle-header:: :header: **Azure Cloud Integration Enhancements**

    - Azure Marketplace images now synced by region rather than by Cloud :superscript:`+`
    - Azure pricing now synced by region and currency rather than Cloud :superscript:`+`
    - Azure VM sizes (Service Plans) now synced by region rather than Cloud :superscript:`+`

- .. toggle-header:: :header: **Budget Enhancements**

    - Budgets based on a yearly interval can now start on a month other than January
    - Multi-year budgets, up to three years, are now supported

- NSX-V: Create and manage SNAT rules from the NAT tab of the Edge Gateway detail page of an NSX-V network integration
- Option Types: Custom help block text can now be displayed with any Option Type
- Security Scanning: Windows support added for SCAP security scans :superscript:`+`
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

- .. toggle-header:: :header: **Invoices Improvements**

    - Invoice tags can now be updated, added and removed through API/CLI
    - Lists of invoices can be filtered by tags (API only, for now)
    - Subtenant users now only see prices (not costs) for Instances provisioned to Clouds owned by the Master Tenant and assigned to the Subtenant when calling the Invoices API

- Metadata: Metadata tags now referred to as ``tags`` and labels now referred to as ``labels``, previously metadata tags were referred to as ``metadata`` and labels were referred to as ``tags`` :superscript:`+`
- Snapshots: Create and view snapshots :superscript:`+`

- .. toggle-header:: :header: **Virtual Images**

    - Associated ``volumes`` are returned with ``maxStorage`` viewable for each :superscript:`+`
    - Added ability to tag Virtual Images (currently API only) :superscript:`+`

Fixes
=====

- Administration: Monitoring Settings: Fixed Validation error for monitoring availability timeframe causes 500 error
- Ansible Galaxy: Fixed group permisison issue on folders created in Roles by Ansible Galaxy
- API/CLI: Fixed issue with Morpheus Network Pool creation 
- Backups: Fixed Backup job Tenant visibility issue
- Backups: Fixed issue restoring a preserved backup to a new Instance after VM deletion.
- Backups: Fixed issue with creating a new backup configuration from an Instance for external Backup providers and selecting "Create and Run".
- Commvault: Fixed when restoring a instance that has been backed up via commvault the instance stays within the restore state after the vm has been restored.
- Google Cloud: Fixed image sync issue where not all Windows 2019 images were available
- Instances: When editing an Instance, the cursor now focuses on NAME field instead of DESCRIPTION field. 
- Kubernetes: Fixed service endpoint config issue when going back in wizard to change cloud during Cluster creation
- Networks: Fixed issue with Interface Label association when removing Interfaces during Reconfigure.
- New Ansible Tower Task Modal | Missing Job Templates
- NSX-V: Fixed distributed firewall rules not displayed in order of priority
- NSX: Fixed NSX Edge Logical Router (DLR) Firewall rules remote change sync
- NSX: If you attach an IP pool to a NSX-v network as a sub-tenant, that IP pool is now visible from the network detail page
- Policies: When using multiple Naming Policies, Tenant assigned Policies will take precedence over a Global policy. 
- Tags: Fixed Null Tags causing Provisioning -> Instances to throw Permission Denied
- VCD: no reboot warning when adding IP
- vCloud Director: Fixed incorrect NIC index sent to VCD on reconfigure
.. - Multiple RDS Issues


- SCAP scan view fix
- API: Push check returns 401 unauthorized for the api key
- Analytics: Utilization vs. cost showing in $
- Warning emails not received for expiring Instances
- Output not displaying in powershell tasks in post provisioning phase of workflow
- Custom Image upload to OTC || Custom Library item
- After Deletion - VMs still powered on
- Extend Character Limitation on Instance Table Columns
- legacy cert modal displayed when no trust provider integration has been added
- Members don‚Äôt get added to NSX-V pool
- NSX-V Virtual Server issue
- NSX-T Routers tab fails to load
- Tags not removing
- List of hosts/instances differs between UI and API
- Creating Blueprints using Azure Spec templates hangs with "Loading configuration"
- Approval policies break and prevent VM deployment
- NSX-v: DLR showing up in the create network page which is group scoped
- Unable to add new Firewall rules in the DLR created with the group scope
- HA K8s Doesn't Work
- Morpheus does not create PTR records using Infoblox integration
- Ansible Tower tasks are not executed as Jobs in Tower
- API: Get a Specific Approval: 403 error when calling on app
- Nutanix provision - hide datastore selection on root disk - add cluster
- Search field app opens create new app window when hit enter
- NSX Network routing functionality is getting removed while trying to delete the network
- Limited Column in network_security_group table
- UI error message doesn‚Äôt surface for the used NSX networks deletion
- Agent install fails on VMware instances when convert to managed
- New NSX-T segment created from morpheus defaults to the first TZ after creation
- Unable to create ICMP rule on AWS Security Group
- NSX-t integration causing lots of error log chatter
- Command for creating new instance cannot specify Group Name with JSON file
- Network Flashes / disappears if Group access is lost on the network permission
- NSX-T distributed firewall rules not displayed in order of priority creation
- English (South Africa): Cost/Sale Price change on Save because of comma decimal
- Pricing/Billing discrepancies from currency conversion inconsistencies.
- Persona tab doesn‚Äôt get cloned
- Spinning ball - Activity History Details
- Status for applications and instances in AWS ( No Agent)
- Global Access "None" in Group permission not working correctly
- User role Network permission with Group shouldn‚Äôt provide access to All groups
- File >2GB fails to upload to Azure-backed archive
- Required field in operational workflows not being enforced
- Activity History Details not shown with expansion arrow
- containerid.domain using ansible
- If role provision tasks are set to none the option list doesn't present
- Filtering for Platform Field on Workflow Not Working
- Nutanix: Hypervisor stats no longer sync
- VMware: Docker Cluster Creation Module is not inheriting VM template disk size
- Checkbox option type value defaults to NULL instead of off on load.
- CSS issues with language translation
- Existing backup job not found
- Service plan name doesn‚Äôt refresh after reconfigure
- Users with "view" on backup perms shown Delete options for failed executions
- Reports: Tenant Filter - remove 'All' placeholder text
- Public images in OpenStack not listed on provisioning
- VCD 10 - Virtual Images not syncing
- 500 error in UI while accessing IP Pool with large set of used IPs
- VMware: Bulk datastore assignment to tenants
- help_block on pythonAdditionalPackages option type shows incorrect syntax
- Amazon | Backup and Restore new instance failure when using public image on "EC2 Instance" instance type
- Azure | Backup and Restore new instance failure when using "Microsoft Azure" instance type
- InstanceTypes with periods in the name cause issues with Environment Prefixes
- Router Policy does not work
- Storage bucket duplication for Public clouds
- Disk layout changes on APP provisioning when selecting different layouts
- NSX-V Sync Issue: Cloning VM template while provisioning instance is expecting property "uuid"
- Hidden text fields not refreshed in blueprints
- No Validation for GIT repository integration
- NSX-v Load Balancers: Persistence info not updating when set to ‚ÄòNone‚Äô on edit



.. - EL8 offline installer stuck at powertools makecache- need clarity on exact versions imapcted 
.. - Upgrade to 5.2.0 from 4.2.4 fails during reconfigure- not done


.. NOTE:: :superscript:`+` indicates items also released in v4.2.5







..
  Appliance Updates
  =================

  .. not sure if we should have separate appliance/installer updates, adding here for now

  - Support added for Installing |morpheus| on Ubuntu 20.04
  - Java: Openjdk-jre updated to 8u275
  - Appliance Logs: Default log rotation added for Nginx and Tomcat logs //add paths & files
  - Installer: ``iptables_bach`` setup bash script moved from /tmp to /opt/morpheus/embedded/bin and renamed to iptables_morpheus.rules. Resolves reconfigure issue for systems with ``noexec`` set on ``/tmp``.
  - Installer: Morpheus can now be installed on el8 
  Agent/Node Package Updates
  ==========================

  .. same

  - Java: openjdk and openjdk-jre updated to 8u275
  - Node and VM Node package versions updates to 3.1.11
  - FIPS mode supported now for el8
  .. add agent package version vars/list to compatibility?
  
