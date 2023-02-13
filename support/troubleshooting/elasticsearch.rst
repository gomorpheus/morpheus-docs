Elasticsearch
^^^^^^^^^^^^^

This page is designed to help troubleshoot issues with Elasticsearch.  

Additional troubleshooting information:

    https://www.elastic.co/guide/en/elasticsearch/reference/master/troubleshooting.html

Log Locations
`````````````

    Embedded: ``/var/log/morpheus/elasticsearch/current``

    External cluster (default location): ``/var/log/elasticsearch/elasticsearch.log``

Common elasticsearch Commands
`````````````````````````````

    .. note:: Elasticsearch does not have commands but you interact with the API using commands such as ``curl``

    **Get Cluster Health**

        .. code-block:: bash

            curl -X GET "localhost:9200/_cluster/health?pretty"

            curl -X GET "localhost:9200/_cluster/health?level=shard?pretty"
    
    **Get Nodes**

        .. code-block:: bash

            curl -X GET "localhost:9200/_cat/nodes?v=true"

    **Get Individual or all Node(s) Info**

        .. code-block:: bash

            # Single node
            curl -X GET "localhost:9200/_nodes/<IPAddress or ID>/h=name?pretty"

            # All nodes
            curl -X GET "localhost:9200/_nodes/_all/h=name?pretty"

    **Get All Indicies**

        .. code-block:: bash

            curl -X GET "localhost:9200/_cat/indices"

    **Delete All Indicies**

        .. important:: This will **not** delete the indicies, it will just print out the commands needed to delete each one, if desired.  The resulting commands would need to be run to delete the indicies

        Be sure to replace the ``<pattern>`` in the below command with a pattern that pulls the indicies needed.

        .. code-block:: bash

            curl -X GET "localhost:9200/_cat/indices" | grep <pattern> | gawk '{print "curl -XDELETE https://10.60.1.32:9200/"$3}'

    **Get Shards and List Unassigned Fields**
        
        .. code-block:: bash

            curl -X GET "localhost:9200/_cat/shards?h=index,shard,state,unassigned,reason"
        	
        **Issue**

            If shards are UNASSIGNED, you may see the an error that says:

                ``"explanation" : "shard has exceeded the maximum number of retries [5] on failed allotcation attempts ... "``

            .. image:: /images/support/troubleshooting/elasticsearch_maximum_retries.png

        **Resolution**

            Retry the unassigned shards:
        
            .. code-block:: bash

            	curl -X POST "localhost:9200/_cluster/reroute?retry_failed=true

    **Increase Shard Limit from 1,000 to 2,000**

        Incease the shards per node:

            .. code-block:: bash

                curl -XPUT "localhost:9200/_cluster/settings" -H 'Content-Type: application/json' -d'
                {
                    "persistent" : {
                        "cluster.max_shards_per_node": "2000"
                    }
                }
                '

        Also, expand the replicas used with the shards change above:

            .. code-block:: bash

            	curl -XPUT "localhost:9200/_template/default_template" -H 'Content-Type: application/json' -d'
                {
                "index_patterns": ["*"],
                    "settings": {
                        "index": {
                        "number_of_replicas": 0,
                        "auto_expand_replicas": "0-1"
                        }
                    }
                }
                '