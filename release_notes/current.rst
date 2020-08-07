.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading to |morpheus| |morphver|.

|morpheus| UI Updates
*********************

Highlights
==========

**NSX-T Integration** Enhancements

- Create and manage NSX-T load balancers for NSX-T
- Create and manage load balancer monitors
- Create and manage load balancer pools and pool members
- Create and manage virtual servers for NSX-T
- Reserve and release IP addresses NSX-T IP pools when provisioning and decommissioning

.. image:: /images/releases/422/nsxt.png

**NSX-V Integration** Enhancements

- Create, manage and sync load balancers for NSX-V
- Configure NSX-V load balancers in instance/app wizards
- Add or remove load balancers to/from existing Instances
- Edit load balancers on existing Instances
- Create and manage load balancer monitors
- Create and manage pools and pool members
- Create and manage virtual servers for NSX-V
- Scope NSX-V load balancers to Groups such that they are owned by and, by default, only visible to that Group. They are also subject to Group-level policies

**Kubernetes** Enhancements

- Kubernetes version 1.17 support for Morpheus-type (MKS) Kubernetes deployments

Other New Features
==================

- Advanced Search: Enhancements and stability improvements to advanced search and filtering tools released in |morpheus| 4.2.1
- Appliance: Various optimizations resulting in reduced CPU usage and improved performance
- Azure: Azure China Cloud support added :superscript:`-2`
- Azure: Azure German Cloud Support added :superscript:`-2`
- Azure: Azure Stack Integration updated to support latest Azure Stack version & 2019-03-01-hybrid api-profile:superscript:`-2`
- Azure: Azure US Government support added :superscript:`-2`
- Azure: Cloud Type selection added to Azure Cloud config for specifying Standard, US Gov, China and German environments:superscript:`-2`
- Azure: Costing sync updates and enhancements :superscript:`-2`
- Catalog: openSUSE 15.1 catalog item added for SCVMM Clouds
- Kubernetes: Version 1.17 support for Morpheus-type Kubernetes deployments (MKS)
- NSX-T: Improvements to NSX-T integration including the ability to work with load balancers and virtual servers
- NSX-V: Improvements to NSX-V integration including the ability to work with load balancers and virtual servers
- NSX-V: Expanded options for NSX-V load balancer pool members to include more objects available in vCenter :superscript:`-3`
- NSX-V: Create, manage, and delete NSX-V SSL certificates :superscript:`-3`
- NSX-V: Create, manage, and delete NSX-V load balancer profiles :superscript:`-3`
- NSX-V: Create, manage, and delete NSX-V load balancer rule scripts :superscript:`-3`
- NSX-V: Status of pools and pool nodes is now displayed :superscript:`-3`
- Nutanix: MAC Address now displayed in the Instance/Server Detail Network tab :superscript:`-2`
- OCI: Support for Recursive Compartments added :superscript:`-2`
- Open Telekom Cloud: Added bandwidth option to floating IP selection
- Policies: Policies now apply when Reconfiguring an Instance or Server :superscript:`-2`
- RabbitMQ: Agent Queue consolidation. ``monitorJobs*`` and ``statCommands*`` agent queues removed, agent messages now use ``morpheusAgentActions`` queue
- RabbitMQ: Stomp Broker removed. A Load Balancer is no longer required for external RabbitMQ clusters.
- vCloud Director: Proxy support added
- VMware: MAC Address now displayed in the Instance/Server Detail Network tab :superscript:`-2`

Fixes
=====

