Installation
============

|morpheus| comes packaged as a ``debian`` or ``yum`` based package. It can be installed on a single on/off premise linux based host, or configured for high availability and horizontal scaling.

Configurations
--------------

All components required for Morpheus are installed and configured by default during the Morpheus ``reconfigure`` command. The Morpheus config file, ``morpheus.rb``, can optionally be configured to point the Morpheus App to external services (distributed configuration).

on a single host.

- Application Tier
   - Morpheus App
- Database Tier
   - MySQL
- Message Tier
   - RabbitMQ
- Search Tier
   - Elasticsearch

This is the single node/all-in-one configuration, as all tiers are local to the appliance and no services are external to the Appliance Host.

Morpheus can optionally be configured to use external Database, Messaging, and/or Search Tiers. This means instead of installing, for example, MySQL on the same host as the Morpheus App, the Morpheus configuration file (morpheus.rb) is setup to point to an external MySQL host, cluster or service, and MySQL will not be installed or configured on the Appliance Host.

This is one example of a distributed configuration, as the database tier is external from the Application tier.

.. Note::  You can view our offline installation guide at :ref:`offline-installer`.

.. include:: /getting_started/installation/singleNode/singleNode.rst
.. include:: /getting_started/installation/distributed/distributed.rst
.. include:: additional.rst

.. |morpheushub| raw:: html

   <a href="https://morpheushub.com/" target="_blank">morpheushub.com</a>
