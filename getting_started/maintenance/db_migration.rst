Morpheus DB Migration
---------------------

If your new installation is part of a migration or you need to move the data from your original Morpheus database, this is easily accomplished by using a stateful dump.

To begin this, stop the Morpheus UI on your original Morpheus server:

.. code-block:: bash

 [root@app-server-old ~] morpheus-ctl stop morpheus-ui

Once this is done you can safely export. For an embedded database using generated credentials, retrieve the exact MySQL application-user key without printing unrelated secrets:

.. code-block:: bash

  [root@app-server-old ~] jq -r '.mysql.morpheus_password' /etc/morpheus/morpheus-secrets.json

For an external database or customized connection, obtain the database name, host, user, and password from the effective ``mysql`` configuration in ``/etc/morpheus/morpheus.rb``. Do not use generated values from ``morpheus-secrets.json`` for an external service. Morpheus provides embedded client binaries, but the following example applies only to the default local database and schema. Enter the password when prompted:

.. code-block:: bash

  [root@app-server-old ~] /opt/morpheus/embedded/mysql/bin/mysqldump -u morpheus -h 127.0.0.1 morpheus -p > /tmp/morpheus_backup.sql
  Enter password:


This file needs to be pushed to the new Morpheus Installation's backend. Depending on the GRANTS in the new MySQL backend, this will likely require moving this file to one of the new Morpheus frontend servers.

Once the file is in place it can be imported into the backend. Begin by ensuring the Morpheus UI service is stopped on all of the application servers:

.. code-block:: bash

 [root@app-server-new ~] morpheus-ctl stop morpheus-ui

The previously documented direct ``mysql`` import command is not a supported general migration procedure. Stateful dumps may contain database-level statements, and the correct target, privileges, topology sequence, and post-import checks vary with custom schema names and external databases. Contact HPE Support for a migration and rollback plan validated for both appliance versions and database topologies. Keep every application UI stopped until the import has been validated.

After validation, start the UI on each application server as directed by the migration plan:

.. code-block:: bash

  [root@app-server-new ~] morpheus-ctl start morpheus-ui

With the migration complete, you will also need to update the stored password for the appliance backup job as the destination appliance will have a different dynamically-generated MySQL password. We can update that password value by altering the backup directly in the |morpheus| database.

.. code-block:: bash

  select * from backup where `name` ='Morpheus Appliance';
  UPDATE `morpheus`.`backup` SET `ssh_host` = '127.0.0.1', `target_password` = 'its-a-secret' WHERE `id` = '1';

.. important:: After the migration it is important to reset the unique ID of the Morpheus Appliance. This will ensure your new installation will communicate correctly with the Morpheus Hub.

The final step is to generate a new unique ID for the Morpheus Appliance. Firstly run the following SQL command on the database for the new installation:

.. code-block:: bash

  UPDATE appliance_instance SET hub_unique_id = NULL;

Secondly, re-apply your Morpheus license key within the Morpheus UI via the "Upgrade A License" action within Administration -> Settings -> License
