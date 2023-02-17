.. _opensearch-elasticsearch:

Amazon OpenSearch (Elasticsearch)
---------------------------------

Introduction
^^^^^^^^^^^^

Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that streamlines setup, operation, and management of message brokers on AWS.  It can be designed to be multi-AZ
capable, allows scaling up, and minimal downtime.

At the time of this writing, |morpheus| is designed to use RabbitMQ, which means the RabbitMQ Broker Engine must be used.  **Do not select Apache ActiveMQ** as the Broker Engine.

Create Elasticsearch Domain (UI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: The following configuration has recommended values but requirements may differ per customer

#. Login to the AWS console:

    http://console.aws.amazon.com/

#. Navigate to the ``EC2`` section by searching at the top
#. Click the ``Security Groups`` link on the left side
#. Create a Security Group that allows ``Inbound`` for port ``443`` to allow access to the API from the nodes
#. Once the Security group is crearted, navigate to the ``Amazon OpenSearch Service`` section by searching at the top
#. Click the ``Get started`` button.  If the ``Get started`` button is not available, click the ``Domains`` link on the left side and then click the ``Create domain`` button
#. Ensure the following settings are chosen for the domain:
    
    .. list-table:: **Minimum Required Domain Settings**
        :header-rows: 1

        * - Setting
          - Value
        * - Deployment type
          - Production
        * - Version
          - Elasticsearch 7.10
        * - Availability Zones
          - 2-AZ (3-AZ is also acceptable)
        * - (Data Nodes) Instance type
          - m6g.large.search
        * - EBS storage size per node
          - 2 (3 if 3-AZ was chosen)
        * - EBS volume type
          - gp2
        * - EBS storage size per node
          - Refer to the internal storage calculator
        * - (Dedicated master nodes) Instance Type
          - m6g.large.search
        * - Number of master nodes
          - 3
        * - Network
          - VPC access (recommended)
        * - Subnets
          - Choose one subnet from at least two AZs
        * - Security Group(s)
          - Choose the Security Group previously created
        * - Fine-grained access control
          - **Unchecked**

    .. note:: Any settings not listed above can be kept at their default, or items such as usernames, VPCs, maintenance, etc. are all preferences of the customer and will not affect the performance or availability

Create Elasticsearch Domain (UI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are familiar with using the AWS CLI, you can run the following commands to more easily create the broker, instead of using the UI.

#. Install the AWS CLI following the documentation:

  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#. Setup the authentication for the AWS CLI, using one of the many methods.  Environment variables are recommended:

  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

#. Finally, run the below commands to create the broker:

  Documentation:  https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/create-domain.html

  .. code-block:: bash

      # Set all variables to preferred values
      domain_name="morpheusdomain"
      
      # username="admin"
      # Password must be a minimum 12 characters, at least 4 unique characters. Can't contain commas (,), colons (:), equals signs (=), spaces or non-printable ASCII characters.
      # password="abc123123123123"
      security_group_ids="sg-0c6cd7efd0cff7696"
      subnet_ids="subnet-0ed95648b7e27a375,subnet-00422803877471552"
      volume_size_gb="10"

      # Create Amazone MQ Broker
      aws opensearch create-domain --domain-name $domain_name \
        --engine-version "Elasticsearch_7.10" \
        --cluster-config InstanceType=m6g.large.search,InstanceCount=2,DedicatedMasterEnabled=true,ZoneAwarenessEnabled=true,ZoneAwarenessConfig={AvailabilityZoneCount=2},DedicatedMasterType=m6g.large.search,DedicatedMasterCount=3 \
        --ebs-options EBSEnabled=true,VolumeType=gp2,VolumeSize=$volume_size_gb \
        --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Deny","Principal":{"AWS":"*"},"Action":"es:*","Resource":"arn:aws:es:us-east-2:426242579432:domain/testdomain/*"}]}' \
        --vpc-options SubnetIds=$subnet_ids,SecurityGroupIds=$security_group_ids \
        --encryption-at-rest-options Enabled=true \
        --node-to-node-encryption-options Enabled=true \
        --domain-endpoint-options EnforceHTTPS=true \
        --tag-list "Key=application,Value=morpheus"