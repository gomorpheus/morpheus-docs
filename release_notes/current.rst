.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. IMPORTANT:: In |morpheus| |morphver|, many third party integrations have been moved out of the core installer package and converted to |morpheus| plugins. As a result, during the upgrade process your appliance will need to be able to access share.morpheusdata.com, the online repository for all |morpheus| plugins. Where this is not possible, users may instead apply the supplemental installer package which is also available at |morpheus| Hub alongside the main installer package.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - Added CRUD functionality for NSX-T Groups via the ``network-server-groups`` API endpoint :superscript:`5.4.14`
             - Floating IPs can be attached and detached on Instance containers via |morpheus| API and CLI as they can in UI
             - Key pairs can now be generated via |morpheus| API and CLI as they can in the |InfKeyKey| section of the UI
             - Listing and managing floating IPs can be handled through |morpheus| API and CLI. This functionality was also added to the UI with this release
             - Max Cores, Max Memory, Max Storage, Max VMs, Max Containers, and Max Hosts Policies can now be scoped to Service Plans via |morpheus| API and CLI. This feature has also been added to |morpheus| UI with this release
             - Resource Pool Groups functionality has been added for |morpheus| API and CLI. This functionality is similar to Network Groups except the Resource Pool is selected based on capacity at provision time
             - Self-service provisioning catalog items can now be filtered by category when ordering via |morpheus| API and CLI. This functionality was also included with |morpheus| UI in this release
             - ``--quiet`` cli parameter added for task and workflow execution. Suppress the output to stdout
:Automation Power Schedules: - When an Instance is on a power schedule and the power state is manually toggled on or off the schedule will no longer automatically change the power state until the next scheduled state change time
:Azure: - |morpheus| now supports enabling Azure boot diagnostics with a custom storage account rather than only supporting enabled with a managed storage account (default option) or disabling
:Bare Metal: - Storage and network details are now visible on the Hosts detail page for managed bare metal Instances :superscript:`5.4.15`
:Blueprints: - The Workflow select field on App and App Blueprint wizards is now a typeahead field to match Workflow select fields in other areas of the UI
:Catalog: - Catalog Workflows can now utilize Inputs and have a custom config field (works just like custom config on an Operational Workflow) :superscript:`5.4.15`
           - Catalog items can now be assigned a category on create or edit. When browsing the Catalog (|ProCat|), items can then be filtered by category
           - Catalog items now have a code property
           - Default AlmaLinux 9 images are now seeded into |morpheus| by default and are compatible with most major supported Clouds
           - Default Rocky 9 images are now seeded into |morpheus| by default and are compatible with most major supported Clouds
           - In Catalog (|ProCat|), the Inventory tab has been relabeled to Order History and includes links to Instance or App detail pages as well as Workflow execution pages
           - Self-service catalog Workflows now include the option for Inputs and the addition of a custom config body as Workflows already did in the Standard Persona
           - The catalog of default library items included with |morpheus| has been culled to remove most non-OS and non-Cloud default Instance Types. Examples include the default Apache, ActiveMQ, and Elasticsearch Instance Types
           - The default CentOS 8 Stream image has been updated for most major supported Cloud types
           - The default CentOS 9 Stream image has been updated for most major supported Cloud types
           - The default Rocky 8 image included by default with |morpheus| has been updated for all major supported Cloud types
           - The self-service catalog inventory page is now the "Order History" page. It shows a complete order history with links through to any ordered items (Instances, etc.) which still exist
:Clouds: - Nutanix Prism Central Cloud type now supported via custom plugin. See share.morpheusdata.com for the plugin files and additional details
          - The OneView Cloud type is now disabled by default and must be enabled in global settings to be restored
          - The UCS Cloud type is now disabled by default and must be turned on in global settings to be restored
:Clusters: - Resource Pool Groups functionality has been added allowing the Resource Pool to be automatically selected based on capacity at provision time
            - Some older default Kubernetes Cluster layouts (1.20 - 1.22) have been disabled for Cloud types which support newer Cluster layouts (1.23+) :superscript:`5.4.15`
:Dashboard: - The main appliance Dashboard (|OpeDas|) has been completely redesigned
:Health: - Appliance storage metrics have been added to the Health page (|AdmHea|) which can help diagnosing appliance performance issues
          - The Elastic health logic on the Health page (|AdmHea|) no longer shows Elastic health in a warned state for single node appliances
