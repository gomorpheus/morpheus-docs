.. _external-opensearch:

OpenSearch
----------

OpenSearch provides log aggregation, metrics storage, and full-text search for |morpheus|. This page covers setting up and configuring OpenSearch when running it as an external or distributed service.

.. note::

   For HVM deployments and all-in-one installations, OpenSearch is embedded and requires no configuration. This page is only relevant when running OpenSearch externally or in a multi-node embedded cluster.

Settings Reference
^^^^^^^^^^^^^^^^^^

The following settings control OpenSearch behavior. They can be set in ``/etc/morpheus/morpheus.rb`` under the ``opensearch[...]`` namespace (or the legacy ``elasticsearch[...]`` namespace — values are bridged automatically, with ``opensearch[...]`` taking precedence).

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Setting
     - opensearch.yml Mapping
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
     - Username for |morpheus| to authenticate with OpenSearch. Used for external clusters. When nil and ``secure_mode`` is enabled, the auto-created ``morpheus`` internal user is used.
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
^^^^^

Ensure the following ports are open between all OpenSearch cluster nodes:

- **9200** — HTTP (client queries)
- **9300** — Transport (inter-node communication and cluster formation)

Notes
^^^^^

- You can use either ``elasticsearch[...]`` or ``opensearch[...]`` keys in ``morpheus.rb``. The ``elasticsearch`` keys are bridged to ``opensearch`` automatically. If the same key is set under both namespaces, the ``opensearch[...]`` value takes precedence.
- The reconfigure strips ``127.0.0.1`` from ``es_hosts`` when more than one host is present, so you don't need to exclude it.
- In secure mode, ``admin_dn`` and ``nodes_dn`` default to ``O=Morpheus,OU=Ops,CN=<node_name>`` and are set automatically per node. These only need to be overridden when using custom certificates.

Custom Certificates
^^^^^^^^^^^^^^^^^^^

When using your own certificates instead of the auto-generated ones, set ``admin_dn`` and ``nodes_dn`` to match the subject DN of your certificates:

- ``admin_dn`` — Identifies the certificate authorized to run administrative operations (e.g., ``securityadmin.sh``). Only requests signed by a certificate matching this DN can modify the security index.
- ``nodes_dn`` — Identifies certificates trusted for inter-node transport communication. Nodes will reject transport connections from certificates that don't match.

To extract the subject DN from an existing certificate:

.. code-block:: bash

   openssl x509 -in /path/to/cert.pem -noout -subject -nameopt RFC2253

Set the values in ``/etc/morpheus/morpheus.rb`` on each node:

.. code-block:: ruby

   opensearch['admin_dn'] = 'CN=admin,OU=MyTeam,O=MyOrg'
   opensearch['nodes_dn'] = 'CN=node,OU=MyTeam,O=MyOrg'

If the admin and node certificates share the same DN (common when a single wildcard or shared cert is used), both values can be set to the same string.

Setting the Morpheus User Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When ``secure_mode`` is enabled, reconfigure creates an internal OpenSearch user named ``morpheus`` that |morpheus| uses to authenticate. The password is auto-generated and stored in ``/etc/morpheus/morpheus-secrets.json`` under the ``elasticsearch.morpheus_password`` key. No manual configuration is needed in the default case.

To set a custom password, add it to ``/etc/morpheus/morpheus.rb`` on each node:

.. code-block:: ruby

   opensearch['morpheus_password'] = 'my-custom-password'

Encrypting Passwords
^^^^^^^^^^^^^^^^^^^^

Passwords in ``morpheus.rb`` can be stored in encrypted form using the ``ENC{...}`` wrapper. During reconfigure, the recipe detects the ``ENC`` prefix and decrypts the value automatically.

To generate an encrypted string:

.. code-block:: bash

   morpheus-ctl get-crypto-string string 'my-custom-password'

Use the output in ``morpheus.rb``:

.. code-block:: ruby

   opensearch['morpheus_password'] = 'ENC{aBcDeFgHiJkLmNoPqRsTuVwXyZ...}'

