.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. Small Update, omitting highlights this time
  .. include:: highlights.rst

New Features
============

- Azure: Perf improvements for price sync. Refactored the caching of prices for Azure to use promise chaining. 
- NSX-T: Support firewall priority on routers
- Policy Enforcement - Cluster Provision

|morpheus| API & CLI Improvements
=================================

- API: Virtual Images should return locations
- API: filter by unique id fields

Morpheus Hub 
============

- WLE and Login Count stats to Morpheus Hub

Fixes
=====

- Policy Enforcement - Instance Provision
- Persona: Service Catalog: If you double-click on an order-related button in the service catalog only one item or one order (depending on the context) is created.
- Convert to Managed on Powered Off VM (and no agent install) powers VM On
- Openstack instance clone: instances with additional storage volumes creates a blank volume on the clone instance

Appliance Updates
=================

- Missing Nginx location in morpheus.conf and morpheus-ssl.conf

Agent/Node Package Updates
==========================

- Agent: Fix for symlink removal error when ipv4-rules file was removed.
