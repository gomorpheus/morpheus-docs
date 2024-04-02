InnoDB MySQL Config (my.cnf)
============

Full config 
^^^^^^^^^^^^^^^^^^^^^^^^
.. Full-Config-Section-Start

Possible locations, depending on OS:
    - ``/etc/mysql/my.cnf``
    - ``/etc/my.cnf``
    - ``/etc/my.cnf.d/my.cnf``

    * mySQL config file settings on DB servers

        .. IMPORTANT:: Make sure to update innodb_buffer_pool_size and innodb_buffer_pool_instances to the appropriate size.
        
        .. code-block:: bash
             
             [mysqld]
             bind-address = 0.0.0.0
             max_connections = 2001                # Increases Max Connections Supported
             innodb_buffer_pool_size=6G            # **Change 6 to actual number**. Runs more in RAM, 70% of available MEM is currently being set with scripted install
             innodb_buffer_pool_instances=6        # **Change 6 to actual number**. Allows for better Multi-Threading. Should be 1 instance per 1G of buffer pool size above.
             innodb_use_fdatasync=ON               # Enables fdatasync() for faster writes than fsync()
             sql_generate_invisible_primary_key=1  # This ensures that MySQL creates an invisible primary key for each Morpheus table that does not have one. 
             binlog_expire_logs_seconds=604800     # Set binlog experation to 7 days (default is 30 days)
             binlog_expire_logs_auto_purge=ON      # This is on by default - Allows binlogs to be purged based on what is set 

             [mysqldump]
             set-gtid-purged=OFF                   # This is to ensure if a mysqldump is performed from the DB node it is in the proper format for restore.

.. Full-Config-Section-Stop

InnoDB Backup Settings
^^^^^^^^^^^^^^^^^^^^^^^^
    .. include:: ./innodbBackup.rst

InnoDB BinLog Settings
^^^^^^^^^^^^^^^^^^^^^^^^
    .. include:: ./innodbBinlog.rst