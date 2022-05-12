.. _Release Notes:

*************************
|morphver| Release Notes
*************************

Release Date: |releasedate|

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst


|morpheus| v5.5.0 is the first version of the v5.5 Feature Branch. In addition to the features listed below not included in v5.4.6, v5.5.0 contains "under the hood" updates in support of upcoming features and capabilities.

New Features
============

:API & CLI: - A checksum property is now also returned when a masked password is returned via |morpheus| API :superscript:`5.4.6`
             - Use credential sets (Infrastructure > Trust) to authenticate calls to populate REST-based Option Lists when creating the Option List via |morpheus| API and CLI :superscript:`5.4.6`
             - Use stored credentials to authenticate HTTP Tasks or Tasks executed on remote servers when creating Tasks via |morpheus| API and CLI :superscript:`5.4.6`
             - VMware Cloud integrations can be created from |morpheus| API and CLI using stored credentials as they already can from |morpheus| UI :superscript:`5.4.6`
:Agent: - Windows Agent msi packages certificate updated. Note the Morpheus Windows Agent version has not changed, this update only applies to the installer packages, no need to update existing 1.8.0 agents. :superscript:`5.4.6`
:Amazon: - Amazon RDS instance types updated to reflect those currently available in the Milan region. |morpheus| Plans also updated to reflect the change :superscript:`5.4.6`
:Clouds: - Manual Cloud refresh (Refresh > Costing from the Cloud detail page) now allows the user to specify a costing period to refresh and whether costing data should be rebuilt entirely :superscript:`5.4.6`
:Credentials: - Expanded the use of stored credentials to include use during creation of backup integrations, including Veeam, Zerto, Commvault, Rubrik, and Avamar
               - OAuth2 credential types are now supported for populating REST-based Option Lists :superscript:`5.4.6`
:Currency: - Support added for Japanese Yen currency (JPY) :superscript:`5.4.6`
            - Support added for Thai Baht currency (THB) :superscript:`5.4.6`
:Docker: - Ubuntu 22.04 (Jammy) is now supported for provisioning Morpheus Docker Hosts & Morpheus KVM/Docker Hosts :superscript:`5.4.6`
:Instances: - The Network section on the Instance detail page now has selectable subsections (security groups, interfaces, etc) rather than putting subsections inside expandable headings
:Kubernetes: - Cluster Events added. K8s Cluster Detail page ``Logs`` tab renamed to monitoring with ``Logs`` and ``Events`` sub tabs :superscript:`5.4.6`
              - Console access added for MKS (Morpheus Kubernetes) POD Instances. Note: Support for External, AKS, EKS, and GKE POD Consoles planned for a later release. :superscript:`5.4.6`
              - Improved Kubernetes Cluster sync performance for reduced overhead and sync times :superscript:`5.4.6`
              - Kubernetes 1.23 system cluster layouts added for Amazon, Digital Ocean, Morpheus (manual), Nutanix, VMware, & Xen :superscript:`5.4.6`
              - Pod Events added. ``Events`` tab added to POD information modal with event TYPE, REASON, NAMESPACE, DATE, OBJECT & MESSAGE details :superscript:`5.4.6`
:Monitoring: - The Monitoring Checks detail page now paginates large lists of Checks results and Check Groups :superscript:`5.4.6`
:NSX-T: - Primary Tenant administrators can now create groups within distributed firewalls and expose them to Subtenant users. The Subtenant can create and modify rules within their allocated groups but cannot create or modify the groups themselves :superscript:`5.4.6`
:OpenStack: - Provision Type setting added to Openstack cloud settings. Image: Relies on the openstack server API to create a volume from the specified image.
Volume: Creates a volume which is then fed to the server api to launch a new server from the volume. :superscript:`5.4.6`
:Plans & Pricing: - Update to database schema handling pricing data to improve efficiency and performance :superscript:`5.4.6`
:SCVMM: - Updated handling of SCVMM workloads with dynamic memory plans :superscript:`5.4.6`
:Virtual Images: - System Ubuntu 22.04 images seeded for Amazon, Azure, DigitalOcean, ESXi, Google, Huawei, HyperV, KVM, Nutanix, Openstack, OTC, SCVMM & VMware :superscript:`5.4.6`


