Database Tier Configuraiton
----------------------------------

Installation and configuraiton of Percona XtraDB Cluster on CentOS/RHEL 7

.. IMPORTANT:: This is a sample configuraiton only. Customer configuraitons and requirements will vary.

Requirements
^^^^^^^^^^^^

Percona requires the following ports for the cluster nodes. Please create the appropriate firewall rules on your
Percona nodes.

- 3306
- 4444
- 4567
- 4568

Percona also recommends setting the selinux policy to permissive. You can temporarily set the permission to permissive by running

.. code-block:: bash

  sudo setenforce 0

You will need to edit the selinux configuration file if you want the permission to take affect permanently which can be found in ``/etc/selinux/config``

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
    sudo yum update -y

Installing Percona XtraDB Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. The below command will install the Percona XtraDB Cluster software and it’s dependences.

   .. code-block:: bash

    sudo yum install Percona-XtraDB-Cluster-57

    NOTE:: During the installation you will receive the below message. Accept the Percona PGP key to install the software.

    retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Percona
    Importing GPG key 0xCD2EFD2A:
    Userid     : "Percona MySQL Development Team <mysql-dev@percona.com>"
    Fingerprint: 430b df5c 56e7 c94e 848e e60c 1c4c bdcd cd2e fd2a
    Package    : percona-release-0.1-4.noarch (installed)
    From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-Percona
    Is this ok [y/N]: y


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

    ALTER USER 'root'@'localhost' IDENTIFIED BY 'MySuperSecurePasswordhere';

#. Create the sstuser user and grant the permissions.

   .. code-block:: bash

    mysql> CREATE USER 'sstuser'@'localhost' IDENTIFIED BY 'M0rpheus17';

   .. NOTE:: The sstuser and password will be used in the /etc/my.cnf configuration.

   .. code-block:: bash

    mysql> GRANT RELOAD, LOCK TABLES, PROCESS, REPLICATION CLIENT ON *.* TO 'sstuser'@'localhost';

    mysql> FLUSH PRIVILEGES;

#. Exit mysql then stop the mysql services:

   .. code-block:: bash

    mysql> exit
    Bye
    $ sudo systemctl stop mysql.service

#. Now install the Percona software on to the other nodes using the same steps.

Once the service is stopped on all nodes move onto the next step.

Add [mysqld] to my.cnf in /etc/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Copy the below contents to ``/etc/my.cnf``.  The node_name and node_address needs to be unique on each of the nodes. The first node does not require the gcomm value to be set.

   .. code-block:: bash

      $ sudo vi /etc/my.cnf

   .. code-block:: bash

      [mysqld]
      wsrep_provider=/usr/lib64/galera3/libgalera_smm.so

      wsrep_cluster_name=popeye
      wsrep_cluster_address=gcomm://  #Leave blank for Master Node. The other nodes require this field. Enter the IP address of the primary node first then remaining nodes. Separating the ip addresses with commas like this 10.30.20.196,10.30.20.197,10.30.20.198##

      wsrep_node_name=morpheus-node01
      wsrep_node_address=10.30.20.57

      wsrep_sst_method=xtrabackup-v2
      wsrep_sst_auth=sstuser:M0rpheus17
      pxc_strict_mode=PERMISSIVE

      binlog_format=ROW
      default_storage_engine=InnoDB
      innodb_autoinc_lock_mode=2

#. Save ``/etc/my.cnf``

Bootstrapping the first Node in the cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. IMPORTANT:: Ensure mysql.service is stopped prior to bootstrap.

#. To bootstrap the first node in the cluster run the below command.

   .. code-block:: bash

    systemctl start mysql@bootstrap.service

   .. NOTE:: The mysql service will start during the boot strap.

