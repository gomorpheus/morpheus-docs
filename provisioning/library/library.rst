Library
=======

Overview
--------

The Library section is used to add Virtual Images as custom Instance Types to the provisioning catalog. The Library section is composed of:

* Instance Types
* Layouts
* Node Types
* Option Types
* Option Lists
* File Templates
* Scripts
* Spec Templates
* Cluster Layouts

When provisioning, the User selects an INSTANCE TYPE from the provisioning wizard. At this stage, we can present custom OPTION TYPES to the User which alter deployment in ways the administrator predetermines. Based on the selected Cloud technology and Version, the User is presented with applicable LAYOUTS selections. LAYOUTS can take advantage of Workflows which automate Tasks and can utilize a wide range of DevOps automation technologies. One or more NODE TYPES is associated with the LAYOUT. NODE TYPES are the bridge between LAYOUTS and Images. NODE TYPES can also take advantage of File Templates for custom configuration and Scripts which can be queued to run at any stage of the Instance lifecycle.

.. image:: /images/provisioning/library/library_items_final.png

.. include:: /provisioning/library/instance_types.rst
.. include:: /provisioning/library/layouts.rst
.. include:: /provisioning/library/node_types.rst
.. include:: /provisioning/library/option_types.rst
.. include:: /provisioning/library/option_lists.rst
.. include:: /provisioning/library/file_templates.rst
.. include:: /provisioning/library/scripts.rst
.. include:: /provisioning/library/specTemplates.rst
.. include:: /provisioning/library/clusterLayouts.rst
