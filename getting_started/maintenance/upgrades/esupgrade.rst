.. _esupgrade:

Elasticsearch 7.x Upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^

.. important:: This is an example Elasticsearch Upgrade for reference only, and is not indicative of the upgrade procedure for every environment/user/customer/configuration. This example assumes CentOS hosts and will result in loss of existing Elasticsearch data and is the fastest upgrade path. Data retention is possible through alternate upgrade paths. Refer to `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before upgrading to v4.1.2 if your Appliance's Elasticsearch service is external.

Overview
````````
|morpheus| v4.1.2+ requires Elasticsearch 7.x. Earlier versions of |morpheus| ran against Elasticsearch v5.x. The Elasticsearch version for Appliance configurations with the default local Elasticsearch target will automatically be upgraded and no manual upgrade is required.

For Appliance configurations with an existing external Elasticsearch service, an upgrade of Elasticsearch to v7.x is required to upgrade |morpheus| to v4.1.2+. |morpheus| can be pointed to a new Elasticsearch 7.x service as an alternate to upgrading an existing cluster.

Elasticsearch 7.x upgrade is really a new install, as by default no data will be retained. Please refer to Elasticsearch documentation if backing up and restoring your 5.x Elasticsearch |morpheus| data is required. For most users, the log and stat data stored in Elasticsearch is not critical and the 5.x Elasticsearch data backup and restoration is not necessary.

.. important:: Elasticsearch 7.x configuration and paths are not the same as v5.x. Please pay attention to the elasticsearch.yml config changes and ensure proper permissions on specified paths.

Install Elasticsearch 7.x
`````````````````````````
.. important:: This is an example Elasticsearch Upgrade for reference only, and is not indicative of the upgrade procedure for every environment/user/customer/configuration. This example assumes CentOS hosts and will result in loss of existing Elasticsearch data and is the fastest upgrade path. Data retention is possible through alternate upgrade paths. Refer to `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before upgrading to v4.1.2 if your Appliance's Elasticsearch service is external.

.. important:: Upgrading from v5.x directly to 7.x requires all nodes in a Cluster to be stopped. The |morpheus| ui should be stopped prior to the cluster upgrade.


#. Stop Elasticsearch on all nodes in the Cluster

   .. code-block:: bash

    sudo -i service elasticsearch stop

#. On each ES node run the following to install Elasticsearch.

   .. code-block:: bash

    rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

   .. code-block:: bash

     wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.5.0-x86_64.rpm

   .. code-block:: bash

    sudo rpm -Uhv elasticsearch-7.5.0-x86_64.rpm

#. If necessary, update permissions for the specified log and data paths

   .. code-block:: bash

    sudo chown -R elasticsearch:elasticsearch /var/log/elasticsearch/
    sudo chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/

#. Edit ``/etc/elasticsearch/elasticsearch.yml`` and update each nodes configurations accordingly. Please note several attributes differ in 7.x from 5.x.

   .. code-block:: bash

    sudo vi /etc/elasticsearch/elasticsearch.yml

          #Sample elasticsearch.yml config. Adjusting values in elasticsearch.yml for each node in the cluster.
          #Note: Sample only, user configurations and requirements will vary.

          node.name: "es-node-01" ##unique name of this node
          network.host: 10.30.22.152 ##ip of this node
          http.port: 9200
          discovery.seed_hosts: ["10.30.22.152","10.30.22.153","10.30.22.154"] ## add all cluster node ip's
          cluster.initial_master_nodes: ["10.30.22.152","10.30.22.153","10.30.22.154"] ## add all cluster node ip's
          path.logs: /var/log/elasticsearch ## Ensure permissions on specified path
          path.data: /usr/share/elasticsearch ## Ensure permissions on specified path
          ## discovery.zen.minimum_master_nodes: 2 ##enabled after cluster is up

#. Save elasticsearch.yml
#. Start Elasticsearch on each node.

   .. code-block:: bash

    sudo service elasticsearch start

#. Once all nodes have joined the cluster, update ``/etc/elasticsearch/elasticsearch.yml`` and uncomment ``discovery.zen.minimum_master_nodes: 2`:

   .. code-block:: bash

    sudo vi /etc/elasticsearch/elasticsearch.yml

          #Sample elasticsearch.yml config. Adjusting values in elasticsearch.yml for each node in the cluster.
          #Note: Sample only, user configurations and requirements will vary.

          node.name: "es-node-01" ##unique name of this node
          network.host: 10.30.22.152 ##ip of this node
          http.port: 9200
          discovery.seed_hosts: ["10.30.22.152","10.30.22.153","10.30.22.154"] ## add all cluster node ip's
          cluster.initial_master_nodes: ["10.30.22.152","10.30.22.153","10.30.22.154"] ## add all cluster node ip's
          path.logs: /var/log/elasticsearch ## Ensure permissions on specified path
          path.data: /usr/share/elasticsearch ## Ensure permissions on specified path
          discovery.zen.minimum_master_nodes: 2 ##enabled after cluster is up

#. Save elasticsearch.yml

#. Restart Ealsticsearch service, one node at a time (2 nodes are now required to be running in the cluster at any give time)

   .. code-block:: bash

    sudo service elasticsearch restart

#. Verify cluster health

   .. code-block:: bash

    curl http://localhost:9200/_cluster/health

    or

    curl http://node_ip:9200/_cluster/health

#. Once the cluster status is green, |morpheus| can be upgraded to v4.1.2+. No configuration or port changes in morpheus.rb on the appliance nodes are required.
