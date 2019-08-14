Installation
============

|morpheus| comes packaged as a ``debian`` or ``yum`` based package. The default configuration installs all required services on a single vm or bare metal node. Morpheus can be configured in a distributed architecture to use one or multiple external services, and multiple application nodes can be configured for High Availability configurations.

All components required for Morpheus are installed and configured by default during the Morpheus ``reconfigure`` command. The Morpheus config file, ``morpheus.rb``, can optionally be configured to point the Morpheus App to external services (distributed configuration).

Morpheus can optionally be configured to use external Database, Messaging, and/or Search Tiers. This means instead of installing, for example, MySQL on the same host as the Morpheus App, the Morpheus configuration file (morpheus.rb) is setup to point to an external MySQL host, cluster or service, and MySQL will not be installed or configured on the Appliance Host.

Configurations
--------------

- Single App Node
- Single App Node with Distributed Service(s)
- Clustered App Nodes with Distributed Database
- Multiple App Nodes with Distributed Services

Pros/Cons
^^^^^^^^^

Single Node
````````````

Advantages
 - Simple Installation
   - Morpheus Installs all required services
 - Simple Configuration
   - Morpheus configures all required services
 - Simple Maintenance
   - All service connections and credential are local
   - All logs are local
   - All Data is local (by default)
 - Not dependent on network connections for vital services
   - Facilitates speed and reliability
Disadvantages
   - Single point of failure
   - Individual services cannot be scaled
   - Upgrades require (minimal) downtime
   - Single region

Single App Node with Distributed Service(s)
````````````````````````````````````````````

Advantages
 - Individual services can be scaled
 - Managed Services such as RDS can be utilized
Disadvantages
 - Single region
 - External services require additional configuration and maintenance
 - Morpheus is subject to network performance, configuration and availability
 - Increased Installation time possible

Clustered App Nodes with Distributed Database
``````````````````````````````````````````````

Advantages
 - Database can be scaled vertically and/or horizontally
 - Managed Services such as RDS can be utilized
 - Zero down time upgrades
 - No single point of failure
 - RabbitMQ and Elasticsearch Clusters
Disadvantages
 - External Database services requires additional configuration and maintenance
 - App node Clustering requires additional configuration and maintenance
 - Extended Installation time
 - Increased Infrastructure requirements
 - Load Balancer required to front App Nodes
 - Shared Storage configuration required

Multiple App Nodes with Distributed Services
`````````````````````````````````````````````

Advantages
 - Individual services can be scaled vertically and/or horizontally
 - Managed Services such as RDS can be utilized
 - Zero down time upgrades
 - No single point of failure
 - Multi region support
Disadvantages
 - External services require additional configuration and maintenance
 - Extended Installation time
 - Increased Infrastructure Requirements
 - Increased Networking requirements
 - Load Balancer required to front App Nodes
 - Shared Storage configuration required
 - Rabbit Load balancer required

.. include:: /getting_started/installation/singleNode/singleNode.rst
.. include:: /getting_started/installation/distributed/distributed.rst
