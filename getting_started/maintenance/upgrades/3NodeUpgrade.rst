3-Node HA Appliance Upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^^^

3-Node HA Appliance represent 3 App nodes with local RabbitMQ and Elasticsearch services clustered across the app nodes, and an external Galera or Percona MySQL cluster.

When upgrading a 3-Node appliance from 3.6.x to |morphver| the following services will be upgraded:

- RabbitMQ upgrade to v3.7
- Elasticsearch upgrade to v7.4

The upgrade process will not upgrade the external MySQL node(s). Refer to :ref:`compatibility` for externalized database version requirements.

Due to RabbitMQ going from 3.4.x to 3.7.x, which has no rolling upgrade path, the RabbitMQ queues and configuration will be dropped, and the cluster will need to be configured and established again. This also ensures new queues are created using our new declaration settings, and removes any old queues not in use anymore.

.. important:: Due to the RabbitMQ upgrade from 3.4.x to 3.7.x, the RabbitMQ queues and configuration will be dropped and the cluster will need to be configured and established again.

#. Stop all Morpheus services via ``morpheus-ctl stop`` on all Nodes
2. Upgrade Node 1, then run a reconfigure on Node 1
3. Upgrade Node 2, then run a reconfigure on Node 2
4. Upgrade Node 3, then run a reconfigure on Node 3
5. Establish the RabbitMQ cluster again using the steps from the :ref:`3nodeinstall` guide.
6. Restart the morpheus-ui service.
