.. _3nodeinstall-al2:

3-Node HA Install (Amazon Linux 2)
---------------------------------

Distributed App Nodes with Externalized DB

.. include:: /installation/app/3-node-ha/assumptions.rst

.. include:: /installation/app/default-locations.rst

.. include::   /installation/database/aurora/aurora-5.7.rst

.. include:: /installation/app/3-node-ha/app-node-installation-al2.rst

.. include:: /installation/app/3-node-ha/clustering-rabbitmq.rst

.. include:: /installation/load_balancer/ha_load_balancer.rst

.. include:: /installation/storage/HA_Shared_Storage.rst

.. include:: /installation/app/database-migration.rst

.. include:: /installation/app/recovery.rst

WIP

Security Group
2 x M5 Large - 2CPU, 8GB

elastic fix
wget 
rpm -ihv /home/kgawronski/morpheus-appliance-5.4.15-1.amzn2.x86_64.rpm
nano /etc/morpheus/morpheus.rb
    appliance_url 'https://morpheus.localdomain'
    elasticsearch['es_hosts'] = {'10.0.2.222' => 9200, '10.0.2.219' => 9200, '10.0.2.151' => 9200}
    elasticsearch['node_name'] = '10.0.2.222'
    elasticsearch['host'] = '0.0.0.0'
    rabbitmq['host'] = '0.0.0.0'
    rabbitmq['nodename'] = 'rabbit@node01'
    mysql['enable'] = false
    mysql['host'] = 'morpheus-cluster.cluster-cgguv6wqc1al.us-east-2.rds.amazonaws.com'
    mysql['morpheus_db'] = 'morpheus'
    mysql['morpheus_db_user'] = 'morpheusDbUser'
    mysql['morpheus_password'] = 'morpheusDbUserPassword'
nano /etc/hosts
    10.0.2.222 node01
    10.0.2.219 node02
    10.0.2.151 node03
yum install libatomic
/opt/morpheus/embedded/bin/mysql -h 'database-1.cluster-cgguv6wqc1al.us-east-2.rds.amazonaws.com' -u admin -p
morpheus-ctl reconfigure
morpheus-ctl tail morpheus-ui