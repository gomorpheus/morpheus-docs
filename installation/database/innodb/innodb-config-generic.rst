Configure Morpheus Database and User
````````````````````````````````````

#. Create the Database you will be using with |morpheus|.  Login to mysql on **Node 01**:

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

