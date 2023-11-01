Scripted Install Steps
======================

Install MySQL
-------------

Run the following script on each DB node to install MySQL and configure to best practice.
  
  * Create the shell script 

     .. code-block:: bash

          vi install.sh


  * Add the following code to the file
     .. toggle-header::
            :header: **Expand for Code**

            .. include:: ./scripts/mysqlinstall.rst

  * Save and set the file to executable

      .. code-block:: bash

          chmod +x install.sh

Install MySQL Router 
-------------------------------------------------------------------------
    This should be installed on each Morpheus App Node

      .. include:: ./mysqlRouter.rst
        :start-after: Install-Section-Start
        :end-before: Install-Section-Stop

Configure MySQL Router
--------------------
      
      .. include:: ./mysqlRouter.rst
        :start-after: Config-Section-Start
        :end-before: Config-Section-Stop

Install MySQL Shell 
-------------------
    This should be installed on each Morpheus App Node

    .. include:: ./mysqlShell.rst
      :start-after: Install-Section-Start
      :end-before: Install-Section-Stop

MySQL Shell Script 
------------------
    You will only need to create and run this from a single Node with MySQl Shell installed.

    .. include:: ./scripts.rst
      :start-after: Scripts-Section-Start
      :end-before: Scripts-Section-Stop

    Add the following code to the file

    .. toggle-header::
            :header: **Expand for Single Site Code**

            .. include:: ./scripts/singlesitejs.rst

    .. toggle-header::
            :header: **Expand for Multi Site Code**

            .. include:: ./scripts/multisitejs.rst
    
    |
    Run the code as sudo root

      .. code-block:: bash

          bash myscript.js

MySQL Dump Backup Settings
---------------------------

    .. include:: ./innodbBackup.rst
      :start-after: Config-Section-Start
      :end-before: Config-Section-Stop

* Create Morpheus User and Database
    
    .. include:: ./innodb-config-generic.rst