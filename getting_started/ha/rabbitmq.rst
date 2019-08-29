RabbitMQ Cluster
----------------

An HA deployment will also include a Highly Available RabbitMQ.  This can be achieved through RabbitMQ's HA-Mirrored Queues on at least 3, independent nodes.  To accomplish this we recommend following Pivotal's documentation on RabbitMQ here: https://www.rabbitmq.com/ha.html and https://www.rabbitmq.com/clustering.html

Install RabbitMQ on the 3 nodes and create a cluster.

.. NOTE:: For the most up to date RPM package we recommend using this link: https://www.rabbitmq.com/install-rpm.html#downloads

.. IMPORTANT:: Morpheus connects to AMQP over 5672 or 5671(SSL) and 61613 or 61614(SSL)

On All Nodes:
.............

.. code-block:: bash

  rabbitmq-plugins enable rabbitmq_stomp

Required Rabbitmq Policies:
...........................

The following policies must be set on the morpheus vhost. Failure to apply these policies will cause performance and/or stability issues.

.. code-block:: bash

   rabbitmqctl set_policy -p morpheus --apply-to queues --priority 2 statCommands "statCommands.*" '{"expires":1800000, "ha-mode":"all"}'
   rabbitmqctl set_policy -p morpheus --apply-to queues --priority 2 morpheusAgentActions "morpheusAgentActions.*" '{"expires":1800000, "ha-mode":"all"}'
   rabbitmqctl set_policy -p morpheus --apply-to all --priority 1 ha ".*" '{"ha-mode":"all"}'
