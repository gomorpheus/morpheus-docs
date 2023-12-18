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

    .. code-block:: javascript

            \c clusterAdmin@mysql03.example.local:3306
            cluster = dba.getCluster()
            cluster.status()  // Check Status of cluster before making changes
            cluster.rejoinInstance("clusterAdmin@mysql01.example.local")
            cluster.rejoinInstance("clusterAdmin@mysql02.example.local")
            \exit

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

        cluster.getStatus()