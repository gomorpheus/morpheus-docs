Full HA Upgrade
^^^^^^^^^^^^^^^

When upgrading other Appliance Configurations from 3.6.x or 4.x to |morphver| only services local to the Morpheus App node(s) will be upgraded. For fully distributed configurations (Full HA), where MySQL, RabbitMQ and Elasticsearch are external clusters, the upgrade process will not upgrade these services.

Refer to :ref:`compatibility` for externalized MySQL, Elasticsearch and/or RabbitMQ version requirements.

.. include:: /getting_started/maintenance/upgrades/fullha/deb.rst
.. include:: /getting_started/maintenance/upgrades/fullha/rpm.rst
