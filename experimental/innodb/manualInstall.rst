Manual Install Steps
====================

.. Manual-Section-Start

The purpose of this document is to provide end to end manual steps to prepare and configure an
InnoDB single site cluster.

#. Disable AppArmor/SELinux.

    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                systemctl stop apparmor
                systemctl disable apparmor
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash
                
                setenforce 0
                sed -i 's/^SELINUX=.*/SELINUX=permissive/g' /etc/selinux/config && cat /etc/selinux/config
                sestatus


#. Disable/Add Firewall Rules.
    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                #Firewall should be disabled by default.
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash
                
                # To stop and disable FW
                systemctl stop firewalld
                systemctl disable firewalld

                # To add public FW rules for MySQL InnoDB Cluster
                firewall-cmd --zone=public --add-port=3306/tcp
                firewall-cmd --permanent --zone=public --add-port=3306/tcp
                firewall-cmd --zone=public --add-port=33060/tcp
                firewall-cmd --permanent --zone=public --add-port=33060/tcp
                firewall-cmd --zone=public --add-port=33061/tcp
                firewall-cmd --permanent --zone=public --add-port=33061/tcp
                firewall-cmd --zone=public --add-port=33062/tcp
                firewall-cmd --permanent --zone=public --add-port=33062/tcp
                
#. Install MySQL on Each DB Node.

    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                apt update
                apt install mysql-server
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash

                dnf install mysql-server
                systemctl start mysqld.service
                systemctl enable mysqld.service
                
                

#. Configure MySQL on Each DB Node.
     
    * This will configure MySQL with some basic hardening along with setting the root password and creating a clusterAdmin account.
      Make sure to set the variables to the desired values before running.
      The clusterAdmin account is used to create all the clustering from MySQL Shell. 
      Setting the invisible primary is required to support Morpheus tables that do not have primary keys.

         .. code-block:: bash

            mysqlrootpass="P@ssw0rd!"
            clusterAdminUser="clusterAdmin"
            clusterAdminPass="P@ssw0rd!"
            mysql --user=root <<_EOF_
            DELETE FROM mysql.user WHERE User='';
            DROP DATABASE IF EXISTS test;
            DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
            set persist sql_generate_invisible_primary_key=1;
            ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '${mysqlrootpass}';
            CREATE USER '${clusterAdminUser}'@'%' IDENTIFIED BY '${clusterAdminPass}';
            GRANT ALL PRIVILEGES ON *.* TO '${clusterAdminUser}'@'%' with grant option;
            FLUSH PRIVILEGES;
            _EOF_
    
    

    * Check the global MySQL properties to confirm invisible primary key is on.     
        
        .. code-block:: 

           mysql> SHOW GLOBAL VARIABLES LIKE 'sql_generate_invisible_primary_key';

    * Update the MySQL config to listen on external address.    
        
        .. tabs::

            .. group-tab:: Ubuntu 22.04

                .. code-block:: bash
                    
                    # This should set the bind-address in a single command.
                    sed -i '/^bind-address\s*=/ {s/=.*/= 0.0.0.0/; h;}; $ {x;/^$/{s//bind-address = 0.0.0.0/;H};x}' /etc/mysql/mysql.conf.d/mysqld.cnf
                    
                    # This is where the config file is to confirm or set manually.
                    vi /etc/mysql/mysql.conf.d/mysqld.cnf
                    
                **change bind-address = 0.0.0.0**
                        
            .. group-tab:: RHEL 8/9

                .. code-block:: bash
                    
                    # This should set the bind-address in a single command.
                    sed -i '/^bind-address\s*=/ {s/=.*/= 0.0.0.0/; h;}; $ {x;/^$/{s//bind-address = 0.0.0.0/;H};x}' /etc/my.cnf.d/mysql-server.cnf
                    
                    # This is where the config file is to confirm or set manually.
                    vi /etc/my.cnf.d/mysql-server.cnf
                    
                **add  bind-address  = 0.0.0.0**


        
    * Restart mysql service.    
        
        .. tabs::

            .. group-tab:: Ubuntu 22.04

                .. code-block:: bash
        
                    systemctl restart mysql.service
                    
                        
            .. group-tab:: RHEL 8/9

                .. code-block:: bash

                    systemctl restart mysqld.service

    .. note:: You need to make sure that all nodes can reach each other by short name.  You can also use IPs or FQDN, as long as they match how they are configured below.            

.. Manual-Section-Stop

