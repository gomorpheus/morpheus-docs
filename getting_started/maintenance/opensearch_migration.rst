.. _opensearch-migration:

Migrating from Elasticsearch to OpenSearch
------------------------------------------

Starting with |morpheus| 8.1.0, the embedded search service changed from Elasticsearch to OpenSearch. This migration only affects appliances upgrading from earlier versions — fresh installations and HVM deployments already use OpenSearch.

During upgrade, the reconfigure process will:

- Automatically disable the old Elasticsearch service
- Start OpenSearch in its place
- Migrate the Elasticsearch PKCS12 CA to PEM format if ``secure_mode`` is enabled

No changes to ``/etc/morpheus/morpheus.rb`` are required. Existing ``elasticsearch[...]`` settings are bridged to the ``opensearch`` namespace automatically.

.. important::

   Data (indices) must be migrated separately using ``morpheus-ctl migrate-elasticsearch``. Run ``morpheus-ctl migrate-elasticsearch help`` on an appliance after upgrade for full usage information.

Single Node — Upgrading from Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1 — Upgrade the Morpheus package**

Install the new |morpheus| package. Do **NOT** run reconfigure yet.

**Step 2 — Run the migration script**

For single-node appliances, the migration script handles everything automatically:

.. code-block:: bash

   sudo morpheus-ctl migrate-elasticsearch

This script does the following:

#. Starts a temporary Elasticsearch instance using the preserved ES installation
#. Resets voting configuration if needed (for nodes which were previously part of a cluster)
#. Sets replicas to 0 for single-node operation
#. Exports all indices to JSON files
#. Imports into OpenSearch
#. Stops the temporary ES cluster

**Step 3 — Reconfigure**

.. code-block:: bash

   morpheus-ctl reconfigure

The old Elasticsearch service is disabled automatically and OpenSearch starts in its place. If ``secure_mode`` was enabled, the Elasticsearch PKCS12 CA is automatically migrated to PEM format.

3-Node Cluster — Upgrading from Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1 — Upgrade the Morpheus package**

Install the new |morpheus| package on all 3 nodes. Do **not** run reconfigure yet. The preinstall script preserves the Elasticsearch installation at ``/var/opt/morpheus/elasticsearch-8.15.5/home/``. The ES data and binaries are preserved across package install, reconfigure, and normal operation — the migration export can be run at any time until the ES data is removed.

**Step 2 — Check the ES cluster configuration**

Run the following and note the ``discovery.seed_hosts`` and ``cluster.initial_master_nodes``:

.. code-block:: bash

   cat /var/opt/morpheus/elasticsearch-8.15.5/home/config/elasticsearch.yml

**Step 3 — Start Elasticsearch on all nodes**

Start ES on each node within 30 seconds of each other (order does not matter):

.. code-block:: bash

   su -s /bin/bash es-morpheus -c 'ES_JAVA_HOME=/var/opt/morpheus/elasticsearch-8.15.5/home/jdk /var/opt/morpheus/elasticsearch-8.15.5/home/bin/elasticsearch -d'

**Step 4 — Verify cluster health**

From any node:

.. code-block:: bash

   curl http://127.0.0.1:9200/_cluster/health?pretty

You should see: ``"status": "green"``, ``"number_of_nodes": 3``, ``"unassigned_shards": 0``

**Step 5 — Run the migration export**

From any node:

.. code-block:: bash

   sudo morpheus-ctl migrate-elasticsearch

The script will detect the running ES cluster and export from it.

**Step 6 — Stop Elasticsearch on all nodes**

After the migration completes, on each node:

.. code-block:: bash

   pkill -f 'elasticsearch-8.15.5'

**Step 7 — Reconfigure all nodes**

.. code-block:: bash

   morpheus-ctl reconfigure

External Cluster — Upgrading
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the existing |morpheus| installation was already configured to use an external Elasticsearch or OpenSearch cluster, the upgrade is straightforward — no data migration is needed on the appliance side since the data lives on the external cluster. The external cluster does not need to be migrated to OpenSearch; |morpheus| supports both.

**Step 1 — Upgrade the Morpheus package**

Install the new |morpheus| package on each appliance node.

**Step 2 — Reconfigure**

No ``morpheus.rb`` changes are needed. The existing ``elasticsearch[...]`` settings are bridged automatically.

.. code-block:: bash

   morpheus-ctl reconfigure
