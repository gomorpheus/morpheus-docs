.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: This list includes improvements added in 4.2.4 which were not part of the 5.0.0 beta. Users upgrading from 4.x.x may also want to review the `5.0.0 change list <https://docs.morpheusdata.com/en/5.0.0/release_notes/current.html>`_ to get a complete picture of the changes.

.. include:: highlights.rst

All New Features
----------------

- .. toggle-header:: :header: Amazon: **Amazon AWS Cloud Integration Improvements**

     - Deploying MySQL or SQL Server with Amazon RDS now automatically creates the corresponding check and Instance status is reported
     - Hong Kong region (ap-east-1) support added

- Amazon EKS: Support added for version 1.7.x
- Azure AKS: Support added for version 1.7.11

- .. toggle-header:: :header: Azure Public Cloud: **Azure Cloud Integration Improvements**

     - Option to enable Azure Guest OS Diagnostics when provisioning Instance or App
     - Added option to enable Azure Boot Diagnostics when provisioning an Instance or App
     - Set disk encryption (user or platform-managed) and an encryption set (if user-managed) for an Azure Cloud integration (Add/Edit Cloud modal)

- Azure Stack: Azure Stack: Added support for ARM templates

- Blueprints: Added ability to set fields as hidden when creating a Blueprint. These fields will not be visible when provisioning an App from the Blueprint. Previously fields could be locked but not hidden.
- Clouds: Cloud sync enhancements including variable sync schedules that auto-adjust per cloud, resulting in optimized sync times and reduction in sync overlaps and record lock conflicts

- .. toggle-header:: :header: KVM: **KVM Improvements**

     - Console access is now available for VMs on the KVM server which were not provisioned by Morpheus

- Networks: Visibility and Tenant permissions added for IP Pools (select Permissions under the "MORE" menus on the IP Pools)
- NSX-V: Create and manage DHCP Pools for Edge Gateway routers

- .. toggle-header:: :header: NSX-T: **NSX-T Integration Improvements**

     - Visibility and Tenant permissions added for Transport Zones (select Permissions under the "MORE" menus on the Transport Zone tab)
     - Visibility and Tenant permissions added for Edge Clusters (select Permissions under the "MORE" menus on the Edge Clusters tab)
     - Create and manage NAT rules for T-0 and T-1 routers (see NAT tab on the detail page for a T-0 or T-1 router)
     - Role permissions added to control access to the T-0 and T-1 routers tabs for an NSX-T network integration
     - Interfaces tab for T-1 routers renamed to Service Interfaces for clarity

- OpenStack: Backup process improved to handle longer running jobs for backing up large instances
- Openstack: ``Service Endpoints`` section added to cloud config for manually overriding OpenStack cloud API endpoints
- Policies: Load balancer pricing is factored when enforcing budget policies during provisioning and reconfiguration

- .. toggle-header:: :header: Pricing: **Load Balancer Price Tracking**

     - Load balancer support in Price Plans, Price Sets, and Prices (Administration > Plans & Pricing)
     - Load balancer price data sync for Azure and Amazon
     - Automatically apply Price Plans to load balancers based on Plan configuration
     - Usage and Billing data for load balancers

- Provisioning: Set a value to be prepended to all environment variables loaded as part of Instance or App provisioning
- Proxies: Global proxy setting now applies to all Morpheus functionality, including local integrations such as Ansible and Terraform
- Reports: "Invoice Details" report added to list of available report types. For a selected Cloud, group invoices by up to two additional parameters (Region, Cloud, Plan, Tag or Tenant)

- .. toggle-header:: :header: Security Scanning: **Run SCAP Scans to Confirm Security Compliance**

     - Create Jobs to run SCAP scans against any group of Instances or Servers either on-demand or on recurring schedules
     - View complete SCAP evaluation reports on your systems from inside the Morpheus UI
     - View and track security scan run histories

- .. toggle-header:: :header: Roles: **Role Permission Changes**

     - Network integration firewall permissions (Infrastructure > Network > Integrations > Selected integration > Firewalls) now have their own setting (Infrastructure: Network Firewalls). Previously they were inherited from the “Network: Integrations” permission
     - Role permissions added to control access to the T-0 and T-1 routers tabs for an NSX-T network integration
     - ``Security: Scanning`` **Feature Access Permission added**

      - Determines access to the Security Packages tab on the Jobs list page (Provisioning > Jobs), Security Scanning type Jobs, and Security Subtab inside the Software tab on a server detail page where the results of security scans are viewed
      - Allows access to view, create, and run security scans on existing systems, as well as view the results of previously-run scans
      - This permission is recommended for those responsible for security compliance of existing systems

