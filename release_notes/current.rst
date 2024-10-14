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

:MVM: - Added capability to schedule full synthetic backups for MVM workloads in addition to the incremental backups that were already supported for all workload types. See Backups documentation for complete details
       - When reconfiguring MVM Instances, users now have the option to select a different datastore which will migrate the disk to the new datastore
:Plugins: - Added a new concept of a generic-type integration which can respond to events in the Cluster lifecycle. See developer documentation (developer.morpheusdata.com) for more information
:Roles: - Certain action controls on State tabs are no longer accessible when the "Provisioning: State" Role permission is set to Read


Fixes
=====

:API & CLI: - Changing an Instance's Group association via |morpheus| API now results in the associated servers having updated Group associations as well 
             - When creating an Instance via |morpheus| API and specifying a hostname, the resulting workload now has the correct hostname applied
             - |morpheus| is no longer duplicating the ``zone`` field in the response payload from the ``/api/instances/{id}`` endpoint
:AVI Load Balancer: - Fixed an issue updating the virtual server VIP address for AVI load balancers
                  - The VIP object is now properly deleted when a virtual server is deleted
:Blueprints: - When Terraform App Blueprints are sourced from a specific branch of a Git repository, updated configurations are now taken when the branch is updated and state is newly applied to any deployed Apps
:Catalog: - Fixed Config-phase Tasks not running if present on Provisioning Workflows tied to Catalog Items
           - Fixed a scenario where users with read-only access to a Group could provision to it when deploying a Catalog item
           - Fixed an issue with the Disk field reloading properly when a Cloud selection was changed on Form-based Catalog items 
:Clone: - Fixed clone failures that could result when required Input values were changed between when the original Instance was provisioned and when the clone was attempted
:Hosts: - When moving a managed server to a different Tenant, the ``provision_site_id`` value is also now updated to match the changed Group 
:Instances: - Fixed an issue with detecting and updating workload power state changes from outside of |morpheus| for certain Cloud types
             - Fixed an issue with updating Group selection for Instances after moving to a different Cloud using Change Cloud functionality
             - The ``max_storage`` and ``max_memory`` are now updating on the ``compute_capacity_info`` after a reconfigure (such as to add or remove storage or memory)
             - Updated the logic for Instance-level and server-level metrics graphs to ensure they are in alignment
             - When an Instance is locked, the "Remove from Control" action is no longer clickable. Previously it could be clicked but gave no indication why the action did not take place
             - When viewing the Resources tab on an Instance detail, the option to remove individual nodes is now given
:MVM: - Removed some fields that should not have been present on the Edit modal for RDB datastores associated with MVM clusters
       - When moving disks associated with MVM Instances (such as when reconfiguring to move a disk to a different datastore), |morpheus| no longer uses a different naming pattern which resulted in renamed disks
:Node Types: - Fixed errors in logs when Node Types with set environment variables were deleted
:Nutanix Prism Element: - |morpheus| no longer tries to double register host records to the DNS service when provisioning to Nutanix Prism Central using a pool from an IPAM integration
:Provisioning: - You can now remove a load balancer when you set a Load Balancer configuration on the Automation tab of the Instance provisioning wizard, advance to the Review tab, and then return
:Security: - Added validation and sanitization to Role names to prevent a potential XSS attack vector
            - Added validation and sanitization to Tenant name values to prevent a potential vector for an HTML injection attack
            - Removed access to the ``admin/settings/settingsInfo`` endpoint for users who do not have "Admin: Settings" permissions
:Tasks: - Reading out Cypher values in Ansible Task command options is now working
:Terraform: - Added improvements to the |morpheus| HCL parser
:Virtual Images: - Fixed an issue that allowed Subtenant users to delete Virtual Images shared down from the |mastertenant| using |morpheus| API


Appliance & Agent Updates
=========================

:Appliance: - Improved logic that cleared refresh tokens after clearing or regenerating which previously could create a situation where the ``refresh_token`` table could grow very large


Appliance & Agent Updates
=========================

:Agent Node Packages: - |morpheus| linux agent updated to v2.8.2 with improved reconnection after disconnects
                      - |morpheus| node & vm node packages updated to v3.2.29 with linux agent v2.8.2
:Embedded Plugins: - Efficient IP plugin updated to v1.2.5 with increased concurrency to improve outcomes with highly scaled Instances
