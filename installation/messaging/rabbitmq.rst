RabbitMQ Cluster
^^^^^^^^^^^^^^^^

An HA deployment will also include a Highly Available RabbitMQ.  This can be achieved through RabbitMQ's HA-Mirrored Queues on at least 3, independent nodes.  To accomplish this we recommend following Pivotal's documentation on RabbitMQ here: https://www.rabbitmq.com/ha.html and https://www.rabbitmq.com/clustering.html

Install RabbitMQ on the 3 nodes and create a cluster.

.. NOTE:: For the most up to date RPM package we recommend using this link: :link: https://www.rabbitmq.com/install-rpm.html#downloads

.. IMPORTANT:: Morpheus connects to AMQP over 5672 or 5671(SSL) and 61613 or 61614(SSL)

Requirements
````````````

RabbitMQ requires the following TCP ports for the cluster nodes. Please create the appropriate firewall rules on your
Percona nodes.

  - 4369
  - 5671 (TLS)
  - 5672
  - 15671 (TLS)
  - 15672
  - 25672
  - 61613
  - 61614 (TLS)

  .. code-block:: bash

    [root]# firewall-cmd --zone=public --add-port={4369/tcp,5671/tcp,5672/tcp,15671/tcp,15672/tcp,25672/tcp,61613/tcp,61614/tcp} --permanent
    [root]# firewall-cmd --reload

Install the versionlock plugin for dnf to lock the version of packages

   .. code-block:: bash

      dnf install python3-dnf-plugin-versionlock -y

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

#. Install erlang and rabbitmq-server repositories using Cloudsmith.io, as recommended by RabbitMQ's documentation:

   `RabbitMQ Documentation <https://www.rabbitmq.com/install-rpm.html#cloudsmith>`_
   `Cloudsmith.io erlang Documentation <https://cloudsmith.io/~rabbitmq/repos/rabbitmq-erlang/setup/#formats-rpm>`_
   `Cloudsmith.io rabbitmq-server Documentation <https://cloudsmith.io/~rabbitmq/repos/rabbitmq-server/setup/#formats-rpm>`_

   .. code-block:: bash

      curl -1sLf 'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/setup.rpm.sh' | sudo -E bash
      curl -1sLf 'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-server/setup.rpm.sh' | sudo -E bash

#. The below commands will locate all versions available for erlang and rabbitmq-server but only install the OTP and RAbbitMQ version that is listed as supported above in the **RabbitMQ/Erlang Compatibility Table**

   .. code-block:: bash

      dnf --showduplicates list erlang
      dnf --showduplicates list rabbitmq-server

   .. important:: In this example, we'll install 24.3.4.7-1.el8 OTP/erlang and rabbitmq-server-3.9.27-1.el8.noarch RabbitMQ. At the time of this writing, 24.x OTP and 3.9 RabbitMQ are the maximum supported versions

#. Install the pacakges using the versions selected above:

   .. code-block:: bash

      dnf install erlang-24.3.4.7-1.el8.x86_64 -y
      dnf install rabbitmq-server-3.9.27-1.el8.noarch -y

   .. important:: Format is [package-name]-[version].[architecture]

#. Pin the packages to ensure they are not accidentally upgraded:

   .. code-block:: bash

      dnf versionlock erlang-24.3.4.7-1.el8.x86_64
      dnf versionlock rabbitmq-server-3.9.27-1.el8.noarch

   .. note:: Instructions to enable versionlock is listed in the **Requirements** section

#. Configure node settings

   Set the service to start automatically

   .. code-block:: bash

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

   To verify the name that RabbitMQ has configured after startup, run the following command:

   .. code-block:: bash

      rabbitmqctl eval "node()."

   .. note:: More environment variables can be found here:  https://www.rabbitmq.com/configure.html#supported-environment-variables
      
#. Copy the erlang.cookie from Node 1

   .. code-block:: bash

     cat /var/lib/rabbitmq/.erlang.cookie

   # Copy the .erlang.cookie value

#. Overwrite ``/var/lib/rabbitmq/.erlang.cookie`` on Nodes 2 & 3 with value from Node 1 and change its permissions using the follow commands:

   .. code-block:: bash

      chown rabbitmq:rabbitmq /var/lib/rabbitmq/*
      chmod 400 /var/lib/rabbitmq/.erlang.cookie

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

#. Run the following commands on Node 2 and on Node 3 to join them to the Cluster:

   .. code-block:: bash

       rabbitmqctl stop_app
       rabbitmqctl join_cluster rabbit@<<node 1 shortname>>
       rabbitmqctl start_app

   .. important:: A reminder that the node 1 shortname must be resolvable, in addition to all other node shortnames.

#. The cluster can be validated using the following command.  IF successful, all three nodes should be listed under "Running Nodes"

   .. code-block:: bash

      rabbitmqctl cluster_status

#. On Node 1, create vhost and add Admin user for |morpheus|

   .. code-block:: bash

      rabbitmqctl add_vhost morpheus
      rabbitmqctl add_user \<\<admin username>> \<\<password>>
      rabbitmqctl set_permissions -p morpheus \<\<admin username>> ".*" ".*" ".*"
      rabbitmqctl set_user_tags \<\<admin username>> administrator

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