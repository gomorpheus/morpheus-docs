.. _aurora-mysql-5_7:

Aurora mySQL 5.7
----------------

Introduction
^^^^^^^^^^^^

Amazon Aurora is a relational database management system (RDBMS) built for the cloud with full mySQL compatibility.  It can be designed to be multi-AZ
capable, allows scaling up, and minimal downtime.

In this document, the non-serverless version will be created and configured.  At the time of this writing, |morpheus| only support mySQL 5.7, which
Aurora only supports on non-serverless.  Aurora Serverless v2 does support mySQL 8 but until |morpheus| supports that version, it is untested.

Being non-serverless means that there will be costs for the instances that back Aurora, as long as it is available.  With serverless, the nodes scale 
as needed, even down to 0, to save costs and you only pay for the compute used.

.. note:: Non-serverless Aurora will turn itself back on each week, if you have it off.  It must be on to perform updates and it will not stay off for longer than 7 days.

Create Aurora Instance (UI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: The following configuration has recommended values but requirements may differ per customer

#. Login to the AWS console:

    http://console.aws.amazon.com/

#. Navigate to the ``EC2`` section by searching at the top
#. Click the ``Security Groups`` link on the left side
#. Create a Security Group that allows ``Inbound`` for port ``3306`` to allow the mySQL traffic into the Aurora instances
#. Once the Securit group is crearted, navigate to the ``RDS`` section by searching at the top
#. Click the ``Subnet groups`` link on the left side
#. Click the ``Create DB subnet group`` button
    
    * Ensure the subnet group contains two AZs at a minimum, to be highly available
    * You will need a subnet created in each AZ under the same VPC, if not already available

#. Click the ``Databases`` link on the left side
#. Click the ``Create New Database`` button
#. Ensure the following settings are chosen for the database:
    
    .. list-table:: ** Minimum Required Database Settings**
        :header-rows: 1

        * - Setting
          - Value
        * - Engine Type
          - Amazon Aurora
        * - Edition
          - Amazon Aurora MySQL-Compatible Edition
        * - Engine Version
          - Aurora (MySQL 5.7) 2.11.1 **(must be MySQL 5.7)**
        * - Templates
          - Production
        * - DB instance class
          - db.r5.large (2 vCPUs 16GB RAM)
        * - Multi-AZ deployment
          - Create an Aurora Replica
        * - Database authentication options
          - Password Authentication
        * - DB subnet group
          - Choose the created DB subnet group
        * - Existing VPC security groups
          - Choose the created Security Group

    .. note:: Any settings not listed above can be kept at their default, or items such as usernames, VPCs, monitoring, etc. are all preferences of the customer and will not affect the performance or availability

    .. important:: **Do not create the initial database** for |morpheus| using the UI, it will be created following the ``app`` documentation

Create Aurora Instance (CLI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are familiar with using the AWS CLI, you can run the following commands to more easily create the database, instead of using the UI.

#. Install the AWS CLI following the documentation:

  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#. Setup the authentication for the AWS CLI, using one of the many methods.  Environment variables are recommended:

  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

#. Finally, run the below commands to create the DB Cluster and DB Instances.  The cluster will contain the instances, which one instance will automatically become the writer instance and one will become the reader instance.

  .. code-block:: bash

      # Set all variables to preferred values
      
      db_subnet_group_name="morpheussubnetgroup"
      # subnet_ids must contain at least two from different AZs that match the availability_zones below
      subnet_ids="subnet-0ed95648b7e27a375 subnet-00422803877471552"
      availability_zones="us-east-2a us-east-2b"
      db_cluster_identifier="morpheus-cluster"
      vpc_security_group_ids="sg-02ce7e19679b4b0a6"
      # Get engine verisons:  aws rds describe-db-engine-versions --engine aurora-mysql --query "DBEngineVersions[].EngineVersion"
      engine_version="5.7.mysql_aurora.2.11.1"
      master_username="admin"
      master_user_password="abc123123"
      db_instance1_identifier="instance1"
      db_instance2_identifier="instance2"

      # Create DB subnet group
      aws rds create-db-subnet-group --db-subnet-group-name $db_subnet_group_name \
      --db-subnet-group-description "Contains subnets for mySQL to be deployed to for Morpheus" \
      --subnet-ids $subnet_ids

      # Create RDS cluster
      aws rds create-db-cluster --availability-zones $availability_zones \
      --db-cluster-identifier $db_cluster_identifier \
      --vpc-security-group-ids $vpc_security_group_ids \
      --db-subnet-group-name $db_subnet_group_name \
      --engine "aurora-mysql" \
      --engine-version $engine_version \
      --master-username $master_username  \
      --master-user-password $master_user_password \
      --no-enable-iam-database-authentication \
      --engine-mode "provisioned" \
      --network-type "IPV4" \
      --backup-retention-period 3 \
      --copy-tags-to-snapshot \
      --tags "Key=application,Value=morpheus" \
      --deletion-protection

      # Create first instance
      aws rds create-db-instance --db-instance-identifier $db_instance1_identifier \
      --db-cluster-identifier $db_cluster_identifier \
      --engine "aurora-mysql" \
      --db-instance-class "db.r5.large" \
      --no-publicly-accessible \
      --no-enable-performance-insights

      # Create second instance
      aws rds create-db-instance --db-instance-identifier $db_instance2_identifier \
      --db-cluster-identifier $db_cluster_identifier \
      --engine "aurora-mysql" \
      --db-instance-class "db.r5.large" \
      --no-publicly-accessible \
      --no-enable-performance-insights