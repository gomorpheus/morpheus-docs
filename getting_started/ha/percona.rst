Database Tier
---------------


Morpheus needs a database to connect to.  Out of the box Morpheus uses MySQL but Morpheus supports any mySQL compliant database.  There are many ways to set up a highly available, MySQL dialect based database.  One which has found favor with many of our customers is Percona's XtraDB Cluster.  Percona's product is based off of Galera's WSREP Clustering, which is also supported.

If you're not as familiar with WSREP and prefer replication, some of our customers prefer to configure a failover connection to a MariaDB or MySQL based Master/Master Replication cluster.  Less often used, though still a viable option, is MySQL based NDB Clustering.  Wonderful guides for each of these HA and DR based database management strategies can be found here: https://www.percona.com/doc/percona-xtradb-cluster/LATEST/index.html


Requirements
^^^^^^^^^^^^

.. NOTE:: Morpheus idiomatically connects to database nodes over 3306

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

    mysql> GRANT ALL PRIVILEGES ON morpheus_db_name.* TO 'morpheus_db_user'@'$source_ip' IDENTIFIED BY 'morpheus_db_user_pw' with grant option;

    mysql>  GRANT SELECT, PROCESS, SHOW DATABASES, SUPER ON *.* TO 'morpheus_db_user'@'$source_ip' IDENTIFIED BY 'morpheus_db_user_pw';

    mysql> FLUSH PRIVILEGES;

#. Checking Permissions for your user.

   .. code-block:: bash

    SHOW GRANTS FOR '$morpheus_db_user_name'@'$source_ip';
