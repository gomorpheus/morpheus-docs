3-Node HA Upgrade
^^^^^^^^^^^^^^^^^

3-Node HA Appliance represent 3 App nodes with local RabbitMQ and Elasticsearch services clustered across the app nodes, and an external Galera/Percona MySQL cluster.

|morpheus| Packages
```````````````````
|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_ 


3.6.x -> 4.x upgrade 
....................

When upgrading a 3-Node appliance from 3.6.x to |morphver| the following services will be upgraded:

- RabbitMQ upgrade to v3.7
- Elasticsearch upgrade to v7.4

The upgrade process will not upgrade the external MySQL node(s). Refer to :ref:`compatibility` for externalized database version requirements.

Due to RabbitMQ going from 3.4 to 3.7, which has no rolling upgrade path, the RabbitMQ queues and configuration will be dropped, and the cluster will need to be configured and established again. This also ensures new queues are created using our new declaration settings, and removes any old queues not in use anymore.

.. important:: Due to the RabbitMQ upgrade from 3.4 to 3.7, the RabbitMQ configuration will be dropped and the cluster will need to be configured and established again.

4.2.1 -> 4.2+ upgrade 
.....................

|morpheus| has added added improvements to system RabbitMQ configs to enhance upgrading multi-node configurations using the system (morpheus) RabbitMQ cluster. Each node can be upgraded one at a time or all nodes can be upgraded at once and the RabbitMQ Cluster config will persist and the cluster will recover on start-up. It is no longer required to reestablish system RabbitMQ clusters after upgrades in multi-node/HA configurations using the system RabbitMQ service.

.. toctree::
   :maxdepth: 3

   deb.rst
   rpm.rst
