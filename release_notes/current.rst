.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:Administration: - Improved CEF audit logging for situations when a user is being impersonated :superscript:`7.0.2`
:Amazon: - Added support for new reserved keywords in RDS MySQL 3.06.0 :superscript:`7.0.2`
:Clouds: - Users must now type "DELETE" into a text field to confirm they wish to delete a Cloud which is a safeguard already available on other resources in Morpheus :superscript:`7.0.2`
:License: - Updated wording on the license application page (|AdmSetLic|) to reflect updated licensing policies :superscript:`7.0.2`
:MicrosoftDNS: - Major improvements added to the MicrosoftDNS plugin. See updated MSDNS integration documentation for further details :superscript:`7.0.2`
:Nutanix Prism Central: - Added a "Windows Defender Credential Guard" checkbox when "Secure Boot" is also checked which mirrors functionality available in NPC :superscript:`7.0.2`
                  - Added support for Nutanix Prism Central Projects. Clouds can be scoped to a specific project or Instances can be provisioned to specific projects :superscript:`7.0.2`
:Oracle Cloud: - Added ``mx-queretaro-1`` region support for Oracle Clouds :superscript:`7.0.2`
:Reports: - Removed the Invoice Details report :superscript:`7.0.2`
:Security: - Embedded Apache Tomcat upgraded to 9.0.88 to mitigate CVE-2024-23672 :superscript:`7.0.2`
            - Upgraded ``jose4j`` to 0.9.4 to mitigate CVE-2.23-51775
            - Upgraded ``netty-codec-http`` to 4.1.108.Final to mitigate CVE-2024-29025
:Tenants: - The impersonate option for a user with "Password Expired" checked, is no longer active. Previously when click the user would be directed back to the Dashboard page of the |mastertenant| which was confusing :superscript:`7.0.2`


Fixes
=====

:API & CLI: - The ``https://<morpheusUrl>/api/zones/<id>/security-groups`` endpoint now properly returns the expected Security Groups :superscript:`7.0.2`
             - When running a Workflow on a host via API, a ``processId`` is now returned along with the success boolean so that the execution history may also be tracked via API if desired :superscript:`7.0.2`
:Amazon: - Fixed AWS Clouds getting stuck in the "Initializing" status prior to initial sync on creation of the Cloud in specific scenarios :superscript:`7.0.2`
          - Fixed AWS prices not syncing for Clouds scoped to the Osaka region :superscript:`7.0.2`
          - Fixed Amazon EKS controller subnet filtering which was not properly filtering the list based on the selected VPC :superscript:`7.0.2`
          - Fixed Amazon EKS role filtering in the provisioning wizard for EKS clusters. Roles are no longer duplicated for each region which was not necessary :superscript:`7.0.2`
          - When unable to properly authenticate with a Role ARN, the cloud will not be added using the root account instead. An error appears now appear confirming the connection to AWS cannot be made :superscript:`7.0.2`
:Archives: - Within an Archive, on the scripts tab of a file detail page, fixed an HTML ``<a>`` tag which was being shown as visible text copy on the page :superscript:`7.0.2`
:Azure: - Azure VMs which are discovered by |morpheus| and converted to managed Instances, now correctly update on the server detail page to show they are managed rather than unmanaged :superscript:`7.0.2`
         - Fixed an issue causing Italy North-region Plans not syncing to |morpheus| :superscript:`7.0.2`
         - Fixed public IP addresses not syncing when provisioning to Azure Clouds using an API proxy :superscript:`7.0.2`
:Backups: - When deleting a backups integration, users will no longer see a flash stating "No status message declared" :superscript:`7.0.2`
:Blueprints: - Morpheus-type App Blueprints now have access to variables from any TFVars Secret configuration present on the Layouts :superscript:`7.0.2`
:Budgets: - Improved the logic for computed actual costs in the Budget UI to ensure they were in line with the Cloud costs history :superscript:`7.0.2`
:Catalog: - Fixed Catalog Item order page not displaying App validation errors which prevented ordering without informing the reason to the user :superscript:`7.0.2`
           - Inputs on Instance Type Catalog Items contain Instance and Instance Type information once again to maintain compatibility with previously written translation scripts :superscript:`7.0.2`
:Clouds: - When adding a new Cloud in the |mastertenant| and selecting a Tenant (other than the |mastertenant|) for "Visibility" purposes, the Visibility configuration is automatically saved as "Private" even if left with the default "Public" configuration :superscript:`7.0.2`
          - When creating or editing Clouds or Groups to have the same name as existing resources, the record is not saved and a friendly UI warning is shown to indicate the name must be unique :superscript:`7.0.2`
:Costing: - Fixed usage records not being re-created after a hot-resize which didn't require the workload to be restarted :superscript:`7.0.2`
           - Improved "Costs this Month" totals on the Clouds list page which in certain cases could be off due to currency conversions :superscript:`7.0.2`
           - In the Services Breakdown section of the Costing tab of an AWS Cloud detail page, there will no longer be unlabeled categories of services :superscript:`7.0.2`
:Dashboard: - Fixed an issue that caused workloads converted to managed Instances via API to be categorized under "none" Cloud type on |morpheus| dashboard :superscript:`7.0.2`
:Forms: - Default values for Disks fields on Forms will now load properly when the field visibility is dependent on another field :superscript:`7.0.2`
         - Fixed Virtual Image fields not populating when creating Form-based Catalog Items for Nutanix Prism Central provisioning :superscript:`7.0.2`
         - Fixed an issue that caused configured defaults for disk sizes on Forms to be computed and displayed incorrectly :superscript:`7.0.2`
