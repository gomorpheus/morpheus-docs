Database Tier
---------------


Installation and configuration of Percona XtraDB Cluster on CentOS/RHEL 7 can be found at https://www.percona.com/doc/percona-server/LATEST/installation.html.

Requirements
^^^^^^^^^^^^

Percona requires the following ports for the cluster nodes. Please create the appropriate firewall rules on your
Percona nodes.

- 3306
- 4444
- 4567
- 4568


Once you have your database installed and configured:

#. Create the Database you will be using with morpheus.

   .. code-block:: bash

    mysql> CREATE DATABASE morpheusdb;

    mysql> show databases;


#. Next create your morpheus database user. The user needs to be either at the IP address of the morpheus application server or use ``@'%'`` within the user name to allow the user to login from anywhere.

   .. code-block:: bash

    mysql> CREATE USER '$morpheus_db_user_name'@'$source_ip' IDENTIFIED BY '$morpheus_db_user_pw';

#. Next Grant your new morpheus user permissions to the database.

   .. code-block:: bash

    mysql> GRANT ALL PRIVILEGES ON *.* TO '$morpheus_db_user_name'@'$source_ip' IDENTIFIED BY '$morpheus_db_user_pw' with grant option;

    mysql>  GRANT SELECT, PROCESS, SHOW DATABASES, SUPER ON *.* TO 'morpheusdbuser'@'$source_ip' IDENTIFED BY PASSWORD 'secretpasshere';

    mysql> FLUSH PRIVILEGES;

#. Checking Permissions for your user.

   .. code-block:: bash

    SHOW GRANTS FOR '$morpheus_db_user_name'@'$source_ip';
