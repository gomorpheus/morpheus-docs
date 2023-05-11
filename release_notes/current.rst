.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. WARNING:: |morpheus| |morphver| only supports rolling upgrades for HA environments when upgrading from v6.0.2.

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|

.. IMPORTANT:: In |morpheus| |morphver|, many third party integrations have been moved out of the core installer package and converted to |morpheus| plugins. As a result, during the upgrade process your appliance will need to be able to access share.morpheusdata.com, the online repository for all |morpheus| plugins. Where this is not possible, users may instead apply the supplemental installer package which is also available at |morpheus| Hub alongside the main installer package.

.. IMPORTANT:: NSX-V support is deprecated though still supported as of |morpheus| 6.0.0. It will be removed and unsupported in 6.1.1 and higher.

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:Health: - The database version is now shown in the database section of the Health page (|AdmHea|) :superscript:`6.1.1`
:Instances: - Instances now have a Name and Display Name field when editing. Previously editing the Name only updated the Display Name database property which created confusion when duplicate name warnings were received in future provisioning
:KVM: - KVM hypervisors on OpenStack now display server stats (CPU, memory, storage) consistently as ESXi hypervisors do in |morpheus| :superscript:`6.1.1`
:Logs: - |morpheus| Agent logs can now be disabled on a per-server basis in additional to the global enable/disable setting which is already in the product :superscript:`6.1.1`
:Plugins: - The F5 load balancer integration has been converted to a plugin. The plugin is available at share.morpheusdata.com and, once added to the appliance, makes the F5 integration type available :superscript:`6.1.1`
           - The MicrosoftDNS plugin has been updated to version 2.0.0. It is recommended that users upgrade their plugin. The new version and updated release notes are at share.morpheusdata.com
:ServiceNow: - Payloads sent from |morpheus| to ServiceNow now include the appliance URL in the payload, which is validated in addition to the stored credentials
:VMware: - In vCenter Clouds, ESXi host status will now show as offline when in maintenance mode :superscript:`6.1.1`
:Virtual Machines: - Default user accounts are no longer included in the |morpheus| default catalog of virtual images :superscript:`6.1.1`


Fixes
=====

:API & CLI: - Added API endpoint for registering NSX-T load balancer pool members :superscript:`6.1.1`
             - Creating Network Firewall Rules via |morpheus| API no longer fails with errors
             - Fixed an issue that prevented updating Instance Scale Thresholds through |morpheus| API :superscript:`6.1.1`
             - For API calls to GET a specific network (and corresponding CLI commands), IPv6 properties for CIDR, gateway, netmask, primary DNS, secondary DNS, pool, and DHCP are being returned in the API response as they are for IPv4 :superscript:`6.1.1`
             - Updated the Create Instance API payload to accept an ``externalId`` attribute for the VMware folder to avoid user confusion as to which value is needed :superscript:`6.1.1`
             - Updating an Instance via |morpheus| API no longer fails when a new Monitoring Check has been added to the Monitoring Group for that Instance :superscript:`6.1.1`
             - Using the Create a Storage Bucket API endpoint to create a NFS file share is now working properly whether or not the bucket property is passed :superscript:`6.1.1`
             - When calling |morpheus| API to get permissions for a Role, the Group permissions are now shown accurately in the API payload as compared with what is shown in the UI :superscript:`6.1.1`
             - When starting and stopping Instances via |morpheus| API, Tasks in the startup and shutdown phases now run successfully and their history is logged :superscript:`6.1.1`
             - |morpheus| API and CLI calls to add new Cypher entries are now working correctly when the Cypher key has a whitespace (" ") in it :superscript:`6.1.1`
