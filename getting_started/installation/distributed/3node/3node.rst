.. _3nodeinstall:

3-Node HA Install
-----------------

Distributed App Nodes with Externalized DB

Assumptions
^^^^^^^^^^^

This guide assumes the following:

- The Baremetal nodes cannot access the public internet
- The base OS is RHEL 8.x
- Shortname versions of hostnames will be resolvable
- All nodes have access to a shared volume for ``/var/opt/morpheus/morpheus-ui``. This can be done as a post startup step.
- This configuration will support the complete loss of a single node, but no more.  Specifically the Elasticsearch tier requires at least two nodes to always be clustered..

.. thumbnail:: /images/arch/morpheus-3node-arch-2.png
   :alt: Morpheus 3-Node HA Architecture

   Morpheus 3-Node HA Architecture

Default Locations
^^^^^^^^^^^^^^^^^

|morpheus| follows several install location conventions. Below is a list of system defaults for convenient management:

* Installation Location: ``/opt/morpheus``
* Log Location: ``/var/log/morpheus``

  * Morpheus-UI: ``/var/log/morpheus/morpheus-ui``
  * NginX: ``/var/log/morpheus/nginx``
  * Check Server: ``/var/log/morpheus/check-server``
  * Elastic Search: ``/var/log/morpheus/elasticsearch``
  * RabbitMQ: ``/var/log/morpheus/rabbitmq``

*  User-defined install/config: ``/etc/morpheus/morpheus.rb``

.. include::   /getting_started/installation/distributed/full/perconaTls.rst

App Node Installation
^^^^^^^^^^^^^^^^^^^^^

#. First begin by downloading and installing the requisite |morpheus| packages to the |morpheus| nodes.

   .. note:: For offline or nodes that cannot reach |repo_host_url|, both the standard and supplemental packages will need to be transferred and then installed on the |morpheus| nodes.

   .. content-tabs::

      .. tab-container:: tab1
         :title: All Nodes

         .. code-block:: bash

            [root@node-(1/2/3) ~]# wget https://example/path/morpheus-appliance-ver-1.el7.x86_64.rpm
            [root@node-(1/2/3) ~]# rpm -i morpheus-appliance-offline-ver-1.noarch.rpm

#. Do NOT run reconfigure yet. The |morpheus| configuration file must be edited prior to the initial reconfigure.