:Hosts: - Added validation improvements to Change Cloud functionality to prevent cases of moving workloads to improper places :superscript:`7.0.2`
:Hub: - Fixed an issue where |morpheus| Hub would not be updated with a new license being used by an appliance if Hub were unavailable or some other network issue prevented the Hub update at the moment the new license was applied :superscript:`7.0.2`
:Instances: - When an Instance is provisioned to a Cloud and the Cloud is removed from the Group configured at Instance provision time, the Instance detail page will no longer fail to open with an "Instance not found" UI warning :superscript:`7.0.2`
:Integrations: - Added helper text "Warning! Using HTTP URLS are insecure and not recommended." on integration modals which lacked it :superscript:`7.0.2`
:Jobs: - The targets list on a Jobs detail page (|ProJob| > Selected Job) now updates with the live status of the Instance targets rather than displaying a cached status :superscript:`7.0.2`
:Kubernetes: - When provisioning Kubernetes clusters to Clouds with associated Workflow Policies, the Platform configuration on the Workflows will now be properly used to avoid running Windows Workflows against Linux workloads (and vice versa) :superscript:`7.0.2`
:MicrosoftDNS: - Unchecking the "Inventory Existing" box on a MSDNS integration now sets the associated attribute to ``off`` rather than ``null`` :superscript:`7.0.2`
:NSX: - Tenants are now able to be deleted if they had NSX network groups associated with them :superscript:`7.0.2`
:Network: - Improved Cloud-init network config syntax and nameserver configuration under specific conditions when utilizing networks with IPv4 and IPv6 enabled along with IP Pools and DNS configured for IPv4 and IPv6 :superscript:`7.0.2`
:Nutanix Prism Central: - Fixed ``HostSync`` and ``SyncTask`` errors in logs when syncing Nutanix Prism Central Clouds :superscript:`7.0.2`
                  - Fixed an issue that left images deleted from Nutanix Prism Central remaining with |morpheus| and using storage unnecessarily :superscript:`7.0.2`
                  - Fixed images not uploading from NFS storage to integrated Nutanix Prism Central Clouds :superscript:`7.0.2`
                  - Fixed intermittent errors (``error executing query``) in logs coming from Nutanix Prism Central integrations :superscript:`7.0.2`
                  - Fixed the hypervisor console not working on subsequent attempts to access it, only working the first time :superscript:`7.0.2`
                  - Saving edits to synced images in airgapped environments no longer fails with 500 errors :superscript:`7.0.2`
:Nutanix: - Fixed an issue that caused provisioning failure when an NFS file share was used as the image repository on a |morpheus| appliance :superscript:`7.0.2`
:Proxies: - Updated several internally-developed plugins to honor the "No Proxy" configuration when present :superscript:`7.0.2`
:Roles: - Users in Roles with "Read" permission on Clouds will no longer be allowed to manually trigger a refresh the Cloud, which brings UI behavior in line with API behavior :superscript:`7.0.2`
         - When viewing user permissions for a currently logged in user which has only the built-in System Admin Role, the Cypher feature permission level is now properly shown as "Full Decrypted" :superscript:`7.0.2`
:Security: - Fixed a bug that allowed delete confirmation modals requiring the user to type "DELETE" to be bypassed without typing the required word which could lead to unintended deletions :superscript:`7.0.2`
            - Improved the CyberArk plugin to prevent what could be considered a sensitive information disclosure in stacktrace error messages :superscript:`7.0.2`
:Tasks: - Powershell Tasks are now run in 64-bit rather than 32-bit :superscript:`7.0.2`
:Tenants: - We now gracefully handle situations where previously a workload could not be assigned from the |mastertenant| to another Tenant if there was a currently-existing workload with the same name :superscript:`7.0.2`
:Terraform: - After deploying a Terraform App, renaming any ``.tf`` files in the repository will no longer cause problems for future attempts to apply state :superscript:`7.0.2`
             - Fixed Terraform Instances and Apps bypassing Approve Delete Policies which allowed them to be deleted without approval :superscript:`7.0.2`
:Trust: - Added UI validation when adding SSH keypairs in the Trust section (|InfTru|) to make it clearer to the user when an invalid keypair has been entered :superscript:`7.0.2`
         - When attempting to remove a keypair which is already linked to another resource (integration, etc.), there is now a clearer UI warning to indicate why the keypair cannot be deleted :superscript:`7.0.2`
:VMware: - Fixed an issue that could cause orphaned VMware-related records to pile up in the database and create performance issues :superscript:`7.0.2`
          - Fixed issue where using the "Order Again" button in Catalog would provision the new VM into the root vCenter folder rather than the folder selected for the original VM ordered :superscript:`7.0.2`
          - Instances which were powered off will no longer appear in a running state in |morpheus| following a reconfigure (though they were always still off in VMware) :superscript:`7.0.2`
:Virtual Images: - Creating a new Virtual Image sourced by URL will now go through any configured global proxies :superscript:`7.0.2`
                  - The filter "VMware (vmdk/ovf/ova)" now includes images synced from vCloud Director :superscript:`7.0.2`


Appliance & Agent Updates
=========================

:Appliance: - Added a configuration in ``morpheus.rb`` to enable the ipv6 listener for Nginx with ``nginx['listen_ipv6'] = true`` (note: IPv6 will be added to ``morpheus.conf`` and ``morpheus-ssl.conf`` listeners if any value is set in morpheus.rb other than ``nil``, including "off" or false) :superscript:`7.0.2`
:Database: - External mysql service: Added support for Appliance using Amazon Aurora RDS MySQL version 3.06.0+ :superscript:`7.0.2`