Fixes
=====

:API & CLI: - Calls to the |morpheus| API Security Groups endpoint now returns the object database ID as intended :superscript:`5.4.6`
             - Fixed an issue that prevented creation of OpenStack Clouds via |morpheus| CLI in specific scenarios :superscript:`5.4.6`
             - The ``prices add`` CLI command now allows Price creation in all currencies that are supported in |morpheus| UI :superscript:`5.4.6`
:Agent: - Fixed an issue with Instance metrics reporting incorrectly from the Linux Agent (server metrics were unaffected) :superscript:`5.4.5`
:Azure: - Fixed an issue that could cause 500 errors to be thrown when clicking into the detail page for provisioned Azure Instances :superscript:`5.4.6`
         - Fixed an issue that prevented provisioning from certain Azure marketplace offers :superscript:`5.4.6`
:Blueprints: - Fixed an issue that could prevent Subtenant users which weren't the original creator of an App Blueprint from provisioning Apps based on the Blueprint :superscript:`5.4.6`
:Catalog: - Fixed an issue that could cause validation messages to be duplicated when Inputs with specific configurations are used with Catalog Items :superscript:`5.4.6`
:Clouds: - Updated database schema to prevent Cloud sync from stopping under certain conditions :superscript:`5.4.6`
:Clusters: - The cluster workloads donut chart (Infrastructure > Clusters) has been updated to more easily distinguish between workloads whose truncated names end up being identical (have the same first characters) :superscript:`5.4.6`
:Compute: - After converting discovered Windows VMs to managed Instances, they now appear correctly under VMs (rather than hosts) in the compute section (Infrastructure > Compute) and no longer appear with an incorrect Windows version :superscript:`5.4.5`
           - Fixed an issue that could cause Subtenant workloads to appear on the compute list page (Infrastructure > Compute) in the Primary Tenant :superscript:`5.4.6`
:Costing: - Usage checks have been refactored for efficiency and accuracy, primarily in very large environments :superscript:`5.4.6`
:Credentials: - Fixed an issue that prevented integrating new GCP Clouds using credential sets which were stored on an external Cypher server :superscript:`5.4.6`
:Distributed Worker: - Fixed issue with image uploads using morpheus worker hitting Socket Buffer limit :superscript:`5.4.6`
:F5: - Fixed an issue that prevented F5 virtual servers and nodes from being edited when set on a partition :superscript:`5.4.6`
:Identity Sources: - Improved validation on the "Add SAML SSO" modal to surface friendly validation warnings rather than throw errors when the modal is not filled out completely :superscript:`5.4.6`
                  - |morpheus| now trims any whitespace characters coming back from Active Directory, such as in usernames or email addresses, that could potentially create failures :superscript:`5.4.6`
:Inputs: - Input visibility is now honored for all Input types, including radio list, typeahead, and text area :superscript:`5.4.6`
          - Input visibility settings now work in Operational Workflow execution in addition to the Provisioning Catalog :superscript:`5.4.6`
:Instances: - The "Remove Node" option is no longer missing in specific scenarios for Windows 2016 custom Instances :superscript:`5.4.6`
:Invoices: - Fixed an issue that could cause the Cloud filter on the Invoice list page to show invoices for Clouds outside the filter parameter :superscript:`5.4.6`
:Kubernetes: - Fixed an issue that could cause "Add Job" to fail for Kubernetes clusters in some scenarios :superscript:`5.4.6`
              - Fixed an issue that could cause |morpheus| to attempt to delete EKS clusters from AWS if the cluster object is missing from |morpheus| :superscript:`5.4.5`
              - Fixed an issue that would leave external Kubernetes clusters in a "warning" status due to an inability to render cronjobs on the cluster :superscript:`5.4.6`
