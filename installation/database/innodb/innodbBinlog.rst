BinLog Experation
=======
.. Config-Section-Start

Perform on all DB nodes

The default binary log expiration period is 2592000 seconds, which equals 30 days (30*24*60*60 seconds). This can end up taking up a lot of space and cause the databse node to run out of storage. 
To prevent this we can set the epxiration perired lower (We recommend 7 days)

BinLog file location 
    - ``/var/lib/mysql``

The following settings should to be set on all database nodes. 

    * Add these entries manually to the appropriate file.
        
        .. code-block:: 

           [mysqld]
           binlog_expire_logs_seconds=604800

    * To make the settings take effect you can restart mysql service or if you can't bring down mysql run the following 

        .. code-block:: 
            # Set binlog_expire_logs_seconds
            mysql> SET GLOBAL binlog_expire_logs_seconds = 604800;
            mysql> show variables like 'binlog_expire_logs_seconds';
            
            # Flush binlogs
            # All bin logs older than what was set will be purged
            mysql> flush binary logs;

.. Config-Section-Stop