:Active Directory: - Fixed an issue causing intermittent login failure when two or more Active Directory ID sources with required groups were active :superscript:`6.1.1`
:Activity: - In the History tab of the Activity section (|OpeAct|), expired Tasks will now show a red "X" icon rather than the spinning circular arrow :superscript:`6.1.1`
:Alibaba Cloud: - The Cloud region attribute is now editable prior to the first daily Cloud sync :superscript:`6.1.1`
:Amazon: - Fixed Cloud sync failures associated with removal of a VPC via the AWS web console which at one time had associated Instances :superscript:`6.1.1`
          - Fixed an issue that caused discovered AWS Windows VMs to be incorrectly tagged with an OS type of Linux :superscript:`6.1.1`
          - Updated EBS volume configuration to reflect updated size minimums (ex. EBS SC1 volumes can now be as small as 125 GB) :superscript:`6.1.1`
          - When creating AWS RDS Instances from Subtenants, the required DB Engine Version and DB Subnet Group dropdown menus (required) are now populated :superscript:`6.1.1`
:Ansible: - Command options can now be used successfully in Ansible Tasks which are part of provisioning workflows and entered at provision time
           - Fixed an issue that caused Ansible Tasks to fail when run against the Server context :superscript:`6.1.1`
:Approvals: - Fixed an issue that caused Delete Approvals to pile up when Azure SQL database instances were deleted from the cloud console outside of |morpheus| :superscript:`6.1.1`
             - When an Approvals Policy targeted to a ServiceNow integration has an Approval cancelled in |morpheus|, the status of the Approval is now updated on the ServiceNow side :superscript:`6.1.1`
:Apps: - When provisioning Apps, "field is required" messages will no longer supersede and obscure any help block text which has been set on the required Input :superscript:`6.1.1`
:Azure: - Network Security Groups now require a name value as they do on the Azure backend :superscript:`6.1.1`
         - When editing Azure networks, the correct Resource Pool is now shown in the UI and matches up with the Pool given in the API response :superscript:`6.1.1`
:Backups: - Disabling the appliance backup from global settings (|AdmSet|) will no longer delete any existing backups that may have been taken :superscript:`6.1.1`
           - Removed SQL server-type backup jobs from Instance provisioning wizard for certain Instance types which wasn't supported :superscript:`6.1.1`
:Bluecat: - Secondary DNS server IPs are now correctly set in the guest OS when provisioning to Clouds with a configured Bluecat DNS integration :superscript:`6.1.1`
:Blueprints: - When App Blueprint names are very long, the disk volume size on the Edit Blueprint modal is no longer obscured :superscript:`6.1.1`
:Catalog: - Catalog items will now give more freedom in adding and removing config from the JSON map. Previously some additions and deletions from the config would not be saved :superscript:`6.1.1`
           - Fixed an issue that allowed Catalog Items to be ordered without filling all required Inputs when Input visibility was dependent on other Inputs :superscript:`6.1.1`
:Costing: - The price comparison pop-out panel in the Instance Provisioning Wizard now mixes in Azure Cloud price comparisons in more cases :superscript:`6.1.1`
           - Updated datastore pricing logic to ensure accuracy in specific scenarios :superscript:`6.1.1`
:Deployments: - Fixed deployments failing when using Git tag references :superscript:`6.1.1`
:Email Notifications: - Fixed certain variables not resolving in Instance Ready and Instance Expiration email notifications :superscript:`6.1.1`
:Git Repository: - Fixed access issues to integrated Git repositories over SSH in certain scenarios :superscript:`6.1.1`
                  - Git integrations can now be successfully created or edited when there is a non-empty file named "config" in the "/tmp" directory :superscript:`6.1.1`
:Hashicorp Vault: - Fixed an issue that could cause Hashicorp Vault integrations to become stuck in a syncing state and never complete :superscript:`6.1.1`
:Hosts: - Fixed ESXi hosts displaying an incorrect ESXi version number on their host detail pages :superscript:`6.1.1`
         - The Delete Host modal help text no longer references the "Remove Infrastructure" option unless it is present on the modal :superscript:`6.1.1`
         - When viewing the server detail page for Subtenant-owned servers from the Primary Tenant, the search and sync capabilities of the Software tab are now working correctly :superscript:`6.1.1`
