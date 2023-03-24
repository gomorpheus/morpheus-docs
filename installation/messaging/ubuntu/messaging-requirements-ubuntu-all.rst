Requirements
````````````

RabbitMQ requires the following TCP ports for the cluster nodes. Please create the appropriate firewall rules on your
RabbitMQ nodes.

  - 4369
  - 5671 (TLS)
  - 5672
  - 15671 (TLS)
  - 15672
  - 25672
  - 61613
  - 61614 (TLS)

  .. code-block:: bash

    ufw allow 4369,5671,5672,15671,15672,25672,61613,61614/tcp