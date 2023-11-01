.. _Percona TLS RHEL Verify:

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