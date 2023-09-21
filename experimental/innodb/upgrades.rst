InnoDB Cluster Upgrades 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Single Site Cluster Upgrade
```````````````````````````
    Upgrade Order
    
    * MySQl Router
    * MySQL Shell
    * MySQl Server


MySQL Server Upgrade
====================

#. Get the current cluster status. This can be done from any VM that has MySQL Shell installed. 
   (typically the Morpheus App Nodes)

    .. code-block:: bash

        mysqlsh
        \c clusterAdmin@dba-1:3306
        cluster = dba.getCluster()
        cluster.status()

#. Upgrade one of the secondary servers from the status above.

    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                apt-get install mysql-server
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash
                
                dnf upgrade mysql-server

    * Confirm the the cluster status after upgrade is complete using steps from 1. 
    * Node should show Online and new version. replicationLag should not have any errors

#. Upgrade the other secondary server.
 
    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                apt-get install mysql-server
             
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash
                
                dnf upgrade mysql-server

    * Confirm the the cluster status after upgrade is complete using steps from 1. 
    * Node should show Online and new version. replicationLag should not have any errors

#. Upgrade the primary server.
 
    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                apt-get install mysql-server
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash
                
                dnf upgrade mysql-server

    * Confirm the the cluster status after upgrade is complete using steps from 1. 
    * Node should show Online and new version. replicationLag should not have any errors.

    * Upgrade of the Cluster shoud now be complete. During the upgrade of the primary you should have 
      noticed a few second failover and one of the secondaries should now be primary.