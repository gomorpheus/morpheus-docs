.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. Small Update, omitting highlights this time
  .. include:: highlights.rst

New Features
============

- Backups: Azure VMs can now be restored to a current Instance, previously they needed to be restored to a new Instance
- Clouds: Grant read-level access to Clouds for Tenants through the applied Tenant Role
- Policies: Policy types including budget, max cores, max hosts, max memory, and max storage are now considered when provisioning a new cluster or when adding a new host to an existing cluster
- Policies: When provisioning Apps, Instance types containing multiple nodes (such as Redis master/replica) or Instances with scale factor are considered against policy types including budget, max containers, max cores, max memory, max storage, and max VM
- Policies: When completing cart checkout in the Service Catalog Persona view, the sum of all ordered items within the cart are considered against any policies that may be in place
- Terraform: Support added for Terraform v0.14
- UI: Executions list page (Automation > Executions) now automatically refreshes to display new executions

|morpheus| API & CLI Improvements
=================================

Clone: "Clone To Image" action added for API/CLI

Fixes
=====

..
  Morpheus Hub
  ============

  Appliance Updates
  =================

  Agent/Node Package Updates
  ==========================
