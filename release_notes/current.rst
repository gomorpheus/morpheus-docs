.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. important:: Updates to many plugins have been timed for the release of |morpheus| 5.5.2. After completing an appliance upgrade, see share.morpheusdata.com and apply any plugin updates which may be available. Those using a previous version of the Infoblox plugin (prior to 1.1.0) should note that the new version of the plugin will not directly upgrade an existing version. This is because previous versions had an identification code of ``infoblox2`` whereas all future versions will have an identification code of ``infoblox``. This was done to prevent conflicts with the embedded Infoblox integration during early testing which has now concluded. The best upgrade approach is to remove any existing integrations and earlier versions of the plugin, apply the new plugin, and re-create your integrations. If this is not possible, there is a method by which existing pool server entries in the database can be updated for the new version of the plugin. Please contact |morpheus| support for assistance with this process and reference this note in your case.

.. important:: |morpheus| |morphver| requires Morpheus Worker |workerVer|. Please upgrade any existing Morpheus Workers to the |workerVer| Worker package to ensure compatibility with Morpheus |morphver|.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

Release Dates
  - 5.5.2 |releasedate|

- .. toggle-header:: :header: **5.5.2 RBAC Changes**

    |morpheus| 5.5.2 includes changes to Role permissions UI, improvements to make permissions more granular, and changes to make Tenant management easier for Primary Tenant administrators. See the embedded video below for a walkthrough of the changes.

    .. raw:: html

        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
            <iframe src="//www.youtube.com/embed/752-Bnu0f30" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
        </div>

|

New Features
============

:API & CLI: - Added API and CLI coverage for creating and working with Security Scan Jobs which was already possible from |morpheus| UI :superscript:`5.4.12`
             - Added API and CLI coverage for creating and working with security package templates for security scans which is already possible via |morpheus| UI :superscript:`5.4.12`
             - Added API endpoints to manage the creation and deletion of user-created OAuth clients
             - Added API functionality to update the permissions of Ansible Tower>Inventory items :superscript:`5.4.13`
             - Added ability to associate Instance Type Layout Price Sets to Layouts via |morpheus| API and CLI. This functionality has also been added to |morpheus| UI
             - Added ability to associate Instance Type Price Sets to Instance Types via |morpheus| API and CLI. This functionality has also been added to |morpheus| UI
             - Added bulk "remove from control" functionality to |morpheus| API and CLI for removing Instances based on brownfield workloads from |morpheus| control. Greenfield Instances still must be deleted to be removed for licensing reasons
             - Added plugin upload capability for |morpheus| API and CLI :superscript:`5.4.12`
             - Alert and Contact creation is now handled as expected through |morpheus| API and CLI when "Monitoring" Role permission is set to "User" level :superscript:`5.4.10`
             - Create and manage Scale Thresholds (Library > Automation > Scale Thresholds) from |morpheus| API and CLI :superscript:`5.4.11`
             - Improved |morpheus| API and CLI response related to networks including the addition of Search Domains when getting Networks and setting/updating Search Domains :superscript:`5.4.11`
             - IPAM Network Integrations can now be added via API
             - Labels can now be added to Tasks, Workflows, and Jobs through |morpheus| API and CLI
             - New feature permission "Lifecycle: Environment Variables" can be managed through |morpheus| API and CLI
             - Updating Kubernetes Clusters via |morpheus| API or CLI now allows toggling the "Managed" attribute or adding an "API Token" value as you can already through |morpheus| UI :superscript:`5.4.9`
             - When integrating Clouds via |morpheus| API and CLI, associating a custom icon with the new Cloud is now supported
             - ``library-node-types`` add and update commands in |morpheus| CLI now properly support passing in ``evars`` and ``evars-json`` parameters :superscript:`5.4.10`
:Alerts: - Users with "Monitoring" Role permission set to "User" can now only edit and delete contacts they've created and can only set alert rules for Apps/Instances they can access (even when selecting all) :superscript:`5.4.10`
:Amazon: - Amazon storage pricing is now syncing instead of seeded
          - Jakarta (ap-southeast-3) and UAE (me-central-1) regions added for scoping Amazon AWS Clouds :superscript:`5.4.10`
:Azure: - Azure workloads can now be provisioned to different regions from the resource group (if desired) as you can from the Azure web console :superscript:`5.4.9`
         - Guidance recommendations can now be surfaced for Azure VMs which don't have the |morpheus| Agent installed
         - The Inventory Level field has been removed from Azure Cloud config. It was previously needed to enable or disable power state sync for Azure workloads but this data can now be gathered from other API payloads we already sync for other purposes
:Clouds: - Added ability to associate existing VMs (Infrastructure > Compute > Virtual Machines) to different Clouds. **NOTE: This is not a migration tool. Once a workload has been moved to a new Cloud, use this functionality to associate the existing managed VM record to the new Cloud and wipe out the newly discovered unmanaged VM record. This preserves the original VM record and associated historical data while recognizing the new Cloud and continuing monitoring operations from the new VM** :superscript:`5.4.9`
          - Added the ability to set custom icons when integrating new Clouds or editing existing Clouds.
          - The Connection Options section of the Cloud config modal has been moved higher for added visibility. This section only appears when proxies or workers are set up in |morpheus|
          - When first integrating a new Cloud, the Cloud's status will be given as "initializing" to indicate that the Cloud is doing its initial syncs before going into "OK" status to indicate that the Cloud integration is ready
:Compute: - Added ability to remove Instances based on brownfield workloads from |morpheus| control in bulk from the Instances List Page. Greenfield workloads must still be deleted to be removed for licensing reasons
:Currency: - Add support for Polish Zloty (PLN) currency :superscript:`5.4.12`
:Distributed Worker: - Set a currently-integrated Morpheus Worker as the default gateway for remote console sessions in global settings (|AdmSet|). Integrated VDI gateways can also be set as the default gateway for console access on Networks (|InfNet|)
:Google Cloud (GCP): - Cloud sync for GCP Clouds is no longer interrupted when Projects are disabled or do not have API access granted :superscript:`5.4.9`
                  - The "Google Cloud" built-in Instance Type now includes the option to select public images in addition to private and local images which were previously available
