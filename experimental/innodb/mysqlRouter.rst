MySQL Router
^^^^^^^^^^^^

Introduction
````````````

MySQL Router is lightweight middleware that provides transparent routing between your 
application and any backend MySQL Servers. This router can run directly on the application 
nodes and be bootstrapped from the MySQL cluster.  

Download MySQL Routere from: https://dev.mysql.com/downloads/router/

Official Documentation: https://dev.mysql.com/doc/mysql-router/8.0/en/

The Default location of a bootstrapped mysqlrouter config file is: /etc/mysqlrouter/mysqlrouter.conf

.. Install-Section-Start

Install MySQL Router
````````````````````

    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                wget https://dev.mysql.com/get/Downloads/MySQL-Router/mysql-router-community_8.0.34-1ubuntu22.04_amd64.deb
                dpkg -i mysql-router-community_8.0.34-1ubuntu22.04_amd64.deb
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash

                wget https://dev.mysql.com/get/Downloads/MySQL-Router/mysql-router-community-8.0.34-1.el9.x86_64.rpm
                rpm -i mysql-router-community-8.0.34-1.el9.x86_64.rpm

.. Install-Section-Stop

.. Config-Section-Start

Configure MySQL Router
``````````````````````
    #. Bootstrap the cluster. (This will pull the config from the cluster and create a MySQL Router config file.)
     
        .. code-block:: bash

           mysqlrouter --bootstrap clusterAdmin@adb-5:3306 --account routeruser --user=mysqlrouter --disable-rest
           systemctl restart mysqlrouter

        You should get back a number of ports available to connect to.
        
        .. code-block:: 

            ## MySQL Classic protocol

            Read/Write Connections: localhost:6446
            Read/Only Connections:  localhost:6447

            ## MySQL X protocol

            Read/Write Connections: localhost:6448
            Read/Only Connections:  localhost:6449

      #. Restart mysqlrouter service.
     
        .. code-block:: bash

           systemctl restart mysqlrouter

    #. To confirm if MySQL Router is listening on the ports you can run.
     
        .. code-block:: bash

           sudo lsof -i -P -n | grep LISTEN | grep mysqlrout

.. Config-Section-Stop    