#. To verify the bootstrap, on the master node login to mysql and run ``show status like 'wsrep%';``

   .. code-block:: bash

      # mysql -u root -p

         mysql>  show status like 'wsrep%';
         +----------------------------------+--------------------------------------+
         | Variable_name                    | Value                                |
         +----------------------------------+--------------------------------------+
         | wsrep_local_state_uuid           | 591179cb-a98e-11e7-b9aa-07df8a228fe9 |
         | wsrep_protocol_version           | 7                                    |
         | wsrep_last_committed             | 1                                    |
         | wsrep_replicated                 | 0                                    |
         | wsrep_replicated_bytes           | 0                                    |
         | wsrep_repl_keys                  | 0                                    |
         | wsrep_repl_keys_bytes            | 0                                    |
         | wsrep_repl_data_bytes            | 0                                    |
         | wsrep_repl_other_bytes           | 0                                    |
         | wsrep_received                   | 2                                    |
         | wsrep_received_bytes             | 141                                  |
         | wsrep_local_commits              | 0                                    |
         | wsrep_local_cert_failures        | 0                                    |
         | wsrep_local_replays              | 0                                    |
         | wsrep_local_send_queue           | 0                                    |
         | wsrep_local_send_queue_max       | 1                                    |
         | wsrep_local_send_queue_min       | 0                                    |
         | wsrep_local_send_queue_avg       | 0.000000                             |
         | wsrep_local_recv_queue           | 0                                    |
         | wsrep_local_recv_queue_max       | 2                                    |
         | wsrep_local_recv_queue_min       | 0                                    |
         | wsrep_local_recv_queue_avg       | 0.500000                             |
         | wsrep_local_cached_downto        | 0                                    |
         | wsrep_flow_control_paused_ns     | 0                                    |
         | wsrep_flow_control_paused        | 0.000000                             |
         | wsrep_flow_control_sent          | 0                                    |
         | wsrep_flow_control_recv          | 0                                    |
         | wsrep_flow_control_interval      | [ 100, 100 ]                         |
         | wsrep_flow_control_interval_low  | 100                                  |
         | wsrep_flow_control_interval_high | 100                                  |
         | wsrep_flow_control_status        | OFF                                  |
         | wsrep_cert_deps_distance         | 0.000000                             |
         | wsrep_apply_oooe                 | 0.000000                             |
         | wsrep_apply_oool                 | 0.000000                             |
         | wsrep_apply_window               | 0.000000                             |
         | wsrep_commit_oooe                | 0.000000                             |
         | wsrep_commit_oool                | 0.000000                             |
         | wsrep_commit_window              | 0.000000                             |
         | wsrep_local_state                | 4                                    |
         | wsrep_local_state_comment        | Synced                               |
         | wsrep_cert_index_size            | 0                                    |
         | wsrep_cert_bucket_count          | 22                                   |
         | wsrep_gcache_pool_size           | 1320                                 |
         | wsrep_causal_reads               | 0                                    |
         | wsrep_cert_interval              | 0.000000                             |
         | wsrep_ist_receive_status         |                                      |
         | wsrep_ist_receive_seqno_start    | 0                                    |
         | wsrep_ist_receive_seqno_current  | 0                                    |
         | wsrep_ist_receive_seqno_end      | 0                                    |
         | wsrep_incoming_addresses         | 10.30.20.196:3306                    |
         | wsrep_desync_count               | 0                                    |
         | wsrep_evs_delayed                |                                      |
         | wsrep_evs_evict_list             |                                      |
         | wsrep_evs_repl_latency           | 0/0/0/0/0                            |
         | wsrep_evs_state                  | OPERATIONAL                          |
         | wsrep_gcomm_uuid                 | 07c8c8fe-a998-11e7-883e-06949cfe5af3 |
         | wsrep_cluster_conf_id            | 1                                    |
         | wsrep_cluster_size               | 1                                    |
         | wsrep_cluster_state_uuid         | 591179cb-a98e-11e7-b9aa-07df8a228fe9 |
         | wsrep_cluster_status             | Primary                              |
         | wsrep_connected                  | ON                                   |
         | wsrep_local_bf_aborts            | 0                                    |
         | wsrep_local_index                | 0                                    |
         | wsrep_provider_name              | Galera                               |
         | wsrep_provider_vendor            | Codership Oy <info@codership.com>    |
         | wsrep_provider_version           | 3.22(r8678538)                       |
         | wsrep_ready                      | ON                                   |
         +----------------------------------+--------------------------------------+
          67 rows in set (0.01 sec)

   A table will appear with the status and rows.


#. Next Create the Database you will be using with morpheus.

   .. code-block:: bash

    mysql> CREATE DATABASE morpheusdb;

    mysql> show databases;


#. Next create your morpheus database user. The user needs to be either at the IP address of the morpheus application server or use @'%' within the user name to allow the user to login from anywhere.

   .. code-block:: bash

    mysql> CREATE USER 'morpheusadmin'@'%' IDENTIFIED BY 'Cloudy2017';

#. Next Grant your new morpheus user permissions to the database.

   .. code-block:: bash

    mysql> GRANT ALL PRIVILEGES ON * . * TO 'morpheusadmin'@''%' IDENTIFIED BY 'Cloudy2017' with grant option;


    mysql> FLUSH PRIVILEGES;

#. Checking Permissions for your user.

   .. code-block:: bash

    SHOW GRANTS FOR 'morpheusadmin'@''%'';


Bootstrap the Remaining Nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. To bootstrap the remaining nodes into the cluster run the following command on each node:

   .. code-block:: bash

    sudo systemctl start mysql.service

   The services will automatically connect to the cluster using the sstuser we created earlier.

   .. NOTE:: Bootstrap failures are commonly caused by misconfigured /etc/my.cnf files.

Verification
^^^^^^^^^^^^

