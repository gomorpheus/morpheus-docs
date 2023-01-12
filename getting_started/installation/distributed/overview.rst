HA Installation Overview
^^^^^^^^^^^^^^^^^^^^^^^^

Morpheus provides a wide array of options when it comes to deployment architectures. It can start as a simple one machine instance where all services run on the same machine, or it can be split off into individual services per machine and configured in a high availability (HA) configuration, either in the same region or cross-region. Naturally, high availability can grow more complicated, depending on the configuration you want to do and this article will cover the basic concepts of the Morpheus HA architecture that can be used in a wide array of configurations. 

There are four primary tiers of services represented within the Morpheus appliance. They are the Application Tier, Transactional Database Tier, Non-Transactional Database Tier, and Messaging Tier. Each of these tiers have their own recommendations for High availability deployments.

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary.  Please contact your account manager if you wish to deploy or transition to a HA environment.

Application Tier
`````````````````
The application tier is easily installed with the same apt or yum repository package that Morpheus is normally distributed with. Advanced configuration allows for the additional tiers to be skipped and leave only the “stateless” services that need run. These stateless services include Nginx and Tomcat.  They can be configured across all regions and placed behind a central load-balancer or geo-based load balancer.  They typically connect to all other tiers as none of the other tiers talk to each other besides through the central application tier. One final piece when it comes to setting up the Application tier is shared storage, which is necessary when it comes to maintaining deployment archives, virtual image catalogs, backups, etc. These can be externalized to an object storage service such as Amazon S3 or Openstack Swiftstack as well. Alternatively, a simple NFS cluster can also be used to handle the shared storage structure.  Alternatively, supported (Platform as a Service) PaaS offerings can be used that provide a NFS compatible shared storage, eliminating the need to manage the underlying infrastructure.

Transactional Database Tier
````````````````````````````
The Transactional Database tier consists of a MySQL compatible database. It is recommended that a lockable clustered configuration be used, such as a Galera cluster, which can also provide high availability.  Alternatively, supported PaaS offerings can be used that provide a mySQL compatible database, eliminating the need to manage the underlying infrastructure.

Non-Transactional Database Tier
```````````````````````````````
The Non-Transactional tier consists of an Elasticsearch cluster. Elastic Search is used for log aggregation data and temporal aggregation data (essentially stats, metrics, and logs). This enables for a high write throughput at scale. ElasticSearch is a Clustered database meaning all nodes no matter the region need to be connected to each other over what they call a “Transport” protocol. It is fairly simple to get setup as all nodes are identical. It is also a java based system and does require a sizable chunk of memory for larger data sets.  Alternatively, supported PaaS offerings can be used that provide an Elasticsearch compatible deployment, eliminating the need to manage the underlying infrastructure.

Messaging Tier
``````````````
The Messaging tier is an AMQP based tier along with STOMP Protocol (used for agent communication). The primary model recommended is to use RabbitMQ for queue services. RabbitMQ is also a cluster-based queuing system and needs at least 3 instances for HA configurations. This is due to elections in the failover scenarios RabbitMQ can manage. If doing a cross-region HA RabbitMQ cluster it is recommended to have at least 3 Rabbit queue clusters per region. Typically to handle HA a RabbitMQ cluster should be placed between a load balancer and the front-end application server to handle cross host connections.  Alternatively, supported PaaS offerings can be used that provide a RabbitMQ compatible deployment, eliminating the need to manage the underlying infrastructure.

HA Installation Architectures
`````````````````````````````

3-Node HA (Recommended)
  In this architecture, all tiers are deployed on three machines by Morpheus during the installation, with the exception of the Transactional Database Tier.  This provides HA not just for the Morpheus Application Tier but all underlying tiers that support Morpheus.  The Transactional Database Tier will remain external, either as a separate cluster or PaaS, following the supported services.

Distributed HA
  In this architecture, the tiers do not need to reside on the same machines, each can be hosted by a supprted cluster or PaaS offering.  This provides flexibility and reuse of already existing technologies such as RabbitMQ or Elasticsearch.  Each tier should be architected to provide HA following the vendor's documentation, to ensure no downtime for the Morpheus Application Tier.