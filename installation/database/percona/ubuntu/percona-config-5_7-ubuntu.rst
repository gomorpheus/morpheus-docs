Add Percona Repo
````````````````

Additional information can be found below:
`Using percona-release <https://docs.percona.com/percona-software-repositories/installing.html>`_
`percona-release Documentation <https://docs.percona.com/percona-software-repositories/percona-release.html>`_
`percona-release Repository Locations <https://docs.percona.com/percona-software-repositories/repository-location.html>`_

#. Add the Percona repo to your Linux Distro.

   .. code-block:: bash

    [root]# apt update -y
    [root]# apt install curl -y
    [root]# curl -O https://repo.percona.com/apt/percona-release_latest.generic_all.deb
    [root]# apt install gnupg2 lsb-release ./percona-release_latest.generic_all.deb -y
    [root]# apt update -y
    [root]# percona-release setup pxc-57

Installing Percona XtraDB Cluster
``````````````````````````````````

#. Install the Percona XtraDB Cluster software and it’s dependences on each database node.

   .. code-block:: bash

    [root]# apt install percona-xtradb-cluster-57 -y
       set root password during install

#. Enable the mysql service so that the service starts at boot on each database node.

   .. code-block:: bash

    [root]# systemctl enable mysql

#. Start mysql on each database node.

   .. code-block:: bash

    [root]# systemctl start mysql

#. From **Node 01**, log into the mysql server using the password set during installation

   .. code-block:: bash

    [root]# mysql -u root -p
       password: `enter password from installation`

#. **(Optional)** Change the root user password to the mysql DB.  Note that the database from Node 01 will be replicated to all other nodes, changing the password on the additional nodes is not required.

   .. code-block:: bash

    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'rootPassword';

#. Create the sstuser user, grant the permissions, and exit mysql.

   .. code-block:: bash

    mysql> CREATE USER 'sstuser'@'localhost' IDENTIFIED BY 'sstUserPassword';

   .. NOTE:: The sstuser and password will be used in the /etc/my.cnf configuration.

   .. code-block:: bash

    mysql> GRANT RELOAD, LOCK TABLES, PROCESS, REPLICATION CLIENT ON *.* TO 'sstuser'@'localhost';

    mysql> FLUSH PRIVILEGES;

    mysql> exit
    Bye

#. Stop the mysql service on **all nodes**
   
   .. code-block:: bash

    [root]# systemctl stop mysql

Once the service is stopped on all nodes move onto the next step.