:Groups: - When adding Clouds to Groups (from the Clouds tab of Group detail page), added the ability to select multiple Clouds and add them to the Group simultaneously
:Guidance: - Guidance added for Amazon Orphaned Volumes
            - |morpheus| Guidance now detects orphaned volumes as an opportunity for cost savings
:Jenkins: - The Jenkins integration has been deprecated and removed from the product. A Jenkins Task Plugin has been created for triggering Jenkins jobs. See share.morpheusdata.com for more details on that Plugin :superscript:`5.4.12`
:Jobs: - Provisioning : Jobs list view updated to Advanced Table
:Labels: - Users can now label many |morpheus| constructs (Tasks, Workflows, Jobs, App Blueprints, Instance Types, Layouts, Node Types, Virtual Images, Inputs, and Option Types) for easier filtering of large list views
:Library: - Dark theme versions of Instance Type logos can now be managed via |morpheus| API and CLI :superscript:`5.4.12`
:Morpheus IP Pools: - Added IPv6 pool support for |morpheus| IP Pools
:Network: - Network labels (display names) are now editable from the Network tab of the Instance detail page :superscript:`5.4.10`
:OpenStack: - Added ability to create OpenStack Manila FileShares
:Oracle Cloud: - Oracle Cloud costing features have migrated from using the Cloud Metered Billing API to using Cost and Usage Report data :superscript:`5.4.11`
:Plans and Pricing: - Add Instance Type Layout Prices to Instance Type Layout Price Sets and associate them with Layouts. When workloads are provisioned based on the associated Layout, this pricing is added to any which may apply from the Service Plan
                  - Add Instance Type Prices to Instance Type Price Sets and associate them with Instance Types to add additional costing amounts to any which may apply from the Service Plan pricing
                  - Added capability to export Service Plans list as a CSV document (Administration > Plans & Pricing > Plans) :superscript:`5.4.9`
:PowerDNS: - PowerDNS integrations now include the "Create Pointers" option to automatically create reverse records as other DNS integrations currently do :superscript:`5.4.9`
:Puppet: - Support added for Puppet Agent 7 :superscript:`5.4.10`
:Roles:  - Access to Workflows and Tasks can now be delegated by Role. From the Role detail page, Task and Workflow tabs can now be used to control access for each Role
         - Added a search bar to the Features tab of the User detail page and to the Features tab of the Role detail page. This makes it easy to search for a specific feature permission to determine a User or Role access
         - Added new Role permission Lifecycle: Environment Variables.This was split out from the former Provisioning: Instances permission to increase granularity and handles access to the Environments tab on the Instance detail page, as well as related API functionality
         - Added new Role permission Provisioning: Instances: Add. This was split out from the former Provisioning: Instances permission to increase granularity and handles access to the Add Instances wizard as well as the Add Instances API
         - Added new Role permission Provisioning: Instances: Delete. This was split out from the former Provisioning: Instances permission to increase granularity and handles access to the Instance delete actions in |morpheus| UI and the delete Instances API
         - Added new Role permission Provisioning: Instances: EditThis was split out from the former Provisioning: Instances permission to increase granularity and handles access to the EDIT button on Instance detail pages as well as the update Instances API
         - Added new Role permission Provisioning: Instances: List. This was split out from the former Provisioning: Instances permission to increase granularity and controls which Instances the users sees on the Instances list page
         - Added new Role permission Provisioning: Instances: Lock/Unlock. This was split out from the former Provisioning: Instances permission to increase granularity and handles access to the lock/unlock action for Instances as well as the corresponding API
         - Added new Role permission Provisioning: Instances: Lock/Unlock.This was split out from the former Provisioning: Instances permission to increase granularity and handles access to scaling-related features on the Instance detail page. This includes Add/Remove Node from the Actions menu, access to Thresholds and Schedules from the Scale tab, and related API functionality
         - Added new Role permission Provisioning: Instances: Settings.This was split out from the former Provisioning: Instances permission to increase granularity and handles access to the Settings tab of the Instance detail page. This tab allows for setting SSL Certificates and other settings files. This permission also encompasses the related API actions
         - Added new Role permission Provisioning: Power Control. This was split out from the former Provisioning: Instances permission to increase granularity and handles access to power state controls for Instances and VMs
         - Added paging to each tab on Role detail pages, such as the Instance Types tab, Groups tab, and all other tabs which appear on this page. This improves load performance and searchability of very large lists
         - Improved experience of setting Role permissions by adding categories, permissions descriptions, and global permission toggles to the Role detail page
         - "Provisioning: State" role permission added to control access to the State tab on Terraform Instance detail pages. **IMPORTANT**: This permission is "None" by default for all users other than System Admins. Following upgrade, users which are not System Admins will no longer have access to the State tab. Role permissions will need to be updated for all users which need access to the State tab. :superscript:`5.4.9`
         - The existing permission Provisioning: Allow Remove From Control has been renamed Provisioning: Remove From Control
         - The existing permission Provisioning: Remote Console can now be set to "User" which gives console access only to workloads provisioned by the current user. The "Provisioned" permission setting is removed
         - Updated the functionality of individual object permission tabs for Roles (Groups, Clouds, Catalog Items, etc.). Set a default access for all objects of that type (Full or None) and then individually apply alternate rights to individual objects if needed
         - User Roles within Subtenants can now be edited from the Primary Tenant. Previously Primary Tenant Users needed to impersonate a Tenant User to edit these Role permissions
