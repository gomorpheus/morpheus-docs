File Templates
--------------

File Templates are for generating config files, such as my.cnf, elasticsearch.yml, morpheus.rb, or any text file. With full config map variable support, Template Files are dynamically generated during a Workflow phase or ad hoc via Instance actions.

File Templates can also be exposed on Instances in the Settings Tab. Ensure the Instance Type supports settings, and Category is defined in Advance Options on the Library Template config.

.. note:: |morpheus| variables are supported in Library Templates using ``<%= variable.var %>`` format

Examples:

HA Proxy Config (haproxy.cfg)

- FILE NAME: haproxy.cfg
- FILE PATH: /config/haproxy.cfg
- PHASE: Pre Provision
- TEMPLATE:
- SETTING NAME: haproxyConfig
- SETTING CATEGORY: haproxy

.. code-block:: bash

  #!/bin/bash

  global
   maxconn 256
   log /dev/log local0 warning
   log-tag <%=logTag%>

  defaults
   mode http
   timeout connect 5000ms
   timeout client 50000ms
   timeout server 50000ms
   log global

  frontend http-in
   bind *:<%=container.externalPort%>
   default_backend servers

  backend servers
   # server server1 127.0.0.1:80 maxconn 32


mysql config (mysqld.cnf)

- FILE NAME: mysqld.cnf
- FILE PATH: /config/mysqld.cnf
- PHASE: Pre Provision

.. code-block:: bash

   #!/bin/bash

   [mysqld]
   pid-file= /var/run/mysqld/mysqld.pid
   socket= /var/run/mysqld/mysqld.sock
   datadir= /var/lib/mysql
   # Disabling symbolic-links is recommended to prevent assorted security risks
   symbolic-links=0
   explicit_defaults_for_timestamp = 1
