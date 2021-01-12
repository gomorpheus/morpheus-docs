.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. Small Update, omitting highlights this time
  .. include:: highlights.rst

New Features
============

- Azure: Performance improvements for Azure price sync
- NSX-T: Support firewall priority on routers
- Policies: Improved handling for budget, max cores, max hosts, max memory, and max storage policies during cluster provisioning

|morpheus| API & CLI Improvements
=================================

- API: ``locations`` can now be returned for each virtual image
- API: Hosts ``api/servers`` can now be queried by unique ID fields

Morpheus Hub
============

- Improved statistics including login and workload element counts in Morpheus Hub

Fixes
=====

- Apps: The App wizard now automatically handles situations where multiple Instances in the App have the same name, which would cause the provisioning to fail
- Policies: Improved policy handling when provisioning Instances as it relates to specific handling of copy and scale scenarios, friendlier policy warning messages, and other improvements
- Service Catalog Persona: If you double-click on an order-related button in the service catalog, only one item or one order (depending on the context) is created
- Convert to Managed on Powered Off VM (and no agent install) powers VM On
- Openstack instance clone: instances with additional storage volumes creates a blank volume on the clone instance

Appliance Updates
=================

- Missing NGINX location in ``morpheus.conf`` and ``morpheus-ssl.conf``

Agent/Node Package Updates
==========================

- Agent: Fix for symlink removal error when ``ipv4-rules`` file was removed
