.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading |morpheus|

New Features
------------

- Amazon AWS Integration: Amazon cost explorer pricing has been brought back for integrations without a costing report configured
- Appliance Compatibility: Ubuntu 20.04 appliance installation is now supported

- .. toggle-header:: :header: **Multi-year Budgets with Custom Fiscal Years**

    - Budgets based on a yearly interval can now start on a month other than January
    - Multi-year budgets, up to three years, are now supported

- NSX-T: Priority field exposed for Firewall rules
- NSX-V: Create and manage SNAT rules from the NAT tab of the Edge Gateway detail page of an NSX-V network integration"
- Prices: Instances in a suspended state no longer incur prices set to be incurred "While Running" just as stopped Instances do not incur them
- Tags: Morpheus `naming variables <https://docs.morpheusdata.com/en/latest/troubleshooting/Variables_Examples.html?highlight=naming%20policy#pre-provision-vars>`_ can be used as tag values for Instances and VMs/servers at provision time
- Virtual Images: A “FIPS Compliant Image?” checkbox has been added to the Add/Edit Virtual Image modal. When checked, Morpheus will install the FIPS-compliant Agent package

API & CLI Enhancements
----------------------

- Dashboard: dashboard command added to give a high level overview of Morpheus activities such as aggregate Instance usage data, monitoring alerts, backup event alerts, recent user activity, and more

- .. toggle-header:: :header: **Invoice Tagging and Tenant Data Filtering Improvements**

    - Invoice tags can now be updated, added and removed through API/CLI
    - Lists of invoices can be filtered by tags (API only, for now)
    - Subtenant users now only see prices (not costs) for Instances provisioned to Clouds owned by the Master Tenant and assigned to the Subtenant when calling the Invoices API

Fixes
-----

