Single Node Install Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a Single Host/All-in-one configuration, all components required for Morpheus are automatically installed and configured during the Morpheus ``reconfigure`` command.

.. image:: /images/arch/morpharchSingleV3.png
   :align: center

Appliance Host
 - Application
    - Morpheus App
 - Web Server/Proxy
    - NGINX
 - Database
    - MySQL
 - Messaging
    - RabbitMQ
 - Search
    - Elasticsearch
 - Console
    - Guacamole
 - Monitoring
    - Check Server

Default Paths
`````````````

|morpheus| follows several install location conventions. Below is a list of the system paths.

.. important:: Altering the default system paths is not supported and may break functionality.

* Installation Location: ``/opt/morpheus``
* Log Location: ``/var/log/morpheus``

  * Morpheus-UI: ``/var/log/morpheus/morpheus-ui``
  * MySQL: ``/var/log/morpheus/mysql``
  * NginX: ``/var/log/morpheus/nginx``
  * Check Server: ``/var/log/morpheus/check-server``
  * Elastic Search: ``/var/log/morpheus/elasticsearch``
  * RabbitMQ: ``/var/log/morpheus/rabbitmq``

*  User-defined install/config: ``/etc/morpheus/morpheus.rb``
