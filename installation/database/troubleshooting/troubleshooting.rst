.. _db-troubleshooting:

Troubleshooting
===============

SELinux Issues
^^^^^^^^^^^^^^

Creating a profile
``````````````````

* Install the tools

   * yum install policycoreutils-python-utils

* Have SELinux in ``permissive`` mode
* Run through all tasks to create the denied messages
* Run this command to grab the entries from the log and create a policy file
    
    .. code-block:: bash

        grep -i denied /var/log/audit/audit.log | grep mysqld_t | audit2allow -M PXC
    
    This will create 2 files a ``PXC.pp`` and a ``PXC.te`` The ``PXC.te`` is a human readble version of the ``PXC.pp`` policy file

* Run this command to make this policy active

    .. code-block:: bash
        
        semodule -i PXC.pp

Create or update an existing config
```````````````````````````````````

* Create/edit your ``PXC.te`` file with the config
* Run the following commands
    
    .. code-block::

        checkmodule -M -m -o PXC.mod PXC.te
        semodule_package -o PXC.pp -m PXC.mod
        semodule -i PXC.pp

Additional Info
```````````````

* SELinux file location

    ``/etc/selinux/targeted/policy``

* Helpful commands
    
    * Will list all loaded modules. Custom modules display at the top

        .. code-block:: bash
            
            semodule -l

    * Check policy type

        .. code-block:: bash
            
            sestatus | grep Loaded 

    * Disable a policy

        .. code-block:: bash

            semodule -d

    * Remove a module

        .. code-block:: bash

            semodule -r

    * Enable a module

        .. code-block:: bash

            semodule -e

MySQL Issues
^^^^^^^^^^^^^^

Reset forgotten root password
```````````````````````````````````

        .. code-block:: bash

            systemctl stop mysql
            #add to /etc/my.cnf:
               #skip-grant-tables
            systemctl start mysql
            #Change password:
            mysql> FLUSH PRIVILEGES;
            mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY ('NewPassword');
            mysql> FLUSH PRIVILEGES;
            mysql> exit
            systemctl stop mysql
            #remove from /etc/my.cnf:
               #skip-grant-tables
            systemctl start mysql

Rejoin InnoDB node(s) to cluster (at least one cluster member is functioning)
`````````````````````````````````````````````````````````````````````````````

This assumes that at least one member node is accessible and ``ONLINE`` but one or more are ``OFFLINE``.  When using MySQL Shell 
be sure to connect to the node that is ``ONLINE``, otherwise you'll receive errors of being unable to get cluster info.  If ``dba.rebootClusterFromCompleteOutage()`` 
is used, the following error may be seen, which indicates the cluster is online and this procedure is appropriate:

    .. code-block:: text
        
        Cluster instances: 'mysql01.example.local:3306' (OFFLINE), 'mysql02.example.local:3306' (OFFLINE), 'mysql03.example.local:3306' (ONLINE)
        ERROR: The Cluster is ONLINE
        Dba.rebootClusterFromCompleteOutage: The Cluster is ONLINE (RuntimeError)

Other errors may contain errors related to quorum or even the MySQL Router timesout when starting.

.. important::
    The ``OFFLINE`` nodes must be powered on, with mysqld service started, and accessible.  Test accessing them using the ``mysql`` command if needed

Rejoin the ``OFFLINE`` nodes to the cluster:

    .. code-block:: js

            \c clusterAdmin@mysql03.example.local:3306
            cluster = dba.getCluster()
            cluster.status()  // Check Status of cluster before making changes
            cluster.rejoinInstance("clusterAdmin@mysql01.example.local")
            cluster.rejoinInstance("clusterAdmin@mysql02.example.local")
            \exit


Recover From Failed Single Site when dba.rebootclusterfromcompleteoutage() and rejoins dont work
````````````````````````````````````````````````````````````````````````
* Take a backup of the DB before performing any of these tasks.
* Make sure morpheus-ui is stopped on all all nodes.
* Stop mysqlrouter on all nodes.

*  Connect to mysql on each DB node and run the following to get the node with the latest GTID to use as source.
    
    .. code-block:: bash

        mysql -u clusterAdmin -p 
        SHOW VARIABLES LIKE 'gtid_executed';


*  Connect to each DB Node and drop the metadata and turn off super read only.
    
    .. code-block:: bash

        mysql -u clusterAdmin -p 
        set global super_read_only = OFF;
        DROP DATABASE mysql_innodb_cluster_metadata;

