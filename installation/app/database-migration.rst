Database Migration
^^^^^^^^^^^^^^^^^^

If your new installation is part of a migration then you need to move the data from your original |morpheus| database to your new one. This is easily accomplished by using a stateful dump.

#. To begin this, stop the |morpheus| UI on your original |morpheus| server:

   .. code-block:: bash

    [root@node-old ~]# morpheus-ctl stop morpheus-ui

#. Once this is done you can safely export. To access the MySQL shell we will need the password for the |morpheus| DB user. We can find this in the morpheus-secrets file:

   .. code-block:: bash

      [root@node-old ~]# cat /etc/morpheus/morpheus-secrets.json

        {
          "mysql": {
              "root_password": "***REDACTED***",
              "morpheus_password": "***REDACTED***",
              "ops_password": "***REDACTED***"
                },
          "rabbitmq": {
                    "morpheus_password": "***REDACTED***",
                    "queue_user_password": "***REDACTED***",
                    "cookie": "***REDACTED***"
          },
          "vm-images": {
            "s3": {
                "aws_access_id": "***REDACTED***",
                "aws_secret_key": "***REDACTED***"
              }
            }
        }

#. Take note of this password as it will be used to invoke a dump. |morpheus| provides embedded binaries for this task. Invoke it via the embedded path and specify the host. In this example we are using the |morpheus| database on MySQL listening on localhost. Enter the password copied from the previous step when prompted:

   .. code-block:: bash

      [root@node-old ~]# /opt/morpheus/embedded/mysql/bin/mysqldump -u morpheus -h 127.0.0.1 morpheus -p > /tmp/morpheus_backup.sql

      Enter password:

   This file needs to be pushed to the new |morpheus| Installation’s backend. Depending on the GRANTS in the new MySQL backend, this will likely require moving this file to one of the new |morpheus| frontend servers.

#. Once the file is in place it can be imported into the backend. Begin by ensuring the |morpheus| UI service is stopped on all of the application servers:

   .. code-block:: bash

      [root@node-1 ~]# morpheus-ctl stop morpheus-ui
      [root@node-2 ~]# morpheus-ctl stop morpheus-ui
      [root@node-3 ~]# morpheus-ctl stop morpheus-ui

#. Then you can import the MySQL dump into the target database using the embedded MySQL binaries, specifying the database host, and entering the password for the |morpheus| user when prompted:

   .. code-block:: bash

      [root@node-1 ~]# /opt/morpheus/embedded/mysql/bin/mysql -u morpheus -h 10.130.2.38 morpheus -p < /tmp/morpheus_backup.sql
      Enter password: