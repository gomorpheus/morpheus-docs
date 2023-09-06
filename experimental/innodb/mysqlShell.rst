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

Install MySQL Shell
````````````````````

    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell_8.0.34-1ubuntu23.04_amd64.deb
                dpkg -i mysql-shell_8.0.34-1ubuntu22.04_amd64.deb
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash
                
MySQL Shell Commands
````````````````````
    * Failover to another Cluster Member at the same site.
        .. code-block:: bash
            
            \c clusterAdmin@dbb-1:3306
            cluster = dba.getCluster()
            cluster.setPrimaryInstance("bdb-2:3306") 
            cluster.status()

    * Failover to another Site.
        .. code-block:: bash
           
            \c clusterAdmin@dbb-1:3306
            cs = dba.getClusterSet()
            cs.setPrimaryCluster("B") 
            cs.status()   

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
        
    * Using a Script 
        .. code-block:: bash
            
            mysqlsh --file myscript.js
