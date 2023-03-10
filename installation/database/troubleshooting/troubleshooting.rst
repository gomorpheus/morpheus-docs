.. _db-troubleshooting:

Troubleshooting
===============

SELinux Issues
^^^^^^^^^^^^^^

Creating a profile
``````````````````

* Install the tools

   * yum install policycoreutils-python-utils

* Have SELinux in ``permissive`` mode
* Run through all tasks to create the denied messages
* Run this command to grab the entries from the log and create a policy file
    
    .. code-block:: bash

        grep -i denied /var/log/audit/audit.log | grep mysqld_t | audit2allow -M PXC
    
    This will create 2 files a ``PXC.pp`` and a ``PXC.te`` The ``PXC.te`` is a human readble version of the ``PXC.pp`` policy file

* Run this command to make this policy active

    .. code-block:: bash
        
        semodule -i PXC.pp

Create or update an existing config
```````````````````````````````````

* Create/edit your ``PXC.te`` file with the config
* Run the following commands
    
    .. code-block::

        checkmodule -M -m -o PXC.mod PXC.te
        semodule_package -o PXC.pp -m PXC.mod
        semodule -i PXC.pp

Additional Info
```````````````

* SELinux file location

    ``/etc/selinux/targeted/policy``

* Helpful commands
    
    * Will list all loaded modules. Custom modules display at the top

        .. code-block:: bash
            
            semodule -l

    * Check policy type

        .. code-block:: bash
            
            sestatus | grep Loaded 

    * Disable a policy

        .. code-block:: bash

            semodule -d

    * Remove a module

        .. code-block:: bash

            semodule -r

    * Enable a module

        .. code-block:: bash

            semodule -e