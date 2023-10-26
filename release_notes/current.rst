.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. IMPORTANT:: |morpheus| 6.3.0 is the first version to require Plugin API version 1.0.0+. As a result, small changes will need to be made in order to make plugins created by earlier versions of |morpheus| compatible. Please see the related `article in our KnowledgeBase <https://support.morpheusdata.com/s/article/Making-plugins-compatible-with-Morpheus-6-3-0?language=en_US>`_ for full details on updating plugins.
.. IMPORTANT:: |morphver| contains embedded MySQL v8 upgrade when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
.. IMPORTANT:: Minimum v6.x required to upgrade to |morphver| for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6, or 6.1.0 - 6.2.1 prior to upgrading to |morphver|
.. WARNING:: Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

Features
========


Appliance & Agent Updates
=========================
