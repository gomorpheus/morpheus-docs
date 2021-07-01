.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Items appended with :superscript:`5.2.x` are also included in that version

.. include:: highlights.rst

New Features
============

- Clouds: Added scale factor setting for Instance scaling at provision time to all cloud integrations that didn't currently support it
- Google Cloud: Added disk type selection support. When provisioning (Instances, Apps, Clusters), cloning and reconfiguring, choose standard, balanced or ssd disk types. Pricing is synced based on the selected disk type and disk type information is onboarded or updated on Cloud sync
- Job Executions: A job execution record is now created for every target the job is run against, previously a record was only created for the last target the job was run against
- Job Executions: UI updated with a detail page for each job execution providing easier access to process outputs and error messages for each Task and target associated with the job
- Job Executions: The search bar on the Job Executions tab is updated to search against and return executions based on the target name in addition to the job name which was already searched
- NSX-T: Create and manage NSX-T load balancer profiles (Infrastructure > Load Balancers > Selected Load Balancer > Profiles Tab), previously this tab was read-only:superscript:`5.2.6`
- Option Types: "Radio List" Option Types can now be added which present options to the provisioning user as radio buttons
- Software: Patch version numbers are now surfaced on the Software tab of server detail pages (mouse hover over software name) and in Software reports:superscript:`5.2.6`
- vCloud Director: Added support for API version 34.0 on vCD 10.2+:superscript:`5.2.6`
- VMware vCenter: CPU and memory hot-add settings are now evaluated independently when reconfiguring CPU and memory for vCenter Instances. Previously, these settings were evaluated as a group rather than independently which could cause VMs to be restarted even when they were configured to support hot-add of memory and/or CPU:superscript:`5.2.7`

Fixes
=====

- UI: Some UI pages have been updated to display data differently when the number of relevant objects is high enough to potentially impact application performance:superscript:`5.2.6`

Appliance & Agent Updates
=========================

Refer to :ref:`compatibility` for additional details.

|morpheus| API & CLI Improvements
=================================

- Instances: The ``details`` parameter is set to ``true`` by default for API calls to GET a specific Instance. For calls to GET all Instances, the ``details`` parameter is still ``false`` by default
- Instances: The ``instances`` endpoint now returns ``volumes`` and ``containers`` lists under ``containerDetails`` to match data which was already returned for VMs
- NSX-T: Subtenant users can access shared NSX-T integrations and load balancers through Morpheus API and CLI as they already can through Morpheus UI:superscript:`5.2.6`
- NSX-V: Router management support added in Morpheus API and CLI to match functionality currently available in Morpheus UI:superscript:`5.2.6`
- Servers: The ``servers`` API endpoint returns the ``volumes`` and ``controllers`` lists when passing the ``details=true`` parameter to match behavior already included with the ``instances`` endpoint

Fixes
-----
