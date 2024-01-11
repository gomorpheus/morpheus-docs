.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. IMPORTANT:: |morphver| contains embedded MySQL v8 upgrade when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
.. IMPORTANT:: Minimum v6.x required to upgrade to |morphver| for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6, or 6.1.0 - 6.2.1 prior to upgrading to |morphver|
.. WARNING:: Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - Removed API calls and CLI commands related to |morpheus| Dashboard as that is no longer a standardized page and may be replaced by a Dashboard Plugin in some appliances :superscript:`6.2.6`
:Ansible Tower: - Added more descriptive error messages for failed Ansible Tower Tasks, particularly when the Task fails due to being pointed at an incorrect Inventory to make it clearer to the user what has failed :superscript:`6.2.6`
:Apps: - Removed the Tier subtab within the Instances tab of the App detail page :superscript:`6.2.6`
:Plugins: - Nutanix Prism Central plugin leaves beta and enters general availability. See share.morpheusdata.com for more information and release notes specific to this plugin :superscript:`6.2.6`
:Security: - Upgraded ``gradle.properties`` to 9.0.83 to mitigate multiple CVEs :superscript:`6.0.11 6.2.6`
            - Upgraded ``netty`` to version 4.1.100.final to mitigate CVE-2023-44487 and CVE-2023-41881 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-boot-actuator-autoconfigure`` to 2.7.11 to mitigate CVE-2023-20873 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-boot-autoconfigure`` to 2.7.12 to mitigate CVE-2023-20883 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-boot`` to version 2.7.18 to mitigate CVE-2023-34055 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-expression`` to version 5.3.17 to mitigate CVE-2022-22950 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-expression`` to version 5.3.27 to mitigate CVE-2023-20863 and CVE-2023-20861 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-security-web`` to 5.7.8 to mitigate CVE-2023-20862 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-webmvc`` to version 5.3.30 to mitigate CVE-2023-20860 :superscript:`6.0.11 6.2.6`
            - Upgraded ``jknack/handlebars.java`` to version 4.3.1 to mitigate CVE-2022-42889 :superscript:`6.0.11 6.2.6`


Fixes
=====

:API & CLI: - Fixed 500 errors being shown when calling ``invoices refresh -c`` against Cloud types that didn't support it in favor of more graceful handling :superscript:`6.2.6`
             - Fixed CLI call to fetch certificates to limit the list to just those shown on the SSL certificates list page in UI :superscript:`6.2.6`
             - Fixed calls to ``/api/options/zoneNetworkOptions`` giving the "threw a gasket" error when not supplied with ``zoneId`` and ``provisionTypeId`` query parameters :superscript:`6.2.6`
             - The "name" and "phrase" filter parameters are now working correctly for calls to GET ``/api/provision-types`` :superscript:`6.2.6`
             - The API call to GET all IP addresses for a specific network pool is now updated so it will filter the results properly by the "hostname" query parameter :superscript:`6.2.6`
             - When provisioning an Instance via |morpheus| API or CLI, the IP address and port endpoints are no longer being duplicated in the addresses popout on the Instance detail page Summary tab :superscript:`6.2.6`
:Agent: - Upgraded |morpheus| Agent to prevent automation failures when run under specific conditions :superscript:`6.0.11 6.2.6`
:Amazon: - When Instance tags are edited in |morpheus| after provisioning, the Labels value on associated volumes is no longer updated :superscript:`6.2.6`
:Azure: - Fixed Azure Run not being used for Agent installs or running Tasks (when Agent not present) when set as the default RPC for an Azure Cloud :superscript:`6.2.6`
         - Fixed an incorrect failure message that was shown after successfully adding worker nodes to an AKS cluster :superscript:`6.2.6`
         - If an Azure scale set VM is deleted in the Azure portal, the sync back to |morpheus| via cloud refresh no longer triggers an extra VM delete request in Azure as this caused confusion during auditing :superscript:`6.2.6`
         - When |morpheus| cleans up discovered VMs which have deleted from Azure, it no longer lists in the Activity section that they were deleted by |morpheus| (which was misleading as |morpheus| did not delete them) :superscript:`6.2.6`
