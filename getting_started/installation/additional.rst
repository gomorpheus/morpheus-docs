Additional Options
------------------

There are several additional configuration options during installation that may be performed. For example, |morpheus| provides convenient options for uploading your own SSL certificates as well as externalizing several dependent services.

System Defaults
^^^^^^^^^^^^^^^

|morpheus| follows several install location conventions. Below is a list of system defaults for convenient management:

* Installation Location: ``/opt/morpheus``
* Log Location: ``/var/log/morpheus``

  * Morpheus-UI: ``/var/log/morpheus/morpheus-ui``
  * MySQL: ``/var/log/morpheus/mysql``
  * NginX: ``/var/log/morpheus/nginx``
  * Check Server: ``/var/log/morpheus/check-server``
  * Elastic Search: ``/var/log/morpheus/elsticsearch``
  * RabbitMQ: ``/var/log/morpheus/rabbitmq``
  * Redis: ``/var/log/morpheus/redis``

*  User-defined install/config: ``/etc/morpheus/morpheus.rb``

SSL Certificates
^^^^^^^^^^^^^^^^

The default installation generates a self-signed SSL certificate. To implement a third-party certificate:

#. Copy the private key and certificate to ``/etc/morpheus/ssl/your_fqdn_name.key`` and ``/etc/morpheus/ssl/your_fqdn_name.crt`` respectively.

#. Edit the configuration file ``/etc/morpheus/morpheus.rb`` and add the following entries:

   .. code-block:: bash

    nginx['ssl_certificate'] = 'path to the certificate file'
    nginx['ssl_server_key'] = 'path to the server key file'

   .. NOTE:: Both files should be owned by root and only readable by root, also if the server certificate is signed by an intermediate then you should include the signing chain inside the certificate file.

#. Next simply reconfigure the appliance and restart nginx:

   .. code-block:: bash

    sudo morpheus-ctl reconfigure
    sudo morpheus-ctl restart nginx

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
  mysql['mysql_url_overide'] = 'jdbc:mysql://10.30.20.10:3306,10.30.20.11:3306,10.30.20.12:3306/morpheusdb?autoReconnect=true&useUnicode=true&characterEncoding=utf8&failoverReadOnly=false&useSSL=false'

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
