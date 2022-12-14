.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. important:: |morpheus| |morphver| requires Morpheus Worker |workerVer|. Please upgrade any existing Morpheus Workers to the |workerVer| Worker package to ensure compatibility with Morpheus |morphver|.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - Added an API endpoint to restart hosts, similar to how Instances, containers, and other constructs could be restarted :superscript:`5.4.13`
             - Roles administration via |morpheus| API and CLI now allows for a "User" level permission for many Instance permissions. This was added to |morpheus| UI in 5.5.2
             - |morpheus| API and CLI now support CRUD actions for auto scaling thresholds and for setting thresholds on Instances in the same way as can be done from |morpheus| UI :superscript:`5.4.13`
:Clone: - Selecting "Clone to Image" for a VM in an Instance containing multiple VMs now only runs the clone process for the one selected VM :superscript:`5.4.13`
:Currency: - Added support for Russian Rubles (RUB) with |morpheus| currency and costing features :superscript:`5.4.13`
:Google Cloud (GCP): - |morpheus| now supports syncing existing VMs with custom plans (non-static vCPU and memory configurations) and provisioning Instances with custom plans
:NSX-T: - Added |morpheus| API endpoints for NSX-T network server group CRUD functionality :superscript:`5.4.13`
:Plugins: - Plugin is now available (share.morpheusdata.com) which matches the functionality offered by the Rubrik integration which previously was enabled in |morpheus| by default
:UI: - UI translations for Japanese and Polish have been completed and added to the product :superscript:`5.4.13`
:vCloud Director: - When a Cluster is provisioned to a vCloud Director Cloud, each host in the Cluster will be provisioned to the same vApp. Previously, each host was provisioned to its own vApp. :superscript:`5.4.135.4.1`


Fixes
=====

:API & CLI: - Fixed an issue that caused updates to IP Pool ranges to create duplicate ranges rather than updating the existing range when updated through |morpheus| API :superscript:`5.4.13`
             - Templates can now be applied to Kubernetes clusters via |morpheus| API and CLI :superscript:`5.4.13`
:Agent: - Fixed an issue that caused non-ASCII characters in the Cloud or Group name to break the |morpheus| Agent install script :superscript:`5.4.13`
:Ansible: - Fixed an issue which caused Ansible inventory files not to be parsed correctly when SSH passwords contain spaces (which should be valid despite being uncommonly used) :superscript:`5.4.13`
:Automation Execute Schedules: - Daylight Saving considerations are now taken into account when |morpheus| computes and displays a "Next Run" time for a Job :superscript:`5.4.13`
:Blueprints: - OpenStack availability zone and security group configurations are now being retained correctly after editing an resaving an App Blueprint :superscript:`5.4.13`
:Clusters: - Fixed an issue that prevented services (|InfClu| > Network tab > Services tab) from being deleted (failed with 500 error) :superscript:`5.4.13`
:Credentials: - Oauth credential sets can now be added (|InfTru|) even with very long tokens :superscript:`5.4.13`
:Cypher: - Fixed an issue that prevented Cypher entries stored in the |mastertenant| from being accessible to Subtenants even when they were used in publicly-shared constructs (such as a Workflow) :superscript:`5.4.13`
:Google Cloud (GCP): - Images for all GCP projects are now displayed when provisioning the Google Cloud Instance type. Previously only images associated with the selected project were usable but GCP itself had no such restriction :superscript:`5.4.13`
:Instances: - Fixed an issue that could cause the wrong volume to be resized during reconfigure under specific plan settings :superscript:`5.4.13`
:Integrations: - Updated required fields for several integration types to disallow integration creation if the field is not filled :superscript:`5.4.13`
:Load Balancers: - Instance and App provisioning wizards will now allow users to select an Amazon ALB when it's in the same availability zone as the Instance :superscript:`5.4.13`
                  - Removing a node from an Instance (either manually or through auto scale-down) will now correctly update F5 load balancer configuration :superscript:`5.4.13`
:NSX-T: - NSX-T firewall groups and rules created in the NSX-T console are now successfully synced back to |morpheus| :superscript:`5.4.13`
:Network IP Pools: - The permissions modal for network pools associated with integrated IPAM solutions (Networks > Integrations > Selected IPAM integration > Network Pools > MORE > Permissions) now pops up when clicked as it should :superscript:`5.4.13`
:Node Types: - Fixed an issue that caused a failure in saving edits to Node Types when existing Instances had already been provisioned from the Node Type :superscript:`5.4.13`
:Nutanix: - Fixed an issue that caused Nutanix host reconfigure to fail :superscript:`5.4.13`
:Open Telekom Cloud: - Fixed an issue that caused OTC host reconfigure to fail :superscript:`5.4.13`
:OpenStack: - Fixed an issue that caused Instance statuses to be reported as unknown when a Subtenant user provisions to a privately-assigned Resource Pool with inventory turned off for the Cloud :superscript:`5.4.13`
             - Fixed an issue that caused Octavia-related errors to appear in appliance logs even when Octavia was no longer integrated :superscript:`5.4.13`
             - Fixed an issue that caused reconfigure to fail for OpenStack VMs :superscript:`5.4.13`
             - Fixed an issue that caused some Resource Pools to not appear as provisioning targets even when the Cloud was scoped for all Projects and sufficient access was granted to the Resource Pools :superscript:`5.4.13`
:Plans and Pricing: - Updating Subtenant Group permissions on Service Plans via |morpheus| API and CLI is now working properly
:Reports: - Fixed a display issue for the number of cores on the workload summary report for Instances provisioned as having a certain number of millicores rather than cores :superscript:`5.4.13`
:Rubrik: - Fixed an issue that could cause deletion of Rubrik backups to fail
:Security Groups: - Security Groups created in |morpheus| are now available for provisioning immediately. Previously they became available after the next Cloud sync (approximately five minutes, by default) :superscript:`5.4.13`
:Security: - Fixed an issue that could cause another user's API token to be revealed in API return payload :superscript:`5.4.13`
:Tenants: - Fixed an issue that prevented Tenant deletion when provisioned catalog items were present :superscript:`5.4.13`
:UI: - Fixed an issue that occurred when using pre-defined date range filters (like "Today") on certain pages when the web browser language was set to Korean :superscript:`5.4.13`
      - Removed duplicated Chinese locales from the Default Locale setting within User Settings :superscript:`5.4.13`
:UpCloud: - Fixed an issue that caused UpCloud host reconfigure to fail :superscript:`5.4.13`
:Users: - Fixed an issue that prevented deleting a user which had previously provisioned a Kubernetes cluster :superscript:`5.4.13`
:VMware: - Disk increases for VMs using a VSAN datastore no longer stop and start the VM to complete this process (which was not required) :superscript:`5.4.13`
:Workflows: - Fixed an issue that prevented Task results from being chained into the next Task of the Workflow when Operational Workflows were run against a VM context :superscript:`5.4.13`
