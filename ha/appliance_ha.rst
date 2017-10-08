Application Tier
----------------

{morpheus} configuration is controlled by a configuration file located
at /etc/morpheus/morpheus.rb. This file is read when you run
morpheus-ctl reconfigure after installing the appliance package. Each
section is tied to a deployment tier: database is mysql, message queue
is rabbitmq, serach index is elasticsearch. There are no entries for the
web and application tiers since those are part of the core application
server where the configuration file resides.

#. Download and install the Morpheus Applaince Package
#. After installing and prior to reconfiguring, edit the morpheus.rb file

   .. code-block:: bash

    sudo vi /etc/morpheus/morpheus.rb

   Change the values to match your configured services:

   .. code-block:: bash

    mysql['enable'] = false
    mysql['host'] = {'52.53.240.28' => 10004,  '52.53.241.94' => 10004}
    mysql['morpheus_db'] = 'morpheusdb01'
    mysql['morpheus_db_user'] = 'merovingian'
    mysql['morpheus_password'] = 'Wm5n5gXqXCe9v52'
    rabbitmq['enable'] = false rabbitmq['vhost'] = 'zion' rabbitmq['queue_user'] = 'dujour'
    rabbitmq['queue_user_password'] = '5tfg9n2iBifzW5c'
    rabbitmq['host'] = 'rabbitmq-lb01.morpheusdata.com'
    rabbitmq['port'] = '10008'
    rabbitmq['stomp_port'] = '10010'
    rabbitmq['heartbeat'] = 50
    elasticsearch['enable'] = false
    elasticsearch['cluster'] = 'nebuchadnezzar'
    elasticsearch['es_hosts'] = {'52.53.214.68' => 10003, '52.53.242.129' => 10003, '52.53.68.67' => 10003} ----

#. Recofigure Morpheus

   .. code-block:: bash

    sudo morpheus-ctl reconfigure
