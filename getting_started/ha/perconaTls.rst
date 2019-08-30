Install Percona XtraDB Cluster with TLS
---------------------------------------

Installation and configuration of Percona XtraDB Cluster on CentOS/RHEL 7 with TLS enabled for all comms.

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary.

Requirements
^^^^^^^^^^^^

Percona requires the following ports for the cluster nodes. Please create the appropriate firewall rules on your
Percona nodes.

- 3306
- 4444
- 4567
- 4568

Add Percona Repo
^^^^^^^^^^^^^^^^

#. Add the percona repo to your Linux Distro.

   .. code-block:: bash

    sudo yum install http://www.percona.com/downloads/percona-release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm

#. Check the repo by running the below command.

   .. code-block:: bash

    sudo yum list | grep percona

#. The below commands will clean the repos and update the server.

   .. code-block:: bash

    sudo yum clean all
    sudo yum update -y --skip-broken

Installing Percona XtraDB Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. The below command will install the Percona XtraDB Cluster software and it’s dependences.

   .. code-block:: bash

    sudo yum install Percona-XtraDB-Cluster-57

   .. NOTE:: During the installation you will need to Accept the Percona PGP key to install the software.

#. Next we need enable the mysql service so that the service started at boot.

   .. code-block:: bash

    sudo systemctl enable mysql

#. Next we need to start mysql

   .. code-block:: bash

    sudo systemctl start mysql

#. Next we will log into the mysql server and set a new password. To get the temporary root mysql password you will need to run the below command.The command will print the password to the screen. Copy the password.

   .. code-block:: bash

      sudo grep 'temporary password' /var/log/mysqld.log

#. Login to mysql

   .. code-block:: bash

    mysql -u root -p
    password: `enter password copied above`

#. Change the root user password to the mysql db

   .. code-block:: bash

    ALTER USER 'root'@'localhost' IDENTIFIED BY 'rootPassword';

#. Create the sstuser user and grant the permissions.

   .. code-block:: bash

    mysql> CREATE USER 'sstuser'@'localhost' IDENTIFIED BY 'sstUserPassword';

   .. NOTE:: The sstuser and password will be used in the /etc/my.cnf configuration.

   .. code-block:: bash

    mysql> GRANT RELOAD, LOCK TABLES, PROCESS, REPLICATION CLIENT ON *.* TO 'sstuser'@'localhost';

    mysql> FLUSH PRIVILEGES;

#. Exit mysql then stop the mysql services:

   .. code-block:: bash

    mysql> exit
    Bye
    $ sudo systemctl stop mysql.service

#. Now install Percona on to the other nodes using the same steps.

Once the service is stopped on all nodes move onto the next step.

Add [mysqld] to my.cnf in /etc/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Add the following to ``/etc/my.cnf``.  The node_name and node_address needs to be unique on each of the nodes.

Node 01:

   .. code-block:: bash

      [root]# vi /etc/my.cnf

   .. code-block:: bash

      [mysqld]
      pxc_encrypt_cluster_traffic=ON
      max_connections = 300
      wsrep_provider=/usr/lib64/galera3/libgalera_smm.so

      wsrep_cluster_name=morpheusdb-cluster
      wsrep_cluster_address=gcomm://10.30.20.10,10.30.20.11,10.30.20.12

      # for wsrep_cluster_address=gcomm://Enter the IP address of the primary node first then remaining nodes. Separating the ip addresses with commas

      wsrep_node_name=morpheus-node01
      wsrep_node_address=10.30.20.10

      wsrep_sst_method=xtrabackup-v2
      wsrep_sst_auth=sstuser:sstUserPassword
      pxc_strict_mode=PERMISSIVE
      wsrep_sync_wait=2

      skip-log-bin
      default_storage_engine=InnoDB
      innodb_autoinc_lock_mode=2


Node 02

   .. code-block:: bash

      $ [root]# vi /etc/my.cnf

   .. code-block:: bash

      [mysqld]
      pxc_encrypt_cluster_traffic=ON
      max_connections = 300
      wsrep_provider=/usr/lib64/galera3/libgalera_smm.so

      wsrep_cluster_name=morpheusdb-cluster
      wsrep_cluster_address=gcomm://10.30.20.10,10.30.20.11,10.30.20.12

      # for wsrep_cluster_address=gcomm://Enter the IP address of the primary node first then remaining nodes. Separating the ip addresses with commas

      wsrep_node_name=morpheus-db-node02
      wsrep_node_address=10.30.20.11

      wsrep_sst_method=xtrabackup-v2
      wsrep_sst_auth=sstuser:sstUserPassword
      pxc_strict_mode=PERMISSIVE
      wsrep_sync_wait=2

      skip-log-bin
      default_storage_engine=InnoDB
      innodb_autoinc_lock_mode=2

