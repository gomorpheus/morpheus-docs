3 Node with Externalized DB Configuration
-----------------------------------------

Assumptions
^^^^^^^^^^^^

This guide assumes the following:

- There is an externalized database running for Morpheus to access.
- The database service is a MySQL dialect (MySQL, MariaDB, Galera, etc...)
- A database has been created for Morpheus as well as a user and proper grants have been run for the user. Morpheus will create the schema.
- The baremetal nodes cannot access the public internet
- The base OS is RHEL 7.x
- Shortname versions of hostnames will be resolvable
- All nodes have access to a shared volume for /var/opt/morpheus/morpheus-ui. This can be done as a post startup step.
- This configuration will support the complete loss of a single node, but no more.  Specifically the Elasticsearch tier requires at least two nodes to always be clustered..

Steps
^^^^^

#. First begin by downloading the requisite Morpheus packages either to the nodes or to your workstation for transfer. These packages need to be made available on the nodes you wish to install Morpheus on.

   .. code-block:: text

    [root@app-server-1 ~]# wget https://downloads.gomorpheus.com/yum/el/7/noarch/morpheus-appliance-offline-3.1.5- 1.noarch.rpm
    [root@app-server-1 ~]# wget https://downloads.gomorpheus.com/yum/el/7/x86_64/morpheus-appliance-3.1.5- 1.el7.x86_64.rpm

#. Once the packages are available on the nodes they can be installed. Make sure that no steps beyond the rpm install are run.

   .. code-block:: bash

    [root@app-server-1 ~]# rpm -i morpheus-appliance-3.1.5-1.el7.x86_64.rpm
    [root@app-server-1 ~]# rpm -i morpheus-appliance-offline-3.1.5-1.noarch.rpm

#. Next you will need to edit the Morpheus configuration file on each node.

   **Node 1**

   .. code-block:: bash

     appliance_url 'https://esmort01.qcorpaa.aa.com'
     elasticsearch['es_hosts'] = {'10.130.2.1' => 9300, '10.130.2.2' => 9300, '10.130.2.3' => 9300} elasticsearch['node_name'] = 'morpheus1'
     elasticsearch['host'] = '0.0.0.0'
     rabbitmq['host'] = '0.0.0.0'
     rabbitmq['nodename'] = 'rabbit@esmort01'
     mysql['enable'] = false
     mysql['host'] = '10.130.12.228'
     mysql['morpheus_db'] = 'morpheusdb'
     mysql['morpheus_db_user'] = 'morpheus'
     mysql['morpheus_password'] = 'password'

   **Node 2**

   .. code-block:: bash

    appliance_url 'https://esmort02.qcorpaa.aa.com'
    elasticsearch['es_hosts'] = {'10.130.2.2' => 9300, '10.130.2.1' => 9300, '10.130.2.3' => 9300} elasticsearch['node_name'] = 'morpheus2'
    elasticsearch['host'] = '0.0.0.0'
    rabbitmq['host'] = '0.0.0.0'
    rabbitmq['nodename'] = 'rabbit@esmort02'
    mysql['enable'] = false
    mysql['host'] = '10.130.12.228'
    mysql['morpheus_db'] = 'morpheusdb'
    mysql['morpheus_db_user'] = 'morpheus'
    mysql['morpheus_password'] = 'password'

   **Node 3**

   .. code-block:: bash

       appliance_url 'https://esmort03.qcorpaa.aa.com'
       elasticsearch['es_hosts'] = {'10.130.2.3' => 9300, '10.130.2.2' => 9300, '10.130.2.1' => 9300} elasticsearch['node_name'] = 'morpheus3'
       elasticsearch['host'] = '0.0.0.0'
       rabbitmq['host'] = '0.0.0.0'
       rabbitmq['nodename'] = 'rabbit@esmort03'
       mysql['enable'] = false
       mysql['host'] = '10.130.12.228'
       mysql['morpheus_db'] = 'morpheusdb'
       mysql['morpheus_db_user'] = 'morpheus'
       mysql['morpheus_password'] = 'password'

.. note::

  If you are running MySQL in a Master/Master configuration we will need to slightly alter the mysql['host'] line in the morpheus.rb to account for both masters in a failover configuration. As an example:

.. code-block:: bash

    mysql['host'] = '10.130.12.228:3306,10.130.12.109'