:IPAM: - Validation is no longer performed when saving disabled IPAM integrations as this could potentially make it impossible to disable an unreachable IPAM integration :superscript:`6.1.1`
:Identity Sources: - Password reset email is no longer sent for Active Directory-sourced users as it should be for |morpheus|-local users :superscript:`6.1.1`
:Inputs: - Both Select List and Typeahead Inputs tied to |morpheus| API Group Option Lists now provide the zoneId, cloudId, siteId, and groupId in the response :superscript:`6.1.1`
          - Fixed an issue that caused incorrect Input values to be returned when the default value for dependent Inputs was used :superscript:`6.1.1`
:Instances: - Added a reboot warning when reconfiguring Instances to add cores per socket (which will reboot the VMs) :superscript:`6.1.1`
             - Added validation to Environment Prefix values and Environment Variable Name values to ensure users aren't adding illegal characters for the OS type, such as "(" in Linux :superscript:`6.1.1`
             - Fixed an issue which could cause the scaling tools (remove node button, Scale tab, etc.) not to appear on the Instance detail page even if the Instance Type should support scaling :superscript:`6.1.1`
             - Fixed reconfigure actions to add disks also removing and re-adding NICs :superscript:`6.1.1`
             - Fixed |morpheus| variables not resolving correctly in Tasks on nodes which were added to the Instance after provisioning :superscript:`6.1.1`
:KVM: - Fixed an issue that caused Max Cores Policies to be applied incorrectly when provisioning KVM Instances or Clusters :superscript:`6.1.1`
:Kubernetes: - Cluster delete no longer fails when all nodes have already been deleted from the Cloud itself outside of |morpheus| :superscript:`6.1.1`
              - Updated field type on a specific database field to prevent sync errors on Kubernetes clusters due to data length :superscript:`6.1.1`
:Layouts: - The Edit Layout modal now properly handles adding/removing multiple nodes of the same type as the Add Node modal already did correctly :superscript:`6.1.1`
:Library: - The logo set on each library item is now used in more places in the UI to replace generic logo imagery
:Load Balancers: - Domains of more than 3 parts can now be used for the VIP hostname when provisioning a load balancer :superscript:`6.1.1`
                  - When adding an F5 load balancer to an Amazon Instance, the partition list will not populate correctly :superscript:`6.1.1`
:MacStadium: - Fixed log errors that would appear when syncing cost data from MacStadium Cloud
:Morpheus IP Pools: - Fixed a display issue associated with some IP Pool ranges :superscript:`6.1.1`
:NSX-T: - Added validation when deleting NSX-T Load Balancers with associated virtual servers to mirror the behavior of the NSX-T console which does not allow this without first cleaning up the associated virtual servers :superscript:`6.1.1`
         - Fixed pagination when more than 25 NSX-T firewall rules are present :superscript:`6.1.1`
         - Improved status reporting (provisioning, online, offline, unknown, etc.) for NSX-T Load Balancers and their components (pools, virtual servers, etc.) to more accurately reflect in Morpheus the reported state in NSX-T :superscript:`6.1.1`
         - When editing NSX-T server groups with segments attached as group members, the segments are displayed correctly :superscript:`6.1.1`
:Network: - Networks are no longer validated when saved if the Network is disabled :superscript:`6.1.1`
:Nutanix: - Fixed Nutanix server provisioning with machine type :superscript:`6.1.1`
           - Fixed an issue assigning static IPs to Nutanix workloads that caused a pool IP to be used over the static IP assignment :superscript:`6.1.1`
           - When provisioning Nutanix Instances, disk name labels will now reflect the name given at provision time on the Nutanix side rather than being named with an ID value :superscript:`6.1.1`
