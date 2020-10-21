.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading |morpheus|

4.2.4 Highlights
================

SCAP Scans Confirm Security Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SCAP program (Security Content Automation Program) from NIST (National Institute of Standards and Technology) is designed to create an automated and reliable method for setting or verifying security configurations for a system or group of systems. |morpheus| |morphver| adds the ability to call in SCAP security packages and perform SCAP scans using pre-existing scan checklists and security profiles.

- Ensure security compliance of any |morpheus|-managed Instance(s) or server(s)
- Call in existing SCAP packages and checklists from online repositories
- Create Jobs to run SCAP scans against any group of Instances or Servers either on-demand or on recurring schedules
- View complete SCAP evaluation reports on your systems from inside the |morpheus| UI
- `Learn how to run SCAP scans in Morpheus <https://docs.morpheusdata.com/en/4.2.4/provisioning/jobs/jobs.html#creating-and-running-security-scan-jobs>`_

.. image:: /images/provisioning/jobs/security/6server_results.png

ServiceNow Incident Report Improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Through its ServiceNow integration, |morpheus| can pass incident data for viewing and handling through the ServiceNow console. In |morpheus| 4.2.4, additional details are passed through to the ServiceNow incident record to directly link back to the specific incident in |morpheus|, as well as provide details on the severity and current resource status.

- Link directly to the matching incident object in |morpheus|
- See incident severity information
- Link directly to the associated Check or Check Group in |morpheus|
- See additional details on the check including its interval, number of failed checks, and whether this incident impacts availability percentage

.. image:: /images/releases/424/servicenow.png

All New Features
----------------

- Amazon: Deploying MySQL or SQL Server with Amazon RDS now automatically creates the corresponding check and Instance status is reported
- Amazon: Routes on AWS routers are now editable (Infrastructure > Network > Selected AWS Network > Routing tab > Pencil icon) in addition to viewing, creating and deleting which could be done previously
- Amazon: Cloud Sync enhancements, reduced sync times
- Amazon EKS: Support Added for version k8s v1.7.11

- .. toggle-header:: :header: Azure Public Cloud: **Azure Cloud Integration Improvements**

     - Option to enable Azure Guest OS Diagnostics when provisioning Instance or App
     - Added option to enable Azure Boot Diagnostics when provisioning an Instance or App
     - Set disk encryption (user or platform-managed) and an encryption set (if user-managed) for an Azure Cloud integration (Add/Edit Cloud modal)

- Azure AKS: Support added for version 1.7.11
- Azure Stack: Added support for ARM templates
- Automation: Option Types: ``DISPLAY VALUE ON DETAILS`` flag added to Option Types to toggle display of associated Option Type values on Instance Detail pages 
- BlueCat: Support added for Bluecat 9.x
- Clouds: Cloud sync enhancements including variable sync schedules that auto-adjust per cloud, resulting in optimized sync times and reduction in sync overlaps and record lock conflicts.
- Clusters: Docker Hosts: Added the ability to set and edit security groups on Docker hosts for clouds that support native security groups (amazon, azure, openstack)

- .. toggle-header:: :header: KVM: **KVM Improvements**

     - KVM Windows provisioning support added
     - Console access is now available for VMs on the KVM server which were not provisioned by |morpheus|

- OpenStack: Clone updated to work with new OpenStack backup process
- NSX-V: Create and manage DHCP Pools for Edge Gateway routers
- Policies: Load balancer pricing is factored when enforcing budget policies during provisioning and reconfiguration

- .. toggle-header:: :header: Pricing: **Load Balancer Price Tracking**

     - Load balancer support in Price Plans, Price Sets, and Prices (Administration > Plans & Pricing)
     - Load balancer price data sync for Azure and Amazon
     - Automatically apply Price Plans to load balancers based on Plan configuration
     - Usage and Billing data for load balancers

- Provisioning: Enhancements added to speed up provisioning when "Install Agent" is skipped.
- Provisioning: Set a value to be prepended to all environment variables loaded as part of Instance or App provisioning
- Proxies: Global proxy setting now applies to all |morpheus| functionality, including local integrations such as Ansible and Terraform

- .. toggle-header:: :header: Roles: **Role Permission Changes**

     - Network integration firewall permissions (Infrastructure > Network > Integrations > Selected integration > Firewalls) now have their own setting (Infrastructure: Network Firewalls). Previously they were inherited from the "Network: Integrations" permission
     - ``Security: Scanning`` Feature Access Permission added        
        - Determines access to the Security Packages tab on the Jobs list page (Provisioning > Jobs), Security Scanning type Jobs, and Security Subtab inside the Software tab on a server detail page where the results of security scans are viewed
        - Allows access to view, create, and run security scans on existing systems, as well as view the results of previously-run scans
        - This permission is recommended for those responsible for security compliance of existing systems
     
