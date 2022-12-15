.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

Release Dates
  - |morphVer|-1 |releasedate|

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - Added API functionality to update the permissions of Ansible Tower>Inventory items :superscript:`5.5.2`
             - Added an API endpoint to restart hosts, similar to how Instances, containers, and other constructs could be restarted :superscript:`5.5.3`
             - |morpheus| API and CLI now support CRUD actions for auto scaling thresholds and for setting thresholds on Instances in the same way as can be done from |morpheus| UI :superscript:`5.5.3`
:Clone: - Selecting "Clone to Image" for a VM in an Instance containing multiple VMs now only runs the clone process for the one selected VM :superscript:`5.5.3`
:Currency: - Added support for Russian Rubles (RUB) with |morpheus| currency and costing features :superscript:`5.5.3`
:NSX-T: - Added |morpheus| API endpoints for NSX-T network server group CRUD functionality :superscript:`5.5.3`
:UI: - UI translations for Japanese and Polish have been completed and added to the product :superscript:`5.5.3`
:vCloud Director: - When a Cluster is provisioned to a vCloud Director Cloud, each host in the Cluster will be provisioned to the same vApp. Previously, each host was provisioned to its own vApp. :superscript:`5.5.35.4.1`


Fixes
=====

:API & CLI: - Fixed an issue that caused the Tenants block not to be returned for some Network objects when calling the Get All Networks endpoint :superscript:`5.5.2`
             - Fixed an issue that caused updates to IP Pool ranges to create duplicate ranges rather than updating the existing range when updated through |morpheus| API :superscript:`5.5.3`
             - Templates can now be applied to Kubernetes clusters via |morpheus| API and CLI :superscript:`5.5.3`
:ARM: - ARM template parameters are now visible in the instance wizard when provisioning a instance type pointing to an ARM template when logged in as a sub-tenant user. :superscript:`5.5.2`
:Agent: - Fixed an issue that caused non-ASCII characters in the Cloud or Group name to break the |morpheus| Agent install script :superscript:`5.5.3`
:Ansible Tower: - Ansible Tower Tasks can now be configured to use the Tenant default inventory whether the |mastertenant| has a default inventory set or not :superscript:`5.5.2`
:Ansible: - Fixed an issue which caused Ansible inventory files not to be parsed correctly when SSH passwords contain spaces (which should be valid despite being uncommonly used) :superscript:`5.5.3`
:Automation Execute Schedules: - Daylight Saving considerations are now taken into account when |morpheus| computes and displays a "Next Run" time for a Job :superscript:`5.5.3`
                  - Fixed UI issues related to plain text cron interpretation shown when creating or editing and Execution Schedule :superscript:`5.5.2`
:Azure: - Fixed an issue which caused Azure Instances created from backup restoration to have incorrect disk type (HDD vs SSD, for example) :superscript:`5.5.2`
:Blueprints: - OpenStack availability zone and security group configurations are now being retained correctly after editing an resaving an App Blueprint :superscript:`5.5.3`
:Clusters: - During cluster provisioning, custom input values are now accessible from the worker nodes and not just the master node
            - Fixed an issue that prevented services (|InfClu| > Network tab > Services tab) from being deleted (failed with 500 error) :superscript:`5.5.3`
            - Removed support for editing tags on clusters which was not working. Tags may still be added at cluster creation time and they are applied to the hosts rather than the cluster. :superscript:`5.5.2`
:Credentials: - Oauth credential sets can now be added (|InfTru|) even with very long tokens :superscript:`5.5.3`
:Cypher: - Fixed an issue that prevented Cypher entries stored in the |mastertenant| from being accessible to Subtenants even when they were used in publicly-shared constructs (such as a Workflow) :superscript:`5.5.3`
:Google Cloud (GCP): - Images for all GCP projects are now displayed when provisioning the Google Cloud Instance type. Previously only images associated with the selected project were usable but GCP itself had no such restriction :superscript:`5.5.3`
:Instances: - Fixed an issue that could cause the wrong volume to be resized during reconfigure under specific plan settings :superscript:`5.5.3`
:Integrations: - Updated required fields for several integration types to disallow integration creation if the field is not filled :superscript:`5.5.3`
:Library: - The set of and order for spec templates and file templates are being retained on node type add and edit/save. :superscript:`5.5.2`
:Load Balancers: - Instance and App provisioning wizards will now allow users to select an Amazon ALB when it's in the same availability zone as the Instance :superscript:`5.5.3`
                  - Removing a node from an Instance (either manually or through auto scale-down) will now correctly update F5 load balancer configuration :superscript:`5.5.3`
