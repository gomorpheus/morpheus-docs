Requirements
````````````

Ensure the firewall (or security group) allows |morpheus| ``outbound`` access to the various backend services:

  - mySQL Ports
    
    - 3306/tcp
  
  - Elasticsearch
    
    - 9200/tcp
  
  - RabbitMQ Ports (current documentation is without TLS)
    
    - 5671/tcp (TLS from nodes to RabbitMQ)

    - 5672/tcp (non-TLS from nodes to RabbitMQ)
    
    - 15671/tcp (HTTPS API)

    - 15672/tcp (HTTP API)
  
  - NFS Port
    
    - 2049/tcp

Ensure the firewall (or security group) allows |morpheus| ``inbound`` from agents and users:

  - HTTPS Port
    
    - 443/tcp

  Example commands to run in the OS, if needed.  By default, |morpheus| will modify the OS firewall automatically, if the firewall is enabled.  Usually, in public clouds, the firewall is **not** enabled.

    .. tabs::

      .. group-tab:: RHEL 8/9

        .. code-block:: bash

          firewall-cmd --zone=public --add-port=443/tcp --permanent
          firewall-cmd --reload
                      
      .. group-tab:: Ubuntu

          .. code-block:: bash

            ufw allow 443/tcp