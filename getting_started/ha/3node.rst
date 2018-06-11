3 Node with Externalized DB Configuration
-----------------------------------------

Assumptions
^^^^^^^^^^^^

This guide assumes the following:

- There is an externalized database running for Morpheus to access.
- The database service is a MySQL dialect (MySQL, MariaDB, Galera, etc...)
- A database has been created for Morpheus as well as a user and proper grants have been run for the user. Morpheus will create the schema.
- The baremetal nodes cannot access the public internet
- The base OS is RHEL 7.x
- Shortname versions of hostnames will be resolvable
- All nodes have access to a shared volume for /var/opt/morpheus/morpheus-ui. This can be done as a post startup step.
- This configuration will support the complete loss of a single node, but no more.  Specifically the Elasticsearch tier requires at least two nodes to always be clustered..

Steps
^^^^^

#. First begin by downloading the requisite Morpheus packages either to the nodes or to your workstation for transfer. These packages need to be made available on the nodes you wish to install Morpheus on.

   .. code-block:: bash

  [root@app-server-1 ~]# wget https://downloads.gomorpheus.com/yum/el/7/noarch/morpheus-appliance-offline-3.1.5- 1.noarch.rpm
  [root@app-server-1 ~]# wget https://downloads.gomorpheus.com/yum/el/7/x86_64/morpheus-appliance-3.1.5- 1.el7.x86_64.rpm

#. Once the packages are available on the nodes they can be installed. Make sure that no steps beyond the rpm install are run.

   .. code-block:: bash

  [root@app-server-1 ~]# rpm -i morpheus-appliance-3.1.5-1.el7.x86_64.rpm
  [root@app-server-1 ~]# rpm -i morpheus-appliance-offline-3.1.5-1.noarch.rpm

#. Next you will need to edit the Morpheus configuration file on each node.

   Node 1

   .. code-block:: bash

   appliance_url 'https://esmort01.qcorpaa.aa.com'
   elasticsearch['es_hosts'] = {'10.130.2.1' => 9300, '10.130.2.2' => 9300, '10.130.2.3' => 9300} elasticsearch['node_name'] = 'morpheus1'
   elasticsearch['host'] = '0.0.0.0'
   rabbitmq['host'] = '0.0.0.0'
   rabbitmq['nodename'] = 'rabbit@esmort01'
   mysql['enable'] = false
   mysql['host'] = '10.130.12.228'
   mysql['morpheus_db'] = 'morpheusdb'
   mysql['morpheus_db_user'] = 'morpheus'
   mysql['morpheus_password'] = 'password'

   Node 2

   .. code-block:: bash

   appliance_url 'https://esmort02.qcorpaa.aa.com'
    elasticsearch['es_hosts'] = {'10.130.2.2' => 9300, '10.130.2.1' => 9300, '10.130.2.3' => 9300} elasticsearch['node_name'] = 'morpheus2'
    elasticsearch['host'] = '0.0.0.0'
    rabbitmq['host'] = '0.0.0.0'
    rabbitmq['nodename'] = 'rabbit@esmort02'
    mysql['enable'] = false
    mysql['host'] = '10.130.12.228'
    mysql['morpheus_db'] = 'morpheusdb'
    mysql['morpheus_db_user'] = 'morpheus'
    mysql['morpheus_password'] = 'password’

   Node 3

   .. code-block:: bash

    appliance_url 'https://esmort03.qcorpaa.aa.com'
     elasticsearch['es_hosts'] = {'10.130.2.3' => 9300, '10.130.2.2' => 9300, '10.130.2.1' => 9300} elasticsearch['node_name'] = 'morpheus3'
     elasticsearch['host'] = '0.0.0.0'
     rabbitmq['host'] = '0.0.0.0'
     rabbitmq['nodename'] = 'rabbit@esmort03'
     mysql['enable'] = false
     mysql['host'] = '10.130.12.228'
     mysql['morpheus_db'] = 'morpheusdb'
     mysql['morpheus_db_user'] = 'morpheus'
     mysql['morpheus_password'] = 'password’


  .. Note :: If you are running MySQL in a Master/Master configuration we will need to slightly alter the mysql['host'] line in the morpheus.rb to account for both masters in a failover configuration. As an example:



