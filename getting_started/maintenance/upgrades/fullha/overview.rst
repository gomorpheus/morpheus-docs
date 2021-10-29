Full HA Upgrade
^^^^^^^^^^^^^^^

Full HA configurations represent multiple app nodes with external (non-system) MySQL, RabbitMQ and Elasticsearch Clusters or Services.

|morpheus| Packages
```````````````````
|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_ 

Overview
````````
When upgrading to |morphver| only services local to the Morpheus App node(s) will be upgraded. For fully distributed configurations (Full HA) where MySQL, RabbitMQ and Elasticsearch are external, the upgrade process will not upgrade these services.

Refer to :ref:`compatibility` for externalized MySQL, Elasticsearch and/or RabbitMQ version requirements.

Upgrade Instructions
````````````````````

.. toctree::
   :maxdepth: 3

   deb.rst
   rpm.rst

.. WARNING:: Upgrades can add additional storage load on database nodes. Please refer to database storage requirements within :ref:`perconainstall` before upgrading.
