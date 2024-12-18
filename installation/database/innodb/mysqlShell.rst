MySQL Shell
============

Introduction
^^^^^^^^^^^^

MySQl Shell is an advanced client and code editor for MySQL. In addition to the provided 
SQL functionality, MySQL Shell provides scripting capabilities for JavaScript and Python 
and includes APIs for working with MySQL. X DevAPI enables you to work with both relational 
and document data. AdminAPI enables you to work with InnoDB Cluster, InnoDB ClusterSet, and 
InnoDB ReplicaSet 

Download MySQL Shell from: https://dev.mysql.com/downloads/shell/ 

Official Documentation: https://dev.mysql.com/doc/mysql-shell/8.0/en/

.. Install-Section-Start

Install MySQL Shell
^^^^^^^^^^^^^^^^^^^

Install by Repository
`````````````````````

`MySQL Documentation <https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install-linux-quick.html>`_ 

  - Locate the current respoitory files needed.  The installation example below may be outdated but the links/version can be found here:
    
    - `YUM/DNF MySQL Repositories <https://dev.mysql.com/downloads/repo/yum/>`_
    - `APT MySQL Repositories <https://dev.mysql.com/downloads/repo/apt/>`_
  
  - Install Repository

    .. note::
        Below is the automated method of installing the repo for a specific version using APT.  Should you use the incorrect version by accident and you need to change
        it to a different one after installing the repo, the ``dpkg-reconfigure mysql-apt-config`` command can be used with an interactive
        GUI.  Be sure to ``unset DEBIAN_FRONTEND`` prior or you will not see the GUI.

    .. tabs::

        .. group-tab:: Ubuntu

            .. code-block:: bash
                
                # Example: mysql-8.0, mysql-5.7, mysql-8.4-lts
                mySqlRepo=mysql-8.0
                export DEBIAN_FRONTEND=noninteractive
                echo mysql-apt-config mysql-apt-config/enable-repo select $mySqlRepo | sudo debconf-set-selections
                echo mysql-apt-config mysql-apt-config/select-server select $mySqlRepo | sudo debconf-set-selections
                curl https://repo.mysql.com/mysql-apt-config_0.8.33-1_all.deb -o mysql-apt.deb
                dpkg -i mysql-apt.deb
                unset DEBIAN_FRONTEND
                apt update
                        
        .. group-tab:: RHEL 9

            .. code-block:: bash

                curl https://repo.mysql.com//mysql80-community-release-el9-5.noarch.rpm -o mysql-yum.rpm
                rpm -ihv mysql-yum.rpm
        
        .. group-tab:: RHEL 8

            .. code-block:: bash

                curl https://repo.mysql.com//mysql80-community-release-el8-9.noarch.rpm -o mysql-yum.rpm
                rpm -ihv mysql-yum.rpm

  - Install MySQL Shell

    .. tabs::

        .. group-tab:: Ubuntu

            .. code-block:: bash
        
                apt install mysql-shell -y
                        
        .. group-tab:: RHEL

            .. code-block:: bash

                yum install mysql-shell -y

Install by Download
```````````````````
    
    .. toggle-header::
        :header: **Expand for Install by Download**
        
        - The example below may be outdated but the links/versions can be found here:
            - `YUM/DNF MySQL Repositories <https://dev.mysql.com/downloads/>`_

        .. tabs::

            .. group-tab:: Ubuntu 22.04

                .. code-block:: bash
            
                    wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell_8.0.34-1ubuntu22.04_amd64.deb
                    dpkg -i mysql-shell_8.0.34-1ubuntu22.04_amd64.deb
                            
            .. group-tab:: RHEL 9
                    
                .. code-block:: bash
                    
                    wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell-8.0.34-1.el9.x86_64.rpm
                    rpm -i mysql-shell-8.0.34-1.el9.x86_64.rpm

.. Install-Section-Stop

.. Commands-Section-Start
MySQL Shell Commands
^^^^^^^^^^^^^^^^^^^^

