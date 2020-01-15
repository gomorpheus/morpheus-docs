3-Node HA Appliance Upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^^^

3-Node HA Appliance represent 3 App nodes with local RabbitMQ and Elasticsearch services clustered across the app nodes, and an external Galera or Percona MySQL cluster.

When upgrading a 3-Node appliance from 3.6.x to |morphver| the following services will be upgraded:

- RabbitMQ upgrade to v3.7
- Elasticsearch upgrade to v7.4

The upgrade process will not upgrade the external MySQL node(s). Refer to :ref:`compatibility` for externalized database version requirements.

Due to RabbitMQ going from 3.4 to 3.7, which has no rolling upgrade path, the RabbitMQ queues and configuration will be dropped, and the cluster will need to be configured and established again. This also ensures new queues are created using our new declaration settings, and removes any old queues not in use anymore.

.. important:: Due to the RabbitMQ upgrade from 3.4 to 3.7, the RabbitMQ configuration will be dropped and the cluster will need to be configured and established again.

CentOS / RHEL
`````````````
Applies to 3.6.x -> 4.0.x, 4.1.0 or 4.1.1

#. Starting with Node 3, on All App Nodes, stop all Morpheus services via ``morpheus-ctl stop``. This will stop all system services. If any services timeout, run ``morpheus-ctl stop`` again.
   
   .. code-block:: bash
    
    [root@app-server-3 ~]# morpheus-ctl stop
    
    .. code-block:: bash
    
    [root@app-server-2 ~]# morpheus-ctl stop
    
    .. code-block:: bash
    
    [root@app-server-1 ~]# morpheus-ctl stop

#. Upgrade the rpm package on Node 1, then run a Reconfigure on Node 1
  
   .. code-block:: bash

    [root@app-server-1 ~]# sudo wget https://packageUrl.morpheus-appliance-x.x.x-x.x86_64.rpm
    [root@app-server-1 ~]# sudo rpm -Uhv morpheus-appliance-x.x.x-x.x86_64.rpm
    [root@app-server-1 ~]# sudo morpheus-ctl reconfigure

#. Upgrade the rpm package on Node 2, then run a Reconfigure on Node 2

   .. code-block:: bash

    [root@app-server-2 ~]# sudo wget https://packageUrl.morpheus-appliance-x.x.x-x.x86_64.rpm
    [root@app-server-2 ~]# sudo rpm -Uhv morpheus-appliance-x.x.x-x.x86_64.rpm
    [root@app-server-2 ~]# sudo morpheus-ctl reconfigure

#. Upgrade the rpm package on Node 3, then run a Reconfigure on Node 3

   .. code-block:: bash

    [root@app-server-3 ~]# sudo wget https://packageUrl.morpheus-appliance-x.x.x-x.x86_64.rpm
    [root@app-server-3 ~]# sudo rpm -Uhv morpheus-appliance-x.x.x-x.x86_64.rpm
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

      This step will fail. This is ok, and expected. If the reconfigure hangs then use Ctrl+C to quit the reconfigure run and force a failure.

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
     
#. Next run a reconfigure on Nodes 2 & 3.

   .. code-block:: bash

    [root@app-server-2 ~] morpheus-ctl reconfigure
    [root@app-server-3 ~] morpheus-ctl reconfigure

#. You will be able to verify that the UI services have restarted properly by inspecting the logfiles. A standard practice after running a restart is to tail the UI log file.

   .. code-block:: bash

      root@app-server-2 ~]# morpheus-ctl tail morpheus-ui
