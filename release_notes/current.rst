v4.1.0
======

Highlights
----------

- Job executions can now be expanded to show process details in ``Provisioning > Automation > Executions``
- Individual tasks and scripts can now be run against hosts and virtual machines in ``Infrastructure > Hosts``. Previously workflows would be executed but not individual scripts or tasks.
- Clone system layouts in ``Provisioning > Library > CLUSTER LAYOUTS`` for use in custom layouts. Buttons to edit and delete existing custom layouts also appear alongside the clone button in the list view.
- Data Stores, History, and Logs tabs added to detail page for KVM clusters
- Setting to Reuse Sequence Numbers added to ``Administration > Provisioning``
- `VMWare on AWS` cloud type added to ``Infrastructure > Clouds``
- `User Data` field on images and clouds now supports YAML
- Kubernetes clusters can now be created in ``Infrastructure > Clusters > +ADD CLUSTER``
- Kubernetes blueprints can now be created in ``Provisioning > Blueprints``
- Metadata is now synced to vCenter to set tags on VMs. Existing tags are also inventoried into Morpheus as Metadata
- Static IP addresses can now be assigned on vCD cloud via Guest Customizations during instance provisioning
- `Morpheus Api` has been added as a type selection in Option Lists (``Provisioning > Library > OPTION LISTS``)

Automation tasks
^^^^^^^^^^^^^^^^^^^^^^^
- Ansible Tower automation task type added in ``Provisioning > Automation``
- `Email` tasks can now be created and added to Workflows

Subnet handling
^^^^^^^^^^^^^^^^^^^^^^^

- Added `SUBNETS` tab to the network detail page in ``Infrastructure > Network > (Your specific Network)`` which allows subnets to be searched and edited.
- Subnets can now be created and edited on an Azure VNet from ``Infrastructure > Network``.
- Azure networks sync as subnets. Previously, subnets were synced as individual networks
- Network subnets can now be selected from the `Networks` dropdown list when provisioning an instance
- Group permissions can now be modified on subnets just like networks
- Subnet options are now respected just like networks in terms of visibility, group access, and defaults
- Subnets are now selectable when adding or editing a Network Group in ``Infrastructure > Network > NETWORK GROUPS``

Fixes
----------
- Output results now appear correctly in the Execution Detail window in ``Provisioning > Automation > Executions``. Similarly, output results will also now appear correctly in the Execution Detail window in ``Provisioning > Jobs > Job Executions``.
- Fixed an issue where backups were not being created in some cases when integrating with Veeam 9.5
- Time period definitions within the specified dates are now honored in data calls to the Billing API
- Removing an instance or VM from Morpheus no longer removes serverExternalID and serverInternalID values from /api/billing records
- General improvements to Usage data
- Fixed an issue where the list of floating or elastic IP addresses available was not being immediately updated on some clouds when provisioning an instance and selecting an external IP pool for the floating IP pool
- Stopped and started usage records (``Operations > Activity > USAGE``) are no longer created when there is an error in calling the Azure API. In some cases this could cause interruptions in billing data.

Role Permission Updates
^^^^^^^^^^^^^^^^^^^^^^^

Service Version Compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When externalizing MySQL, Elasticsearch and/or RabbitMQ services, the following versions are compatible with Morpheus 4.0.0:

+---------------------------------------+----------------------+-----------------------------+
| **Service**                           |**Compatible Branch** | **4.1.0 Installed Version** |
+---------------------------------------+----------------------+-----------------------------+
| MySQL                                 | 5.7                  | 5.7.27                      |
+---------------------------------------+----------------------+-----------------------------+
| Elasticsearch: 5.6 (5.6.16 installed) | 5.6                  | 5.6.16                      |
+---------------------------------------+----------------------+-----------------------------+
| RabbitMQ: 3.7 (3.7.16 installed)      | 3.7                  | 3.7.16                      |
+---------------------------------------+----------------------+-----------------------------+
