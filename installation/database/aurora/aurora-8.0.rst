.. _aurora-mysql-8_0:

Aurora (MySQL 8.0)
^^^^^^^^^^^^^^^^^^

Introduction
````````````

Amazon Aurora is a relational database management system (RDBMS) built for the cloud with full MySQL compatibility.  It can be designed to be multi-AZ
capable, allows scaling up, and minimal downtime.

In this document, the non-serverless version will be created and configured.  At the time of this writing, |morpheus| only supports MySQL 5.7 and 8.0, but 5.7
is being deprecated.  Aurora Serverless v2 does support MySQL 8.0 but until |morpheus| tests it, it is unsupported.

Being non-serverless means that there will be costs for the instances that back Aurora, as long as it is available.  With serverless, the nodes scale 
as needed, even down to 0, to save costs and you only pay for the compute used.

.. note:: Non-serverless Aurora will turn itself back on each week, if you have it off.  It must be on to perform updates and it will not stay off for longer than 7 days.

Create Aurora Instance (UI)
```````````````````````````

.. note:: The following configuration has recommended values but requirements may differ per customer

#. Login to the AWS console:

    http://console.aws.amazon.com/

#. Navigate to the ``EC2`` section by searching at the top
#. Click the ``Security Groups`` link on the left side
#. Create a Security Group that allows ``Inbound`` for port ``3306`` to allow the MySQL traffic into the Aurora instances
#. Once the Security Group is crearted, navigate to the ``RDS`` section by searching at the top
#. Click the ``Subnet groups`` link on the left side
#. Click the ``Create DB subnet group`` button
    
    * Ensure the subnet group contains two AZs at a minimum, to be highly available
    * You will need a subnet created in each AZ under the same VPC, if not already available

#. Click the ``Databases`` link on the left side
#. Click the ``Create New Database`` button
#. Ensure the following settings are chosen for the database:
    
    .. list-table:: **Minimum Required Database Settings, others are at the customer's discretion**
        :header-rows: 1

        * - Setting
          - Value
        * - Creation Method
          - Standard Create
        * - Engine Type
          - Aurora (MySQL Compatible)
        * - Engine Version
          - Aurora MySQL 3.05.2 (compatible with MYSQL 8.0.32) **(a higher 8.0 version can be chosen)**
        * - Templates
          - Production
        * - DB Cluster Identifier
          - Enter a name for the RDS in AWS
        * - Master username
          - Enter a username and note it for later
        * - Credential Management
          - Self-managed is recommended but either way be sure to note the password for later
        * - DB instance class
          - db.r6g.large (2 vCPUs 16GB RAM)
        * - Multi-AZ deployment
          - Create an Aurora Replica
        * - Network type
          - Be sure this matches the subnets being deployed to.  For example, if the subnets supports IPv4 and IPv6, choose dual-stack mode
        * - VPC and DB subnet group
          - Choose the previously created DB subnet group from the correct VPC
        * - Existing VPC security groups
          - Choose the previously created Security Group

    .. note:: Any settings not listed above can be kept at their default, or items such as usernames, VPCs, monitoring, etc. are all preferences of the customer and will not affect the performance or availability

    .. important:: **Do not create the initial database** for |morpheus| using the UI, it will be created following the ``App`` documentation

Create Aurora Instance (CLI)
````````````````````````````

If you are familiar with using the AWS CLI, you can run the following commands to more easily create the database, instead of using the UI.

#. Install the AWS CLI following the documentation:  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#. Setup the authentication for the AWS CLI, using one of the many methods.  Environment variables are recommended:  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

#. Finally, run the below commands to create the DB Cluster and DB Instances.  The cluster will contain the instances, which one instance will automatically become the writer instance and one will become the reader instance.

  Documentation:  https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html

  .. code-block:: bash

      # Set all variables to preferred values
      
      db_subnet_group_name='morpheussubnetgroup'
      # subnet_ids must contain at least two from different AZs that match the availability_zones below
      subnet_ids='subnet-0ed95648b7e27a375 subnet-00422803877471552'  # Space separated list
      availability_zones='us-east-2a us-east-2b'  # Space separated list
      db_cluster_identifier='morpheus-cluster'
      vpc_security_group_ids='sg-0a24611271fd99b3a'
      # Get a list of engine verisons:  aws rds describe-db-engine-versions --engine aurora-mysql --query "DBEngineVersions[].EngineVersion"
      engine_version='8.0.mysql_aurora.3.05.2'
      master_username='admin'
      # Password must be at least 8 printable ASCII characters. Can't contain any of the following: / (slash), '(single quote), "(double quote) and @
      master_user_password='abc123123'
      db_instance1_identifier='instance1'
      db_instance2_identifier='instance2'

      # Create DB subnet group
      aws rds create-db-subnet-group --db-subnet-group-name $db_subnet_group_name \
        --db-subnet-group-description 'Contains subnets for MySQL to be deployed to for Morpheus' \
        --subnet-ids $subnet_ids

      # Create RDS cluster
      aws rds create-db-cluster --availability-zones $availability_zones \
        --db-cluster-identifier $db_cluster_identifier \
        --vpc-security-group-ids $vpc_security_group_ids \
        --db-subnet-group-name $db_subnet_group_name \
        --engine 'aurora-mysql' \
        --engine-version $engine_version \
        --master-username $master_username  \
        --master-user-password $master_user_password \
        --no-enable-iam-database-authentication \
        --engine-mode 'provisioned' \
        --network-type 'IPV4' \
        --backup-retention-period 3 \
        --copy-tags-to-snapshot \
        --tags 'Key=application,Value=morpheus' \
        --deletion-protection

      # Create first instance
      aws rds create-db-instance --db-instance-identifier $db_instance1_identifier \
        --db-cluster-identifier $db_cluster_identifier \
        --engine 'aurora-mysql' \
        --db-instance-class 'db.r6g.large' \
        --no-publicly-accessible \
        --no-enable-performance-insights

      # Create second instance
      aws rds create-db-instance --db-instance-identifier $db_instance2_identifier \
        --db-cluster-identifier $db_cluster_identifier \
        --engine 'aurora-mysql' \
        --db-instance-class 'db.r6g.large' \
        --no-publicly-accessible \
        --no-enable-performance-insights

Configure Morpheus Database and User
````````````````````````````````````

#. Create the Database you will be using with |morpheus|.  Login to Aurora on **Node 01**:

   .. code-block:: bash

    [root]# /opt/morpheus/embedded/bin/mysql -h 'database-1.cluster-cgguv6wqc1al.us-east-2.rds.amazonaws.com' -u admin -p
      password: `enter admin password`

    mysql> CREATE DATABASE morpheus CHARACTER SET utf8 COLLATE utf8_general_ci;

    mysql> show databases;

#. Next create your |morpheus| database user. This is the user the |morpheus| app nodes will auth with Aurora:

   .. code-block:: bash

    mysql> CREATE USER 'morpheusDbUser'@'%' IDENTIFIED BY 'morpheusDbUserPassword';

#. Next grant your new |morpheus| user permissions:

   .. code-block:: bash

    mysql> GRANT ALL PRIVILEGES ON morpheus.* TO 'morpheusDbUser'@'%' with grant option;

    mysql> GRANT SELECT, PROCESS, SHOW DATABASES, RELOAD ON *.* TO 'morpheusDbUser'@'%';

    mysql> FLUSH PRIVILEGES;

    mysql> exit

#. The database should be prepared for |morpheus| to connect

Example morpheus.rb File Section
````````````````````````````````

File ``/etc/morpheus/morpheus.rb``

  .. code-block:: ruby

    mysql['enable'] = false
    mysql['host'] = 'morpheus-cluster.cluster-cgguv6wqc1al.us-east-2.rds.amazonaws.com'
    mysql['morpheus_db'] = 'morpheus'
    mysql['morpheus_db_user'] = 'morpheusDbUser'
    mysql['morpheus_password'] = 'morpheusDbUserPassword'