- Activity: Fixed an issue where Activity History details were not shown when activating the expansion arrow
- Activity: Fixed loading issue with Activity History Details for some Activity types
- Administration: Monitoring Settings: Fixed an issue where the validation error for monitoring availability timeframe could cause a 500 error
- Amazon: Fixed a potential backup and restore failure when using public images on “EC2 Instance” Instance type
- Amazon: Fixed Instance Status sync when not using |morpheus| Agent
- Ansible Galaxy: Fixed group permission issue on folders created in Roles by Ansible Galaxy
- Ansible: Fixed Inventory displaying containerid.domain for Instances that were converted to managed.
- API/CLI: Fixed issue with Morpheus Network Pool creation
- Apps: Fixed pressing `Enter` opening App Provision wizard when cursor focus is in App search field
- Apps: Fixed disk layout changes on App provisioning when selecting different layouts
- AWS: Fixed AWS Security Group ICMP rule creation
- Azure: Fixes File >2GB fails to upload to Azure-backed archive
- Azure: Fixed a potential backup and restore failure when using public images on “Microsoft Azure” Instance type
- Backups: Fixed Backup Job visibility issue for Tenants
- Backups: Fixed issue restoring a preserved backup to a new Instance after VM deletion
- Backups: Fixed issue with creating a new backup configuration from an Instance for external Backup providers and selecting "Create and Run"
- Blueprints: Fixed an issue related to hidden text fields not refreshing in Blueprints
- Commvault: Fixed an issue when restoring an Instance that has been backed up via Commvault and the Instance would stay in the restore state after the VM has been restored
- Git Integration: Successful connection validation added when creating Git repository integrations
- Google Cloud: Fixed an image sync issue where not all Windows 2019 images were available
- Infoblox: PTR records can now be automatically created during provisioning
- Instance Types: Fixed issues with environment prefixes on Instance Types with periods in their name
- Instances: When editing an Instance, the cursor now focuses on NAME field instead of DESCRIPTION field
- Kubernetes: Fixed service endpoint configuration issue when going back a step in the wizard to change cloud selection during Cluster creation
- Networks: Fixed issue with Interface Label association when removing Interfaces during a reconfigure
- Networks: Fixed potential 500 errors in while accessing IP Pools with a  large set of used IPs
- Networks: Network Security Group ``externalId`` character limit expanded to 512
- New NSX-T segment created from morpheus defaults to the first TZ after creation
- NSX-T: Fixed an issue where distributed firewall rules were not displayed in order of priority
- NSX-T: Reduced the amount of log chatter created by an NSX-T integration
- NSX-V: Fixed distributed firewall rules not displayed in order of priority
- NSX-V: Fixed load balancer persistence info not updating when set to “None” after edit and save
- NSX-V: Fixed sync issue when cloning VM template while the provisioning Instance is expecting property “uuid”
- NSX: Added validation to SNX network deletion to prevent removal of associations when Network deletion does not succeed
- NSX: Fixed NSX Edge Logical Router (DLR) Firewall rules remote change sync
- NSX: If you attach an IP pool to an NSX-V network as a Subtenant, that IP pool is now visible from the Network Detail page
- Nutanix: Fixed Hypervisor stat sync
- Nutanix: Root disk Datastore is no longer selectable and defaults to the templates datastore as required by Nutanix
- OpenStack: Fixed an issue where public images in OpenStack were  not listed on provisioning
- Option Types: Checkbox option type values previously defaulted to NULL rather than OFF on initial load
- Policies: Fixed an issue with Router Quota policies
- Policies: When using multiple Naming Policies, Tenant-assigned Policies will take precedence over a Global policy
- Prices: Corrected potential pricing or billing discrepancies created by currency conversion inconsistencies
- Prices: Fixed l8n issue with South Africa English and decimal places
- Reconfigure: Fixed existing networks hiding on reconfigure when networks are not accessible from network Group Access permissions.
- Reports: "All" placeholder text removed from Tenant filter on Reports
- Roles: Fixed an issue where Global Access set to "None" on the Group Permissions tab was not working correctly
- Roles: Fixed an issue where users with “view” permission on “Backup” were shown delete options for failed executions
- Service Plans: Fixed an issue causing service plan names not to refresh after a reconfigure
- SCAP Scans: Fixed a display issue for SCAP scan results
- Storage: Fixed storage bucket duplication for public clouds
- Tags: Fixed ``Null`` Tags causing ``Provisioning > Instances`` to throw Permission Denied
- Tasks: The ``help_block`` under the Additional Packages field on a Python Task now shows a correct syntax example
- UI error message doesn‚Äôt surface for the used NSX networks deletion
- UI: Fixed CSS issues related to language translation
- User role Network permission with Group should not provide access to All groups
- vCloud Director: No reboot warning when adding IP
- vCloud Director: Fixed an issue causing Virtual Images not to sync for vCD 10
- vCloud Director: Fixed incorrect NIC index sent to vCD on reconfigure
- VMware: Fixed an issue where |morpheus| Agent install could fail on VMware instances when converting to managed
- VMware: Fixed an issue where the Docker Cluster Creation Module was not inheriting the VM template disk size
- VMware: Fixed bulk datastore assignment for Tenants
- Workflows: Required fields in operational workflows are now being enforced
- Workflows: Fixed an issue causing filtering Workflows by the platform field not to work correctly
- Dashboard: Fix issue with red X shown with 0 Incident count

..
  - If role provision tasks are set to none the option list doesn't present
  - Existing backup job not found
  .. - EL8 offline installer stuck at powertools makecache- need clarity on exact versions imapcted
  .. - Upgrade to 5.2.0 from 4.2.4 fails during reconfigure- not done
  - New Ansible Tower Task Modal | Missing Job Templates

Appliance Updates
=================

- Support added for Installing |morpheus| on Ubuntu 20.04
- Java: Openjdk-jre updated to 8u275
- Appliance Logs: Default log rotation added for Nginx and Tomcat logs //add paths & files
- Installer: ``iptables_bach`` setup bash script moved from /tmp to /opt/morpheus/embedded/bin and renamed to iptables_morpheus.rules. Resolves reconfigure issue for systems with ``noexec`` set on ``/tmp``.
- Installer: Morpheus can now be installed on el8

Agent/Node Package Updates
==========================

- Java: openjdk and openjdk-jre updated to 8u275
- Node and VM Node package versions updates to 3.1.11
- FIPS mode supported now for el8
