.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:Administration: - Improved CEF audit logging for situations when a user is being impersonated :superscript:`6.2.10`
:Amazon: - Added support for new reserved keywords in RDS MySQL 3.06.0 :superscript:`6.2.10`
:Budgets: - Budgets now include the option to choose from one of two data forecasting models to estimate out the budget through the end of its configured term
:Clouds: - Added more granular controls around automatic Cloud inventory. Depending on Cloud feature capability, set the default active or inactive state for Plans, Networks, Security Groups, Datastores, Folders, and more
          - Users must now type "DELETE" into a text field to confirm they wish to delete a Cloud which is a safeguard already available on other resources in Morpheus :superscript:`6.2.10`
:Email Notifications: - Added "Email Templates" tab to the global settings section (|AdmSet|). Create new templates to replace the system default templates for notifications such as Instance provisioning completion, password reset, policy warnings, and much more
:Jobs: - Jobs can now be configured to only run on workloads with an on or an off power state (or keep the default behavior of running with any power state)
:License: - Updated wording on the license application page (|AdmSetLic|) to reflect updated licensing policies :superscript:`6.2.10`
:MicrosoftDNS: - Major improvements added to the MicrosoftDNS plugin. See updated MSDNS integration documentation for further details :superscript:`6.2.10`
:Nutanix Prism Central: - Added a "Windows Defender Credential Guard" checkbox when "Secure Boot" is also checked which mirrors functionality available in NPC :superscript:`6.2.10`
                  - Added support for Nutanix Prism Central Projects. Clouds can be scoped to a specific project or Instances can be provisioned to specific projects :superscript:`6.2.10`
:Oracle Cloud: - Added ``mx-queretaro-1`` region support for Oracle Clouds :superscript:`6.2.10`
:Personas: - Added a new API Persona. This allows service accounts to be configured for API use which have no |morpheus| UI access
:Reports: - For scheduled reports, added a link to include a comma-separated list of email addresses which should be notified each time the report is run
           - Removed the Invoice Details report :superscript:`6.2.10`
           - Updated the Time Series Cost report with improved Group filtering and sort ordering
:Security: - Embedded Apache Tomcat upgraded to 9.0.88 to mitigate CVE-2024-23672 :superscript:`6.2.10`
:Tasks: - For Powershell Tasks, added a Powershell version configuration to run the Task in a specified version of Powershell. The selected version must be installed on the targer for this to function correctly
:Tenants: - The impersonate option for a user with "Password Expired" checked, is no longer active. Previously when click the user would be directed back to the Dashboard page of the |mastertenant| which was confusing :superscript:`6.2.10`
:VMware: - Added SR-IOV network adapter support
:Virtual Images: - In the Locations section of a Virtual Image detail page, the "CLOUD" column has been relabeled to "REFERENCE" as the source can be a Cluster or a Cloud
                  - Virtual Image types are no longer a static list but can be dynamically added to an appliance based on integrated Cloud types


Fixes
=====

:API & CLI: - The ``https://<morpheusUrl>/api/zones/<id>/security-groups`` endpoint now properly returns the expected Security Groups :superscript:`6.2.10`
             - When running a Workflow on a host via API, a ``processId`` is now returned along with the success boolean so that the execution history may also be tracked via API if desired :superscript:`6.2.10`
:Amazon: - Fixed AWS Clouds getting stuck in the "Initializing" status prior to initial sync on creation of the Cloud in specific scenarios :superscript:`6.2.10`
          - Fixed AWS prices not syncing for Clouds scoped to the Osaka region :superscript:`6.2.10`
          - Fixed Amazon EKS controller subnet filtering which was not properly filtering the list based on the selected VPC :superscript:`6.2.10`
          - Fixed Amazon EKS role filtering in the provisioning wizard for EKS clusters. Roles are no longer duplicated for each region which was not necessary :superscript:`6.2.10`
          - When unable to properly authenticate with a Role ARN, the cloud will not be added using the root account instead. An error appears now appear confirming the connection to AWS cannot be made :superscript:`6.2.10`
:Archives: - Within an Archive, on the scripts tab of a file detail page, fixed an HTML ``<a>`` tag which was being shown as visible text copy on the page :superscript:`6.2.10`
:Azure: - Azure VMs which are discovered by |morpheus| and converted to managed Instances, now correctly update on the server detail page to show they are managed rather than unmanaged :superscript:`6.2.10`
         - Fixed an issue causing Italy North-region Plans not syncing to |morpheus| :superscript:`6.2.10`
         - Fixed public IP addresses not syncing when provisioning to Azure Clouds using an API proxy :superscript:`6.2.10`
