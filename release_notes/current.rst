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
- Create and manage load balance monitors
- Create and manage load balance pools and pool members
- Create an manage virtual servers for NSX-T
- Reserve and release IP addresses NSX-T IP pools when provisioning and decommissioning

.. image:: /images/releases/422/nsxt.png

**NSX-V Integration** Enhancements

- Create, manage and sync load balancers for NSX-V
- Configure a load balancer in an instance/app wizard
- Add or remove load balancers to/from existing Instances
- Edit load balancers on existing Instances
- Create and manage load balance monitors
- Create and manage pools and pool members
- Create and manage virtual servers for NSX-V
- Scope NSX-V load balancers to Groups such that they are owned by and, by default, only visible to that Group. They are also subject to Group-level policies

**Kubernetes** Enhancements

- Kubernetes version 1.17 support for Morpheus-type (MKS) Kubernetes deployments

Other New Features
==================

- Appliance: Various optimizations resulting in reduced CPU usage and improved performance 
- Advanced Search: Enhancements and stability improvements to advanced search and filtering tools released in |morpheus| 4.2.1
- Catalog: openSUSE 15.1 catalog item added for SCVMM Clouds
- Kubernetes: Version 1.17 support for Morpheus-type Kubernetes deployments (MKS)
- NSX-T: Improvements to NSX-T integration including the ability to work with load balancers and virtual servers
- NSX-V: Improvements to NSX-V integration including the ability to work with load valancers and virtual servers
- Open Telekom Cloud: Added bandwidth option to floating IP selection
- RabbitMQ: Stomp Broker removed. A Load Balancer is no longer required for external RabbitMQ clusters.
- RabbitMQ: Agent Queue consolidation. ``monitorJobs*`` and ``statCommands*`` agent queues removed, agent messages now use ``morpheusAgentActions`` queue.
- vCloud Director: Proxy support

Fixes
=====

- API/CLI: Fixed calls to instances without containers throwing a gasket
- API/CLI: The exportMeta property is now provided for an option type in both the CLI and API. This maps to the "Export As Tag" checkbox setting on the Option Type dialog in the UI.
- Bluecat: Fixed removal of Network Pool record when deleting a Bluecat Integration
- Clusters: Fixed available host check when adding new nodes to Instances in Docker Clusters
- Hosts: Fixed for bulk convert-to-managed
- Identity Sources: Custom External SSO Identity Source: Fixed AES encryption setting
- Instances: Fixed edit Wiki button displayed on Instances when user has Read Only Instance access.
- Instances: Special Characters can now be used in Instances names, will be stripped from hostname and host names.
- Logs: Removed ``println "Not a master"`` from MorphTagLib service
- Networks: Fixed display error when editing tenant permissions on existing network
- Networks: IP Pools: Fixed conflict when using 169.x.x.x pool address ranges
- SCVMM: Guacd updated to support SCVMM Hypervisor Console
- ServiceNow: Plugin: v2.0.6  Fixed multiple Name fields appear for Instance provisioning form in ServiceNow catalog Item. (Plugin: v > 2.0.6)
- ServiceNow: Plugin: v2.0.6: Fixed snow plugin not including Instance environment data in Blueprint provisioning requests from ServiceNow
- Usage: Fixed Usage record time periods overlapping time periods (milliseconds) for the same object
- Users: Fixed "Disable User if Inactive For" User setting locking non-local user accounts
- vCloud Director: Fixed ``validateResizeContainer error`` in morpheus-ui logs
- vCloud Director: Fixed cloud-sync connection timeouts

..
  |morpheus| API Updates
  **********************

  API Fixes
  =========



  |morpheus| CLI Updates
  **********************

  CLI Fixes
  =========
