Full HA
-------

Default Locations
^^^^^^^^^^^^^^^^^

|morpheus| follows several install location conventions. Below is a list of system defaults for convenient management:

* Installation Location: ``/opt/morpheus``
* Log Location: ``/var/log/morpheus``

  * Morpheus-UI: ``/var/log/morpheus/morpheus-ui``
  * NginX: ``/var/log/morpheus/nginx``
  * Check Server: ``/var/log/morpheus/check-server``
  * Redis: ``/var/log/morpheus/redis``

*  User-defined install/config: ``/etc/morpheus/morpheus.rb``

.. include:: /getting_started/installation/distributed/full/percona.rst
.. include:: /getting_started/installation/distributed/full/perconaTls.rst
.. include:: /getting_started/installation/distributed/full/rabbitmq.rst
.. include:: /getting_started/installation/distributed/full/elasticsearch.rst
.. include:: /getting_started/installation/distributed/full/appliance_ha.rst
.. include:: /getting_started/installation/distributed/HA_Shared_Storage.rst
