Advanced morpheus.rb Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Morpheus allows for additional advanced customizations to the morpheus.rb file located in ``/etc/morpheus/morpheus.rb``.  Below is a list of the supported items available in the morpheus.rb file.

.. code-block:: bash

  appliance_url 'https://morpheus.appliance-url.com' # do not add a trailing `/`.
    # Appending alternate port to appliance_url is supported. ie 'https://morpheus.appliance-url.com:8443'

  ui['vm_images_cdn_url'] = 'https://morpheus-images.morpheusdata.com'
  ui['kerberos_config'] = nil
  ui['kerberos_login_config'] = nil
  ui['max_memory_mb'] = nil
  ui['memory_map_threshold'] = 131072
  ui['memory_trim_threshold'] = 131072
  ui['memory_top_pad'] = 131072
  ui['memory_map_max'] = 65536
  ui['memory_alloc_arena_max'] = 2
  ui['http_client_connect_timeout'] = 10000
  ui['http_client_connect_timeout'] = 600000

  mysql['enable'] = true
  mysql['morpheus_db'] = 'morpheus'
  mysql['morpheus_db_user'] = 'morpheus'
  mysql['max_active'] = 100
  mysql['host'] = '127.0.0.1'
  mysql['port'] = 3306
  mysql['tmp_dir'] = '/tmp/mysql'
  mysql['mysql_url_overide'] = 'jdbc:mysql://10.30.20.10:3306,10.30.20.11:3306,10.30.20.12:3306/morpheusdb?autoReconnect=true&useUnicode=true&characterEncoding=utf8&failOverReadOnly=false&useSSL=false'

  logging['svlogd_size'] = 209715200 # 200 MB in bytes
  logging['svlogd_num'] = 30 # keep 30 rotated log files
  logging['svlogd_timeout'] = 86400 # rotate after 24 hours in seconds

  rabbitmq['enable'] = true
  rabbitmq['vhost'] = 'morpheus'
  rabbitmq['queue_user'] = 'queue_user'
  rabbitmq['host'] = '127.0.0.1'
  rabbitmq['port'] = '5672'
  rabbitmq['nodename'] = 'rabbit@localhost'
  rabbitmq['stomp_port'] = 61613
  rabbitmq['heartbeat'] = nil

  elasticsearch['enable'] = true
  elasticsearch['host'] = "127.0.0.1"
  elasticsearch['es_hosts'] = {'127.0.0.1' => 9200}
  elasticsearch['open_files'] = 204800
  elasticsearch['memory_map_threshold'] = 131072
  elasticsearch['memory_trim_threshold'] = 131072
  elasticsearch['memory_top_pad'] = 131072
  elasticsearch['memory_map_max'] = 65536
  elasticsearch['memory_alloc_arena_max'] = 2
  elasticsearch['replica_count'] = 1

  nginx['enable'] = true
  nginx['workers'] = integer calculated from number of cpus
  nginx['worker_connections'] = 10240
  nginx['cache_max_size'] = '5000m'
  nginx['ssl_country_name'] = "US"
  nginx['ssl_state_name'] = "CA"
  nginx['ssl_locality_name'] = "San Mateo"
  nginx['ssl_company_name'] = "Morpheus, LLC"
  nginx['ssl_organizational_unit_name'] = "DevOps"
  nginx['ssl_email_address'] = "personal@email.com"
  nginx['ssl_ciphers'] = "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES256-GCM-SHA384:AES128-GCM-SHA256:AES256-SHA256:AES128-SHA256:AES256-SHA:AES128-SHA:DES-CBC3-SHA:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!MD5:!PSK:!RC4"
  nginx['ssl_protocols'] = "TLSv1 TLSv1.1 TLSv1.2"
  nginx['ssl_session_cache'] = "builtin:1000  shared:SSL:10m"
  nginx['ssl_session_timeout'] = "5m"
  nginx['loading_pages']['max_loops'] = 60 # seconds
  nginx['loading_pages']['timeout_page'] = '/timeout.html'
  nginx['loading_pages']['iteration_time'] = 10000 # milliseconds
  nginx['loading_pages']['loading_page_title'] = 'Morpheus Loading'
  nginx['loading_pages']['loading_page_h1'] = 'Morpheus is Loading...'
  nginx['loading_pages']['loading_page_h2'] = 'please wait'
  nginx['loading_pages']['timout_page_title'] = 'Morpheus timeout, please try again...'
  nginx['loading_pages']['timout_page_h1'] = 'Timeout waiting for Morpheus to load, click below to try again.'
  nginx['loading_pages']['failure_page_title'] = 'Morpheus Server Error'
  nginx['loading_pages']['failure_page_h1'] = 'Morpheus Server Error'
  nginx['loading_pages']['failure_page_h2'] = 'Please contact your system administrator for assistance.'

  repo['repo_host_url'] = 'https://downloads.morpheusdata.com'

.. NOTE:: elasticsearch['replica_count'] settings only apply to local Elasticsearch and not an external cluster. The user must set the replica count in the code for each index. The setting in morpheus.rb is only the cluster default and only applies to the all-in-one appliance. If the cluster is external, the user must set the default on their Elasticsearch config file.

Enabling SSL for connecting to external Elasticsearch
----------------------------------

Users must turn on Elasticsearch HTTPS configuration in morpheus.rb in order to connect to Elasticsearch externally. The elasticsearch['es_hosts'] value is a hash where the host name is the key and the value is the port. We must also set elasticsearch['use_tls'] to true. An example configuration is below:

.. code-block:: bash

  elasticsearch['enable'] = false
  elasticsearch['cluster'] = 'yourCluster'
  elasticsearch['es_hosts'] = {'10.0.0.1' => 9200, '10.0.0.2' => 9200, '10.0.0.3' => 9200}
  elasticsearch['use_tls'] = true

.. include:: offline.rst
.. include:: proxies.rst
