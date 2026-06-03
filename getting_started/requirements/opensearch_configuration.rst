OpenSearch Configuration
========================

Starting with |morpheus| 8.1.0, the embedded search service changes from Elasticsearch to OpenSearch. All HPE Morpheus VM Essentials Software versions already use OpenSearch — this change only affects |morpheus| appliance upgrades. Hewlett Packard Enterprise continues to support both Elasticsearch and OpenSearch for external clusters.

During upgrade, the reconfigure process will:

- Automatically disable the old Elasticsearch service
- Start OpenSearch in its place
- Migrate the Elasticsearch PKCS12 CA to PEM format if ``secure_mode`` is enabled

No changes to ``/etc/morpheus/morpheus.rb`` are required. Existing ``elasticsearch[...]`` settings are bridged to the ``opensearch`` namespace automatically (see Notes for details on key precedence).

Data (indices) must be migrated separately using ``morpheus-ctl migrate-elasticsearch`` (see upgrade sections below, or run ``morpheus-ctl migrate-elasticsearch help`` on an appliance after upgrade for more info).

What the Settings Control
-------------------------

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Setting
     - opensearch.yml
     - Purpose
   * - ``enable``
     - —
     - Enable/disable the embedded OpenSearch service. Set to ``false`` when using an external cluster. Default ``true``.
   * - ``es_hosts``
     - ``cluster.initial_master_nodes``, ``discovery.seed_hosts``
     - Cluster membership and discovery. For external clusters, lists the external hosts.
   * - ``node_name``
     - ``node.name``
     - Unique name for this node within the cluster.
   * - ``host``
     - ``network.host`` or ``network.bind_host``
     - Interface to bind to. Default ``127.0.0.1``. Set to ``0.0.0.0`` for cluster use.
   * - ``publish_ip``
     - ``network.publish_host``
     - The IP other nodes use to reach this node. Falls back to Ohai's ``node['ipaddress']`` if not set.
   * - ``secure_mode``
     - ``plugins.security.disabled: false``, TLS config
     - Enables TLS on HTTP and transport layers, generates certs, runs securityadmin.sh.
   * - ``cluster``
     - ``cluster.name``
     - Cluster name. Defaults to ``morpheus``. Must be the same on all nodes.
   * - ``use_tls``
     - —
     - Connect to OpenSearch over HTTPS. Automatically set to ``true`` when ``secure_mode`` is enabled on the embedded service. Set manually for external TLS clusters.
   * - ``auth_user``
     - —
     - Username for Morpheus to authenticate with OpenSearch. Used for external clusters. When nil and ``secure_mode`` is enabled, the auto-created ``morpheus`` internal user is used.
   * - ``auth_password``
     - —
     - Password for ``auth_user``. Used for external clusters.
   * - ``replica_count``
     - ``numberOfReplicas``
     - Number of index replicas. Default ``1``. Set to ``0`` for single-node deployments.
   * - ``admin_dn``
     - ``plugins.security.authcz.admin_dn``
     - Distinguished name for the admin certificate. Defaults to ``O=Morpheus,OU=Ops,CN=<node_name>``.
   * - ``nodes_dn``
     - ``plugins.security.nodes_dn``
     - Distinguished name for trusted node certificates. Defaults to ``O=Morpheus,OU=Ops,CN=<node_name>``.

Ports
-----

For embedded clusters, ensure the following ports are open between all cluster nodes:

- **9200** — HTTP (client queries)
- **9300** — Transport (inter-node communication and cluster formation)

Notes
-----

- You can use either ``elasticsearch[...]`` or ``opensearch[...]`` keys in ``morpheus.rb``. The ``elasticsearch`` keys are bridged to ``opensearch`` automatically. If the same key is set under both namespaces, the ``opensearch[...]`` value takes precedence.
- The reconfigure strips ``127.0.0.1`` from ``es_hosts`` when more than one host is present, so you don't need to exclude it.
- In secure mode, ``admin_dn`` and ``nodes_dn`` default to ``O=Morpheus,OU=Ops,CN=<node_name>`` and are set automatically per node. These only need to be overridden when using custom certificates (see below).

Custom Certificates (admin_dn and nodes_dn)
-------------------------------------------

When using your own certificates instead of the auto-generated ones, set ``admin_dn`` and ``nodes_dn`` to match the subject DN of your certificates. These values map to ``plugins.security.authcz.admin_dn`` and ``plugins.security.nodes_dn`` in ``opensearch.yml``.

