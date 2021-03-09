.. _Release Notes:

************************
|morphver| Release Notes
************************

.. Small Update, omitting highlights this time
  .. include:: highlights.rst

.. NOTE:: Features marked with :superscript:`5.3.0` are also included in Morpheus UI 5.3.0 standard (non-LTS) release version

New Features
============

- Activity: View results, including any errors, from teardown-phase Tasks on History page (Operations > Activity > History). Previously, cleanup errors were not visible because this page did not show any Instance activity after the Instance was deleted :superscript:`5.3.0`
- Amazon: Amazon AWS Clouds can now be scoped to the “Africa (Cape Town)” region :superscript:`5.3.0`
- CloudFormation: Values entered into password fields are no longer revealed in plaintext on the summary tab of the App provisioning wizard during provisioning :superscript:`5.3.0`
- Clouds: The manual cloud refresh button is now a dropdown with refresh options. “Short” refresh immediately performs a cloud sync that otherwise occurs at five-minute intervals (by default), “Daily” runs the heavier nightly cloud sync, and “Costing” will immediately perform the nightly cost sync from the cloud. The costing refresh option is only available for public cloud types which offer live cost syncing :superscript:`5.3.0`
- Library: Canonical MaaS and Lumen Edge are now selectable as technology types for Library items such as Layouts and Node Types
- Networks: Removed the default and uneditable description on the localdomain (Infrastructure > Networks > Domains) which could be misleading under some configurations :superscript:`5.3.0`
- NSX-V: Priority is now displayed for firewall groups and rules on the Firewall tab of NSX-V integrations :superscript:`5.3.0`
- NSX-V: Configure DHCP and DHCP log levels on Edge Gateways
- NSX-V: Create and manage DHCP Pools for Edge Gateways
- NSX-V: Create and manage DHCP Relay for Edge Gateways and Logical Routers
- NSX-V: Create and manage DHCP Bindings for Edge Gateways
- Self-Service Catalog Tool: Configure Catalog Apps using the familiar App provisioning wizard. Previously, Catalog Apps were configured by selecting an existing Blueprint and at least setting minimally-required App Spec with YAML  :superscript:`5.3.0`
- Plugins: Added soft reloads for updating Plugins. An updated plugin file can now be uploaded without having to delete the previous file, preserving settings such as Role Access permissions.
- Policies: Cloning Instances now respects policies such as budget, max containers, max cores, max memory, and max storage :superscript:`5.3.0`
- Policies: "Host Name" Policy renamed to "Cluster Resource Name" for clarity
- Roles: The “Tenant Admin” Role, which is included out-of-the-box and is not editable, now gives “Full” permissions for Snapshots :superscript:`5.3.0`
- Settings: "Reuse Naming Sequence Numbers" setting in Administration > Settings > Provisioning now applies to all Instance naming patterns using``${sequence}`` values. Previously Reuse Naming Sequence Numbers = false was only applicable for Naming Policies
- Spec Templates: Morpheus now intelligently detects the template file for ARM deployment in a Spec Template from a Git repository. Previously, users were required to provide a path containing just one .json file :superscript:`5.3.0`


|morpheus| API Improvements
===========================

- Billing: The ``billing`` API endpoint now returns ``resourcePoolId`` and ``resourcePoolName``
- Clouds: ``scalePriority`` is now handled properly for get, add and update requests to the ``clouds`` API :superscript:`5.3.0`


Fixes
=====

- API: Fixed Access to virtual images not allowed in UI but successful using the API
- API: Prices: Fixed ```account`` value not respected when creating a price and assigning to a Tenant.
- Azure: Fixed evaluated name not being used for Azure public ip dns hostname when using Naming Policy containing ``customOptions`` variable(s), causing "DNS name label not available" error
- Azure: Fixed Network Groups not getting mapped on provisioning
- Azure: Fixed network sync issue when multiple address Prefixes exist for the ip range on a network and subnet
- Azure: Fixed sync issue where a public IP would still show in |morpheus| for Azure Instances when the Public IP has been deleted/removed in Azure
- Blueprints: Fixed Custom Options value overrides reverting to default value when saving Blueprints.
- CLI: Service Plans: Group Permissions: Fixed ``service-plans update <servicePlanId> --group-access-all on`` setting Group Visibility to ``null``
- Clusters: Kubernetes: Fixed issue with VM and DNS naming discrepancies when using a Cluster Resource Name/Host Name Policy (Note the "Host Name" Policy type has been renamed to "Cluster Resource Name")
- Costing: Account Usage Checks Refactored
- Dell Isilon: Fixed share creation not creating the share in the correct storage group
- F5: Added additional log/error output when https Virtual Server creation fails due to F5 unable to reach |morpheus| Appliance to obtain certificate file.
- Hosts: Advanced Filters: Removed "Discovered" option from ``STATUS`` filter as it was being confused with Server Type "Discovered" (Discovered is a Status for Bare Metal Servers)
- Microsoft DNS: Integration validation requests now use elevated flag to lower service account permission requirements
- Networks: Reduced network activity and connections when "Scan Network" is enabled on a Network
- NSX-V: Fixed distributed firewall groups not displayed in order of priority
- Plans: Fixed Instance Plans not updating on Cloud refresh when the cpu/memory/storage of the target VM changed in Cloud and not all Containers within the Instance are on the same plan in VMware, Nutanix and SCVMM Cloud types.
- Reports: Tenant Usage Report: Removed additional unreadable date being include when exporting Tenant Usage Reports
- Rubrik: Blueprints: Fixed SLA Domain option not displayed in Blueprints
- Security: Fixed occurrence of user csrf token being transmitted via query string parameter
- Security: XSS vulnerabilities closed for Reconfigure and Library
- Tasks: Fixed Task Result chaining not working when running in server context
- UI: Fixed unexpected logouts due to Session Expiration in another non-active tab
- Workflows: Fixed issue with available Group scoping during Task execution on Instances where the Instances' assigned Group is not accessible to the User who created the Instance.
- Workflows: Fixed Task phase assignment changing upon edit and save of a Workflow when using the same Task in multiple phases in the same Workflow


Agent/Node Package Updates
==========================

|morpheus| Node & |morpheus| VM Node Packages Version: v3.1.14
|morphues| Linux Agent version: v2.1.1
|morphues| Linux Agent: Fixed issue with stat collector network interface bonding in Ubuntu 18.04

