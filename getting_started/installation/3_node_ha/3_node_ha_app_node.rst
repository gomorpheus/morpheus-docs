App Node Installation
^^^^^^^^^^^^^^^^^^^^^

Requirements
````````````

Ensure the firewall (or security group) allows |morpheus| ``outbound`` access to the various backend services:

  - mySQL Port to External DB
    
    - 3306/tcp 

Ensure the firewall (or security group) allows |morpheus| ``inbound`` from agents and users:

  - HTTPS Port
    
    - 443/tcp

  - RabbitMQ Ports 

    - 4369 (epmd - inter node cluster discovery)
    
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

Installation
````````````

#. First begin by downloading and installing the requisite |morpheus| packages to ALL |morpheus| app nodes.

   |morpheus| packages can be found in the Downloads section of the `Morpheus Hub <https://morpheushub.com/download>`_

   .. content-tabs::

      .. tab-container:: tab1
         :title: RHELL/CentOS

         .. code-block:: bash
    
            [root@node: ~] wget https://example/path/morpheus-appliance-ver-1.el8.x86_64.rpm
            [root@node: ~] rpm -ihv morpheus-appliance-appliance-ver-1.el8.x86_64.rpm

      .. tab-container:: tab2
         :title: Ubuntu

         .. code-block:: bash
    
            [root@node: ~] wget https://example/path/morpheus-appliance_ver-1.amd64.deb
            [root@node: ~] dpkg -i morpheus-appliance-appliance_ver-1.amd64.deb

#. Do NOT run reconfigure yet. The |morpheus| configuration file must be edited prior to the initial reconfigure.

#. Next you will need to edit the |morpheus| configuration file ``/etc/morpheus/morpheus.rb`` on each node.

   .. include:: /getting_started/installation/3_node_ha/3_node_ha_morpheus_rb.rst

#. Mount shared storage at /var/opt/morpheus/morpheus-ui on each App node if you have not already done so. Create the directory if it does not already exist.

#. Reconfigure on all nodes

   .. content-tabs::

      .. tab-container:: tab1
         :title: All Nodes

         .. code-block:: bash

            [root@node: ~] morpheus-ctl reconfigure

   |morpheus| will come up on all nodes and Elasticsearch will auto-cluster. RabbitMQ will need to be clustered manually after reconfigure completes on all nodes. 
