.. _perconainstall:

Percona XtraDB Cluster
^^^^^^^^^^^^^^^^^^^^^^

Out of the box Morpheus uses MySQL but Morpheus supports any mySQL compliant database.  There are many ways to set up a highly available, MySQL dialect based database.  One which has found favor with many of our customers is Percona's XtraDB Cluster.  Percona's product is based off of Galera's WSREP Clustering, which is also supported.

.. important:: Currently, you must use a v5.7-compatible version of MySQL/Percona. Complete compatibility information is available in the `Compatibility and Breaking Changes <https://docs.morpheusdata.com/en/latest/release_notes/compatibility.html>`_ page. Additional configuration for Percona Clusters with TLS enabled is required. Refer to :ref:`Percona TLS` Configuration in our full HA docs for details.

Storage Requirements
````````````````````

- 30 GB storage minimum for each database node. This should be monitored and increased if the Morpheus database requires more space.

After database installation ensure that the minimum storage requirement is available for the mysql tmpdir. By default mysql will write temporary files in "/tmp". 
The mysql tmpdir configuration can be modified using the following steps for each database node:

#.  Create the new directory.

   .. code-block:: bash

    mkdir /path/to/mysql/tmp/directory
    chown -R mysql:mysql /path/to/mysql/tmp/directory

#. Edit /etc/my.cnf.

   .. code-block:: bash

    [mysqld]
    tmpdir=/path/to/mysql/tmp/directory


.. important:: Failing to provide sufficient storage to the mysql tmpdir can result in failed database migrations and Morpheus upgrades.

Permission Requirements
```````````````````````

.. NOTE:: Morpheus idiomatically connects to database nodes over 3306

Once you have your database installed and configured:


#. The |morpheus| appliance uses the utf8 character set and the UTC+0 timezone. Set the variables below on your external database clusters to prevent timestamp errors from being thrown later in |morpheus| UI. For all distributions, the configuration is set in /etc/my.cnf for each database node.

   .. code-block:: bash

    [mysql]
    default-character-set = utf8

    [mysqld]
    default_time_zone = "+00:00"

#. Create the Database you will be using with morpheus.

   .. code-block:: bash

    mysql> CREATE DATABASE morpheus CHARACTER SET utf8 COLLATE utf8_general_ci;

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