#. Next you will need to edit the |morpheus| configuration file ``/etc/morpheus/morpheus.rb`` on each node.

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 1

         .. code-block:: bash

            appliance_url 'https://morpheus1.localdomain'
            elasticsearch['es_hosts'] = {'10.100.10.121' => 9200, '10.100.10.122' => 9200, '10.100.10.123' => 9200}
            elasticsearch['node_name'] = '10.100.10.121'
            elasticsearch['host'] = '0.0.0.0'
            rabbitmq['host'] = '0.0.0.0'
            rabbitmq['nodename'] = 'rabbit@node01'
            mysql['enable'] = false
            mysql['host'] = {'10.100.10.111' => 3306, '10.100.10.112' => 3306, '10.100.10.113' => 3306}
            mysql['morpheus_db'] = 'morpheus'
            mysql['morpheus_db_user'] = 'morpheusDbUser'
            mysql['morpheus_password'] = 'morpheusDbUserPassword'

      .. tab-container:: tab2
         :title: Node 2

         .. code-block:: bash

            appliance_url 'https://morpheus2.localdomain'
            elasticsearch['es_hosts'] = {'10.100.10.121' => 9200, '10.100.10.122' => 9200, '10.100.10.123' => 9200}
            elasticsearch['node_name'] = '10.100.10.122'
            elasticsearch['host'] = '0.0.0.0'
            rabbitmq['host'] = '0.0.0.0'
            rabbitmq['nodename'] = 'rabbit@node02'
            mysql['enable'] = false
            mysql['host'] = {'10.100.10.111' => 3306, '10.100.10.112' => 3306, '10.100.10.113' => 3306}
            mysql['morpheus_db'] = 'morpheus'
            mysql['morpheus_db_user'] = 'morpheusDbUser'
            mysql['morpheus_password'] = 'morpheusDbUserPassword'

     .. tab-container:: tab3
        :title: Node 3

         .. code-block:: bash

            appliance_url 'https://morpheus3.localdomain'
            elasticsearch['es_hosts'] = {'10.100.10.121' => 9200, '10.100.10.122' => 9200, '10.100.10.123' => 9200}
            elasticsearch['node_name'] = '10.100.10.123'
            elasticsearch['host'] = '0.0.0.0'
            rabbitmq['host'] = '0.0.0.0'
            rabbitmq['nodename'] = 'rabbit@node03'
            mysql['enable'] = false
            mysql['host'] = {'10.100.10.111' => 3306, '10.100.10.112' => 3306, '10.100.10.113' => 3306}
            mysql['morpheus_db'] = 'morpheus'
            mysql['morpheus_db_user'] = 'morpheusDbUser'
            mysql['morpheus_password'] = 'morpheusDbUserPassword'

   .. note:: If using a load balancer, the ``appliance_url`` field should match the FQDN of the load balancer, meaning all three configurations would have the same URL.

   .. important:: The elasticsearch node names set in ``elasticsearch['node_name']`` must match the host entries in elasticsearch['es_hosts']. ``node_name`` is used for ``node.name`` and ``es_hosts`` is used for ``cluster.initial_master_nodes`` in the generated elasticsearch.yml config. Node names that do not match entries in cluster.initial_master_nodes will cause clustering issues.

   .. important:: The nodename after the **@** in the ``rabbitmq['nodename']`` field should be DNS resolvable, do not use a FQDN.

#. Reconfigure on all nodes

   .. content-tabs::

      .. tab-container:: tab1
         :title: All Nodes

         .. code-block:: bash

            [root@node-[1/2/3] ~] morpheus-ctl reconfigure

   |morpheus| will come up on all nodes and Elasticsearch will auto-cluster. The only item left is the manual clustering of RabbitMQ.

Clustering RabbitMQ
^^^^^^^^^^^^^^^^^^^

#. Select one of the nodes to be your Source Of Truth (SOT) for RabbitMQ clustering (Node 1 for this example). On the nodes that are **NOT** the SOT (Nodes 2 & 3 in this example), begin by stopping the UI and RabbitMQ.

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 2

         .. code-block:: bash

          [root@node-2 ~] morpheus-ctl stop morpheus-ui
          [root@node-2 ~] source /opt/morpheus/embedded/rabbitmq/.profile
          [root@node-2 ~] rabbitmqctl stop_app
          [root@node-2 ~] morpheus-ctl stop rabbitmq

      .. tab-container:: tab2
         :title: Node 3

         .. code-block:: bash

          [root@node-3 ~] morpheus-ctl stop morpheus-ui
          [root@node-3 ~] source /opt/morpheus/embedded/rabbitmq/.profile
          [root@node-3 ~] rabbitmqctl stop_app
          [root@node-3 ~] morpheus-ctl stop rabbitmq


#. Then on the SOT node, we need to copy the secrets for RabbitMQ.

   Begin by copying secrets from the SOT node to the other nodes.

   .. content-tabs::

     .. tab-container:: tab1
        :title: Node 1

        .. code-block:: bash

           [root@node-1 ~] cat /etc/morpheus/morpheus-secrets.json

            "rabbitmq": {
              "morpheus_password": "***REDACTED***",
              "queue_user_password": "***REDACTED***",
              "cookie": "***REDACTED***"
            },

     .. tab-container:: tab2
        :title: Node 2

        .. code-block:: bash

           [root@node-2 ~] vi /etc/morpheus/morpheus-secrets.json

             "rabbitmq": {
               "morpheus_password": "***node-1_morpheus_password***",
               "queue_user_password": "***node-1_queue_user_password***",
               "cookie": "***node-1_cookie***"
             },

     .. tab-container:: tab3
        :title: Node 3

        .. code-block:: bash

           [root@node-3 ~] vi /etc/morpheus/morpheus-secrets.json

           "rabbitmq": {
             "morpheus_password": "***node-1_morpheus_password***",
             "queue_user_password": "***node-1_queue_user_password***",
             "cookie": "***node-1_cookie***"
           },

