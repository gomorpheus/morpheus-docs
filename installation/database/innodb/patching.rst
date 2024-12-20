InnoDB Cluster Maintenance/Patching 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


MySQL Patching
====================

#. Get the current cluster status. This can be done from any VM that has MySQL Shell installed. 
   (typically the Morpheus App Nodes)

    .. code-block:: js
        :force:

            mysqlsh
            \c clusterAdmin@dba-1:3306
            cluster = dba.getCluster()
            cluster.status()

#. Ensure that all nodes of the cluster are online and each node is not reporting any replication lag.


#. Patch one of the secondary servers from the status above.

    * Stop the mysql service.
    * perform any patching.
    * reboot if needed. 
    * ensure mysql service is running or start mysql service.
    * Check the cluster status. (make sure this node is back online and there is no replication lag.Depending on the number of new writes this may take some time. Continue to check status)    
        
        .. code-block:: js
            :force:

                mysqlsh
                \c clusterAdmin@dba-1:3306
                cluster = dba.getCluster()
                cluster.status()

    * Once the node is confirmed up and good from the cluster status preceed to the next secondary node.

#. Upgrade the other secondary server.
 
    * Stop the mysql service.
    * perform any patching.
    * reboot if needed. 
    * ensure mysql service is running or start mysql service.
    * Check the cluster status. (make sure this node is back online and there is no replication lag.Depending on the number of new writes this may take some time. Continue to check status)    
        
        .. code-block:: js
            :force:

                mysqlsh
                \c clusterAdmin@dba-1:3306
                cluster = dba.getCluster()
                cluster.status()

    * Once the node is confirmed up and good from the cluster status preceed to the primary node.

#. Upgrade the primary server.
 
    * failover over primary to one of the secondary nodes.
         
         .. code-block:: js
            :force:

            mysqlsh 
            \c clusterAdmin@dba-1:3306
            cluster = dba.getCluster()
            cluster.setPrimaryInstance("dba-2:3306") 
            cluster.status()

    * Check the cluster status. (Make sure that this node is now a secondary and your other node is primary)    
        
        .. code-block:: js
            :force:

                mysqlsh
                \c clusterAdmin@dba-1:3306
                cluster = dba.getCluster()
                cluster.status()

    * Stop the mysql service.
    * Perform any patching.
    * Reboot if needed. 
    * Ensure mysql service is running or start mysql service.
    * Check the cluster status. (make sure this node is back online and there is no replication lag.Depending on the number of new writes this may take some time. Continue to check status)    
        
        .. code-block:: js
            :force:

                mysqlsh
                \c clusterAdmin@dba-1:3306
                cluster = dba.getCluster()
                cluster.status()

    * Once the cluster is confirmed up and in sync the patching is compete.