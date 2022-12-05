.. _Percona TLS:

CentOS/RHEL Percona XtraDB Cluster with TLS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Out of the box |morpheus| uses MySQL but |morpheus| supports any mySQL-compliant database. There are many ways to set up a highly available, MySQL dialect-based database. One which has found favor with many of our customers is Percona's XtraDB Cluster.  Percona's product is based off of Galera's WSREP Clustering, which is also supported.

.. important:: Currently, you must use a v5.7-compatible version of MySQL/Percona. Complete compatibility information is available in the `Compatibility and Breaking Changes <https://docs.morpheusdata.com/en/latest/release_notes/compatibility.html>`_ page. Additional configuration for Percona Clusters with TLS enabled is required. Refer to :ref:`Percona TLS` Configuration in our full HA docs for details.

Installation and configuration of Percona XtraDB Cluster on **CentOS/RHEL 8** with TLS enabled for all communication.  Refer to :ref:`Percona-TLS-ubuntu` for **Debian/Ubuntu**.

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary.

Additional information can be found here:

`XtraDB 5.7 Installation <https://www.percona.com/doc/percona-xtradb-cluster/5.7/install/yum.html>`_

Requirements
````````````

**Storage Requirements**

   30 GB storage minimum for each database node. This should be monitored and increased if the |morpheus| database requires more space.

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


   .. important:: Failing to provide sufficient storage to the mysql tmpdir can result in failed database migrations and |morpheus| upgrades.

Current Operating System (OS) support can be found here:

`XtraDB 5.7 Support <https://www.percona.com/services/policies/percona-software-support-lifecycle#mysql>`_

Percona requires the following TCP ports for the cluster nodes. Please create the appropriate firewall rules on your
Percona nodes.

  - 3306
  - 4444
  - 4567
  - 4568

  .. code-block:: bash

    [root]# firewall-cmd --add-port={3306/tcp,4444/tcp,4567/tcp,4568/tcp}

The following OS repositories are required, in addition to the Percona repositories:
  
  - rhel-8-for-x86_64-baseos-rpms
  - rhel-8-for-x86_64-appstream-rpms

Configure SElinux
`````````````````

Percona recommends setting SELinux from ``enforcing`` to ``permissive`` to eliminate interference.  Run the following to set SELinux to permissive on each database node:
  
  .. code-block:: bash

    [root]# setenforce 0
    [root]# sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/selinux/config

If enforcing is required by the organization, SELinux rules can be added to ensure interference is eliminated.  To allow Percona XtraDB Cluster functionality when SELinux is ``Enforcing``, run the following on each database Node:

#. Install SELinux utilities

   .. code-block:: bash

    [root]# yum install -y policycoreutils-python.x86_64

#. Configure Percona ports for SELinux:

   .. code-block:: bash

    [root]# semanage port -m -t mysqld_port_t -p tcp 4444
    [root]# semanage port -m -t mysqld_port_t -p tcp 4567
    [root]# semanage port -a -t mysqld_port_t -p tcp 4568

#. Create the policy file PXC.te

   .. code-block:: bash

    [root]# vi PXC.te
    module PXC 1.0;
    require {
            type unconfined_t;
            type mysqld_t;
            type unconfined_service_t;
            type tmp_t;
            type sysctl_net_t;
            type kernel_t;
            type mysqld_safe_t;
            class process { getattr setpgid };
            class unix_stream_socket connectto;
            class system module_request;
            class file { getattr open read write };
            class dir search;
      }

      #============= mysqld_t ==============

     allow mysqld_t kernel_t:system module_request;
     allow mysqld_t self:process { getattr setpgid };
     allow mysqld_t self:unix_stream_socket connectto;
     allow mysqld_t sysctl_net_t:dir search;
     allow mysqld_t sysctl_net_t:file { getattr open read };
     allow mysqld_t tmp_t:file write;

#. Compile and load the SELinux policy

   .. code-block:: bash

    [root]# checkmodule -M -m -o PXC.mod PXC.te
    [root]# semodule_package -o PXC.pp -m PXC.mod
    [root]# semodule -i PXC.pp


Add Percona Repo
````````````````

Additional information can be found here:

`Using percona-release <https://docs.percona.com/percona-software-repositories/installing.html>`_

`percona-release Documentation <https://docs.percona.com/percona-software-repositories/percona-release.html>`_

`percona-release Repository Locations <https://docs.percona.com/percona-software-repositories/repository-location.html>`_

#. Add the Percona repo to your Linux Distro.

   .. code-block:: bash

    [root]# yum install -y https://repo.percona.com/yum/percona-release-latest.noarch.rpm 
    [root]# percona-release setup pxc-57

#. The below commands will clean the repos and update the server.

   .. code-block:: bash

    [root]# yum clean all
    [root]# yum update -y --skip-broken

Installing Percona XtraDB Cluster
``````````````````````````````````

#. Install the Percona XtraDB Cluster software and it’s dependences on each database node.

   .. code-block:: bash

    [root]# yum install -y Percona-XtraDB-Cluster-57

#. Enable the mysql service so that the service starts at boot on each database node.

   .. code-block:: bash

    [root]# systemctl enable mysql

#. Start mysql on each database node.

   .. code-block:: bash

    [root]# systemctl start mysql

#. From **Node 01**, log into the mysql server and set a new root password. To get the temporary root mysql password you will need to run the below command.  The command will print the password to the screen. Copy the password and use it when logging in.

   .. code-block:: bash

    [root]# grep 'temporary password' /var/log/mysqld.log
    [root]# mysql -u root -p
       password: `enter password copied above`

