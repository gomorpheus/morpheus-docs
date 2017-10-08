Elasticsearch
-------------

Install 3 node Elasticsearch Cluster on Centos 7

.. IMPORTANT:: This is a sample configuraiton only. Customer configuraitons and requirements will vary. 

Requirements
^^^^^^^^^^^^

#. Three Existing Cenots 7+ nodes accessible to the Morpheus Appliance

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

Installation
^^^^^^^^^^^^

#. Download and Install Elasticsearch

   Elasticsearch can be downloaded directly from elastic.co in zip, tar.gz, deb, or rpm packages. For CentOS, it's best to use the native rpm package which will install everything you need to run Elasticsearch. Download it in a directory of your choosing with the command:

   .. code-block:: bash

    wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.3.noarch.rpm

   Then install it in the usual CentOS way with the rpm command like this:

   .. code-block:: bash

    sudo rpm -ivh elasticsearch-1.7.3.noarch.rpm

   This results in Elasticsearch being installed in /usr/share/elasticsearch/ with its configuration files placed in /etc/elasticsearch and its init script added in /etc/init.d/elasticsearch.

   To make sure Elasticsearch starts and stops automatically, add its init script to the default runlevels with the command:

   .. code-block:: bash

    sudo systemctl enable elasticsearch.service

#. Configuring Elastic

   Now that Elasticsearch and its Java dependencies have been installed, it is time to configure Elasticsearch.

   The Elasticsearch configuration files are in the /etc/elasticsearch directory. There are two files:

   .. code-block:: bash

    sudo vi /etc/elasticsearch/elasticsearch.yml

   elasticsearch.yml
    Configures the Elasticsearch server settings. This is where all options, except those for logging, are stored, which is why we are mostly interested in this file.

   logging.yml
    Provides configuration for logging. In the beginning, you don't have to edit this file. You can leave all default logging options. You can find the resulting logs in /var/log/elasticsearch by default.

   The first variables to customize on any Elasticsearch server are node.name and cluster.name in elasticsearch.yml. As their names suggest, node.name specifies the name of the server (node) and the cluster to which the latter is associated.

   Node 1

   .. code-block:: bash

    cluster.name: morpheusha1
    node.name: "morpheuses1"
    discovery.zen.ping.unicast.hosts: ["10.30.20.91","10.30.20.149","10.30.20.165"]

   Node 2

   .. code-block:: bash

     cluster.name: morpheusha1
     node.name: "morpheuses2"
     discovery.zen.ping.unicast.hosts: ["10.30.20.91","10.30.20.149","10.30.20.165"]

   Node 3

   .. code-block:: bash

     cluster.name: morpheusha1
     node.name: "morpheuses3"
     discovery.zen.ping.unicast.hosts: ["10.30.20.91","10.30.20.149","10.30.20.165"]

   For the above changes to take effect, you will have to restart Elasticsearch with the command:

   .. code-block:: bash

    sudo service elasticsearch restart

#. Testing

   By now, Elasticsearch should be running on port 9200. You can test it with curl, the command line client-side URL transfers tool and a simple GET request like this:

   .. code-block:: bash

    [~]$ sudo curl -X GET 'http://10.30.20.149:9200'
          {
            "status" : 200,
            "name" : "morpheuses1",
            "cluster_name" : "morpheusha1",
            "version" : {
              "number" : "1.7.3",
              "build_hash" : "05d4530971ef0ea46d0f4fa6ee64dbc8df659682",
              "build_timestamp" : "2015-10-15T09:14:17Z",
              "build_snapshot" : false,
              "lucene_version" : "4.10.4"
            },
