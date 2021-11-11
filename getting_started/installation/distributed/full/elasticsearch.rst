Elasticsearch
^^^^^^^^^^^^^

Sample Install of 3 node Elasticsearch Cluster on CentOS 7

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary.

.. IMPORTANT:: |morpheus| v4.1.2+ requires Elasticsearch v7.x.

Requirements
````````````

#. Three Existing CentOS 7+ nodes accessible to the Morpheus Appliance

#. Install Java on each node

   You can install the latest OpenJDK with the command:

   .. code-block:: bash

    sudo yum install java-1.8.0-openjdk.x86_64

   To verify your JRE is installed and can be used, run the command:

   .. code-block:: bash

    java -version

   The result should look like this:

   .. code-block:: bash

      Output of java -version
      openjdk version "1.8.0_65"
      OpenJDK Runtime Environment (build 1.8.0_65-b17)
      OpenJDK 64-Bit Server VM (build 25.65-b01, mixed mode)

Install Elasticsearch 7.x
`````````````````````````
.. important:: This is an example Elasticsearch Upgrade for reference only, and is not indicative of the upgrade procedure for every environment/user/customer/configuration.

#. On each ES node run the following to install Elasticsearch.

   .. code-block:: bash

    rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

   .. code-block:: bash

    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.6.2-x86_64.rpm

   .. code-block:: bash

    sudo rpm -Uhv elasticsearch-7.6.2-x86_64.rpm

#. If necessary, update permissions for the specified log and data paths

   .. code-block:: bash

    sudo chown -R elasticsearch:elasticsearch /var/log/elasticsearch/
    sudo chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/

#. Edit ``/etc/elasticsearch/elasticsearch.yml`` and update each node configuration accordingly. Please note several attributes differ in 7.x from 5.x.

   Node 1 Example (customer configurations will vary)

   .. code-block:: bash

    sudo vi /etc/elasticsearch/elasticsearch.yml

          #Sample elasticsearch.yml config. Adjusting values in elasticsearch.yml for each node in the cluster.
          #Note: Sample only, user configurations and requirements will vary.

          node.name: "es-node-01" ##unique name of this node
          network.host: 10.30.22.152 ##ip of this node
          http.port: 9200
          discovery.seed_hosts: ["10.30.22.152","10.30.22.153","10.30.22.154"] ## add all cluster node ip's
          cluster.initial_master_nodes: ["10.30.22.152","10.30.22.153","10.30.22.154"] ## add all cluster node ip's
          path.logs: /var/log/elasticsearch ## Or your preferred location.
          path.data: /usr/share/elasticsearch/ ## Or your preferred location.
          discovery.zen.minimum_master_nodes: 2

   Node 2 Example (customer configurations will vary)

   .. code-block:: bash

    sudo vi /etc/elasticsearch/elasticsearch.yml

          #Sample elasticsearch.yml config. Adjusting values in elasticsearch.yml for each node in the cluster.
          #Note: Sample only, user configurations and requirements will vary.

          node.name: "es-node-02" ##unique name of this node
          network.host: 10.30.22.153 ##ip of this node
          http.port: 9200
          discovery.seed_hosts: ["10.30.22.152","10.30.22.153","10.30.22.154"] ## add all cluster node ip's
          cluster.initial_master_nodes: ["10.30.22.152","10.30.22.153","10.30.22.154"] ## add all cluster node ip's
          path.logs: /var/log/elasticsearch ## Or your preferred location.
          path.data: /usr/share/elasticsearch/ ## Or your preferred location.
          discovery.zen.minimum_master_nodes: 2

   Node 3 Example (customer configurations will vary)

   .. code-block:: bash

    sudo vi /etc/elasticsearch/elasticsearch.yml

          #Sample elasticsearch.yml config. Adjusting values in elasticsearch.yml for each node in the cluster.
          #Note: Sample only, user configurations and requirements will vary.

          node.name: "es-node-03" ##unique name of this node
          network.host: 10.30.22.154 ##ip of this node
          http.port: 9200
          discovery.seed_hosts: ["10.30.22.152","10.30.22.153","10.30.22.154"] ## add all cluster node ip's
          cluster.initial_master_nodes: ["10.30.22.152","10.30.22.153","10.30.22.154"] ## add all cluster node ip's
          path.logs: /var/log/elasticsearch ## Or your preferred location.
          path.data: /usr/share/elasticsearch/ ## Or your preferred location.
          discovery.zen.minimum_master_nodes: 2

#. Save elasticsearch.yml

#. Start Elasticsearch on each node.

   .. code-block:: bash

    sudo service elasticsearch start

#. Verify cluster health

   .. code-block:: bash

    curl http://localhost:9200/_cluster/health

    or

    curl http://node_ip:9200/_cluster/health