Morpheus will append the ‘3306’ port to the end of the final IP in the string, which is why we leave it off but explicitly type it for the first IP in the string. The order of IPs matters in that it should be the same across all three Morpheus Application Servers. As mentioned, this will be a failover configuration for MySQL in that the application will only read/write from the second master if the first master becomes unavailable. This way we can avoid commit lock issues that might arise from a load balanced Master/Master.



Run the reconfigure on all nodes

.. code-block:: bash

  [root@app-server-1 ~] morpheus-ctl reconfigure

Morpheus will come up on all nodes and Elasticsearch will auto-cluster. The only item left is the manual clustering of RabbitMQ.

Select one of the nodes to be your Source Of Truth (SOT) for RabbitMQ clustering. We need to share secrets for RabbitMQ, the erlang cookie and join the other nodes to the SOT node.
Begin by copying secrets from the SOT node to the other nodes.

.. code-block:: bash

  [root@app-server-1 ~] cat /etc/morpheus/morpheus-secrets.json
  {
    "mysql": {
      "root_password": "wam457682b67858ae2cf4bc",
      "morpheus_password": "password",
      "ops_password": "98d9677686698d319r6356ae3a77"
    },
    "rabbitmq": {
      "morpheus_password": "adff00cf8714b25mc",
      "queue_user_password": "r075f26158c1fes2",
      "cookie": "6458933CD86782AD39E25"
    },
    "vm-images": {
      "s3": {
        "aws_access_id": "AKIAI6OFPBN4NWSFBXRQ",
        "aws_secret_key": "a9vxxjH5xkgh6dHgRjLl37i33rs8pwRe3"
     }
    }
   }

Then copy the erlang.cookie from the SOT node to the other nodes

.. code-block:: bash

 [root@app-server-1 ~] cat /opt/morpheus/embedded/rabbitmq/.erlang.cookie
 # 754363AD864649RD63D28

Once this is done run a reconfigure on the two nodes that are NOT the SOT nodes.

.. code-block:: bash

[root@app-server-2 ~] morpheus-ctl reconfigure

.. NOTE:: This step will fail. This is ok, and expected. If the reconfigure hangs then use Ctrl+C to quit the reconfigure run and force a failure.

Subsequently we need to stop and start Rabbit on the NOT SOT nodes.

.. code-block:: bash

 [root@app-server-2 ~] morpheus-ctl stop rabbitmq
 [root@app-server-2 ~] morpheus-ctl start rabbitmq
 [root@app-server-2 ~]#PATH=/opt/morpheus/sbin:/opt/morpheus/sbin:/opt/morpheus/embedded/sbin:/opt/morpheus/embedded/bin:$PATH
 [root@app-server-2 ~]# rabbitmqctl stop_app

 Stopping node 'rabbit@app-server-2' ...

 [root@app-server-2 ~]# rabbitmqctl join_cluster rabbit@app-server-1 Clustering node 'rabbit@app-server-2' with 'rabbit@app-server-1' ... [root@app-server-2 ~]# rabbitmqctl start_app

 Starting node 'rabbit@app-server-2' ...

Once the Rabbit services are up and clustered on all nodes they need to be set to HA/Mirrored Queues:

.. code-block:: bash

   rabbitmqctl set_policy -p morpheus --priority 1 --apply-to all ha ".*" '{"ha-mode":"all"}'

.. code-block:: bash

  [root@app-server-2 ~]# rabbitmqctl set_policy -p morpheus --priority 1 --apply-to all ha ".*" '{"ha-mode": "all"}'

The last thing to do is restart the Morpheus UI on the two nodes that are NOT the SOT node.

.. code-block:: bash

  [root@app-server-2 ~]# morpheus-ctl restart morpheus-ui

If this command times out then run:

.. code-block:: bash

   [root@app-server-2 ~]# morpheus-ctl kill morpheus-ui
   [root@app-server-2 ~]# morpheus-ctl start morpheus-ui

You will be able to verify that the UI services have restarted properly by inspecting the logfiles. A standard practice after running a restart is to tail the UI log file.

.. code-block:: bash

  [root@app-server-2 ~]# morpheus-ctl tail morpheus-ui

Lastly, we need to ensure that Elasticsearch is configured in such a way as to support a quorum of 2. We need to do this step on EVERY NODE.

.. code-block:: bash

  [root@app-server-2 ~]# echo "discovery.zen.minimum_master_nodes: 2" >> /opt/morpheus/embedded/elasticsearch/config/elasticsearch.yml
  [root@app-server-2 ~]# morpheus-ctl restart elasticsearch

For moving /var/opt/morpheus/morpheus-ui files into a shared volume make sure ALL Morpheus services on ALL three nodes are down before you begin.

