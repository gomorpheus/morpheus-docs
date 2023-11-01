Configure Morpheus Database and User
````````````````````````````````````

#. Create the Database you will be using with |morpheus|.  Login to mysql on **Node 01**:

   .. code-block:: bash

    [root]# mysql -u root -p
      password: `enter root password`

    mysql> CREATE DATABASE morpheus CHARACTER SET utf8 COLLATE utf8_general_ci;

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

Copy SSL Files to other nodes
`````````````````````````````

During initialization of **Node 01** the required `pem` files will be generated in ``/var/lib/mysql``. The ``ca.pem``, ``server-cert.pem`` and ``server-key.pem`` files need to match on all nodes in the cluster.

#. Copy the following files from **Node 01** to the same path (default is /var/lib/mysql) on **Node 02** and **Node 03**:

   - /var/lib/mysql/ca.pem
   - /var/lib/mysql/server-cert.pem
   - /var/lib/mysql/server-key.pem

   .. content-tabs::

      .. tab-container:: tab1
         :title: DB Node 1

         .. code-block:: bash

            [root]# scp /var/lib/mysql/ca.pem /var/lib/mysql/server-cert.pem /var/lib/mysql/server-key.pem root@192.168.101.02:/root

            [root]# scp /var/lib/mysql/ca.pem /var/lib/mysql/server-cert.pem /var/lib/mysql/server-key.pem root@192.168.101.03:/root

      .. tab-container:: tab2
         :title: DB Node 2

         .. code-block:: bash
   
            [root]# cp /root/ca.pem /root/server-cert.pem /root/server-key.pem /var/lib/mysql/
      
      .. tab-container:: tab3
         :title: DB Node 3

         .. code-block:: bash
   
            [root]# cp /root/ca.pem /root/server-cert.pem /root/server-key.pem /var/lib/mysql/

   .. important:: Ensure all 3 files match on all 3 nodes, including path, owner and permissions.

   .. note:: The generated certificate is self-signed. Consult Percona documentation for [mysqld] and SSL file configuration when providing your own.

Start the Remaining Nodes
`````````````````````````

   .. content-tabs::

      .. tab-container:: tab1
         :title: DB Node 2

         .. code-block:: bash

            [root]# systemctl start mysql

      .. tab-container:: tab2
         :title: DB Node 3

         .. code-block:: bash

            [root]# systemctl start mysql

   The services will automatically join the cluster using the sstuser we created earlier.

   .. NOTE:: Startup failures are commonly caused by misconfigured /etc/my.cnf files.

(Optional) Require Client Side TLS
``````````````````````````````````

It is recommended to enable TLS to secure communications with |morpheus|, or any application.  By default, Percona/MySQL will have TLS enabled using a
locally-signed certificate (the same used for replication above.  In |morpheus| the ``mysql['use_tls'] = true`` option in ``/etc/morpheus/morpheus.rb``
can be set to ensure the communication is using TLS.  However, this still allows |morpheus| to be misconfigured or another user/application to connect
to the database without TLS.

To ensure TLS is used, perform the following:

#. Edit the ``/etc/my.cnf`` file on **All Nodes** and add the following to the ``[mysqld]`` section:

   .. code-block:: bash

      require_secure_transport=ON

#. **One at a time**, restart the MySQL service on **All Nodes**

   .. code-block:: bash

      systemctl restart mysql

   .. important:: 
      **Node 01** may still be running the ``mysql@bootstrap.service`` service, and not mysql.  You can run ``systemctl stop mysql@bootstrap.service`` first
      and then run ``systemctl start mysql`` to restart the service.  The bootstrap service just needs to be run initially when the cluster is started.

#. To verify that mySQL now requires TLS, run the following command, replacing parameters as needed.  You should receive an error similar to 
   ``ERROR 3159 (HY000): Connections using insecure transport are prohibited while --require_secure_transport=ON``

   .. code-block:: bash

      mysql --ssl-mode=DISABLED -h 192.168.101.01 -u morpheusDbUser -p

Additional info:

   - https://dev.mysql.com/doc/refman/5.7/en/connection-options.html
   - https://dev.mysql.com/doc/refman/5.7/en/using-encrypted-connections.html
   - https://dev.mysql.com/doc/refman/5.7/en/encrypted-connection-protocols-ciphers.html