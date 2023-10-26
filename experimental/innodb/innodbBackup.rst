Backups
=======
.. Config-Section-Start

The following settings need to be set on any node that will be performing a mysqldump
This includes every Morpheus App node. If doing appliance backups the Morpheus app nodes will initiate 
a mysqldump and if this is not set the backup will have errors and not be restorable.

    * The below will create the file /etc/my.cnf and add the folllowing lines. 
      If you are adding this to a DB server that alrady has this file with configurations add these entries manually to that file.
        
        [mysqldump]
        set-gtid-purged=OFF

         .. code-block:: 

           echo -e "[mysqldump]\nset-gtid-purged=OFF" | sudo tee /etc/my.cnf

.. Config-Section-Stop