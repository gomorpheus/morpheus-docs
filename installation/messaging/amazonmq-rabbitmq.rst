.. _amazonmq-rabbitmq:

Amazon MQ (RabbitMQ)
^^^^^^^^^^^^^^^^^^^^

Introduction
````````````

Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that streamlines setup, operation, and management of message brokers on AWS.  It can be designed to be multi-AZ
capable, allows scaling up, and minimal downtime.

At the time of this writing, |morpheus| is designed to use RabbitMQ, which means the RabbitMQ Broker Engine must be used.  **Do not select Apache ActiveMQ** as the Broker Engine.

Create RabbitMQ Broker (UI)
```````````````````````````

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
#. Note the ``Endpoints`` path for ``AMQP`` for the next steps, which will also be used when configuring Morpheus (without the ``amqps://``)

Create RabbitMQ Broker (CLI)
````````````````````````````

If you are familiar with using the AWS CLI, you can run the following commands to more easily create the broker, instead of using the UI.

#. Install the AWS CLI following the documentation:  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
#. Setup the authentication for the AWS CLI, using one of the many methods.  Environment variables are recommended:  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
#. Run the below commands to create the broker:

  Documentation:  https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-broker.html

  .. code-block:: bash

    # Set all variables to preferred values
    mq_broker_name='morpheusbroker'
    mq_admin_username='admin'
    # Password must be a minimum 12 characters, at least 4 unique characters. Can't contain commas (,), colons (:), equals signs (=), spaces or non-printable ASCII characters.
    mq_admin_password='abc123123123123'
    mq_security_groups='sg-01d8ca613f69ec769'
    mq_subnet_ids='subnet-0ed95648b7e27a375 subnet-00422803877471552'

    # Create Amazon MQ Broker and get the ID
    broker_id=$(aws mq create-broker --auto-minor-version-upgrade \
      --broker-name $mq_broker_name \
      --deployment-mode 'CLUSTER_MULTI_AZ' \
      --engine-type 'RABBITMQ' \
      --engine-version '3.9.24' \
      --host-instance-type 'mq.m5.large' \
      --no-publicly-accessible \
      --users Username=$mq_admin_username,Password=$mq_admin_password \
      --security-groups $mq_security_groups \
      --subnet-ids $mq_subnet_ids \
      --tags 'Key=application,Value=morpheus' \
      --no-paginate | grep 'BrokerId' | awk '{print $2}' | sed -r 's/"|,//g')

    # Retrieve the details - instance needs to be almost ready for these to be available
    echo "Console URL:  $(aws mq describe-broker --broker-id $mq_broker_id | grep 'ConsoleURL' | awk '{print $2}' | sed -r 's/"|,//g')"
    echo "Endpoint:  $(aws mq describe-broker --broker-id $mq_broker_id | grep 'amqps://' | sed -r 's/"|,|amqps:\/\/| //g')"

#. Note the ``Console URL`` path for the next steps
#. Note the ``Endpoint`` path for ``AMQP`` for the next steps, which will also be used when configuring Morpheus

Configure RabbitMQ
``````````````````

.. important:: Note that the next steps, the system attempting to access the path MUST be connected to the VPC, or travels through it, as the cluster is private and not publicly accessible

  .. code-block:: ruby

    # Note that these commands MUST be ran by a system on the VPC, such as the Morpheus nodes, as the cluster is private
    # Note the above note ^^^^^^^^
    mq_console_url=<pasteConsoleURL>
    mq_admin_username='admin'
    mq_admin_password='abc123123123123'
    mq_morpheus_username='morpheus-user'
    # Password must be a minimum 12 characters, at least 4 unique characters. Can't contain commas (,), colons (:), equals signs (=), spaces or non-printable ASCII characters.
    mq_morpheus_password='abc123123123123'
    curl --user $mq_admin_username:$mq_admin_password -X PUT $mq_console_url/api/vhosts/morpheus
    curl --user $mq_admin_username:$mq_admin_password -X PUT $mq_console_url/api/users/$mq_morpheus_username -d '{"password":"'$mq_morpheus_password'","tags":"administrator"}'
    curl --user $mq_admin_username:$mq_admin_password -X PUT $mq_console_url/api/permissions/morpheus/$mq_morpheus_username -d '{"configure":".*","write":".*","read":".*"}'
    curl --user $mq_admin_username:$mq_admin_password -X PUT $mq_console_url/api/policies/morpheus/statCommands -d '{"pattern":"statCommands.*", "definition":{"expires":1800000, "ha-mode":"all"}, "priority":2, "apply-to":"queues"}'
    curl --user $mq_admin_username:$mq_admin_password -X PUT $mq_console_url/api/policies/morpheus/morpheusAgentActions -d '{"pattern":"morpheusAgentActions.*", "definition":{"expires":1800000, "ha-mode":"all"}, "priority":2, "apply-to":"queues"}'
    curl --user $mq_admin_username:$mq_admin_password -X PUT $mq_console_url/api/policies/morpheus/monitorJobs -d '{"pattern":"monitorJobs.*", "definition":{"expires":1800000, "ha-mode":"all"}, "priority":2, "apply-to":"queues"}'
    curl --user $mq_admin_username:$mq_admin_password -X PUT $mq_console_url/api/policies/morpheus/ha -d '{"pattern":".*", "definition":{"ha-mode":"all"}, "priority":1, "apply-to":"all"}'

Example morpheus.rb File Section
````````````````````````````````

File ``/etc/morpheus/morpheus.rb``

  .. code-block:: ruby
      
    rabbitmq['enable'] = false
    rabbitmq['host'] = 'b-dc5b6c9b-112f-4ebe-a53b-129328fd2f2f.mq.us-east-2.amazonaws.com'
    rabbitmq['port'] = '5671'
    rabbitmq['vhost'] = 'morpheus'
    rabbitmq['queue_user'] = 'morpheus-user'
    rabbitmq['queue_user_password'] = 'abc123123123123'
    rabbitmq['use_tls'] = true