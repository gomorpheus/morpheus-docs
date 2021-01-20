.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. Small Update, omitting highlights this time
  .. include:: highlights.rst

New Features
============

- Azure: Optimizations of Azure Resource & Price sync with 3x speed improvements and reduced Appliance CPU utilization
- NSX-T: Gateway Firewall Groups can now be created and shared across Routers
- NSX-T: Groups/Policies and CRUD methods added to Gateway Firewall tabs
- NSX-T: Support for firewall priority on supported Router types added
- Option Types: Added `Visibility field <https://docs.morpheusdata.com/en/latest/provisioning/library/library.html#visibility-field>_` to configure visibility of the current Option Type based on the value of another existing Option Type. For now, works only when the Option Type is associated with Service Catalog items.
- Policies: Improved handling for budget, max cores, max hosts, max memory, and max storage policies during cluster provisioning
- Policies: Improved policy handling when provisioning Instances as it relates to specific handling of copy and scale scenarios, friendlier policy warning messages, and other improvements
- Security Updates

|morpheus| API & CLI Improvements
=================================

- API/CLI: ``location`` records now returned with ``virtual-images`` requests
- API/CLI: ``api/servers`` (hosts) can now be queried/filtered by ``uuid``, ``externalId``, ``internalId``, and ``externalUniqueId`` (uniqueId)

Morpheus Hub
============

- Improved statistics including current and max Workload Element (WLE) count and last check-in date metrics

Fixes
=====

- Apps: The App wizard now automatically handles situations where multiple Instances in the App have the same name, which would cause the provisioning to fail
- Hosts: Converting a powered off VM to managed when agent install is not enabled will no longer automatically power on the VM when Automatically Power On (managed) VMs" is enabled in the source Cloud.
- Openstack: Fixed issue when cloning Instances with additional storage volumes creating a blank volume on the cloned Instance

Appliance Updates
=================

- NGINX: Fixed potential timeout issue with private local image uploads greater than 1GB to Azure
- Installer: Resolved ``PowerTools`` vs ``powertools`` repo name issue with centOS 8.3

Agent/Node Package Updates
==========================

- Agent: Fix for symlink removal error when ``ipv4-rules`` file was removed