- ``admin_dn`` — Identifies the certificate authorized to run administrative operations (e.g., ``securityadmin.sh``). Only requests signed by a certificate matching this DN can modify the security index.
- ``nodes_dn`` — Identifies certificates trusted for inter-node transport communication. Nodes will reject transport connections from certificates that don't match.

To extract the subject DN from an existing certificate:

.. code-block:: bash

   openssl x509 -in /path/to/cert.pem -noout -subject -nameopt RFC2253

Set the values in ``/etc/morpheus/morpheus.rb`` on each node:

.. code-block:: ruby

   opensearch['admin_dn'] = 'CN=admin,OU=MyTeam,O=MyOrg'
   opensearch['nodes_dn'] = 'CN=node,OU=MyTeam,O=MyOrg'

If the admin and node certificates share the same DN (common when a single wildcard or shared cert is used), both values can be set to the same string. With the default auto-generated certificates, these are set to ``O=Morpheus,OU=Ops,CN=<node_name>`` per node and do not need to be configured manually.

Setting the Morpheus User Password
-----------------------------------

When ``secure_mode`` is enabled, reconfigure creates an internal OpenSearch user named ``morpheus`` that |morpheus| uses to authenticate with OpenSearch. The password for this user is auto-generated and stored in ``/etc/morpheus/morpheus-secrets.json`` under the ``elasticsearch.morpheus_password`` key. No manual configuration is needed in the default case.

To set a custom password, add it to ``/etc/morpheus/morpheus.rb`` on each node:

.. code-block:: ruby

   opensearch['morpheus_password'] = 'my-custom-password'

Encrypting the Password
------------------------

Passwords in ``morpheus.rb`` can be stored in encrypted form using the ``ENC{...}`` wrapper. During reconfigure, the recipe detects the ``ENC`` prefix and decrypts the value automatically. Plaintext values are used as-is.

To generate an encrypted string:

.. code-block:: bash

   morpheus-ctl get-crypto-string string 'my-custom-password'

This outputs an encrypted value that can be used in ``morpheus.rb``:

.. code-block:: ruby

   opensearch['morpheus_password'] = 'ENC{aBcDeFgHiJkLmNoPqRsTuVwXyZ...}'

The encryption uses the appliance's ``encryption_key_suffix`` (from ``/etc/morpheus/morpheus-secrets.json``), so the encrypted value is specific to that appliance. All nodes in the cluster share the same secrets file contents, so the same encrypted string works on all nodes.

Any password setting in ``morpheus.rb`` supports this format (under either the ``opensearch[...]`` or ``elasticsearch[...]`` namespace), including ``morpheus_password`` and ``auth_password``. As with other settings, ``opensearch[...]`` takes precedence over ``elasticsearch[...]`` if both are set.

Single Node
-----------

A single-node setup uses the embedded OpenSearch service with default settings. No ``morpheus.rb`` changes are required unless enabling secure mode.

Single Node — Fresh Install
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The embedded OpenSearch service starts automatically after the initial reconfigure. No configuration is needed:

.. code-block:: bash

   morpheus-ctl reconfigure

To enable secure mode, add to ``/etc/morpheus/morpheus.rb``:

.. code-block:: ruby

   opensearch['secure_mode'] = true

Single Node — Upgrading from Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1 — Upgrade the Morpheus package**

Install the new |morpheus| package. Do **NOT** run reconfigure yet.

**Step 2 — Run the migration script**

For single-node Morpheus appliances, the migration script handles everything automatically. Run ``sudo morpheus-ctl migrate-elasticsearch``. This script does the following:

#. Start a temporary Elasticsearch instance using the preserved ES installation
#. Reset voting configuration if needed (for nodes which were previously part of a cluster)
#. Set replicas to 0 for single-node operation
#. Export all indices to JSON files
#. Import into OpenSearch
#. Stop the temporary ES cluster

**Step 3 — Reconfigure**

.. code-block:: bash

   morpheus-ctl reconfigure

The old Elasticsearch service is disabled automatically (if necessary) and OpenSearch starts in its place. If ``secure_mode`` was enabled, the Elasticsearch PKCS12 CA is automatically migrated to PEM format.

3-Node Embedded Cluster
-----------------------

Prerequisites
^^^^^^^^^^^^^

**Networking**

- All 3 nodes must be able to reach each other on:

  - **Port 9200 (TCP)** — HTTP API (client queries, health checks)
  - **Port 9300 (TCP)** — Transport (inter-node communication, cluster formation, shard replication)

- Each node needs a stable, routable IP address or resolvable hostname that the other nodes can reach (no NAT between nodes)
- Both IP addresses and hostnames are supported in ``es_hosts`` and ``publish_ip``

