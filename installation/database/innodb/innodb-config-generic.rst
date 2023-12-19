Configure Morpheus Database and User
````````````````````````````````````

#. Create the Database you will be using with |morpheus|.  Login to mysql on **Node 01**:

   .. note:: 
      When connecting to the database to run the following commands, either use a MySQL node to connect (since it has the ``mysql`` command installed) 
      or use a |morpheus| App node, if the Morpheus RPM/DEB has been installed.  The location for the ``mysql`` command after |morpheus| is installed is 
      : ``/opt/morpheus/embedded/bin/mysql``

   .. note:: 
      If connecting to a MySQL node directly, this will use port ``3306``.  If connecting to a MySQL router on an app node, this will use port ``6446``.  Examples:

      ``mysql -u root -p``
      ``/opt/morpheus/embedded/bin/mysql -h dbnode1 -u clusterAdmin -p``
      ``/opt/morpheus/embedded/bin/mysql -h 127.0.0.1 -P 6446 -u clusterAdmin -p``
   
   .. code-block:: bash

    [root]# mysql -u root -p
      password: `enter root password`

    mysql> CREATE DATABASE morpheus CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

    mysql> show databases;


#. Next create your |morpheus| database user. This is the user the |morpheus| app nodes will auth with mysql.

   .. code-block:: bash

    mysql> CREATE USER 'morpheusDbUser'@'%' IDENTIFIED BY 'morpheusDbUserPassword';

#. Next Grant your new |morpheus| user permissions.

   .. code-block:: bash

    mysql> GRANT ALL PRIVILEGES ON morpheus.* TO 'morpheusDbUser'@'%' with grant option;

    mysql> GRANT SELECT, PROCESS, SHOW DATABASES, RELOAD ON *.* TO 'morpheusDbUser'@'%';

    mysql> FLUSH PRIVILEGES;

    mysql> exit