:OpenStack: - Fixed Instance reconfiguration of multi-VM Instances removing and re-adding network interfaces on the VMs causing them to become unreachable :superscript:`6.1.1`
             - Fixed OpenStack Plans not being listed in Morpheus API-type Option Lists when applied to Inputs on Instance or Blueprint Catalog Items :superscript:`6.1.1`
             - The external IP address is now shown for OpenStack routers created in |morpheus| as was already the case for synced routers coming from OpenStack itself :superscript:`6.1.1`
:Oracle Cloud: - Adding and removing volumes on Instances converted from brownfield VMs now works properly :superscript:`6.1.1`
:Plans and Pricing: - Fixed an issue that caused failures adding external Kubernetes Clusters when the "Default External" Kubernetes Plan was deactivated :superscript:`6.1.1`
                  - For appliances with only one Tenant, Service Plans are no longer hidden from the UI when a specific Group permission is assigned to the Plan :superscript:`6.1.1`
                  - Plans with root volume storage set to 0 and the option to customize the root volume unchecked are no longer filtered out from "Plan" Inputs sourced from Morpheus API Option Lists during Catalog Item provisioning :superscript:`6.1.1`
:Policies: - Disabled ServiceNow integrations are no longer available for selection as Approval Policy targets :superscript:`6.1.1`
            - Fixed an issue where a Delayed Delete Policy could cause backend infrastructure to be removed on delete even when the option was unchecked :superscript:`6.1.1`
            - When changing an Approval Policy from ServiceNow to an internal Approval Policy, the Policies list view now properly updates the Approval type to internal :superscript:`6.1.1`
            - When making configurations in the Instance provisioning wizard which trigger a locked naming Policy, then changing the configuration to something outside the Policy scope, the Name field now unlocks as expected :superscript:`6.1.1`
:PowerShell: - Fixed an issue that caused PowerShell Tasks to fail if they exceeded a certain character count :superscript:`6.1.1`
:Provisioning: - Provisioning with JSON passed as an Input (customOption) is now working properly :superscript:`6.1.1`
                - The default scale type (such as in the scale type dropdown on the AUTOMATION tab of the provisioning wizard) has been relabeled "Standard" as opposed to "Morpheus" :superscript:`6.1.1`
                - Updated logic for the Cloud Price Comparison panel which can be viewed from the provisioning wizard to better select analogous plan types for comparison :superscript:`6.1.1`
:Reports: - Improved logic to correct discrepancies in the Group Inventory Summary Report :superscript:`6.1.1`
:Resource Pools: - Plan access permissions set on the Resource Pool are now correctly honored within the Instance Provisioning Wizard. Once the Plan is set only Resource Pools with access to the Plan appear in the dropdown :superscript:`6.1.1`
:Roles: - When editing Group permissions for a Subtenant's User Roles from the Primary Tenant, the "Update All" dropdown now correctly updates the permission level for all Groups :superscript:`6.1.1`
         - When feature permissions for backups are set to "None" the "Backup" option from the ACTIONS menu on the Instances list page is hidden (as is already the case from the Instance detail page) :superscript:`6.1.1`
:Route 53: - Fixed an issue which caused the Add Zone Record modal to get stuck when creating Route 53 Zone Records :superscript:`6.1.1`
:Scaling: - When both a threshold and schedule are defined on an instance, the schedule config for the scaling behavior wins out and no longer is counterbalanced by any conflicting settings in the threshold :superscript:`6.1.1`
:Security: - The User's first and last name are now excrypted in the database to protect personally identifiable information :superscript:`6.1.1`
:Tags: - Fixed an issue that caused tag dropdown menus not to appear in the provisioning wizard even when a strict tag enforcement policy was set :superscript:`6.1.1`
:Tasks: - Fixed a UI issue related to adding multiple headers to HTTP Tasks :superscript:`6.1.1`
         - Fixed an issue that caused Powershell Tasks not to authenticate properly when using stored credential sets :superscript:`6.1.1`
         - Powershell Tasks are no longer incorrectly run as Bash Tasks when run against Linux workloads. Powershell must already be installed on the workload or Powershell Tasks will fail :superscript:`6.1.1`
         - Tasks executed in a server context will now evaluate the "tenant" variable (<%=tenant%>) properly :superscript:`6.1.1`
         - When Tasks are re-saved to run against a "Resource" context rather than a static remote context and then run via WinRM on the resource, the "Resource" context is now honored :superscript:`6.1.1`
