.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade versions: Non-rolling: |minUpgradeVer| (Rolling upgrades not supported for 8.0.4)

.. .. NOTE:: Items appended with :superscript:`7.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

.. _Release Notes:

|

New Features
============

:Instances: - The Instances list page now includes an optional Date Created field and is sortable by this field
:VMware: - Added the option to select a memory snapshot when creating a snapshot of an Instance running in a VMware Cloud
:HVM: - Users can now opt out of moving powered-off VMs to other hosts when placing a host into maintenance mode

Fixes
=====

:API & CLI: - Attempts to delete Workflows via |morpheus| API while they are associated with a Layout now fail more gracefully
            - Subtenant users are no longer able to view Service Plans via API which are privately scoped to the |mastertenant|
:Automation: - Tasks selected manually to run during Instance provisioning will no longer cause other Workflows to run if they happen to have the same ID value
:Backups: - Attempts to backup HVM Instances having mixed storage volumes (ex. local storage and Alletra storage) no longer fail
:Backups: - Snapshotting HVM Instances having mixed storage volumes (ex. local storage and Alletra storage) will no longer fail
:Clone: - Clone creation no longer fails for HVM Instances having mixed storage volumes (ex. local storage and Alletra storage)
:Clusters: - The datastores list within a Cluster detail page (Storage tab) can now show more than 25 datastores
:Costing: - Fixed cloud cost comparisons in the Instance provisioning wizard not displaying comparisons against comparable workloads in Azure
:OpenStack: - Removed the ability to reconfigure networks for OpenStack workloads as it did not work as expected. To change network, remove the interface and re-add it, which is consistent with the same process in the OpenStack console
:Option Lists: - Fixed an issue where select list items which are very long could overflow and obscure other UI controls (delete buttons, etc)
:Security: - Subtenant users can no longer see which other Tenants a Service Plan is assigned to in API responses
:Storage: - Fixed adding storage buckets not honoring "No Proxy" configurations
           - Fixed the |morpheus| footer not extending the entire page width on storage bucket detail pages
:Terraform: - Fixed Post-Provision phase Tasks also being executed in the Provision phase for Terraform Instances

Appliance & Agent Updates
=========================

:VM Node Packages: - i386 node/vm-node/agent packages have been removed.