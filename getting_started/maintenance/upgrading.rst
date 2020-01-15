Upgrading
---------

.. important:: |morpheus| v4.1.2+ requires Elasticsearch 7.x. Earlier versions of |morpheus| ran against Elasticsearch v5.x. The Elasticsearch version for Appliance configurations with the default local Elasticsearch target will automatically be upgraded and no manual upgrade is required. For Appliance configurations with an existing external Elasticsearch service, an upgrade of Elasticsearch to v7.x is required to upgrade |morpheus| to v4.1.2+. |morpheus| can be pointed to a new Elasticsearch 7.x service as an alternate to upgrading an existing cluster. Elasticsearch 7.x upgrade is really a new install, as by default no data will be retained. Please refer to Elasticsearch documentation if backing up and restoring your 5.x Elasticsearch |morpheus| data is required. For most users, the log and stat data stored in Elasticsearch is not critical and the 5.x Elasticsearch data backup and restoration is not necessary. Refer to :ref:`esupgrade` for upgrading external ES Clusters.

.. important:: Elasticsearch 7.x configuration and paths are not the same as v5.x. Please pay attention to the elasticsearch.yml config changes and ensure proper permissions on specified paths. will be upgraded from 5.x to 7.x. Refer to :ref:`esupgrade` for upgrading external ES Clusters.


3.6.x to |morphver| Upgrade Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Only appliances running Morpheus v3.6.0 or higher can upgrade to 4.x.
* MySQL will be upgraded to 5.7.x on Appliances with MySQL running on the app node (Single Node or "all-in-one" Appliances). Backup your database before running the upgrade.

  .. important:: BACKUP YOUR DATABASE before the upgrade. You can use the appliance backup job in Morpheus, but make sure you download it before you do the upgrade.

* RabbitMQ will be upgraded from 3.4.x to 3.7.x. On 3-Node configurations, the RabbitMQ queues and configuration will be dropped and the cluster will need to be configured and established again.
* Elasticsearch will be upgraded from 5.x to 7.x. Refer to :ref:`esupgrade` for upgrading external ES Clusters.
* Stop all morpheus services, not just the morpheus-ui, before the upgrade. Although the upgrade process will also stop the services, take this step to ensure they are stopped.
* Warnings about missing files during the removal phase are expected and can be ignored.
* The repo download location has changed to https://downloads.morpheusdata.com from https://downloads.gomorpheus.com so if a customer has an ACL on their firewall or proxy they will need to update the ACL.

Refer to :ref:`compatibility` for externalized MySQL, Elasticsearch and/or RabbitMQ version requirements.

4.x to |morphver| Upgrade Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Elasticsearch will be upgraded from 5.x to 7.x. Refer to :ref:`esupgrade` for upgrading external ES Clusters.

.. include:: /getting_started/maintenance/upgrades/singleNodeUpgrade.rst
.. include:: /getting_started/maintenance/upgrades/3NodeUpgrade.rst
.. include:: /getting_started/maintenance/upgrades/fullHaUpgrade.rst
.. include:: /getting_started/maintenance/upgrades/esupgrade.rst
