Full HA Upgrade
^^^^^^^^^^^^^^^

Full HA configurations represent multiple app nodes with external (non-system) MySQL, RabbitMQ and Elasticsearch Clusters or Services.

|morpheus| Packages
```````````````````
|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_ 


Overview
````````
When upgrading other Appliance Configurations from 3.6.x or 4.x to |morphver| only services local to the Morpheus App node(s) will be upgraded. For fully distributed configurations (Full HA), where MySQL, RabbitMQ and Elasticsearch are external clusters or services, the upgrade process will not upgrade these services.

Refer to :ref:`compatibility` for externalized MySQL, Elasticsearch and/or RabbitMQ version requirements.

- Refer to `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to v4.1.2 if your Appliance's Elasticsearch is external.

.. important:: |morpheus| v4.1.2+ requires Elasticsearch 7.x. Earlier versions of |morpheus| ran against Elasticsearch v5.x.

    - The Elasticsearch version for Appliance configurations with the default local Elasticsearch target will automatically be upgraded and no manual upgrade is required.
    - For Appliance configurations with an existing external Elasticsearch service, an upgrade of Elasticsearch to v7.x is required to upgrade |morpheus| to v4.1.2+.
    - |morpheus| can also be pointed to a new Elasticsearch 7.x cluster or service as an alternate to upgrading an existing cluster.
    - Elasticsearch data will not be retained during a direct 5.x to 7.x upgrade by default. Please refer to Elasticsearch documentation if backing up and restoring your 5.x Elasticsearch |morpheus| data is required.
    - If log and stat data stored in Elasticsearch is not critical, a 5.x Elasticsearch data backup and restoration to 7.x, or a 5.x -> 6.x -7.x rolling upgrade is not necessary as |morpheus| will rebuild the indices upon connection to the 7.x cluster.

    - Refer to `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to v4.1.2 if your Appliance's Elasticsearch is external.

Upgrade Instructions
````````````````````


.. toctree::
   :maxdepth: 3

   deb.rst
   rpm.rst
