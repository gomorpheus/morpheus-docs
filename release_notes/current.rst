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

:Amazon: - When provisioning to Amazon Cloud targets, added an option for "No EIP" configuration in the "PUBLIC IP" field in addition to "Assign EIP" and "Subnet Default" options
:Catalog: - Added Debian 12 default catalog Layouts for most supported Cloud types
           - Disabled default Layouts for CentOS 7 as it has reached end of life
           - Disabled default Layouts for Debian 10 as it has reached end of life
:Infoblox: - Added "Host Only" option to create only a host record in Infoblox. Added "ALTERNATE DNS METHOD" option where DNS will create Host, A record and PTR record for the domain selected during provisioning
:Kubernetes: - Updated some packages to allow for skipping confirmation of results which should significantly improve provisioning time for Kubernetes clusters
:Nutanix Prism Central: - Added "VMM API VERSION" configuration for Nutanix Prism Central Clouds. This allows the user to select which VMM API versions their environment will support as |morpheus| cannot auto-detect this and endpoint support differs between versions
:Packages: - Packages (|AdmIntPac|) can now be deleted from the packages list page. Deleting packages will not clean up all of the items imported by uploading the package but the delete confirmation modal will show the user the items added with the package
:Plugins: - Added a generic integration provider plugin which allows users to develop plugin types which are outside of the specific provider types. See developer.morpheusdata.com for more details
           - Added a new plugin type for custom analytics pages. This is similar to custom reports but adds new analytics types to the analytics list page (|OpeAna|)
           - Added warning in logs when a plugin is uploaded with a duplicate provider code


Fixes
=====

:Ansible Tower: - Terraform secrets are no longer exposed as Ansible Tower Extravars in state after execution of Ansible Tower jobs
:Azure: - Fixed SQL servers being discovered along with their associated databases as Instances even when the Resource Pool (Resource Group) they lived inside was configured to not discover resources
:Blueprints: - When Terraform App Blueprints are sourced from a specific branch of a Git repository, updated configurations are now taken when the branch is updated and state is newly applied to any deployed Apps
:Catalog: - Fixed specific scenarios where Workflow-type Catalog items targeted to Server or Instance contexts could ignore Role Group permissions and allow the Workflow to be run against any Instance or server
           - Hitting return within Text-type Inputs on Catalog order pages will no longer submit the form and return a 403 error under certain conditions
:Clusters: - Cleaned up a few spots in the UI that did not display updated memory configurations if MKS worker nodes were reconfigured to add memory
:Forms: - Fixed a situation where a bad Input default value could make a Form uneditable (modal closes immediately on edit attempt)
         - Integers can now be used as intended in Text Array-type Inputs on Forms
:Google Cloud: - Updated GCP pricing logic to improve some scenarios where |morpheus| and GCP pricing were not aligning, including when pricing is updated on Plan change
:Health: - When viewing the health summary page at ``/admin/health/live``, the health status icon for "Storage" now displays properly
:Hosts: - When performing a Change Cloud operation on a server, |morpheus| now detects if a target VM is managed and simply raises an error in logs rather than creating a duplicate VM on the target Cloud
:Identity Sources: - |morpheus| can now detect when SAML identity sources send roles in multiple attributes to properly map all applicable Roles on the |morpheus| side
:Import/Export: - Fixed failing imports of code repositories which contain Ansible Tower integrations
:Kubernetes: - Added pagination to the container list on the host detail page. Previously, in certain cases, very large lists of discovered containers could cause poor performance
              - External Kubernetes clusters running on VMware and onboarded into |morpheus| now show correct power state
:Network: - For networks containing IPv4 and IPv6 pools and shared with Subtenants, the Subtenant no longer sees the IPv4 gateway address in the IPv6 gateway field
:Nutanix Prism Central: - When attempting to delete a VM, |morpheus| now checks and waits for any pending actions which would prevent the delete action from succeeding
:Nutanix Prism Element: - Fixed Windows servers deployed to Nutanix Prism Element Clouds not taking the timezone configured on the Cloud
                  - Images synced from Nutanix Prism Element Clouds are now selectable as Virtual Images on Node Types
:Nutanix: - Additional NICs added to VMs in |morpheus| will no longer come back after subsequent Cloud syncs if they are deleted
:OpenStack: - The Service Plan access setting for Resource Pools now works properly for OpenStack Cloud targets. The available Resource Pools are filtered correctly based on the selected Service Plan
:Terraform: - Deploying a Windows Instance using Terraform with the |morpheus| variable to install the |morpheus| Agent now results in successful Agent installation
:Trust: - Trust integrations can no longer be saved without validation. When saving, the presence of an API URL and successful authentication are confirmed prior to saving
:XenServer: - Fixed Instance power status displaying as "Unknown" in UI while Instances were up in a Ready state
             - Improved logic detecting external CIFS vs NFS datastores to ensure the correct type is used for ISO storage


Appliance & Agent Updates
=========================

:Agnet Node Packages: - |morpheus| linux agent updated to v2.7.1
                      - |morpheus| node & vm node packages updated to v3.2.26 with linux agent v2.7.1
:Embedded Plugins: - bigip-plugin updated to v1.3.4
                   - digital-ocean-plugin updated to v1.3.3
                   - infoblox-plugin updsated to v1.4.0
                   - XCP-ng plugin updated to v1.0.1