:Rubrik: - Rubrik integration settings are updated to remove username and password fields and replace them with an API key field. Existing integrations will continue to work unless upgraded to the latest Rubrik versions which require MFA to be enabled. :superscript:`5.4.9`
:SAML: - When creating a new SAML integration, the default SAML REQUEST value is now "Self-Signed" and the default SAML RESPONSE value is now "Validate Assertion Signature" to prevent unintentional insecure configuration :superscript:`5.4.11`
:SCVMM: - Reconfiguring SCVMM Instances or VMs between dynamic and static service plans now includes improved memory validation :superscript:`5.4.10`
:Security: - MySQL upgraded to 5.7.39 (CVE-2022-1292, CVE-2022-27778, CVE-2018-25032, CVE-2022-21515) :superscript:`5.4.9`
            - Velocity templates upgraded to 2.3 (CVE-2022-13936) :superscript:`5.4.9`
            - aws-java-sdk-s3 upgraded to version 1.12.261 (CVE-2022-31159) :superscript:`5.4.9`
            - esapi upgraded to version 2.3.0.0 (CVE-2022-23457) :superscript:`5.4.9`
            - liquibase-core upgraded to 4.14.0 (CVE-2022-0839 :superscript:`5.4.9`
            - mysql-connector-java upgraded to 8.0.28 (CVE-2022-21363) :superscript:`5.4.9`
            - tomcat upgraded to 9.0.65 (CVE-2022-34305) :superscript:`5.4.9`
            - xmlrpc-common upgraded to version 3.1.3 (CVE-2019-17570) :superscript:`5.4.11`
            - xmlsec upgraded to 2.2.3 (CVE-2021-40690) :superscript:`5.4.9`
:ServiceNow: - Added support for using a MID server during credential validation (in both single and multi-tenant installations) as well as support for using a MID server when fetching the auth token :superscript:`5.4.10`
              - Inputs with visibility dependent on other Inputs are now shown/hidden properly on Catalog Items exposed to ServiceNow via the |morpheus| plugin
              - The History tab on Instance detail pages now includes an entry for when provisioning approval from a ServiceNow integration was given
              - When Instances are ordered through a ServiceNow integration, the RITM number is tracked on the Instance (or Inventory) detail page
              - When a |morpheus| alert triggers an incident in a ServiceNow integration, we now tie the incident to the Configuration Item (CI) if the integration is set as the CMDB for the workload
              - When approvals are routed through a ServiceNow integration, custom options (name/values pairs) set on the Catalog Item, Instance Type, or Layout are surfaced in the approval request seen from ServiceNow
:Settings: - Added Clients tab to global settings to create a space for managing OAuth client functionality. Add new entries and set the expiration time for any generated tokens. Generate a new token under the created client in the API Access area of User Settings
            - Global logging settings (|AdmSet|) are now shown on the Monitoring tab rather than having their own tab
:Softlayer: - Softlayer cloud type has been removed. Existing softlayer clouds will be migrated automatically to the IBM cloud type.
:Tasks: - Added pop-out column to the add/edit Tasks modal which allows the user to easily drag and drop |morpheus| variable calls into the Task config
        - Tasks now have a visibility field which allows |mastertenant| users to share Tasks with Subtentants (public visibility) if desired
:Terraform: - Added data grouping to the Resource tab of the Detail page for Terraform Apps and Instances to make data more consumable in situations with large numbers of resources :superscript:`5.4.10`
             - Improved Terraform state file cleanup procedures after Terraform apply and delete actions are taken :superscript:`5.4.10`
             - Improved Terraform state import (brownfield Terraform management) functionality to support a greater number of Terraform spec configurations :superscript:`5.4.11`
             - Support added for Terraform 1.2.x Apps and Instances :superscript:`5.4.10`
             - Terraform Spec Templates can now reference directories of a Git repository and automatically onboard all files (including those in subdirectories) into the Spec Template similar to the way Terraform App Blueprints can already reference directoriesPreviously, Terraform Spec Templates needed to reference individual .tf files :superscript:`5.4.10`
             - Terraform variables flagged as "sensitive" are now masked from all areas of |morpheus| UI. Previously they were masked in provisioning wizards but could be revealed in some other places :superscript:`5.4.10`
:UI: - Execute Tasks and Workflows actions from Instance and server detail pages are now typeahead fields due to the potentially large number of Tasks and Workflows in some environments
      - From the Clouds Tab of the Group Detail Page, users can only add and remove existing Clouds for the Group. Users can no longer integrate new Clouds or edit existing Clouds from this page
:Usage: - Calls to the billing API now includes a ``usages`` block in the return payload which includes resource information (CPU cores, memory, disk sizes, etc.) for the Instance/VMThis ensures users can access this information for accurate billing even in situations where the associated price types are resource-agnostic (such as "Everything" price types) :superscript:`5.4.10`
:Users: - The tabs on the User detail page (for Group Access, Instance Types, etc.) are all now paged to improve performance and searchability when lists are very long
:vCloud Director: - VMs for multi-node vCD Instances are now created within the same vApp on the vCD side. Previously, a separate vApp was created for each VM :superscript:`5.4.9`
:Workflows: - Added Price phase to Provisioning Workflows. This phase is invoked when the Workflow is tied to a Layout and allows Task logic to override any other pricing (such as on the Service Plan). See the Workflows section of |morpheus| docs for a demonstration



Fixes
=====

:API & CLI: - API endpoints for adding power schedules to Instances have been updated for intuitiveness and consistency :superscript:`5.4.12`
             - Fixed ``archives list-files`` CLI command to properly list files in buckets by bucket ID or by "bucket:/path" string arguments
             - Fixed an issue causing commands to get a Cloud or list Clouds within Subtenants to return incorrect Group IDs :superscript:`5.4.12`
             - Fixed an issue that caused "Library Script" and "Library Template" type Tasks created via |morpheus| CLI not to be associated with the script or template resource indicated in the command :superscript:`5.4.12`
             - Fixed an issue that caused Azure Instance resizing to fail when triggered via |morpheus| API or CLI :superscript:`5.4.12`
             - Fixed an issue that caused OpenStack, Huawei, and OTC Clouds created via |morpheus| API and CLI not to work properly :superscript:`5.4.9`
             - Fixed an issue that caused the "providerType" query parameter for the Get All Cluster Types API call not to work properly :superscript:`5.4.12`
             - Fixed an issue that caused the Tenants block not to be returned for some Network objects when calling the Get All Networks endpoint :superscript:`5.4.13`
             - Fixed an issue that caused the ``price-sets list`` command in |morpheus| CLI to fail with an Unexpected Error :superscript:`5.4.10`
             - Fixed an issue that could cause provisioning of Azure Marketplace images through |morpheus| API to fail depending on marketplaceOffer syntax used :superscript:`5.4.11`
             - Fixed an issue that prevented Service Plans from being created via |morpheus| CLI without a pre-determined disk size (which should be allowed)
             - Fixed an issue that prevented adding deployment versions of type "fetch" using the no prompt approach and specifying the fetch URL option in the command :superscript:`5.4.9`
             - Fixed an issue that prevented upload of Virtual Images of type azure-reference via |morpheus| CLI :superscript:`5.4.9`
             - Fixed an issue with adding Oracle Cloud Instances via |morpheus| CLI which would fail due to a missing Availability Zone prompt :superscript:`5.4.11`
             - Fixed an issue with the |morpheus| CLI ``clouds-add`` command not prompting for stored credential sets to authenticate the cloud integration :superscript:`5.4.10`
             - Tags can now be added normally via |morpheus| API and CLI to Instances added by provisioning an App Blueprint. Previously, these needed to be passed via the customOption block in an update JSON block :superscript:`5.4.9`
             - The ``networkServer`` property is now being returned at the root of the return payload from calls to the Get All Clouds and Get a Specific Cloud API endpoints :superscript:`5.4.10`
             - When creating Azure Resource Pools via |morpheus| API, the inventory flag now defaults to true to minimize confusion :superscript:`5.4.9`
             - When sourcing an Option List from the |morpheus| Plans API, memory and storage fields now return data properly rather than null values :superscript:`5.4.12`
:ARM: - ARM template parameters are now visible in the instance wizard when provisioning a instance type pointing to an ARM template when logged in as a sub-tenant user. :superscript:`5.4.13`
:Alibaba Cloud: - Fixed an issue affecting the display of the Costing Status value on the detail page for Alibaba Clouds
:Amazon: - Fixed an issue related to |morpheus| Agent install when cloning Amazon Windows Instances :superscript:`5.4.10`
          - Fixed an issue that caused duplicate backups to occur for AWS Instances when scheduled backups were run :superscript:`5.4.12`
          - Fixed an issue that caused failed provisioning with AWS Aurora MySQL Instances :superscript:`5.4.10`
          - Fixed an issue that caused provisioning the |morpheus|-default AWS Ubuntu 22.04 image to fail :superscript:`5.4.11`
          - Fixed an issue that caused the server.hostName property to be dropped after provisioning AWS Windows Instances. This could lead to configuration failures following provisioning :superscript:`5.4.10`
          - Fixed an issue with Amazon AWS Security Group detail pages that caused the list of Instances associated with the SG to be blank :superscript:`5.4.12`
          - Users can now successfully provision to AWS Clouds when Service Control Policies for Tagging are set in AWS :superscript:`5.4.9`
          - When provisioning a Windows Instance to AWS, hostnames longer than 15 characters are now truncated down to 15. This is to resolve an issue preventing backup restoration if the hostname was too long :superscript:`5.4.11`
:Ansible Tower: - Ansible Tower Tasks and Workflows can now be run against the server context. Previously they could only be run against the Instance context :superscript:`5.4.9`
                 - Ansible Tower Tasks can now be configured to use the Tenant default inventory whether the |mastertenant| has a default inventory set or not :superscript:`5.4.13`
                 - Fixed an issue that caused Ansible Tower sync to break if templates with certain configurations are deleted via |morpheus| :superscript:`5.4.11`
:Ansible: - Ansible Tasks and Workflows now use the '/var/opt/morpheus/morpheus-local/workspace' directory instead of '/var/opt/morpheus/morpheus-ui/workspace' :superscript:`5.4.9`
           - Ansible scripts now work when applied against the Instance level, previously these would fail but would be successful when run against the server level :superscript:`5.4.11`
           - Fixed an issue that caused App provisioning to fail if the Ansible command options field was locked on the App Blueprint :superscript:`5.4.9`
           - When |morpheus| Agent is installed but the command bus is not used, |morpheus| will now use the SSH username and keypair :superscript:`5.4.9`
:Apps: - Fixed an issue that caused only one Instance within an App to be displayed on the App detail page if the Instance contained many nodes (~25+) :superscript:`5.4.12`
:Automation Execute Schedules: - Fixed UI issues related to plain text cron interpretation shown when creating or editing and Execution Schedule :superscript:`5.4.13`
                  - Fixed an issue that caused the Edit Execution Schedule modal window to hang if certain special cron expressions were used :superscript:`5.4.10`
:Automation Scale Thresholds: - Fixed an issue that could cause Scale Thresholds to repeatedly create and destroy VMs under certain configurations :superscript:`5.4.9`
:Automation Tasks: - Fixed an issue that prevented users from creating or editing Tasks if they did not have "Infrastructure: Credentials" permissions set to Full on their Roles :superscript:`5.4.9`
                  - When a Task is referencing a file tracked in a Github repository that does not exist, the Task detail page can now be viewed rather than a 403 error page being displayed :superscript:`5.4.9`
                  - When selecting many Instances or servers (typically around 15 or more), and running a Task or Workflow against them, the desired automation is now run on all selected workloads rather than just some :superscript:`5.4.9`
:Automation Workflows: - Fixed an issue that caused Post Provision-phase to be executed twice on ARM template-based Instances :superscript:`5.4.11`
:Azure: - Additional refinements have been added to Azure costing computations to ensure complete accuracy in very specific situations :superscript:`5.4.10`
         - Azure Clouds no longer lose their scope (Resource Group and Region) when updating the Client Secret used to authenticate the Cloud :superscript:`5.4.9`
         - Fixed an issue that caused Azure NSG source ports to be overwritten to the destination port value following Cloud sync. This issue affected only the port shown in |morpheus| UI, it did not actually make that change in the Azure backend :superscript:`5.4.12`
         - Fixed an issue that caused a Cloud costing refresh for a previous month to raise invoice amounts, which required costing to be rebuilt to be accurate once again :superscript:`5.4.9`
         - Fixed an issue that could cause the backup and restore process for Azure workloads to set an incorrect storage type (Premium SSD, etc.) :superscript:`5.4.10`
         - Fixed an issue that could prevent Azure provisioning under specific scenarios if a stored credential set was used to authenticate the Cloud integration :superscript:`5.4.12`
         - Fixed an issue that prevented creating a new Azure Load Balancer to associate with an Instance if one was created at provision time and later removed via the Instance detail page :superscript:`5.4.9`
         - Fixed an issue that prevented setting destination ports on Azure Security Groups (NSGs) :superscript:`5.4.9`
         - Fixed an issue that preventing costing sync from ever completing for very large Azure Clouds :superscript:`5.4.9`
         - Fixed an issue which caused Azure Instances created from backup restoration to have incorrect disk type (HDD vs SSD, for example) :superscript:`5.4.13`
         - Improved handling of situations where the Azure API returns bad or unexpected responses :superscript:`5.4.10`
         - Private IP address changes on Azure workloads are now automatically synced back to |morpheus| :superscript:`5.4.10`
         - Service Plans are now synced for locations of all resource groups and all other VM locations to prevent situations where VMs could be discovered and no Service Plan would be set :superscript:`5.4.10`
:Backups: - Added a cleanup job to eventually expire out stuck or failed "in progress" backup jobs. This prevents a situation where a backup job can be stuck with no way to delete it :superscript:`5.4.9`
:Bluecat: - Fixed an issue that could create errors when provisioning Instances to Bluecat IP Pools
           - When Bluecat IP Pool names are updated in the Bluecat console, the changed name will now sync back to |morpheus| :superscript:`5.4.10`
:Blueprints: - App Blueprints can no longer be saved with identical names to other App Blueprints by pre-pending them with leading whitespace characters (which would be automatically removed after the validation step) :superscript:`5.4.9`
              - App Blueprints which currently have Apps deployed from them can no longer be deleted. UI messages are surfaced to inform the user why the App Blueprint cannot be deleted :superscript:`5.4.9`
              - Fixed an issue that could cause volume controllers to be mis-assigned when switching Layouts during App provisioning
              - Improved handling of situations when ARM Spec Templates are provisioned through the provisioning wizard without the adminPassword parameter set :superscript:`5.4.10`
:Buckets: - Fixed an issue that could cause "inactive" AWS S3 Buckets to still be visible in the UI :superscript:`5.4.9`
:Catalog: - Fixed a display issue that caused very long Input help blocks to overset the Catalog Item order window :superscript:`5.4.9`
           - Fixed an issue that caused very long Input labels to wrap incorrectly and end up behind the field itself :superscript:`5.4.9`
           - Fixed an issue that could cause a Catalog Item to lose Inputs during ordering if it was built and ordered under specific conditions :superscript:`5.4.11`
           - Fixed an issue that could cause areas of the Service Catalog Cart page to be formatted incorrectly if Input labels, Input values, or Catalog Item names/descriptions were very large :superscript:`5.4.9`
           - Fixed an issue that prevented provisioning of ARM template-based App Blueprints from the Service Catalog if the item relied on password values being set as Inputs :superscript:`5.4.105.4.9`
           - Fixed an unintended permissions-related issue that would cause a 500 error when browsing |ProCat| even if the user had required permissions :superscript:`5.4.11`
           - Fixed some odd behavior that could arise for Inputs in Service Catalog items depending on the interaction between dependent, visibility, and required settings related to other Input values :superscript:`5.4.9`
           - Hidden-type Inputs are no longer shown on the order review page when checking out selected Service Catalog items :superscript:`5.4.11`
           - The "More" button near the bottom of the Executions tab on the Catalog Inventory page now expands as expected :superscript:`5.4.9`
           - When editing an existing Service Catalog item that uses a |morpheus|-included logo, the saved logo no longer disappears from the Edit Catalog Item modal :superscript:`5.4.9`
           - Workflow-based Service Catalog items no longer have potential to hang when multiple typeahead Input values are selected :superscript:`5.4.10`
:Clone: - Fixed an issue that caused clones to fail for VMs which had been reconfigured :superscript:`5.4.10`
         - Fixed an issue that prevented the clone function from working properly if a Deploy Folder value was set on the Node Type :superscript:`5.4.9`
:CloudFormation: - Fixed an issue that caused CloudFormation Apps to fail deployment if they contained an EC2 Instance and had a UserData block :superscript:`5.4.10`
:Clouds: - Minor cleanup has been conducted around the Change Cloud functionality to make record presentation more accurate and user-friendly :superscript:`5.4.10`
          - The Cost History chart on Cloud Detail Pages now correctly plots small positive values higher than 0 along the Y axis :superscript:`5.4.10`
:Clusters: - Removed support for editing tags on clusters which was not working. Tags may still be added at cluster creation time and they are applied to the hosts rather than the cluster. :superscript:`5.4.13`
:Code: - Fixed an issue that caused failures when creating a Task from a Code Detail Page (|ProCod|) that referred to a specific Git Tag reference :superscript:`5.4.10`
:Compute: - Improved reporting of server OS in situations where |morpheus| is unaware of the guest OS platform :superscript:`5.4.9`
:Costing: - Fixed an issue that could cause incorrect currency to be configured for server-type invoices and server invoice line items in specific contexts :superscript:`5.4.10`
           - Fixed an issue that prevented configuration of GCP cloud costing using stored credentials (|InfTru|) :superscript:`5.4.10`
           - Fixed issues where invoices could show negative cost amounts under specific conditions :superscript:`5.4.9`
:Credentials: - Stored API key credentials (|InfTru|) now support longer inputs up to 1024 characters as API keys from some popular services could overset the previous limit
:Currency: - Currency exchange sync now honors any configured proxies :superscript:`5.4.11`
:Cypher: - When configuring Terraform App Blueprints, Users can no longer select and use tfvars files from Cypher if a Cypher Access Policy (|AdmPol|) restricts it from them :superscript:`5.4.10`
:DNS: - Fixed an pagination record that prevented zone records from the 26th domain and higher from being available in DNS integrations :superscript:`5.4.10`
:Distributed Worker: - Fixed an issue that caused Distributed Workers to disconnect which interrupted sync with associated Clouds :superscript:`5.4.9`
:Google Cloud (GCP): - Fixed issue with hyphens from GCP instance names being removed :superscript:`5.4.12`
                  - When provisioning to Google Cloud, the Hostname and Domain under Advanced Options on the Configure tab in the instance wizard are honored :superscript:`5.4.9`
:Guidance: - Guidance logic has been updated to default to $0 savings when the real savings cannot be determined. Previously, it defaulted to a nominal small amount but this change was made to avoid artificially increasing potential savings amounts
:Identity Sources: - Fixed CSP dev console errors that could appear in logs when viewing the Identity Sources list page :superscript:`5.4.9`
                  - Fixed an issue that could display identity source role mappings incorrectly when an existing identity source was edited :superscript:`5.4.9`
:Infoblox: - Improved validation on Infoblox integration add/edit modal to only allow a throttle rate up to 5000ms. If a greater time is entered, the value will be set to 5000 :superscript:`5.4.9`
:Inputs: - Fixed an issue that caused dependent Input fields not to reload in response to values added to the parent Input in certain contexts :superscript:`5.4.105.4.1`
          - Fixed issue with Verify Pattern validation for inputs that are hidden in the instance wizard
          - Password-type data in Inputs are no longer written to |morpheus| logs in plain text :superscript:`5.4.10`
          - Select List-type Inputs which have dependent refresh based on another Input no longer make the identical refresh call twice :superscript:`5.4.11`
          - When checkbox-type Inputs are left unchecked, their values are no longer missing from the Python "morpheus['customOptions']" :superscript:`5.4.9`
:Instances: - After renaming an Instance, the old Instance name no longer appears in the History tab of the Instance detail page. It is updated correctly :superscript:`5.4.12`
             - Fixed an issue that caused Instance counts not to be set correctly on the Instances list page when the user has no Group access :superscript:`5.4.11`
             - Fixed an issue that prevented Instance detail pages from being opened for brownfield Instances which were converted to managed and in a delayed/pending delete state :superscript:`5.4.12`
             - Fixed an issue where the listed size of an Instance disk could be incorrect following reconfigure that did not update disk size (though the disk was not actually resized) :superscript:`5.4.12`
             - The Instance display name (the value you would change when editing an Instance and updating the Name field) is now used to set a console tab's window name and used when searching for an Instance by name :superscript:`5.4.10`
:Jobs: - Fixed an issue that could prevent a Job from executing properly if done from the Job detail page (Provisioning > Jobs > Selected Job > Execute) :superscript:`5.4.9`
:Kubernetes: - Fixed an issue that caused Kubernetes Clusters provisioned to OpenStack Clouds with floating IP addresses to be unreachable from outside the cluster due to certificates being registered to private addresses rather than public :superscript:`5.4.9`
              - Fixed an issue that caused cluster stats not to be reported correctly on External (brownfield) Kubernetes clusters :superscript:`5.4.10`
              - Fixed an issue that could cause External Kubernetes clusters to become stuck in the deprovisioning state during deletion and never leave the UI :superscript:`5.4.9`
              - Plan is now hidden as expected when adding an external Kubernetes cluster from a Subtenant :superscript:`5.4.11`
              - Required fields are now respected when adding external Kubernetes clusters :superscript:`5.4.9`
:Layouts: - The "Permissions" selection inside the Action menu on a Layout Detail page (Library > Blueprints > Layouts > Selected Layout) now works correctly :superscript:`5.4.9`
:Library: - The set of and order for spec templates and file templates are being retained on node type add and edit/save. :superscript:`5.4.13`
:MicrosoftDNS: - Fixed an issue causing PTR records to be created in the wrong zone when creating MicrosoftDNS records via |morpheus| API :superscript:`5.4.9`
                - Fixed sync issue caused by ttl values in non-standard formats :superscript:`5.4.9`
:Monitoring: - Added TLS support for RabbitMQ-type checks (Monitoring > Checks) :superscript:`5.4.9`
:Network: - Fixed an issue that caused CSV export on several Network list pages (Networks, Network Groups, Domains, etc.) to fail :superscript:`5.4.11`
:NSX-T: - BGP Enable Status for NSX-T Tier0 Routers is now returned in a GET call to the |morpheus| API for the router :superscript:`5.4.9`
         - Fixed a CIDR validation issue on IPv6 networks which caused a number of issues and prevented networks from being saved with changes :superscript:`5.4.11`
         - Fixed an issue that caused creation of new NSX-T IP Pools to fail with errors :superscript:`5.4.12`
         - The Host Records tab is now hidden for NSX-T networks which are not associated with IP Pools to avoid confusion :superscript:`5.4.9`
:NetScaler: - When |morpheus| deletes a virtual server from NetScaler, it now also deletes the certificate :superscript:`5.4.11`
:Network: - Fixed an issue that caused the Edit modal to become inaccessible on certain network integration detail pages following a refresh of the page
           - Fixed an issue that preventing saving an IP Pool association at the time when a subnet was created requiring the user to edit the subnet once again to save the IP Pool association :superscript:`5.4.10`
           - The Scan Network property has been removed from networks in the UI, API, CLI :superscript:`5.4.13`
:OpenStack: - A more descriptive error is now surfaced when attempting to create an OpenStack Security Group when the SG quota is already reached :superscript:`5.4.9`
             - Fixed an issue that allowed the root volume to be resized for OpenStack Windows VMs in |morpheus| in some scenarios which shouldn't have been allowed :superscript:`5.4.12`
             - Fixed an issue that caused OpenStack Clouds scoped to all Projects to sync duplicate Virtual Images :superscript:`5.4.12`
             - Fixed an issue that caused a UI error to be surfaced when editing an OpenStack network (though the edit would be successful and Instances would pick up the changes correctly) :superscript:`5.4.10`
             - Fixed an issue that caused new OpenStack instance names not to be synced back to |morpheus| when updated on the OpenStack side :superscript:`5.4.12`
             - Fixed an issue that could cause additional disks to be shown in |morpheus| UI (not in the Cloud backend) when deploying Windows workloads to OpenStack Clouds :superscript:`5.4.9`
             - Fixed an issue that could cause discrepancy between network interface labels on an OpenStack Instance and that which was being reported on the Instance detail page in |morpheus| :superscript:`5.4.9`
             - OpenStack load balancer virtual server creation now works properly :superscript:`5.4.10`
             - Price calculations for OpenStack Instances and Apps now correctly account for storage costs :superscript:`5.4.10`
             - UI errors are now surfaced for situations when OpenStack load balancer creation cannot complete due to a load balancer quota having been reached :superscript:`5.4.10`
:Oracle Cloud: - Currency and conversion rate are now being handled correctly for non-USD costing for Oracle Cloud workloads :superscript:`5.4.9`
                - Fixed an issue that prevented |morpheus| Agent install for OCI Windows 2019 Instances unless the VM IP address was added to the WinRM port on the security group outbound rule :superscript:`5.4.9`
                - Updated the manner in which |morpheus| displays the number of CPU cores for Oracle Cloud workloads to better reflect the specifics of Oracle CPU count :superscript:`5.4.9`
:Plans and Pricing: - Fixed an issue that caused a random Service Plan to be accessed when users were attempting to edit an existing Virtual Image or VM Snapshot-type Service Plan :superscript:`5.4.10`
                  - Fixed unexpected behavior related to prices (comma vs period-separated decimals) when mixed browser locales were used :superscript:`5.4.10`
                  - When adding Price Sets to plans, it's no longer possible for very long Price Set text to overset the Edit Price Plan modal :superscript:`5.4.9`
                  - When deleting a Service Plan, Instances associated with that Plan will have their Plans automatically updated to a new one. Previously, under certain scenarios, the Plan association could remain tied to the now-deleted Plan :superscript:`5.4.9`
:Plugins: - Custom Catalog Plugins now have access to the "Dark Mode" themed versions of icon images :superscript:`5.4.9`
           - The search bar on the plugins list page now works correctly :superscript:`5.4.9`
           - When adding a new Plugin to |morpheus|, an info block tells the required plugin API version for the current version of |morpheus|. In some prior versions, the listed version was incorrect but this has been corrected
:Policies: - Cloud-scoped Delayed Delete and Delete Approval Policies now apply as expected to XaaS (Workflow-based) Instance Types :superscript:`5.4.9`
            - Fixed an issue that caused sequence numbers to be set incorrectly when used as part of a hostname policy :superscript:`5.4.10`
            - Fixed an issue that could cause Tagging Policies not to be applied if a Naming Policy did not also apply to the workload being provisioned :superscript:`5.4.9`
            - Fixed an issue that would rename hosts in clusters which were under a cluster naming policy if the host was later edited :superscript:`5.4.9`
            - When creating Backup Targets Policies, the new policy is no longer created with a null target selected which would prevent the new policy from being saved if it were not manually cleared
:Provisioning: - Fixed an issue that prevented Safari web browser users from setting a custom memory amount at provision time for Service Plans which allowed it :superscript:`5.4.9`
                - Fixed an issue that prevented hostnames from being set correctly if given in all caps and the Instance contained multiple VMs :superscript:`5.4.9`
                - Fixed an issue where |morpheus| Agent would fail to Install when workloads were provisioned to Clouds or Groups with apostrophe (') in the name :superscript:`5.4.10`
                - Fixed awkward line wraps that could appear in certain tabs of the Instance provisioning wizard :superscript:`5.4.9`
                - When provisioning fails due to an error in a Provision-phase Workflow Task, the Instance History tab now shows a fail icon (red "x" symbol) in the provision phase history rather than a green success check icon :superscript:`5.4.10`
:Puppet: - Fixed an issue that caused the Puppet agent not to be installed correctly on Windows workloads :superscript:`5.4.9`
          - Improvements made to Puppet integration, including validation added when creating the integration, Puppet Tasks showing in the Instance history tab, Puppet Tasks and Puppet provisioning now include a version picker, and more :superscript:`5.4.10`
:Reports: - Fixed a memory consumption issue caused when exporting very large reports (Operations > Reports) to CSV. It should now be safe to export very large reports :superscript:`5.4.9`
           - The instance type and layout for instances are now displayed in the instance cost report and export :superscript:`5.4.13`
           - Updated the UI description for the Virtual Machine Inventory report which was incorrect :superscript:`5.4.10`
:Roles: - When renaming Multitenant User Roles, the new Role name is now reflected in the Roles list on the User detail :superscript:`5.4.9`
:Security:  - Fixed an issue related to passwords being exposed in a specific log file :superscript:`5.4.10`
            - Fixed a potential command injection vulnerability related to Ansible integrations :superscript:`5.4.10`
            - Fixed an issue that allowed Primary Tenant users to view Subtenant Group information via |morpheus| API by modifying the request in a specific way :superscript:`5.4.9`
            - The Azure access token used is no longer written into |morpheus| logs during teardown-phase actions :superscript:`5.4.10`
            - The csrf token value is no longer being passed to the GET query call on the policies list and instance list pages :superscript:`5.4.13`
:ServiceNow: - Dependent required Inputs (those which become required based on the value of other Inputs) are now honored for Catalog Items shared with an integrated ServiceNow appliance
             - Fixed an issue that caused Naming Policy errors when provisioning Service Catalog items via ServiceNow integration :superscript:`5.4.9`
             - |morpheus| now updates the state of created ServiceNow RITMs when a provision approval policy holds up provisioning. After approval or denial, the state will change to "Closed Complete" or "Closed Incomplete" :superscript:`5.4.11`
:Settings: - Removed the "Default Appliance Locale" setting from the global settings (Administration > Settings) panel for Subtenants. This option was not meant to be exposed to Subtenants and only the Primary Tenant's setting applied to the appliance anyway :superscript:`5.4.9`
            - |morpheus| will now generate email successfully when global SMTP settings are configured for an SMTP server that requires no authentication credentials :superscript:`5.4.10`
:Storage: - Fixed an issue that prevented display of IOPs metrics on some server detail pages :superscript:`5.4.9`
:Tags: - General validation improvements made to tags, such as setting max tag name lengths based on specific cloud requirements and validating for disallowed characters :superscript:`5.4.11`
:Tenants: - Improvements added to the Tenant delete process which, under certain conditions, could become stuck due to SQL constraint issues :superscript:`5.4.9`
          - Fixed an issue that prevented deletion of Tenants if they had Archive buckets associated with them :superscript:`5.4.9`
:Terraform: - Additional actions (Edit Inputs and Edit State) have been added under the Actions Menu on Terraform App and Terraform Instance detail pages :superscript:`5.4.10`
            - Fixed a display issue that could cause individual VM components of a Terraform App (such as an EC2 Instance) to be labeled as a container rather than a VM :superscript:`5.4.9`
            - Fixed an issue that appeared to show Terraform Apply State functionality would make unwanted changes (such as to an Instance name) though the change would not actually be made :superscript:`5.4.10`
            - Fixed an issue that caused Cypher entries at the tfvar mount point not to show up correctly under the Profiles tab for the target Cloud :superscript:`5.4.11`
            - Fixed an issue that caused Terraform Apps created via imported state not to transition from a "deploying" to "running" state even after they were successfully provisioned :superscript:`5.4.12`
            - Fixed an issue that caused var files passed with a "-var-file" option not to be interpolated correctly :superscript:`5.4.10`
            - Fixed an issue that led to large Terraform Apps causing the web browser tab to consume large amounts of memory and crash :superscript:`5.4.12`
            - Fixed an issue that prevented saving edits to Terraform Spec Templates directly from the Spec Tab of a Terraform App Detail Page :superscript:`5.4.10`
            - Improved the handling of adding tags to VMs associated with Terraform Apps as previously the added tags would make the Apps always in a drift state :superscript:`5.4.11`
            - Removing a Spec Template from a new Terraform App Blueprint draft will no longer close the New App Blueprint modal entirely :superscript:`5.4.11`
            - Terraform App detail pages no longer return 404 errors during the early part of the provisioning process :superscript:`5.4.9`
:UI:  - An error is now surfaced when the user attempts to create a new Amazon Node Type without specifying an AMI :superscript:`5.4.10`
      - Filters set on the Backups List Page now hold when navigating to the next page of results :superscript:`5.4.10`
      - Fixed a typo in global settings (|AdmSet|) in the help block related to the Exchange URL field
      - Fixed a UI rendering issue on the edit modal for an existing identity source :superscript:`5.4.9`
      - Fixed an issue on the VMs list page (Infrastructure > Compute > Virtual Machines) that could cause the Power On/Off fly-out menu to be partially cut off :superscript:`5.4.9`
      - Fixed an issue that allowed the volumes information to overset the wizard window on the review tab of the New App Wizard :superscript:`5.4.10`
      - Fixed an issue that caused Input fields to overset the Service Catalog item box when its associated help block was very long :superscript:`5.4.9`
      - Fixed an issue that caused Input name labels to overlap each other on Service Catalog item pages if the label was very long :superscript:`5.4.9`
      - Fixed an issue that caused widgets on the Instances list page to display incorrect Instance counts or incorrect running/stopped Instance counts :superscript:`5.4.10`
      - Fixed an issue that could cause text on the Instance Provisioning wizard Review tab to overset the menu window :superscript:`5.4.9`
      - Fixed an issue that hid the IP addresses from the Instance detail page when viewed at narrow (mobile) widths :superscript:`5.4.9`
      - Minor spelling and spacing cleanup on title bars of some integration types :superscript:`5.4.9`
      - Search bars in |morpheus| (Instance list, server list, etc.) will now search properly on numerals entered as search terms :superscript:`5.4.9`
      - The filters in the Type dropdown on the Backups List Page are now sorted in alphabetical order to make them easier to find :superscript:`5.4.10`
      - Updated help block text for Tenant Visibility settings to more accurately reflect the current functionality of Visibility settings :superscript:`5.4.9`
:Users: - Fixed an issue that prevented deleting a user which had created a credential (Infrastructure > Trust) :superscript:`5.4.9`
        - Fixed an issue that stopped CSV exports of Users and User Group lists from executing correctly :superscript:`5.4.11`
         - When creating new |morpheus| users, a dash (-) is now counted as a symbol for purposes of password complexity :superscript:`5.4.11`
:VMware: - Fixed a sync error that would occur when updating a VMware Cloud to scope it to a different Resource Pool :superscript:`5.4.13`
          - Fixed an issue that could cause VMware VMs to fail to boot when using multiple disks and Cloud-init :superscript:`5.4.9`
          - Fixed an issue that could cause snapshots not to be cleaned up after execution of clone process on VMware Clouds :superscript:`5.4.9`
          - VMware Clouds scoped to a specific Resource Pool will now only inventory VMs from that Resource Pool and will only display that Resource Pool in the Resources section :superscript:`5.4.11`
          - When deleting VMs in a disconnected or not responding state, |morpheus| no longer reports them deleted until the deleted state can be confirmed on the Cloud backend :superscript:`5.4.9`
:Virtual Images: - Fixed an issue that cleared manual configurations set in |morpheus| on Virtual Images synced from VMware Content Library after the next Cloud sync :superscript:`5.4.9`
                  - Fixed an issue that could cause failures when uploading Virtual Images via |morpheus| CLI when the same image could be uploaded fine via |morpheus| UI :superscript:`5.4.9`
:Workflows: - Workflows which are attached to Layouts will now be invoked for workloads which are converted from discovered to |morpheus|-managed Instances :superscript:`5.4.13`
:vCloud Director: - Datastores now sync in correctly when vCD Clouds are integrated using the System Admin user :superscript:`5.4.9`
                  - Fixed an issue that prevented the provisioning of library items based on uploaded OVFs which include NVRAM files :superscript:`5.4.10`

Appliance & Agent Updates
=========================

:Appliance: - Appliance, Node & VM Node Package Java updated to 11.0.17.8 :superscript:`5.4.13`
             - Elasticsearch Java updated to 17.0.5.8 :superscript:`5.4.13`
             - Fixed an issue that caused SeedService errors to appear in the logs on appliance start up
             - Fixed an issue that led to appliance start-up failures when ENC and suffixes were used with an external database :superscript:`5.4.13`
             - Fixed seedService warnings that would appear in logs during startup of a new |morpheus| appliance :superscript:`5.4.9`
             - |morpheus| Node & VM Node packages updated to v3.2.10. Note: Due to build java requiremnets, the i386.deb and i386.rpm (32-bit) VM Node Packages will can longer be updated, and remain on v3.2.9.
             - RHEL 9 is now supported for |morpheus| appliance installation
             - Tomcat-embed-core version upgraded to 9.0.58 (CVE-2022-23181) :superscript:`5.4.9`
             - Updated |morpheus| installer for SUSE 15 SP 2 and 3 to automate some manual steps that were previously required, including uuid-devel repo access and a second reconfigure step :superscript:`5.4.13`
             - |morpheus| installer and reconfigure action will now ignore missing susefirewall2 in SLES15 as it has been deprecated. Previously, workarounds were require
