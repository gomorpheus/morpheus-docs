v4.1.0
======

Highlights
----------
- Job executions can now be expanded to show process details in ``Provisioning > Automation > Executions``
- Added `SUBNETS` tab to the network detail page in ``Infrastructure > Network > (Your specific Network)`` which allows subnets to be searched and edited. Subnets can also be created on an Azure VNet.
- Individual tasks and scripts can now be run against hosts and virtual machines in ``Infrastructure > Hosts``. Previously workflows would be executed but not individual scripts or tasks.
- Clone system layouts in ``Provisioning > Library > CLUSTER LAYOUTS`` for use in custom layouts. Buttons to edit and delete existing custom layouts also appear alongside the clone button in the list view.
- Ansible Tower automation task type added in ``Provisioning > Automation``
- Data Stores, History, and Logs tabs added to detail page for KVM clusters
- Setting to Reuse Sequence Numbers added to ``Administration > Provisioning``
- `VMWare on AWS` cloud type added to ``Infrastructure > Clouds``
- `User Data` field on images and clouds now supports YAML
- Kubernetes clusters can now be created in ``Infrastructure > Clusters > +ADD CLUSTER``
- Kubernetes blueprints can now be created in ``Provisioning > Blueprints``
- Azure networks sync as subnets. Previously, subnets were synced as individual networks
- Network subnets can now be selected from the `Networks` dropdown list when provisioning an instance
- Updates to Morpheus API and CLI to handle management of Kubernetes cluster namespaces
- Updates to Morpheus API and CLI to handle management of Kubernetes and Docker cluster workers

Fixes
----------
- Output results now appear correctly in the Execution Detail window in `Provisioning > Automation > Executions`. Similarly, output results will also now appear correctly in the Execution Detail window in `Provisioning > Jobs > Job Executions`.
- Fixed an issue where backups were not being created in some cases when integrating with Veeam 9.5
- Time period definitions within the specified dates are now honored in data calls to the Billing API
- Removing an instance or VM from Morpheus no longer removes serverExternalID and serverInternalID values from /api/billing records
- General improvements to Usage data

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
