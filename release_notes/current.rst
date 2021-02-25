.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. Small Update, omitting highlights this time
  .. include:: highlights.rst
.. important:: In 5.2.3 ``codeready`` (codeready-builder-for-rhel-8-x86_64-rpms) repo access required for RHEL 8+ Appliances, replacing the previous PowerTools/powertools requirement.

New Features
============

- Activity: View results, including any errors, from teardown-phase Tasks on History page (Operations > Activity > History). Previously, cleanup errors were not visible because this page did not show any Instance activity after the Instance was deleted
- CloudFormation: Values entered into password fields are no longer revealed in plaintext on the summary tab of the App provisioning wizard during provisioning
- NSX-V: Priority is now displayed for firewall groups and rules on the Firewall tab of NSX-V integrations
- Policies: Cloning Instances now respects policies such as budget, max containers, max cores, max memory, and max storage
- Prices and Plans: Price Set and Pricing Plan types added for VMware virtual image billing
- Self- Service Catalog Tool: Configure Catalog Apps using the familiar App provisioning wizard. Previously, Catalog Apps were configured by selecting an existing Blueprint and at least setting minimally-required App Spec with YAML
- Tasks: Set Shell Script Tasks to run as ``sudo`` by marking the added check box
- Virtual Images: Added the option to also remove Virtual Images from VMware clouds when deleting them out of |morpheus|
- Workflows: Startup and Shutdown phases added for Provisioning Workflows. Tasks in the Startup phase run after the target is started and Tasks in the Shutdown phase run immediately before the target is shutdown

|morpheus| API & CLI Improvements
=================================


..
  Morpheus Hub
  ============


Fixes
=====


Appliance Updates
=================


Agent/Node Package Updates
==========================
