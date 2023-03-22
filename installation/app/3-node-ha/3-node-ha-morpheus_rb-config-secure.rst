.. note::
   In the configuration below, the UID and GID for the users and groups are defined for services that will be embedded.  This ensures
   they are consistent on all nodes. If they are not consistent, the shared storage permissions can become out of sync and errors will
   appear for plugins, images, etc. If not specified, Morpheus will automatically find available UIDs/GIDs starting at 999 and work down.
   Availabililty of UIDs and GIDs can be seen by inspecting ``/etc/passwd`` and ``/etc/group`` respectively.  Change the UIDs and GIDs
   below based on what is available.

.. content-tabs::

   .. tab-container:: tab1
      :title: Node 1

      .. code-block:: bash

         appliance_url 'https://morpheus.localdomain'
         elasticsearch['es_hosts'] = {'192.168.104.01' => 9200, '192.168.104.02' => 9200, '192.168.104.03' => 9200}
         elasticsearch['node_name'] = '192.168.104.01'
         elasticsearch['host'] = '0.0.0.0'
         elasticsearch['secure_mode'] = true
         elasticsearch['use_tls'] = true
         elasticsearch['truststore_path'] = '/var/opt/morpheus/certs/elastic-stack-ca.p12
         elasticsearch['truststore_password'] = 'truststore_path_password'
         elasticsearch['morpheus_password'] = 'morpheusEsUserPassword'
         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node01'
         mysql['enable'] = false
         mysql['host'] = {'192.168.101.01' => 3306, '192.168.101.02' => 3306, '192.168.101.03' => 3306}
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
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
         elasticsearch['secure_mode'] = true
         elasticsearch['use_tls'] = true
         elasticsearch['truststore_path'] = '/var/opt/morpheus/certs/elastic-stack-ca.p12
         elasticsearch['truststore_password'] = 'truststore_path_password'
         elasticsearch['morpheus_password'] = 'morpheusEsUserPassword'
         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node02'
         mysql['enable'] = false
         mysql['host'] = {'192.168.101.01' => 3306, '192.168.101.02' => 3306, '192.168.101.03' => 3306}
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
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
         elasticsearch['secure_mode'] = true
         elasticsearch['use_tls'] = true
         elasticsearch['truststore_path'] = '/var/opt/morpheus/certs/elastic-stack-ca.p12
         elasticsearch['truststore_password'] = 'truststore_path_password'
         elasticsearch['morpheus_password'] = 'morpheusEsUserPassword'
         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node03'
         mysql['enable'] = false
         mysql['host'] = {'192.168.101.01' => 3306, '192.168.101.02' => 3306, '192.168.101.03' => 3306}
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
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