- SCVMM: If virtual image advanced options has vm tools installed (unchecked) system will auto skip network wait on SCVMM now. Matches existing VMware and KVM behavior.
- ServiceNow: "|morpheus| Incident" alerts are now more insightful including links to the related |morpheus| incident or check, severity information, and other details about the failing check
- Security Scanning: Security scan job type added (Provisioning > Jobs) to perform SCAP scans against secure baselines to confirm compliance
- Security: Tomcat version removed from default server error pages
- Settings: Cloud refresh interval is now user-configurable, the settings can be changed in Administration > Settings > Appliance (Default: 300 seconds)

- .. toggle-header:: :header: UI: **Interface and Usability Improvements**

     - Icons added for AWS services (such as in Service Catalog), including AWS App Mesh, AWS SQS, and AWS SDB
     - When applying state to Terraform and CloudFormation Apps, a friendly progress bar is displayed to indicate the change
     - Session expiration times can now be configured (Administration > Settings > Appliance), if desired a window can also be displayed at a specified time to warn about the impending logout
     - MySQL tmp file location moved from ``/tmp`` to ``/var/run/morpheus/mysqld``
     - Advanced table view added to Clusters list page (Infrastructure > Clusters) and Load Balancers list page (Infrastructure > Load Balancers)

- Windows: Windows VMs will now auto-expand their root storage partitions to fill drive space, previously this was done manually
- vCloud Director: Create and delete Snapshots in a vCD Cloud

- .. toggle-header:: :header: Veeam: **Backup Jobs can now be deleted**

     - Backup Jobs are deleted from the ACTIONS menu on the Backup Jobs list page (Backups > Jobs)
     - Delete action existed previously but, due to Veeam API limitations, Morpheus could only disable the job
     - Backup job delete is supported only on Veeam version 10

- VMware: VMware Cloud syncs are now up to 10x faster

Fixes
-----

