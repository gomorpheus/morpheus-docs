#. Stop and enable elasticsearch service

    .. code-block:: bash

        systemctl stop elasticsearch
        systemctl enable elasticsearch

#. Edit ``/etc/elasticsearch/elasticsearch.yml`` and update each node configuration accordingly. Please note several attributes differ in 7.x from 5.x.

   .. note:: Configurations will vary

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 1

         .. code-block:: bash

            vi /etc/elasticsearch/elasticsearch.yml

               #Sample elasticsearch.yml config. Adjusting values in elasticsearch.yml for each node in the cluster.
               #Note: Sample only, user configurations and requirements will vary.

               node.name: "es-node-01" ##unique name of this node, does not need to be resolvable
               network.host: 10.10.10.11 ##ip of this node
               discovery.seed_hosts: ["10.10.10.11","10.10.10.12","10.10.10.13"] ## add all cluster node ip's
               cluster.initial_master_nodes: ["10.10.10.11","10.10.10.12","10.10.10.13"] ## add all cluster node ip's
               discovery.zen.minimum_master_nodes: 2
         
      .. tab-container:: tab2
         :title: Node 2
         
         .. code-block:: bash

            vi /etc/elasticsearch/elasticsearch.yml

               #Sample elasticsearch.yml config. Adjusting values in elasticsearch.yml for each node in the cluster.
               #Note: Sample only, user configurations and requirements will vary.

               node.name: "es-node-01" ##unique name of this node, does not need to be resolvable
               network.host: 10.10.10.12 ##ip of this node
               discovery.seed_hosts: ["10.10.10.11","10.10.10.12","10.10.10.13"] ## add all cluster node ip's
               cluster.initial_master_nodes: ["10.10.10.11","10.10.10.12","10.10.10.13"] ## add all cluster node ip's
               discovery.zen.minimum_master_nodes: 2

      .. tab-container:: tab3
         :title: Node 3
         
         .. code-block:: bash

            vi /etc/elasticsearch/elasticsearch.yml

               #Sample elasticsearch.yml config. Adjusting values in elasticsearch.yml for each node in the cluster.
               #Note: Sample only, user configurations and requirements will vary.

               node.name: "es-node-01" ##unique name of this node, does not need to be resolvable
               network.host: 10.10.10.13 ##ip of this node
               discovery.seed_hosts: ["10.10.10.11","10.10.10.12","10.10.10.13"] ## add all cluster node ip's
               cluster.initial_master_nodes: ["10.10.10.11","10.10.10.12","10.10.10.13"] ## add all cluster node ip's
               discovery.zen.minimum_master_nodes: 2

|
   The following options can be also modified to change directory locations for the data and logs:

   - ``path.logs`` (default = /var/log/elasticsearch)
   - ``path.data`` (default = /var/lib/elasticsearch/)
   - ``http.port`` (default = 9200)

#. Start Elasticsearch on each node.

    .. code-block:: bash

        systemctl start elasticsearch

#. Verify cluster health

    .. code-block:: bash

        curl http://node_ip:9200/_cluster/health
    
        or

        curl http://localhost:9200/_cluster/health