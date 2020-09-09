Full HA Debian / Ubuntu Upgrade
```````````````````````````````

The following covers upgrading the |morpheus| App nodes in Full HA Architecture configurations to |morphver|.

.. important:: The following is only for Full HA Architecture configurations, where MySQL, Elasticsearch and RabbitMQ services are external to the App nodes.


|morpheus| Packages
...................
|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_ 


4.1.2+ -> |morphver| (rolling)
..............................
.. note:: All system services will automatically be stopped during the package install, and started during the reconfigure process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``. 
 
.. important:: Any externalized/non-system install services will not be stopped/started/upgraded/touched during package installs/upgrades or during reconfigures.

#. Upgrade the DEB package on Node 1, then run a Reconfigure on Node 1

   .. code-block:: bash

    [root@app-server-1 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-1 ~]# sudo dpkg -i morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-1 ~]# sudo morpheus-ctl reconfigure

#. Once Node 1 upgrade has completed and the u is available, upgrade the DEB package on Node 2, then run a Reconfigure on Node 2.

   .. code-block:: bash

    [root@app-server-2 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.de
    [root@app-server-2 ~]# sudo dpkg -i morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-2 ~]# sudo morpheus-ctl reconfigure

#. Then upgrade the DEB package and run a Reconfigure on Node 3.

   .. code-block:: bash

    [root@app-server-3 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.de
    [root@app-server-3 ~]# ssudo dpkg -i morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-3 ~]# sudo morpheus-ctl reconfigure

#. The upgrade is complete and the |morpheus|-ui services should be running across the 3 nodes.


4.0.0, 4.1.0, 4.1.1 -> |morphver| Upgrade
.........................................
* Elasticsearch 7.x is required for the external Elasticsearch cluster or services. Refer to `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ for upgrading external ES Clusters. The |morpheus| |morphver| package upgrade and reconfigure process will NOT upgrade external services.

#. Starting with Node 3, on All App Nodes, stop all Morpheus services via ``morpheus-ctl stop``. This will stop all system services. If any services timeout, run ``morpheus-ctl stop`` again.

   .. code-block:: bash

    [root@app-server-3 ~]# morpheus-ctl stop

   .. code-block:: bash

    [root@app-server-2 ~]# morpheus-ctl stop

   .. code-block:: bash

    [root@app-server-1 ~]# morpheus-ctl stop

#. Upgrade the deb package on Node 1, then run a Reconfigure on Node 1

   .. code-block:: bash

    [root@app-server-1 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-1 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-1 ~]# sudo morpheus-ctl reconfigure

   .. note::

   	All services will automatically start during the upgrade process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

#. Once Node 1 upgrade has completed and the u is available, upgrade the deb package on Node 2, then run a Reconfigure on Node 2.

   .. code-block:: bash

    [root@app-server-2 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-2 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-2 ~]# sudo morpheus-ctl reconfigure

#. Then upgrade the deb package on Node 3, then run a Reconfigure on Node 3

   .. code-block:: bash

    [root@app-server-3 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-3 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-3 ~]# sudo morpheus-ctl reconfigure

#. After all morpheus-ui services have finished loading, the upgrade is complete.


3.6.x -> |morphver| Upgrade
...........................
* MySQL 5.7.x is required for external MySQL clusters or services. Refer to `Percona Upgrade Documentation <https://www.percona.com/doc/percona-server/5.7/upgrading_guide_56_57.html>`_ for upgrading external Percona Clusters. The |morpheus| |morphver| package upgrade and reconfigure process will NOT upgrade external services.

* Elasticsearch 7.x is required for the external Elasticsearch cluster or services. Refer to `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ for upgrading external ES Clusters. The |morpheus| |morphver| package upgrade and reconfigure process will NOT upgrade external services.

* Existing 3.6.x RabbitMQ clusters are compatible with |morphver| and do not require an upgrade. On 3-Node configurations, the RabbitMQ queues and configuration will be dropped and the cluster will need to be configured and established again.
* The |morpheus| package repo download location has changed to https://downloads.morpheusdata.com from https://downloads.gomorpheus.com. Update firewall and proxy ACLs when applicable.

#. Starting with Node 3, on All App Nodes, stop all Morpheus services via ``morpheus-ctl stop``. This will stop all system services. If any services timeout, run ``morpheus-ctl stop`` again.

   .. code-block:: bash

    [root@app-server-3 ~]# morpheus-ctl stop

   .. code-block:: bash

    [root@app-server-2 ~]# morpheus-ctl stop

   .. code-block:: bash

    [root@app-server-1 ~]# morpheus-ctl stop

#. Upgrade the deb package on Node 1, then run a Reconfigure on Node 1

   .. code-block:: bash

    [root@app-server-1 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-1 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-1 ~]# sudo morpheus-ctl reconfigure

   .. note::

   	All services will automatically start during the upgrade process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

#. Once Node 1 upgrade has completed and the u is available, upgrade the deb package on Node 2, then run a Reconfigure on Node 2.

   .. code-block:: bash

    [root@app-server-2 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-2 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-2 ~]# sudo morpheus-ctl reconfigure

#. Then upgrade the deb package on Node 3, then run a Reconfigure on Node 3

   .. code-block:: bash

    [root@app-server-3 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-3 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-3 ~]# sudo morpheus-ctl reconfigure

#. After all morpheus-ui services have finished loading, the upgrade is complete.