#. Run the reconfigure on all nodes

   .. code-block:: bash

      [root@app-server-1 ~] morpheus-ctl reconfigure

   Morpheus will come up on all nodes and Elasticsearch will auto-cluster.

#. The only item left is the manual clustering of RabbitMQ. Select one of the nodes to be your Source Of Truth (SOT) for RabbitMQ clustering. We need to share secrets for RabbitMQ, the erlang cookie and join the other nodes to the SOT node.

   Begin by copying secrets from the SOT node to the other nodes.

   .. code-block:: bash

      [root@app-server-1 ~] cat /etc/morpheus/morpheus-secrets.json
      {
        "mysql": {
          "root_password": "wam457682b67858ae2cf4bc",
          "morpheus_password": "password",
          "ops_password": "98d9677686698d319r6356ae3a77"
        },
        "rabbitmq": {
          "morpheus_password": "adff00cf8714b25mc",
          "queue_user_password": "r075f26158c1fes2",
          "cookie": "6458933CD86782AD39E25"
        },
        "vm-images": {
          "s3": {
            "aws_access_id": "AKIAI6OFPBN4NWSFBXRQ",
            "aws_secret_key": "a9vxxjH5xkgh6dHgRjLl37i33rs8pwRe3"
         }
        }
       }

#. Then copy the erlang.cookie from the SOT node to the other nodes

   .. code-block:: bash

     [root@app-server-1 ~] cat /opt/morpheus/embedded/rabbitmq/.erlang.cookie
     # 754363AD864649RD63D28

#. Once this is done run a reconfigure on the two nodes that are NOT the SOT nodes.

   .. code-block:: bash

    [root@app-server-2 ~] morpheus-ctl reconfigure

   .. NOTE:: This step will fail. This is ok, and expected. If the reconfigure hangs then use Ctrl+C to quit the reconfigure run and force a failure.

#. Subsequently we need to stop and start Rabbit on the NOT SOT nodes.

   .. code-block:: bash

     [root@app-server-2 ~] morpheus-ctl stop rabbitmq
     [root@app-server-2 ~] morpheus-ctl start rabbitmq

#. After this has been completed we can ensure our scripts and binaries are in our path for manual joining. This is done on both of the NOT SOT nodes.

   .. code-block:: bash

     [root@app-server-2 ~] PATH=/opt/morpheus/sbin:/opt/morpheus/sbin:/opt/morpheus/embedded/sbin:/opt/morpheus/embedded/bin:$PATH

#. Then we will stop the Rabbit service within the Erlang VM and cluster the Rabbit nodes on the two nodes that are NOT the SOT node.

   .. code-block:: bash

     [root@app-server-2 ~] rabbitmqctl stop_app
     # Stopping node 'rabbit@app-server-2' ...
     [root@app-server-2 ~] rabbitmqctl join_cluster rabbit@app-server-1
     # Clustering node 'rabbit@app-server-2' with 'rabbit@app-server-1' ...
     [root@app-server-2 ~] rabbitmqctl start_app
     # Starting node 'rabbit@app-server-2' ...

#. The last thing to do is restart the Morpheus UI on the two nodes that are NOT the SOT node.

   .. code-block:: bash

     [root@app-server-2 ~] morpheus-ctl restart morpheus-ui

#. If this command times out then run:

   .. code-block:: bash

    [root@app-server-2 ~] morpheus-ctl kill morpheus-ui
    [root@app-server-2 ~] morpheus-ctl start morpheus-ui

#. You will be able to verify that the UI services have restarted properly by inspecting the logfiles. A standard practice after running a restart is to tail the UI log file.

   .. code-block:: bash

    [root@app-server-2 ~] morpheus-ctl tail morpheus-ui

#. For moving /var/opt/morpheus/morpheus-ui files into a shared volume make sure ALL Morpheus services on ALL three nodes are down before you begin.

   .. code-block:: bash

    [root@app-server-1 ~] morpheus-ctl stop

.. IMPORTANT:: Permissions are as important as is content, so make sure to preserve directory contents to the shared volume. Subsequently you can start all Morpheus services on all three nodes and tail the Morpheus UI log file to inspect errors.