.. important::
    
    In some cases, there may be an error of GTID conflicts or value not expected.  A force of a primary node can
    be set using the following command example:  ``var cluster = dba.rebootClusterFromCompleteOutage('A',{force: true,primary: "InnoDB1:3306"})``

*  Connect to the DB node with the highest GTID with mysqlsh and create the cluster.
    
    .. code-block:: bash

        \c clusterAdmin@mysql01:3306
        cluster = dba.createCluster("A") # Join the other nodes to this cluster.
        cluster.addInstance("sql02:3306") # Select c to clone.
        cluster.addInstance("sql03:3306") # Select c to clone.
        cluster.status() # Check the cluster status

*  Bootstrap mysqlrouter on each node running it to ensure it has the updated metadata.
    
    .. code-block:: bash
       
        mysqlrouter --bootstrap clusterAdmin@sql01:3306 --account routeruser --user=mysqlrouter --disable-rest force
        systemctl start mysqlrouter # restart mysql router


Recover Secondary Site From Failed Multi Site when dba.rebootclusterfromcompleteoutage() and rejoins dont work
````````````````````````````````````````````````````````````````````````
* Take a backup of the DB before performing any of these tasks.

*  Connect to each DB Node and drop the metadata and turn off super read only.
    
    .. code-block:: bash

        mysql -u clusterAdmin -p 
        set global super_read_only = OFF;
        DROP DATABASE mysql_innodb_cluster_metadata;

*  Connect to a primary site node using mysqlsh
    
    .. code-block:: bash

        \c clusterAdmin@mysql-A01:3306
        cluster = dba.getCluster() # Set the cluster variable
        cluster.status() # Confirm the cluster status of the primary site is healthy before moving on.
        clustersset = dba.getClusterSet()  # Set the cluster set variable
        clusterset.status() # Check the status of the cluster status
        clusterset.removeCluster("B", {force: true}) # Force Remove the Secondary B side cluster
        # Now will recreate the B side Cluster from this same A side Node connection
        clusterb = clusterset.createReplicaCluster("mysql-B01:3306", "B")
        clusterb.addInstance("mysql-B02:3306")
        clusterb.addInstance("mysql-B03:3306")
        clusterb.status() # Confirm the clusterset status.


Force Remove and Rejoin InnoDB node(s) to cluster (brute force)
``````````````````````````````````````````````````````````````````````
Be sure to snapshot systems. This has the potential to be destructive.

*  Connect to mysqlsh
    
    .. code-block:: bash

        var cluster = dba.getCluster(); # From bad node, connect to healthy node.
        cluster.rescan(); # Press 'Y' to remove the missing node(s) on the interactive MySQL Shell window.
        \exit

*  Login to MySQL from bad Node(s)
    
    .. code-block:: bash

        set global super_read_only = OFF;
        STOP GROUP_REPLICATION;
        RESET SLAVE ALL;
        DROP DATABASE mysql_innodb_cluster_metadata;
*  Go to mysqlsh from bad node, and add to cluster
    
    .. code-block:: bash

        cluster.addInstance('clusterAdmin@InnoDB1:3306')
*  On interactive window: Select the recovery method as "Clone"
*  Check status of cluster when done.
    
    .. code-block:: bash

        cluster.status()

Dissolving (destroying) a Cluster - Destructive
```````````````````````````````````````````````

During an installation, there may be issues where the scripted installs fail and instances
may not be able to resolve their hostsnames because they were configured incorrect.  In this
case, the cluster may need to be reset.  More than likely, only 1 instance has been added to
the cluster.  However, it would be good to perform this on each member in case, or at least
check the status of the cluster from each, once the cluster has been dissolved.

Dissolve Documentation:

    `YUM/DNF MySQL Repositories <https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-innodb-cluster-working-with-cluster.html>`_


* Connect to the cluster by using a node from the cluster and create the cluster vairable:

    .. code-block:: bash
        \c clusterAdmin@db01:3306
	    cluster = dba.getCluster()

* Check the status first, to ensure the cluster members but also this is the cluster to dissolve:

    .. code-block:: bash

        cluster.status()

* If this is the cluster you wish to dissolve, use the following command.  **THIS IS DESTRUCTIVE AND THE CLUSTER WILL BE LOST FOREVER**:

    .. code-block:: bash

	    cluster.dissolve()

* In the case mentioned above, where the hostnames were incorrect or not resolvable, update the hostnames with ``hostnamectl set-hostname <hostName>``
and be sure to restart the ``mysql`` or ``mysqld`` service (depending on the OS).

* The ``.js`` scripts can be used to create the cluster again.