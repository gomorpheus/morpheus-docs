Group Replication Transaction Size Limit
========================================
.. Config-Section-Start

The following settings need to be set on InnoDB cluster members./

  Possible locations, depending on OS:
    - ``/etc/mysql/my.cnf``
    - ``/etc/my.cnf``
    - ``/etc/my.cnf.d/my.cnf``

    * If you are adding this to a DB server that already has this file with configurations add these entries manually to that file.
    
        .. code-block:: 

           [mysqld]
           group_replication_transaction_size_limit=0

    * Use this example command to create the file and add the setting.
         
         .. code-block:: bash

           echo -e "group_replication_transaction_size_limit=0" | sudo tee -a /etc/my.cnf

.. IMPORTANT:: Perform on all DB nodes

.. toggle-header::
    :header: **Expand for example mysql config**

      * MySQL config file settings on DB servers

        .. code-block:: bash
              
              [mysqld]
              bind-address = ::                     # Allows both IPv4 and v6.  Alternatively can use * to do the same or 0.0.0.0 for IPv4 only
              max_connections = 2001                # Increases Max Connections Supported
              innodb_buffer_pool_size=6G            # **Change 6 to actual number**. Runs more in RAM, 70% of available MEM is currently being set with scripted install
              innodb_buffer_pool_instances=6        # **Change 6 to actual number**. Allows for better Multi-Threading. Should be 1 instance per 1G of buffer pool size above.
              innodb_use_fdatasync=ON               # Enables fdatasync() for faster writes than fsync()
              sql_generate_invisible_primary_key=1  # This ensures that MySQL creates an invisible primary key for each Morpheus table that does not have one. 
              binlog_expire_logs_seconds=604800
              binlog_expire_logs_auto_purge=ON
              group_replication_transaction_size_limit=0
  
.. Config-Section-Stop