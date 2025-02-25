.. _Release Notes:

************************
|morphver| Release Notes
************************

Release Dates:

- |morphver| |releasedate|

New Features
============

:API & CLI: - When creating Instance snapshots via |morpheus| API, the response now includes process IDs for the triggered snapshots
:HPE VM: - Provisioning to HPE VM Clusters now sets a default "Auto Datastore" selection. Users may manually select a datastore or may leave the default automatic configuration
         - HPE VM Clusters now support network groups
         - Certain actions will no longer update UUIDs for VM storage volumes (moving VM to a different host, changing disk datastores, etc)
         - Significant iops performance for VMs running on HPE VM clusters resulting from a switch to I/O native configuration from I/O threads
:Virtual Images: - When importing images from existing VMs, future attempts to provision from that Virtual Image will automatically set disks on the provisioning wizard to a minimally viable configuration (Ex. three disks in appropriate minimum sizes)

Fixes
=====

:API & CLI: - Fixed results from the ``/instances/stats`` API endpoint to include only statistics from Instances the user can access
          - Fixed calls to return Task executions failing with certain license types which shouldn't have restricted it
:HPE VM: - Fixed an issue where new host nodes added to existing HPE VM clusters with GFS2 datastores would not have the datastore mounted correctly and would face sync errors
:Storage: - Fixed the "Add S3 Bucket" (|InfStoBuc|) modal failing to load
:Tasks: - Fixed Tasks designed for specific versions of Powershell being incorrectly run against the default version under certain configurations
:User Settings: - Fixed a small styling issue on the button to upload an avatar image on the User Settings page

..
  Appliance & Agent Updates
  =========================