#. Then copy the erlang.cookie from the SOT node to the other nodes

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 1

         .. code-block:: bash

            [root@node-1 ~] cat /opt/morpheus/embedded/rabbitmq/.erlang.cookie

            # 754363AD864649RD63D28

      .. tab-container:: tab2
         :title: Node 2

         .. code-block:: bash

            [root@node-2 ~] vi /opt/morpheus/embedded/rabbitmq/.erlang.cookie

            # node-1_erlang_cookie

      .. tab-container:: tab3
         :title: Nodes 3

         .. code-block:: bash

           [root@node-3 ~] vi /opt/morpheus/embedded/rabbitmq/.erlang.cookie

           # node-1_erlang_cookie

#. Once the secrets and cookie are copied from node-1 to nodes 2 & 3, run a reconfigure on nodes 2 & 3.

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 2

         .. code-block:: bash

            [root@node-2 ~] morpheus-ctl reconfigure

      .. tab-container:: tab2
         :title: Node 3

         .. code-block:: bash

            [root@node-3 ~] morpheus-ctl reconfigure

#. Next we will join nodes 2 & 3 to the cluster.

   .. IMPORTANT:: The commands below must be run at root

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 2

         .. code-block:: bash

           [root@node-2 ~]# morpheus-ctl stop rabbitmq
           [root@node-2 ~]# morpheus-ctl start rabbitmq
           [root@node-2 ~]# source /opt/morpheus/embedded/rabbitmq/.profile
           [root@node-2 ~]# rabbitmqctl stop_app

           Stopping node 'rabbit@node-2' ...

           [root@node-2 ~]# rabbitmqctl join_cluster rabbit@node-1

           Clustering node 'rabbit@node-2' with 'rabbit@node-1' ...

           [root@node-2 ~]# rabbitmqctl start_app

           Starting node 'rabbit@node-2' ...

           [root@node-2 ~]#

      .. tab-container:: tab2
         :title: Node 3

         .. code-block:: bash

           [root@node-3 ~]# morpheus-ctl stop rabbitmq
           [root@node-3 ~]# morpheus-ctl start rabbitmq
           [root@node-3 ~]# source /opt/morpheus/embedded/rabbitmq/.profile
           [root@node-3 ~]# rabbitmqctl stop_app

           Stopping node 'rabbit@node-3' ...

           [root@node-3 ~]# rabbitmqctl join_cluster rabbit@node-1

           Clustering node 'rabbit@node-3' with 'rabbit@node-1' ...

           [root@node-3 ~]# rabbitmqctl start_app

           Starting node 'rabbit@node-3' ...

           [root@node-3 ~]#

   .. NOTE:: If you receive an error ``unable to connect to epmd (port 4369) on node-1: nxdomain (non-existing domain)`` make sure to add all IPs and short (non-fqdn) hostnames to the ``etc/hosts`` file to ensure each node can resolve the other hostnames.

#. Next reconfigure Nodes 2 & 3

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 2

         .. code-block:: bash

            [root@node-2 ~] morpheus-ctl reconfigure

      .. tab-container:: tab2
         :title: Node 3

         .. code-block:: bash

            [root@node-3 ~] morpheus-ctl reconfigure

#. The last thing to do is start the |morpheus| UI on the two nodes that are NOT the SOT node.

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 2

         .. code-block:: bash

            [root@node-2 ~] morpheus-ctl start morpheus-ui

      .. tab-container:: tab2
         :title: Node 3

         .. code-block:: bash

            [root@node-3 ~] morpheus-ctl start morpheus-ui


