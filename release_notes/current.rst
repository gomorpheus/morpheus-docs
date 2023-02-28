.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

Release Dates
  - |morphVer|-1 |releasedate|
  - |morphVer|-2 Feb 28 2023

.. toggle-header::
    :header: 5.4.15-2 Updates **Click to Expand/Hide**

     5.4.15-2 contains the following updates not included in 5.4.15-1:

     :Azure: - 5.4.15-2 fixes 5.4.15-1 Azure security group sync issue that can lead to Appliance memory issues. :superscript:`5.4.15-2`
     :VMware Cloud: - 5.4.15-2 fixes VMware Cloud use of Global Proxy settings :superscript:`5.4.15-2`

.. NOTE:: Items appended with :superscript:`6.0.0` are also included in that version
.. .. include:: highlights.rst

New Features
============

:Bare Metal: - Storage and network details are now visible on the Hosts detail page for managed bare metal Instances :superscript:`6.0.0`
:Catalog: - Catalog Workflows can now utilize Inputs and have a custom config field (works just like custom config on an Operational Workflow) :superscript:`6.0.0`
:Clusters: - Some older default Kubernetes Cluster layouts (1.20 - 1.22) have been disabled for Cloud types which support newer Cluster layouts (1.23+) :superscript:`6.0.0`
:Kubernetes: - Added default Kubernetes 1.24 and 1.25 Cluster Layouts for many Cloud types including Amazon AWS, VMWare, Digital Ocean and more :superscript:`6.0.0`
             - Optimized Kubernetes container sync performance :superscript:`6.0.0`
:Workflows: - Tasks may now be selected more than once in an Operational Workflow and more than once in the same phase of Provisioning Workflows :superscript:`6.0.0`


Fixes
=====

:Alibaba Cloud: - Improved plan filtering when provisioning to Alibaba Cloud to show only flavors supported by the current configuration. This should prevent provisioning failures and users guessing at which plans should be supported :superscript:`6.0.0`
:Amazon: - IAM profiles are now selectable at provision time (advanced options section of provisioning wizard) for Subtenant users whether the Cloud is private and shared with the Subtenant or public :superscript:`6.0.0`
:Ansible Tower: - Ansible Tower Tasks now execute properly when the execute target is set to "Local" and the context set to "None" :superscript:`6.0.0`
:Ansible: - Fixed an issue that caused certain |morpheus| variables not to be set at the server context for Ansible Tasks :superscript:`6.0.0`
:Azure: - 5.4.15-2 fixes 5.4.15-1 Azure sercurity group sync issue that can lead to Appliance memory issues. :superscript:`5.4.15-2`
:Backups: - Fixed an issue that could cause schedule backups to continue even when the "Scheduled Backups" option is disabled in global settings (Administration > Settings > Backups) :superscript:`6.0.0`
:Blueprints: - Fixed an issue that caused 500 errors when accessing a Blueprint-based Catalog Item which was based off a Morpheus-type Blueprint utilizing a Terraform Instance Type :superscript:`6.0.0`
:Code: - Reading Git repositories which contain submodules will no longer cause issues in |morpheus| :superscript:`6.0.0`
:Costing: - Rebuilding costing data (costing refresh from Cloud detail page) with the REBUILD option checked will now take into account existing usage records in recreating the cost data :superscript:`6.0.05.4.1`
:Google Cloud (GCP): - For finalizing the previous month's costing, |morpheus| will now increase the lag time from one day to five days to ensure complete reporting :superscript:`6.0.0`
:Identity Sources: - Fixed an issue where the new/edit identity source modal would disappear after failing the create/update validation and become stuck with no obvious way to reopen it and fix the error :superscript:`6.0.0`
:Instances: - Aligned the reconfigure prompts for Instances and servers which could have differences in certain cases :superscript:`6.0.0`
:Kubernetes: - On MKS cluster control plane nodes, containerd will now automatically restart when the host is rebooted without additional configuration from the user :superscript:`6.0.0`
             - Fixed issue with Kubernetes cron job sync :superscript:`6.0.0`
             - Improved Kubernetes host sync matching and OS type assignment :superscript:`6.0.0`
:Option Lists: - When setting Active Directory options via custom Inputs sourced from LDAP-based Option Lists, selections will no longer get stuck when options have spaces or special characters :superscript:`6.0.0`
:Plans and Pricing: - Updating Subtenant Group permissions on Service Plans via |morpheus| API and CLI is now working properly :superscript:`5.5.3`
:Policies: - Creating an internal expiration policy after a ServiceNow provision approval policy will no longer cause the provisioning approval to also be internal (rather than a ServiceNow approval) :superscript:`6.0.0`
:Reports: - Fixed an issue that caused the Instance Inventory Summary report not to pull the correct Instances when filtered on more than one tag :superscript:`6.0.0`
:Scaling: - Fixed an issue where |morpheus| would send the scaling success email whether or not the scaling action was successful :superscript:`6.0.0`
:ServiceNow: - Fixed an issue that caused errors in Morpheus logs after completing Bulk Insert in ServiceNow :superscript:`6.0.0`
              - Fixed an issue with multiselect Typeahead Input fields when ordering catalog items via ServiceNow :superscript:`6.0.0`
:Snapshots: - Certain reconfigure actions, such as those which alter CPU, memory or plan will no longer cause existing snapshots to be deleted. Others, such as adding a disk, will still result in existing snapshots being deleted :superscript:`6.0.0`
:Terraform: - Fixed an issue that caused errors when refreshing or applying state to Terraform Instances or Apps if the provider version was updated in the Terraform spec :superscript:`6.0.0`
             - Fixed an issue that caused provisioning failures for catalog items based on Terraform Blueprints which would provision successfully as Apps outside the provisioning catalog :superscript:`6.0.0`
             - Fixed an issue that could cause Terraform Instance or App data not to be displayed correctly on editing or applying state in specific configurations :superscript:`6.0.0`
             - Fixed an issue that could caused REST-based Inputs not to show their values on the Apply State view for Terraform Instances and Apps :superscript:`6.0.0`
             - Fixed an issue where |morpheus| would convert object-type Terraform variables to strings which caused failures :superscript:`6.0.0`
             - Improvement made to Terraform HCL parsing for Terraform Instances and Apps :superscript:`6.0.0`
:VMware: - On Cloud sync, |morpheus| will now update OS type on Windows VMs if set to a non-Windows OS type :superscript:`6.0.0`
          - Provisioning ISO images on VMware Clouds is now working properly when a host is selected during the process :superscript:`6.0.0`
:VMware Cloud: - 5.4.15-2 fixes VMware Cloud use of Global Proxy settings :superscript:`5.4.15-2`


Appliance & Agent Updates
=========================

:Agent Packages: Node & VM Node Packages version updated to 3.2.11
:Agent Packages: Node & VM Node Java version updated to 11.0.18