Save History
`````````````
    
    .. code-block:: bash
            
        \option --persist history.autoSave=1 

Get Status
``````````
    
    * Get Cluster Status
        .. code-block:: js
            :force:
            
            \c clusterAdmin@dbb-1:3306
            cluster = dba.getCluster()
            cluster.status()
    
    * Get Extended Cluster Status. (This will provide a more detailed return)
        .. code-block:: js
            :force:
            
            \c clusterAdmin@dbb-1:3306
            cluster = dba.getCluster()
            cluster.status({extended: 1})
    
    * Get Cluster Set Status.
        .. code-block:: js
            :force:
            
            \c clusterAdmin@dbb-1:3306
            clusterset = dba.getClusterSet()
            clusterset.status()
    
    * Get Extended Cluster Set Status. (This will provide a more detailed return)
        .. code-block:: js
            :force:
            
            \c clusterAdmin@dbb-1:3306
            clusterset = dba.getClusterSet()
            clusterset.status({extended: 1})
    

Add/Remove Nodes
````````````````

    * Removing a Node from a Cluster  
        .. code-block:: js
            :force:
            
            \c clusterAdmin@dbb-1:3306
            cluster = dba.getCluster()
            cluster.removeInstance('clusterAdmin@dbd-2:3306') 
            cluster.status()

    * Adding a Node to a Cluster 
        .. code-block:: js
            :force:
            
            \c clusterAdmin@dbb-1:3306
            cluster = dba.getCluster()
            cluster.addInstance('clusterAdmin@dbd-2:3306')
            cluster.status()

Running Scripts
```````````````

    * Using a Script 
        .. code-block:: bash
            
            mysqlsh --file myscript.js

Planned Failover
````````````````

    * Failover to another Cluster Member at the same site.
        .. code-block:: js
            :force:
            
            \c clusterAdmin@dbd-1:3306
            cluster = dba.getCluster()
            cluster.setPrimaryInstance("dbd-2:3306") 
            cluster.status()

    * Failover to another Site.
        .. code-block:: js
            :force:
           
            \c clusterAdmin@dbd-1:3306
            cs = dba.getClusterSet()
            cs.setPrimaryCluster("B") 
            cs.status()   
 
 
Unplanned Disaster Failover
```````````````````````````

    * Recover from all nodes down at a single site
        .. code-block:: js
            :force:
            
            mysqlsh
            \c clusterAdmin@dbd-1:3306
            dba.rebootClusterFromCompleteOutage()
    
    * Emergency Failover when a site is down. 
      This process will bring up the Cluster at site B. 
      You should take steps to ensure that no writes go to site A if/when it comes back up. This can be done
      by stopping the morpheus-ui and/or fencing the router traffic.

        .. note:: This should only be done as a last resort when the primary site can't be brought up

        .. code-block:: js
            :force:
            
            mysqlsh
            \c clusterAdmin@dbd-1:3306
            clusterset = dba.getClusterSet()
            clusterset.status()
            clusterset.forcePrimaryCluster("B")
            clusterset.status()

    * Emergency Failover Recovery of down site. 
      Once Power is restored to Site A nodes, you can go through the repair process. 
        .. code-block:: js
            :force:
            
            // Connect to site A node to repair cluster from all nodes down.
            mysqlsh 
            \c clusterAdmin@dbd-1:3306
            dba.rebootClusterFromCompleteOutage()
            clusterset = dba.getClusterSet()
            clusterset.rejoinCluster("A")
    
Router Config
`````````````
 
    * Setting MySQL Router target Cluster. This will force the router to only connect to the cluster specified.
        .. code-block:: js
            :force:
            
            mysqlsh 
            \c clusterAdmin@dbd-1:3306
            clusterset = dba.getClusterSet()
            // get the connected router information
            clusterset.routingOptions()
            // Find the router you want to change.
            clusterset.setRoutingOption('morphb.test.local::morphb', 'target_cluster', 'B')
            // confirm the settings
            clusterset.routingOptions()
           
.. Commands-Section-Stop    
        