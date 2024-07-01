Default Paths
^^^^^^^^^^^^^

|morpheus| follows several install location conventions. Below is a list of the system paths.

.. important:: Altering the default system paths is not supported and may break functionality.

* Installation Location: ``/opt/morpheus``
* Log Location: ``/var/log/morpheus``

  * Morpheus-UI: ``/var/log/morpheus/morpheus-ui``
  * NginX: ``/var/log/morpheus/nginx``
  * Check Server: ``/var/log/morpheus/check-server``
  * Elastic Search: ``/var/log/morpheus/elasticsearch``
  * RabbitMQ: ``/var/log/morpheus/rabbitmq``

*  User-defined install/config: ``/etc/morpheus/morpheus.rb``