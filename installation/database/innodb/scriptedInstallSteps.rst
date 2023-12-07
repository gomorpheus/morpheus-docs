Scripted Install Steps
======================

Install MySQL
^^^^^^^^^^^^^

Run the following script on each DB node to install MySQL and configure to best practice.
  
  * Create the shell script 

     .. code-block:: bash

          vi install.sh


  * Add the following code to the file
     .. toggle-header::
            :header: **Expand for Code**

            .. include:: /installation/database/innodb/scripts/mysqlinstall.rst

  * Save and set the file to executable

      .. code-block:: bash

          chmod +x install.sh

  * View what the mysql config file should have set.
     .. toggle-header::
            :header: **Expand for mysql config**

              * mySQL config file settings on DB servers
        
                .. code-block:: bash
                     
                     [mysqld]
                     bind-address = 0.0.0.0
                     max_connections = 2000                # Increases Max Connections Supported
                     innodb_buffer_pool_size=6G            # **Change 6 to actual number**. Runs more in RAM, 70% of available MEM is currently being set with scripted install
                     innodb_buffer_pool_instances=6        # **Change 6 to actual number**. Allows for better Multi-Threading. Should be 1 instance per 1G of buffer pool size above.
                     innodb_use_fdatasync=ON               # Enables fdatasync() for faster writes than fsync()
                     sql_generate_invisible_primary_key=1  # This ensures that MySQL creates an invisible primary key for each Morpheus table that does not have one. 
        
                     [mysqldump]
                     set-gtid-purged=OFF                   # This is to ensure if a mysqldump is performed from the DB node it is in the proper format for restore.
            

Morpheus App Node mySQL config file 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
  Setup my.cnf config file on each **Morpheus App Node**. (you will need to create the /etc/my.cnf)
        
        .. code-block:: bash
             
             [mysqldump]
             set-gtid-purged=OFF       # without this setting Morpheus will not be able to create backups that can be used for restore.
 

Install MySQL Router 
^^^^^^^^^^^^^^^^^^^^
    This should be installed on each Morpheus App Node

      .. include:: /installation/database/innodb/mysqlRouter.rst
        :start-after: Install-Section-Start
        :end-before: Install-Section-Stop

Configure MySQL Router
^^^^^^^^^^^^^^^^^^^^^^
      
      .. include:: /installation/database/innodb/mysqlRouter.rst
        :start-after: Config-Section-Start
        :end-before: Config-Section-Stop

Install MySQL Shell 
^^^^^^^^^^^^^^^^^^^
    This should be installed on each Morpheus App Node

    .. include:: /installation/database/innodb/mysqlShell.rst
      :start-after: Install-Section-Start
      :end-before: Install-Section-Stop

MySQL Shell Script 
^^^^^^^^^^^^^^^^^^
    You will only need to create and run this from a single Node with MySQl Shell installed.

    .. include:: /installation/database/innodb/scripts.rst
      :start-after: Scripts-Section-Start
      :end-before: Scripts-Section-Stop

    Add the following code to the file

    .. toggle-header::
            :header: **Expand for Single Site Code**

            .. include:: /installation/database/innodb/scripts/singlesitejs.rst

    .. toggle-header::
            :header: **Expand for Multi Site Code**

            .. include:: /installation/database/innodb/scripts/multisitejs.rst
    
    |
    Run the code as sudo root

      .. code-block:: bash

          bash myscript.js

MySQL Dump Backup Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. include:: /installation/database/innodb/innodbBackup.rst
      :start-after: Config-Section-Start
      :end-before: Config-Section-Stop

Create Morpheus Database and User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    .. include:: /installation/database/innodb/innodb-config-generic.rst