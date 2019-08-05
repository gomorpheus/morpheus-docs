Elasticsearch
-------------

Install 3 node Elasticsearch Cluster on Centos 7

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary.

Requirements
^^^^^^^^^^^^

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

Installation
^^^^^^^^^^^^

To install Elasticsearch please use the following instructions

https://www.elastic.co/guide/en/elasticsearch/reference/current/rpm.html#install-rpm


Once installed, to make sure Elasticsearch starts and stops automatically, add its init script to the default runlevels with the command:

.. code-block:: bash

 sudo systemctl enable elasticsearch.service

Configuring Elastic
^^^^^^^^^^^^^^^^^^^

   Now that Elasticsearch and its Java dependencies have been installed, it is time to configure Elasticsearch.

   The Elasticsearch configuration files are in the ``/etc/elasticsearch`` directory. There are two files:

   .. code-block:: bash

    sudo vi /etc/elasticsearch/elasticsearch.yml

   elasticsearch.yml
    Configures the Elasticsearch server settings. This is where all options, except those for logging, are stored, which is why we are mostly interested in this file.

   logging.yml
    Provides configuration for logging. In the beginning, you don't have to edit this file. You can leave all default logging options. You can find the resulting logs in ``/var/log/elasticsearch`` by default.

   The first variables to customize on any Elasticsearch server are ``node.name`` and ``cluster.name`` in ``elasticsearch.yml``. As their names suggest, node.name specifies the name of the server (node) and the cluster to which the latter is associated.

   .. important:: Make sure to uncomment each of the following listed below in `/etc/elasticsearch/elasticsearch.yml`



   Node 1

   .. code-block:: yaml

    cluster.name: morpheusha1
    node.name: "morpheuses1"
    network.host: enter the IP of the node ex: 10.30.22.130
    http.port: 9200
    discovery.zen.ping.unicast.hosts: ["10.30.20.91","10.30.20.149","10.30.20.165"]

   Node 2

   .. code-block:: yaml

     cluster.name: morpheusha1
     node.name: "morpheuses2"
     network.host: enter the IP of the node ex: 10.30.22.130
     http.port: 9200
     discovery.zen.ping.unicast.hosts: ["10.30.20.91","10.30.20.149","10.30.20.165"]

   Node 3

   .. code-block:: yaml

     cluster.name: morpheusha1
     node.name: "morpheuses3"
     network.host: enter the IP of the node ex: 10.30.22.130
     http.port: 9200
     discovery.zen.ping.unicast.hosts: ["10.30.20.91","10.30.20.149","10.30.20.165"]

   For the above changes to take effect, you will have to restart Elasticsearch with the command:

   .. code-block:: bash

    sudo service elasticsearch restart

   Next restart the network with the command:

   .. code-block:: bash

    sudo service network restart

Testing
^^^^^^^

To make sure Elasticsearch is running use the following commands

https://www.elastic.co/guide/en/elasticsearch/reference/current/rpm.html#rpm-check-running
