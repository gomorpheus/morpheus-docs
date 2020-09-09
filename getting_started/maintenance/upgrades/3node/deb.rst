3-Node HA Debian / Ubuntu Upgrade
`````````````````````````````````
The following covers upgrading the |morpheus| App nodes in 3 Node HA configurations to |morphver|.

.. important:: The following is only for "3 Node HA" Architecture configurations.

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

#. The upgrade is complete and the |morpheus|-ui services should be running with clustered Elasticsearch and RabbitMQ services across the 3 nodes.


4.0.0, 4.1.0, 4.1.1 -> |morphver| Upgrade
.........................................
* Elasticsearch will be upgraded from 5.6 to 7.2.

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

#. Once Node 1 upgrade has completed and the ui is available, upgrade the deb package on Node 2, then run a Reconfigure on Node 2.

   .. code-block:: bash

    [root@app-server-2 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-2 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-2 ~]# sudo morpheus-ctl reconfigure

#. Then upgrade the deb package and run a Reconfigure on Node 3

   .. code-block:: bash

    [root@app-server-3 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-3 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-3 ~]# sudo morpheus-ctl reconfigure

#. The upgrade is complete and the |morpheus|-ui services should be running with clustered Elasticsearch and RabbitMQ services across the 3 nodes.


3.6.x -> |morphver| Upgrade
...........................
* RabbitMQ will be upgraded from 3.5 to 3.7. On 3-Node configurations, the RabbitMQ queues and configuration will be dropped and the cluster will need to be configured and established again.
* Elasticsearch will be upgraded from 5.6 to 7.2. Refer to `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ for upgrading external ES Clusters.
* Stop all morpheus services, not just the morpheus-ui, before the upgrade. Although the upgrade process will also stop the services, take this step to ensure they are stopped.
* Warnings about missing files during the removal phase are expected and can be ignored.
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

#. Upgrade the deb package on Node 2, then run a Reconfigure on Node 2

   .. code-block:: bash

    [root@app-server-2 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-2 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-2 ~]# sudo morpheus-ctl reconfigure

#. Upgrade the deb package on Node 3, then run a Reconfigure on Node 3

   .. code-block:: bash

    [root@app-server-3 ~]# sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
    [root@app-server-3 ~]# sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
    [root@app-server-3 ~]# sudo morpheus-ctl reconfigure

#. After reconfigure has completed on Node 1, apply the required ``ha-mode`` and ``expires`` policies to the morpheus vhost:

   .. code-block:: bash

    [root@app-server-1 ~] source /opt/morpheus/embedded/rabbitmq/.profile
    [root@app-server-1 ~] rabbitmqctl set_policy -p morpheus --apply-to queues --priority 2 statCommands "statCommands.*" '{"expires":1800000, "ha-mode":"all"}'
    [root@app-server-1 ~] rabbitmqctl set_policy -p morpheus --apply-to queues --priority 2 morpheusAgentActions "morpheusAgentActions.*" '{"expires":1800000, "ha-mode":"all"}'
    [root@app-server-1 ~] rabbitmqctl set_policy -p morpheus --apply-to queues --priority 2 monitorJobs "monitorJobs.*" '{"expires":1800000, "ha-mode":"all"}'
    [root@app-server-1 ~] rabbitmqctl set_policy -p morpheus --apply-to all --priority 1 ha ".*" '{"ha-mode":"all"}'

   .. important:: Failure to set the proper policies will result in degraded RabbitMQ performance, Java Heap issues, and/or refused RabbitMQ connections resulting in degraded |morpheus| UI performance, unconsumed messages or UI failure.

#. After reconfigure has completed on Nodes 2 and 3, stop the morpheus-ui service that was automatically started during the reconfigure process.

   .. code-block:: bash

      [root@app-server-2 ~]# morpheus-ctl stop morpheus-ui

   .. code-block:: bash

      [root@app-server-1 ~]# morpheus-ctl stop morpheus-ui

#. Copy the secrets and erlang cookie from Node 1 to Nodes 2 and 3

   Begin by copying secrets from the Node 1 other nodes.

   .. code-block:: bash

    [root@app-server-3 ~]# cat /etc/morpheus/morpheus-secrets.json

     "rabbitmq": {
       "morpheus_password": "***REDACTED***",
       "queue_user_password": "***REDACTED***",
       "cookie": "***REDACTED***"
     },

   Then copy the erlang.cookie from the Node 1 to Nodes 2 and 3

   .. code-block:: bash

     [root@app-server-1 ~]# cat /opt/morpheus/embedded/rabbitmq/.erlang.cookie

     # 754363AD864649RD63D28

#. Once this is done run a reconfigure on Nodes 2 & 3.

   .. code-block:: bash

       [root@app-server-2 ~] morpheus-ctl reconfigure

   .. NOTE::

      If the reconfigure fails or hangs it is ok. If the reconfigure hangs then use Ctrl+C to quit the reconfigure run and force a failure. Another reconfigure will be run after clustering.

#. Next on Node 2, ensure the ui is stopped, then stop and start RabbitMQ and join the Node to the Cluster. Do not stop and start RabbitMQ on Node 1.

   .. IMPORTANT:: The commands below must be run at root

   .. code-block:: bash

     [root@app-server-1 ~]# morpheus-ctl stop morpheus-ui
     [root@app-server-2 ~]# morpheus-ctl stop rabbitmq
     [root@app-server-2 ~]# morpheus-ctl start rabbitmq
     [root@app-server-2 ~]# source /opt/morpheus/embedded/rabbitmq/.profile
     [root@app-server-2 ~]# rabbitmqctl stop_app

     Stopping node 'rabbit@app-server-2' ...

     [root@app-server-2 ~]# rabbitmqctl join_cluster rabbit@app-server-1

     Clustering node 'rabbit@app-server-2' with 'rabbit@app-server-1' ...

     [root@app-server-2 ~]# rabbitmqctl start_app

     Starting node 'rabbit@app-server-2' ...

#. Perform the same steps on Node 3 to join the Node to the Cluster. Again, do not stop and start RabbitMQ on Node 1.

   .. IMPORTANT:: The commands below must be run at root

   .. code-block:: bash

     [root@app-server-3 ~]# morpheus-ctl stop rabbitmq
     [root@app-server-3 ~]# morpheus-ctl start rabbitmq
     [root@app-server-3 ~]# source /opt/morpheus/embedded/rabbitmq/.profile
     [root@app-server-3 ~]# rabbitmqctl stop_app

     Stopping node 'rabbit@app-server-3' ...

     [root@app-server-3 ~]# rabbitmqctl join_cluster rabbit@app-server-1

     Clustering node 'rabbit@app-server-3' with 'rabbit@app-server-1' ...

     [root@app-server-3 ~]# rabbitmqctl start_app

     Starting node 'rabbit@app-server-3' ...

#. Next run a final reconfigure on Nodes 2 & 3 and start the |morpheus| ui.

   .. code-block:: bash

    [root@app-server-2 ~] morpheus-ctl reconfigure
    [root@app-server-2 ~] morpheus-ctl start morpheus-ui

    [root@app-server-3 ~] morpheus-ctl reconfigure
    [root@app-server-3 ~] morpheus-ctl start morpheus-ui

#. You will be able to verify that the UI services have restarted properly by inspecting the logfiles. A standard practice after running a restart is to tail the UI log file.

   .. code-block:: bash

      root@app-server-2 ~]# morpheus-ctl tail morpheus-ui

|
|
