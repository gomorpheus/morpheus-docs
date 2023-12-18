Backups
=======
.. Config-Section-Start

The following settings need to be set on any node that will be performing a mysqldump.
This includes every Morpheus App node. If doing appliance backups the Morpheus app nodes will initiate 
a mysqldump and if this is not set the backup will have errors and not be restorable.

    * If you are adding this to a DB server that already has this file with configurations add these entries manually to that file.
        
        .. code-block:: 

           [mysqldump]
           set-gtid-purged=OFF

    * Use this example command to create the file and add the setting.

         Possible locations, depending on OS:
        
           - ``/etc/mysql/my.cnf``
           - ``/etc/my.cnf``
           - ``/etc/my.cnf.d/my.cnf``
         
         .. code-block:: bash

           echo -e "[mysqldump]\nset-gtid-purged=OFF" | sudo tee -a /etc/my.cnf

.. Config-Section-Stop