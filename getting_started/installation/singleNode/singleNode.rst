Single Node
------------

.. image:: /images/arch/morpharch single v3.png
   :align: center

In the Single Node/All-in-one configuration, all components required for Morpheus are installed and configured during the Morpheus ``reconfigure`` command.

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

.. include:: debian.rst
.. include:: centos.rst
.. include:: redhat.rst
.. include:: additional.rst
