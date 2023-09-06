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
                
                