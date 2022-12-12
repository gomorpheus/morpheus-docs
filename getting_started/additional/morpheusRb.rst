.. _morpheus.rb:

Advanced morpheus.rb Settings
-----------------------------

Morpheus allows for additional advanced customizations for system managed services within the morpheus.rb file located in ``/etc/morpheus/morpheus.rb``.  Below is a list of the supported items available in the ``morpheus.rb`` file.

.. note:: Service configuration settings are not applicable for externalized services such as external mysql/percona, elasticsearch or rabbitmq clusters. Only connection settings are applicable for external services. Additionally, to configure |morpheus| to utilize alternate ports for SSL, you may have to take additional configuration steps. If simply appending a port to your ``appliance_url`` value doesn't work, consult the related article in our `KnowledgeBase <https://support.morpheusdata.com/s/article/Configure-Morpheus-to-utilize-and-alternate-port-for-SSL?language=en_US>`_.

.. code-block:: ruby

  app['encryption_key_suffix'] = 'key'
  appliance_url 'https://morpheus.appliance-url.com'
    # Appending alternate port to appliance_url is supported. ie 'https://morpheus.appliance-url.com:8443'
    # The appliance_url cannot exceed 64 characters
    # The appliance_url must not contain a trailing `/`.

  bitcan['backup_directory'] = '/var/opt/morpheus/bitcan/backups'
  bitcan['working_directory'] = '/var/opt/morpheus/bitcan/working'

  elasticsearch['auth_password'] = 'xxxxxxxxxxxxxxxx'
  elasticsearch['auth_user'] = 'morpheus-es-user'
  elasticsearch['enable'] = true
  elasticsearch['es_hosts'] = {'127.0.0.1' => 9200}
  elasticsearch['host'] = "127.0.0.1"
  elasticsearch['port'] = "9200"
  elasticsearch['tmp_dir'] = '/var/tmp/elasticsearch'
  elasticsearch['use_tls'] = false
  ↓ The following elasticsearch settings are only valid for Internal/Embedded elasticsearch services
  elasticsearch['log_dir'] = '/var/log/morpheus/elasticsearch'
  elasticsearch['memory_alloc_arena_max'] = 2
  elasticsearch['memory_map_max'] = 65536
  elasticsearch['memory_map_threshold'] = 131072
  elasticsearch['memory_top_pad'] = 131072
  elasticsearch['memory_trim_threshold'] = 131072
  elasticsearch['open_files'] = 204800
  elasticsearch['secure_mode'] = false

  guacd['guacamole_enabled'] = false

  logging['svlogd_num'] = 30 #### keep 30 rotated log files
  logging['svlogd_size'] = 209715200 #### 200 MB in bytes
  logging['svlogd_timeout'] = 86400 #### rotate after 24 hours in seconds

  mysql['enable'] = true
  mysql['host'] = {'127.0.0.1' => 3306}
  mysql['use_tls'] = false
  mysql['morpheus_db_user'] = 'morpheus-db-user'
  mysql['morpheus_db'] = 'xxxxxxxxxxxxxxxx'
  mysql['mysql_url_overide'] = 'jdbc:mysql://10.30.20.10:3306,10.30.20.11:3306,10.30.20.12:3306/morpheusdb?autoReconnect=true&useUnicode=true&characterEncoding=utf8&failOverReadOnly=false&useSSL=false'
  ↓ The following mysql settings are only valid for Internal/Embedded mysql services
  mysql['tmp_dir'] = '/tmp/mysql'
  mysql['log_dir'] = '/var/log/morpheus/mysql'
  mysql['max_active'] = 150 # The combined value off all app node max_active values must be lower than max_connections setting in mysql
  mysql['max_connections'] = 151
  mysql['max_allowed_packet'] = 67108864


  nginx['cache_max_size'] = '5000m'
  nginx['enable'] = true
  nginx['loading_pages']['failure_page_h1'] = 'Morpheus Server Error'
  nginx['loading_pages']['failure_page_h2'] = 'Please contact your system administrator for assistance.'
  nginx['loading_pages']['failure_page_title'] = 'Morpheus Server Error'
  nginx['loading_pages']['iteration_time'] = 10000 # milliseconds
  nginx['loading_pages']['loading_page_h1'] = 'Morpheus is Loading...'
  nginx['loading_pages']['loading_page_h2'] = 'please wait'
  nginx['loading_pages']['loading_page_title'] = 'Morpheus Loading'
  nginx['loading_pages']['max_loops'] = 60 # seconds
  nginx['loading_pages']['timeout_page'] = '/timeout.html'
  nginx['loading_pages']['timout_page_h1'] = 'Timeout waiting for Morpheus to load, click below to try again.'
  nginx['loading_pages']['timout_page_title'] = 'Morpheus timeout, please try again...'
  nginx['log_format_name'] = 'custom'
  nginx['log_format'] = '\'$remote_addr - $remote_user [$time_local] "$request" \' \'$status $body_bytes_sent "$http_referer" \' \'"$http_user_agent" "$http_x_forwarded_for" \' \'rt=$request_time uct="$upstream_connect_time" uht="$upstream_header_time" urt="$upstream_response_time"\';'
  nginx['ssl_ciphers'] = "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES256-GCM-SHA384:AES128-GCM-SHA256:AES256-SHA256:AES128-SHA256:AES256-SHA:AES128-SHA:DES-CBC3-SHA:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!MD5:!PSK:!RC4"
  nginx['ssl_company_name'] = "Morpheus, LLC"
  nginx['ssl_country_name'] = "US"
  nginx['ssl_email_address'] = "personal@email.com"
  nginx['ssl_locality_name'] = "San Mateo"
  nginx['ssl_organizational_unit_name'] = "DevOps"
  nginx['ssl_protocols'] = "TLSv1 TLSv1.1 TLSv1.2"
  nginx['ssl_session_cache'] = "builtin:1000  shared:SSL:10m"
  nginx['ssl_session_timeout'] = "5m"
  nginx['ssl_state_name'] = "CA"
  nginx['worker_connections'] = 10240
  nginx['workers'] = integer calculated from number of cpus

  rabbitmq['enable'] = true
  rabbitmq['host'] = '127.0.0.1'
  rabbitmq['port'] = '5672'
  rabbitmq['queue_user_password'] = 'xxxxxxxxxxxxxxxx'
  rabbitmq['queue_user'] = 'morpheus-rmq-user'
  rabbitmq['vhost'] = 'morpheus'
  ↓ The following rabbitmq settings are only valid for Internal/Embedded rabbitmq services
  rabbitmq['heartbeat'] = nil
  rabbitmq['log_dir'] = '/var/log/morpheus/rabbitmq'
  rabbitmq['nodename'] = 'rabbit@localhost'
  rabbitmq['port'] = '5672'
  rabbitmq['use_tls'] = false

  repo['repo_host_url'] = 'https://downloads.morpheusdata.com'

  ui['http_client_connect_timeout'] = 10000  #### milliseconds
  ui['jobs_enabled'] = true #### This option disables the appliance jobs service on the appliance node when set to false. This should be disabled only when configuring jobs to run on specific app nodes in HA environments.
  ui['kerberos_config'] = nil
  ui['kerberos_login_config'] = nil
  ui['log_dir'] = '/var/log/morpheus/morpheus-ui'
  ui['max_memory_mb'] = nil
  ui['memory_alloc_arena_max'] = 2
  ui['memory_map_max'] = 65536
  ui['memory_map_threshold'] = 131072
  ui['memory_top_pad'] = 131072
  ui['memory_trim_threshold'] = 131072
  ui['pxe_boot_enabled'] = false #### This option disables the PXE service within the app
  ui['vm_images_cdn_url'] = 'https://morpheus-images.morpheusdata.com'
