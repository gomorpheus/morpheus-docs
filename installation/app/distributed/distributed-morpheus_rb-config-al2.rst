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
         elasticsearch['enable'] = false
         elasticsearch['auth_user'] = 'admin'
         elasticsearch['auth_password'] = 'Abc123123@'
         # 'cluster' is the same as the ES 'domain'
         elasticsearch['cluster'] = 'morpheusdomain'
         elasticsearch['es_hosts'] = {'vpc-morpheusdomain-4ypsets66htlwedmhew45kfxd4.us-east-2.es.amazonaws.com' => 443}
         elasticsearch['use_tls'] = true
         rabbitmq['enable'] = false
         rabbitmq['host'] = 'b-eed117b0-8bed-43f7-8fc1-dcaba4453846.mq.us-east-2.amazonaws.com'
         rabbitmq['port'] = '5671'
         rabbitmq['vhost'] = 'morpheus'
         rabbitmq['queue_user'] = 'morpheus-user'
         rabbitmq['queue_user_password'] = 'abc123123123123'
         rabbitmq['use_tls'] = true
         mysql['enable'] = false
         mysql['host'] = 'morpheus-cluster.cluster-cgguv6wqc1al.us-east-2.rds.amazonaws.com'
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'
         user['uid'] = 899
         user['gid'] = 899
         # at the time of this writing, 'local_user' is not valid as an option so the full entry is needed
         node.default['morpheus_solo']['local_user']['uid'] = 898
         node.default['morpheus_solo']['local_user']['gid'] = 898
         guacd['uid'] = 894
         guacd['gid'] = 894