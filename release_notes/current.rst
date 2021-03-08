.. _Release Notes:

************************
|morphver| Release Notes
************************

.. Small Update, omitting highlights this time
  .. include:: highlights.rst

New Features
============

- Clouds: The manual cloud refresh button is now a dropdown with refresh options. “Short” refresh immediately performs a cloud sync that otherwise occurs at five-minute intervals (by default), “Daily” runs the heavier nightly cloud sync, and “Costing” will immediately perform the nightly cost sync from the cloud. The costing refresh option is only available for public cloud types which offer live cost syncing
- Self-Service Catalog Tool: Configure Catalog Apps using the familiar App provisioning wizard. Previously, Catalog Apps were configured by selecting an existing Blueprint and at least setting minimally-required App Spec with YAML
- Plugins: Added soft reloads for updating Plugins. An updated plugin file can now be uploaded without having to delete the previous file, preserving settings such as Role Access permissions. 
- Administration: Provisioning: "Reuse Naming Sequence Numbers" setting now applies to all Instance naming patterns using``${sequence}`` values. Previously Reuse Naming Sequence Numbers = false was only applicable for Naming Policies
- Policies: "Host Name" Policy renamed to "Cluster Resource Name" for clarity


Fixes
=====

- Azure: Fixed Network Groups not getting mapped on provisioning 
- Tasks: Fixed Task Result chaining not working when running in server context 
.. verify - Security: XSS vulnerabilities closed for Reconfigure and Library
- Costing: Account Usage Checks Refactored
- NSX-V: Fixed distributed firewall groups not displayed in order of priority
- API: Fixed Access to virtual images not allowed in UI but successful using the API
.. wtf - Hosts: Advanced Filters: Removed "Discovered" option from ``STATUS`` filter as it was being confused with Server Type "Discovered" (Discovered is a Status for Bare Metal Servers)
- UI: Fixed unexpected logouts due to Session Expiration in another non-active tab 
- Plans: Fixed Instance Plans not updating on Cloud refresh when the cpu/memory/storage of the target VM changed in Cloud and not all Containers within the Instance are on the same plan in VMware, Nutanix and SCVMM Cloud types.
- Security: Fixed occurrence of user csrf token being transmitted via query string parameter
- Workflows: Fixed Task phase assignment changing upon edit and save of a Workflow when using the same Task in multiple phases in the same Workflow 
- F5: Added additional log/error output when https Virtual Server creation fails due to F5 unable to reach |morpheus| Appliance to obtain certificate file.
- Dell Isilon: Fixed share creation not creating the share in the correct storage group
- Blueprints: Fixed Custom Options value overrides reverting to default value when saving Blueprints.
- Rubrik: Blueprints: Fixed SLA Domain option not displayed in Blueprints
- CLI: Service Plans: Group Permissions: Fixed ``service-plans update <servicePlanId> --group-access-all on`` setting Group Visibility to ``null``
- API: Prices: Fixed ```account`` value not respected when creating a price and assigning to a Tenant.
- Reports: Tenant Usage Report: Removed additional unreadable date being include when exporting Tenant Usage Reports
- Clusters: Kubernetes: Fixed issue with VM and DNS naming discrepancies when using a Cluster Resource Name/Host Name Policy (Note the "Host Name" Policy type has been renamed to "Cluster Resource Name")
.. verify - Workflows: Fixed issue with available Group scoping during Task execution on Instances where the Instances' assigned Group is not accessible to the User who created the Instance.
- Azure: Fixed evaluated name not being used for Azure public ip dns hostname when using Naming Policy containing ``customOptions`` variable(s), causing "DNS name label not available" error
- Microsoft DNS: Integration validation requests now use elevated flag to lower service account permission requirements
- Networks: Reduced network activity and connections when "Scan Network" is enabled on a Network 
- Azure: Fixed sync issue where a public IP would still show in |morpheus| for Azure Instances when the Public IP has been deleted/removed in Azure
.. verify - Azure: Fixed network sync issue when multiple address Prefixes exist for the ip range on a network and subnet


Agent/Node Package Updates
==========================

|morpheus| Node & |morpheus| VM Node Packages Version: v3.1.14
|morphues| Linux Agent version: v2.1.1
|morphues| Linux Agent: Fixed issue with stat collector network interface bonding in Ubuntu 18.04
  
..


  |morpheus| API Improvements
  ===========================

  Appliance Updates
  =================


  Morpheus Hub
  ============

