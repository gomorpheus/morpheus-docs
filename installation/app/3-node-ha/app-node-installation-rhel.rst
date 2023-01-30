App Node Installation
^^^^^^^^^^^^^^^^^^^^^

#. First begin by downloading and installing the requisite |morpheus| packages to the |morpheus| nodes.

   .. note:: For offline or nodes that cannot reach |repo_host_url|, both the standard and supplemental packages will need to be transferred and then installed on the |morpheus| nodes.

   .. note:: |morpheus| packages can be found in the Downloads section of the `Morpheus Hub <https://morpheushub.com/download>`_

   .. content-tabs::

      .. tab-container:: tab1
         :title: All Nodes

         .. include:: /installation/app/morpheus-install-rhel.rst

#. Do NOT run reconfigure yet. The |morpheus| configuration file must be edited prior to the initial reconfigure.

#. Next you will need to edit the |morpheus| configuration file ``/etc/morpheus/morpheus.rb`` on each node.

   .. include:: /installation/app/3-node-ha/3-node-ha-morpheus_rb-config.rst

   .. note:: The configurations above for ```mysql['host']`` shows a list of hosts, if the database has multiple endpoints.  Like other options in the configuration, ``mysql['host']`` can be a single entry, if the database has a single endpoint:  ``mysql['host'] = 'myDbEndpoint.example.com`` or ``mysql['host'] = '10.100.10.111'``
   
   .. important:: The elasticsearch node names set in ``elasticsearch['node_name']`` must match the host entries in elasticsearch['es_hosts']. ``node_name`` is used for ``node.name`` and ``es_hosts`` is used for ``cluster.initial_master_nodes`` in the generated elasticsearch.yml config. Node names that do not match entries in cluster.initial_master_nodes will cause clustering issues.

   .. important:: The rabbitmq['node_name'] in the Node 1 example above is **rabbit@node01**.  The shortname for the server of node01 must be resolvable by DNS or /etc/hosts of all other hosts, same for node02 and node03.  FQDNs cannot be used here

#. Reconfigure on all nodes

   .. content-tabs::

      .. tab-container:: tab1
         :title: All Nodes

         .. code-block:: bash

            [root@node-[1/2/3] ~] morpheus-ctl reconfigure

   |morpheus| will come up on all nodes and Elasticsearch will auto-cluster. The only item left is the manual clustering of RabbitMQ.