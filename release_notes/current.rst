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

:API & CLI: - Added API support for optionally specifying a stack name when provisioning from CloudFormation templates
             - Added API support for specifying an S3 bucket to read CloudFormation templates from during provisioning. This is necessary when provisioning from CF templates greater than 50 KB
:Agent: - Updated the Windows Agent to send fewer logs :superscript:` 7.0.0`
:CloudFormation: - Provisioning from CloudFormation templates now includes a "STACK NAME" configuration. By default, this will be the same as the Instance or App name but can be overridden :superscript:` 7.0.0`
                  - When provisioning from CloudFormation Spec Templates, added a configuration to specify an S3 bucket to read the Spec Template from. This is required for CF templates greater than 50 KB :superscript:` 7.0.0`
:Dashboard: - Added support for Spanish-language localizations for |morpheus| Dashboard :superscript:` 7.0.0`
:Identity Sources: - "Post RelayState" field added for For SAML SSO Identity Sources using "Post Binding Mode" for defining RelayState post parameter. :superscript:` 7.0.0`
:Installer: - Added a FIPS-compliant |morpheus| installer for SLES 15 :superscript:` 7.0.0`
:Kubernetes: - System Kubernetes 1.29 Layouts added :superscript:` 7.0.0`
:Security: - Upgraded ``spring-web`` to version 5.3.32 to mitigate CVE-2024-22243
:Terraform: - For licensing reasons, automated Terraform installs handled by |morpheus| are now capped at version 1.5.5. Other versions may be utilized in |morpheus| through manual installation :superscript:` 7.0.0`
:VMware: - When Snapshot names are changed in VMware, the name change is now reflected in |morpheus| following the next Cloud sync :superscript:`7.0.0 `


Fixes
=====

:API & CLI: - Adding or updating Identity Sources via |morpheus| API, will no longer fail when adding a mapping for a built-in role (such as System Admin) :superscript:` 7.0.0`
             - After updating the CODE value on a Cloud (via UI or API), GET calls to ``/api/billing/zones`` no longer return the old ``zoneCode`` value :superscript:` 7.0.0`
             - Fixed situations where a 200 status and a ``success=false`` message could be received in the same response when creating virtual servers for load balancers via |morpheus| API :superscript:` 7.0.0`
             - Service Plans created via API without a ``config.ranges`` value in the payload can now be updated normally via API :superscript:` 7.0.0`
             - Updating Catalog Item icon logos via |morpheus| API now works correctly
:Agent: - Fixed an issue with the Windows Agent that could cause CPU usage to be reported incorrectly for VMs within the UI :superscript:` 7.0.0`
         - Linux Agent upgrades now update the appliance URL (if applicable) to account for situations in which this has changed since the last Agent upgrade :superscript:` 7.0.0`
:Amazon: - Fixed an issue causing actions such as adding nodes or reconfiguring at the Instance or VM level from working correctly for discovered nodes which were converted to managed
          - Fixed an issue that prevented AWS Clouds scoped to all regions from reading from region-scoped S3 buckets
          - When creating RDS Instances on AWS Clouds, the subnet groups now populate correctly for Clouds scoped to all regions :superscript:` 7.0.0`
          - When scoping AWS Clouds to all VPCs, DB subnets available on the AWS Cloud are now discovered properly and are available for selection during RDS provisioning. Previously, this only worked correctly when scoping to a specific VDC :superscript:` 7.0.0`
:Apps: - When adding an Instance to an existing App, the display name of the Instance is now shown rather than the Instance name :superscript:` 7.0.0`
:Catalog: - The default FORM TYPE value for catalog items is now "Select" (that is, unselected) rather than "Form" :superscript:` 7.0.0`
:Cluster Layouts: - Hidden-type Inputs on Cluster Layouts now show the ``inputName`` value along with "(hidden" when the Cluster Layout is later edited :superscript:` 7.0.0`
                  - On custom Cluster Layouts, Inputs are no longer shown in an order when many Inputs are used (approximately five or more) :superscript:` 7.0.0`
:Clusters: - When additional nodes are added to Clusters, they now have the custom options values (Input values) that nodes created at initial cluster provision had :superscript:` 7.0.0`
:Costing: - Fixed the "Cost this Month" figure displayed for a Cloud integrated in the |mastertenant| and shared down with a Subtenant :superscript:` 7.0.0`
:Cypher: - Removed the "sys" mountpoint tool tip from the "ADD KEY" modal that appears when adding a new entry to Cypher :superscript:` 7.0.0`
          - When File Templates containing calls to Cypher are set on a Node Type created in the |mastertenant|, the Cypher values are now properly decrypted when provisioning involving the Node Type takes place in a subtenant :superscript:` 7.0.0`