Node 03

   .. code-block:: bash

      $ [root]# vi /etc/my.cnf

   .. code-block:: bash

      [mysqld]
      pxc_encrypt_cluster_traffic=ON
      max_connections = 300
      wsrep_provider=/usr/lib64/galera3/libgalera_smm.so

      wsrep_cluster_name=morpheusdb-cluster
      wsrep_cluster_address=gcomm://10.30.20.10,10.30.20.11,10.30.20.12

      # for wsrep_cluster_address=gcomm://Enter the IP address of the primary node first then remaining nodes. Separating the ip addresses with commas

      wsrep_node_name=morpheus-node03
      wsrep_node_address=10.30.20.12

      wsrep_sst_method=xtrabackup-v2
      wsrep_sst_auth=sstuser:sstUserPassword
      pxc_strict_mode=PERMISSIVE
      wsrep_sync_wait=2

      skip-log-bin
      default_storage_engine=InnoDB
      innodb_autoinc_lock_mode=2

      .. note:: The default setting on |morpheus| app nodes for ``max_active`` database connections is 100. For this example we are setting ``max_connections = 300`` to account for 3 maximum simultaneous morpheus app node connections. If ``max_active`` is configured higher on the app nodes, or the number of app nodes is not 3, adjust accordingly for your configuration.

#. Save ``/etc/my.cnf``

Bootstrap Node 01
^^^^^^^^^^^^^^^^^

.. IMPORTANT:: Ensure mysql.service is stopped prior to bootstrap.

#. To bootstrap the first node in the cluster run the below command.

   .. code-block:: bash

    systemctl start mysql@bootstrap.service

   .. NOTE:: The mysql service will start during the bootstrap.

   .. NOTE:: Startup failures are commonly caused by misconfigured ``/etc/my.cnf`` files. Also verify ``safe_to_bootstrap`` is set to ``1`` on Node 01.

Configure Morpheus Database and User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Create the Database you will be using with morpheus.

Login to mysql on Node 01:

   .. code-block:: bash

    mysql -u root -p
    password:

    mysql> CREATE DATABASE morpheusdb;

    mysql> show databases;


#. Next create your morpheus database user. This is the user the morpheus app nodes will auth with mysql.

   .. code-block:: bash

    mysql> CREATE USER 'morpheusDbUser'@'%' IDENTIFIED BY 'morpheusDbUserPassword';

#. Next Grant your new morpheus user permissions.

   .. code-block:: bash

    mysql> GRANT ALL PRIVILEGES ON *.* TO 'morpheusDbUser'@'%' IDENTIFIED BY 'morpheusDbUserPassword' with grant option;

    mysql> FLUSH PRIVILEGES;

    .. important:: If you grant privileges to the morpheusDbUser to only the morpheusdb database, you will also need to GRANT SELECT, PROCESS, SHOW DATABASES, SUPER ON PRIVILEGES to the morpheusDbUser on *.* for the Appliance Health service.

Copy SSL Files to other nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During initialization of Node 01 the required `pem` files will be generated in ``/var/lib/mysql``. The ``ca.pem``, ``server-cert.pem`` and ``server-key.pem`` files need to match on all nodes in the cluster.

#. Copy the following files from Node 01 to the same path (default is /var/lib/mysql) on Node 02 and Node 03:

   .. code-block:: bash

    /var/lib/mysql/ca.pem
    /var/lib/mysql/server-cert.pem
    /var/lib/mysql/server-key.pem

    .. important:: Ensure all 3 files match on all 3 nodes, including path, owner and permissions.

    .. note:: The generated certificate is self signed. Consult Percona documentation for [mysqld] and SSL file configuration when providing your own.

Start the Remaining Nodes
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Start mysql on Node 02 and Node 03

   .. code-block:: bash

    sudo systemctl start mysql.service

   The services will automatically join the cluster using the sstuser we created earlier.

   .. NOTE:: Startup failures are commonly caused by misconfigured /etc/my.cnf files.

Verification
^^^^^^^^^^^^

#. To verify the cluster, on the master login to mysql and run ``show status like 'wsrep%';``

   .. code-block:: bash

     $ mysql -u root -p

      mysql>  show status like 'wsrep%';

#. Verify ``wsrep_cluster_size`` is ``3`` and ``wsrep_incoming_addresses`` lists all 3 node ip addresses.

#. From all |morpheus| app nodes, verify that you can login to all 3 database nodes

   .. code-block:: bash

    mysql -u morpheusDbUser -p  -h 10.30.20.10
    mysql -u morpheusDbUser -p  -h 10.30.20.11
    mysql -u morpheusDbUser -p  -h 10.30.20.12

If you are unable to login to mysql from an app node, ensure credentials are correct, privileges have been granted, and mysql is running.

To validate network accessibility, use telnet to verify app node can reach db nodes on 3306: ``telnet 10.30.20.10 3306``

#. All done!
