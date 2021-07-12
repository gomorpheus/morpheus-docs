.. _Release Notes:

************************
|morphver| Release Notes
************************

.. No highlights this time, small update
  .. include:: highlights.rst

.. NOTE:: Items appended with :superscript:`5.3.2` are also included with that version.

New Features
============

- Huawei Cloud: Image upload functionality now supports images greater than 2GB in size. When adding/editing the Cloud, set an OBS bucket in the IMAGE STORE field as a permanent store location for Morpheus virtual images :superscript:`5.3.2`
- Hyper-V: Added discovery and inventory for Hyper-V Clouds. Mark checkbox to “INVENTORY EXISTING INSTANCES” on the add/edit Cloud modal to enable or disable this option. As with other Cloud types, discovered VMs can be converted to managed Instances and deleted with or without removing the underlying infrastructure :superscript:`5.3.2`
- Invoices: The Invoices UI no longer shows Subtenant users the cost value for invoices which are owned by the primary Tenant. Instead they will see price values (which include any price markup set by primary Tenant administrators) mirrored as the cost value
- Logging: Added support for custom NGINX log formats by updating morpheus.rb with a new log_format_name and log_format value

|morpheus| API Improvements
===========================

- Instances: The ``details`` parameter is set to ``true`` by default for API calls to GET a specific Instance. For calls to GET all Instances, the ``details`` parameter is still ``false`` by default :superscript:`5.3.2`
- Instances: The instances endpoint now returns volumes and containers lists under containerDetails to match data which was already returned for VMs :superscript:`5.3.2`
- ServiceNow Integration: Expose or unexpose |morpheus| Clouds, Library items, Blueprints, and Catalog Items to ServiceNow through |morpheus| API and CLI. Users can also view items which are currently exposed

Fixes
=====
