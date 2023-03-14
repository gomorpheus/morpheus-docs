Additional Options
------------------

There are several additional configuration options during installation that may be performed. For example, |morpheus| provides convenient options for uploading your own SSL certificates as well as externalizing several dependent services.

System Defaults
^^^^^^^^^^^^^^^

|morpheus| follows several install location conventions. Below is a list of system defaults for convenient management:

Installation Location: ``/opt/morpheus``

-  *Log Location:* ``/var/log/morpheus`` \*\* *|morpheus| -UI:*
   ``/var/log/morpheus/morpheus-ui`` \*\* *MySQL:*
   ``/var/log/morpheus/mysql`` \*\* *NginX:* ``/var/log/morpheus/nginx``
   \*\* *Check Server:* ``/var/log/morpheus/check-server`` \*\* *Elastic
   Search:* ``/var/log/morpheus/elsticsearch`` \*\* *RabbitMQ:*
   ``/var/log/morpheus/rabbitmq`` \*\* *Redis:*
   ``/var/log/morpheus/redis``
-  *User-defined install/config:* ``/etc/morpheus/morpheus.rb``

SSL Certificates
^^^^^^^^^^^^^^^^

The default installation generates a self-signed SSL certificate. To
implement a third-party certificate:

1. Copy the private key and certificate to
   ``/etc/morpheus/ssl/your_fqdn_name.key`` and
   ``/etc/morpheus/ssl/your_fqdn_name.crt`` respectively.
2. Edit the configuration file ``/etc/morpheus/morpheus.rb`` and add the
   following entries:

.. code-block:: bash
  nginx[‘ssl\_certificate’] = ‘path to the certificate file'
  nginx[‘ssl\_server\_key’] = ‘path to the server key file' ----

NOTE: Both files should be owned by root and only readable by root, also if the server certificate is signed by an intermediate then you should include the signing chain inside the certificate file.

Next simply reconfigure the appliance and restart nginx:

.. code-block:: bash
  sudo morpheus-ctl reconfigure
  sudo morpheus-ctl restart nginx

Additional Configuration Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are several other options available to the
``/etc/morpheus/morpheus.rb`` file that can be useful when setting up
external service integrations or high availability:

.. code-block:: bash
  mysql['enable'] = false mysql['host'] = '52.53.240.28' mysql['port'] =
  10004 mysql['morpheus\_db'] = 'morpheusdb01' mysql['morpheus\_db\_user']
  = 'merovingian' mysql['morpheus\_password'] = 'Wm5n5gXqXCe9v52'
  rabbitmq['enable'] = false rabbitmq['vhost'] = 'zion'
  rabbitmq['queue\_user'] = 'dujour' rabbitmq['queue\_user\_password'] =
  '5tfg9n2iBifzW5c' rabbitmq['host'] = '54.183.196.152' rabbitmq['port'] =
  '10008' rabbitmq['stomp\_port'] = '10010' redis['enable'] = false
  redis['host'] = '52.53.240.28' redis['port'] = 10009
  elasticsearch['enable'] = false elasticsearch['cluster'] =
  'nebuchadnezzar' elasticsearch['es\_hosts'] = {'52.53.214.68' => 10003}

These settings allow one to externally configure and scale mysql, elasticsearch, redis, and rabbitmq which is critical for a high availability setup.
