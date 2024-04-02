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

:API & CLI: - Added API support for optionally specifying a stack name when provisioning from CloudFormation templates :superscript:`6.2.8`
             - Added API support for specifying an S3 bucket to read CloudFormation templates from during provisioning. This is necessary when provisioning from CF templates greater than 50 KB :superscript:`6.2.8`
:CloudFormation: - Provisioning from CloudFormation templates now includes a "STACK NAME" configuration. By default, this will be the same as the Instance or App name but can be overridden :superscript:`6.2.8`
                  - When provisioning from CloudFormation Spec Templates, added a configuration to specify an S3 bucket to read the Spec Template from. This is required for CF templates greater than 50 KB :superscript:`6.2.8`
:Dashboard: - Added support for Spanish-language localizations for |morpheus| Dashboard :superscript:`6.2.8`
:Identity Sources: - "Post RelayState" field added for For SAML SSO Identity Sources using "Post Binding Mode" for defining RelayState post parameter. :superscript:`6.2.8`
:Import/Export: - Forms can now be used with the import/export feature. Export Forms as code into an integrated Git repository and import them back into any other appliance with the same repository integrated
:Kubernetes: - System Kubernetes 1.29 Layouts added :superscript:`6.2.8`
:Policies: - The Roles and Policies list pages have been updated to give the user control over visible output columns and page size
:Roles: - Added a Cluster Types tab to the Role detail page to control the Cluster types available to the Role
:Security: - Upgraded ``spring-web`` to version 5.3.32 to mitigate CVE-2024-22243 :superscript:`6.2.8`
:Terraform: - For licensing reasons, automated Terraform installs handled by |morpheus| are now capped at version 1.5.5. Other versions may be utilized in |morpheus| through manual installation :superscript:`6.2.8`
:VMware: - When Snapshot names are changed in VMware, the name change is now reflected in |morpheus| following the next Cloud sync :superscript:`6.2.8`


Fixes
=====

:API & CLI: - Adding or updating Identity Sources via |morpheus| API, will no longer fail when adding a mapping for a built-in role (such as System Admin) :superscript:`6.2.8`
             - After updating the CODE value on a Cloud (via UI or API), GET calls to ``/api/billing/zones`` no longer return the old ``zoneCode`` value :superscript:`6.2.8`
             - Fixed situations where a 200 status and a ``success=false`` message could be received in the same response when creating virtual servers for load balancers via |morpheus| API :superscript:`6.2.8`
             - Service Plans created via API without a ``config.ranges`` value in the payload can now be updated normally via API :superscript:`6.2.8`
             - Updating Catalog Item icon logos via |morpheus| API now works correctly :superscript:`6.2.8`
:Agent: - Fixed an issue with the Windows Agent that could cause CPU usage to be reported incorrectly for VMs within the UI :superscript:`6.2.8`
         - Linux Agent upgrades now update the appliance URL (if applicable) to account for situations in which this has changed since the last Agent upgrade :superscript:`6.2.8`
:Amazon: - Fixed an issue causing actions such as adding nodes or reconfiguring at the Instance or VM level from working correctly for discovered nodes which were converted to managed :superscript:`6.2.8`
          - Fixed an issue that prevented AWS Clouds scoped to all regions from reading from region-scoped S3 buckets :superscript:`6.2.8`
          - Fixed an issue with snapshot sync when more than 1000 snapshots exist in an aws account. :superscript:`6.2.8-2`
          - When creating RDS Instances on AWS Clouds, the subnet groups now populate correctly for Clouds scoped to all regions :superscript:`6.2.8`
          - When scoping AWS Clouds to all VPCs, DB subnets available on the AWS Cloud are now discovered properly and are available for selection during RDS provisioning. Previously, this only worked correctly when scoping to a specific VDC :superscript:`6.2.8`
:Apps: - When adding an Instance to an existing App, the display name of the Instance is now shown rather than the Instance name :superscript:`6.2.8`
:Catalog: - The default FORM TYPE value for catalog items is now "Select" (that is, unselected) rather than "Form" :superscript:`6.2.8`
:Cluster Layouts: - Hidden-type Inputs on Cluster Layouts now show the ``inputName`` value along with "(hidden" when the Cluster Layout is later edited :superscript:`6.2.8`
                  - On custom Cluster Layouts, Inputs are no longer shown in an order when many Inputs are used (approximately five or more) :superscript:`6.2.8`
:Clusters: - When additional nodes are added to Clusters, they now have the custom options values (Input values) that nodes created at initial cluster provision had :superscript:`6.2.8`
:Costing: - Fixed costs shown on Instance detail pages within Subtenants showing costs in USD rather than the configured Tenant currency :superscript:`6.2.9`
           - Fixed the "Cost this Month" figure displayed for a Cloud integrated in the |mastertenant| and shared down with a Subtenant :superscript:`6.2.8`
:Cypher: - Removed the "sys" mountpoint tool tip from the "ADD KEY" modal that appears when adding a new entry to Cypher :superscript:`6.2.8`
          - When File Templates containing calls to Cypher are set on a Node Type created in the |mastertenant|, the Cypher values are now properly decrypted when provisioning involving the Node Type takes place in a subtenant :superscript:`6.2.8`