- ACI: Fixed invalid display error when creating ACI Application Profile
- ACI: Fixed network deletion issue caused by illegal characters in CIDR
- ACI: Fixed tabs not displaying on ACI integration detail pages when accessed via ``/infrastructure/networks`` (displayed when accessed via ``/admin/integrations``)
- Amazon: Cloud Summary Page: Resources: Fixed ``Security Groups`` stat always showing ``0``
- Amazon: Route53: Updates to handle rate limits when syncing large number of Route53 domain records
- Amazon: Fixed issue with S3 bucket sync that could cause excessive Appliance memory usage.
- Ansible Tower: Fixed invalid Ansible Tower integration link in cloud details pages
- API/CLI: Fixed Task creation when using Repository Source.
- Apps: Fixed inconsistent app, node and execution statuses during App provisioning when a Workflow Task fails during Provision Phase.
- Apps: Updated the NAME property for VM and Container lists on App Detail views to match Instance Detail views
- Azure: Added support for adding and removing non-primary nic's on single nic VM's
- Azure: ARM Instance Spec Templates: Fixed long running provision timeouts
- Azure: Cloud Summary Page: Resources: Fixed ``Security Groups`` stat always showing ``0``
- Azure: Fix for automated Active Directory domain joins due to -NewName
- Azure: Fixed AKS Cluster Deployment failure when Azure Cloud is scoped to single Resource Group (note: Cloud discovery must be enabled for AKS provisions in this scenario to discover worker vm's)
- Azure: Fixed issue adding Azure Security Group Rule names containing spaces
- Azure: Fixed issue with deleting a Resource Group created from an ARM App when an Azure Cloud is scoped to a single Resource Group.
- Azure: Fixed provisioning issue when specifying mixed managed disk types
- Azure: Fixed user provided disk labels being overwritten with external_id names
- Backups: Fixed enable/disable flag for Veeam Backups 
- Budgets: Fixed current years actuals displaying in future years budgets
- Cisco ACI: Fixed potential issues preventing deletion of Cisco ACI Integrations
- Cloud Formation: Fixed issue creating Lambda resources from CF Blueprints. (Note: Lambda resource objects will be added in future release)
- Cloud Removal not clearing storage volumes
- Clusters: Hosts: Fixed Workflow execution not displaying in History tab on Host detail pages
- Convert To Managed: Removed legacy ``Existing <X>`` layout from available layout options during Convert to Managed action
- ElasticSearch: Added auto-reconnect or rebuilding of es client on runtime exceptions
- Git: Fixed issue deleting Git Integrations with existing file content associations
- Health: Fixed display of ``Memory: System Swap`` and ``Memory: Free Swap`` values in the Appliance Health section. 
- Infrastructure: Hosts: Virtual Machines: The Remove Infrastructure and Preserve Volumes checkboxes are now present and functional when performing bulk VM delegations.
- Instance Power On / Power Off actions (including power schedule) broken for Exis
- Networks: Fixed display of invalid Groups in Network Group Access section, causing Group Access changes to not persist
- Networks: If a user has only read permissions for the Infrastructure: Network Routers feature permission, that user no longer has the ability to edit or delete router firewall rules.
- Networks::  If a user has only read permissions for the Infrastructure: Network Routers feature permission, the Create Neighbor button on the router detail page's BGP tab is now hidden
- NSX-T: Fixed inaccessible Routers displaying for Subtenants
- NSX-T: Fixed issue with NSX-T IP Pool creation
- NSX-V: CIDR is no longer required when editing existing Logical Switches
- NSX:  The Name field is now visually identified as a required field on the Create Rule dialog for NSX-v and NSX-t network firewalls
- NSX: Added validation to prevent deletion of NSX networks still in use by existing entities.
- Nutanix: Fixed issue provisioning custom images stored in S3
- Nutanix: Removed root disk storage container selection during provisioning as root disk must be created on same Storage Container as Template (Nutanix req).
- Openstack Clouds: Fixed security groups scoped to "All" Clouds not displayed during provisioning.
- OTC: Fixed issue with long running Instance backups not exporting.
- Policies: Fixed issue with Expiration policies not removing resources in a Failed state
- Policies: Fixed issue with sub-tenant whitelabling of full page MOTD policies
- Policies: Tags: Fixed issue where vm tags were allowed to be changed to values not compliant with an active, strictly enforced Tag policy.
- Policies: Updated email notification Instance links to redirect to subtenant logins
- PowerDNS: Fixed display issue with Power DNS records "Content" field
- Provisioning: Fixed sudoer permissions for Users created during provisioning when users linux username contains a ``.``  
- PXE Boot: Fixed editing of discovered Mac Addresses
- RDS: Fixed issue with editing Power Schedules for AWS RDS Instances
- Reconfigure: Fixed issue with core count being set to plan default vs existing count when reconfiguring and selecting a custom plan with customizable cores
- Reconfigure: Fixed page error when decimal is specified in a disk size during reconfigure
- Reports: Fixed issue with Instance Inventory Summary Report potentially showing old resource values on reconfigured Instances
- Reports: Fixed Tenant Cost Reports not displaying correct Instance counts
- Reports: Updates and fixes to Cloud Cost and Tenant Cost Reports
- SCVMM: Adding a disk, resizing a data disk, or removing a data disk during Reconfigure will no longer trigger a restart.
- SCVMM: Fixed adding disks during reconfigure of Generation 2 virtual machines
- SCVMM: Fixed issue where selected SCVMM Cloud was not being passed in SCVMM VM config
- SCVMM: Fixed issue with Optical drive being removed during provisioning of Generation 2 virtual machines
- SCVVM: Fixed Instance reconfigure startup memory and fixed memory allocation
- SCVVM: Fixed startup memory and fixed memory allocations when dynamic memory is enabled
- Security: XSS vulnerability removed
- Tags: Fixed error when trying to create a tag without a value
- Terraform: App Provision: Resolved issue where :guilabel:`Next` button would become re-enabled prior to completion of validations over 35 seconds 
- UI: Updates to prevent Invalid CSRF Token Error on stale pages.
- User Profiles: Clouds listed in ``Default Cloud`` now filtered by Group association/access
- vCloud Director: Fixed issue with frequent usage record restarts
- VMware: Fixed datastore cluster references for datastores shared across multiple clusters
- VMware: Fixed issue with Subtenant setting VMware Folder Group Access permissions.
- VMware: Hypervisor Console: Fixed issue with high resolution consoles showing blank on initial uncompressed connection
- Waiting for network message during SCVMM provisioning
- White-labelling: Fixed page refresh issue with custom ``Terms and Conditions`` and ``Privacy`` Pages
- Workflows: Fixed issue with Reboot tasks potentially causing Instance state to show as Running when a Provision phase task has failed


|morpheus| API & CLI Updates
============================

API & CLI Enhancements
----------------------

- .. toggle-header:: :header: Deployments: **Deployments API/CLI Improvements**

     - Support for adding files to a Deployment version
     - Support for managing Instance deploys (appDeploys). This used to only provide endpoints for a specific instance to deploy and list deploys. Now it has full CRUD, and list shows account wide deploys. See `morpheus deploys`.

- Hosts: Search by tag names and values
- Instances: Search by tag names and values
- Instances: Support added for filtering by ``expireDate`` and ``shutdownDate``
- Search: Global search added similar to the global search bar that has existed in the UI

API & CLI Fixes
---------------

- Billing: Optional parameters added to support pagination of large returns
- Deployments: The command ``morpheus deploy`` was fixed to correct some unwanted behavior, the ``--help`` flag output was also improved
- Fixed ``service-plans add`` monthly price set association
- Fixed issue when creating a blueprint and passing a yaml or json file
- Fixed issue when creating a blueprint and passing a yaml or json file
- Fixed missing config properties issue with Azure Virtual Images
- Proper error message returned when provision request exceeds max cores policy limit.
- Validation and response added when passing invalid value for ``POST /api/roles`` : ``roleType`` 
- virtual-images GET no longer returns information on soft deleted Virtual Images
