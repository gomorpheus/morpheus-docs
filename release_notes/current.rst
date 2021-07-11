.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Items appended with :superscript:`5.2.x` are also included in that version

.. might not do highlights this time
  .. include:: highlights.rst

New Features
============

- Clouds: Added scale factor setting for Instance scaling at provision time to all cloud integrations that didn't currently support it
- Clouds: All Cloud types now have the option to skip |morpheus| Agent installation at provision time. Previously this was only supported on the most commonly-used Cloud types
- Google Cloud: Added disk type selection support. When provisioning (Instances, Apps, Clusters), cloning and reconfiguring, choose standard, balanced or ssd disk types. Pricing is synced based on the selected disk type and disk type information is onboarded or updated on Cloud sync
- Costing: Added a standard costing service with invoice support (Operations > Costing > Invoices) for on-prem clouds to mirror the public cloud real-time costing experience. This functionality must be enabled by setting the COSTING field to "Sync Costing" in the Advanced Options section of the add/edit Cloud modal (Infrastructure > Clouds > Selected Cloud > EDIT button)
- Huawei Cloud: Image upload functionality now supports images greater than 2GB in size. When adding/editing the Cloud, set an OBS bucket in the IMAGE STORE field as a permanent store location for |morpheus| virtual images
- Hyper-V: Added discovery and inventory for Hyper-V Clouds. Mark checkbox to "INVENTORY EXISTING INSTANCES" on the add/edit Cloud modal to enable or disable this option. As with other Cloud types, discovered VMs can be converted to managed Instances and deleted with or without removing the underlying infrastructure
- Job Executions: A job execution record is now created for every target the job is run against, previously a record was only created for the last target the job was run against
- Job Executions: UI updated with a detail page for each job execution providing easier access to process outputs and error messages for each Task and target associated with the job
- Job Executions: The search bar on the Job Executions tab is updated to search against and return executions based on the target name in addition to the job name which was already searched
- NSX-T: Create and manage NSX-T load balancer profiles (Infrastructure > Load Balancers > Selected Load Balancer > Profiles Tab), previously this tab was read-only :superscript:`5.2.6`
- Open Telekom Cloud: Image upload functionality now supports images greater than 2GB in size. When adding/editing the Cloud, set an OBS bucket in the IMAGE STORE field as a permanent store location for |morpheus| virtual images
- Option Types: "Radio List" Option Types can now be added which present options to the provisioning user as radio buttons
- Roles: Report Types tab added to user and tenant role permission sets. Assign access permission to specific reports for users with access to the Reports section under the Operations menu
- Software: Patch version numbers are now surfaced on the Software tab of server detail pages (mouse hover over software name) and in Software reports :superscript:`5.2.6`
- Storage: Added support for Google Cloud Storage bucket creation and management (Infrastructure > Storage > Buckets tab)
- vCloud Director: Added support for API version 34.0 on vCD 10.2+ :superscript:`5.2.6`
- VMware vCenter: Added the option to select a folder when cloning an Instance to image (Actions menu of the Instance detail page). Previously, images were copied to the root folder
- VMware vCenter: CPU and memory hot-add settings are now evaluated independently when reconfiguring CPU and memory for vCenter Instances. Previously, these settings were evaluated as a group rather than independently which could cause VMs to be restarted even when they were configured to support hot-add of memory and/or CPU :superscript:`5.2.7`

Fixes
=====

- UI: Some UI pages have been updated to display data differently when the number of relevant objects is high enough to potentially impact application performance :superscript:`5.2.6`

Appliance & Agent Updates
=========================

Refer to :ref:`compatibility` for additional details.

|morpheus| API & CLI Improvements
=================================

- Instances: The ``details`` parameter is set to ``true`` by default for API calls to GET a specific Instance. For calls to GET all Instances, the ``details`` parameter is still ``false`` by default
- Instances: The ``instances`` endpoint now returns ``volumes`` and ``containers`` lists under ``containerDetails`` to match data which was already returned for VMs
- NSX-T: Subtenant users can access shared NSX-T integrations and load balancers through Morpheus API and CLI as they already can through Morpheus UI :superscript:`5.2.6`
- NSX-V: Router management support added in Morpheus API and CLI to match functionality currently available in Morpheus UI :superscript:`5.2.6`
- Option Lists: API calls to get all Option Lists (``api/option-type-lists/``) or get a specific Option List (``api/option-type-lists/:id``) no longer return ``listItems`` as this could potentially return millions of values in some scenarios. Users can now issue a GET request to ``/api/option-type-lists/:id/items`` to return all items in a specific Option List
- Servers: The ``servers`` API endpoint returns the ``volumes`` and ``controllers`` lists when passing the ``details=true`` parameter to match behavior already included with the ``instances`` endpoint