:Tenants: - Fixed an issue that prevented deleting Tenants if a Task had been created in the Tenant :superscript:`6.1.1`
           - Fixed an issue which prevented Tenants from being deleted successfully if they had Ansible Tower integrations which had synced job templates :superscript:`6.1.1`
           - When deleting a Tenant and leaving "Remove Associated Resources" unchecked, load balancers associated with the Tenant are no longer removed :superscript:`6.1.1`
:Terraform: - Errors are no longer received when changing the Git branch on an existing Terraform Blueprint :superscript:`6.1.1`
             - TF builds no longer fail with a space in the "required_version" configuration (ex. required_version = ">= 0.12") :superscript:`6.1.1`
             - Terraform auto download functionality will now utilize the configured global proxy if one is set :superscript:`6.1.1`
:UI: - On the Compute List page (Hosts, Containers, VMs, etc.), users can no longer add a "Used" column to the view which did not show any data :superscript:`6.1.1`
      - On the Instance Detail History Tab, when clicking on the info (i) button to see complete output, very long error messages from the section above will no longer overset the output area below :superscript:`6.1.1`
      - Prices shown on the Instance Detail Page are now limited to two decimal places of precision for increased readability :superscript:`6.1.1`
      - The Instances List Page is now sorted on the display name of the Instance rather than an internal "name" value in the database which isn't surfaced into the UI :superscript:`6.1.1`
:Usage: - When changing currency on the Tenant, Usage records will now restart as expected :superscript:`6.1.1`
:VDI Gateways: - Access to VDI Gateways and VDI Apps tabs is now dependent only on the "Virtual Desktop: VDI Pools" feature permission and no longer requires "Tools: Image Builder" permission as well :superscript:`6.1.1`
:VMware: - Fixed resizing errors that could appear when reconfiguring VMware volumes even though the resize would take place correctly on the backend :superscript:`6.1.1`
          - In Instance, App, Blueprint, and Cluster Wizards, the datastores and hosts are correctly filtered based on the Resource Pool selection. Without filtering, incorrect configurations were possible :superscript:`6.1.1`
          - Removed a warning related to Snapshots being deleted when reconfiguring VMware Instances to add disks as Snapshots were not actually deleted in that case :superscript:`6.1.1`
          - Removed the "ACTIVE" checkbox for folders from the view of non-owners of the folder (only owners could successfully adjust the property anyway) :superscript:`6.1.1`
          - When credentials are changed or expire preventing |morpheus| from talking to VMware or NSX-T, errors are now given in logs in addition to the UI :superscript:`6.1.1`
:Veeam: - When provisioning to VMware Clouds which have an associated Veeam backup integration, the backups section of the wizard will automatically expand to make it more obvious that section is required and that the wizard isn't simply stuck :superscript:`6.1.1`
:Virtual Images: - |morpheus| now assumes OVF capacity values to be in bytes rather than GB unless an allocation unit is specifically set to align with open specification standards :superscript:`6.1.1`
:Workflows: - Fixed an issue that caused Teardown-phase Tasks not to run at Instance delete :superscript:`6.1.1`
             - Fixed an issue that caused provisioning failure when File Templates containing calls to |morpheus| Cypher were included in the Pre-Provision phase of a Provisioning Workflow :superscript:`6.1.1`
             - Fixed differing output of same Workflow and custom options when Workflow was executed via the Workflows list page or via a Workflow-based Catalog Item :superscript:`6.1.1`


Appliance & Agent Updates
=========================

:Appliance: - Encryption: Fixed ``extract ca certificate`` issue when using ENC() string for keystore_password


.. ..
