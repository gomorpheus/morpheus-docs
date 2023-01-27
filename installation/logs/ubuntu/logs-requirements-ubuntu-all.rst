Requirements
````````````

- Elasticsearch requires the following TCP ports for the cluster nodes. Please create the appropriate firewall rules on your
Percona nodes.

  - 9200
  - 9300

  .. code-block:: bash

    ufw allow 9200,9300/tcp

- Three RHEL 8 nodes accessible to the Morpheus Appliance