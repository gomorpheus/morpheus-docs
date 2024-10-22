An HA deployment will also include a Highly Available RabbitMQ.  This can be achieved through RabbitMQ's HA-Mirrored Queues on at least 3, independent nodes.  To accomplish this we recommend following Pivotal's documentation on RabbitMQ here: https://www.rabbitmq.com/ha.html and https://www.rabbitmq.com/clustering.html

Install RabbitMQ on the 3 nodes and create a cluster.

.. NOTE:: For the most up to date RPM package we recommend using this link: https://www.rabbitmq.com/install-rpm.html#downloads

.. IMPORTANT:: Morpheus connects to AMQP over 5672 or 5671(TLS) and 61613 or 61614(TLS)

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary.

RabbitMQ requires Erlang to be installed, the exact version will depend on which version of RabbitMQ you're installing on your queue-tier nodes. Click the following link to view the `Compatibility Matrix <https://www.rabbitmq.com/which-erlang.html#compatibility-matrix>`_ for RabbitMQ and Erlang. Note that |morpheus| is compatible with RabbitMQ 3.5.x and higher, however, versions 3.7.x and earlier have reached their end of life and RabbitMQ does not encourage their use. If needed, a compatibility table for these sunsetted versions is in `RabbitMQ documentation <https://www.rabbitmq.com/which-erlang.html#eol-series>`_.

.. important:: To find what version or RabbitMQ is supported please visit `Morpheus Compatibility Docs <https://docs.morpheusdata.com/en/latest/release_notes/compatibility.html#services>`_ 

|

It is best practice to place a load balancer in front of the RabbitMQ nodes, to distribute traffic efficiently.  The VIP or IP that will be assigned to the load balancer will be needed whenconfiguring the application. Alternatively, you can use rabbitmq['addresses'] = '192.168.103.01,192.168.103.02,192.168.103.03' - Morpheus will always try to connect from left to right so, if node 1 is down it will connect and stay connected to the second node. If node 2 goes down (and node1 is back up) it will go back to and stay on node 1. This is not the preferred method but can be made better by giving each node the ips in a different order. 