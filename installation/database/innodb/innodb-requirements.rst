Requirements
````````````

Ensure the firewall (or security group) allows MySQL and InnoDB traffic ``inbound``:

  .. important::
    The installation script will open the firewall ports automatically.  However, these commands are here as reference in case they are needed.

  - MySQL Port (From |morpheus|)

    - 3306

  - InnoDB Ports (From |morpheus|)
  
    - 33060 (MySQL Client to Server – New X Protocol)
    - 33062 (admin_port)

  - InnoDB Ports (Between InnoDB Nodes)
    
    - 33061 (MySQL Group Replication internal communications port)

  Example commands to run in the OS, if needed.  Usually, in public clouds, the firewall is **not** enabled and this is not required.


  

    .. tabs::

      .. group-tab:: RHEL 8/9

        .. code-block:: bash

          firewall-cmd --zone=public --add-port={3306/tcp,33060/tcp,33061/tcp,33062/tcp} --permanent
          firewall-cmd --reload
                      
      .. group-tab:: Ubuntu

          .. code-block:: bash

            ufw allow 3306,33060,33061,33062/tcp

.. important::
    Verify DNS resolution of DNS names for all DB nodes.  Note that by default, InnoDB will use the hostname FQDN returned from the OS, not an alias you specify. 
    It is important that all expected names can be resolved properly.  Edit ``/etc/hosts`` if needed and/or use ``hostnamectl set-hostname <name>`` to modify the hostname.

.. important::
    Run all scripts as ``root`` to avoid any issues with elevation.  Example:  ``sudo -s``