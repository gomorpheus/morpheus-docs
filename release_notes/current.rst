.. _Release Notes:

************************
|morphver| Release Notes
************************

.. No highlights this time, small update
  .. include:: highlights.rst

.. NOTE:: OpenStack v2 Identity API will be deprecated in v5.2.9 and will be removed in v5.3.3

New Features
============

:Openstack: OpenStack v2 Identity API will be deprecated in v5.2.9 and will be removed in v5.3.3

|morpheus| API Improvements
===========================


Fixes
=====

:Rubrik: Backup size now displayed as ``-`` instead of ``0`` when backup size is not available
:Reports: Fix for display of utilization statistics in some Cloud Usage Reports
:Blueprints: Rapidly activating different Builder, Raw, and Preview tabs in the blueprint wizard no longer causes the active tab content to get stuck.
:Roles: Datastores: Edit option no longer displayed for Role Permission ``Infrastructure -> Datastores: Read``
:Keypairs: Synced keypairs are now filtered from Key Pairs selection list in user settings and admin provisioning settings. Synced Key Pair records do not contain any key data and are not usabled for user and global keypairs.
:Analytics: Cloud Costs: Fixed selecting a tag name and value combination in the "more" filters in Cloud Cost Analysis
:Localization: Portuguese: The strings displayed in the Create Cloud dialog are now being displayed properly when selecting Portuguese as the language. Pass in ``?lang=pt_BR`` or ``?lang=pt_PT`` in the url to force the UI to Portuguese Brazil and Portugal, respectively
:Health: Fixed issue with |morpheus| Appliance logs not displaying in ``Administration -> Health: Logs`` when ``appliance_instance`` id not equal to ``1``
:Clusters: Docker Clusters: Fixed custom option type issues required flag enforcemnet and type ahead option type issue when provisioning Docker Clusters
:Library: Fixed display of sub-tab selection in ``Provisioning -> Library`` UI mobile views 
:vCloud Director: Fixed ``safeComputerName`` issue during Windows Guest Customizations
Unmanage VM W/ remove assoc instance option w/ Delay removal it shuts VM down
Activity Logs is requiring Operations: Reports permission too
Variable - Current User?
Chef bootstrap now requires license agreement to proceed.
Ansible task execution fails when user has special characters in their name
Cloud count disappears inside Groups->Clouds section
Errors when deleting a nic in VMware
Boot order for app blueprints isn‚Äôt being honoured with approval policy in place
NSX-T: Cannot select SERVICE TYPE at the time of NSX-T SSL certificate creation
Cannot Stop/Power off VM on Azure from Server Context
ARM Git source issues ... Wrong path
The jQuery libraries in use are outdated (v3.5.1)
Copies does not work on instance provisioning
Cloning Windows Instance - Agent Installation hangs in Finalising
Guidance resizing incorrectly for CPU recommendations
Resource Pools not populating in multi VMware clouds
Not able to create prices in USN using the API.
Updating Linux/Windows passwords on user settings doesn‚Äôt give success message
Null values in Terraform code show as [object object] in Morpheus UI
Image Builder Timeout
Ansible integration issue - command bus option not saving
API/CLI: If a tenant still has users/instances tied to it, the delete will fail
NSX-V: Additional instance nodes are not adding under LB pool members
Ansible Galaxy Race Condition | Roles can be removed during Ansible playbook execution causing failed task executions
vCD:  Windows User creation is not working for guest customizations

Appliance & Agent Updates
=========================

:Openstack: OpenStack v2 Identity API will be deprecated in v5.2.9 and will be removed in v5.3.3