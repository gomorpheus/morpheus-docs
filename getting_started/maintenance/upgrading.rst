.. _upgrades:

Upgrading |morpheus|
--------------------

The following covers upgrading Morpheus Appliances to |morpheus| |morphver|.

.. important:: Morpheus v3.6.0 or higher is required to upgrade to 4.x including |morphver|.

Upgrade Requirements
^^^^^^^^^^^^^^^^^^^^

3.6.x to |morphver| Upgrade
```````````````````````````

* Only appliances running Morpheus v3.6.0 or higher can upgrade to 4.x.
* MySQL will be upgraded to 5.7.x on Appliances with MySQL running on the app node (Single Node or "all-in-one" Appliances). Backup your database before running the upgrade.

  .. important:: BACKUP YOUR DATABASE before the upgrade. You can use the appliance backup job in Morpheus, but make sure you download it before you do the upgrade.

* RabbitMQ will be upgraded to v3.7 on Appliances with RabbitMQ running on the app node (Single Node or "all-in-one" Appliances). On 3-Node configurations, the RabbitMQ queues and configuration will be dropped and the cluster will need to be configured and established again.
* Elasticsearch has a minor upgrade from 5.4 to 5.6 on Appliances with Elasticsearch running on the app node (Single Node or "all-in-one" Appliances)
* Stop all morpheus services, not just the morpheus-ui, before the upgrade. Although the upgrade process will also stop the services, take this step to ensure they are stopped.
* Warnings about missing files during the removal phase are expected and can be ignored.
* The repo download location has changed to https://downloads.morpheusdata.com from https://downloads.gomorpheus.com so if a customer has an ACL on their firewall or proxy they will need to update the ACL.

Refer to :ref:`compatibility` for externalized MySQL, Elasticsearch and/or RabbitMQ version requirements.


.. include:: /getting_started/maintenance/upgrades/single/singlenode.rst
.. include:: /getting_started/maintenance/upgrades/3node/overview.rst
.. include:: /getting_started/maintenance/upgrades/fullha/overview.rst
