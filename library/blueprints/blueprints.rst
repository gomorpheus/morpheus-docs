Blueprints
==========

Overview
--------

The Blueprints section is used to add Virtual Images as custom Instance Types to the provisioning catalog. The Library section is composed of:

* Instance Types
* Layouts
* Node Types
* App Blueprints
* Catalog Items
* Cluster Layouts

Additionally, items from Options and Templates sections are incorporated to call in custom options for users, IaaS spec files, scripts, and more. See Options and Templates within |morpheus| Library for more information on creating or sourcing the items below from version control. In some cases, they may need to be pre-existing for the most efficient creation of Blueprints.

* Inputs
* Option Lists
* File Templates
* Scripts
* Spec Templates

Blueprint Development Overview
------------------------------

When provisioning, the User selects an INSTANCE TYPE from the provisioning wizard. At this stage, we can present custom INPUTS to the User which alter deployment in ways the administrator predetermines. Based on the selected Cloud technology and Version, the User is presented with applicable LAYOUTS selections. LAYOUTS can take advantage of Workflows which automate Tasks and can utilize a wide range of DevOps automation technologies. One or more NODE TYPES is associated with the LAYOUT. NODE TYPES are the bridge between LAYOUTS and Images. NODE TYPES can also take advantage of File Templates for custom configuration and Scripts which can be queued to run at any stage of the Instance lifecycle.

.. image:: /images/provisioning/library/library_item_transparent.png
  :align: center

.. include:: /library/blueprints/instance_types.rst
.. include:: /library/blueprints/layouts.rst
.. include:: /library/blueprints/node_types.rst

App Blueprint Overview
----------------------

App Blueprints support a vast array of providers and configurations with programmatic markup or Infrastructure as Code capabilities. Blueprints configs can be manually added or scoped to a git repo. |morpheus| blueprints allows for full automation configuration, locked fields, tiered boots, and linked tiers with exported evars. All blueprints have permission settings for controlling group and tenant access.

App Blueprint Types
-------------------

- |morpheus|
- Terraform
- ARM (Azure)
- CloudFormation (AWS)
- Kubernetes
- Helm

.. include:: /provisioning/blueprints/morpheus.rst
.. include:: /provisioning/blueprints/terraform.rst
.. include:: /provisioning/blueprints/arm.rst
.. include:: /provisioning/blueprints/cloudFormation.rst
.. include:: /provisioning/blueprints/kubernetes.rst
.. include:: /provisioning/blueprints/helm.rst

..
  CATALOG BUILDER SECTION

.. include:: /library/blueprints/self-service.rst

..
  CLUSTER LAYOUTS SECTION BELOW

.. include:: /library/blueprints/clusterLayouts.rst