**Configuration**

- Each node must have:

  - The same ``es_hosts`` hash listing all 3 nodes
  - A unique ``node_name``
  - A unique ``publish_ip`` matching that node's routable IP
  - ``host`` set to ``0.0.0.0`` (default ``127.0.0.1`` only listens locally and will not allow cluster formation)

- All nodes must share the same ``cluster`` name (defaults to ``morpheus`` — only set this if you need to change it)

**Secure Mode**

- When ``secure_mode`` is enabled, TLS is used on both HTTP and transport layers
- All nodes must share the **same root CA** — Node 1 must be reconfigured first to generate the CA, then the CA files are copied to the remaining nodes before their first reconfigure
- Each node auto-generates its own node certificate signed by the shared CA

**Example nodes:**

- Node 1: ``10.0.0.1`` (morpheus-1)
- Node 2: ``10.0.0.2`` (morpheus-2)
- Node 3: ``10.0.0.3`` (morpheus-3)

Fresh Install — Without Secure Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: ``elasticsearch[...]`` keys can also be used in place of ``opensearch[...]`` on fresh installs. They are bridged automatically.

**Node 1** — ``/etc/morpheus/morpheus.rb``:

.. code-block:: ruby

   opensearch['es_hosts'] = {'10.0.0.1' => 9200, '10.0.0.2' => 9200, '10.0.0.3' => 9200}
   opensearch['node_name'] = 'morpheus-1'
   opensearch['host'] = '0.0.0.0'
   opensearch['publish_ip'] = '10.0.0.1'

**Node 2** — ``/etc/morpheus/morpheus.rb``:

.. code-block:: ruby

   opensearch['es_hosts'] = {'10.0.0.1' => 9200, '10.0.0.2' => 9200, '10.0.0.3' => 9200}
   opensearch['node_name'] = 'morpheus-2'
   opensearch['host'] = '0.0.0.0'
   opensearch['publish_ip'] = '10.0.0.2'

**Node 3** — ``/etc/morpheus/morpheus.rb``:

.. code-block:: ruby

   opensearch['es_hosts'] = {'10.0.0.1' => 9200, '10.0.0.2' => 9200, '10.0.0.3' => 9200}
   opensearch['node_name'] = 'morpheus-3'
   opensearch['host'] = '0.0.0.0'
   opensearch['publish_ip'] = '10.0.0.3'

**Apply**

Run on all three nodes:

.. code-block:: bash

   morpheus-ctl reconfigure

Nodes can be reconfigured in any order. The cluster will form once all nodes are up and can reach each other on ports 9200 and 9300.

Fresh Install — With Secure Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: ``elasticsearch[...]`` keys can also be used in place of ``opensearch[...]`` on fresh installs. They are bridged automatically.

Secure mode enables TLS on both the HTTP and transport layers. Each node generates its own node certificate, but all nodes must share the **same root CA** so they trust each other.

**Step 1 — Configure and reconfigure Node 1 first**

Node 1 — ``/etc/morpheus/morpheus.rb``:

.. code-block:: ruby

   opensearch['es_hosts'] = {'10.0.0.1' => 9200, '10.0.0.2' => 9200, '10.0.0.3' => 9200}
   opensearch['node_name'] = 'morpheus-1'
   opensearch['host'] = '0.0.0.0'
   opensearch['publish_ip'] = '10.0.0.1'
   opensearch['secure_mode'] = true

Run reconfigure on Node 1:

.. code-block:: bash

   morpheus-ctl reconfigure

This generates the root CA and node certificate at:

- ``/opt/morpheus/embedded/opensearch-2.18.0/config/root-ca.pem``
- ``/opt/morpheus/embedded/opensearch-2.18.0/config/root-ca-key.pem``

**Step 2 — Copy the root CA to Nodes 2 and 3**

Copy both CA files from Node 1 to the same path on Nodes 2 and 3 **before** running reconfigure on them:

.. code-block:: bash

   # From Node 1:
   scp /opt/morpheus/embedded/opensearch-2.18.0/config/root-ca.pem     node2:/opt/morpheus/embedded/opensearch-2.18.0/config/
   scp /opt/morpheus/embedded/opensearch-2.18.0/config/root-ca-key.pem  node2:/opt/morpheus/embedded/opensearch-2.18.0/config/

   scp /opt/morpheus/embedded/opensearch-2.18.0/config/root-ca.pem     node3:/opt/morpheus/embedded/opensearch-2.18.0/config/
   scp /opt/morpheus/embedded/opensearch-2.18.0/config/root-ca-key.pem  node3:/opt/morpheus/embedded/opensearch-2.18.0/config/