#. Change the root user password to the mysql DB.  Note that the database from Node 1 will be replicated to all other nodes, changing the password on the additional nodes is not required.

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

Add [mysqld] to my.cnf in /etc/
```````````````````````````````

#. Add the following to ``/etc/my.cnf``.  The ``wsrep_node_name`` and ``wsrep_node_address`` fields must to be unique on each of the nodes.  The ``wsrep_sst_auth`` field should match the SST username and password created previously.

   .. content-tabs::

      .. tab-container:: tab1
         :title: DB Node 1

         .. code-block:: bash

            [root]# vi /etc/my.cnf

            [mysqld]
            pxc_encrypt_cluster_traffic=ON
            max_connections = 451
            max_allowed_packet = 256M
            
            wsrep_provider=/usr/lib64/galera3/libgalera_smm.so
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

            [root]# vi /etc/my.cnf

            [mysqld]
            pxc_encrypt_cluster_traffic=ON
            max_connections = 451
            max_allowed_packet = 256M
            
            wsrep_provider=/usr/lib64/galera3/libgalera_smm.so
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

            [root]# vi /etc/my.cnf

            [mysqld]
            pxc_encrypt_cluster_traffic=ON
            max_connections = 451
            max_allowed_packet = 256M
            
            wsrep_provider=/usr/lib64/galera3/libgalera_smm.so
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

#. Save ``/etc/my.cnf``

Bootstrap Node 01
`````````````````

.. IMPORTANT:: Ensure mysql.service is stopped prior to bootstrap.

#. To bootstrap the first node in the cluster run the below command.

   .. code-block:: bash

    systemctl start mysql@bootstrap.service

   .. NOTE:: The mysql service will start during the bootstrap.

   .. NOTE:: Startup failures are commonly caused by misconfigured ``/etc/my.cnf`` files. Also verify ``safe_to_bootstrap`` is set to ``1`` on Node 01 in ``/var/lib/mysql/grastate.dat``.

Configure Morpheus Database and User
````````````````````````````````````

#. Create the Database you will be using with |morpheus|.  Login to mysql on **Node 01**:

   .. code-block:: bash

    [root]# mysql -u root -p
      password: `enter root password`

    mysql> CREATE DATABASE morpheus CHARACTER SET utf8 COLLATE utf8_general_ci;

    mysql> show databases;


#. Next create your |morpheus| database user. This is the user the |morpheus| app nodes will auth with mysql.

   .. code-block:: bash

    mysql> CREATE USER 'morpheusDbUser'@'%' IDENTIFIED BY 'morpheusDbUserPassword';

#. Next Grant your new |morpheus| user permissions.

   .. code-block:: bash

    mysql> GRANT ALL PRIVILEGES ON *.* TO 'morpheusDbUser'@'%' IDENTIFIED BY 'morpheusDbUserPassword';

    mysql> FLUSH PRIVILEGES;

   .. important:: If you grant privileges to the morpheusDbUser to only the morpheus database, you will also need to GRANT SELECT, PROCESS, SHOW DATABASES, SUPER ON PRIVILEGES to the morpheusDbUser on *.* for the Appliance Health service.

    mysql> exit

Copy SSL Files to other nodes
`````````````````````````````

During initialization of **Node 01** the required `pem` files will be generated in ``/var/lib/mysql``. The ``ca.pem``, ``server-cert.pem`` and ``server-key.pem`` files need to match on all nodes in the cluster.

#. Copy the following files from **Node 01** to the same path (default is /var/lib/mysql) on **Node 02** and **Node 03**:

   From **Node 01**
   
   .. code-block:: bash

    [root]# scp /var/lib/mysql/ca.pem root@192.168.101.02:/root
    [root]# scp /var/lib/mysql/server-cert.pem root@192.168.101.02:/root
    [root]# scp /var/lib/mysql/server-key.pem root@192.168.101.02:/root

    [root]# scp /var/lib/mysql/ca.pem root@192.168.101.03:/root
    [root]# scp /var/lib/mysql/server-cert.pem root@192.168.101.03:/root
    [root]# scp /var/lib/mysql/server-key.pem root@192.168.101.03:/root

   From **Node 02** and **Node 03**
   
   .. code-block:: bash
   
    [root]# cp /root/ca.pem /var/lib/mysql/
    [root]# cp /root/server-cert.pem /var/lib/mysql/
    [root]# cp /root/server-key.pem /var/lib/mysql/

   .. important:: Ensure all 3 files match on all 3 nodes, including path, owner and permissions.

   .. note:: The generated certificate is self-signed. Consult Percona documentation for [mysqld] and SSL file configuration when providing your own.

Start the Remaining Nodes
`````````````````````````

#. Start mysql on **Node 02** and **Node 03**

   .. code-block:: bash

    [root]# systemctl start mysql

   The services will automatically join the cluster using the sstuser we created earlier.

   .. NOTE:: Startup failures are commonly caused by misconfigured /etc/my.cnf files.


Verify Configuration
````````````````````

#. Verify SELinux is not rejecting any db cluster communication by running the below on all db nodes:

   .. code-block:: bash

    [root@allDbNodes]# grep -i denied /var/log/audit/audit.log | grep mysqld_t

   If there are any results, address the source or update the SELinux Policy to resolve.

#. Update SELinux if necessary

   .. code-block:: bash

    [root@allDbNodes]# rm -f PXC.*
    [root@allDbNodes]# grep -i denied /var/log/audit/audit.log | grep mysqld_t | audit2allow -M PXC
    [root@allDbNodes]# semodule -i PXC.pp


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