:NSX-T: - NSX-T firewall groups and rules created in the NSX-T console are now successfully synced back to |morpheus| :superscript:`5.5.3`
:Network IP Pools: - The permissions modal for network pools associated with integrated IPAM solutions (Networks > Integrations > Selected IPAM integration > Network Pools > MORE > Permissions) now pops up when clicked as it should :superscript:`5.5.3`
:Network: - The Scan Network property has been removed from networks in the UI, API, CLI :superscript:`5.5.2`
:Node Types: - Fixed an issue that caused a failure in saving edits to Node Types when existing Instances had already been provisioned from the Node Type :superscript:`5.5.3`
:Nutanix: - Fixed an issue that caused Nutanix host reconfigure to fail :superscript:`5.5.3`
:Open Telekom Cloud: - Fixed an issue that caused OTC host reconfigure to fail :superscript:`5.5.3`
:OpenStack: - Fixed an issue that caused Instance statuses to be reported as unknown when a Subtenant user provisions to a privately-assigned Resource Pool with inventory turned off for the Cloud :superscript:`5.5.3`
             - Fixed an issue that caused Octavia-related errors to appear in appliance logs even when Octavia was no longer integrated :superscript:`5.5.3`
             - Fixed an issue that caused reconfigure to fail for OpenStack VMs :superscript:`5.5.3`
             - Fixed an issue that caused some Resource Pools to not appear as provisioning targets even when the Cloud was scoped for all Projects and sufficient access was granted to the Resource Pools :superscript:`5.5.3`
:Reports: - Fixed a display issue for the number of cores on the workload summary report for Instances provisioned as having a certain number of millicores rather than cores :superscript:`5.5.3`
           - The instance type and layout for instances are now displayed in the instance cost report and export :superscript:`5.5.2`
:Security Groups: - Security Groups created in |morpheus| are now available for provisioning immediately. Previously they became available after the next Cloud sync (approximately five minutes, by default) :superscript:`5.5.3`
:Security: - Fixed an issue that could cause another user's API token to be revealed in API return payload :superscript:`5.5.3`
            - The csrf token value is no longer being passed to the GET query call on the policies list and instance list pages :superscript:`5.5.2`
:Tenants: - Fixed an issue that prevented Tenant deletion when provisioned catalog items were present :superscript:`5.5.3`
:UI: - Fixed an issue that occurred when using pre-defined date range filters (like "Today") on certain pages when the web browser language was set to Korean :superscript:`5.5.3`
      - Removed duplicated Chinese locales from the Default Locale setting within User Settings :superscript:`5.5.3`
:UpCloud: - Fixed an issue that caused UpCloud host reconfigure to fail :superscript:`5.5.3`
:Users: - Fixed an issue that prevented deleting a user which had previously provisioned a Kubernetes cluster :superscript:`5.5.3`
:VMware: - Disk increases for VMs using a VSAN datastore no longer stop and start the VM to complete this process (which was not required) :superscript:`5.5.3`
          - Fixed a sync error that would occur when updating a VMware Cloud to scope it to a different Resource Pool :superscript:`5.5.2`
:Workflows: - Fixed an issue that prevented Task results from being chained into the next Task of the Workflow when Operational Workflows were run against a VM context :superscript:`5.5.3`
             - Workflows which are attached to Layouts will now be invoked for workloads which are converted from discovered to |morpheus|-managed Instances :superscript:`5.5.2`


Appliance & Agent Updates
=========================

:Appliance: - Appliance Java updated to 11.0.17.8 :superscript:`5.5.2`
             - Elasticsearch Java updated to 17.0.5.8 :superscript:`5.5.2`
             - Updated |morpheus| installer for SUSE 15 SP 2 and 3 to automate some manual steps that were previously required, including uuid-devel repo access and a second reconfigure step :superscript:`5.5.2`
             - |morpheus| installer and reconfigure action will now ignore missing susefirewall2 in SLES15 as it has been deprecated. Previously, workarounds were required if it was not present :superscript:`5.5.2`