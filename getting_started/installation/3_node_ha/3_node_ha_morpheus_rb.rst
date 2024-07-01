.. note::
   In the configuration below, the UID and GID for the users and groups are defined for services that will be embedded.  This ensures
   they are consistent on all nodes. If they are not consistent, the shared storage permissions can become out of sync and errors will
   appear for plugins, images, etc. If not specified, Morpheus will automatically find available UIDs/GIDs starting at 999 and work down.
   Availability of UIDs and GIDs can be seen by inspecting ``/etc/passwd`` and ``/etc/group`` respectively.  Change the UIDs and GIDs
   below based on what is available.

You can find additional configuration settings `here <https://docs.morpheusdata.com/en/latest/getting_started/additional/additional_configuration.html#advanced-morpheus-rb-settings>`_

.. content-tabs::

   .. tab-container:: tab1
      :title: Node 1

      .. code-block:: bash

         appliance_url 'https://morpheus.localdomain'
         elasticsearch['es_hosts'] = {'192.168.104.01' => 9200, '192.168.104.02' => 9200, '192.168.104.03' => 9200}
         elasticsearch['node_name'] = '192.168.104.01'
         elasticsearch['host'] = '0.0.0.0'
         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node01'
         mysql['enable'] = false
         mysql['host'] = {'127.0.0.1' => 6446}
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheus'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'
         user['uid'] = 899
         user['gid'] = 899
         # at the time of this writing, local_user is not valid as an option so the full entry is needed
         node.default['morpheus_solo']['local_user']['uid'] = 898
         node.default['morpheus_solo']['local_user']['gid'] = 898
         elasticsearch['uid'] = 896
         elasticsearch['gid'] = 896
         rabbitmq['uid'] = 895
         rabbitmq['gid'] = 895
         guacd['uid'] = 894
         guacd['gid'] = 894

   .. tab-container:: tab2
      :title: Node 2

      .. code-block:: bash

         appliance_url 'https://morpheus.localdomain'
         elasticsearch['es_hosts'] = {'192.168.104.01' => 9200, '192.168.104.02' => 9200, '192.168.104.03' => 9200}
         elasticsearch['node_name'] = '192.168.104.02'
         elasticsearch['host'] = '0.0.0.0'
         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node02'
         mysql['enable'] = false
         mysql['host'] = {'127.0.0.1' => 6446}
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheus'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'
         user['uid'] = 899
         user['gid'] = 899
         # at the time of this writing, local_user is not valid as an option so the full entry is needed
         node.default['morpheus_solo']['local_user']['uid'] = 898
         node.default['morpheus_solo']['local_user']['gid'] = 898
         elasticsearch['uid'] = 896
         elasticsearch['gid'] = 896
         rabbitmq['uid'] = 895
         rabbitmq['gid'] = 895
         guacd['uid'] = 894
         guacd['gid'] = 894

   .. tab-container:: tab3
      :title: Node 3

      .. code-block:: bash

         appliance_url 'https://morpheus.localdomain'
         elasticsearch['es_hosts'] = {'192.168.104.01' => 9200, '192.168.104.02' => 9200, '192.168.104.03' => 9200}
         elasticsearch['node_name'] = '192.168.104.03'
         elasticsearch['host'] = '0.0.0.0'
         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node03'
         mysql['enable'] = false
         mysql['host'] = {'127.0.0.1' => 6446}
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheus'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'
         user['uid'] = 899
         user['gid'] = 899
         # at the time of this writing, local_user is not valid as an option so the full entry is needed
         node.default['morpheus_solo']['local_user']['uid'] = 898
         node.default['morpheus_solo']['local_user']['gid'] = 898
         elasticsearch['uid'] = 896
         elasticsearch['gid'] = 896
         rabbitmq['uid'] = 895
         rabbitmq['gid'] = 895
         guacd['uid'] = 894
         guacd['gid'] = 894

.. note:: The configurations above for ```mysql['host']`` shows a list of hosts, if the database has multiple endpoints.  Like other options in the configuration, ``mysql['host']`` can be a single entry, if the database has a single endpoint:  ``mysql['host'] = 'myDbEndpoint.example.com`` or ``mysql['host'] = '10.100.10.111'``

.. important:: The elasticsearch node names set in ``elasticsearch['node_name']`` must match the host entries in elasticsearch['es_hosts']. ``node_name`` is used for ``node.name`` and ``es_hosts`` is used for ``cluster.initial_master_nodes`` in the generated elasticsearch.yml config. Node names that do not match entries in cluster.initial_master_nodes will cause clustering issues.

.. important:: The rabbitmq['node_name'] in the Node 1 example above is **rabbit@node01**.  The shortname for the server of node01 must be resolvable by DNS or /etc/hosts of all other hosts, same for node02 and node03.  FQDNs cannot be used here