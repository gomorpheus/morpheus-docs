3 Node Embedded MySQL InnoDB Cluster 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The purpose of this document is to provide the steps to cluster the AIO embedded MySQL 8 
with InnoDB Cluster.

#. Install Morpheus AIO with normal steps.

#. Edit morpheus.rb file and add the following lines. This will set MySQL to listen 
   on its external interface and set the connection to the mysl router using jdbc.

    .. code-block:: bash

        mysql['host'] = '0.0.0.0'
        mysql['mysql_url_overide'] = 'jdbc:mysql://127.0.0.1:6446/morpheus'

#. Reconfigure Morpheus

    .. code-block:: bash

        morpheus-ctl reconfigure


#. Stop morpheus-ui. Now that MySQL is listining on the external address we can cluster the DB.
    
    .. code-block:: bash
        
        morpheus-ctl stop morpheus-ui

#. Modify the Chef Recipe to remove MySQL tasks that use localhost. If this is not removed then
   on reconfgiure it will error out.

    .. code-block:: bash
        
        vi /opt/morpheus/embedded/cookbooks/morpheus-solo/recipes/mysql.rb

    Remove the following 5 tasks. These should be the last 5 items in the recipe.
    mysql_connection_info
    mysql_database node
    mysql_database_user node
    mysql_database_user node
    mysql_database_user node

#. Copy the MySQL credentials section from node 1 to the rest of the nodes.
    Save the root password you will need this in a later step.

    .. code-block:: bash

        vi /etc/morpheus/morpheus-secrets.json

#. Reconfigure Morpheus

    .. code-block:: bash

        morpheus-ctl reconfigure

#. Configure MySQL on Each DB Node.
     
    * This will configure MySQL with some basic hardening along with setting the root password and creating a clusterAdmin account.
      Make sure to set the variables to the desired values before running.
      The clusterAdmin account is used to create all the clustering from MySQL Shell. 
      Setting the invisible primary is required to support Morpheus tables that do not have primary keys.

         .. code-block:: bash

            mysqlrootpass="P@ssw0rd!"
            clusterAdminUser="clusterAdmin"
            clusterAdminPass="P@ssw0rd!"
            /opt/morpheus/embedded/mysql/bin/mysql -h 127.0.0.1 --user=root --password="${mysqlrootpass}" <<_EOF_
            DELETE FROM mysql.user WHERE User='';
            DROP DATABASE IF EXISTS morpheus;
            set persist sql_generate_invisible_primary_key=1;
            CREATE USER '${clusterAdminUser}'@'%' IDENTIFIED BY '${clusterAdminPass}';
            GRANT ALL PRIVILEGES ON *.* TO '${clusterAdminUser}'@'%' with grant option;
            FLUSH PRIVILEGES;
            _EOF_

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
        
        .. code-block:: bash

           dba.checkInstanceConfiguration('clusterAdmin@dba-1:3306')

    * If the return shows required changed run the following command to set the changes. (This should be run against all DB nodes)   
        
        .. code-block:: bash

           dba.configureInstance('clusterAdmin@dba-1:3306')

    * Run the Configure Instance again to confirm they are all set with  no changes.
        
        .. code-block:: bash

           dba.configureInstance('clusterAdmin@dba-1:3306')

    * Connect to one of the DB nodes at the primary site.
        
        .. code-block:: bash

           \c clusterAdmin@dba-1:3306

    * Create the Primary Cluster. (In this example "A" will be the Cluster name)
        
        .. code-block:: bash

           cluster = dba.createCluster("A")

    * Add additional nodes to this cluster. (This should be the nodes at the same site) (Accept the default to Clone)
        
        .. code-block:: bash

           cluster.addInstance("dba-2:3306")
           cluster.addInstance("dba-3:3306")

#. Install MySQL Router

    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                wget https://dev.mysql.com/get/Downloads/MySQL-Router/mysql-router-community_8.0.34-1ubuntu22.04_amd64.deb
                dpkg -i mysql-router-community_8.0.34-1ubuntu22.04_amd64.deb
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash

                wget https://dev.mysql.com/get/Downloads/MySQL-Router/mysql-router-community-8.0.34-1.el9.x86_64.rpm
                rpm -i mysql-router-community-8.0.34-1.el9.x86_64.rpm

#. Configure MySQL Router

    #. Bootstrap the cluster. (This will pull the config from the cluster and create a MySQL Router config file.)
     
        .. code-block:: bash

           mysqlrouter --bootstrap clusterAdmin@adb-5:3306 --account routeruser --user=mysqlrouter --name=morpha
           systemctl restart mysqlrouter

        You should get back a number of ports available to connect to.
        
        .. code-block:: bash

            ## MySQL Classic protocol

            Read/Write Connections: localhost:6446
            Read/Only Connections:  localhost:6447

            ## MySQL X protocol

            Read/Write Connections: localhost:6448
            Read/Only Connections:  localhost:6449

      #. Restart mysqlrouter service.
     
        .. code-block:: bash

           systemctl restart mysqlrouter

    #. To confirm if MySQL Router is listening on the ports you can run.
     
        .. code-block:: bash

           sudo lsof -i -P -n | grep LISTEN|grep mysqlrout

#. Restart Morphues UI on the first node and confirm it come up without issue.
 
    .. code-block:: bash

        morpheus-ctl restart morpheus-ui
        morpheus-ctl tail morpheus-ui

#. Once first node is complete proceed to the other 2 nodes
 
    .. code-block:: bash

        morpheus-ctl restart morpheus-ui
        morpheus-ctl tail morpheus-ui
