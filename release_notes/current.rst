.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade versions: Rolling: |minRollingUpgradeVer| Non-rolling: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`8.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:Agent: - Linux Agent upgraded to 2.9.2 :superscript:`8.0.1`
:Backups: - When restoring an Instance from backup or restoring to a new Instance, the restore event is shown in the Instance history :superscript:`8.0.1`
:Clusters: - Removed KVM cluster types and the ability to add new hosts to existing KVM clusters :superscript:`8.0.1`
:MVM: - MVM cluster types are disabled and adding new hosts to existing MVM clusters is also disabled. This was a beta feature in |morpheus| 7.x.x, upgrade to |morpheus| 8.x.x to use HPE VM clusters (formerly MVM)
:Roles: - In the Guidance section, Users now only see data for Instances they have access to via the "Instances: List" permission :superscript:`8.0.1`
:Trust - Key Pairs: - Dropdowns to select keypairs now show both the keypair name and fingerprint since keypairs with duplicate names are allowed :superscript:`8.0.1`
:Virtual Images: - Creating a VM from a QCOW image that did not have a ``.qcow`` extension no longer fails :superscript:`8.0.1`


Fixes
=====

:API & CLI: - Fixed 500 errors thrown when creating network routers via |morpheus| CLI :superscript:`8.0.1`
             - Resizing Instances via |morpheus| API now works without including volume details in the payload :superscript:`8.0.1`
             - Retrieving the appliance settings via |morpheus| API now returns all settings which can be updated via the API :superscript:`8.0.1`
             - Updating a multi-Tenant User Role (locked) to have a different default Persona via |morpheus| API is now working properly :superscript:`8.0.1`
             - Zone (Cloud) Name and Code values are now included with calls to ``/api/billing/zones`` even after the Zone (Cloud) has been deleted :superscript:`8.0.1`
:Catalog: - Assigning static IP addresses to Catalog Instances is now working properly rather than assigning the next available IP address in the pool :superscript:`8.0.1`
:Clouds: - When adding Clouds, a new help text is included for Cloud URL fields warning that http URLs are insecure and not recommended :superscript:`8.0.1`
:Code: - Fixed files inside subfolders within the repository folder structure not reloading properly after switching branches :superscript:`8.0.1`
:Domains: - Certain legal symbol characters in passwords will no longer cause problems when provisioning Windows and joining an Active Directory domain :superscript:`8.0.1`
:Executions: - Some additional execution history is now shown in the History tab of the Instance detail :superscript:`8.0.1`
:Google Cloud: - GCP Clouds now sync the correct Plans when the Cloud's region scoping is updated :superscript:`8.0.1`
:Guidance: - Guidance will still be generated when Tenant scoping is later changed on a Cloud :superscript:`8.0.1`
:Hosts: - When editing a Windows VM, we no longer default the RPC Host port to 22 and instead default to 5985 when |morpheus| knows the OS type :superscript:`8.0.1`
:Import/Export: - The "Export to Repository" modal now properly refreshes the GIT REF field when a new repository is selected :superscript:`8.0.1`
:Instances: - Attempting to reduce disk size through a reconfigure, which is not allowed, no longer adds a "null" entry in the Instance history :superscript:`8.0.1`
             - Fixed an issue with reconfigure caused by provisioning the Instance using a network group, which is then assigned to a new network outside the group prior to the reconfigure attempt :superscript:`8.0.1`
             - Removing a node from an Instance now creates an entry in the Instance history tab :superscript:`8.0.1`
             - The "Start" action from the Instances action menu is now grayed out during the initial Instance deployment :superscript:`8.0.1`
             - When converting to managed, Plans with an incompatible "cores per socket" value are no longer shown :superscript:`8.0.1`
:Kubernetes: - Fixed provision failures with some Kubernetes versions with Azure AKS clusters :superscript:`8.0.1`
              - Scale options are removed from the provisioning wizard for Kubernetes Instances as they do not apply to those Instance types :superscript:`8.0.1`
:Morpheus IP Pools: - Fixed IP Pool ranges being duplicated when editing a pool with a range that is already in use :superscript:`8.0.1`
:Nutanix Prism Central: - Fixed volumes synced from Prism Central displaying in the wrong order :superscript:`8.0.1`
:Oracle Cloud: - Fixed Edit Cloud modal not launching if the integration is unreachable :superscript:`8.0.1`
:Power Scheduling: - Power Schedules will no longer set Instances back from a status of pending reconfigure approval to normal running :superscript:`8.0.1`
                  - When Instances are in a stopping state (in the process of being stopped), power schedules will not attempt to start them :superscript:`8.0.1`
:Provisioning: - Fixed the Instance provisioning wizard breaking if the port input field is selected in but not filled out :superscript:`8.0.1`
:Resource Pools: - Improved auditing for deleted Resource Pools by making it clearer in logs which Resource Pool was deleted :superscript:`8.0.1`
:Security: - When editing credentials in the Trust section, secret values are now masked in the network response as they are in the UI :superscript:`8.0.1`
:Terraform: - Fixed potential for crash related to the in-built HCL parser :superscript:`8.0.1`
             - Terraform Input labels can now wrap when long enough instead of over-setting the available space in the UI :superscript:`8.0.1`
:VMware: - Datastore maintentance mode is now synced into |morpheus|. Unavailable datastores will appear as offline and will not be selectable as provisioning targets :superscript:`8.0.1`
          - Made more network interface data available on Instance and server variables during Provision and Post Provision Workflow phases to improve scripting capability :superscript:`8.0.1`
          - When a Cloud is scoped to one Resource Pool and that Resource Pool is deleted in VMware, |morpheus| will no longer sync VMs from another available Resource Pool :superscript:`8.0.1`
          - When new top level folders are discovered in a vCenter Cloud, they are now always assigned to the |mastertenant| :superscript:`8.0.1`
:Workflows: - The platform check ensuring Workflows only run against compatible platforms now works properly when multiple Instances are selected :superscript:`8.0.1`

Appliance & Agent Updates
=========================

:Agent: - Linux agent updated to v2.9.2 :superscript:`8.0.1`
:Node & VM Node Packages: - Updated to v3.2.31 with v2.9.2 linux agent :superscript:`8.0.0`