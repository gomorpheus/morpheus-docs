Requirements
````````````

Ensure the firewall (or security group) allows |morpheus| ``outbound`` access to the various backend services:

  - Should mirror the ``inbound`` ports below for RabbitMQ and ElasticSearch
  
  - mySQL Port to External DB
    
    - 3306/tcp 

Ensure the firewall (or security group) allows |morpheus| ``inbound`` from agents and users:

  - HTTPS Port
    
    - 443/tcp

  - RabbitMQ Ports (3-node is non-TLS by default)

    - 4369 (empd - inter node cluster discovery)
    
    - 5671 (TLS from nodes to RabbitMQ)
    
    - 5672 (non-TLS from nodes to RabbitMQ)
    
    - 15671 (HTTPS API)

    - 15672 (HTTP API)
    
    - 25672 (inter node cluster communication)
    
    - 61613 (STOMP - non-TLS)

    - 61614 (STOMP - TLS)

  - Elasticsearch Ports
  
    - 9200 (API access)

    - 9300 (inter node cluster communication)

  Example commands to run in the OS, if needed.  By default, |morpheus| will modify the OS firewall automatically, if the firewall is enabled.  Usually, in public clouds, the firewall is **not** enabled and this is not required.

    .. tabs::

      .. group-tab:: RHEL 8/9

        .. code-block:: bash

          firewall-cmd --zone=public --add-port={443/tcp,4369/tcp,5671/tcp,5672/tcp,15671/tcp,15672/tcp,25672/tcp,61613/tcp,61614/tcp,9200/tcp,9300/tcp} --permanent
          firewall-cmd --reload
                      
      .. group-tab:: Ubuntu

          .. code-block:: bash

            ufw allow 443,4369,5671,5672,15671,15672,25672,61613,61614,9200,9300/tcp