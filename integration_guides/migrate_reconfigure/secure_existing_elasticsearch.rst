Enable Secure Elasticsearch on an Existing Morpheus Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    This guide assumes a 3-node HA configuration but can be adapated to a single node

.. include:: /installation/app/3-node-ha/securing-elasticsearch.rst
    :start-after: Content-Begin
    :end-before: Content-End

#. On ``Node 1``, note/save the ``morpheus_password`` and the ``elastic_password`` from the ``/etc/morpheus/morpheus-secrets.json`` file in the ``elasticsearch`` section.  This same username and password will be used on all three nodes

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 1

         .. code-block:: bash
      
            cat /etc/morpheus/morpheus.rb
    
    Example output of the ``elasticsearch`` section:

        .. code-block:: json
      
            {
                "elasticsearch": {
                    "keystore_password": "e04cddda73855c4eb0bb68bee19b2647417f",
                    "truststore_password": "f4d42ce9e05156470ad837b5215d502ccca0",
                    "elastic_password": "b512bb1fe07e2004366ff4f990f0ee1dd7c8",
                    "morpheus_password": "660f9cb0363a1c9a38299f4f"
                }
            }

#. On ``All Nodes``, modify the ``/etc/morpheus/morpheus.rb`` file and add the following lines

    .. code-block:: ruby

        elasticsearch['secure_mode'] = true  # enables both username/password auth and TLS
        elasticsearch['use_tls'] = true  # instructs Morpheus to use HTTPS/TLS when connecting
        elasticsearch['truststore_path'] = '/var/opt/morpheus/certs/elastic-stack-ca.p12'  # the generated CA certificate
        elasticsearch['truststore_password'] = 'myfakepassword'  # password on the generated CA certificate
        elasticsearch['elastic_password'] = 'b512bb1fe07e2004366ff4f990f0ee1dd7c8'  # elastic_password from Node 1 morpehus-secret.json
        elasticsearch['morpheus_password'] = '660f9cb0363a1c9a38299f4f'  # morpheus_password from Node 1 morpehus-secret.json
        
#. On ``All Nodes``, stop the ``morpheus-ui`` and ``elasticsearch`` services

    .. code-block:: ruby

        morpheus-ctl stop morpheus-ui
        morpheus-ctl stop elasticsearch

.. note::
      For the next step, utilize a 4th terminal window.  When the nodes are reconfiguring, they will be hung waiting for Elasticsearch to start
      and the additional window will be used to connect to the node and start the service.  This avoids an error when reconfiguring and running
      the reconfigure multiple times.

#. Reconfigure ``Node 1`` and wait for the ``ruby_block[elasticsearch_wait]`` block, which the reconfigure will stop at

#. Using the 4th terminal window mentioned above, SSH to ``Node 1`` and run the following:

    .. code-block:: bash

        morpheus-ctl start elasticsearch

#. Repeat the reconfigure process and 4th terminal window method on the remaining two nodes

#. All nodes should come up and join the cluster as they were before

#. Verify the cluster using the following example commands for a (or all) nodes, now using auth (username/password seen above) and TLS

    .. code-block:: bash

        curl -k -u morpheus:660f9cb0363a1c9a38299f4f -X GET "https://localhost:9200/_cluster/health?pretty"
        curl -k -u morpheus:660f9cb0363a1c9a38299f4f -X GET "https://localhost:9200/_cat/nodes?v=true"

#. Additional troubleshooting can be done for the ``elasticsearch`` service by invtestigating the ``/var/log/morpheus/elasticsearch/current`` log

#. Once the cluster is up and running successfully, start the ``morpheus-ui`` service

    .. code-block:: bash

        morpheus-ctl start morpheus-ui