The encryption uses the appliance's ``encryption_key_suffix`` (from ``/etc/morpheus/morpheus-secrets.json``), so the encrypted value is specific to that appliance. All nodes in the cluster share the same secrets file contents.

Single Node (Embedded)
^^^^^^^^^^^^^^^^^^^^^^

A single-node setup uses the embedded OpenSearch service with default settings. No ``morpheus.rb`` changes are required unless enabling secure mode.

The embedded OpenSearch service starts automatically after reconfigure. To enable secure mode:

.. code-block:: ruby

   opensearch['secure_mode'] = true

3-Node Embedded Cluster
^^^^^^^^^^^^^^^^^^^^^^^^

Prerequisites
"""""""""""""

**Networking:**

- All 3 nodes must be able to reach each other on ports 9200 (HTTP) and 9300 (Transport)
- Each node needs a stable, routable IP address or resolvable hostname
- Both IP addresses and hostnames are supported in ``es_hosts`` and ``publish_ip``

**Configuration:**

- Each node must have the same ``es_hosts`` hash listing all 3 nodes
- A unique ``node_name`` per node
- A unique ``publish_ip`` matching that node's routable IP
- ``host`` set to ``0.0.0.0`` (default ``127.0.0.1`` only listens locally)
- All nodes must share the same ``cluster`` name (defaults to ``morpheus``)

**Example nodes:**

- Node 1: ``10.0.0.1`` (morpheus-1)
- Node 2: ``10.0.0.2`` (morpheus-2)
- Node 3: ``10.0.0.3`` (morpheus-3)

Without Secure Mode
"""""""""""""""""""

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

Run on all three nodes:

.. code-block:: bash

   morpheus-ctl reconfigure

Nodes can be reconfigured in any order. The cluster will form once all nodes are up and can reach each other.

With Secure Mode
""""""""""""""""

Secure mode enables TLS on both the HTTP and transport layers. Each node generates its own node certificate, but all nodes must share the **same root CA**.

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

- ``/opt/morpheus/embedded/opensearch-*/config/root-ca.pem``
- ``/opt/morpheus/embedded/opensearch-*/config/root-ca-key.pem``

**Step 2 — Copy the root CA to Nodes 2 and 3**

Copy both CA files from Node 1 to the same path on Nodes 2 and 3 **before** running reconfigure on them:

.. code-block:: bash

   # From Node 1:
   scp /opt/morpheus/embedded/opensearch-*/config/root-ca.pem     node2:/opt/morpheus/embedded/opensearch-*/config/
   scp /opt/morpheus/embedded/opensearch-*/config/root-ca-key.pem  node2:/opt/morpheus/embedded/opensearch-*/config/

Set ownership on Nodes 2 and 3:

.. code-block:: bash

   chown morpheus-es:morpheus-es /opt/morpheus/embedded/opensearch-*/config/root-ca*.pem

**Step 3 — Configure and reconfigure Nodes 2 and 3**

Set the same configuration with ``secure_mode = true`` on each node (with the appropriate ``node_name`` and ``publish_ip``), then run ``morpheus-ctl reconfigure``. Each node will skip CA generation (the files already exist) and generate its own node certificate signed by the shared CA.

External Cluster
^^^^^^^^^^^^^^^^

When using an externally managed OpenSearch (or Elasticsearch) cluster, disable the embedded service and point |morpheus| at the external hosts.

Add the following to ``/etc/morpheus/morpheus.rb`` on each |morpheus| appliance node:

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

The embedded OpenSearch service will not be started. |morpheus| connects directly to the external cluster.

**Notes for external clusters:**

- ``auth_user`` and ``auth_password`` are sent to the external cluster for authentication. These must match a user configured on the external cluster.
- ``auth_password`` supports the ``ENC{...}`` encrypted format (see Encrypting Passwords above).
- Do **not** set ``secure_mode`` — that setting controls the embedded service's certificate generation. For external TLS clusters, use ``use_tls`` instead.
- ``replica_count`` can be adjusted to match the external cluster's topology (default ``1``).
- |morpheus| supports both OpenSearch and Elasticsearch as the external cluster — no migration is required on the external side.
