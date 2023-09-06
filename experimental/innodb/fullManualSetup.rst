MySQL InnoDB Cluster MultiSite Full Install 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prupose of this document is to provide to the end to end manual steps to prepare and configure an
InnoDB multi site cluster.

#. Disable AppArmor/SELinux.

    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                systemctl stop apparmor
                systemctl disable apparmor
                reboot
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash
                

#. Install MySQL on Each DB Node.

    .. tabs::

        .. group-tab:: Ubuntu 22.04

            .. code-block:: bash
        
                apt update
                apt install mysql-server
                        
        .. group-tab:: RHEL 8/9

            .. code-block:: bash


 #. Configure MySQL on Each DB Node. Logon to MySQL for the following commands.
     
    #. (Optional) Change MySQL Root to use password.

        .. code-block:: bash

           ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'P@ssw0rd!';

    #. Set global MySQL invisible primary. This is required to support Morpheus tables without primary keys.     
         
        .. code-block:: bash

           set persist sql_generate_invisible_primary_key=1;

    #. Check the global MySQL properties to confirm invisible primary key is on.     
        
        .. code-block:: bash

           SHOW GLOBAL VARIABLES LIKE 'sql_generate_invisible_primary_key';

    #. Create an Admin account to be used with MySQl Shell     
        
        .. code-block:: bash

           CREATE USER 'clusterAdmin'@'%' IDENTIFIED BY 'P@ssw0rd!';
           GRANT ALL PRIVILEGES ON *.* TO 'clusterAdmin'@'%' with grant option;

    #. Update the MySQL config to listen on external address.    
        
        .. code-block:: bash

           vi /etc/mysql/mysql.conf.d/mysqld.cnf
           
        bind-address            = 127.0.0.1,192.168.100.67