- .. toggle-header:: :header: Service Catalog: **Service Catalog Persona Improvements**

     - Operational Workflows can be made available as Service Catalog Items and ordered by Service Catalog Persona users
     - Catalog Items can be categorized under specific headers for easier discoverability as the catalog grows
     - Quantity selector added for items in cart to avoid the need for adding duplicate items

- .. toggle-header:: :header: ServiceNow: **ServiceNow Integration Improvements**

     - "|morpheus| Incident” alerts are now more insightful including links to the related Morpheus incident or check, severity information, and other details about the failing check
     - Provision Service Catalog Items through the Morpheus ServiceNow plugin
     - Inventory list view now includes much greater detail about each inventory item
     - Added the capability to identify a MID server once on the properties page rather than setting it individually for each call
     - Pricing data is now available to the ServiceNow plugin when ordering Service Catalog items. This is made available on the XML as a monthly price, users would have to modify the form UI to surface this information

- Tasks: Tasks now have a detail page with a Summary tab showing the script and a Workflows tab listing the Workflows in which the Task is used
- Tenants: Metadata, specifically an account number, account name, and customer number, can now be tracked for Tenants

- .. toggle-header:: :header: UI: **Interface and Usability Improvements**

     - Administrators can now determine the required length and complexity of user passwords (Administration > Settings > Appliance > User Management Settings)
     - When applying state to Terraform and CloudFormation Apps, a friendly progress bar is displayed to indicate the change
     - Icons added for AWS services (such as in Service Catalog), including AWS App Mesh, AWS SQS, and AWS SDB
     - MySQL tmp file location moved from ``/tmp`` to ``/var/run/morpheus/mysqld``
     - Session expiration times can now be configured (Administration > Settings > Appliance), if desired a window can also be displayed at a specified time to warn about the impending logout
     - All navigations bars with potential for high tab counts now handle this scenario gracefully
     - Visibility column added to Catalog Item list (Tools > Self Service) to conveniently indicate whether an item is shared with Tenants
     - Friendly error messages are surfaced if there is a problem creating the items checked out in a Service Catalog cart, the Instance was simply not created and log access was needed to see what went wrong
     - CenturyLink Edge Cloud type renamed to Lumen Edge

- Workflows: "Configuration" phase added to Provisioning Workflows. Tasks in this phase are run prior to the initial provision.

|morpheus| API & CLI Improvements
-------------------------------

- Billing: Optional parameters added to support pagination of large returns

- .. toggle-header:: :header: Deployments: **Deployments API/CLI Improvements**

     - Support for adding files to a Deployment version
     - Support for managing Instance deploys (appDeploys). This used to only provide endpoints for a specific instance to deploy and list deploys. Now it has full CRUD, and list shows account wide deploys. See `morpheus deploys`.

- Instances: Support added for filtering by ``expireDate`` and ``shutdownDate``
- Instances: Search by tag names and values

- .. toggle-header:: :header: Personas: **Personas and Service Catalog Persona Functionality Added**

     - Set the default Persona for a user
     - Create catalog items for Service Catalog Persona users
     - Set Role permissions regarding Persona and Catalog Item type access
     - Browse the catalog, add items to cart, and checkout as a Service Catalog Persona user

- Search: Global search added similar to the global search bar that has existed in the UI
- Tenants: Account (Tenant) metadata field support added (``customerNumber``, ``accountNumber``, and ``accountName``)
- Virtual Images: Associated ``volumes`` are returned with ``maxStorage`` viewable for each

Fixes
-----

