An HA deployment will also include a Highly Available RabbitMQ.  This can be achieved through RabbitMQ's HA-Mirrored Queues on at least 3, independent nodes.  To accomplish this we recommend following Pivotal's documentation on RabbitMQ here: https://www.rabbitmq.com/ha.html and https://www.rabbitmq.com/clustering.html

Install RabbitMQ on the 3 nodes and create a cluster.

.. NOTE:: For the most up to date RPM package we recommend using this link: :link: https://www.rabbitmq.com/install-rpm.html#downloads

.. IMPORTANT:: Morpheus connects to AMQP over 5672 or 5671(TLS) and 61613 or 61614(TLS)

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary.

RabbitMQ requires Erlang to be installed, the exact version will depend on which version of RabbitMQ you're installing on your queue-tier nodes. Click the link below to expand a compatibility table for RabbitMQ and Erlang. Note that |morpheus| is compatible with RabbitMQ 3.5.x and higher, however, versions 3.7.x and earlier have reached their end of life and RabbitMQ does not encourage their use. If needed, a compatibility table for these sunsetted versions is in `RabbitMQ documentation <https://www.rabbitmq.com/which-erlang.html#eol-series>`_.

.. toggle-header:: :header: **RabbitMQ/Erlang Compatibility Table**

    .. list-table::
       :header-rows: 1

       * - RabbitMQ Version
         - Minimum Required Erlang/OTP
         - Maximum Supported Erlang/OTP
       * - 3.9.x
         - 23.2
         - 24.x
       * - 3.8.16 - 3.8.19
         - 23.2
         - 24.x
       * - 3.8.9 - 3.8.15
         - 22.3
         - 23.x
       * - 3.8.4 - 3.8.8
         - 21.3
         - 23.x
       * - 3.8.0 - 3.8.3
         - 21.3
         - 22.x

|

It is best practice to place a load balancer in front of the RabbitMQ nodes, to distribute traffic efficiently.  The VIP or IP that will be assigned to the load balancer will be needed when
configuring the application.  Alternatively, each node could be pointed at a single RabbitMQ but this will not provide redundancy for each application node.