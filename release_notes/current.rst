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
- 7.0.6-2 September 16 2024

7.0.6-2 Updates
===============

:Provisioning: - Windows: Fixed issue with network wait status when image configuration should skip network wait
:MVM: - Fixed issue with vm's being created with file-backed memory configuration
      - Fixed ssh key race condition for non-hci mvm hosts
      - Increased morpheus agent jvm mxm to 256MB for mvm and kvm host type


New Features
============

:API & CLI: - Added API and CLI support for MVM actions placing a host in maintenance mode, removing a host from maintenance mode, and updating VM placement on hosts. These changes have been added to API and CLI documentation
             - Updated the |morpheus| API documentation to note that you can add a ``zoneId`` query parameter to a call to the endpoint to get all networks to filter the results
:Activity: - The Activity page (|OpeAct|) now shows the user who took the indicated action for a greater number of possible activities that can appear on the page
:Catalog: - Disabled default Ubuntu 14.04 Layouts as end of life has been reached
:Forms: - For Forms Inputs, when configuring a "Visibility Field," a new option will appear to "Keep Default Value on Show." When checked, an Input will have its default value loaded when its visibility is triggered on
:Plugins: - Added a new plugin type for creating custom Guidance recommendations. See developer.morpheusdata.com for more details
           - Added support for OLVM (Oracle Linux Virtualization Manager) Cloud types by adding the official plugin from share.morpheusdata.com
:XenServer: - New VHD image files can now be uploaded to XCP via |morpheus|


Fixes
=====

:API & CLI: - Fixed a missing ``ipMode`` flag from the payload generated when adding Instances from |morpheus| CLI so that static IP addresses can be assigned
             - Fixed the underlying payload generated with the ``morpheus clusters add`` command which could be incorrectly formed in some scenarios
             - The ``destinationPortRange`` parameter is now available when reading, adding or updating Security Group rules via |morpheus| API
:Alibaba: - Fixed provisioning failures to Alibaba Cloud targets when Cloud, Cloud SSD, or Ultra Cloud disk types were selected
:Catalog: - Fixed Input help text alignment which, in some cases, could be aligned out to the far left of the window rather than directly under the field
           - Fixed an issue that could cause the "order again" function for Catalog Items not to work correctly if Inputs on the original order were injecting an array of custom values
           - Fixed datastore details not updating when toggling one VMware Cloud to another on the Catalog order page
           - When building Instance-type Catalog Items from an Instance Type containing more than one Layout, the version number from the selected Layout now appears in the Instance JSON map rather than the version of the first Layout :superscript:` 7.2.0`