:Installer: - The embedded RabbitMQ service has been upgraded to 3.11.9
             - The embedded version of Java has been upgraded to 11.0.18+10
:Instances: - Instance detail pages now include a Resources tab which shows VMs, containers, Apps, and other constructs which may be associated with the Instance. Previously this information was on the main detail page, not inside its own tab
             - The Instance detail page headers has been redesigned to move more of the most important information to the top of the page
             - The Instance detail page now includes a costing tab. This tab pulls and aggregates Instance and host invoices, pricing history charts, pricing trends, and lists associated metered prices
             - The Instances detail page now includes a Summary tab which holds information that was previously in the Info section of the page and was always present (regardless of which subtab the user was looking at)
             - The Instances detail page now includes a monitoring tab which holds memory, storage, CPU, disk I/O and network stats. This information can be shown over a maximum of 90 days depending on your appliance stats retainment setting
:Keys & Certs: - Key pairs can now be generated in |morpheus| by navigating to |InfKeyKey| and clicking +ADD. This functionality is also added to |morpheus| API and CLI with this release
:Kubernetes: - Added default Kubernetes 1.24 and 1.25 Cluster Layouts for many Cloud types including Amazon AWS, VMWare, Digital Ocean and more :superscript:`5.4.15`
:Network: - Added support for Floating IP sync and management in OpenStack, Huawei, and OTC Clouds. Floating IPs tab added to UI (|InfNetFlo|) and option to release Floating IP on Instance delete added
:Option Lists: - "Instance Type Layouts" is now a selectable source object for |morpheus| API-type Option Lists
:Personas: - Instances, Apps and Workflow Executions list pages are now accessible through the Service Catalog Persona (the same view available in the standard Persona). When needed these pages may be restricted to show only the current user's own objects through role-based access controls
:Policies: - Max Cores, Max Memory, Max Storage, Max VMs, Max Containers, and Max Hosts Policies can now be scoped to Service Plans.
:Roles: - Several feature permissions for Roles have been updated to curate access to information on Instance detail pages.
         - The Provisioning: Executions feature permission now includes a "User" level to show only executions which are owned by the current user
:Salt: - The Salt Master integration type is now deprecated with |morpheus| 6.0.0
:Security: - Embedded MySQL has been upgraded to 5.7.41 (CVE-2023-21840)
            - Embedded Tomcat has been upgraded to 9.0.70 (CVE-2022-42252) :superscript:`5.4.14`
            - OpenSSL has been upgraded to 1.1.1t (CVE-2022-4450)
:ServiceNow: - ServiceNow integrations now support OAuth 2.0 in addition to simple username and password authentication
:Settings: - A stats retainment setting has been added to global settings (|AdmSet|) to extend the monitoring statistics available (such as on Instance detail pages) if desired
:Workflows: - Workflows may be added to Nested Workflow-type Tasks allowing Workflows to be nested inside other Workflows. This greatly simplifies the process of making Workflows which only have slight differences or which contain common pieces
             - There are a number of places in the UI where Workflows are selected. These have been converted from dropdown menus to typeahead fields
             - Workflows which fail can now be retried from immediately after the last successful Task. When a problem occurs with a long-running Workflow, it can now be corrected and the Workflow can be resumed from the fail point. Tasks can also be retried within some parts of an Instance provisioning history as well


Fixes
=====

:API & CLI: - Fixed an issue related to creating string type Cypher secrets through |morpheus| API :superscript:`5.4.14`
             - Fixed an issue that caused 404 errors when issuing the ``storage-buckets list-files`` command
             - Fixed an issue that caused Workflows to be duplicated in the return payload for calls to the Get all Workflows API
             - Fixed an issue that caused a 500 error when adding a Role with a |mastertenant| owner and user role type via |morpheus| API or CLI :superscript:`5.4.14`
             - Fixed an issue that prevented creation of Instance Inventory Summary reports via |morpheus| CLI :superscript:`5.4.14`
             - Fixed an issue that prevented updating Instance Type access on Subtenant User Roles for Instance Types created in the Subtenant :superscript:`5.4.14`
             - Fixed an issue that prevented updating NSX-T load balancers via |morpheus| API and CLI :superscript:`5.4.14`
             - Fixed an issue with the ``hosts add`` CLI flow that caused failures when adding Azure Docker hosts
             - Reports with custom date ranges can now accept day-level granularity (YYYY-MM-DD) when passing a custom date range to the report via |morpheus| API :superscript:`5.4.14`
             - Subtenant users can now see Catalog Items publicly shared from the |mastertenant| via |morpheus| API :superscript:`5.4.14`
             - The ``openapi`` endpoint to |morpheus| API now requires authentication since it returns the current appliance version
             - ``catalog add`` and ``catalog add-order`` CLI commands now present the correct Inputs and in the correct order
             - ``layoutCode`` and ``visibility`` attributes are now returned when retrieving Catalog Item Types via |morpheus| API :superscript:`5.4.14`
             - |morpheus| API no longer allows users to provision from disabled Instance Types or Layouts
