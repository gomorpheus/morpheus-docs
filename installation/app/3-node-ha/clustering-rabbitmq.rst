Clustering RabbitMQ
^^^^^^^^^^^^^^^^^^^

Morpheus will now auto cluster the embedded RabbitMQ for you, provided you add the correct options in the Morpheus.rb file before the first reconfigure. 

.. content-tabs::

   .. tab-container:: tab1
      :title: Node 1

      .. code-block:: bash

         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node01'
         #The following is needed to have internal rabbit cluster itself
         rabbitmq['queue_user'] = 'morpheus'
         rabbitmq['queue_user_password'] = 'morpheusQueueUserPassword'
         rabbitmq['admin_user'] = 'admin'
         rabbitmq['morpheus_password'] = 'AdminUserPassword'
         rabbitmq['cookie'] = 'rabbitCookie' #Example: 7E213AEF5C79DF704DAB
         rabbitmq['rabbit_cluster_nodes'] = {'rabbit@node01' => 5672,'rabbit@node02' => 5672,'rabbit@node03' => 5672}

   .. tab-container:: tab2
      :title: Node 2

      .. code-block:: bash

         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node02'
         #The following is needed to have internal rabbit cluster itself
         rabbitmq['queue_user'] = 'morpheus'
         rabbitmq['queue_user_password'] = 'morpheusQueueUserPassword'
         rabbitmq['admin_user'] = 'admin'
         rabbitmq['morpheus_password'] = 'AdminUserPassword'
         rabbitmq['cookie'] = 'rabbitCookie' #Example: 7E213AEF5C79DF704DAB
         rabbitmq['rabbit_cluster_nodes'] = {'rabbit@node01' => 5672,'rabbit@node02' => 5672,'rabbit@node03' => 5672}

   .. tab-container:: tab3
      :title: Node 3

      .. code-block:: bash

         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node03'
         #The following is needed to have internal rabbit cluster itself
         rabbitmq['queue_user'] = 'morpheus'
         rabbitmq['queue_user_password'] = 'morpheusQueueUserPassword'
         rabbitmq['admin_user'] = 'admin'
         rabbitmq['morpheus_password'] = 'AdminUserPassword'
         rabbitmq['cookie'] = 'rabbitCookie' #Example: 7E213AEF5C79DF704DAB
         rabbitmq['rabbit_cluster_nodes'] = {'rabbit@node01' => 5672,'rabbit@node02' => 5672,'rabbit@node03' => 5672}

To check the cluster health after reconfigure you can run the following. 

.. code-block:: bash 

   source /opt/morpheus/embedded/rabbitmq/.profile
   rabbitmqctl cluster_status

