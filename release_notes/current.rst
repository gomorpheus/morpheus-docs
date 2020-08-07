.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading to |morpheus| |morphver|.

|morpheus| UI Updates
*********************

Highlights
==========

New Features
============

- Amazon: Create and manage Amazon Internet Gateway routers including syncing, creating and managing routes
- NSX-T: Create, manage and delete NSX-T load balancers from the scale tab of the Instance detail page
- OpenTelekom Cloud: A floating IP can now have variable bandwidth, option is available in the Instance and App provisioning wizards
- UI: Environment Tag field relabeled as "Environment" on Group tab of the Instance provisioning wizard
- UI: Advanced views and filtering added to networks list page (Infrastructure > Networks)

Fixes
=====

|morpheus| API Updates
**********************

API Enhancements
================

- Azure: Added granular invoice and line item costing as we currently have for Amazon and Oracle Clouds
- Azure: CSP pricing support
- User Sources: The ``userSources`` API now returns ``externalLogin`` and ``allowCustomMappings`` fields

API Fixes
=========

|morpheus| CLI Updates
**********************

CLI Enhancements
================

- User Sources: External Login and Allow Custom Mappings can now be displayed

CLI Fixes
=========
