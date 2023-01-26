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

           [root@node-3 ~]# rabbitmqctl join_cluster rabbit@node01

           Clustering node 'rabbit@node-3' with 'rabbit@node01' ...

           [root@node-3 ~]# rabbitmqctl start_app

           Starting node 'rabbit@node03' ...

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

      [root@node-1/2/3 ~]# morpheus-ctl tail morpheus-ui