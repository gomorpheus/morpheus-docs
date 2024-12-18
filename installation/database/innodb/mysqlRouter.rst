MySQL Router
============

Introduction
^^^^^^^^^^^^

MySQL Router is lightweight middleware that provides transparent routing between your 
application and any backend MySQL Servers. This router can run directly on the application 
nodes and be bootstrapped from the MySQL cluster.  

Download MySQL Routere from: https://dev.mysql.com/downloads/router/

Official Documentation: https://dev.mysql.com/doc/mysql-router/8.0/en/

The Default location of a bootstrapped mysqlrouter config file is: /etc/mysqlrouter/mysqlrouter.conf

.. Install-Section-Start

Install MySQL Router
^^^^^^^^^^^^^^^^^^^^

Install by Repository
`````````````````````

`MySQL Documentation <https://dev.mysql.com/doc/mysql-router/8.0/en/mysql-router-installation-linux.html>`_ 

  - Locate the current respoitory files needed.  The installation example below may be outdated but the links/versions can be found here:
    
    - `YUM/DNF MySQL Repositories <https://dev.mysql.com/downloads/repo/yum/>`_
    - `APT MySQL Repositories <https://dev.mysql.com/downloads/repo/apt/>`_
  
  - Install Repository

    .. note::
        Below is the automated method of installing the repo for a specific version.  Should you use the incorrect version by accident and you need to change
        it to a different one after installing the repo, the ``dpkg-reconfigure mysql-apt-config`` command can be used with an interactive
        GUI.  Be sure to ``unset DEBIAN_FRONTEND`` prior or you will not see the GUI.

    .. tabs::

        .. group-tab:: Ubuntu

            .. code-block:: bash
        
                # Example: mysql-8.0, mysql-5.7, mysql-8.4-lts
                mySqlRepo=mysql-8.0
                export DEBIAN_FRONTEND=noninteractive
                echo mysql-apt-config mysql-apt-config/enable-repo select $mySqlRepo | sudo debconf-set-selections
                echo mysql-apt-config mysql-apt-config/select-server select $mySqlRepo | sudo debconf-set-selections
                curl https://repo.mysql.com/mysql-apt-config_0.8.33-1_all.deb -o mysql-apt.deb
                dpkg -i mysql-apt.deb
                unset DEBIAN_FRONTEND
                apt update
                        
        .. group-tab:: RHEL 9

            .. code-block:: bash

                curl https://repo.mysql.com//mysql80-community-release-el9-5.noarch.rpm -o mysql-yum.rpm
                rpm -ihv mysql-yum.rpm
        
        .. group-tab:: RHEL 8

            .. code-block:: bash

                curl https://repo.mysql.com//mysql80-community-release-el8-9.noarch.rpm -o mysql-yum.rpm
                rpm -ihv mysql-yum.rpm

  - Install MySQL Router

    .. IMPORTANT:: Make sure to pin the package to prevent accidental upgrades.

    .. tabs::

        .. group-tab:: Ubuntu

            .. code-block:: bash
        
                apt install mysql-router-community -y

                # Pin version 
                sudo apt-mark hold mysql-router-community
                apt-mark showhold
                        
        .. group-tab:: RHEL

            .. code-block:: bash

                yum install mysql-router-community -y

                # Pin version 
                sudo echo "exclude=mysql*" | sudo tee -a /etc/yum.conf

Install by Download
```````````````````
    
    .. toggle-header::
        :header: **Install by Download**
        
        - The example below may be outdated but the links/versions can be found here:
            - `YUM/DNF MySQL Repositories <https://dev.mysql.com/downloads/>`_

        .. tabs::

            .. group-tab:: Ubuntu 22.04

                .. code-block:: bash
            
                    wget https://dev.mysql.com/get/Downloads/MySQL-Router/mysql-router-community_8.0.34-1ubuntu22.04_amd64.deb
                    dpkg -i mysql-router-community_8.0.34-1ubuntu22.04_amd64.deb
                            
            .. group-tab:: RHEL 9
                    
                .. code-block:: bash
                    
                    wget https://dev.mysql.com/get/Downloads/MySQL-Router/mysql-router-community-8.0.34-1.el9.x86_64.rpm
                    rpm -i mysql-router-community-8.0.34-1.el9.x86_64.rpm

.. Install-Section-Stop

.. Config-Section-Start

Configure MySQL Router
^^^^^^^^^^^^^^^^^^^^^^

        Bootstrap the cluster. (This will pull the config from the cluster and create a MySQL Router config file.)
        **Before running this make sure you created the router user with mysqlsh in the previous steps.  This is also contained in the .js scripts**
     
        .. code-block:: bash

           mysqlrouter --bootstrap clusterAdmin@adb-5:3306 --account routeruser --user=mysqlrouter --disable-rest

        You should get back a number of ports available to connect to.
        
        .. code-block:: 

            ## MySQL Classic protocol

            Read/Write Connections: localhost:6446
            Read/Only Connections:  localhost:6447

            ## MySQL X protocol

            Read/Write Connections: localhost:6448
            Read/Only Connections:  localhost:6449

        Enable and Restart mysqlrouter service.
     
        .. code-block:: bash

           systemctl restart mysqlrouter
           systemctl enable mysqlrouter

        To confirm if MySQL Router is listening on the ports you can run.
     
        .. code-block:: bash

           sudo lsof -i -P -n | grep LISTEN | grep mysqlrout

.. Config-Section-Stop    