:Backups: - When deleting a backups integration, users will no longer see a flash stating "No status message declared" :superscript:`6.2.10`
:Blueprints: - Morpheus-type App Blueprints now have access to variables from any TFVars Secret configuration present on the Layouts :superscript:`6.2.10`
:Budgets: - Improved the logic for computed actual costs in the Budget UI to ensure they were in line with the Cloud costs history :superscript:`6.2.10`
:Catalog: - Fixed Catalog Item order page not displaying App validation errors which prevented ordering without informing the reason to the user :superscript:`6.2.10`
           - Inputs on Instance Type Catalog Items contain Instance and Instance Type information once again to maintain compatibility with previously written translation scripts :superscript:`6.2.10`
:Clouds: - When adding a new Cloud in the |mastertenant| and selecting a Tenant (other than the |mastertenant|) for "Visibility" purposes, the Visibility configuration is automatically saved as "Private" even if left with the default "Public" configuration :superscript:`6.2.10`
          - When creating or editing Clouds or Groups to have the same name as existing resources, the record is not saved and a friendly UI warning is shown to indicate the name must be unique :superscript:`6.2.10`
:Clusters: - When a Teardown-phase Task fails, the Cluster no longer continues on to be deleted allowing the user to correct the issue so Teardown-phase Tasks are run successfully prior to deleting
:Costing: - Fixed usage records not being re-created after a hot-resize which didn't require the workload to be restarted :superscript:`6.2.10`
           - Improved "Costs this Month" totals on the Clouds list page which in certain cases could be off due to currency conversions :superscript:`6.2.10`
           - In the Services Breakdown section of the Costing tab of an AWS Cloud detail page, there will no longer be unlabeled categories of services :superscript:`6.2.10`
:Dashboard: - Fixed an issue that caused workloads converted to managed Instances via API to be categorized under "none" Cloud type on |morpheus| dashboard :superscript:`6.2.10`
:DigitalOcean: - When DigitalOcean Clouds are scoped to a specific VPC, newly provisioned clusters are now provisioned to that VPC rather than default VPC for the datacenter
                - When DigitalOcean Clouds are scoped to a specific VPC, the App provisioning wizard no longer presents the user with a VPC configuration selection
:Forms: - Default values for Disks fields on Forms will now load properly when the field visibility is dependent on another field :superscript:`6.2.10`
         - Fixed Virtual Image fields not populating when creating Form-based Catalog Items for Nutanix Prism Central provisioning :superscript:`6.2.10`
         - Fixed an issue that caused configured defaults for disk sizes on Forms to be computed and displayed incorrectly :superscript:`6.2.10`
:Hosts: - Added validation improvements to Change Cloud functionality to prevent cases of moving workloads to improper places :superscript:`6.2.10`
:Hub: - Fixed an issue where |morpheus| Hub would not be updated with a new license being used by an appliance if Hub were unavailable or some other network issue prevented the Hub update at the moment the new license was applied :superscript:`6.2.10`
:Instances: - When an Instance is provisioned to a Cloud and the Cloud is removed from the Group configured at Instance provision time, the Instance detail page will no longer fail to open with an "Instance not found" UI warning :superscript:`6.2.10`
:Integrations: - Added helper text "Warning! Using HTTP URLS are insecure and not recommended." on integration modals which lacked it :superscript:`6.2.10`
:Jobs: - The targets list on a Jobs detail page (|ProJob| > Selected Job) now updates with the live status of the Instance targets rather than displaying a cached status :superscript:`6.2.10`
:Kubernetes: - When provisioning Kubernetes clusters to Clouds with associated Workflow Policies, the Platform configuration on the Workflows will now be properly used to avoid running Windows Workflows against Linux workloads (and vice versa) :superscript:`6.2.10`
:MicrosoftDNS: - Unchecking the "Inventory Existing" box on a MSDNS integration now sets the associated attribute to ``off`` rather than ``null`` :superscript:`6.2.10`
:NSX: - Tenants are now able to be deleted if they had NSX network groups associated with them :superscript:`6.2.10`
:Network: - Improved Cloud-init network config syntax and nameserver configuration under specific conditions when utilizing networks with IPv4 and IPv6 enabled along with IP Pools and DNS configured for IPv4 and IPv6 :superscript:`6.2.10`
:Nutanix Prism Central: - Fixed ``HostSync`` and ``SyncTask`` errors in logs when syncing Nutanix Prism Central Clouds :superscript:`6.2.10`
                  - Fixed an issue that left images deleted from Nutanix Prism Central remaining with |morpheus| and using storage unnecessarily :superscript:`6.2.10`
                  - Fixed images not uploading from NFS storage to integrated Nutanix Prism Central Clouds :superscript:`6.2.10`
                  - Fixed intermittent errors (``error executing query``) in logs coming from Nutanix Prism Central integrations :superscript:`6.2.10`
                  - Fixed the hypervisor console not working on subsequent attempts to access it, only working the first time :superscript:`6.2.10`
                  - Saving edits to synced images in airgapped environments no longer fails with 500 errors :superscript:`6.2.10`
