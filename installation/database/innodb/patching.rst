InnoDB Cluster Maintenance/Patching 
===================================

#. Get the current cluster status. This can be done from any VM that has MySQL Shell installed. 
   (typically the Morpheus App Nodes)

    .. important::
        if multi-site then always start at the secondary site nodes first before the primary site.
    
    .. code-block:: js
        :force:

            mysqlsh
            \c clusterAdmin@dba-1:3306
            cluster = dba.getCluster()
            cluster.status()

#. Ensure that all nodes of the cluster are online and each node is not reporting any replication lag.


#. Patch each of the secondary servers from the status above. 

    .. important::
        make sure to only do one at a time following this process before continuing.


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

    * Once the node is confirmed up and good from the cluster status preceed to the next secondary node.



#. Patch the primary server.
 
    * Fail over primary node to one of the patched secondary nodes.
         
         .. code-block:: js
            :force:

            mysqlsh 
            \c clusterAdmin@dba-1:3306
            cluster = dba.getCluster()
            cluster.setPrimaryInstance("dba-2:3306") 
            cluster.status()

    * Check the cluster status. 
    
        .. important::
            Make sure that this node is now a secondary and your other node is primary before continuing.    
        
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
    * Check the cluster status. 
        
        .. important::
            Make sure this node is back online and there is no replication lag. Depending on the number of new writes this may take some time. Continue to check status.
        
        .. code-block:: js
            :force:

                mysqlsh
                \c clusterAdmin@dba-1:3306
                cluster = dba.getCluster()
                cluster.status()

    * Once the cluster is confirmed up and in sync the patching is compete.