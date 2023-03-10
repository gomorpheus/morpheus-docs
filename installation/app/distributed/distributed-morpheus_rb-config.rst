.. note::
   In the configuration below, the UID and GID for the users and groups are defined for services that will be embedded.  This ensures
   they are consistent on all nodes. If they are not consistent, the shared storage permissions can become out of sync and errors will
   appear for plugins, images, etc. If not specified, Morpheus will automatically find available UIDs/GIDs starting at 999 and work down.
   Availabililty of UIDs and GIDs can be seen by inspecting ``/etc/passwd`` and ``/etc/group`` respectively.  Change the UIDs and GIDs
   below based on what is available.

.. content-tabs::

   .. tab-container:: tab1
      :title: All Nodes

      .. code-block:: bash

         appliance_url 'https://morpheus.localdomain'
         mysql['enable'] = false
         mysql['host'] = {'192.168.101.01' => 3306, '192.168.101.02' => 3306, '192.168.101.03' => 3306}
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'
         rabbitmq['enable'] = false
         rabbitmq['vhost'] = 'morpheus'
         rabbitmq['queue_user'] = 'admin'
         rabbitmq['queue_user_password'] = 'admin_password'
         rabbitmq['host'] = 'rabbitVIP'
         rabbitmq['port'] = '5672'
         rabbitmq['heartbeat'] = 50
         elasticsearch['enable'] = false
         elasticsearch['cluster'] = 'morpheus'
         elasticsearch['es_hosts'] = {'192.168.103.01' => 9200, '192.168.103.02' => 9200, '192.168.103.03' => 9200}
         user['uid'] = 899
         user['gid'] = 899
         # at the time of this writing, 'local_user' is not valid as an option so the full entry is needed
         node.default['morpheus_solo']['local_user']['uid'] = 898
         node.default['morpheus_solo']['local_user']['gid'] = 898
         guacd['uid'] = 894
         guacd['gid'] = 894