- Amazon: Fixed issue with Amazon Costing Inventory Reports not handling changing rates from previously processed line items correctly. Totals are also now recalculated on a daily basis:superscript:`-2`
- Amazon: Fixed deletion of non-|morpheus| keypairs when deleting the first |morpheus| integration created with an AWS account :superscript:`-3`
- Bluecat: Fixed removal of Network Pool record when deleting a Bluecat Integration
- Chef: Chef private keys are now masked like passwords when later viewing the edit integration modal :superscript:`-3`
- Clusters: Fixed available host check when adding new nodes to Instances in Docker Clusters
- Clusters: Fixed an issue causing service plans with "private" visibility to not appear on cluster provisioning :superscript:`-3`
- Console: Fixed issue causing Instance and Server Consoles form displaying in Safari browsers :superscript:`-2`
- Cypher: Fixed an issue where Cypher-generated passwords could contain breaking characters in certain scenarios :superscript:`-3`
- Fixed issue we found causing slow Elasticsearch queries on certain indices :superscript:`-2`
- Hosts: Fixed for bulk convert-to-managed
- Identity Sources: Custom External SSO Identity Source: Fixed AES encryption setting
- Instances: Fixed edit Wiki button displayed on Instances when user has Read Only Instance access
- Instances: Special Characters can now be used in Instances names, will be stripped from hostname and host names.
- Instances: Fixed issue where hostname would be set to "null" on nodes added to an Instance via the Actions menu on the Instance detail page :superscript:`-3`
- Logs: Removed ``println "Not a master"`` from MorphTagLib service
- Networks: Fixed display error when editing tenant permissions on existing network
- Networks: IP Pools: Fixed conflict when using 169.x.x.x pool address ranges
- NSX-V: Fixed an issue that could cause changes to not be saved after editing an NSX-V load balancer :superscript:`-3`
- NSX-V: Fixed an issue that caused an error when syncing back a NSX-V ESG with DHCP IP pool :superscript:`-3`
- NSX-V: General cleanup of minor issues around NSX-V load balancers :superscript:`-3`
- NSX-V: Fixed an issue affecting updating of HTTPS offloading profiles for NSX-V load balancers :superscript:`-3`
- NSX-V: Fixed an issue with the NSX-V load balancer service that could cause high CPU usage in certain scenarios :superscript:`-3`
- NSX-V: Edits made to NSX-V router interface addresses are now reflected properly in vCenter :superscript:`-3`
- OpenStack: Synced images from OpenStack clouds now appear as provisionable images for OpenStack clouds privately assigned to a Subtenant :superscript:`-3`
- Option Types: Fixed Field Name returning instead of Field Value for Custom Options variables when using Typeahead Option Types in Blueprints/Apps*
- Option Types: Fixed LDAP Typeahead search not searching against multiple fields :superscript:`-2`
- Oracle Cloud: Fix Oracle Cloud Costing sync when using a Proxy :superscript:`-2`
- SCVMM: Guacd updated to support SCVMM Hypervisor Console
- SCVMM: Fixed issue causing console not to connect :superscript:`-3`
- Security: Fixed a path traversal vulnerability in specific file upload scenarios :superscript:`-3`
- Security: Resolved reflected cross-site scripting (XSS) vulnerabilities :superscript:`-3`
- Security: Other security enhancements :superscript:`-3`
- ServiceNow: Plugin: v2.0.6  Fixed multiple Name fields appear for Instance provisioning form in ServiceNow catalog Item. (Plugin: v > 2.0.6)
- ServiceNow: Plugin: v2.0.6: Fixed snow plugin not including Instance environment data in Blueprint provisioning requests from ServiceNow
- UI: "Administrator" is now spelled correctly in the Windows Settings > Administrator Password field in Administration > Provisioning > Settings tab :superscript:`-3`
- Usage: Fixed Usage record time periods overlapping time periods (milliseconds) for the same object
- Users: Fixed "Disable User if Inactive For" User setting locking non-local user accounts
- vCloud Director: Fixed ``validateResizeContainer error`` in morpheus-ui logs
- vCloud Director: Fixed cloud-sync connection timeouts

|morpheus| API Updates
**********************

API Fixes
=========
- API/CLI: Fixed calls to instances without containers throwing a gasket
- API/CLI: The exportMeta property is now provided for an option type in both the CLI and API. This maps to the "Export As Tag" checkbox setting on the Option Type dialog in the UI.
- API/CLI: Changes to expiration now honored when cloning an Instance :superscript:`-3`
- API: Fixed an issue that caused processed versions of PNG whitelabel images uploaded over API not to be saved :superscript:`-3`

|morpheus| CLI Updates
**********************

CLI Enhancements
================
- CLI: Improved logs list output, the message output will flex to the width of the terminal and show more than one line, also new option --table is available. This also impacts health logs , instances logs, etc.

CLI Fixes
=========

- CLI: Fixed tasks add add --no-prompt still prompting for Content Ref. This fixes spec-templates add as well.
- CLI: Fixed login -T always resulting in Token not valid error.
- CLI: Fixed remote add --insecure not working.
- CLI: Fixed several issues with invoices.

.. note::  
   
   | :superscript:`-2` Indicates features and fixes added in 4.2.2-2 release packages
   | :superscript:`-3` Indicates features and fixes added in 4.2.2-3 release packages
