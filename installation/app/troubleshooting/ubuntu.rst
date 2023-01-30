Troubleshooting
^^^^^^^^^^^^^^^

**Issue**

    When attempting to install Morpheus using dpkg, the following error may be seen:

        ``root@app:~# dpkg -i /home/kgawronski/morpheus-appliance_5.5.3-1_amd64.deb
        dpkg: error: dpkg frontend lock was locked by another process with pid ####
        Note: removing the lock file is always wrong, and can end up damaging the
        locked area and the entire system. See <https://wiki.debian.org/Teams/Dpkg/FAQ>.``
    
**Resolution**

    It is a common issue for newly created systems.  IF configured, Ubuntu will automatically start an upgrade, which can lock the installation from proceeding.
    Unfortuantely, it is best to wait for the process to finish before continuing.

    Usethe following commands to check when it is complete.  Once complete, the entry should no longer show:

        .. code:: bash

            root@app: ~# ps -aux | grep <PID_mentioned>

            # Example output:
            root **3535** 11.1 0.9 324516 162600 ? Sl 13:24 1:54 /usr/bin/python3 **/usr/bin/unattended-upgrade**