#. You will be able to verify that the UI services have restarted properly by inspecting the logfiles. A standard practice after running a restart is to tail the UI log file.

   .. code-block:: bash

      root@node-1/2/3 ~]# morpheus-ctl tail morpheus-ui


..
  #. Lastly, we need to ensure that Elasticsearch is configured in such a way as to support a quorum of 2. We need to do this step on EVERY NODE.

     .. code-block:: bash

        [root@node-2 ~]# echo "discovery.zen.minimum_master_nodes: 2" >> /opt/morpheus/embedded/elasticsearch/config/elasticsearch.yml
        [root@node-2 ~]# morpheus-ctl restart elasticsearch


     .. NOTE::
         For moving ``/var/opt/morpheus/morpheus-ui`` files into a shared volume make sure ALL |morpheus| services on ALL three nodes are down before you begin.

     .. code-block:: bash

      [root@node-1 ~]# morpheus-ctl stop

  #. Permissions are as important as is content, so make sure to preserve directory contents to the shared volume.

  #. Subsequently you can start all |morpheus| services on all three nodes and tail the |morpheus| UI log file to inspect errors.

|

-----

Database Migration
^^^^^^^^^^^^^^^^^^

If your new installation is part of a migration then you need to move the data from your original |morpheus| database to your new one. This is easily accomplished by using a stateful dump.

#. To begin this, stop the |morpheus| UI on your original |morpheus| server:

   .. code-block:: bash

    [root@node-old ~]# morpheus-ctl stop morpheus-ui

#. Once this is done you can safely export. To access the MySQL shell we will need the password for the |morpheus| DB user. We can find this in the morpheus-secrets file:

   .. code-block:: bash

      [root@node-old ~]# cat /etc/morpheus/morpheus-secrets.json

        {
          "mysql": {
              "root_password": "***REDACTED***",
              "morpheus_password": "***REDACTED***",
              "ops_password": "***REDACTED***"
                },
          "rabbitmq": {
                    "morpheus_password": "***REDACTED***",
                    "queue_user_password": "***REDACTED***",
                    "cookie": "***REDACTED***"
          },
          "vm-images": {
            "s3": {
                "aws_access_id": "***REDACTED***",
                "aws_secret_key": "***REDACTED***"
              }
            }
        }

#. Take note of this password as it will be used to invoke a dump. |morpheus| provides embedded binaries for this task. Invoke it via the embedded path and specify the host. In this example we are using the |morpheus| database on MySQL listening on localhost. Enter the password copied from the previous step when prompted:

   .. code-block:: bash

      [root@node-old ~]# /opt/morpheus/embedded/mysql/bin/mysqldump -u morpheus -h 127.0.0.1 morpheus -p > /tmp/morpheus_backup.sql

      Enter password:

   This file needs to be pushed to the new |morpheus| Installation’s backend. Depending on the GRANTS in the new MySQL backend, this will likely require moving this file to one of the new |morpheus| frontend servers.

#. Once the file is in place it can be imported into the backend. Begin by ensuring the |morpheus| UI service is stopped on all of the application servers:

   .. code-block:: bash

      [root@node-1 ~]# morpheus-ctl stop morpheus-ui
      [root@node-2 ~]# morpheus-ctl stop morpheus-ui
      [root@node-3 ~]# morpheus-ctl stop morpheus-ui

#. Then you can import the MySQL dump into the target database using the embedded MySQL binaries, specifying the database host, and entering the password for the |morpheus| user when prompted:

   .. code-block:: bash

      [root@node-1 ~]# /opt/morpheus/embedded/mysql/bin/mysql -u morpheus -h 10.130.2.38 morpheus -p < /tmp/morpheus_backup.sql
      Enter password:

|

-------

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