:Alibaba Cloud: - Improved plan filtering when provisioning to Alibaba Cloud to show only flavors supported by the current configuration. This should prevent provisioning failures and users guessing at which plans should be supported :superscript:`5.4.15`
:Amazon: - IAM profiles are now selectable at provision time (advanced options section of provisioning wizard) for Subtenant users whether the Cloud is private and shared with the Subtenant or public :superscript:`5.4.15`
          - When editing Amazon Load Balancers (ALBs), the listed Security Groups and Subnets are filtered by VPC rather than being shown for all VPCs :superscript:`5.4.14`
          - When provisioning AWS workloads, the Security Groups list is now refreshed when you navigate from the CONFIGURE tab back to the GROUP tab and select a different AWS cloud :superscript:`5.4.14`
:Ansible Tower: - Ansible Tower Tasks now execute properly when the execute target is set to "Local" and the context set to "None" :superscript:`5.4.15`
:Ansible: - Fixed an issue that caused certain |morpheus| variables not to be set at the server context for Ansible Tasks :superscript:`5.4.15`
:Automation Scale Thresholds: - Fixed an issue that prevented timed scale thresholds from executing during the configured window :superscript:`5.4.14`
                  - When setting scale schedules based on dates, the dates are no longer incorrect when the browser language is set to Korean :superscript:`5.4.14`
:Backups: - Fixed an issue that could cause schedule backups to continue even when the "Scheduled Backups" option is disabled in global settings (Administration > Settings > Backups) :superscript:`5.4.15`
:Blueprints: - Fixed an issue that caused 500 errors when accessing a Blueprint-based Catalog Item which was based off a Morpheus-type Blueprint utilizing a Terraform Instance Type :superscript:`5.4.15`
              - Fixed an issue that caused App Blueprints with custom memory values not to pick up the entered amount at provision time but take the default value on the Plan instead :superscript:`5.4.14`
              - Fixed an issue that caused Groups not to populate when Subtenant users provisioned a public App Blueprint while their Tenant or User Role permission were set for "Library: Blueprints - Provision" :superscript:`5.4.14`
:Clusters: - Fixed an issue that caused storage classes for Kubernetes clusters to appear when provisioning Instances to a Docker cluster which was in the same Tenant at the Kubernetes cluster :superscript:`5.4.14`
:Code: - Reading Git repositories which contain submodules will no longer cause issues in |morpheus| :superscript:`5.4.15`
:Costing: - Rebuilding costing data (costing refresh from Cloud detail page) with the REBUILD option checked will now take into account existing usage records in recreating the cost data :superscript:`5.4.155.4.1`
:Executions: - Fixed an issue that caused incorrect formatting for long outputs on Task Execution detail pages (Library > Automation > Tasks > Selected Task > Executions Tab > Expand selected execution > Info "i" button) :superscript:`5.4.14`
:File Templates: - File Templates can now be deleted from |morpheus| UI so long as they are not in use. If File Templates are in use, a warning message will appear letting the user know it cannot be deleted :superscript:`5.4.14`
:Google Cloud (GCP): - After uploading a Virtual Image to a GCP bucket via |morpheus| and then provisioning the image, |morpheus| will no longer create a new bucket in a US region and upload the image as part of the provisioning process :superscript:`5.4.14`
                  - Fixed an issue that caused deactivated GCP Service Plans to be duplicated on the next cloud sync :superscript:`5.4.14`
                  - Fixed an issue that prevented RAW images stored locally on the |morpheus| appliance from being provisioned successfully to GCP
                  - For finalizing the previous month's costing, |morpheus| will now increase the lag time from one day to five days to ensure complete reporting :superscript:`5.4.15`