Add [mysqld] to my.cnf in /etc/mysql/
```````````````````````````````

#. Add the following to ``/etc/mysql/my.cnf``.  The ``wsrep_node_name`` and ``wsrep_node_address`` fields must to be unique on each of the nodes.  The ``wsrep_sst_auth`` field should match the SST username and password created previously.

   .. content-tabs::

      .. tab-container:: tab1
         :title: DB Node 1

         .. code-block:: bash

            [root]# nano /etc/mysql/my.cnf

            [mysqld]
            pxc_encrypt_cluster_traffic=ON
            max_connections = 451
            max_allowed_packet = 256M
            
            wsrep_provider=/usr/lib/galera3/libgalera_smm.so
            wsrep_provider_options="cert.optimistic_pa=NO"
            wsrep_certification_rules='OPTIMIZED'
            
            wsrep_cluster_name=morpheusdb-cluster
            wsrep_cluster_address=gcomm://192.168.101.01,192.168.101.02,192.168.101.03
            
            wsrep_node_name=morpheus-db-node01
            wsrep_node_address=192.168.101.01
            
            wsrep_sst_method=xtrabackup-v2
            wsrep_sst_auth=sstuser:sstUserPassword
            pxc_strict_mode=PERMISSIVE
            wsrep_sync_wait=2
            
            skip-log-bin
            default_storage_engine=InnoDB
            innodb_autoinc_lock_mode=2
            character-set-server=utf8
            default_time_zone="+00:00"

      .. tab-container:: tab2
         :title: DB Node 2

         .. code-block:: bash

            [root]# nano /etc/mysql/my.cnf

            [mysqld]
            pxc_encrypt_cluster_traffic=ON
            max_connections = 451
            max_allowed_packet = 256M
            
            wsrep_provider=/usr/lib/galera3/libgalera_smm.so
            wsrep_provider_options="cert.optimistic_pa=NO"
            wsrep_certification_rules='OPTIMIZED'
            
            wsrep_cluster_name=morpheusdb-cluster
            wsrep_cluster_address=gcomm://192.168.101.01,192.168.101.02,192.168.101.03
            
            wsrep_node_name=morpheus-db-node02
            wsrep_node_address=192.168.101.02
            
            wsrep_sst_method=xtrabackup-v2
            wsrep_sst_auth=sstuser:sstUserPassword
            pxc_strict_mode=PERMISSIVE
            wsrep_sync_wait=2
            
            skip-log-bin
            default_storage_engine=InnoDB
            innodb_autoinc_lock_mode=2
            character-set-server=utf8
            default_time_zone="+00:00"


      .. tab-container:: tab3
         :title: DB Node 3

         .. code-block:: bash

            [root]# nano /etc/mysql/my.cnf

            [mysqld]
            pxc_encrypt_cluster_traffic=ON
            max_connections = 451
            max_allowed_packet = 256M
            
            wsrep_provider=/usr/lib/galera3/libgalera_smm.so
            wsrep_provider_options="cert.optimistic_pa=NO"
            wsrep_certification_rules='OPTIMIZED'
            
            wsrep_cluster_name=morpheusdb-cluster
            wsrep_cluster_address=gcomm://192.168.101.01,192.168.101.02,192.168.101.03
            
            wsrep_node_name=morpheus-db-node03
            wsrep_node_address=192.168.101.03
            
            wsrep_sst_method=xtrabackup-v2
            wsrep_sst_auth=sstuser:sstUserPassword
            pxc_strict_mode=PERMISSIVE
            wsrep_sync_wait=2
            
            skip-log-bin
            default_storage_engine=InnoDB
            innodb_autoinc_lock_mode=2
            character-set-server=utf8
            default_time_zone="+00:00"
            
   .. note:: The default setting on |morpheus| app nodes for ``max_active`` database connections is 150. For this example we are setting ``max_connections = 451`` to account for 3 maximum simultaneous |morpheus| app node connections. If ``max_active`` is configured higher on the app nodes, or the number of app nodes is not 3, adjust accordingly for your configuration.

#. Save ``/etc/mysql/my.cnf``

Bootstrap Node 01
`````````````````

.. IMPORTANT:: Ensure mysql.service is stopped prior to bootstrap.

#. To bootstrap the first node in the cluster run the below command.

   .. code-block:: bash

    [root]# /etc/init.d/mysql bootstrap-pxc

   .. NOTE:: The mysql service will start during the bootstrap.

   .. NOTE:: Startup failures are commonly caused by misconfigured ``/etc/mysql/my.cnf`` files. Also verify ``safe_to_bootstrap`` is set to ``1`` on Node 01 in ``/var/lib/mysql/grastate.dat``.

.. include:: /installation/database/percona/percona-config-5_7-generic.rst

Verify Configuration
````````````````````

#. To verify all nodes joined the cluster, on any db node login to mysql and run ``show status like 'wsrep%';``

   .. code-block:: bash

    [root@anyDbNode]# mysql -u root -p

    mysql>  show status like 'wsrep%';

#. Verify ``wsrep_cluster_size`` is ``3`` and ``wsrep_incoming_addresses`` lists all 3 node ip addresses.

#. From all |morpheus| app nodes, verify that you can login to all 3 database nodes

   .. code-block:: bash

    [root@allAppNodes] cd /opt/morpheus/embedded/bin/
    [root@appNode01]# ./mysql -h 192.168.101.01 -u morpheusDbUser -p
    [root@appNode02]# ./mysql -h 192.168.101.02 -u morpheusDbUser -p
    [root@appNode03]# ./mysql -h 192.168.101.03 -u morpheusDbUser -p

If you are unable to login to mysql from an app node, ensure credentials are correct, privileges have been granted, mysql is running, and ports are open.

To validate network accessibility, use telnet to verify app node can reach db nodes on 3306: ``telnet 192.168.101.01 3306``