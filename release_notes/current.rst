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

:VMware: - Added the option to select a memory snapshot when creating a snapshot of an Instance running in a VMware Cloud
:HVM: - Users can now opt out of moving powered-off VMs to other hosts when placing a host into maintenance mode

Fixes
=====

:API & CLI: - Attempts to delete Workflows via |morpheus| API while they are associated with a Layout now fail more gracefully
:Backups: - Attempts to backup HVM Instances having mixed storage volumes (ex. local storage and Alletra storage) no longer fail
:Backups: - Snapshotting HVM Instances having mixed storage volumes (ex. local storage and Alletra storage) will no longer fail
:Clone: - Clone creation no longer fails for HVM Instances having mixed storage volumes (ex. local storage and Alletra storage)
:Clusters: - The datastores list within a Cluster detail page (Storage tab) can now show more than 25 datastores

Appliance & Agent Updates
=========================
