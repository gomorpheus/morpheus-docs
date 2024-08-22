BinLog Experation
=======
.. Config-Section-Start

Perform on all DB nodes

The default binary log expiration period is 2592000 seconds, which equals 30 days (30*24*60*60 seconds). This can end up taking up a lot of space and cause the database node to run out of storage. To prevent this we can set the expiration period lower (We recommend 7 days)

The following settings should to be set on all database nodes. 

    Possible locations, depending on OS:
        - ``/etc/mysql/my.cnf``
        - ``/etc/my.cnf``
        - ``/etc/my.cnf.d/my.cnf``

    * Add these entries manually to the appropriate file.
        
        .. code-block:: 

           [mysqld]
           binlog_expire_logs_seconds=604800

    * To make the settings take effect you can restart mysql service or if you can't bring down mysql run the following 

        .. code-block:: bash

            # Set binlog_expire_logs_seconds
            mysql> SET GLOBAL binlog_expire_logs_seconds = 604800;

            # Confirm binlog_expire_logs_seconds was set and auto purge is ON
            mysql> show variables like 'binlog_expire_logs_seconds';
            mysql> show variables like 'binlog_expire_logs_auto_purge';
            
            # Flush binlogs manually - All bin logs older than what was set will be purged
            mysql> flush binary logs;
.. Config-Section-Stop

.. note:: 
    The default binary log expiration period is 2592000 seconds, which equals 30 days (30*24*60*60 seconds). 
    The default applies if neither binlog_expire_logs_seconds nor the **deprecated** system variable expire_logs_days has a value set at startup. 
    If a non-zero value for one of the variables binlog_expire_logs_seconds or expire_logs_days is set at startup, this value is used as the binary log expiration period. 
    If a non-zero value for both of those variables is set at startup, the value for binlog_expire_logs_seconds is used as the binary log expiration period, and the value for expire_logs_days is ignored with a warning message.


BinLog file location 
    - ``/var/lib/mysql``

`Understaning Binlogs <https://www.linkedin.com/pulse/detailed-guide-understanding-mysql-binlogs-pranav-pandey/>`_ 