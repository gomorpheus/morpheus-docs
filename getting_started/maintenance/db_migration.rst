Morpheus DB Migration
---------------------

If your new installation is part of a migration or you need to move the data from your original Morpheus database, this is easily accomplished by using a stateful dump.

To begin this, stop the Morpheus UI on your original Morpheus server:

.. code-block:: bash

 [root@app-server-old ~] morpheus-ctl stop morpheus-ui

Once this is done you can safely export. To access the MySQL shell we will need the password for the Morpheus DB user. We can find this in the morpheus-secrets file:

.. code-block:: bash

  [root@app-server-old ~] cat /etc/morpheus/morpheus-secrets.json | grep morpheus_password
  "morpheus_password": "451e122cr5d122asw3de5e1b", <---------------this one
  "morpheus_password": "9b5vdj4de5awf87d",

Take note of the first ``morpheus_password`` as it will be used to invoke a dump. Morpheus provides embedded binaries for this task. Invoke it via the embedded path and specify the host. In this example we are using the morpheus database on the MySQL listening on localhost. Enter the password copied from the previous step when prompted:

.. code-block:: bash

  [root@app-server-old ~] /opt/morpheus/embedded/mysql/bin/mysqldump -u morpheus -h 127.0.0.1 morpheus -p > /tmp/morpheus_backup.sql
  Enter password:


This file needs to be pushed to the new Morpheus Installation's backend. Depending on the GRANTS in the new MySQL backend, this will likely require moving this file to one of the new Morpheus frontend servers.

Once the file is in place it can be imported into the backend. Begin by ensuring the Morpheus UI service is stopped on all of the application servers:

.. code-block:: bash

 [root@app-server-new ~] morpheus-ctl stop morpheus-ui

Then you can import the MySQL dump into the target database using the embedded MySQL binaries, specifying the database host, and entering the password for the morpheus user when prompted:

.. code-block:: bash

  [root@app-server-new ~] /opt/morpheus/embedded/mysql/bin/mysql -u morpheus -h 10.1.2.2 morpheus -p < /tmp/morpheus_backup.sql
  Enter password:

The data from the old appliance is now replicated on the new appliance. Simply start the UI to complete the process:

.. code-block:: bash

  [root@app-server-new ~] morpheus-ctl start morpheus-ui

With the migration complete, you will also need to update the stored password for the appliance backup job as the destination appliance will have a different dynamically-generated MySQL password. We can update that password value by altering the backup directly in the |morpheus| database.

.. code-block:: bash

  select * from backup where `name` ='Morpheus Appliance';
  UPDATE `morpheus`.`backup` SET `ssh_host` = '127.0.0.1', `target_password` = 'its-a-secret' WHERE `id` = '1';
