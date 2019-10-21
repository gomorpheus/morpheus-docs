Morpheus Documentation
======================

What's new in v4.1.0
--------------------

.. |vro| image:: /images/automation/tasks/vro_logo.png
.. |email| image:: /images/automation/tasks/email_logo.png
.. |ansibletower| image:: /images/automation/tasks/ansible_tower_logo.png
.. |typeahead| image:: /provisioning/library/typeahead.png

.. important:: v3.6.0 or later required to upgrade to 4.1.0. Upgrading from v3.6.x to v4.x contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x a database backup is recommended due to MySQL version upgrade.

VMware on AWS support added
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /images/infrastructure/clouds/vmwareCloudAws.png

- ``VMware on AWS`` Clouds can now be added to Morpheus
- ``VMware on AWS`` Cloud Type Added
- ``VMware on AWS`` Clouds support the same Feature set as VMware vCenter Clouds

vRealize Orchestrator Integration (vRO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|vro|

Morpheus now integrates with vRealize Orchestrator to call any VRO workflow via Morpheus tasks.

- Syncs all available vRO workflows by category
- These workflows can also be chained easily into non-vRO workflows
- ``vRealize Orchestrator Workflow`` (vRO) Task Type added. Executes Workflow from any vRO integration. Parameter Body accepts JSON.

.. image:: /images/automation/tasks/vROSample.gif
   :width: 600

New Automation Task Types
^^^^^^^^^^^^^^^^^^^^^^^^^
|ansibletower|

New ``Ansible Tower Job`` Task Type added. Executes a Job from any Ansible Tower integration with inventory, group, execution mode and target options.

|email|

New ``Email`` Task Type added. Sends email to specified address with defined subject and body upon successful workflow execution. Address, Subject and Body fields support variables, and body field supports html.

|vro|

New ``vRealize Orchestrator Workflow`` (vRO) Task Type added. Executes Workflow from any vRO integration. Parameter Body accepts JSON.

Option Types & Lists Enhancements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
New ``Typeahead`` Option Type with multi-selection support. Presents an Option List in a typeahead field vs the dropdown selection list field in ``Select List`` types.

.. image:: /provisioning/library/typeahead.png

New ``Morpheus API`` Option List type with Clouds, Groups, Instances, Instances Wiki, Servers and Servers Wiki object targets.

New ``REQUEST SCRIPT`` field added to ``REST`` and ``Morpheus API`` option list settings. Create a js script to prepare the request. Return a data object as the body. The input data is provided as data and the result should be put on the global variable results.

.. image:: /provisioning/library/morphuesApiOptionType.png

``Select`` Option Type name changed to ``Select List``

New ``DEPENDENT FIELD`` setting in ``Select List`` Option Types. Allows using results from a previous Option Type in a ``Select List`` Option List script. Data will reload when an associated dependent fields value is defined or changed.

.. image:: /provisioning/library/dependentField.png

Additional Changes and Improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Ansible: Removed requirement of an Ansible Integration being set on a Group or Cloud Configuration Management setting for Windows playbooks to execute via WinRM.
- Appliance: Quartz removed from system services
- AWS: Amazon M5A and M5AD Plans (Amazon Instance Types) added
- Cloud-Init: ``USER DATA (LINUX)`` field on Virtual Image and Clouds Settings now supports Cloud Config Data YAML
- Jobs: Job executions can now be expanded to show process details in ``Provisioning > Automation > Executions``
- KVM: Clusters: Data Stores, History, and Logs tabs added to detail page for KVM clusters
- Library: ``Clone`` action added to clone system layouts in ``Provisioning > Library > CLUSTER LAYOUTS`` for use in custom layouts.
- Localization: German l8n properties updated with improved translations.
- Openstack: Added support for Openstack Availability Zones
- Provisioning: ``Reuse Naming Sequence Numbers`` setting added to ``Administration > Provisioning``. If enabled, ${sequence} numbers used in naming patterns will be re-used once they are available again. When disabled, ${sequence} numbers will always increase by one, ensuring the same number in a pattern is never re-used (default and previous behavior).
- SCVMM: Listed datastore names for SCVMM instances (``Infrastructure > Clouds > DATASTORES``) are now prefixed with the host or cluster name for easier identification
- ServiceNow: CMDB: CMDB Target table now customizable
- ServiceNow: CMDB: Custom Mapping for CMDB records added
- Subnets can be created and edited from ``Infrastructure > Network``.
- Subnets now represented as type: subnet and are nested under parent networks when appropriate.
- Upcloud: Added Morpheus-provided catalog image for Ubuntu 18 on UpCloud
- vCloud Director: Added support for Static IP assignment via Guest Customizations in vCD.
- VMware: Tagging support added. Metadata is now synced to vCenter to set tags on VMs. Existing tags are also inventoried into Morpheus as Metadata.


Fixes
-----
- Stopped and started usage records are created appropriately for managed and unmanaged instances on each cloud sync when stopping or starting them outside of Morpheus
- Output results now appear correctly in the Execution Detail window in ``Provisioning > Automation > Executions``. Similarly, output results will also now appear correctly in the Execution Detail window in ``Provisioning > Jobs > Job Executions``.
- Fixed an issue where backups were not being created in some cases when integrating with Veeam 9.5
- Time period definitions within the specified dates are now honored in data calls to the Billing API
- Removing an instance or VM from Morpheus no longer removes serverExternalID and serverInternalID values from /api/billing records
- General improvements to Usage data
- Fixed an issue where the list of floating or elastic IP addresses available was not being immediately updated on some clouds when provisioning an instance and selecting an external IP pool for the floating IP pool
- Stopped and started usage records (``Operations > Activity > USAGE``) are no longer created when there is an error in calling the Azure API. In some cases this could cause interruptions in billing data.

CLI
---

v4.1.0

CLI Enhancements
^^^^^^^^^^^^^^^^
- New command ``clusters``
- New command ``networks list-subnets|get-subnet|etc`` for managing network subnets.
- New option ``user-settings --user-id`` for managing other users tokens,etc.
- Updated roles add and roles update to support the ``--payload`` option.
- New command ``networks list-subnets|get-subnet|etc`` for managing network subnets.
- New subcommand ``containers logs``

CLI Fixes
^^^^^^^^^
- Fix issue with ``library-option-lists update`` not allowing arbitrary ``-O`` options.
- Fix error seen with ``library-node-type remove``.

Service Version Compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When externalizing MySQL, Elasticsearch and/or RabbitMQ services, the following versions are compatible with Morpheus 4.1.0:

+---------------------------------------+----------------------+-----------------------------+
| **Service**                           |**Compatible Branch** | **4.1.0 Installed Version** |
+---------------------------------------+----------------------+-----------------------------+
| MySQL                                 | 5.7                  | 5.7.27                      |
+---------------------------------------+----------------------+-----------------------------+
| Elasticsearch: 5.6 (5.6.16 installed) | 5.6                  | 5.6.16                      |
+---------------------------------------+----------------------+-----------------------------+
| RabbitMQ: 3.7 (3.7.16 installed)      | 3.7                  | 3.7.16                      |
+---------------------------------------+----------------------+-----------------------------+

Security
^^^^^^^^
CVEs remediated in 4.1.0

- CVE-2019-8323 - RubyGems 2.7
- CVE-2019-13990 - quartz-2.2.4


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
   :maxdepth: 4
   :caption: Release Notes

   release_notes/current.rst
   release_notes/compatibility.rst
   release_notes/previousReleases.rst


.. |morpheus| replace:: Morpheus
