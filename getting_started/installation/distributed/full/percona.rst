Percona XtraDB Cluster
^^^^^^^^^^^^^^^^^^^^^^

Out of the box Morpheus uses MySQL but Morpheus supports any mySQL compliant database.  There are many ways to set up a highly available, MySQL dialect based database.  One which has found favor with many of our customers is Percona's XtraDB Cluster.  Percona's product is based off of Galera's WSREP Clustering, which is also supported.


.. important:: Additional configuration for Percona Clusters with TLS enabled is required. Refer to :ref:`Percona TLS` Configuration: for details.

Requirements
````````````

.. NOTE:: Morpheus idiomatically connects to database nodes over 3306

Once you have your database installed and configured:


#. Create the Database you will be using with morpheus.

   .. code-block:: bash

    mysql> CREATE DATABASE morpheusdb;

    mysql> show databases;

#. Ensure the database is using UTF-8 collation

    .. code-block:: bash

    mysql> ALTER DATABASE morpheusdb CHARACTER SET utf8 COLLATE utf8_general_ci;

    .. NOTE:: Percona defaults to Latin-1 and, as a result, some customers have created databases with Latin-1 as the default character set. In some cases, this can create problems down the road as the application is accepting UTF-8. Setting UTF-8 collation at the time of database creation may prevent problems in the future.

#. Next, create your morpheus database user. The user needs to be either at the IP address of the morpheus application server or use ``@'%'`` within the user name to allow the user to login from anywhere.

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
