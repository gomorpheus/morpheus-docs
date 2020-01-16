3-Node HA Upgrade
^^^^^^^^^^^^^^^^^

3-Node HA Appliance represent 3 App nodes with local RabbitMQ and Elasticsearch services clustered across the app nodes, and an external Galera/Percona MySQL cluster.

When upgrading a 3-Node appliance from 3.6.x to |morphver| the following services will be upgraded:

- RabbitMQ upgrade to v3.7
- Elasticsearch upgrade to v5.6

The upgrade process will not upgrade the external MySQL node(s). Refer to :ref:`compatibility` for externalized database version requirements.

Due to RabbitMQ going from 3.4 to 3.7, which has no rolling upgrade path, the RabbitMQ queues and configuration will be dropped, and the cluster will need to be configured and established again. This also ensures new queues are created using our new declaration settings, and removes any old queues not in use anymore.

.. important:: Due to the RabbitMQ upgrade from 3.4 to 3.7, the RabbitMQ configuration will be dropped and the cluster will need to be configured and established again.

.. include:: /getting_started/maintenance/upgrades/3node/deb.rst
.. include:: /getting_started/maintenance/upgrades/3node/rpm.rst