.. code-block:: bash

  [root@app-server-1 ~]# morpheus-ctl stop

Permissions are as important as is content, so make sure to preserve directory contents to the shared volume. Subsequently you can start all Morpheus services on all three nodes and tail the Morpheus UI log file to inspect errors.

Database Migration
^^^^^^^^^^^^^^^^^^^^

If your new installation is part of a migration then you need to move the data from your original Morpheus database to your new one. This is easily accomplished by using a stateful dump.

To begin this, stop the Morpheus UI on your original Morpheus server:

.. code-block:: bash

  [root@app-server-old ~]# morpheus-ctl stop morpheus-ui

Once this is done you can safely export. To access the MySQL shell we will need the password for the Morpheus DB user. We can find this in the morpheus-secrets file:

.. code-block:: bash

    [root@app-server-old ~]# cat /etc/morpheus/morpheus-secrets.json

.. code-block:: javascript
  {
    "mysql": {
        "root_password": "2dee0d72a0e20729ef35ad86",
        "morpheus_password": "149c15471484228385f9ccd4",
        "ops_password": "7e6040b3b3a14d8a083fb57e"
          },
    "rabbitmq": {
              "morpheus_password": "35e259a167b2a296",
              "queue_user_password": "c90717995720ab7f",
              "cookie": "3F1B7B5C8B24A6FF1C9A"
    },
    "vm-images": {
      "s3": {
          "aws_access_id": "AKIAI6SF4BN7NWSFAWVQ",
          "aws_secret_key": "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"
        }
      }
  }

Take note of this password as it will be used to invoke a dump. Morpheus provides embedded binaries for this task. Invoke it via the embedded path and specify the host. In this example we are using the morpheus database on the MySQL listening on localhost. Enter the password copied from the previous step when prompted:

.. code-block:: bash

    [root@app-server-old ~]# /opt/morpheus/embedded/mysql/bin/mysqldump -u morpheus -h 127.0.0.1 morpheus -p > /tmp/morpheus_backup.sql
    Enter password:

This file needs to be pushed to the new Morpheus Installation’s backend. Depending on the GRANTS in the new MySQL backend, this will likely require moving this file to one of the new Morpheus frontend servers.
Once the file is in place it can be imported into the backend. Begin by ensuring the Morpheus UI service is stopped on all of the application servers:

.. code-block:: bash

  [root@app-server-1 ~]# morpheus-ctl stop morpheus-ui
  [root@app-server-2 ~]# morpheus-ctl stop morpheus-ui
  [root@app-server-3 ~]# morpheus-ctl stop morpheus-ui

Then you can import the MySQL dump into the target database using the embedded MySQL binaries, specifying the database host, and entering the password for the morpheus user when prompted:

.. code-block:: bash

  [root@app-server-1 ~]# /opt/morpheus/embedded/mysql/bin/mysql -u morpheus -h 10.130.2.38 morpheus -p < /tmp/morpheus_backup.sql
  Enter password:


Recovery
^^^^^^^^^
If a node happens to crash most of the time Morpheus will start upon boot of the server and the services will self-recover. However, there can be cases where RabbitMQ and Elasticsearch are unable to recover in a clean fashion and it require minor manual intervention. Regardless, it is considered best practice when recovering a restart to perform some manual health

.. code-block:: bash

  [root@app-server-1 ~]# morpheus-ctl status
  run: check-server: (pid 17808) 7714s;
  run: log: (pid 549) 8401s
  run: elasticsearch: (pid 19207) 5326s;
  run: log: (pid 565) 8401s
  run: guacd: (pid 601) 8401s;
  run: log: (pid 573) 8401s
  run: morpheus-ui: (pid 17976) 7633s;
  run: log: (pid 555) 8401s
  run: nginx: (pid 581) 8401s;
  run: log: (pid 544) 8401s
  run: rabbitmq: (pid 17850) 7708s;
  run: log: (pid 542) 8401s
  run: redis: (pid 572) 8401s;
  run: log: (pid 548) 8401s


But, a status can report false positives if, say, RabbitMQ is in a boot loop or Elasticsearch is up, but not able to join the cluster. It is always advisable to tail the logs of the services to investigate their health.

.. code-block:: bash

  [root@app-server-1 ~]# morpheus-ctl tail rabbitmq
  [root@app-server-1 ~]# morpheus-ctl tail elasticsearch

Output that would indicate a problem with RabbitMQ would be visible in a StackTrace and resembles this example:

.. image:: /images/ha3node/HA3nodeRabbitMQ.png

