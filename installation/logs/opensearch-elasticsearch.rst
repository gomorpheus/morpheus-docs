.. _opensearch-elasticsearch:

Amazon OpenSearch (Elasticsearch)
---------------------------------

Introduction
^^^^^^^^^^^^

AAmazon OpenSearch Service makes it easy for you to perform interactive log analytics, real-time application monitoring, website search, and more. 
OpenSearch is an open source, distributed search and analytics suite derived from Elasticsearch.  It can be designed to be multi-AZ capable, allows 
scaling up, and minimal downtime.

At the time of this writing, |morpheus| is designed to use Elasticsearch, which means the Elastisearch engine should be used.

.. note:: The OpenSearch engine has been seen to work on the current version but general support is not available yet for |morpheus|

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
          - **Checked**
        * - Fine-grained access control
          - Enter a username and password for the administrator account
        * - Access Policy
          - Choose "Only use fine-grained access control"

    .. note:: Any settings not listed above can be kept at their default, or items such as usernames, VPCs, maintenance, etc. are all preferences of the customer and will not affect the performance or availability

Create Elasticsearch Domain (CLI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are familiar with using the AWS CLI, you can run the following commands to more easily create the domain, instead of using the UI.

#. Install the AWS CLI following the documentation:  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
#. Setup the authentication for the AWS CLI, using one of the many methods.  Environment variables are recommended:  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
#. Finally, run the below commands to create the domain:

  Documentation:  https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/create-domain.html

  .. code-block:: bash

      # Set all variables to preferred values
      es_domain_name='morpheusdomain'
      es_security_group_ids='sg-0c6cd7efd0cff7696'
      es_subnet_ids='subnet-0ed95648b7e27a375,subnet-00422803877471552'
      es_volume_size_gb='10'
      es_master_username='admin'
      # Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.
      es_master_password='Abc123123@'

      # Create Amazon OpenSearch Domain
      aws opensearch create-domain --domain-name $es_domain_name \
        --engine-version 'Elasticsearch_7.10' \
        --cluster-config InstanceType=m6g.large.search,InstanceCount=2,DedicatedMasterEnabled=true,ZoneAwarenessEnabled=true,ZoneAwarenessConfig={AvailabilityZoneCount=2},DedicatedMasterType=m6g.large.search,DedicatedMasterCount=3 \
        --ebs-options EBSEnabled=true,VolumeType=gp2,VolumeSize=$es_volume_size_gb \
        --advanced-security-options "Enabled=true,InternalUserDatabaseEnabled=true,MasterUserOptions={MasterUserName=$es_master_username,MasterUserPassword=$es_master_password}" \
        --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"*"},"Action":"es:*","Resource":"arn:aws:es:us-east-2:426242579432:domain/'$es_domain_name'/*"}]}' \
        --vpc-options SubnetIds=$es_subnet_ids,SecurityGroupIds=$es_security_group_ids \
        --encryption-at-rest-options Enabled=true \
        --node-to-node-encryption-options Enabled=true \
        --domain-endpoint-options EnforceHTTPS=true \
        --tag-list 'Key=application,Value=morpheus'

      # Retrieve the details - instance needs to be ready for this to be available
      echo "Endpoint:  $(aws opensearch describe-domain --domain-name $es_domain_name --no-paginate | grep '"vpc":' | awk '{print $2}' | sed -r 's/"//g')"

Testing Elasticsearch Domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the following command to test the cluster, replacing the ``es_master_username`` and ``es_master_password`` with the username and password created. Also, replace ``es_domain_endpoint`` with the ``Domain endpoint (VPC)`` located on the OpenSearch cluster

  .. code-block:: bash

    # Note that these commands MUST be ran by a system on the VPC, such as the Morpheus nodes, as the cluster is private
    # Note the above note ^^^^^^^^

    es_domain_endpoint='<pastedEndpoint>'
    es_master_username='admin'
    es_master_password='Abc123123@'
    curl --user $es_master_username:$es_master_password https://$es_domain_endpoint/_cluster/health?pretty
  
  Documentation: https://www.elastic.co/guide/en/elasticsearch/reference/current/http-clients.html

Example Morpheus.rb File Section
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. code-block:: ruby

    elasticsearch['enable'] = false
    elasticsearch['auth_user'] = 'admin'
    elasticsearch['auth_password'] = 'Abc123123@'
    elasticsearch['cluster'] = 'morpheusdomain'
    elasticsearch['es_hosts'] = {'vpc-morpheusdomain-4ypsets66htlwedmhew45kfxd4.us-east-2.es.amazonaws.com' => 443}
    elasticsearch['use_tls'] = true