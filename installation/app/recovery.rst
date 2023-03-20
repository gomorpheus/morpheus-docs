Recovery
^^^^^^^^

If a node happens to crash most of the time |morpheus| will start upon boot of the server and the services will self-recover. However, there can be cases where RabbitMQ and Elasticsearch are unable to recover in a clean fashion and require minor manual intervention. Regardless, it is considered best practice when recovering a restart to perform some manual health checks.

.. code-block:: bash

   [root@node-1 ~]# morpheus-ctl status
   run: check-server: (pid 17808) 7714s; run: log: (pid 549) 8401s
   run: elasticsearch: (pid 19207) 5326s; run: log: (pid 565) 8401s
   run: guacd: (pid 601) 8401s; run: log: (pid 573) 8401s
   run: morpheus-ui: (pid 17976) 7633s; run: log: (pid 555) 8401s
   run: nginx: (pid 581) 8401s; run: log: (pid 544) 8401s
   run: rabbitmq: (pid 17850) 7708s; run: log: (pid 542) 8401s


But, a status can report false positives if, say, RabbitMQ is in a boot loop or Elasticsearch is up, but not able to join the cluster. It is always advisable to tail the logs of the services to investigate their health.

.. code-block:: bash

  [root@node-1 ~]# morpheus-ctl tail rabbitmq
  [root@node-1 ~]# morpheus-ctl tail elasticsearch


To minimize disruption to the user interface, it is advisable to remedy Elasticsearch clustering first. Due to write locking in Elasticsearch it can be required to restart other nodes in the cluster to allow the recovering node to join. Begin by determining which Elasticsearch node became the master during the outage. On one of the two other nodes (not the recovered node):

.. code-block:: bash

   [root@node-2 ~]# curl localhost:9200/_cat/nodes
   node-1 10.100.10.121 7 47 0.21 d * morpheus1
   localhost 127.0.0.1 4 30 0.32 d m morpheus2

The master is determined by identifying the row with the ``‘*’`` in it. SSH to this node (if different) and restart Elasticsearch.

.. code-block:: bash

   [root@node-1 ~]# morpheus-ctl restart elasticsearch

Go to the other of the two ‘up’ nodes and run the curl command again. If the output contains three nodes then Elasticsearch has been recovered and you can move on to re-clustering RabbitMQ. Otherwise you will see output that contains only the node itself:

.. code-block:: bash

   [root@node-2 ~]# curl localhost:9200/_cat/nodes
   localhost 127.0.0.1 4 30 0.32 d * morpheus2

If this is the case then restart Elasticsearch on this node as well:

.. code-block:: bash

   [root@node-2 ~]# morpheus-ctl restart elasticsearch

After this you should be able to run the curl command and see all three nodes have rejoined the cluster:

.. code-block:: bash

   [root@node-2 ~]# curl localhost:9200/_cat/nodes
   node-1 10.100.10.121 9 53 0.31 d * morpheus1
   localhost 127.0.0.1 7 32 0.22 d m morpheus2
   node-3 10.100.10.123 3 28 0.02 d m morpheus3

The most frequent case of restart errors for RabbitMQ is with epmd failing to restart. |morpheus|’s recommendation is to ensure the epmd process is running and daemonized by starting it:

.. code-block:: bash

   [root@node-1 ~]# /opt/morpheus/embedded/lib/erlang/erts-5.10.4/bin/epmd -daemon

And then restarting RabbitMQ:

.. code-block:: bash

   [root@node-1 ~]# morpheus-ctl restart rabbitmq

And then restarting the |morpheus| UI service:

.. code-block:: bash

   [root@node-1 ~]# morpheus-ctl restart morpheus-ui

Again, it is always advisable to monitor the startup to ensure the |morpheus| Application is starting without error:

.. code-block:: bash

   [root@node-1 ~]# morpheus-ctl tail morpheus-ui

Recovery Thoughts/Further Discussion: If |morpheus| UI cannot connect to RabbitMQ, Elasticsearch or the database tier it will fail to start. The |morpheus| UI logs can indicate if this is the case.

Aside from RabbitMQ, there can be issues with false positives concerning Elasticsearch’s running status. The biggest challenge with Elasticsearch, for instance, is that a restarted node has trouble joining the ES cluster. This is fine in the case of ES, though, because the minimum_master_nodes setting will not allow the un-joined singleton to be consumed until it joins. |morpheus| will still start if it can reach the other two ES hosts, which are still clustered.

The challenge with RabbitMQ is that it is load balanced behind |morpheus| for requests, but each |morpheus| application server needs to boostrap the RabbitMQ tied into it. Thus, if it cannot reach its own RabbitMQ startup for it will fail.

Similarly, if a |morpheus| UI service cannot reach the database, startup will fail. However, if the database is externalized and failover is configured for Master/Master, then there should be ample opportunity for |morpheus| to connect to the database tier.

Because |morpheus| can start even though the Elasticsearch node on the same host fails to join the cluster, it is advisable to investigate the health of ES on the restarted node after the services are up. This can be done by accessing the endpoint with curl and inspecting the output. The status should be “green” and number of nodes should be “3”:

.. code-block:: bash

   [root@node-1 ~]# curl localhost:9200/_cluster/health?pretty=true
   {
   "cluster_name" : "morpheus",
   "status" : "green",
   "timed_out" : false,
   "number_of_nodes" : 3,
   "number_of_data_nodes" : 3,
   "active_primary_shards" : 110,
   "active_shards" : 220,
   "relocating_shards" : 0,
   "initializing_shards" : 0,
   "unassigned_shards" : 0,
   "number_of_pending_tasks" : 0,
   "number_of_in_flight_fetch" : 0
   }

If this is not the case it is worth investigating the Elasticsearch logs to understand why the singleton node is having trouble joining the cluster. These can be found at ``/var/log/morpheus/elasticsearch/current``

Outside of these stateful tiers, the “morpheus-ctl status” command will not output a “run” status unless the service is successfully running. If a stateless service reports a failure to run, the logs should be investigated and/or sent to |morpheus| for additional support. Logs for all |morpheus| embedded services are found in ``/var/log/morpheus``.

