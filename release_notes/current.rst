.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade versions: Rolling: |minRollingUpgradeVer| Non-rolling: |minUpgradeVer|

.. .. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - The Group attribute for Network Pools can now be updated via |morpheus| API and CLI. This functionality is also added to |morpheus| UI in this release
:Catalog: - Catalog item names now truncate after wrapping to a second line rather than at the end of the first line which often cut off too much of longer names
:Docker: - When running a non-Kubernetes Docker image with image tag set to latest, we now force-pull the image to update the Docker host
:Kubernetes: - Added default Kubernetes MKS 1.30 Layouts for all supported Clouds
:Library: - Added or updated Oracle Linux 6, 7, 8 and 9 images for various Cloud types to the default catalog
           - Default Ubuntu 24.04 images have been added for VMware, Azure, AWS, and MVM/KVM Clouds
:Load Balancers: - |morpheus| IP Pools can now be used to auto-assign an IP address for the VIP address field when creating a load balancer Instance
:NSX: - NSX and NSX Cloud now support a configured global proxy
:Network: - Network Domains can now be scoped to a specific Group. Additionally, the "Network: Domains" Role permission now has a Group access level which limits Domain visibility only to those scoped to accessible Groups
           - Network Pools can now be scoped to a specific Group. Additionally, the "Network: IP Pools" Role permission now has a Group access level which limits Network Pool visibility only to those scoped to accessible Groups
:Nutanix Prism Central: - Improved handling of unmanaged VLAN networks. Managed and unmanaged VLANs are no longer synced as the same network type
:Nutanix Prism Element: - References to "Nutanix Prism" integration have been updated to "Nutanix Prism Element" to differentiate from "Nutanix Prism Central"
:vCloud Director: - vCD Clouds can now be authenticated through API tokens in addition to username/password authentication
                  - vCD Clouds will now sync in Plans created in vCD, allow users to select these plans at provision time, and allow access to reconfigure and costing features when custom plans are utilized


Fixes
=====

:API & CLI: - Tenant permissions for NSX integrations can now be set via |morpheus| API
             - When listing Roles via |morpheus| API and filtering to include only Tenant Roles, the response will no longer include the built-in System Admin Role which is not selectable as a Tenant Role
:Amazon: - Creating AWS Clouds utilizing assume role and an external ID will now authenticate correctly
          - db.r7g plans are now available when provisioning RDS Instances
:Ansible Tower: - When Ansible Tower integrations are updated with invalid credentials, the integration cannot be saved and both UI and log errors are thrown
:Apps: - Fixed Layouts not properly being filtered out based on Group selection when provisioning Apps in the App Wizard
        - Selecting Instances when creating Apps is now done by their display names (if set) rather than their names
:Azure: - Prices and Price Sets are now syncing properly for EA account types
:Bluecat: - Restored support for quick deploy in the Bluecat plugin once again
:Catalog: - Fixed UI validation errors on catalog order forms indicating on the wrong field rather than correctly identifying the field which had incorrect data type or format
           - Fixed an issue that could cause 500 errors to be thrown when viewing the detail page for some service catalog items
           - Fixed an issue where viewing the order page for an ARM blueprint catalog item would throw a 500 error
           - Some longer Input labels will no longer wrap awkwardly on the catalog item order page
           - The catalog now uses the same logo icon in both the Standard and the Service Catalog Personas
:CyberArk Conjur: - CyberArk Conjur integrations now properly honor configured global proxies and ``no_proxy`` setting
:Email Notifications: - Fixed password update success email being sent when the account settings update success email should have been sent
                  - Password reset email no longer fails to send when whitelabeling is turned on and custom terms of service text has been entered
:Forms: - Fixed datastore selection field not appearing when the default Cloud on the Form doesn't match the Cloud selected at the time of creating the catalog item
         - Fixed multiple issues related to File Content-type Inputs on Forms, including Repository sourcing crashing the Form builder and the content area being too small for locally-sourced file content
         - Fixed tag-type Inputs on Forms not retrieving the key value for any applicable Tag Policies
         - For Disk-type Inputs on Forms, fixed ADD VOLUMES and CUSTOMIZE EXTRA VOLUMES configurations not being honored on the catalog item order page
         - Layout-type Inputs on Forms are now properly filtered based on Group Input selection
         - The Form creation modal will no longer crash and close when Key/Value-type inputs are added with default value JSON entered
         - The description field for Forms is now limited to 256 characters
         - When using the Resource Pool-type Input on Forms, the full hierarchy for the resource pool is now displayed (as it is in the Instance wizard) rather than just the lowest level node which could make it unclear which Resource Pool is being selected
:Google Cloud: - Fixed errors related to integrating GCP Clouds through a proxy requiring authentication
:Import/Export: - Fixed Workflow-type Catalog Items not importing successfully into new environments
:Instances: - Instance status is no longer switched to "Running" when the |morpheus| Agent is rebooted during post-provisioning
             - The "Suspend" button is now hidden from the ACTIONS menu when users do not have permission to update workload power state
             - When force deleting Instances from the Instances list page, the delete modal now includes the warning that infrastructure may need to be manually deleted from the target cloud. Deleting Instances from their detail pages already showed this warning
:Kubernetes: - When provisioning the default Kubernetes Instance Type to Amazon Clouds, the list of Plans is now populated
:MVM: - Fixed a bug which prevented Instances from being provisioned successfully to an MVM cluster if the Instance name contained a whitespace character (" ")
:NSX: - For NSX ALBs we are now correctly setting the VIP address and showing appropriate errors if the address is invalid or missing
:Network: - For networks whose network type is configured to not be deletable, we now hide the delete button in all areas of the UI
:Nutanix Prism Central: - Fixed ISOs not ejecting consistently following provisioning of Nutanix Prism Central Instances
                  - Fixed power status on Instances displaying as "Unknown" when the Cloud scope was updated (Project scope changed)
:Option Lists: - Option Lists items with a value of "0" are now selectable
:Packages: - Fixed packages needing to be added a second time in order for Task and Workflows to be successfully added
            - Fixed packages needing to be added a second time in order to properly associate uploaded Form resources with uploaded catalog item resources
            - The Packages list page (|AdmIntPac|) will now page when more than 25 packages have been added to |morpheus|
:Plans and Pricing: - Fixed an intermittent issue where changing Service Plans on the Instance Provisioning Wizard could cause the configured root disk size to spontaneously change
                  - Updating Prices via |morpheus| API no longer ``incurCharges`` or ``markupType`` values if they aren't included in the payload
:PowerShell: - Fixed an issue that caused very large PowerShell scripts with USING statements to fail
:Tenants: - It's no longer possible to disable the |mastertenant| through |morpheus| UI, API or CLI
:VMware: - Fixed image upload timeout that could occur when provisioning large multi-VMDK images
          - Made network sync calls more efficient to improve network sync performance in environments with many networks
:vCloud Director: - When vCloud Director-type Clouds are configured with a manually-entered API version, |morpheus| disables calls used to auto-detect the API version in the event this endpoint has been disabled by the user


Appliance & Agent Updates
=========================

:Appliance: - Embedded Tomcat upgraded to 9.0.90
