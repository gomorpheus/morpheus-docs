Blueprints
==========

Overview
--------

The Blueprints section is used to compose provisioning catalogs. The Blueprints section is composed of:

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
.. include:: /library/blueprints/appBlueprints.rst

..
  CATALOG BUILDER SECTION

.. include:: /library/blueprints/self-service.rst

..
  CLUSTER LAYOUTS SECTION BELOW

.. include:: /library/blueprints/clusterLayouts.rst