And for Elasticsearch:

.. image:: /images/ha3node/HA3nodeElasticSearch.png

To minimize disruption to the user interface, it is advisable to remedy Elasticsearch clustering first. Due to write locking in Elasticsearch it can be required to restart other nodes in the cluster to allow the recovering node to join. Begin by determining which Elasticsearch node became the master during the outage. On one of the two other nodes (not the recovered node):

.. code-block:: bash

  [root@app-server-2 ~]# curl localhost:9200/_cat/nodes
  app-server-1 10.130.2.13 7 47 0.21 d * morpheus1
  localhost 127.0.0.1 4 30 0.32 d m morpheus2

The master is determined by identifying the row with the ‘*’ in it.
SSH to this node (if different) and restart Elasticsearch.

.. code-block:: bash

  [root@app-server-1 ~]# morpheus-ctl restart elasticsearch

Go to the other of the two ‘up’ nodes and run the curl command again. If the output contains three nodes then Elasticsearch has been recovered and you can move on to re-clustering RabbitMQ. Otherwise you will see output that contains only the node itself:

.. code-block:: bash

  [root@app-server-2 ~]# curl localhost:9200/_cat/nodes
  localhost 127.0.0.1 4 30 0.32 d * morpheus2

If this is the case then restart Elasticsearch on this node as well:

.. code-block:: bash

  [root@app-server-2 ~]# morpheus-ctl restart elasticsearch

After this you should be able to run the curl command and see all three nodes have rejoined the cluster:

.. code-block:: bash

  [root@app-server-2 ~]# curl localhost:9200/_cat/nodes
  app-server-1 10.130.2.13 9 53 0.31 d * morpheus1
  localhost 127.0.0.1 7 32 0.22 d m morpheus2
  app-server-3 10.130.2.11 3 28 0.02 d m morpheus3

The most frequent case of restart errors for RabbitMQ is with epmd failing to restart. Morpheus’s recommendation is to ensure the epmd process is running and daemonized by starting it:

.. code-block:: bash

  [root@app-server-1 ~]# /opt/morpheus/embedded/lib/erlang/erts-5.10.4/bin/epmd - daemon

And then restarting RabbitMQ:

.. code-block:: bash

  [root@app-server-1 ~]# morpheus-ctl restart rabbitmq

And then restarting the Morpheus UI service:

.. code-block:: bash

  [root@app-server-1 ~]# morpheus-ctl restart morpheus-ui

Again, it is always advisable to monitor the startup to ensure the Morpheus Application is starting without error:

.. code-block:: bash

  [root@app-server-1 ~]# morpheus-ctl tail morpheus-ui

**Recovery Thoughts/Further Discussion:** If Morpheus UI cannot connect to RabbitMQ, Elasticsearch or the database tier it will fail to start. The Morpheus UI logs can indicate if this is the case.

Aside from RabbitMQ, there can be issues with false positives concerning Elasticsearch’s running status. The biggest challenge with Elasticsearch, for instance, is that a restarted node has trouble joining the ES cluster. This is fine in the case of ES, though, because the minimum_master_nodes setting will not allow the un-joined singleton to be consumed until it joins. Morpheus will still start if it can reach the other two ES hosts, which are still clustered.

The challenge with RabbitMQ is that it is load balanced behind Morpheus for requests, but each Morpheus application server needs to boostrap the RabbitMQ tied into it. Thus, if it cannot reach its own RabbitMQ startup for it will fail.

Similarly, if a Morpheus UI service cannot reach the database, startup will fail. However, if the database is externalized and failover is configured for Master/Master, then there should be ample opportunity for Morpheus to connect to the database tier.

Because Morpheus can start even though the Elasticsearch node on the same host fails to join the cluster, it is advisable to investigate the health of ES on the restarted node after the services are up. This can be done by accessing the endpoint with curl and inspecting the output. The status should be “green” and number of nodes should be “3”:

.. code-block:: bash

  [root@app-server-1 ~]# curl localhost:9200/_cluster/health?pretty=true
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

If this is not the case it is worth investigating the Elasticsearch logs to understand why the singleton node is having trouble joining the cluster. These can be found at:

``/var/log/morpheus/elasticsearch/current``

Outside of these stateful tiers, the “morpheus-ctl status” command will not output a “run” status unless the service is successfully running. If a stateless service reports a failure to run, the logs should be investigated and/or sent to Morpheus for
additional support. Logs for all Morpheus embedded services are found below:

``/var/log/morpheus``
