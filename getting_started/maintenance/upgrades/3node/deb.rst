3-Node HA Debian / Ubuntu Upgrade
`````````````````````````````````
The following covers upgrading the |morpheus| App nodes in 3 Node HA configurations to |morphver|.

.. warning:: As a best practice, always backup your database prior to any upgrade.

.. important:: The following is only for "3 Node HA" Architecture configurations.

|morpheus| Packages
...................
|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_

|nonRollingUpgradeVer| or lower -> |morphver| Upgrade
.....................................................

.. warning:: Rolling upgrades from |nonRollingUpgradeVer| or lower to |morphver| are not supported

.. important:: It is important to stop the morpheus-ui service on all app nodes prior to upgrade. Failure to do so will resilt in a flood of log errors due to previous message serializaiton conflict. The messages will eventually expire and the logs will clear.

.. warning:: |morpheus| |morphver| contains new node and VM node packages that require 3.5GB of storage. It is safe to run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after |morphver| package installation and before reconfigure to clean old node and vm node packages from the package-repo when room is needed.

#. Starting with Node 3, on **All** App Nodes, stop the morpheus-ui services via ``morpheus-ctl stop morpheus-ui``. If you receive a timeout, run ``morpheus-ctl graceful-kill morpheus-ui``.

   .. code-block:: bash

    [root@app-server-3 ~]# morpheus-ctl stop morpheus-ui

   .. code-block:: bash

    [root@app-server-2 ~]# morpheus-ctl stop morpheus-ui

   .. code-block:: bash

    [root@app-server-1 ~]# morpheus-ctl stop morpheus-ui

#. Upgrade the deb package on Node 1, then run a Reconfigure on Node 1

   .. code-block:: bash

    [root@app-server-1 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-1 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-1 ~]# sudo morpheus-ctl reconfigure

   .. note::	All services will automatically be stopped and started during the reconfigure process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

#. Once Node 1 upgrade has completed and the ui is available, upgrade the deb package on Node 2, then run a Reconfigure on Node 2.

   .. code-block:: bash

    [root@app-server-2 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-2 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-2 ~]# sudo morpheus-ctl reconfigure

#. Then upgrade the deb package on Node 3, and run a Reconfigure on Node 3

   .. code-block:: bash

    [root@app-server-3 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-3 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-3 ~]# sudo morpheus-ctl reconfigure

#. The upgrade is complete and the |morpheus|-ui services should be running with clustered Elasticsearch and RabbitMQ services across the 3 nodes.

.. important:: If reconfigure after a rpm package upgrade stalls or hangs on starting a service (mysql, rabbitmq, elasticsearch ...) it is possible the ``morpheus-runsvdir`` service did not start or a process it was managing was manually shutdown or killed. To resolve, run ``systemctl stop morpheus-runsvdir`` then ``systemctl start morpheus-runsvdir``, then run reconfigure again, ``morpheus-ctl reconfigure``.

|

|minRollingUpgradeVer| -> |morphver| Upgrade
............................................

.. NOTE:: Rolling upgrades are supported for |minRollingUpgradeVer| -> |morphver| only.

.. warning:: |morpheus| |morphver| contains new node and VM node packages that require 3.5GB of storage. It is safe to run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after |morphver| package installation and before reconfigure to clean old node and vm node packages from the package-repo when room is needed.

#. Upgrade the deb package on Node 1, then run a Reconfigure on Node 1

   .. code-block:: bash

    [root@app-server-1 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-1 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-1 ~]# sudo morpheus-ctl stop morpheus-ui
    [root@app-server-1 ~]# sudo morpheus-ctl reconfigure
    [root@app-server-1 ~]# sudo morpheus-ctl start morpheus-ui

   After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``. Once morpheus-ui is started, proceed to the next node.

#. Once Node 1 upgrade has completed and the ui is available, upgrade the deb package on Node 2, then run a Reconfigure on Node 2.

   .. code-block:: bash

    [root@app-server-2 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-2 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-2 ~]# sudo morpheus-ctl stop morpheus-ui
    [root@app-server-2 ~]# sudo morpheus-ctl reconfigure
    [root@app-server-2 ~]# sudo morpheus-ctl start morpheus-ui

   After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``. Once morpheus-ui is started, proceed to the next node.

#. Once Node 2 upgrade has completed and the ui is available, upgrade the deb package on Node 3, and run a Reconfigure on Node 3

   .. code-block:: bash

    [root@app-server-3 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-3 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-3 ~]# sudo morpheus-ctl stop morpheus-ui
    [root@app-server-3 ~]# sudo morpheus-ctl reconfigure
    [root@app-server-3 ~]# sudo morpheus-ctl start morpheus-ui


   After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

#. The upgrade is complete and the |morpheus|-ui services should be running with clustered Elasticsearch and RabbitMQ services across the 3 nodes.

.. important:: If reconfigure after a rpm package upgrade stalls or hangs on starting a service (mysql, rabbitmq, elasticsearch ...) it is possible the ``morpheus-runsvdir`` service did not start or a process it was managing was manually shutdown or killed. To resolve, run ``systemctl stop morpheus-runsvdir`` then ``systemctl start morpheus-runsvdir``, then run reconfigure again, ``morpheus-ctl reconfigure``.
