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

:Bare Metal: - The modal for adding bare metal hosts no longer shows common fields from other modals which don't apply to bare metal :superscript:`8.0.3`
:Kubernetes: - Added default Kubernetes 1.32 cluster layouts for all supported Cloud types :superscript:`8.0.3`
:ServiceNow: - All usage of the old ServiceNow logo within the product have been updated :superscript:`8.0.3`
:VDI Gateways: - VDI gateway services will now utilize an overriding Cloud plugin (if present) rather than using an embedded Cloud plugin :superscript:`8.0.3`


Fixes
=====

:API & CLI: - API calls to restart deployments to Kubernetes clusters are now working properly :superscript:`8.0.3`
             - Fixed failures when calling restart or delete actions against StatefulSets in Kubernetes clusters :superscript:`8.0.3`
             - Fixed results from the ``/instances/stats`` API endpoint to include only statistics from Instances the user can access :superscript:`8.0.3`
:Ansible Tower: - Fixed an issue where hosts could be added to inventory under a renamed group rather than a newly created group :superscript:`8.0.3`
:Azure: - Fixed Azure backups not being successfully created under certain configurations :superscript:`8.0.3`
         - Fixed missing Azure storage price sets :superscript:`8.0.3`
         - Resize actions that require reboot will now warn the user the action will require a restart. Resize actions that do not require a restart will not include such a warning prior to being executed :superscript:`8.0.3`
:Clouds: - When setting the "Disk Encryption" configuration to use encryption sets and saving before selecting an encryption set, the modal no longer locks up :superscript:`8.0.3`
:Kubernetes: - Restarting an Instance which is representative of a workload running on a Kubernetes cluster no longer creates duplicate containers :superscript:`8.0.3`
:NSX: - Fixed NSX router route IDs being incremented after the first refresh is performed :superscript:`8.0.3`
       - When creating network segments in |morpheus|, we now perform a network refresh immediately to make the new network usable right away rather than following the next scheduled network sync :superscript:`8.0.3`
:OpenStack: - Fixed an issue that prevented assignment of renamed OpenStack Security Groups to Instances :superscript:`8.0.3`
:PowerVC: - Fixed an issue with reconfiguring PowerVC Instances that didn't include resizing disks :superscript:`8.0.3`
:Tasks: - Fixed Tasks designed for specific versions of Powershell being incorrectly run against the default version under certain configurations :superscript:`8.0.3`
:Usage: - Container usage is now properly restarted for VMware workloads even when a reconfigure does not require a reboot :superscript:`8.0.3`
:Workflows: - When Workflows are renamed, the name is now updating as expected within any pre-existing Nested Workflow-type Tasks :superscript:`8.0.3`
:vCloud Director: - Fixed provisioning issues that could arise from integrating vCD Clouds with the system provider user :superscript:`8.0.3`

=========================
Appliance & Agent Updates
=========================

:Linux Agent: - |morpheus| linux agnet updated to v2.9.3 :superscript:`8.0.3`
:Node Packages: - Updated to v3.2.33 with |morpheus| linux agent v2.9.3 :superscript:`8.0.3`