:Library: - The Library menu in |morpheus| UI is now visible when the user's role permissions give them access only to the Power Schedule section :superscript:`5.4.6`
:Network: - Fixed an issue that caused 500 errors to be thrown when editing a security group scoped to all Clouds to add a location :superscript:`5.4.6`
           - Fixed an issue that caused a 500 error to be thrown when attempting to save a new zone record without filling in any fields on the modal :superscript:`5.4.6`
           - From the Primary Tenant, the Cloud filter on the Networks list page (Infrastructure > Network > Networks) now allows filtering by Clouds created in the Primary Tenant and assigned to a Subtenant :superscript:`5.4.6`
           - Updates to database schema for network domains table to prevent issues in specific scenarios :superscript:`5.4.6`
:Oneview: - Fixed ``cacheServerTemplates`` log errors during Oneview cloud syncs :superscript:`5.4.6`
:OpenStack: - Fixed an issue that could cause provisioning failure when using an image that has recently been uploaded :superscript:`5.4.6`
             - Fixed issue with PowerVC attribute error during provisioning. :superscript:`5.4.6`
:Oracle Cloud: - Removed "Oracle Cloud VM Instance" and "Oracle Cloud Windows Instance" selections from the "Add Resource" menu under the Hosts tab on an Oracle Cloud detail page :superscript:`5.4.6`
:Plans & Pricing: - Increased precision of price and cost sets to eight decimal places to ensure accurate figures in all scenarios :superscript:`5.4.6`
:Plugins: - Fixed an issue that could cause problems integrating plugins with HA appliances :superscript:`5.4.6`
:Policies: - Fixed an issue that caused Budget Policies to be applied incorrectly in some situations when App Blueprints were provisioned in Subtenants :superscript:`5.4.6`
            - Fixed an issue that caused Max VM Policies to be applied incorrectly in certain situations when multiple copies were provisioned simultaneously :superscript:`5.4.6`
:PowerShell: - Fixed an issue that caused PowerShell Tasks run against remote hosts to throw errors and not run as expected :superscript:`5.4.6`
:Reports: - Fixed a filtering issue that could cause some reports or views to show no data when filtered by Cloud or Group :superscript:`5.4.6`
           - Fixed an issue with the Time Series Cost report that caused errors to be thrown when the report was run with certain filters applied :superscript:`5.4.6`
:SCVMM: - Fixed an issue that prevented provisioning of VMs with multiple disks on SCVMM Clouds :superscript:`5.4.6`
:Security: - Fixed permission issue with /library/services api endpoint :superscript:`5.4.6`
            - Security: Fixed issue with tenant permissions for some /network/services endpoints :superscript:`5.4.6`
:Tags: - Tags applied to Kubernetes Master/Worker nodes via |morpheus| CLI ``hosts update --tags`` command are no longer removed on the next cloud sync :superscript:`5.4.6`
:Tasks: - Fixed an issue that caused stored credentials not to be loaded properly when editing a Task associated with a credential set (HTTP Task or Task executed on a remote server) :superscript:`5.4.6`
:Virtual Images: - The "Source Image" on an Instance detail page is no longer hyperlinked back to the Virtual Image detail page when the user does not have permission to view the Virtual Image :superscript:`5.4.6`
:Wiki: - Improved sync of Wiki content for Instances containing multiple VMs, including handling situations when the first VM in the Instance is deleted :superscript:`5.4.6`
:vCloud Director: - Subtenant users can now create and manage NSX-T routers in vCD Clouds shared from the Primary Tenant :superscript:`5.4.6`


Appliance & Agent Updates
=========================

:Appliance: - Appliance Java version updated to 11.0.15+10 :superscript:`5.4.6`
             - Ubuntu 22.04 (Jammy) is now supported for Morpheus Appliance hosts :superscript:`5.4.6`

:Agent Packages:  - Linux Node & VM Node Package Java version updated to 11.0.15+10 :superscript:`5.4.6`. MacOS agent java remains at 11.0.14+9 due to 11.0.15+10 jre macos pkg issue.
                  - Linux Node & VM Node Package verison update to 3.2.7                 
                  - Linux Node Packages now support installing Dokcer on Ubuntu 22.04 (Jammy) :superscript:`5.4.6`
                  - Windows Agent msi packages updated to 1.8.0-2 with updated certificate. Note the Morpheus Windows Agent version (1.8.0) has not changed, this update only applies to the .msi installer packages & there is no need to update existing 1.8.0 agents. :superscript:`5.4.6`