:Nutanix: - Fixed an issue that caused provisioning failure when an NFS file share was used as the image repository on a |morpheus| appliance :superscript:`6.2.10`
:Proxies: - Updated several internally-developed plugins to honor the "No Proxy" configuration when present :superscript:`6.2.10`
:Roles: - Users in Roles with "Read" permission on Clouds will no longer be allowed to manually trigger a refresh the Cloud, which brings UI behavior in line with API behavior :superscript:`6.2.10`
         - When viewing user permissions for a currently logged in user which has only the built-in System Admin Role, the Cypher feature permission level is now properly shown as "Full Decrypted" :superscript:`6.2.10`
:Security: - Fixed a bug that allowed delete confirmation modals requiring the user to type "DELETE" to be bypassed without typing the required word which could lead to unintended deletions :superscript:`6.2.10`
            - Improved the CyberArk plugin to prevent what could be considered a sensitive information disclosure in stacktrace error messages :superscript:`6.2.10`
:Tasks: - Powershell Tasks are now run in 64-bit rather than 32-bit :superscript:`6.2.10`
:Tenants: - We now gracefully handle situations where previously a workload could not be assigned from the |mastertenant| to another Tenant if there was a currently-existing workload with the same name :superscript:`6.2.10`
:Terraform: - After deploying a Terraform App, renaming any ``.tf`` files in the repository will no longer cause problems for future attempts to apply state :superscript:`6.2.10`
             - Fixed Terraform Instances and Apps bypassing Approve Delete Policies which allowed them to be deleted without approval :superscript:`6.2.10`
             - Updated the HCL parser to improve compatibility in certain scenarios
:Trust: - Added UI validation when adding SSH keypairs in the Trust section (|InfTru|) to make it clearer to the user when an invalid keypair has been entered :superscript:`6.2.10`
         - When attempting to remove a keypair which is already linked to another resource (integration, etc.), there is now a clearer UI warning to indicate why the keypair cannot be deleted :superscript:`6.2.10`
:VMware: - Fixed an issue that could cause orphaned VMware-related records to pile up in the database and create performance issues :superscript:`6.2.10`
          - Fixed issue where using the "Order Again" button in Catalog would provision the new VM into the root vCenter folder rather than the folder selected for the original VM ordered :superscript:`6.2.10`
          - Instances which were powered off will no longer appear in a running state in |morpheus| following a reconfigure (though they were always still off in VMware) :superscript:`6.2.10`
          - Added an optimization to the reconfigure logic for workloads on VMware Clouds. If a server is resized to change network interface details, any reserved IP address is only released to the IP pool if a new network is selected for the interface
:Virtual Images: - Creating a new Virtual Image sourced by URL will now go through any configured global proxies :superscript:`6.2.10`
                  - The filter "VMware (vmdk/ovf/ova)" now includes images synced from vCloud Director :superscript:`6.2.10`


Appliance & Agent Updates
=========================

:Appliance: - Added a configuration in ``morpheus.rb`` to enable the ipv6 listener for Nginx with ``nginx['listen_ipv6'] = true`` (note: IPv6 will be added to ``morpheus.conf`` and ``morpheus-ssl.conf`` listeners if any value is set in morpheus.rb other than ``nil``, including "off" or false) :superscript:`6.2.10`
:Database: - External mysql service: Added support for Appliance using Amazon Aurora RDS MySQL version 3.06.0+ :superscript:`6.2.10`
