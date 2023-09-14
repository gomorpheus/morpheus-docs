MySQL Shell
^^^^^^^^^^^^^^^^^^

Introduction
````````````

MySQl Shell is an advanced client and code editor for MySQL. In addition to the provided 
SQL functionality, MySQL Shell provides scripting capabilities for JavaScript and Python 
and includes APIs for working with MySQL. X DevAPI enables you to work with both relational 
and document data. AdminAPI enables you to work with InnoDB Cluster, InnoDB ClusterSet, and 
InnoDB ReplicaSet 

Download MySQL Shell from: https://dev.mysql.com/downloads/shell/ 

Official Documentation: https://dev.mysql.com/doc/mysql-shell/8.0/en/

Install MySQL Shell
````````````````````

    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell_8.0.34-1ubuntu23.04_amd64.deb
                dpkg -i mysql-shell_8.0.34-1ubuntu22.04_amd64.deb
                        
        .. group-tab:: RHEL 8/9
                
            .. code-block:: bash
                
                wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell-8.0.34-1.el9.x86_64.rpm
                rpm -i mysql-shell-8.0.34-1.el9.x86_64.rpm

MySQL Shell Commands
^^^^^^^^^^^^^^^^^^^^

MySQL Shell Get Status
```````````````````````
    * Get Cluster Status
        .. code-block:: bash
            
            \c clusterAdmin@dbb-1:3306
            cluster = dba.getCluster()
            cluster.status()
    
    * Get Extended Cluster Status. (This will provide a more detailed return)
        .. code-block:: bash
            
            \c clusterAdmin@dbb-1:3306
            cluster = dba.getCluster({extended: 1})
            cluster.status()
    
    * Get Cluster Set Status.
        .. code-block:: bash
            
            \c clusterAdmin@dbb-1:3306
            clusterset = dba.getClusterSet()
            clusterset.status()
    
    * Get Extended Cluster Set Status. (This will provide a more detailed return)
        .. code-block:: bash
            
            \c clusterAdmin@dbb-1:3306
            clusterset = dba.getClusterSet({extended: 1})
            clusterset.status()
    

MySQL Shell Add/Remove Nodes
````````````````````````````

    * Removing a Node from a Cluster  
        .. code-block:: bash
            
            \c clusterAdmin@dbb-1:3306
            cluster = dba.getCluster()
            cluster.removeInstance('clusterAdmin@dbd-2:3306') 
            cluster.status()

    * Adding a Node to a Cluster 
        .. code-block:: bash
            
            \c clusterAdmin@dbb-1:3306
            cluster = dba.getCluster()
            cluster.addInstance('clusterAdmin@dbd-2:3306')
            cluster.status()

MySQL Shell Running Scripts
````````````````````````````

    * Using a Script 
        .. code-block:: bash
            
            mysqlsh --file myscript.js

MySQL Shell Planned Failover
``````````````````````````````

    * Failover to another Cluster Member at the same site.
        .. code-block:: bash
            
            \c clusterAdmin@dbd-1:3306
            cluster = dba.getCluster()
            cluster.setPrimaryInstance("dbd-2:3306") 
            cluster.status()

    * Failover to another Site.
        .. code-block:: bash
           
            \c clusterAdmin@dbd-1:3306
            cs = dba.getClusterSet()
            cs.setPrimaryCluster("B") 
            cs.status()   
 
 
MySQL Shell Unplanned Disaster Failover
````````````````````````````````````````

    * Recover from all nodes down at a single site
        .. code-block:: bash
            
            mysqlsh
            \c clusterAdmin@dbd-1:3306
            dba.rebootClusterFromCompleteOutage()
    
    * Emergency Failover when a site is down. **This should only be done as a last resort when the primary site cant be brought up** 
      This process will bring up the Cluster at site B. 
      You should take steps to ensure that no writes go to site A if/when it comes back up. This can be done
      by stopping the morpheus-ui and/or fencing the router traffic.
        .. code-block:: bash
            
            mysqlsh
            \c clusterAdmin@dbd-1:3306
            clusterset = dba.getClusterSet()
            clusterset.status()
            clusterset.forcePrimaryCluster("B")
            clusterset.status()

    * Emergency Failover Recovery of down site. 
      Once Power is restored to Site A nodes, you can go through the repair process. 
        .. code-block:: bash
            
            //Connect to site A node to repair cluster from all nodes down.
            mysqlsh 
            \c clusterAdmin@dbd-1:3306
            dba.rebootClusterFromCompleteOutage()
            clusterset = dba.getClusterSet()
            clusterset.rejoinCluster("A")
    
MySQL Shell Router Config
````````````````````````````````````````
 
    * Setting MySQL Router target Cluster. This will force the router to only connect to the cluster specified.
        .. code-block:: bash
            
            mysqlsh 
            \c clusterAdmin@dbd-1:3306
            clusterset = dba.getClusterSet()
            #get the connected router information
            clusterset.routingOptions()
            #Find the router you want to change.
            clusterset.setRoutingOption('morphb.test.local::morphb', 'target_cluster', 'B')
            #confirm the settings
            clusterset.routingOptions()
           
    
        