.. _amazonmq-rabbitmq:

Amazon MQ (RabbitMQ)
--------------------

Introduction
^^^^^^^^^^^^

Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that streamlines setup, operation, and management of message brokers on AWS.  It can be designed to be multi-AZ
capable, allows scaling up, and minimal downtime.

At the time of this writing, |morpheus| is designed to use RabbitMQ, which means the RabbitMQ Broker Engine must be used.  **Do not select Apache ActiveMQ** as the Broker Engine.

Create RabbitMQ Broker (UI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: The following configuration has recommended values but requirements may differ per customer

#. Login to the AWS console:

    http://console.aws.amazon.com/

#. Navigate to the ``EC2`` section by searching at the top
#. Click the ``Security Groups`` link on the left side
#. Create a Security Group that allows ``Inbound`` for port ``5671`` to allow AMQP traffic from the nodes.  Additionally, allow ports ``443`` and ``15671`` to allow access to the web console and management UI via TLS, either can access the API.
#. Once the Security Group is crearted, navigate to the ``Amazon MQ`` section by searching at the top
#. Click the ``Get started`` button.  If the ``Get started`` button is not available, click the ``Brokers`` link on the left side and then click the ``Create brokers`` button
#. Choose the ``RabbitMQ`` broker engine, then click ``Next``
#. Choose the ``Cluster deployment`` deployment mode, then click ``Next``
#. Ensure the following settings are chosen for the broker:
    
    .. list-table:: **Minimum Required Broker Settings**
        :header-rows: 1

        * - Setting
          - Value
        * - Broker instance type
          - mq.m5.large
        * - Broker engine version
          - 3.9.24 **(must be 3.9.x)**
        * - Access type
          - Private access
        * - VPC and subnets
          - Select existing VPC and subnet(s) - Choose one subnet from at least two AZs
        * - Security Group(s)
          - Choose the Security Group previously created

    .. note:: Any settings not listed above can be kept at their default, or items such as usernames, VPCs, maintenance, etc. are all preferences of the customer and will not affect the performance or availability

#. Once the broker has been fully created, click on the hyperlink of it in the ``Brokers`` section
#. Note the ``RabbitMQ web console`` path for the next steps
#. Note the ``Endpoints`` path for ``AMQP``, which will be used when configuring Morpheus (without the ``amqps://``)
#. Note that the  next steps, the system attempting to access the path MUST be connected to the VPC, or travels through it, as the cluster is private and not publicly accessible
#. Run the following commands to configure the RabbitMQ cluster via the API, replacing ``$console_url`` with the path noted previously.  Additionally, replace ``$morpheus_user`` and ``$morpheus_password`` with the username and password that should be created the Morpheus will use to connect with
  
    .. code-block:: bash

        curl --user admin:abc123123123123 -X PUT $console_url/api/vhosts/morpheus
        curl --user admin:abc123123123123 -X PUT $console_url/api/users/$morpheus_user -d '{"password":"'$morpheus_password'","tags":"administrator"}'
        curl --user admin:abc123123123123 -X PUT $console_url/api/permissions/morpheus/$morpheus_user -d '{"configure":".*","write":".*","read":".*"}'
        curl --user admin:abc123123123123 -X PUT $console_url/api/policies/morpheus/statCommands -d '{"pattern":"statCommands.*", "definition":{"expires":1800000, "ha-mode":"all"}, "priority":2, "apply-to":"queues"}'
        curl --user admin:abc123123123123 -X PUT $console_url/api/policies/morpheus/morpheusAgentActions -d '{"pattern":"morpheusAgentActions.*", "definition":{"expires":1800000, "ha-mode":"all"}, "priority":2, "apply-to":"queues"}'
        curl --user admin:abc123123123123 -X PUT $console_url/api/policies/morpheus/monitorJobs -d '{"pattern":"monitorJobs.*", "definition":{"expires":1800000, "ha-mode":"all"}, "priority":2, "apply-to":"queues"}'
        curl --user admin:abc123123123123 -X PUT $console_url/api/policies/morpheus/ha -d '{"pattern":".*", "definition":{"ha-mode":"all"}, "priority":1, "apply-to":"all"}'

Create RabbitMQ Broker (CLI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are familiar with using the AWS CLI, you can run the following commands to more easily create the broker, instead of using the UI.

#. Install the AWS CLI following the documentation:  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#. Setup the authentication for the AWS CLI, using one of the many methods.  Environment variables are recommended:  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

#. Finally, run the below commands to create the broker:

  Documentation:  https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-broker.html

  .. code-block:: bash

      # Set all variables to preferred values
      broker_name="morpheusbroker"
      admin_username="admin"
      # Password must be a minimum 12 characters, at least 4 unique characters. Can't contain commas (,), colons (:), equals signs (=), spaces or non-printable ASCII characters.
      admin_password="abc123123123123"
      security_groups="sg-01d8ca613f69ec769"
      subnet_ids="subnet-0ed95648b7e27a375 subnet-00422803877471552"

      # Username and password Morpheus will use to connect with
      morpheus_user="morpheus-user"
      # Password must be a minimum 12 characters, at least 4 unique characters. Can't contain commas (,), colons (:), equals signs (=), spaces or non-printable ASCII characters.
      morpheus_password="abc123123123123"
      

      # Create Amazon MQ Broker and get the ID
      broker_id=$(aws mq create-broker --auto-minor-version-upgrade \
        --broker-name $broker_name \
        --deployment-mode "CLUSTER_MULTI_AZ" \
        --engine-type "RABBITMQ" \
        --engine-version "3.9.24" \
        --host-instance-type "mq.m5.large" \
        --no-publicly-accessible \
        --users Username=$admin_username,Password=$admin_password \
        --security-groups $security_groups \
        --subnet-ids $subnet_ids \
        --tags "Key=application,Value=morpheus" \
        --no-paginate | grep "BrokerId" | awk '{print $2}' | sed -r 's/"|,//g')

      # Revrieve the details
      console_url="$(aws mq describe-broker --broker-id $broker_id | grep 'ConsoleURL' | awk '{print $2}' | sed -r 's/"|,//g')"
      echo "Endpoint:  $(aws mq describe-broker --broker-id $broker_id | grep 'amqps://' | sed -r 's/"|,|amqps:\/\/| //g')"

      # Configures the RabbitMQ cluster
      # Note that these commands MUST be ran by a system on the VPC, such as the Morpheus nodes, as the cluster is private
      curl --user admin:abc123123123123 -X PUT $console_url/api/vhosts/morpheus
      curl --user admin:abc123123123123 -X PUT $console_url/api/users/$morpheus_user -d '{"password":"'$morpheus_password'","tags":"administrator"}'
      curl --user admin:abc123123123123 -X PUT $console_url/api/permissions/morpheus/$morpheus_user -d '{"configure":".*","write":".*","read":".*"}'
      curl --user admin:abc123123123123 -X PUT $console_url/api/policies/morpheus/statCommands -d '{"pattern":"statCommands.*", "definition":{"expires":1800000, "ha-mode":"all"}, "priority":2, "apply-to":"queues"}'
      curl --user admin:abc123123123123 -X PUT $console_url/api/policies/morpheus/morpheusAgentActions -d '{"pattern":"morpheusAgentActions.*", "definition":{"expires":1800000, "ha-mode":"all"}, "priority":2, "apply-to":"queues"}'
      curl --user admin:abc123123123123 -X PUT $console_url/api/policies/morpheus/monitorJobs -d '{"pattern":"monitorJobs.*", "definition":{"expires":1800000, "ha-mode":"all"}, "priority":2, "apply-to":"queues"}'
      curl --user admin:abc123123123123 -X PUT $console_url/api/policies/morpheus/ha -d '{"pattern":".*", "definition":{"ha-mode":"all"}, "priority":1, "apply-to":"all"}'