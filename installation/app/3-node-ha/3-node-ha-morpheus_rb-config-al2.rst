.. content-tabs::

   .. tab-container:: tab1
      :title: Node 1

      .. code-block:: ruby

         appliance_url 'https://morpheus.localdomain'
         elasticsearch['es_hosts'] = {'node01' => 9200, 'node02' => 9200, 'node03' => 9200}
         elasticsearch['node_name'] = 'node01'
         elasticsearch['host'] = '0.0.0.0'
         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node01'
         mysql['enable'] = false
         mysql['host'] = 'morpheus-cluster.cluster-cgguv6wqc1al.us-east-2.rds.amazonaws.com'
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'

   .. tab-container:: tab2
      :title: Node 2

      .. code-block:: ruby

         appliance_url 'https://morpheus.localdomain'
         elasticsearch['es_hosts'] = {'node01' => 9200, 'node02' => 9200, 'node03' => 9200}
         elasticsearch['node_name'] = 'node02'
         elasticsearch['host'] = '0.0.0.0'
         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node02'
         mysql['enable'] = false
         mysql['host'] = 'morpheus-cluster.cluster-cgguv6wqc1al.us-east-2.rds.amazonaws.com'
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'

   .. tab-container:: tab3
      :title: Node 3

      .. code-block:: ruby

         appliance_url 'https://morpheus.localdomain'
         elasticsearch['es_hosts'] = {'node01' => 9200, 'node02' => 9200, 'node03' => 9200}
         elasticsearch['node_name'] = 'node03'
         elasticsearch['host'] = '0.0.0.0'
         rabbitmq['host'] = '0.0.0.0'
         rabbitmq['nodename'] = 'rabbit@node03'
         mysql['enable'] = false
         mysql['host'] = 'morpheus-cluster.cluster-cgguv6wqc1al.us-east-2.rds.amazonaws.com'
         mysql['morpheus_db'] = 'morpheus'
         mysql['morpheus_db_user'] = 'morpheusDbUser'
         mysql['morpheus_password'] = 'morpheusDbUserPassword'