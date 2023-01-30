.. content-tabs::

   .. tab-container:: tab1
      :title: Node 1

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

   .. tab-container:: tab2
      :title: Node 2

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

   .. tab-container:: tab3
      :title: Node 3

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