:Identity Sources: - Fixed an issue where the new/edit identity source modal would disappear after failing the create/update validation and become stuck with no obvious way to reopen it and fix the error :superscript:`5.4.15`
:Inputs: - Fixed an issue that caused Typeahead Input fields not to trigger reloading of downstream dependent fields
          - Fixed an issue that could cause existing Inputs to be migrated incorrectly when |morpheus| is upgraded :superscript:`5.5.3`
          - Fixed checkbox-type Inputs on Cluster Layouts to pass an "off" value when unchecked rather than NULL and empty text fields to pass an empty string ("") rather than Null :superscript:`5.4.14`
:Instances: - Added help block to the Instance Reconfigure modal indicating that adding a NIC merely attaches the network adapter in the cloud service, it does not configure network in the guest OS :superscript:`5.4.14`
             - Aligned the reconfigure prompts for Instances and servers which could have differences in certain cases :superscript:`5.4.15`
             - Exporting the Instances and Hosts list pages now includes both the internal and external IP addresses in the output :superscript:`5.4.14`
             - Fixed a display ordering issue for volumes when converting VMs with multiple volumes to managed Instances :superscript:`5.4.14`
             - The Guidance subtab (under Monitoring) on an Instance detail page is now hidden if the Instance is not VM-based
:Kubernetes: - Fixed issue with Kubernetes cron job sync :superscript:`5.4.15`
              - Improved k8s spec parsing , resolves issue with mismatched api versions :superscript:`5.4.15`
              - Improved onboarding of external Kubernetes clusters to eliminate some edge cases that would fail to be onboarded with errors :superscript:`5.4.14`
              - New config maps will no longer disappear after refreshing the cluster :superscript:`5.4.14`
              - On MKS cluster control plane nodes, containerd will now automatically restart when the host is rebooted without additional configuration from the user :superscript:`5.4.15`
              - Service Plans scoped to the Subtenant are now shown when Subtenant users reconfigure a Kubernetes master or worker node in a Kubernetes cluster :superscript:`5.4.14`
              - The storage type selection is now only displayed on creation of an MKS (Kubernetes) cluster when the option is enabled on the Cloud :superscript:`5.4.14`
:Labels: - Fixed an issue that caused errors to be thrown when duplicate labels (with different casing) were created
:Logs: - Fixed an issue that caused logs to be retained for only seven days even when configured to be retained longer (|AdmSetLog|) :superscript:`5.4.14`
        - Fixed misleading error in logs related to Cloud-Init which would display even when run successfully :superscript:`5.4.14`
:MicrosoftDNS: - Fixed an issue related to a WinRM library which caused problems with remote tasks (those not using |morpheus| Agent) and integrations such as MSDNS when the username was given in a domain\SAMAccountName format :superscript:`5.4.14`
:Morpheus IP Pools: - The MORE pop-out menu on the IP Pools list page (|InfNetIP|) now fully appears without being cut off
:NSX-T: - For NSX-T, the SNAT IP Address(es) field is now being displayed in the Add/Edit Load Balancer dialog on the Scale tab of the Instance detail page or the Load Balancer section of the Instance wizard when SNAT Translation Type is set to "IP Pool" :superscript:`5.4.14`
:OpenStack: - Fixed an issue that caused reconfigures to add or remove network interfaces on OpenStack Instances not to work for OpenStack Clouds which were not scoped to a specific project (multi-project Clouds) :superscript:`5.4.14`
:Option Lists: - When setting Active Directory options via custom Inputs sourced from LDAP-based Option Lists, selections will no longer get stuck when options have spaces or special characters :superscript:`5.4.15`
:Plugins: - Fixed an issue that restored validation for some required fields when saving or editing IPAM and DNS plugins
:Policies: - Creating an internal expiration policy after a ServiceNow provision approval policy will no longer cause the provisioning approval to also be internal (rather than a ServiceNow approval) :superscript:`5.4.15`
            - Fixed an issue that could allow certain Policy types to be exceeded if the user began provisioning additional resources in quick succession :superscript:`5.4.14`
            - Instances which are subject to Delete Approval policies now indicate to the user that the VM will be shutdown until the delete request is approved according to the Policy :superscript:`5.4.14`
:Proxies: - Fixed an issue that caused HTTP Task traffic not to route through configured proxies :superscript:`5.4.14`
           - Traffic from the |morpheus| appliance back to |morpheus| Hub is now relayed through a global proxy if one is configured :superscript:`5.4.14`
