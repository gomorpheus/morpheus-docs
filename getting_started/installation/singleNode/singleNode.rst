Single Node
------------

.. image:: /images/arch/morpharchSingleV3.png
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

.. include:: /getting_started/installation/singleNode/debian.rst
.. include:: /getting_started/installation/singleNode/centos.rst
.. include:: /getting_started/installation/singleNode/redhat.rst
.. include:: /getting_started/installation/additional.rst
