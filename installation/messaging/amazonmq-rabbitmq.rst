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
#. Create a Security Group that allows ``Inbound`` for ports ``5671`` to allow AMQP traffic from the nodes.  Additionally, allow ports ``443`` and ``15671`` to allow access to the web console and management UI
#. Once the Security group is crearted, navigate to the ``Amazon MQ`` section by searching at the top
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
          - Choose one subnet from at least two AZs
        * - Security Group(s)
          - Choose the Security Group previously created

    .. note:: Any settings not listed above can be kept at their default, or items such as usernames, VPCs, maintenance, etc. are all preferences of the customer and will not affect the performance or availability

Create RabbitMQ Broker (CLI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are familiar with using the AWS CLI, you can run the following commands to more easily create the broker, instead of using the UI.

#. Install the AWS CLI following the documentation:

  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#. Setup the authentication for the AWS CLI, using one of the many methods.  Environment variables are recommended:

  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

#. Finally, run the below commands to create the broker:

  Documentation:  https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html

  .. code-block:: bash

      # Set all variables to preferred values
      broker_name="morpheusbroker"
      username="admin"
      # Password must be a minimum 12 characters, at least 4 unique characters. Can't contain commas (,), colons (:), equals signs (=), spaces or non-printable ASCII characters.
      password="abc123123123123"
      security_groups="sg-02ce7e19679b4b0a6"
      subnet_ids="subnet-0ed95648b7e27a375 subnet-00422803877471552"

      # Create Amazone MQ Broker
      aws mq create-broker --auto-minor-version-upgrade \
        --broker-name $broker_name \
        --deployment-mode "CLUSTER_MULTI_AZ" \
        --engine-type "RABBITMQ" \
        --engine-version "3.9.24" \
        --host-instance-type "mq.m5.large" \
        --no-publicly-accessible \
        --users Username=$username,Password=$password \
        --security-groups $security_groups \
        --subnet-ids $subnet_ids \
        --tags "Key=application,Value=morpheus"