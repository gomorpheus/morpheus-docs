.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

Release Dates
  - |morphVer|-1 |releasedate|

.. NOTE:: Items appended with :superscript:`6.0.0` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - Added CRUD functionality for NSX-T Groups via the ``network-server-groups`` API endpoint
:Security: - Embedded Tomcat has been upgraded to 9.0.70 (CVE-2022-42252) :superscript:`6.0.0`


Fixes
=====

:API & CLI: - Fixed an issue related to creating string type Cypher secrets through |morpheus| API
             - Fixed an issue that caused a 500 error when adding a Role with a |mastertenant| owner and user role type via |morpheus| API or CLI
             - Fixed an issue that prevented creation of Instance Inventory Summary reports via |morpheus| CLI
             - Fixed an issue that prevented updating NSX-T load balancers via |morpheus| API and CLI
             - Reports with custom date ranges can now accept day-level granularity (YYYY-MM-DD) when passing a custom date range to the report via |morpheus| API
             - Subtenant users can now see Catalog Items publicly shared from the |mastertenant| via |morpheus| API
             - ``layoutCode`` and ``visibility`` attributes are now returned when retrieving Catalog Item Types via |morpheus| API
:Amazon: - When editing Amazon Load Balancers (ALBs), the listed Security Groups and Subnets are filtered by VPC rather than being shown for all VPCs :superscript:`6.0.0`
          - When provisioning AWS workloads, the Security Groups list is now refreshed when you navigate from the CONFIGURE tab back to the GROUP tab and select a different AWS cloud :superscript:`6.0.0`
:Automation Scale Thresholds: - Fixed an issue that prevented timed scale thresholds from executing during the configured window :superscript:`6.0.0`
                  - When setting scale schedules based on dates, the dates are no longer incorrect when the browser language is set to Korean
:Blueprints: - Fixed an issue that caused App Blueprints with custom memory values not to pick up the entered amount at provision time but take the default value on the Plan instead
              - Fixed an issue that caused Groups not to populate when Subtenant users provisioned a public App Blueprint while their Tenant or User Role permission were set for "Library: Blueprints - Provision"
:Clusters: - Fixed an issue that caused storage classes for Kubernetes clusters to appear when provisioning Instances to a Docker cluster which was in the same Tenant at the Kubernetes cluster
:Executions: - Fixed an issue that caused incorrect formatting for long outputs on Task Execution detail pages (Library > Automation > Tasks > Selected Task > Executions Tab > Expand selected execution > Info "i" button)
:File Templates: - File Templates can now be deleted from |morpheus| UI so long as they are not in use. If File Templates are in use, a warning message will appear letting the user know it cannot be deleted :superscript:`6.0.0`
:Google Cloud (GCP): - After uploading a Virtual Image to a GCP bucket via |morpheus| and then provisioning the image, |morpheus| will no longer create a new bucket in a US region and upload the image as part of the provisioning process :superscript:`6.0.0`
                  - Fixed an issue that caused deactivated GCP Service Plans to be duplicated on the next cloud sync :superscript:`6.0.0`
:Inputs: - Fixed checkbox-type Inputs on Cluster Layouts to pass an "off" value when unchecked rather than NULL and empty text fields to pass an empty string ("") rather than Null
:Instances: - Added help block to the Instance Reconfigure modal indicating that adding a NIC merely attaches the network adapter in the cloud service, it does not configure network in the guest OS :superscript:`6.0.0`
             - Exporting the Instances and Hosts list pages now includes both the internal and external IP addresses in the output :superscript:`6.0.0`
             - Fixed a display ordering issue for volumes when converting VMs with multiple volumes to managed Instances :superscript:`6.0.0`
:Kubernetes: - Improved onboarding of external Kubernetes clusters to eliminate some edge cases that would fail to be onboarded with errors
              - New config maps will no longer disappear after refreshing the cluster :superscript:`6.0.0`
              - Service Plans scoped to the Subtenant are now shown when Subtenant users reconfigure a Kubernetes master or worker node in a Kubernetes cluster :superscript:`6.0.0`
              - The storage type selection is now only displayed on creation of an MKS (Kubernetes) cluster when the option is enabled on the Cloud :superscript:`6.0.0`
:Logs: - Fixed an issue that caused logs to be retained for only seven days even when configured to be retained longer (|AdmSetLog|) :superscript:`6.0.0`
        - Fixed misleading error in logs related to Cloud-Init which would display even when run successfully
:MicrosoftDNS: - Fixed an issue related to a WinRM library which caused problems with remote tasks (those not using |morpheus| Agent) and integrations such as MSDNS when the username was given in a domain\SAMAccountName format :superscript:`6.0.0`
:OpenStack: - Fixed an issue that caused reconfigures to add or remove network interfaces on OpenStack Instances not to work for OpenStack Clouds which were not scoped to a specific project (multi-project Clouds) :superscript:`6.0.0`
:Policies: - Fixed an issue that could allow certain Policy types to be exceeded if the user began provisioning additional resources in quick succession
            - Instances which are subject to Delete Approval policies now indicate to the user that the VM will be shutdown until the delete request is approved according to the Policy :superscript:`6.0.0`
:Proxies: - Fixed an issue that caused HTTP Task traffic not to route through configured proxies :superscript:`6.0.0`
           - Traffic from the |morpheus| appliance back to |morpheus| Hub is now relayed through a global proxy if one is configured :superscript:`6.0.0`
:Reports: - The following report types: Container Host Inventory Summary Report, Virtual Machine Inventory Summary, and Hypervisor Inventory Summary now include the total number of CPU cores in the UI where previously you had to export the report to see that data :superscript:`6.0.0`
:Roles: - Fixed an issue that prevented users with full code integration permissions from creating and managing those integrations if they didn't also have admin integrations permissions
:Tasks: - Fixed an issue that caused display issues for Tasks if the Task contained HTML tags which weren't closed properly :superscript:`6.0.0`
         - Fixed an issue that caused |morpheus| to truncate Task config in certain cases when the Task contained special characters :superscript:`6.0.0`
:Tenants: - Fixed an issue that caused a Tenant status to appear as "deleting failed" for a short time before it was successfully deleted which caused confusion :superscript:`6.0.0`
:VMware: - Fixed an issue that caused provisioning failure after replacing a Virtual Image with a new image having the same name :superscript:`6.0.0`
:Virtual Images: - Fixed a display issue on the Virtual Images list page that arose when a Virtual Image had a visibility value set to NULL
:Virtual Machines: - Updated the breadcrumb on a VM detail page to be dynamic depending on where the user came from (clicked on VM from Instance detail page, clicked on VM from Cloud detail, etc.) rather than always showing the breadcrumb from the Hosts list page :superscript:`6.0.0`
:Whitelabel: - When configuring whitelabel settings, setting a color by name (rather than hex value) no longer breaks whitelabeling :superscript:`6.0.0`


Appliance & Agent Updates
=========================

:Tomcat: - Embedded Tomcat has been upgraded to 9.0.70 (CVE-2022-42252) :superscript:`6.0.0`
:Guacamole: - Guacd build directory moved to ``/opt/morpheus/build``
