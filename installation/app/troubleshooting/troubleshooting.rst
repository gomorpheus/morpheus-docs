Troubleshooting
===============

Ubuntu Unattended Upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^

    **Issue**

        When attempting to install |morpheus| using dpkg, the following error may be seen:

            ``root@app:~# dpkg -i /home/kgawronski/morpheus-appliance_5.5.3-1_amd64.deb
            dpkg: error: dpkg frontend lock was locked by another process with pid ####
            Note: removing the lock file is always wrong, and can end up damaging the
            locked area and the entire system. See <https://wiki.debian.org/Teams/Dpkg/FAQ>.``
    
    **Resolution**

        It is a common issue for newly created systems.  If configured, Ubuntu will automatically start an upgrade, which can lock the installation from proceeding.
        Unfortuantely, it is best to wait for the process to finish before continuing, other the apt database can become corrupt.

        Use the following commands to check when it is complete.  Once complete, the entry should no longer show:

            .. code:: bash

                ps -aux | grep <PID_mentioned>

                # Example output:
                root **3535** 11.1 0.9 324516 162600 ? Sl 13:24 1:54 /usr/bin/python3 **/usr/bin/unattended-upgrade**

    Additional info:

        https://help.ubuntu.com/community/AutomaticSecurityUpdates

Public Key Retrieval is not allowed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **Issue**

        When attempting to do a ``moprheus-ctl reconfigure`` with an external database configured, the following error may be seen:

            ``java.sql.SQLNonTransientConnectionException: Public Key Retrieval is not allowed``
        
    **Resolution**

        Newer verisons of mysql have a public key configured, which the client needs to request.  This can be resolved by setting use_tls to true in the morpheus.rb file:

            .. code:: bash

                echo "mysql['use_tls'] = true" | sudo tee -a /etc/morpheus/morpheus.rb

        Alternatively, a custom JDBC string can be configured in the ``morpheus.rb`` file and adding ``allowPublicKeyRetrieval=true``

    Additional info:
    
        https://docs.morpheusdata.com/en/latest/getting_started/additional/morpheusRb.html
        
        https://stackoverflow.com/questions/50379839/connection-java-mysql-public-key-retrieval-is-not-allowed

vm.max_map_count is too low
^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **Issue**

        When attempting to do a ``moprheus-ctl reconfigure``, the following error may be seen:

            ``max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]``
        
    **Resolution**

        Some OSs, specicially Amazon Linux 2, will present this error and can prevent services from starting, such as Elasticsearch.  To resolve this error, run the following to increase thge vm.max_map_count:

            .. code:: bash

                sysctl -w vm.max_map_count=262144
                echo 'vm.max_map_count = 262144' | sudo tee -a /etc/sysctl.conf

        The first command will change it immediately.  However, after a reboot the setting will be lost, so the ``sysctl.conf`` file needs to be modified.

    Additional info:
    
        https://stackoverflow.com/questions/51445846/elasticsearch-max-virtual-memory-areas-vm-max-map-count-65530-is-too-low-inc