- ACI: Fixed network deletion issue caused by illegal characters in CIDR :superscript:`+`
- Amazon: ALB’s: Fix for adding ALBs in a subtenant
- Amazon: Fixed ``Security Groups`` stat always showing ``0`` on the Resources tab of the Cloud summary page :superscript:`+`
- Amazon: Fixed S3 Bucket create and delete not utilizing AWS Cloud API Proxy config
- Ansible Tower: Fixed invalid Ansible Tower integration link in cloud details pages :superscript:`+`
- Ansible: Ansible integrations now utilize Global Proxy config for repo connections
- API/CLI: Fixed config property of Azure image type missing in GET and POST (CLI) :superscript:`+`
- API/CLI: Fixed Task creation when using a repository source :superscript:`+`
- API/CLI: Validation and response added when passing invalid value for ``POST /api/roles`` : ``roleType`` :superscript:`+`
- Apps: Fixed inconsistent app, node and execution statuses during App provisioning when a Workflow Task fails during the Provision phase :superscript:`+`
- Apps: Updated the NAME property for VM and Container lists on App Detail views to match Instance Detail views :superscript:`+`
- Archives: Fixed timeout issue with archive files > 1GB caused by legacy Archives path set in default Nginx config
- Azure: Fix for automated Active Directory domain joins due to ``-NewName`` :superscript:`+`
- Azure: Fixed long running provision timeouts for ARM Instance Spec Templates :superscript:`+`
- Commvault: Fixed issue with subtenant Commvault Backup Job completion when Backup and Backup Job names use custom values
- Git: Fixed issue deleting Git integrations with existing file content associations :superscript:`+`
- Github: Github integrations now utilize Global Proxy config for Github connections
- Hosts: The Remove Infrastructure and Preserve Volumes checkboxes are now present and functional when performing bulk VM delegations (Infrastructure > Hosts > Virtual Machines) :superscript:`+`
- Identity Sources: SAML: Fixed issue with checkbox rendering in Firefox browsers
- Networks:  If a user has only read-level permission for the "Infrastructure: Network Routers" feature, the :guilabel:`+ CREATE NEIGHBOR` button on the BGP tab of the Router Detail page is now hidden :superscript:`+`
- Networks: If a user has only read-level permission for the "Infrastructure: Network Routers" feature, that user no longer has the ability to edit or delete router firewall rules :superscript:`+`
- NSX-V: Create and manage DHCP Pools for Edge Gateway routers :superscript:`+`
- Nutanix: Fixed issue provisioning custom images stored in Amazon S3 buckets :superscript:`+`
- Nutanix: Removed root disk storage container selection during provisioning as Nutanix requires root disk must be created on the same storage container as the template :superscript:`+`
- Openstack Clouds: Fixed security groups scoped to "All" Clouds which previously were not displayed during provisioning :superscript:`+`
- OTC: Fixed issue with long running Instance backups not exporting :superscript:`+`
- Policies: Fixed issue where VM tags were allowed to be changed to values not compliant with an active, strictly-enforced tag policy. :superscript:`+`
- Policies: Fixed issue with expiration policies not removing resources which are in a failed state :superscript:`+`
- Policies: Updated email notification Instance links to redirect to subtenant logins :superscript:`+`
- PowerDNS: Fixed display issue with PowerDNS record "Content" fields :superscript:`+`
- Provisioning: Fixed sudoer permissions for users created during provisioning when the associated Linux username contains a ``.`` :superscript:`+`
- PXE Boot: Fixed editing of discovered MAC Addresses :superscript:`+`
- RDS: Fixed issue with editing Power Schedules for AWS RDS Instances :superscript:`+`
- Reconfigure: Fixed page error when decimal is specified in a disk size during reconfigure :superscript:`+`
- Reports: Fixed issue with Instance Inventory Summary Report potentially showing old resource values on reconfigured Instances :superscript:`+`
- SCVMM: Adding a disk, resizing a data disk, or removing a data disk during reconfigure will no longer trigger a restart :superscript:`+`
- SCVMM: Fixed adding disks during reconfigure of Generation 2 virtual machines :superscript:`+`
- SCVMM: Fixed issue where selected SCVMM Cloud was not being passed SCVMM VM config :superscript:`+`
- SCVMM: Fixed issue with optical drive being removed during provisioning of Generation 2 virtual machines :superscript:`+`
- SCVVM: Fixed Instance reconfigure startup memory and fixed memory allocation :superscript:`+`
- SCVVM: Fixed startup memory and fixed memory allocations when dynamic memory is enabled :superscript:`+`
- Security: XSS vulnerability removed :superscript:`+`
- Tags: Fixed error when trying to create a tag without a value :superscript:`+`
- Tenants: Fixed Tenant deletion issue related to existing network_security_server records
- Terraform: Resolved issue where :guilabel:`NEXT` button would become re-enabled on App provisioning prior to completion of validations over 35 seconds  :superscript:`+`
- vCloud Director: Fixed issue with frequent usage record restarts :superscript:`+`
- VMware: Fixed datastore cluster references for datastores shared across multiple clusters :superscript:`+`
- VMware: Fixed issue with high-resolution hypervisor consoles showing blank on initial uncompressed connection :superscript:`+`
- VMware: Fixed issue with Subtenant setting VMware Folder Group Access permissions :superscript:`+`

.. note:: :superscript:`+` indicates fix also released in v4.2.4