:Hosts: - Improved the backend logic for handling server records moved from one Cloud type to another (Change Cloud functionality) :superscript:`6.2.8`
:Import/Export: - Fixed a situation where "Export All" could cause the UI to become unresponsive and require restart :superscript:`6.2.8`
:Inputs: - Fixed Input dependency and visibility not working as configured when the Inputs were created by different methods (API vs UI) :superscript:`6.2.8`
:Instances: - Fixed Layout and Version fields not appearing on "Convert to Instance" modal (for converting servers to managed Instances) :superscript:`6.2.9`
             - Fixed reconfigures to add disks dropping the name(s) of the new disk(s) under specific conditions :superscript:`6.2.8`
             - Improved how CPU representation graphs are displayed to prevent misinterpretation of total CPU capacity being used :superscript:`6.2.8`
:Kubernetes: - Fixed 500 errors being thrown when Kubernetes Apps were deleted :superscript:`6.2.8`
:NSX-T: - Fixed network resources being visible in other Subtenants when NSX-T integrations created in one Subtenant were scoped to a public Cloud integrated from the |mastertenant| :superscript:`6.2.9`
         - Load balancer virtual server protocol configuration can now be successfully updated via |morpheus| API and CLI :superscript:`6.2.8`
:Network: - A friendly UI error message is now given when attempting to save a network display name larger than 255 characters :superscript:`6.2.8`
:Nutanix Prism Central: - Discovered hypervisor hosts now correctly display the OS rather than defaulting statically to display "ESXi" :superscript:`6.2.8`
                  - Fixed Instances not deleting when they were provisioned to Nutanix networks utilizing |morpheus| IP Pools :superscript:`6.2.8`
                  - Network interfaces on Prism Central VMs no longer show a null MAC address until after the first Cloud sync following provisioning :superscript:`6.2.8`
:Option Lists: - Setting a proxy that requires authentication no longer causes 407 errors and fetch failures for REST-populated Option Lists :superscript:`6.2.8`
:Plugins: - Updated Ansible Tower and Bluecat plugins to honor global proxy settings :superscript:`6.2.8`
:Proxies: - The |morpheus| Windows Agent now uses a proxy if one is configured :superscript:`6.2.8`
:SAML: - There are no longer two POST BINDING MODE fields on Add/Edit modals for SAML SSO Identity Sources. Additionally, the INCLUDES SAML REQUEST PARAMETER field no longer toggles back to "Yes" on edit :superscript:`6.2.8`
:SCVMM: - Fixed SCVMM Clouds scoped to specific clusters discovering workloads from outside that scoped cluster :superscript:`6.2.8`
         - Fixed an issue that could cause cloned Veeam backups for SCVMM Instances to not be created properly :superscript:`6.2.8`
:Security: - Fixed cache files exposing cloud credentials in plaintext under certain conditions when local credentials (not stored credentials) were used to authenticate the cloud integration :superscript:`6.2.8`
:VMware: - Any changes to minimum memory values for an image in vCenter are now properly synced over to |morpheus| on the next Cloud sync :superscript:`6.2.8`
          - Fixed tag values being updated via |morpheus| API being wiped out on the next Cloud sync :superscript:`6.2.8`


Appliance Updates
=================

:Agents: - Linux Agent: |morpheus| linux agent updated to |linuxagentver| 
         - Windows Agent: |morpheus| Windows Agent updated to |winagentver|
:Appliance: - mysql: Updated default jdbc url used for db cluster connections to include connectTimeout, maxReconnects, queriesBeforeRetrySource and secondsBeforeRetrySource. Default values can be updated in morpheus.rb. :superscript:`6.2.8`
             - nginx: Logging requests to the ``/ping`` endpoint of |morpheus| app nodes are now disabled by default. Logging can be renabled by adding nginx['ssl_access_ping_log'] = true &
nginx['access_ping_log'] = true to morpheus.rb :superscript:`6.2.8`
             - Package repo cleanup: The appliance installer has been updated to clean /var/opt/morpheus/package-repos/ directory after package install when it is larger than 5GB.  The current |morpheus| package repo files will be added during reconfigure or supplemental package install :superscript:`6.2.8`
             - SLES 15 FIPS: - Added a FIPS-compliant |morpheus| installer for SLES 15 :superscript:`6.2.8`
:Embedded Plugins: - Bluecat: bluecat-plugin updated to v1.2.1
                   - DigitalOcean: digital-ocean-plugin updated to v1.2.3
                   - Infoblox: infoblox-plugin updated to v1.3.5
                   - Solarwinds: solarwinds-plugin updated to v1.1.2
                   - phpIPAM: phpipam-plugin updated to v1.2.3
                   - Efficient IP: efficient-ip-plugin updated to v1.2.1
:Node Package: - |morpheus| Node & VM Node Packages updated to |nodePackageVer|

Worker
======

:Distributed Worker: - |morpheus| Worker v7.0.0 now available
                     - Distributed worker v7.0.0 can now be deployed in a highly-available configuration. See distributed worker documentation for additional details
