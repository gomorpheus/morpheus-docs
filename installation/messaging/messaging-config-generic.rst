#. Configure node settings

   Set the service to start automatically

    .. code-block:: bash

        systemctl stop rabbitmq-server
        systemctl enable rabbitmq-server

   By default, RabbitMQ will set the nodename to the following format:  rabbit@HOSTNAME  Example:  rabbit@prdrabbit01
   In this case, the HOSTNAME is determined from the system RabbitMQ is being deployed to.  This hostname MUST be resolvable, either by ``/etc/hosts`` or DNS.
   Alternatively, if a different nodename needs to be specified, ``/etc/rabbitmq/rabbitmq-env.conf`` can be created and populated with environment variable overrides.
   These settings are ready in at the time of the service start.  The HOSTNAME after the ``@`` must still be resolvable.  An example is below of changing the nodename to
   ``rabbit@rabbit-1``.
   
   .. code-block:: bash
      
      vim /etc/rabbitmq/rabbitmq-env.conf
         # Input the following line:
         NODENAME=rabbit@rabbit-1

   To verify the name that RabbitMQ has configured **after startup** (steps are below), run the following command:

   .. code-block:: bash

      rabbitmqctl eval "node()."

   .. note:: More environment variables can be found here:  https://www.rabbitmq.com/configure.html#supported-environment-variables
      
#. Ensure that the shortnames of all the nodes can be resolved by all other nodes, either by DNS or ``/etc/hosts``
   Edit ``/etc/hosts`` file on all 3 nodes to refer to shortnames of the other nodes

   Example for node 1 (adjust for nodes 2 and 3):

   .. code-block:: bash

      vi /etc/hosts
         # Input the following lines:
         10.30.20.101 rabbit-2
         10.30.20.102 rabbit-3

#. Start RabbitMQ on each node:

   .. code-block:: bash

      systemctl start rabbitmq-server

#. Copy the erlang.cookie from Node 1

   .. code-block:: bash

     cat /var/lib/rabbitmq/.erlang.cookie

   # Copy the .erlang.cookie value

#. Overwrite ``/var/lib/rabbitmq/.erlang.cookie`` on Nodes 2 & 3 with value from Node 1 and change its permissions using the follow commands:

   .. code-block:: bash

      chown rabbitmq:rabbitmq /var/lib/rabbitmq/.erlang.cookie
      chmod 400 /var/lib/rabbitmq/.erlang.cookie

   Restart the service after changing the cookie, so it uses the new one

   .. code-block:: bash

      systemctl restart rabbitmq-server

#. Run the following commands on Node 2 and on Node 3 to join them to the Cluster:

   .. code-block:: bash
      
      rabbitmqctl stop_app
      rabbitmqctl join_cluster rabbit@<<node 1 shortname>>
      rabbitmqctl start_app

   .. important:: A reminder that the node 1 shortname must be resolvable, in addition to all other node shortnames.

#. The cluster can be validated using the following command from any node.  If successful, all three nodes should be listed under "Running Nodes"

   .. code-block:: bash

      rabbitmqctl cluster_status

#. On Node 1, create vhost and add Admin user for |morpheus|

   .. code-block:: bash

      rabbitmqctl add_vhost morpheus
      rabbitmqctl add_user <<admin username>> <<password>>
      rabbitmqctl set_permissions -p morpheus <<admin username>> ".*" ".*" ".*"
      rabbitmqctl set_user_tags <<admin username>> administrator

#. On All Nodes, enable stomp and management plugins:

   .. code-block:: bash

      rabbitmq-plugins enable rabbitmq_stomp
      rabbitmq-plugins enable rabbitmq_management

#. On Node 1, add the required Rabbitmq Policies. The policies will propagate to all nodes.

   .. code-block:: bash

      rabbitmqctl set_policy -p morpheus --apply-to queues --priority 2 statCommands "statCommands.*" '{"expires":1800000, "ha-mode":"all"}'
      rabbitmqctl set_policy -p morpheus --apply-to queues --priority 2 morpheusAgentActions "morpheusAgentActions.*" '{"expires":1800000, "ha-mode":"all"}'
      rabbitmqctl set_policy -p morpheus --apply-to queues --priority 2 monitorJobs "monitorJobs.*" '{"expires":1800000, "ha-mode":"all"}'
      rabbitmqctl set_policy -p morpheus --apply-to all --priority 1 ha ".*" '{"ha-mode":"all"}'