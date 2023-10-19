Scripted Install Steps
======================

#. Run the following script on each DB node to install MySQL and configure to best practice.
  
  * Create the shell script 

     .. code-block:: bash

          vi install.sh


  * Add the following code to the file
     .. toggle-header::
            :header: **Click to expand**

            .. include:: ./scripts/mysqlinstall.rst

  * save and set the file to executable

      .. code-block:: bash

          chmod +x install.sh