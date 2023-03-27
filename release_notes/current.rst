.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:Apps: - A Costing tab has been added to App detail pages to aggregate invoice data specific to the App
:Automation: - Run Tasks, Operational Workflows, or Jobs against a Label target rather than an individual Instance or server. The automation will run against all Instances or servers having the selected label
:Catalog: - Catalog Items can now be configured with an option to allow users to specify a quantity which allows the user to order the Instance, App or Workflow multiple times
:Clouds: - A Costing tab has been added to Cloud detail pages to aggregate invoice data specific to the Cloud
:Hosts: - A Costing tab has been added to server detail pages to aggregate invoice data for the server
:Kubernetes: - Added Kubernetes 1.26 support and added default 1.26 cluster layouts for supported Clouds :superscript:`5.4.16`
:NSX: - Services are now listed in a dropdown vs previous lookup field in the NSX-T distributed firewall rule create/update modals.
:Nutanix: - Custom child networks can now be created from Nutanix type clouds networks.
:Oracle Cloud: - Oracle Clouds now have full tag sync capability similar to other |morpheus| public Cloud integrations (like AWS or Azure). Oracle Cloud is updated with |morpheus| tags on provisioning and two-way tag syncing takes place on each |morpheus| Cloud sync
:Plans and Pricing: - Service Plans can now be configured with a total storage range (limits on the total storage for all disks) and a per-disk storage range (limits on the sizes of each disk)
:Policies: - A new Policy type "Approve Workflow Execute" has been added. The Policy is invoked whenever an Operational Workflow is executed from an Instance or server detail page or directly from the Workflows UI section
:Roles: - New feature permission added - Snapshots: Linked Clones. This controls access to the Create Linked Clone command for Snapshots
:Terraform: - Added Terraform support for OpenStack Clouds
:Workflows: - Added the capability to stop the currently-running Task in a Workflow. This is useful when you wish to stop a long-running Task you know will fail or wish to stop attempting a "retryable" Task. The Workflow is then given a status of "cancelled" in History


Fixes
=====

:API & CLI: - The ``make-managed`` CLI call and underlying API call will now properly set tags on the new managed Instance :superscript:`5.4.16`
:Amazon: - Improved Amazon AWS costing sync to better account for child accounts underneath a management account :superscript:`5.4.16`
:Ansible: - Ansible logs in History detail views are updated to be displayed with more easily legible colors. Using the copy button to grab the whole output also now works better with special characters
:Clouds: - Fixed an issue accessing key/value Cloud profile values
:Costing: - Fixed a few issues related to prices vs costs (cost could be higher than price) and improved the accuracy of MTD and projection costs :superscript:`5.4.16`
:Identity Sources: - The |morpheus| LDAP integration is now compatible with OpenLDAP :superscript:`5.4.16`
:Inputs: - Fixed an issue causing Input values not to be verified against a configured regex validation string if a visibility field was also set on the Input
          - Fixed an issue that caused reads from multi-select typeahead Inputs to return a list containing a null item at the start :superscript:`5.4.16`
:Option Lists: - Using ``zoneId`` to filter |morpheus| API-type Option Lists now works correctly :superscript:`5.4.16`
:Policies: - Adding a network to a Subtenant which would cause it to exceed its network quota Policy now fails with a friendly error message rather than throwing a less helpful 500 (threw a gasket) error :superscript:`5.4.16`
:Reports: - Fixed an issue that prevented correct results on the Instance Cost Report when filtering by a tag which contained a hyphen "-"
:Terraform: - Fixed an issue that caused Terraform Instances to be removed from |morpheus| even when the destroy action actually failed which led to orphaned instances left behind in the cloud :superscript:`5.4.16`
             - Fixed an issue that prevented applying state in |morpheus| on Terraform 0.12.31 Apps :superscript:`5.4.16`
             - Improvements added to the HCL parser to account for edge cases that didn't work properly :superscript:`5.4.16`
:UI: - Fixed a UI display issue that could cause the |morpheus| Role names and Active Directory group name fields to overlap each other when adding or editing an Identity Source integration :superscript:`5.4.16`
:Tags: - Inputs which are exported as tags are now set properly on the workloads when multiple copies of an Instance are selected at provision time
:VMware: - Visibility and Tenant ownership of newly synced VMware Cloud folders are now being set properly based on ownership of the parent folder
:Workflows: - Workflows and Tasks run against Instances are now shown in history for all nodes associated with the Instance. Previously they were shown only in the history of the Instance and one of the nodes
             - Fixed an issue with restart Tasks in Workflows which could throw an error cause the rest of the Workflow not to complete after the workload was restarted
