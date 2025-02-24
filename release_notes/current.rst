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

:API & CLI: - When creating Instance snapshots via |morpheus| API, the response now includes process IDs for the triggered snapshots
:Bare Metal: - The modal for adding bare metal hosts no longer shows common fields from other modals which don't apply to bare metal :superscript:`7.0.11`
:HPE VM: - Certain actions will no longer update UUIDs for VM storage volumes (moving VM to a different host, changing disk datastores, etc)
          - HPE VM Clusters now support network groups
          - Provisioning to HPE VM Clusters now sets a default "Auto Datastore" selection. Users may manually select a datastore or may leave the default automatic configuration
:Kubernetes: - Added default Kubernetes 1.32 cluster layouts for all supported Cloud types :superscript:`7.0.11`
:ServiceNow: - All usage of the old ServiceNow logo within the product have been updated :superscript:`7.0.11`
:VDI Gateways: - VDI gateway services will now utilize an overriding Cloud plugin (if present) rather than using an embedded Cloud plugin :superscript:`7.0.11`
:Virtual Images: - When importing images from existing VMs, future attempts to provision from that Virtual Image will automatically set disks on the provisioning wizard to a minimally viable configuration (Ex. three disks in appropriate minimum sizes)


Fixes
=====

:API & CLI: - API calls to restart deployments to Kubernetes clusters are now working properly :superscript:`7.0.11`
             - Fixed calls to return Task executions failing with certain license types which shouldn't have restricted it
             - Fixed failures when calling restart or delete actions against StatefulSets in Kubernetes clusters :superscript:`7.0.11`
             - Fixed results from the ``/instances/stats`` API endpoint to include only statistics from Instances the user can access :superscript:`7.0.11`
:Ansible Tower: - Fixed an issue where hosts could be added to inventory under a renamed group rather than a newly created group :superscript:`7.0.11`
:Azure: - Fixed Azure backups not being successfully created under certain configurations :superscript:`7.0.11`
         - Fixed missing Azure storage price sets :superscript:`7.0.11`
         - Resize actions that require reboot will now warn the user the action will require a restart. Resize actions that do not require a restart will not include such a warning prior to being executed :superscript:`7.0.11`
:Clouds: - When setting the "Disk Encryption" configuration to use encryption sets and saving before selecting an encryption set, the modal no longer locks up :superscript:`7.0.11`
:Kubernetes: - Restarting an Instance which is representative of a workload running on a Kubernetes cluster no longer creates duplicate containers :superscript:`7.0.11`
:NSX: - Fixed NSX router route IDs being incremented after the first refresh is performed :superscript:`7.0.11`
       - When creating network segments in |morpheus|, we now perform a network refresh immediately to make the new network usable right away rather than following the next scheduled network sync :superscript:`7.0.11`
:OpenStack: - Fixed an issue that prevented assignment of renamed OpenStack Security Groups to Instances :superscript:`7.0.11`
:PowerVC: - Fixed an issue with reconfiguring PowerVC Instances that didn't include resizing disks :superscript:`7.0.11`
:Tasks: - Fixed Tasks designed for specific versions of Powershell being incorrectly run against the default version under certain configurations :superscript:`7.0.11`
:Usage: - Container usage is now properly restarted for VMware workloads even when a reconfigure does not require a reboot :superscript:`7.0.11`
:User Settings: - Fixed a small styling issue on the button to upload an avatar image on the User Settings page
:Whitelabel: - Footer logos no longer fail to display when whitelabel is enabled
:Workflows: - When Workflows are renamed, the name is now updating as expected within any pre-existing Nested Workflow-type Tasks :superscript:`7.0.11`
:vCloud Director: - Fixed provisioning issues that could arise from integrating vCD Clouds with the system provider user :superscript:`7.0.11`

=========================
Appliance & Agent Updates
=========================

:Linux Agent: - |morpheus| linux agent updated to v2.9.3 :superscript:`7.0.11`
:Node Packages: - Updated to v3.2.33 with |morpheus| linux agent v2.9.3 :superscript:`7.0.11`
