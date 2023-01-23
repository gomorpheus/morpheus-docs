RabbitMQ Cluster
^^^^^^^^^^^^^^^^

An HA deployment will also include a Highly Available RabbitMQ.  This can be achieved through RabbitMQ's HA-Mirrored Queues on at least 3, independent nodes.  To accomplish this we recommend following Pivotal's documentation on RabbitMQ here: https://www.rabbitmq.com/ha.html and https://www.rabbitmq.com/clustering.html

Install RabbitMQ on the 3 nodes and create a cluster.

.. NOTE:: For the most up to date RPM package we recommend using this link: :link: https://www.rabbitmq.com/install-rpm.html#downloads

.. IMPORTANT:: Morpheus connects to AMQP over 5672 or 5671(SSL) and 61613 or 61614(SSL)

RabbitMQ Installation and Configuration
```````````````````````````````````````

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary.

RabbitMQ requires Erlang to be installed, the exact version will depend on which version of RabbitMQ you're installing on your queue-tier nodes. Click the link below to expand a compatibility table for RabbitMQ and Erlang. Note that |morpheus| is compatible with RabbitMQ 3.5.x and higher, however, versions 3.7.x and earlier have reached their end of life and RabbitMQ does not encourage their use. If needed, a compatibility table for these sunsetted versions is in `RabbitMQ documentation <https://www.rabbitmq.com/which-erlang.html#eol-series>`_.

.. toggle-header:: :header: **RabbitMQ/Erlang Compatibility Table**

    .. list-table::
       :header-rows: 1

       * - RabbitMQ Version
         - Minimum Required Erlang/OTP
         - Maximum Supported Erlang/OTP
       * - 3.9.x
         - 23.2
         - 24.x
       * - 3.8.16 - 3.8.19
         - 23.2
         - 24.x
       * - 3.8.9 - 3.8.15
         - 22.3
         - 23.x
       * - 3.8.4 - 3.8.8
         - 21.3
         - 23.x
       * - 3.8.0 - 3.8.3
         - 21.3
         - 22.x

|

#. Install epel-release and erlang

   .. code-block:: bash

           yum install epel-release
           yum install erlang

#. Install RabbitMQ on all 3 Nodes

   .. code-block:: bash

      wget https://dl.bintray.com/rabbitmq/rabbitmq-server-rpm/rabbitmq-server-3.6.12-1.el7.noarch.rpm

      rpm --import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc

      yum -y install rabbitmq-server-3.6.12-1.el7.noarch.rpm

      chkconfig rabbitmq-server on

      rabbitmq-server -detached

#. Copy the erlang.cookie from Node 1

   .. code-block:: bash

     cat /var/lib/rabbitmq/.erlang.cookie

   # Copy the .erlang.cookie value

#. Overwrite ``/var/lib/rabbitmq/.erlang.cookie`` on Nodes 2 & 3 with value from Node 1 and change its permissions using the follow commands:

   .. code-block:: bash

      chown rabbitmq:rabbitmq /var/lib/rabbitmq/*
      chmod 400 /var/lib/rabbitmq/.erlang.cookie

#. Edit ``/etc/hosts`` file on all 3 nodes to refer to shortnames of the other nodes

   Example for node 1 (adjust for nodes 2 and 3):

   .. code-block:: bash

    vi /etc/hosts

     10.30.20.101 rabbit-2
     10.30.20.102 rabbit-3

#. Run the following commands on Node 2 and on Node 3 to join them to the Cluster:

   .. code-block:: bash

       rabbitmqctl stop
       rabbitmq-server -detached
       rabbitmqctl stop_app
       rabbitmqctl join_cluster rabbit@<<node 1 shortname>>
       rabbitmqctl start_app

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