:Code: - Whitelabeling is now shown correctly on code repository detail pages (|ProCodRep|) if enabled
:Contacts: - Web Hook-type Contacts can now accept a URL value greater than 255 characters
:Costing: - Fixed prices on the Cloud Price Comparison flyout (seen when clicking the small dollar sign icon) on the Configure tab of the Instance Provisioning wizard not updating when a different storage volume type is selected (ex. Amazon GP2 vs GP3)
:Forms: - Default values for Byte-type Inputs now compute and display a MB/GB value rather than MiB/GiB
         - Fixed Number-type Inputs failing validation (too large/small) when no value is entered and the Input is not required
         - Fixed a require dependency not correctly applying to Instances-type Inputs
         - Fixed the drag-and-drop code syntax feature for Inputs created in the Form builder and utilized in Catalog Items to account for proper syntax when Input Field Names contain a hyphen ("-")
         - Fixed |morpheus| API-sourced Option Lists not loading on Forms when Plugin-sourced Cloud types are selected
         - Typing a parenthesis ("(") into the visibility, required or dependent field targeting a Checkbox-type Input will no longer crash the Form builder
         - When Form-based Catalog Items are shared with Subtenants, the Form no longer attempts to set the first Group (from the list in the |mastertenant| as the default Group selection which led to errors
:Google Cloud: - Worker nodes for provisioned GKE clusters no longer fail to appear on the cluster details when inventory is turned off on the Cloud
:Hosts: - Change Cloud functionality for VM records now properly updates the associated Resource Pool
         - If a delete action on a VM fails, the user-entered "DELETE" confirmation text is now cleared and must be re-entered on the subsequent delete attempts
:Inputs: - Added additional validation on Field Names for Inputs to ensure users do not select field names which may cause errors
          - Fixed a situation where custom Inputs might not evaluate properly in Instance JSON when the key in the JSON map matched the Input Field Name value
          - Improved logic for "Require Field" and "Visibility Field" configurations to correct some edge cases where they did not work properly
          - Input validation messages surfaced in the UI have been updated to correct minor grammatical inaccuracies
          - Inputs with a colon (":") in the field name value are now properly added into the list of custom options and can pass validation when the Input is required
          - It's now possible to use "0" as the first character of a number or text-type Input on a Catalog form
:Instances: - It's no longer possible to reconfigure an Instance or server and accidentally set the network to the "Select Network" list placeholder
:Kubernetes: - Custom Layouts for Kubernetes without "mks" in the name will fail kubectl commands run on the cluster detail page
              - When selecting External Kubernetes Layouts, the Layouts are now listed in a logical numerical order
:Library: - Setting an Instance Type Code value to "0" no longer sets that Instance Type as a default filter on certain pages (such as the Instances list page)
:MVM: - Configuring a bad NFS datastore no longer takes the entire cluster offline
:OpenStack: - Converting discovered OpenStack servers to managed without selecting an Instance Type will no longer prevent Instance logs from appearing on the Monitoring tab of the Instance detail
             - If the scoped Project is changed on the Cloud, the previously synced floating IP records which don't belong to the new Project are now removed on the next Cloud sync
:Oracle Cloud: - Oracle Cloud integrations can now show over 100 Compartments when present for scoping
:Plugins: - Text area-type Inputs can now be added to custom Task plugins
:Policies: - Cloud-scoped and "User Configurable" naming Policies set in the |mastertenant| are now resolving the Instance name properly on the Review tab of the Instance provisioning wizard within a Subtenant
            - Fixed an issue that caused incorrect application of naming policies when overlapping scopes were involved
:Security: - Fixed a potential XSS vulnerability related to Virtual Images
            - Update ``apache-httpclient`` to version 4.5.14 to mitigate CVE-2020-15250
:Settings: - Added a help text and validation for the "No Proxy" list under Proxy Settings in global appliance settings (|AdmSetApp|)
:Tasks: - After removing an Ansible Tower integration and causing a new integration to be associated with an Ansible Tower Job-type Task, changes (such as inventory or job template) are now properly picked up by the Task
         - Custom inputs are now available to Tasks in the Pricing phase of Provisioning Workflows
         - Fixed an issue that caused failures with HTTP-type Tasks when "Ignore SSL Errors" was unchecked
         - On-demand executions of Tasks and Workflows targeting the "Instance Label" are now working as designed
:Tenants: - Tenants are no longer prevented from being deleted when they have a record in the ``execute_schedule_type`` database table
:UI: - Improved the process for purging ``process_event`` database table entries to prevent database issues caused by large deletes. Note that this change adds and index so users with large ``process_event`` tables may notice a slight delay during upgrade
:Veeam: - Retention days on Veeam jobs cloned by |morpheus| are now equal to the retention days on the original job cloned from :superscript:` 7.2.0`
:XenServer: - The Log Folder, Config Folder, and Deploy Folder configuration fields are now working correctly for XenServer Node Types
:vCloud Director: - Fixed "Skip Agent Install" flag on the provisioning wizard being ignored



Appliance & Agent Updates
=========================

:Agent Node Packages: - |morpheus| linux agent updated to v2.8.0
                      - |morpheus| node & vm node packages updated to v3.2.27 with linux agent v2.8.0
:Embedded Plugins: - bigip-plugin updated to v1.3.5
                   - XCP-ng plugin updated to v1.0.2