:Catalog: - Added DISABLE AUTO PRICE option to Catalog items which disables dynamic price updates each time a field is changed at purchase time. This is useful when Configuration Tasks take significant time to run as it can bog down the Catalog Item purchase process :superscript:`6.2.6`
:CloudFormation: - Fixed an issue that prevented saving CloudFormation-based App Blueprints sourced from a Git repo containing a CF JSON file :superscript:`6.2.6`
:Costing: - Fixed slight inconsistencies with costing when Service Plans included prices based on multiple time intervals (such as monthly and hourly) :superscript:`6.2.6`
:Cypher: - Fixed Cypher initialization on Tenant creation as provisioning could sometimes fail the first time Cypher was invoked in a brand new Tenant :superscript:`6.2.6`
:Domains: - The Domain Name setting in the Create/Edit Domain dialog is now working properly such that any selected Domain from the dropdown list doesn't override the Domain Name setting :superscript:`6.2.6`
:File Shares: - |morpheus| now provides a friendly error message when creating a File Share without providing a file path rather than generating an unhandled exception :superscript:`6.2.6`
:Forms: - Fixed an issue that caused provisioning failures from Form-based Catalog items when multiple AWS Clouds were present to select :superscript:`6.2.6`
         - Fixed an issue where the default disk size for a selected custom service plan would not be displayed when provisioning a Catalog Item based on the Form :superscript:`6.2.6`
         - When adding an existing Typeahead-type Input to a form, you can no longer edit the CUSTOM DATA field of the Input through the Form builder :superscript:`6.2.6`
         - When ordering a Catalog Item which uses the Byte Size-type Input on Forms, the order review page will now show the value in the selected units (MB or GB) rather than showing it in bytes :superscript:`6.2.6`
         - When selecting a Plan during Catalog provisioning, the cores per socket default value associated with the Plan now fills properly and gets displayed :superscript:`6.2.6`
:Git Repository: - Fixed some issues related to integrating Git repositories and related to master/main branch issues :superscript:`6.2.6`
                  - For Gitlab integrations, the TOKEN field of the Add Integration modal is now ignored as this was primarily meant for Github integrations and it caused issues with Gitlab :superscript:`6.2.6`
:Google Cloud (GCP): - Fixed underscore characters "_" being removed from GCP tags during certain processes, such as when converting a discovered workload to managed :superscript:`6.2.6`
:Inputs: - Validation failure notices are now given when submissions are unsuccessful due to hidden yet required Inputs :superscript:`6.2.6`
:Instances: - Added UI improvements to clarify which Instances actions a user may take (based on Role permissions) from the ACTIONS menu on the Instances list page :superscript:`6.2.6`
             - Fixed network proxy settings not being applied to Windows Instances :superscript:`6.2.6`
             - Improved the process of Instance resizing to ensure correct result in more scenarios :superscript:`6.2.6`
:Jobs: - Instances are now removed as targets for Jobs when the Instance is deleted for performance and database upkeep reasons :superscript:`6.2.6`
:Kubernetes: - Fixed duplicate volumes being shown in the Volumes tab on Cluster detail pages :superscript:`6.2.6`
:NSX-T: - The Create Group dialog accessible from the Groups tab on the NSX-T integration detail page now has a functional add typeahead field under Members > Member Type: Virtual Machine :superscript:`6.2.6`
:Network: - Fixed gateway and DNS details being ignored when non-|morpheus| type IPv6 pools were used :superscript:`6.2.6`
:Nutanix: - Fixed Nutanix VMs still having ISOs mounted even after finalization of the provisioning process was complete :superscript:`6.2.6`
           - Fixed Snapshots created via a Backup in one Tenant being assigned ownership to an incorrect Tenant which caused issues when attempting to revert to the Snapshot :superscript:`6.2.6`
:OpenStack: - OpenStack subnets are now removed from |morpheus| after the next Cloud sync when they have been deleted from the OpenStack side :superscript:`6.2.6`
:PowerVC: - Fixed an issue that could cause PowerVC provisioning failures in certain configurations :superscript:`6.2.6`
:VMware: - Fixed an issue that caused the configured time zone on VMware Cloud settings or in the Instance provision wizard not to be honored in certain cases during Windows provisioning :superscript:`6.2.6`
:Veeam: - Improved response messages returned when deleting Veeam integrations through |morpheus| API and |morpheus| UI to make it clearer to the user that the delete action was successful :superscript:`6.2.6`
:Wiki: - Notes added to VMs on the VMware side are now written to the Instance Wiki in addition to the server Wiki when the discovered VMware VM has been converted to managed :superscript:`6.2.6`
:Workflows: - Fixed an issue that caused certain Tasks in Provisioning Workflows not to be executed at the proper time if another unrelated Task was deleted from the Provisioning Workflow after provisioning :superscript:`6.2.6`


Appliance & Agent Updates
=========================

:Appliance: - Upgraded embedded ``erlang`` to version 26.1.2 :superscript:`6.0.11 6.2.6`
:Agent: - |morpheus| Linux Agent updated to v2.5.2 to prevent automation failures when run under specific conditions :superscript:`6.0.11 6.2.6`
:Node Packages: - |morpheus| node and vm-node packages updated to v 3.2.0 with |morpheus| Linux Agent v2.5.2 :superscript:`6.0.11 6.2.6`