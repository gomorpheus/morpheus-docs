.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade versions: Rolling: |minRollingUpgradeVer| Non-rolling: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`7.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

.. _Release Notes:

*************************
|morphver| Release Notes
*************************

New Features
============

:Backups: - When restoring an Instance from backup or restoring to a new Instance, the restore event is shown in the Instance history :superscript:`7.0.9`
:Clusters: - Removed KVM cluster types and the ability to add new hosts to existing KVM clusters :superscript:`7.0.9`
:Roles: - In the Guidance section, Users now only see data for Instances they have access to via the "Instances: List" permission :superscript:`7.0.9`
:Trust - Key Pairs: - Dropdowns to select keypairs now show both the keypair name and fingerprint since keypairs with duplicate names are allowed :superscript:`7.0.9`
:Virtual Images: - Creating a VM from a QCOW image that did not have a ``.qcow`` extension no longer fails :superscript:`7.0.9`


Fixes
=====

:API & CLI: - Fixed 500 errors thrown when creating network routers via |morpheus| CLI :superscript:`7.0.9`
             - Resizing Instances via |morpheus| API now works without including volume details in the payload :superscript:`7.0.9`
             - Retrieving the appliance settings via |morpheus| API now returns all settings which can be updated via the API :superscript:`7.0.9`
             - Updating a multi-Tenant User Role (locked) to have a different default Persona via |morpheus| API is now working properly :superscript:`7.0.9`
             - Zone (Cloud) Name and Code values are now included with calls to ``/api/billing/zones`` even after the Zone (Cloud) has been deleted :superscript:`7.0.9`
:Catalog: - Assigning static IP addresses to Catalog Instances is now working properly rather than assigning the next available IP address in the pool :superscript:`7.0.9`
:Clouds: - When adding Clouds, a new help text is included for Cloud URL fields warning that http URLs are insecure and not recommended :superscript:`7.0.9`
:Code: - Fixed files inside subfolders within the repository folder structure not reloading properly after switching branches :superscript:`7.0.9`
:Domains: - Certain legal symbol characters in passwords will no longer cause problems when provisioning Windows and joining an Active Directory domain :superscript:`7.0.9`
:Executions: - Some additional execution history is now shown in the History tab of the Instance detail :superscript:`7.0.9`
:Google Cloud: - GCP Clouds now sync the correct Plans when the Cloud's region scoping is updated :superscript:`7.0.9`
:Guidance: - Guidance will still be generated when Tenant scoping is later changed on a Cloud :superscript:`7.0.9`
:Hosts: - When editing a Windows VM, we no longer default the RPC Host port to 22 and instead default to 5985 when |morpheus| knows the OS type :superscript:`7.0.9`
:Import/Export: - The "Export to Repository" modal now properly refreshes the GIT REF field when a new repository is selected :superscript:`7.0.9`
:Instances: - Attempting to reduce disk size through a reconfigure, which is not allowed, no longer adds a "null" entry in the Instance history :superscript:`7.0.9`
             - Fixed an issue with reconfigure caused by provisioning the Instance using a network group, which is then assigned to a new network outside the group prior to the reconfigure attempt :superscript:`7.0.9`
             - Removing a node from an Instance now creates an entry in the Instance history tab :superscript:`7.0.9`
             - The "Start" action from the Instances action menu is now grayed out during the initial Instance deployment :superscript:`7.0.9`
             - When converting to managed, Plans with an incompatible "cores per socket" value are no longer shown :superscript:`7.0.9`
:Kubernetes: - Fixed provision failures with some Kubernetes versions with Azure AKS clusters :superscript:`7.0.9`
              - Scale options are removed from the provisioning wizard for Kubernetes Instances as they do not apply to those Instance types :superscript:`7.0.9`
:Morpheus IP Pools: - Fixed IP Pool ranges being duplicated when editing a pool with a range that is already in use :superscript:`7.0.9`
:Nutanix Prism Central: - Fixed volumes synced from Prism Central displaying in the wrong order :superscript:`7.0.9`
:Oracle Cloud: - Fixed Edit Cloud modal not launching if the integration is unreachable :superscript:`7.0.9`
:Power Scheduling: - Power Schedules will no longer set Instances back from a status of pending reconfigure approval to normal running :superscript:`7.0.9`
                  - When Instances are in a stopping state (in the process of being stopped), power schedules will not attempt to start them :superscript:`7.0.9`
:Provisioning: - Fixed the Instance provisioning wizard breaking if the port input field is selected in but not filled out :superscript:`7.0.9`
:Resource Pools: - Improved auditing for deleted Resource Pools by making it clearer in logs which Resource Pool was deleted :superscript:`7.0.9`
:Security: - When editing credentials in the Trust section, secret values are now masked in the network response as they are in the UI :superscript:`7.0.9`
:Terraform: - Fixed potential for crash related to the in-built HCL parser :superscript:`7.0.9`
             - Terraform Input labels can now wrap when long enough instead of over-setting the available space in the UI :superscript:`7.0.9`
:VMware: - Datastore maintentance mode is now synced into |morpheus|. Unavailable datastores will appear as offline and will not be selectable as provisioning targets :superscript:`7.0.9`
          - Made more network interface data available on Instance and server variables during Provision and Post Provision Workflow phases to improve scripting capability :superscript:`7.0.9`
          - When a Cloud is scoped to one Resource Pool and that Resource Pool is deleted in VMware, |morpheus| will no longer sync VMs from another available Resource Pool :superscript:`7.0.9`
          - When new top level folders are discovered in a vCenter Cloud, they are now always assigned to the |mastertenant| :superscript:`7.0.9`
:Workflows: - The platform check ensuring Workflows only run against compatible platforms now works properly when multiple Instances are selected :superscript:`7.0.9`

Appliance & Agent Updates
=========================

:Agent: - Linux agent updated to v2.9.2 :superscript:`7.0.9`
:Java: Appliance Java updated to v17.0.13+11
:Nginx: Appliance Nginx updated to v1.26.2
:Node & VM Node Packages: - Updated to v3.2.31 with v2.9.2 linux agent :superscript:`7.0.9`
:RabbitMQ: Appliance RabbitMQ updated to v3.13.7, erlang v26.2.5.6
:Tomcat: Appliance Tomcat updated to v9.0.97
