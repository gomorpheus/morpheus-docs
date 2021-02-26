.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. include:: highlights.rst

New Features
============

- Activity: View results, including any errors, from teardown-phase Tasks on History page (Operations > Activity > History). Previously, cleanup errors were not visible because this page did not show any Instance activity after the Instance was deleted
- Amazon: Amazon AWS Clouds can now be scoped to the "Africa (Cape Town)" region
- Azure: |morpheus| now syncs Shared Gallery images and can provision from them. Previously images held in a Shared Gallery were not synced
- Azure: Scope Azure cloud integrations to all regions rather than targeting each integration to a specific region
- CloudFormation: Values entered into password fields are no longer revealed in plaintext on the summary tab of the App provisioning wizard during provisioning
- Clouds: The manual cloud refresh button is now a dropdown with refresh options. "Short" refresh immediately performs a cloud sync that otherwise occurs at five-minute intervals (by default), "Daily" runs the heavier nightly cloud sync, and "Costing" will immediately perform the nightly cost sync from the cloud. The costing refresh option is only available for public cloud types which offer live cost syncing
- Console: Guest Console configuration added to Host, Virtual Machine and Bare Metal resource settings to specify Guest Console connection type (Disabled, SSH, VNC, RDP), if Guest Console is preferred over Hypervisor and Guest Console default Username and Password for auto-login.
- Console: Guest Console configuration for Virtual Images 
- Console: Removed copy and paste field in Console header for Hypervisor Consoles connection where it is not supported
- Console: Switch between Guest Console or Hypervisor Console per console session. :guilabel:`Guest` and :guilabel:`Hypervisor` selection added to console header to toggle between connectiion types. Requires Hypervisor and Guest Consoles to be enabled. 
- Console: User specific auto-logins for Guest Console Sessions. Console Auto-Login now uses credentials from a |morpheus| users Linux and Windows User config in User Settings. Previously the RPC User configuration of a host was used.  
- Networks: Removed the default and uneditable description on the ``localdomain`` (Infrastructure > Networks > Domains) which could be misleading under some configurations
- NSX-V: Priority is now displayed for firewall groups and rules on the Firewall tab of NSX-V integrations
- Personas: Added the Virtual Desktop Persona, a simplified view granting users access to virtual desktops and Instance consoles
- Policies: Cloning Instances now respects policies such as budget, max containers, max cores, max memory, and max storage
- Prices and Plans: Price Set and Pricing Plan types added for snapshots
- Prices and Plans: Price Set and Pricing Plan types added for virtual image billing
- Roles: The "Tenant Admin" Role, which is included out-of-the-box and is not editable, now gives "Full" permissions for Snapshots
- Self- Service Catalog Tool: Configure Catalog Apps using the familiar App provisioning wizard. Previously, Catalog Apps were configured by selecting an existing Blueprint and at least setting minimally-required App Spec with YAML
- Spec Templates: |morpheus| now intelligently detects the template file for ARM deployment in a Spec Template from a Git repository. Previously, users were required to provide a path containing just one .json file
- Tasks: Set Shell Script Tasks to run as ``sudo`` by marking the added check box
- Tools: Added tool for creation of VDI pools for consumption in the Virtual Desktop Persona
- Virtual Images: Added the option to also remove Virtual Images from VMware, Amazon, OTC, Huawei, and OpenStack clouds when deleting them out of |morpheus|
- Workflows: Startup and Shutdown phases added for Provisioning Workflows. Tasks in the Startup phase run after the target is started and Tasks in the Shutdown phase run immediately before the target is shutdown

Fixes
=====

Appliance Updates
=================

Installer: Fixed issue with check failing to recognize when powertools/PowerTools/codeready repos were already enabled

..
  |morpheus| API & CLI Improvements
  =================================

  Morpheus Hub
  ============



  Agent/Node Package Updates
  ==========================
