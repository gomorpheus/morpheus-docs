RabbitMQ Cluster
----------------

RabbitMQ Installation and Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary.

Prerequisites
.................

.. code-block:: bash

  yum install epel-release
  yum install erlang

Install RabbitMQ on the 3 nodes
...............................

.. note::

	For the most up to date RPM package please use this link: https://www.rabbitmq.com/install-rpm.html#downloads

.. code-block:: bash

  wget https://dl.bintray.com/rabbitmq/rabbitmq-server-rpm/rabbitmq-server-3.6.12-1.el7.noarch.rpm

   rpm --import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc

   yum -y install rabbitmq-server-3.6.12-1.el7.noarch.rpm

   chkconfig rabbitmq-server on

   rabbitmq-server -detached

On Node 1:
..........

.. code-block:: bash

  cat /var/lib/rabbitmq/.erlang.cookie

Copy this value

On Nodes 2 & 3:
...............

#. Overwrite ``/var/lib/rabbitmq/.erlang.cookie`` with value from previous step and change its permissions using the follow commands.

   .. code-block:: bash

    chown rabbitmq:rabbitmq /var/lib/rabbitmq/*
    chmod 400 /var/lib/rabbitmq/.erlang.cookie


#. edit ``/etc/hosts`` file to refer to shortname of node 1

   example:

   .. code-block:: bash

    10.30.20.100 rabbit-1

#. Run the commands to join each node to the cluster

   .. code-block:: bash

    rabbitmqctl stop
    rabbitmq-server -detached
    rabbitmqctl stop_app
    rabbitmqctl join_cluster rabbit@<<node 1 shortname>>
    rabbitmqctl start_app


  .. note:: If you receive an error ``ERROR: unable to connect to node 'rabbit@ha': nodedown`` run the following commands

      .. code-block:: bash

        sudo ps aux | grep rabbit | grep -v grep | awk '{print $2}' | xargs kill -9
        ps aux | grep rabbit  "to make sure rabbit is down"
        rabbitmq-server -detached
        "if detach was passed then run" ps aux | grep rabbit "to make sure rabbit is up and running"

      Now ``rabbitmqctl stop`` should work


On Node 1:
..........

.. code-block:: bash

   rabbitmqctl add_user <<admin username>> <<password>>
   rabbitmqctl set_permissions -p / <<admin username>> ".*" ".*" ".*"
   rabbitmqctl set_user_tags <<admin username>> administrator

On All Nodes:
.............

.. code-block:: bash

  rabbitmq-plugins enable rabbitmq_stomp
