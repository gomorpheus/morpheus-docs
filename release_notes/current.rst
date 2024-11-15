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

:API & CLI: - Added the ability to add and remove integrations associated with a Cluster via |morpheus| API and CLI :superscript:`8.0.0`
             - Added the ability to set ``autoRecoverPowerState`` via |morpheus| API as can already be set in UI :superscript:`8.0.0`
             - It's now possible to cancel running Tasks through |morpheus| API and CLI :superscript:`8.0.0`
             - Retrying failed Tasks is now supported through |morpheus| API and CLI in addition to the existing support via |morpheus| UI :superscript:`8.0.0`
             - |morpheus| API and CLI now support working with MVM Cluster datastores :superscript:`8.0.0`
:Azure: - Removed the option for unmanaged disks from Azure provisioning as they are being retired in the near future :superscript:`8.0.0`
:Backups: - Executions for the same backup can no longer be run simultaneously. They are now queued and run in order by their requested time :superscript:`8.0.0`
:Instances: - The Instance history tab now includes backup execution history :superscript:`8.0.0`
:Kubernetes: - Added default Cluster Layouts for Kubernetes 1.31, including HA layouts. Default Kubernetes 1.28 Cluster Layouts have been disabled :superscript:`8.0.0`
:Login: - Removed the "Remember Me" checkbox from the username and password login screen :superscript:`8.0.0`
:MVM: - Added support for retrieving limited monitoring statistics from MVM VMs when the |morpheus| Agent is not installed :superscript:`8.0.0`
:Provisioning: - For Instance Types that require selecting an image (VMware, etc), the Image field is now a typeahead field as the dropdown menus could become quite large :superscript:`8.0.0`
:Virtual Images: - In addition to URL sourcing, Virtual Images can also be sourced by specifying a path within a configured storage bucket :superscript:`8.0.0`


Fixes
=====

:API & CLI: - When resizing multi-VM Instances using |morpheus| CLI, fixed the resize process adding multiple network interfaces even when not specified in the resize :superscript:`8.0.0`
:Agent: - Fixed Windows Agent crashes when Powershell Tasks prompt for ``stdin`` :superscript:`8.0.0`
:Amazon: - Fixed an issue where AWS Clouds scoped to "Global (Costing Aggregator Only)" region could get stuck in the "Initializing" phase for an extremely long period on initial integration :superscript:`8.0.0`
:Blueprints: - When the Layout field is locked and hidden to the user when provisioning a certain App, the Version field is also automatically locked as it's purpose is to filter Layouts :superscript:`8.0.0`
:Catalog: - Fixed a specific case where setting tags (metadata) using |morpheus| variables could break certain custom network configurations :superscript:`8.0.0`
           - For Blueprint-type Catalog items, added a warning to the UI letting the user know that they cannot re-enter the Blueprint configuration wizard after the config JSON has been set into the modal and altered :superscript:`8.0.0`
           - Improved performance in situations where a user has an extremely large catalog order history :superscript:`8.0.0`
           - When creating a Catalog item and entering invalid JSON (such as when sliding an Input into the Config area before configuring the Instance), the UI now gives proper warning rather than the "Configure" button simply not working :superscript:`8.0.0`
:Clusters: - Clicking the "Type" heading on the clusters list page to sort the table by cluster type no longer breaks the table :superscript:`8.0.0`
:Commvault: - When creating a new Instance and selecting an existing Commvault Job for backup, the backup no longer continues to exist in Commvault after the VM is deleted :superscript:`8.0.0`
:Hyper-V: - Fixed Instances provisioned from Gen 1 VHDX images showing as Gen 2 VHDX in the UI :superscript:`8.0.0`
:Inputs: - When saving Inputs with Verify Pattern (Regex) strings, the Regex itself is now validated when the form is saved :superscript:`8.0.0`
:Nutanix Prism Central: - Fixed Windows VMs not unmounting ISOs following provisioning :superscript:`8.0.0`
:Provisioning: - Windows domain joins will no longer fail if the domain join specifies a new computername which is the same as the current computername :superscript:`8.0.0`
:SCVMM: - Marking the "VM TOOLS INSTALLED?" checkbox on the Virtual Image will no longer prevent SCVMM Instances from attempting a domain join :superscript:`8.0.0`
:Security: - Minor security related improvements :superscript:`8.0.0`
:Setup: - On first time setup through either the wizard or the API, added an option to enter a license key :superscript:`8.0.0`
:Startup: - On first ui startup after upgrade, |morpheus| will normalize all IPv6 records within |morpheus|-type pools. There will be a warning in appliance logs warning how many records will be normalized. This takes between 5-15 minutes per 1m records :superscript:`8.0.0`
          - Updated the AccountUsage table in the appliance database to accept LONGTEXT data type to prevent data from oversetting the table in specific scenarios. Note that this schema change will take time for databases with large numbers of account usage records :superscript:`8.0.0`
:Terraform: - Fixed 500 errors thrown when editing Inputs on Terraform Apps without re-entering any Password inputs :superscript:`8.0.0` :superscript:`8.0.0`
:VMware: - Fixed an issue where |morpheus| could encounter a foreign key constraint error during Cloud refresh if certain changes were made to storage controllers from the VMware side :superscript:`8.0.0`
          - Fixed snapshots temporarily disappearing from UI when taken during Cloud sync :superscript:`8.0.0`
:Virtual Images: - For Virtual Images which are not active (that is, not yet fully synced or uploaded), |morpheus| now filters them out of the image select list for Instance Types which include a direct image selection :superscript:`8.0.0`
:vCloud Director: - Fixed failing Powershell executions during provisioning due to a mis-set RPC port :superscript:`8.0.0`
                  - Synced RHEL 9 images no longer revert to "other 64-bit" OS type after Cloud sync :superscript:`8.0.0`


Appliance & Agent Updates
=========================

:Agent: - Linux agent updated to v2.9.2 :superscript:`8.0.0`
        - Windows agent updated to v2.6.1.0 :superscript:`8.0.0`
:mvm console: - mvm console added to appliance app repository :superscript:`8.0.0`
:Node & VM Node Packages: - Updated to v3.2.30 with updated linux and windows agents :superscript:`8.0.0`
