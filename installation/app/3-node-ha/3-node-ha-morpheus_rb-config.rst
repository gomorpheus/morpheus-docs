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
         mysql['host'] = {'192.168.101.01' => 3306, '192.168.101.02' => 3306, '192.168.101.03' => 3306}
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'

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
         mysql['host'] = {'192.168.101.01' => 3306, '192.168.101.02' => 3306, '192.168.101.03' => 3306}
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'

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
         mysql['host'] = {'192.168.101.01' => 3306, '192.168.101.02' => 3306, '192.168.101.03' => 3306}
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'