.. toggle-header:: 
   :header: **Mnaual Cluster - Click to Expand**

   #. Select one of the nodes to be your Source Of Truth (SOT) for RabbitMQ clustering (Node 1 for this example). On the nodes that are **NOT** the SOT (Nodes 2 & 3 in this example), begin by stopping the UI and RabbitMQ.

      .. content-tabs::

         .. tab-container:: tab1
            :title: Node 2

            .. code-block:: bash

               [root@node02 ~] morpheus-ctl stop morpheus-ui
               [root@node02 ~] source /opt/morpheus/embedded/rabbitmq/.profile
               [root@node02 ~] rabbitmqctl stop_app
               [root@node02 ~] morpheus-ctl stop rabbitmq

         .. tab-container:: tab2
            :title: Node 3

            .. code-block:: bash

               [root@node03 ~] morpheus-ctl stop morpheus-ui
               [root@node03 ~] source /opt/morpheus/embedded/rabbitmq/.profile
               [root@node03 ~] rabbitmqctl stop_app
               [root@node03 ~] morpheus-ctl stop rabbitmq


   #. Then on the SOT node, we need to copy the secrets for RabbitMQ.

      Begin by copying secrets from the SOT node to the other nodes.

      .. content-tabs::

         .. tab-container:: tab1
            :title: Node 1

            .. code-block:: bash

               [root@node01 ~] cat /etc/morpheus/morpheus-secrets.json

                  "rabbitmq": {
                  "morpheus_password": "***REDACTED***",
                  "queue_user_password": "***REDACTED***",
                  "cookie": "***REDACTED***"
                  },

         .. tab-container:: tab2
            :title: Node 2

            .. code-block:: bash

               [root@node02 ~] vi /etc/morpheus/morpheus-secrets.json

                  "rabbitmq": {
                     "morpheus_password": "***node01_morpheus_password***",
                     "queue_user_password": "***node01_queue_user_password***",
                     "cookie": "***node01_cookie***"
                  },

         .. tab-container:: tab3
            :title: Node 3

            .. code-block:: bash

               [root@node03 ~] vi /etc/morpheus/morpheus-secrets.json

                  "rabbitmq": {
                     "morpheus_password": "***node01_morpheus_password***",
                     "queue_user_password": "***node01_queue_user_password***",
                     "cookie": "***node01_cookie***"
                  },

   #. Then copy the erlang.cookie from the SOT node to the other nodes

      .. content-tabs::

         .. tab-container:: tab1
            :title: Node 1

            .. code-block:: bash

               [root@node01 ~] cat /opt/morpheus/embedded/rabbitmq/.erlang.cookie

               # 754363AD864649RD63D28

         .. tab-container:: tab2
            :title: Node 2

            .. code-block:: bash

               [root@node02 ~] vi /opt/morpheus/embedded/rabbitmq/.erlang.cookie

               # node01_erlang_cookie

         .. tab-container:: tab3
            :title: Nodes 3

            .. code-block:: bash

               [root@node03 ~] vi /opt/morpheus/embedded/rabbitmq/.erlang.cookie

               # node01_erlang_cookie

   #. Once the secrets and cookie are copied from node01 to nodes 2 & 3, run a reconfigure on nodes 2 & 3.

      .. content-tabs::

         .. tab-container:: tab1
            :title: Node 2

            .. code-block:: bash

               [root@node02 ~] morpheus-ctl reconfigure

         .. tab-container:: tab2
            :title: Node 3

            .. code-block:: bash

               [root@node03 ~] morpheus-ctl reconfigure

   #. Next we will join nodes 2 & 3 to the cluster.

      .. IMPORTANT:: The commands below must be run at root

      .. content-tabs::

         .. tab-container:: tab1
            :title: Node 2

            .. code-block:: bash

               [root@node02 ~] morpheus-ctl stop rabbitmq
               [root@node02 ~] morpheus-ctl start rabbitmq
               [root@node02 ~] source /opt/morpheus/embedded/rabbitmq/.profile
               [root@node02 ~] rabbitmqctl stop_app

               Stopping node 'rabbit@node02' ...

               [root@node02 ~] rabbitmqctl join_cluster rabbit@node01

               Clustering node 'rabbit@node02' with 'rabbit@node01' ...

               [root@node02 ~] rabbitmqctl start_app

               Starting node 'rabbit@node02' ...

         .. tab-container:: tab2
            :title: Node 3

            .. code-block:: bash

               [root@node03 ~] morpheus-ctl stop rabbitmq
               [root@node03 ~] morpheus-ctl start rabbitmq
               [root@node03 ~] source /opt/morpheus/embedded/rabbitmq/.profile
               [root@node03 ~] rabbitmqctl stop_app

               Stopping node 'rabbit@node03' ...

               [root@node03 ~] rabbitmqctl join_cluster rabbit@node01

               Clustering node 'rabbit@node03' with 'rabbit@node01' ...

               [root@node03 ~] rabbitmqctl start_app

               Starting node 'rabbit@node03' ...

      .. NOTE:: If you receive an error ``unable to connect to epmd (port 4369) on node01: nxdomain (non-existing domain)`` make sure to add all IPs and short (non-fqdn) hostnames to the ``etc/hosts`` file to ensure each node can resolve the other hostnames.

   #. Next reconfigure Nodes 2 & 3

      .. content-tabs::

         .. tab-container:: tab1
            :title: Node 2

            .. code-block:: bash

               [root@node02 ~] morpheus-ctl reconfigure

         .. tab-container:: tab2
            :title: Node 3

            .. code-block:: bash

               [root@node03 ~] morpheus-ctl reconfigure

   #. The last thing to do is start the |morpheus| UI on the two nodes that are NOT the SOT node.

      .. content-tabs::

         .. tab-container:: tab1
            :title: Node 2

            .. code-block:: bash

               [root@node02 ~] morpheus-ctl start morpheus-ui

         .. tab-container:: tab2
            :title: Node 3

            .. code-block:: bash

               [root@node03 ~] morpheus-ctl start morpheus-ui


   #. You will be able to verify that the UI services have restarted properly by inspecting the logfiles. A standard practice after running a restart is to tail the UI log file.

      .. code-block:: bash

         [root@node (1/2/3) ~] morpheus-ctl tail morpheus-ui


      The UI should be available once the Morpheus logo is displayed in the logs. 
      Look for the ascii logo accompanied by the install version and start time:
      
      .. code-block:: console

         timestamp:    __  ___              __
         timestamp:   /  |/  /__  _______  / /  ___ __ _____
         timestamp:  / /|_/ / _ \/ __/ _ \/ _ \/ -_) // (_-<
         timestamp: /_/  /_/\___/_/ / .__/_//_/\__/\_,_/___/
         timestamp: ****************************************
         timestamp:   Version: |morphver|
         timestamp:   Start Time: xxx xxx xxx 00:00:00 UTC 2024
         timestamp: ****************************************