Application Tier
^^^^^^^^^^^^^^^^

|morpheus| configuration is controlled by a configuration file located at ``/etc/morpheus/morpheus.rb``. This file is read when you run ``morpheus-ctl reconfigure`` after installing the appliance package. Each section is tied to a deployment tier: database is mysql, message queue is rabbitmq, search index is elasticsearch. There are no entries for the web and application tiers since those are part of the core application server where the configuration file resides.

#. Download and install the Morpheus Appliance Package

#. Next we must install the package onto the machine and configure the morpheus services:

   .. code-block:: bash

      sudo rpm -i morpheus-appliance-x.x.x-1.x86_64.rpm

#. After installing and prior to reconfiguring, edit the ``morpheus.rb`` file

   .. code-block:: bash

      sudo vi /etc/morpheus/morpheus.rb

#. Change the values to match your configured services:

   .. NOTE:: The values below are examples. Update hosts, ports, usernames and password with your specifications. Only include entries for services you wish to externalize.

   .. code-block:: bash

      mysql['enable'] = false
      mysql['host'] = {'10.30.20.139' => 3306, '10.30.20.153' => 3306, '10.30.20.196' => 3306}
      mysql['morpheus_db'] = 'morpheus'
      mysql['morpheus_db_user'] = 'morpheusDbUser'
      mysql['morpheus_password'] = 'morpheusDbUserPassword'
      rabbitmq['enable'] = false
      rabbitmq['vhost'] = 'morpheus'
      rabbitmq['queue_user'] = 'lbuser'
      rabbitmq['queue_user_password'] = 'lbuserpassword'
      rabbitmq['host'] = 'rabbitvip'
      rabbitmq['port'] = '5672'
      rabbitmq['heartbeat'] = 50
      elasticsearch['enable'] = false
      elasticsearch['cluster'] = 'esclustername'
      elasticsearch['es_hosts'] = {'10.30.20.91' => 9200, '10.30.20.149' => 9200, '10.30.20.165' => 9200}
      elasticsearch['use_tls'] = true
      elasticsearch['auth_user'] = 'morpheus-user'
      elasticsearch['auth_password'] = 'xxxxxxxxxxxxxxxx'


#. Reconfigure Morpheus

   .. code-block:: bash

      sudo morpheus-ctl reconfigure
