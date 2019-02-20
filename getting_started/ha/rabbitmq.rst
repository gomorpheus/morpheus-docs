RabbitMQ Cluster
----------------

Install RabbitMQ on the 3 nodes and create a cluster

.. NOTE:: For the most up to date RPM package we recommend using this link: https://www.rabbitmq.com/install-rpm.html#downloads

On All Nodes:
.............

.. code-block:: bash

  rabbitmq-plugins enable rabbitmq_stomp

Recommended Rabbitmq Policies:
..................................

.. code-block:: bash

   rabbitmqctl set_policy -p morpheus --apply-to queues --priority 1 statCommands "statCommands.*" '{expires:1800000}'
   rabbitmqctl set_policy -p morpheus --apply-to queues --priority 1 morpheusAgentActions "morpheusAgentActions.*" '{expires:1800000}'
