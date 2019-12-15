Single Host
-----------

.. image:: /images/arch/morpharchSingleV3.png
   :align: center

In the Single Host/All-in-one configuration, all components required for Morpheus are installed and configured during the Morpheus ``reconfigure`` command.

Appliance Host
 - Application
    - Morpheus App
 - Web Server/Proxy
    - Nginix
 - Cache
    - Redis
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

Default Locations
^^^^^^^^^^^^^^^^^

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

.. include:: /getting_started/installation/singleNode/debian.rst
.. include:: /getting_started/installation/singleNode/centos.rst
.. include:: /getting_started/installation/singleNode/redhat.rst