#. To verify the cluster, on the master login to mysql and run ``show status like 'wsrep%';``

   .. code-block:: bash

     $ mysql -u root -p

      mysql>  show status like 'wsrep%';

     +----------------------------------+-------------------------------------------------------+
      | Variable_name                    | Value                                                 |
      +----------------------------------+-------------------------------------------------------+
      | wsrep_local_state_uuid           | 591179cb-a98e-11e7-b9aa-07df8a228fe9                  |
      | wsrep_protocol_version           | 7                                                     |
      | wsrep_last_committed             | 4                                                     |
      | wsrep_replicated                 | 3                                                     |
      | wsrep_replicated_bytes           | 711                                                   |
      | wsrep_repl_keys                  | 3                                                     |
      | wsrep_repl_keys_bytes            | 93                                                    |
      | wsrep_repl_data_bytes            | 426                                                   |
      | wsrep_repl_other_bytes           | 0                                                     |
      | wsrep_received                   | 10                                                    |
      | wsrep_received_bytes             | 774                                                   |
      | wsrep_local_commits              | 0                                                     |
      | wsrep_local_cert_failures        | 0                                                     |
      | wsrep_local_replays              | 0                                                     |
      | wsrep_local_send_queue           | 0                                                     |
      | wsrep_local_send_queue_max       | 1                                                     |
      | wsrep_local_send_queue_min       | 0                                                     |
      | wsrep_local_send_queue_avg       | 0.000000                                              |
      | wsrep_local_recv_queue           | 0                                                     |
      | wsrep_local_recv_queue_max       | 2                                                     |
      | wsrep_local_recv_queue_min       | 0                                                     |
      | wsrep_local_recv_queue_avg       | 0.100000                                              |
      | wsrep_local_cached_downto        | 2                                                     |
      | wsrep_flow_control_paused_ns     | 0                                                     |
      | wsrep_flow_control_paused        | 0.000000                                              |
      | wsrep_flow_control_sent          | 0                                                     |
      | wsrep_flow_control_recv          | 0                                                     |
      | wsrep_flow_control_interval      | [ 173, 173 ]                                          |
      | wsrep_flow_control_interval_low  | 173                                                   |
      | wsrep_flow_control_interval_high | 173                                                   |
      | wsrep_flow_control_status        | OFF                                                   |
      | wsrep_cert_deps_distance         | 1.000000                                              |
      | wsrep_apply_oooe                 | 0.000000                                              |
      | wsrep_apply_oool                 | 0.000000                                              |
      | wsrep_apply_window               | 1.000000                                              |
      | wsrep_commit_oooe                | 0.000000                                              |
      | wsrep_commit_oool                | 0.000000                                              |
      | wsrep_commit_window              | 1.000000                                              |
      | wsrep_local_state                | 4                                                     |
      | wsrep_local_state_comment        | Synced                                                |
      | wsrep_cert_index_size            | 1                                                     |
      | wsrep_cert_bucket_count          | 22                                                    |
      | wsrep_gcache_pool_size           | 2413                                                  |
      | wsrep_causal_reads               | 0                                                     |
      | wsrep_cert_interval              | 0.000000                                              |
      | wsrep_ist_receive_status         |                                                       |
      | wsrep_ist_receive_seqno_start    | 0                                                     |
      | wsrep_ist_receive_seqno_current  | 0                                                     |
      | wsrep_ist_receive_seqno_end      | 0                                                     |
      | wsrep_incoming_addresses         | 10.30.20.196:3306,10.30.20.197:3306,10.30.20.198:3306 |
      | wsrep_desync_count               | 0                                                     |
      | wsrep_evs_delayed                |                                                       |
      | wsrep_evs_evict_list             |                                                       |
      | wsrep_evs_repl_latency           | 0/0/0/0/0                                             |
      | wsrep_evs_state                  | OPERATIONAL                                           |
      | wsrep_gcomm_uuid                 | 07c8c8fe-a998-11e7-883e-06949cfe5af3                  |
      | wsrep_cluster_conf_id            | 3                                                     |
      | wsrep_cluster_size               | 3                                                     |
      | wsrep_cluster_state_uuid         | 591179cb-a98e-11e7-b9aa-07df8a228fe9                  |
      | wsrep_cluster_status             | Primary                                               |
      | wsrep_connected                  | ON                                                    |
      | wsrep_local_bf_aborts            | 0                                                     |
      | wsrep_local_index                | 1                                                     |
      | wsrep_provider_name              | Galera                                                |
      | wsrep_provider_vendor            | Codership Oy <info@codership.com>                     |
      | wsrep_provider_version           | 3.22(r8678538)                                        |
      | wsrep_ready                      | ON                                                    |
      +----------------------------------+-------------------------------------------------------+


#. Verify that you can login to the MSQL server by running the below command on the Morpheus Application server(s).

   .. code-block:: bash

    mysql -u morpheusadmin -p  -h 192.168.10.100

   .. NOTE:: This command requires mysql client installed. If you are on a windows machine you can connect to the server using mysql work bench which can be found here https://www.mysql.com/products/workbench/
