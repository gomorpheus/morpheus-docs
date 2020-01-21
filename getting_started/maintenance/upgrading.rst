.. _upgrading:

Upgrading |morpheus|
--------------------

.. important:: |morpheus| v4.1.2+ requires Elasticsearch 7.x. Earlier versions of |morpheus| ran against Elasticsearch v5.x.

    - The Elasticsearch version for Appliance configurations with the default local Elasticsearch target will automatically be upgraded and no manual upgrade is required.
    - For Appliance configurations with an existing external Elasticsearch service, an upgrade of Elasticsearch to v7.x is required to upgrade |morpheus| to v4.1.2+.
    - |morpheus| can also be pointed to a new Elasticsearch 7.x cluster or service as an alternate to upgrading an existing cluster.
    - Elasticsearch data will not be retained during a direct 5.x to 7.x upgrade by default. Please refer to Elasticsearch documentation if backing up and restoring your 5.x Elasticsearch |morpheus| data is required.
    - If log and stat data stored in Elasticsearch is not critical, a 5.x Elasticsearch data backup and restoration to 7.x, or a 5.x -> 6.x -7.x rolling upgrade is not necessary as |morphues| will rebuild the indices upon connection to the 7.x cluster.

    - Please refer to `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to v4.1.2 if your Appliance's Elasticsearch is external.

Upgrade Requirements
^^^^^^^^^^^^^^^^^^^^

3.6.x to |morphver| Upgrade
```````````````````````````

* Only appliances running Morpheus v3.6.0 or higher can upgrade to 4.x.
* MySQL will be upgraded to 5.7.x on Appliances with MySQL running on the app node (Single Node or "all-in-one" Appliances). Backup your database before running the upgrade.

  .. important:: BACKUP YOUR DATABASE before the upgrade. You can use the appliance backup job in Morpheus, but make sure you download it before you do the upgrade.

* RabbitMQ will be upgraded to v3.7 on Appliances with RabbitMQ running on the app node (Single Node or "all-in-one" Appliances). On 3-Node configurations, the RabbitMQ queues and configuration will be dropped and the cluster will need to be configured and established again.
* Elasticsearch will be upgraded from 5.x to 7.x. Refer to `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ for upgrading external ES Clusters.
* Stop all morpheus services, not just the morpheus-ui, before the upgrade. Although the upgrade process will also stop the services, take this step to ensure they are stopped.
* Warnings about missing files during the removal phase are expected and can be ignored.
* The repo download location has changed to https://downloads.morpheusdata.com from https://downloads.gomorpheus.com so if a customer has an ACL on their firewall or proxy they will need to update the ACL.

Refer to :ref:`compatibility` for externalized MySQL, Elasticsearch and/or RabbitMQ version requirements.

4.x to |morphver| Upgrade
`````````````````````````

* Elasticsearch will be upgraded from 5.x to 7.x. Refer to `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ for upgrading external ES Clusters.

.. toctree::
   :maxdepth: 2
      
   upgrades/single/singlenode.rst
   upgrades/3node/overview.rst
   upgrades/fullha/overview.rst
