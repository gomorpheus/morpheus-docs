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

    [root]# firewall-cmd --zone=public --add-port={4369/tcp,5671/tcp,5672/tcp,15671/tcp,15672/tcp,25672/tcp,61613/tcp,61614/tcp} --permanent
    [root]# firewall-cmd --reload

Install the versionlock plugin for dnf to lock the version of packages

   .. code-block:: bash

      dnf install python3-dnf-plugin-versionlock -y