:Import/Export: - Fixed a situation where "Export All" could cause the UI to become unresponsive and require restart
:Inputs: - Fixed Input dependency and visibility not working as configured when the Inputs were created by different methods (API vs UI) :superscript:` 7.0.0`
:Instances: - Fixed reconfigures to add disks dropping the name(s) of the new disk(s) under specific conditions :superscript:` 7.0.0`
             - Improved how CPU representation graphs are displayed to prevent misinterpretation of total CPU capacity being used :superscript:` 7.0.0`
:Kubernetes: - Fixed 500 errors being thrown when Kubernetes Apps were deleted :superscript:` 7.0.0`
:NSX-T: - Load balancer virtual server protocol configuration can now be successfully updated via |morpheus| API and CLI :superscript:` 7.0.0`
:Network: - A friendly UI error message is now given when attempting to save a network display name larger than 255 characters :superscript:` 7.0.0`
:Nutanix Prism Central: - Discovered hypervisor hosts now correctly display the OS rather than defaulting statically to display "ESXi" :superscript:` 7.0.0`
                  - Fixed Instances not deleting when they were provisioned to Nutanix networks utilizing |morpheus| IP Pools :superscript:` 7.0.0`
                  - Network interfaces on Prism Central VMs no longer show a null MAC address until after the first Cloud sync following provisioning :superscript:` 7.0.0`
:Option Lists: - Setting a proxy that requires authentication no longer causes 407 errors and fetch failures for REST-populated Option Lists :superscript:` 7.0.0`
:Plugins: - Updated Ansible Tower and Bluecat plugins to honor global proxy settings :superscript:` 7.0.0`
:Proxies: - The |morpheus| Windows Agent now uses a proxy if one is configured :superscript:` 7.0.0`
:SAML: - There are no longer two POST BINDING MODE fields on Add/Edit modals for SAML SSO Identity Sources. Additionally, the INCLUDES SAML REQUEST PARAMETER field no longer toggles back to "Yes" on edit :superscript:` 7.0.0`
:SCVMM: - Fixed SCVMM Clouds scoped to specific clusters discovering workloads from outside that scoped cluster :superscript:` 7.0.0`
         - Fixed an issue that could cause cloned Veeam backups for SCVMM Instances to not be created properly :superscript:` 7.0.0`
:Security: - Fixed cache files exposing cloud credentials in plaintext under certain conditions when local credentials (not stored credentials) were used to authenticate the cloud integration :superscript:` 7.0.0`
:VMware: - Any changes to minimum memory values for an image in vCenter are now properly synced over to |morpheus| on the next Cloud sync :superscript:` 7.0.0`
          - Fixed tag values being updated via |morpheus| API being wiped out on the next Cloud sync :superscript:` 7.0.0`


Appliance Updates
=================

:Agents: - Linux Agent: |morpheus| linux agent updated to |linuxagentver| 
         - Windows Agent: |morpheus| Windows Agent updated to |winagentver|
:Appliance: - mysql: Updated default jdbc url used for db cluster connections to include connectTimeout, maxReconnects, queriesBeforeRetrySource and secondsBeforeRetrySource. Default values can be updated in morpheus.rb. :superscript:` 7.0.0`
             - nginx: Logging requests to the ``/ping`` endpoint of |morpheus| app nodes are now disabled by default. Logging can be renabled by adding nginx['ssl_access_ping_log'] = true &
nginx['access_ping_log'] = true to morpheus.rb :superscript:` 7.0.0`
             - Package repo cleanup: The appliance installer has been updated to clean /var/opt/morpheus/package-repos/ directory after package install when it is larger than 5GB.  The current |morpheus| package repo files will be added during reconfigure or supplemental package install
             - SLES 15 FIPS: - Added a FIPS-compliant |morpheus| installer for SLES 15 :superscript:` 7.0.0`
:Embedded Plugins: - Bluecat: bluecat-plugin updated to v1.1.2
                   - Infoblox: infoblox-plugin updated to v1.2.4
                   - Solarwinds: solarwinds-plugin updated to v1.0.4
                   - phpIPAM: phpipam-plugin updated to v1.1.3
                   - Efficient IP: efficient-ip-plugin updated to v1.1.1
:Node Package: - |morpheus| Node & VM Node Packages updated to |nodePackageVer|