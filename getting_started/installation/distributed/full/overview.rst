Full HA Install Overview
^^^^^^^^^^^^^^^^^^^^^^^^

- App Host(s) with Distributed Services (Full HA)
   Application tier is installed on one or more hosts. All UI hosts point to externalized Transactional Database, Non-Transactional Database, and Message Tiers. The reconfigure process installs only Application services.

.. image:: /images/arch/FullDistributedSingleSite.png

Minimum Nodes
`````````````
For Full High-Availability configurations, RabbitMQ, Elasticsearch and mySQL(Galera/Percona) must be configured in minimum 3 Node Clusters, and 2 or more App Nodes are required.

.. note:: VM requirements assume local services. VM count requirements are not applicable when using hosted services such as AWS RDS mySQL.

Minimum 11 Nodes
   - 2+ Application Hosts
   - 3 Node RabbitMQ Cluster
   - 3 Node Elasticsearch Cluster
   - 3 Node Galera/Percona Cluster

.. important:: Asynchronous Active/Active and Active/Passive Database configurations are not supported for HA configurations. A minimum 3 node mySQL Cluster with synchronous multi-master replication is required for Database Clusters. |morpheus| recommends Percona XtraDB Clusters with synchronous multi-master replication. Asynchronous Active/Passive can be used but is not considered an HA configuration.

.. important:: For Clusters with more than 3 Nodes, always use an odd number of nodes (3,5,7 etc) to ensure Quorum.

Shared Storage
``````````````
For configurations with 2 or more Applications Nodes, Shared Storage is required between the app nodes for ``/var/opt/morpheus/morpheus-ui/*``. Local Storage File Shares will need to be copied to a shared file system so all assets are available on all App nodes.

Shared Assets
`````````````
* Logos
* Uploaded Virtual Images
* Deployment Uploads
* Ansible
* Terraform
* Morpheus Backups

.. note:: Backups, deployment and virtual image storage locations can be overridden within the |morpheus|-ui.

Port Requirements
`````````````````

+---------------+-------------------+------------------+----------------------------------------------+
| Service       | Source            | Destination      | Port(s)                                      |
+---------------+-------------------+------------------+----------------------------------------------+
| Morpheus      | Application Node  | mySQL            | 3306                                         |
+---------------+-------------------+------------------+----------------------------------------------+
| Morpheus      | Application Node  | Elasticsearch    | 9200                                         |
+---------------+-------------------+------------------+----------------------------------------------+
| Morpheus      | Application Node  | RabbitMQ         | 5672/5671(SSL)                               |
+---------------+-------------------+------------------+----------------------------------------------+
| Morpheus      | Application Node  | YUM or APT       | 443                                          |
+---------------+-------------------+------------------+----------------------------------------------+
| Elasticsearch | Elasticsearch     | Elasticsearch    | 9300                                         |
+---------------+-------------------+------------------+----------------------------------------------+
| mySQL         | mySQL             | mySQL            | 4444,4567,4568                               |
+---------------+-------------------+------------------+----------------------------------------------+
| RabbitMQ      | RabbitMQ          | RabbitMQ         | 4369,25672                                   |
+---------------+-------------------+------------------+----------------------------------------------+
| Agents        | Managed Instances | Application Node | 443                                          |
+---------------+-------------------+------------------+----------------------------------------------+
| Web Interface | Internal Clients  | Application Node | 443                                          |
+---------------+-------------------+------------------+----------------------------------------------+

.. list-table:: **RabbitMQ Port Requirement Details**
  :widths: auto
  :header-rows: 1

    * - Source 
      - Destination
      - Port
      - Protocol 
      - 
    * - Application Tier
      - Messaging Tier
      - 5672
      - TCP
      - AMQP non-TLS connections
    * - Application Tier
      - Messaging Tier
      - 5671
      - TCP
      - AMQPS TLS enabled connections
    * - Messaging Tier
      - Messaging Tier
      - 25672
      - TCP
      - Inter-node and CLI tool communication
    * - Administrator Web Browser
      - RabbitMQ Server Management
      - 15672
      - TCP
      - Management plugin
    * - Administrator Web Browser
      - RabbitMQ Server Management
      - 15671
      - TCP
      - Management plugin SSL
    * - Messaging Tier Cluster Node
      - Messaging Tier Cluster Nodes
      - 4369
      - TCP
      - erlang (epmd) peer discovery service used by RabbitMQ nodes and CLI tools



Default Locations
`````````````````
|morpheus| follows several install location conventions. Below is a list of system defaults for convenient management:

* Installation Location: ``/opt/morpheus``
* Log Location: ``/var/log/morpheus``

  * Morpheus-UI: ``/var/log/morpheus/morpheus-ui``
  * NGINX: ``/var/log/morpheus/nginx``
  * Check Server: ``/var/log/morpheus/check-server``

*  User-defined install/config: ``/etc/morpheus/morpheus.rb``