#. Install MySQL Shell. (This does not have to be installed on the DB nodes. In prod it would probably be installed on each Morpheus app node)



        .. tabs::

            .. group-tab:: Ubuntu 22.04

                .. code-block:: bash
        
                    wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell_8.0.34-1ubuntu22.04_amd64.deb
                    dpkg -i mysql-shell_8.0.34-1ubuntu22.04_amd64.deb
                        
            .. group-tab:: RHEL 8/9
                
                .. code-block:: bash

                    wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell-8.0.34-1.el9.x86_64.rpm
                    rpm -i mysql-shell-8.0.34-1.el9.x86_64.rpm



#. Setup Cluster using MySQL Shell (clusterAdmin is the admin user we created, dba-1 is one of the DB Nodes)
    * Start MySQL Shell.    
        
        .. code-block:: bash

           mysqlsh

    * Check if the DB nodes are ready for cluster configuration. (This should be run against all DB nodes)      
        
        .. code-block:: js

           dba.checkInstanceConfiguration('clusterAdmin@dba-1:3306')

    * If the return shows required changed run the following command to set the changes. (This should be run against all DB nodes)   
        
        .. code-block:: js

           dba.configureInstance('clusterAdmin@dba-1:3306')

    * Run the Configure Instance again to confirm they are all set with  no changes.
        
        .. code-block:: js

           dba.configureInstance('clusterAdmin@dba-1:3306')

    * Connect to one of the DB nodes at the primary site.
        
        .. code-block:: 

           \c clusterAdmin@dba-1:3306

    * Create the Primary Cluster. (In this example "A" will be the Cluster name)
        
        .. code-block:: js

           cluster = dba.createCluster("A")

    * Add additional nodes to this cluster. (This should be the nodes at the same site) (Accept the default to Clone)
        
        .. code-block:: js

           cluster.addInstance("dba-2:3306")
           cluster.addInstance("dba-3:3306")

    
    * Validate the Cluster is created.
        
        .. code-block:: js

           cluster.status()



MultiSite Full Install 
^^^^^^^^^^^^^^^^^^^^^^

#. Install MySQL Shell. (This does not have to be installed on the DB nodes. In prod it would probably be installed on each Morpheus app node)

        .. tabs::

            .. group-tab:: Ubuntu 22.04

                .. code-block:: bash
        
                    wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell_8.0.34-1ubuntu22.04_amd64.deb
                    dpkg -i mysql-shell_8.0.34-1ubuntu22.04_amd64.deb
                        
            .. group-tab:: RHEL 8/9
                
                .. code-block:: bash

                    wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell-8.0.34-1.el9.x86_64.rpm
                    rpm -i mysql-shell-8.0.34-1.el9.x86_64.rpm

#. Setup Cluster using MySQL Shell (clusterAdmin is the admin user we created, dba-1 is one of the DB Nodes)
    * Start MySQL Shell.    
        
        .. code-block:: bash

           mysqlsh

    * Check if the DB nodes are ready for cluster configuration. (This should be run against all DB nodes)      
        
        .. code-block:: js

           dba.checkInstanceConfiguration('clusterAdmin@dba-1:3306')

    * If the return shows required changed run the following command to set the changes. (This should be run against all DB nodes)   
        
        .. code-block:: js

           dba.configureInstance('clusterAdmin@dba-1:3306')

    * Run the Configure Instance again to confirm they are all set with  no changes.
        
        .. code-block:: js

           dba.configureInstance('clusterAdmin@dba-1:3306')

    * Connect to one of the DB nodes at the primary site.
        
        .. code-block:: 

           \c clusterAdmin@dba-1:3306

    * Create the Primary Cluster. (In this example "A" will be the Cluster name)
        
        .. code-block:: js

           cluster = dba.createCluster("A")

    * Add additional nodes to this cluster. (This should be the nodes at the same site) (Accept the default to Clone)
        
        .. code-block:: js

           cluster.addInstance("dba-2:3306")
           cluster.addInstance("dba-3:3306")

    * Create the Cluster Set (This will be what Links the Primary Cluster built above with Replica Clusters. You can create multiple Replica Clusters in the Cluster Set.)
        
        .. code-block:: js

           clusterset = cluster.createClusterSet("ClusterSet")
        
        “ClusterSet” can be set to any value, and will be the name of your Cluster Set.
    
    * Validate the Cluster Set is created.
        
        .. code-block:: js

           clusterset.status()
    
    * Create Replica Cluster (This will be an additional Site) Original site was called “A” above we will set this one as “B”
        
        .. code-block:: js

           clusterb = clusterset.createReplicaCluster("dbb-1:3306", "B")

        dbb-1 is a DB node in the secondary site

    * Add additional Nodes to the replica
        
        .. code-block:: js

           clusterb.addInstance("dbb-2:3306")
           clusterb.addInstance("dbb-3:3306")
    
    * Validate Cluster Set
        
        .. code-block:: js

           clusterset.status()

    


        


         

    


    

    



                
