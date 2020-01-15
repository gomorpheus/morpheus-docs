Other Appliance Configurations Upgrades
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When upgrading other Appliance Configurations from 3.6.x or 4.x to |morphver| only services local to the Morpheus App node(s) will be upgraded. For fully distributed configurations, where MySQL, RabbitMQ and Elasticsearch are external, the upgrade process will not upgrade the external services.

Refer to :ref:`compatibility` for externalized MySQL, Elasticsearch and/or RabbitMQ version requirements.

Refer to :ref:`esupgrade` for upgrading external ES Clusters.

.. important:: |morpheus| v4.1.2+ requires Elasticsearch 7.x. Earlier versions of |morpheus| ran against Elasticsearch v5.x. The Elasticsearch version for Appliance configurations with the default local Elasticsearch target will automatically be upgraded and no manual upgrade is required. For Appliance configurations with an existing external Elasticsearch service, an upgrade of Elasticsearch to v7.x is required to upgrade |morpheus| to v4.1.2+. |morpheus| can be pointed to a new Elasticsearch 7.x service as an alternate to upgrading an existing cluster. Elasticsearch 7.x upgrade is really a new install, as by default no data will be retained. Please refer to Elasticsearch documentation if backing up and restoring your 5.x Elasticsearch |morpheus| data is required. For most users, the log and stat data stored in Elasticsearch is not critical and the 5.x Elasticsearch data backup and restoration is not necessary. Refer to :ref:`esupgrade` for upgrading external ES Clusters.

.. important:: Elasticsearch 7.x configuration and paths are not the same as v5.x. Please pay attention to the elasticsearch.yml config changes and ensure proper permissions on specified paths. Refer to :ref:`esupgrade` for upgrading external ES Clusters.
