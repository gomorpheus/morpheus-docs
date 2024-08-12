.. _opensearch-2x:

Amazon OpenSearch 2.x
^^^^^^^^^^^^^^^^^^^^^

Introduction
````````````

Amazon OpenSearch Service makes it easy for you to perform interactive log analytics, real-time application monitoring, website search, and more. 
OpenSearch is an open source, distributed search and analytics suite derived from Elasticsearch.  It can be designed to be multi-AZ capable, allows 
scaling up, and minimal downtime.

At the time of this writing, |morpheus| has confirmed supportability for OpenSearch 2.x.  OpenSearch 1.x and the Elasticsearch 7.10 were used previously, as they were either 
plain Elasticsearch or backwards compatible with Elasticsearch 7.10.  However, with the licensing change of Elasticsearch, OpenSearch was created and has begun to deviate 
from the original Elasticsearch 7.10 code.  This means they may be treated as two differnt products, even though most of the base is still the same.  Elasticsearch 2.x is 
still very close to the same as Elasticsearch but there may be differences between them that |morpheus| will need to continue to support.

Create OpenSearch Domain (UI)
`````````````````````````````

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
      * - Domain Creation Method
        - Standard create
      * - Deployment type
        - Production
      * - Deployment option(s)
        - Domain **without** standby
      * - Availability Zones
        - 3-AZ recommended (2-AZ is possible, see notes below) 
      * - Version
        - (latest) (2.13 tested at the time of this writing)
      * - (Data Nodes) Instance type
        - (General Purpose) m6g.large.search
      * - Number of Nodes
        - 3 (2 if 2-AZ was chosen)
      * - EBS volume type
        - gp3 (gp2 is possible)
      * - EBS storage size per node
        - Refer to the [Storage Calculator](https://docs.morpheusdata.com/en/latest/getting_started/requirements/requirements.html#storage-considerations)
      * - (Dedicated master nodes) Instance Type
        - (General Purpose) m6g.large.search
      * - Number of master nodes
        - 3
      * - Network
        - VPC access (recommended)
      * - Subnets
        - Choose one subnet from at least three AZs (or two if 2-AZ was chosen)
      * - Security Group(s)
        - Choose the Security Group previously created
      * - Fine-grained access control
        - **Checked**
      * - Fine-grained access control
        - **Check** Create master user
      * - Fine-grained access control
        - Enter a username and password for the administrator account
      * - Access Policy
        - Choose "Only use fine-grained access control"

  .. note:: Any settings not listed above can be kept at their default, or items such as usernames, VPCs, maintenance, etc. are all preferences of the customer and will not affect the performance or availability

  .. important:: 
    If ``Domain with standby`` or ``2-AZ`` is chosen, the following line is required in the ``morpheus.rb`` file:  

    ``elasticsearch['replica_count'] = 2``

Create OpenSearch Domain (CLI)
``````````````````````````````

If you are familiar with using the AWS CLI, you can run the following commands to more easily create the domain, instead of using the UI.

#. Install the AWS CLI following the documentation:  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
#. Setup the authentication for the AWS CLI, using one of the many methods.  Environment variables are recommended:  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
#. Finally, run the below commands to create the domain:

  Documentation:  https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/create-domain.html

  .. code-block:: bash

    # Set all variables to preferred values
    es_domain_name='morpheusdomain'
    es_security_group_ids='sg-0c6cd7efd0cff7696'
    es_subnet_ids='subnet-0ed95648b7e27a375,subnet-00422803877471552,subnet-0d15255413b36bb8d'
    es_volume_size_gb='10' # Use the storage calculator to help determine the size needed
    es_master_username='admin'
    # Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.
    es_master_password='Abc123123@'
    aws_account_id='426242579432'

    # Create Amazon OpenSearch Domain
    aws opensearch create-domain --domain-name $es_domain_name \
      --engine-version 'OpenSearch_2.13' \
      --cluster-config "MultiAZWithStandbyEnabled=false,InstanceType=m6g.large.search,InstanceCount=3,DedicatedMasterEnabled=true,ZoneAwarenessEnabled=true,ZoneAwarenessConfig={AvailabilityZoneCount=3},DedicatedMasterType=m6g.large.search,DedicatedMasterCount=3" \
      --ebs-options "EBSEnabled=true,VolumeType=gp3,VolumeSize=$es_volume_size_gb" \
      --advanced-security-options "Enabled=true,InternalUserDatabaseEnabled=true,MasterUserOptions={MasterUserName=$es_master_username,MasterUserPassword=$es_master_password}" \
      --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"*"},"Action":"es:*","Resource":"arn:aws:es:us-east-2:'$aws_account_id':domain/'$es_domain_name'/*"}]}' \
      --vpc-options "SubnetIds=$es_subnet_ids,SecurityGroupIds=$es_security_group_ids" \
      --encryption-at-rest-options 'Enabled=true' \
      --node-to-node-encryption-options 'Enabled=true' \
      --domain-endpoint-options 'EnforceHTTPS=true' \
      --tag-list 'Key=application,Value=morpheus'

    # Retrieve the details - instance needs to be ready for this to be available
    echo "Endpoint:  $(aws opensearch describe-domain --domain-name $es_domain_name --no-paginate | grep '"vpc":' | awk '{print $2}' | sed -r 's/"//g')"

Testing Elasticsearch Domain
````````````````````````````

#. Run the following command to test the cluster, replacing the ``es_master_username`` and ``es_master_password`` with the username and password created. Also, replace ``es_domain_endpoint`` with the ``Domain endpoint (VPC)`` located on the OpenSearch cluster

  .. code-block:: bash

    # Note that these commands MUST be ran by a system on the VPC, such as the Morpheus nodes, as the cluster is private
    # Note the above note ^^^^^^^^

    es_domain_endpoint='<pasteEndpointUrl>'
    es_master_username='admin'
    es_master_password='Abc123123@'
    curl --user $es_master_username:$es_master_password $es_domain_endpoint/_cluster/health?pretty
  
  Documentation: https://www.elastic.co/guide/en/elasticsearch/reference/current/http-clients.html

Example morpheus.rb File Section
````````````````````````````````

File ``/etc/morpheus/morpheus.rb``

  .. code-block:: ruby

    elasticsearch['enable'] = false
    elasticsearch['auth_user'] = 'admin'
    elasticsearch['auth_password'] = 'Abc123123@'
    elasticsearch['cluster'] = 'morpheusdomain'
    elasticsearch['es_hosts'] = {'vpc-morpheusdomain-4ypsets66htlwedmhew45kfxd4.us-east-2.es.amazonaws.com' => 443}
    elasticsearch['use_tls'] = true
    # elasticsearch['replica_count'] is only needed if the option of "Domain with standby" or a "2-AZ" was chosen, as mentioned previously
    # elasticsearch['replica_count'] = 2