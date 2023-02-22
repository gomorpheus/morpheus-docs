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