Installation Overview
---------------------

.. important:: |morpheus| v4.2.0 enhanced security configuration restricts incoming appliance connections to TLS v1.2, potentially impacting front-end load balancer monitoring/health checks that support only TLS v1.1 or lower, as well as |morpheus| Agent installations for Windows nodes using .net versions that do not support TLS v1.2. Refer to TLS

	|morpheus| comes packaged as a ``debian`` or ``yum`` based package. The default configuration installs all required services on a single vm or bare metal Host. Morpheus can be configured in a distributed architecture to use one or multiple external services, and multiple application Hosts can be configured for High Availability configurations.

All components required for |morpheus| are installed and configured by default during the Morpheus ``reconfigure`` command. The Morpheus config file, ``morpheus.rb``, can optionally be configured to point the Morpheus App to external services (distributed configuration).

Morpheus can optionally be configured to use external Database, Messaging, and/or Search Tiers. This means instead of installing, for example, MySQL on the same host as the Morpheus App, the Morpheus configuration file (morpheus.rb) is setup to point to an external MySQL host, cluster or service, and MySQL will not be installed or configured on the Appliance Host.

Install Packages
^^^^^^^^^^^^^^^^

|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_

Configuration Options
^^^^^^^^^^^^^^^^^^^^^

- Single Host (All-In-One/default)
   All tiers running on a single host. The reconfigure process installs all required services. This is the default configuration.
- Single Hosts with Distributed Service(s)
   Transactional Database, Non-Transactional Database, and/or Message tiers are externalized, with the remaining services on a single host. The reconfigure process installs all services not set to false in ``/etc/morpheus/morpheus.rb``
- Clustered Hosts with Distributed Transactional Database (3-Node HA)
   Application, Message and Non-Transactional tiers are installed and clustered on three or more hosts, with all three hosts pointing to externalized database tier. The reconfigure process installs all services except mySQL.

Distributed Configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^

Morpheus provides an array of options when it comes to deployment architectures. It can start as a simple one machine instance where all services run on the same machine, or it can be configured in a high availability architecture where three or more clustered hosts point to an externalized database (either in the same region or cross-region). This article will cover the basic concepts of the Morpheus HA architecture.

There are four primary tiers of services represented within the Morpheus appliance. They are the Application Tier, Transactional Database Tier, Non-Transactional Database Tier, and Messaging Tier.

Application Tier
`````````````````
The application tier is easily installed with the same Debian or yum repository package that Morpheus is normally distributed with. Advanced configuration allows for the additional tiers to be skipped and leave only the “stateless” services that need run. These stateless services include Nginx and Tomcat. They can be configured across all regions and placed behind a central load-balancer or Geo based load-balancer. They typically connect to all other tiers as none of the other tiers talk to each other besides through the central application tier. One final piece when it comes to setting up the Application tier is a shared storage means is necessary when it comes to maintaining things like deployment archives, virtual image catalogs, backups, etc. These can be externalized to an object storage service such as Amazon S3 or Openstack Swiftstack as well. If not using those options a simple NFS cluster can also be used to handle the shared storage structure.

Transactional Database Tier
````````````````````````````
The Transactional database tier usually consists of a MySQL compatible database. It is recommended that a lockable clustered configuration be used (Currently Percona XtraDB Cluster is the most recommended in Permissive Mode). Refer to the setup documentation for your database platform for recommended installation and clustering steps. There are several documents online related to configuring and setting up an XtraDB Cluster but it most simply can be laid out in a many-master configuration. There can be some nodes setup with replication delay as well as some with no replication delay. It is common practice to have no replication delay within the same region and allow some replication delay cross region. This does increase the risk of job run overlap between the 2 regions however, the concurrent operations typically self-correct and this is a non-issue.

Non-Transactional Database Tier
```````````````````````````````
The Non-Transactional tier consists of an ElasticSearch (version |esver|) cluster. ElasticSearch is used for log aggregation data and temporal aggregation data (essentially stats, metrics, and logs). This enables for a high write throughput at scale. ElasticSearch is a Clustered database meaning all nodes no matter the region need to be connected to each other over what they call a “Transport” protocol. It is fairly simple to get setup as all nodes are identical.

Messaging Tier
``````````````
The Messaging tier is an AMQP-based tier along with STOMP Protocol (used for agent communication). The primary model recommended is to use RabbitMQ for queue services.

Pros/Cons
^^^^^^^^^
Single Host
```````````
Advantages
 - Simple Installation
   - Morpheus Installs all required services
 - Simple Configuration
   - Morpheus configures all required services
 - Simple Maintenance
   - All service connections and credentials are local
   - All logs are local
   - All Data is local (by default)
 - Not dependent on network connections for vital services
   - Facilitates speed and reliability
Disadvantages
   - Single point of failure
   - Individual services cannot be scaled
   - Upgrades require (minimal) downtime
   - Single region

Clustered Hosts with Distributed Transactional Database (3-Node HA)
```````````````````````````````````````````````````````````````````
Advantages
 - Database can be scaled vertically and/or horizontally
 - Managed Services such as RDS can be utilized
 - Zero down time upgrades
 - No single point of failure
 - RabbitMQ and Elasticsearch Clusters
Disadvantages
 - External Database services requires additional configuration and maintenance
 - App Host Clustering requires additional configuration and maintenance
 - Extended Installation time
 - Increased Infrastructure requirements
 - Load Balancer required to front App Hosts
 - Shared Storage configuration required
