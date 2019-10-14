
Morpheus Documentation
======================

What's new in v4.1.0
--------------------

.. important:: v3.6.0 or later required to upgrade to 4.1.0. Upgrading from v3.6.x to v4.x contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x a database backup is recommended due to MySQL version upgrade.

Highlights
----------

vRealize Orchestrator Integration (vRO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Syncs all available vRO workflows by category
- These workflows can also be chained easily into non-vRO workflows
- ``vRealize Orchestrator Workflow`` (vRO) Task Type added. Executes Workflow from any vRO integration. Parameter Body accepts JSON.

New Automation Task Types
^^^^^^^^^^^^^^^^^^^^^^^^^
- New ``Ansible Tower Job`` Task Type added. Executes a Job from any Ansible Tower integration with inventory, group, execution mode and target options.
- ``Email`` Task Type added. Sends email to specified address with defined subject and body upon successful workflow execution. Address, Subject and Body fields support variables, and body field supports html.
- ``vRealize Orchestrator Workflow`` (vRO) Task Type added. Executes Workflow from any vRO integration. Parameter Body accepts JSON.

Option Types & Lists Enhancements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- New ``Typeahead`` Option Type with multi-selection support. Presents an Option List in a typeahead field vs the dropdown selection list field in ``Select List`` types.
- New ``Morpheus API`` Option List type with Clouds, Groups, Instances, Instances Wiki, Servers and Servers Wiki object targets.
- New ``REQUEST SCRIPT`` field added to ``REST`` and ``Morpheus API`` option list settings. Create a js script to prepare the request. Return a data object as the body. The input data is provided as data and the result should be put on the global variable results.
- ``Select`` Option Type name changed to ``Select List``
- New ``DEPENDENT FIELD`` setting in ``Select List`` Option Types. Allows using results from a previous Option Type in a ``Select List`` Option List script. Data will reload when an associated dependent fields value is defined or changed.

Subnets
^^^^^^^
- Added `SUBNETS` tab to the network detail page in ``Infrastructure > Network > (Your specific Network)`` which allows subnets to be searched and edited.
- Subnets can now be created and edited on an Azure VNet from ``Infrastructure > Network``.
- Azure networks sync as subnets. Previously, subnets were synced as individual networks
- Network subnets can now be selected from the `Networks` dropdown list when provisioning an instance
- Group permissions can now be modified on subnets just like networks
- Subnet options are now respected just like networks in terms of visibility, group access, and defaults
- Subnets are now selectable when adding or editing a Network Group in ``Infrastructure > Network > NETWORK GROUPS``

VMware on AWS support added
^^^^^^^^^^^^^^^^^^^^^^^^^^^
- ``VMware on AWS`` Clouds can now be added to Morpheus
- ``VMware on AWS`` Cloud Type Added
- ``VMware on AWS`` Clouds support the same Feature set as VMware vCenter Clouds


Additional Changes and Improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Jobs: Job executions can now be expanded to show process details in ``Provisioning > Automation > Executions``
- Library: ``Clone`` action added to clone system layouts in ``Provisioning > Library > CLUSTER LAYOUTS`` for use in custom layouts.
- KVM: Clusters: Data Stores, History, and Logs tabs added to detail page for KVM clusters
- Provisioning: ``Reuse Naming Sequence Numbers`` setting added to ``Administration > Provisioning``. If enabled, ${sequence} numbers used in naming patterns will be re-used once they are available again. When disabled, ${sequence} numbers will always increase by one, ensuring the same number in a pattern is never re-used (default and previous behavior).
- Cloud-Init: ``USER DATA (LINUX)`` field on Virtual Image and Clouds Settings now supports Cloud Config Data YAML
- VMware: Tagging support added. Metadata is now synced to vCenter to set tags on VMs. Existing tags are also inventoried into Morpheus as Metadata.
- vCloud Director: Added support for Static IP assignment via Guest Customizations in vCD.
- ServiceNow: CMDB: CMDB Target table now customizable
- ServiceNow: CMDB: Custom Mapping for CMDB records added
- SCVMM: Listed datastore names for SCVMM instances (``Infrastructure > Clouds > DATASTORES``) are now prefixed with the host or cluster name for easier identification
- AWS: Amazon M5A and M5AD Plans (Amazon Instance Types) added
- Openstack: Added support for Openstack Availability Zones
- Upcloud: Added Morpheus-provided catalog image for Ubuntu 18 on UpCloud
- Localization: German l8n properties updated with improved translations.
- Ansible: Removed requirement of an Ansible Integration being set on a Group or Cloud Configuration Management setting for Windows playbooks to execute via WinRM.
- Appliance: Quartz removed


.. toctree::
   :maxdepth: 3
   :caption: Morpheus UI

   getting_started/getting_started
   provisioning/provisioning
   infrastructure/infrastructure
   administration/administration
   monitoring/monitoring
   logs/logs
   backups/backups
   operations/operations
   tools/tools
   integration_guides/integration_guides
   troubleshooting/troubleshooting


.. toctree::
   :maxdepth: 3
   :caption: Morpheus CLI

   cli/install
   cli/walkthrough
   cli/shell
   cli/commands
   cli/changelog

.. toctree::
   :maxdepth: 3
   :caption: Morpheus API

   api/intro
   api/requests

.. toctree::
   :maxdepth: 3
   :caption: Release Notes

   release_notes/current.rst
   release_notes/previousReleases.rst


.. |morpheus| replace:: Morpheus