Set ownership on Nodes 2 and 3:

.. code-block:: bash

   chown morpheus-es:morpheus-es /opt/morpheus/embedded/opensearch-2.18.0/config/root-ca*.pem

**Step 3 — Configure and reconfigure Nodes 2 and 3**

Node 2 — ``/etc/morpheus/morpheus.rb``:

.. code-block:: ruby

   opensearch['es_hosts'] = {'10.0.0.1' => 9200, '10.0.0.2' => 9200, '10.0.0.3' => 9200}
   opensearch['node_name'] = 'morpheus-2'
   opensearch['host'] = '0.0.0.0'
   opensearch['publish_ip'] = '10.0.0.2'
   opensearch['secure_mode'] = true

Node 3 — ``/etc/morpheus/morpheus.rb``:

.. code-block:: ruby

   opensearch['es_hosts'] = {'10.0.0.1' => 9200, '10.0.0.2' => 9200, '10.0.0.3' => 9200}
   opensearch['node_name'] = 'morpheus-3'
   opensearch['host'] = '0.0.0.0'
   opensearch['publish_ip'] = '10.0.0.3'
   opensearch['secure_mode'] = true

Run reconfigure on Nodes 2 and 3:

.. code-block:: bash

   morpheus-ctl reconfigure

Each node will skip CA generation (the files already exist) and generate its own node certificate signed by the shared CA.

Upgrading from a 3-Node Elasticsearch Cluster
----------------------------------------------

**Step 1 — Upgrade the Morpheus package**

Install the new Morpheus package on all 3 nodes. Do **not** run reconfigure yet. The preinstall script preserves the Elasticsearch installation at ``/var/opt/morpheus/elasticsearch-8.15.5/home/``. The ES data and binaries are preserved across package install, reconfigure, and normal operation, thus, the migration export can be run at any time until the ES data and binaries are removed with the export cleanup option (or manually removed).

**Step 2 — Check the ES cluster configuration**

Run ``cat /var/opt/morpheus/elasticsearch-8.15.5/home/config/elasticsearch.yml`` and note the ``discovery.seed_hosts`` and ``cluster.initial_master_nodes``. These are the cluster nodes.

**Step 3 — Start Elasticsearch on all nodes**

Start ES on each node within 30 seconds of each other. The order does not matter, they will discover each other:

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

External Cluster
----------------

When using an externally managed OpenSearch (or Elasticsearch) cluster, disable the embedded service and point Morpheus at the external hosts.

External Cluster — Fresh Install
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: ``elasticsearch[...]`` keys can also be used in place of ``opensearch[...]`` on fresh installs. They are bridged automatically.

Add the following to ``/etc/morpheus/morpheus.rb`` on each Morpheus appliance node:

.. code-block:: ruby

   opensearch['enable'] = false
   opensearch['es_hosts'] = {'os-node1.example.com' => 9200, 'os-node2.example.com' => 9200, 'os-node3.example.com' => 9200}
   opensearch['auth_user'] = 'morpheus'
   opensearch['auth_password'] = 'the-external-cluster-password'

If the external cluster uses TLS:

.. code-block:: ruby

   opensearch['use_tls'] = true

Then reconfigure:

.. code-block:: bash

   morpheus-ctl reconfigure

The embedded OpenSearch service will not be started. Morpheus will connect directly to the external cluster using the provided hosts and credentials.

- ``auth_user`` and ``auth_password`` are sent to the external cluster for authentication. These must match a user configured on the external cluster.
- ``auth_password`` supports the ``ENC{...}`` encrypted format (see Encrypting the password).
- Do not set ``secure_mode`` — that setting controls the embedded service's certificate generation and security plugin. For external TLS clusters, use ``use_tls`` instead.
- ``replica_count`` can be adjusted to match the external cluster's topology (default ``1``).

Upgrading with an External Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the existing Morpheus installation was already configured to use an external Elasticsearch or OpenSearch cluster, the upgrade is straightforward — no data migration is needed on the appliance side since the data lives on the external cluster. The external cluster does not need to be migrated to OpenSearch; Morpheus supports both.

**Step 1 — Upgrade the Morpheus package**

Install the new Morpheus package on each appliance node.

**Step 2 — Reconfigure**

No ``morpheus.rb`` changes are needed. The existing ``elasticsearch[...]`` settings are bridged automatically.

.. code-block:: bash

   morpheus-ctl reconfigure