:Reports: - Fixed an issue that caused the Instance Inventory Summary report not to pull the correct Instances when filtered on more than one tag :superscript:`5.4.15`
           - The following report types: Container Host Inventory Summary Report, Virtual Machine Inventory Summary, and Hypervisor Inventory Summary now include the total number of CPU cores in the UI where previously you had to export the report to see that data :superscript:`5.4.14`
:Roles: - Fixed an issue that prevented users with full code integration permissions from creating and managing those integrations if they didn't also have admin integrations permissions :superscript:`5.4.14`
:Scaling: - Fixed an issue where |morpheus| would send the scaling success email whether or not the scaling action was successful :superscript:`5.4.15`
:ServiceNow: - Fixed an issue that caused errors in Morpheus logs after completing Bulk Insert in ServiceNow :superscript:`5.4.15`
              - Fixed an issue with multiselect Typeahead Input fields when ordering catalog items via ServiceNow :superscript:`5.4.15`
              - ServiceNow integrations now include an "API Proxy" setting. If configured, ServiceNow integration traffic will be routed through the indicated proxy. If no proxy is configured, ServiceNow traffic will route through a global proxy if one is configured
:Snapshots: - Certain reconfigure actions, such as those which alter CPU, memory or plan will no longer cause existing snapshots to be deleted. Others, such as removing a disk or changing disk size, will still result in existing snapshots being deleted :superscript:`5.4.15`
:Tags: - Fixed an issue that would sometimes cause tags to not be applied to new VMware workloads when the Instance was scaled
:Tasks: - Fixed an issue that caused display issues for Tasks if the Task contained HTML tags which weren't closed properly :superscript:`5.4.14`
         - Fixed an issue that caused |morpheus| to continually attempt to re-run certain Tasks while the VM was powered off which, in the worst cases, could lead to API limits being reached :superscript:`5.4.15`
         - Fixed an issue that caused |morpheus| to truncate Task config in certain cases when the Task contained special characters :superscript:`5.4.14`
         - Fixed an issue that created SQL exceptions in logs when the user accesses the executions page without rights to view Tasks
:Tenants: - Fixed an issue that caused a Tenant status to appear as "deleting failed" for a short time before it was successfully deleted which caused confusion :superscript:`5.4.14`
:Terraform: - Fixed an issue that caused errors when refreshing or applying state to Terraform Instances or Apps if the provider version was updated in the Terraform spec :superscript:`5.4.15`
             - Fixed an issue that caused provisioning failures for catalog items based on Terraform Blueprints which would provision successfully as Apps outside the provisioning catalog :superscript:`5.4.15`
             - Fixed an issue that could cause Terraform Instance or App data not to be displayed correctly on editing or applying state in specific configurations :superscript:`5.4.15`
             - Fixed an issue that could caused REST-based Inputs not to show their values on the Apply State view for Terraform Instances and Apps :superscript:`5.4.15`
             - Fixed an issue where |morpheus| would convert object-type Terraform variables to strings which caused failures :superscript:`5.4.15`
             - Improvement made to Terraform HCL parsing for Terraform Instances and Apps :superscript:`5.4.15`
:UI: - Clicking on an Instance label from the Instance list page (which should simply filter the list on that label) will no longer also take the user to the Instance detail page (which was unintended)
      - Fixed a display issue that could cause the main navigation bar to wrap onto a new line
:VMware: - Fixed an issue that caused provisioning failure after replacing a Virtual Image with a new image having the same name :superscript:`5.4.14`
          - On Cloud sync, |morpheus| will now update OS type on Windows VMs if set to a non-Windows OS type :superscript:`5.4.15`
          - Provisioning ISO images on VMware Clouds is now working properly when a host is selected during the process :superscript:`5.4.15`
:Virtual Images: - Fixed a display issue on the Virtual Images list page that arose when a Virtual Image had a visibility value set to NULL :superscript:`5.4.14`
:Virtual Machines: - Updated the breadcrumb on a VM detail page to be dynamic depending on where the user came from (clicked on VM from Instance detail page, clicked on VM from Cloud detail, etc.) rather than always showing the breadcrumb from the Hosts list page :superscript:`5.4.14`
:Whitelabel: - When configuring whitelabel settings, setting a color by name (rather than hex value) no longer breaks whitelabeling :superscript:`5.4.14`


Appliance & Agent Updates
=========================

:RabbitMQ: - Embedded RabbitMQ version updated to v3.11.9
