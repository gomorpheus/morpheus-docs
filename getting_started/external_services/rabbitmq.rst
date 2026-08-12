.. _external-rabbitmq:

RabbitMQ
--------

RabbitMQ is the message broker for |morpheus|, handling agent communication (STOMP protocol), task orchestration, event processing, and inter-service communication (AMQP protocol). This page covers preparing an external RabbitMQ service for use with |morpheus|.

.. note::

   For HVM deployments and all-in-one installations, RabbitMQ is embedded and requires no configuration. This page is only relevant when running RabbitMQ externally for HA or organizational requirements.

Supported Versions
^^^^^^^^^^^^^^^^^^

- **RabbitMQ |rmqbranch|** (embedded default: |rmqver|)
- **Erlang |erlang|** (must be compatible with your RabbitMQ version)

Password changes for appliance-managed RabbitMQ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changing ``rabbitmq['queue_user_password']`` or the corresponding value in ``morpheus-secrets.json`` and running ``morpheus-ctl reconfigure`` does **not** rotate the password of an existing RabbitMQ user. The appliance recipe creates a missing user, but it does not change the password when that user already exists. Updating only the broker or only the application configuration creates a credential mismatch and can interrupt application and agent messaging.

There is currently no supported self-service password-rotation procedure for the appliance-managed RabbitMQ ``queue_user``. Do not use a sequence that combines ``rabbitmqctl change_password``, direct edits to ``morpheus-secrets.json``, and reconfigure unless HPE Support supplies a procedure for the exact topology and release. Contact HPE Support to coordinate the broker and application credential change, validation, recovery plan, and the ordering of every application node.

For external RabbitMQ, rotate credentials using the external service owner's process and coordinate the matching |morpheus| connection change with HPE Support. Never place a real password in documentation, command transcripts, or support artifacts.

When to Externalize
^^^^^^^^^^^^^^^^^^^

Consider running RabbitMQ externally when:

- You need **high availability** with clustered queues and automatic failover
- Your organization requires messaging infrastructure to be **managed by a dedicated team**
- You are running a **multi-node |morpheus| application tier** (Full HA) and need a shared message bus
- You need to **scale messaging independently** from the application tier

Cluster Architecture
^^^^^^^^^^^^^^^^^^^^

RabbitMQ uses a quorum-based election system for failover, which requires an **odd number of nodes** (minimum 3) for HA configurations.

**Recommended topology:**

- **3 nodes minimum** per region for HA
- All nodes are peers (no designated master)
- Place a **load balancer** between the |morpheus| application nodes and the RabbitMQ cluster to handle connection routing and failover
- Forward both AMQP (5672) and STOMP (61613) ports through the load balancer

**Cross-region considerations:**

- For multi-region HA, deploy at least 3 RabbitMQ nodes per region
- Cross-region clustering is possible but adds latency — evaluate whether federation or shovel plugins are more appropriate for your use case
- Agent STOMP connections are persistent; ensure connection timeouts and keepalives are configured appropriately for cross-region links

Preparing the External RabbitMQ Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1 — Install RabbitMQ**

Install RabbitMQ on each cluster node following the `official RabbitMQ installation guide <https://www.rabbitmq.com/install-debian.html>`_. Ensure all nodes run the same RabbitMQ and Erlang versions.

**Step 2 — Form the cluster**

On nodes 2 and 3, join them to node 1:

.. code-block:: bash

   rabbitmqctl stop_app
   rabbitmqctl join_cluster rabbit@node1
   rabbitmqctl start_app

Verify cluster status:

.. code-block:: bash

   rabbitmqctl cluster_status

**Step 3 — Enable required plugins**

|morpheus| requires the STOMP plugin for agent communication:

.. code-block:: bash

   rabbitmq-plugins enable rabbitmq_stomp

Enable on all cluster nodes.

**Step 4 — Create the Morpheus vhost and user**

.. code-block:: bash

   rabbitmqctl add_vhost morpheus
   rabbitmqctl add_user morpheus '<secure-password>'
   rabbitmqctl set_permissions -p morpheus morpheus ".*" ".*" ".*"
   rabbitmqctl set_user_tags morpheus administrator

**Step 5 — Configure HA policy**

For queue mirroring across cluster nodes:

.. code-block:: bash

   rabbitmqctl set_policy ha-all ".*" '{"ha-mode":"all","ha-sync-mode":"automatic"}' -p morpheus --apply-to queues

This ensures all queues are mirrored across all nodes for failover.

Network Requirements
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 35 20 20 10 15

   * - Description
     - Source
     - Destination
     - Port
     - Protocol
   * - AMQP (application messaging)
     - |morpheus| appliance
     - RabbitMQ node(s)
     - 5672
     - TCP
   * - STOMP (agent communication)
     - |morpheus| appliance / Agents
     - RabbitMQ node(s)
     - 61613
     - TCP
   * - Erlang distribution (inter-node)
     - RabbitMQ node
     - RabbitMQ node
     - 25672
     - TCP
   * - Erlang Port Mapper (epmd)
     - RabbitMQ node
     - RabbitMQ node
     - 4369
     - TCP
   * - Management UI (optional)
     - Admin workstation
     - RabbitMQ node
     - 15672
     - TCP

Load Balancer Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When placing a load balancer in front of the RabbitMQ cluster:

- Forward **port 5672** (AMQP) with TCP mode (not HTTP)
- Forward **port 61613** (STOMP) with TCP mode
- Use **round-robin** or **least-connections** balancing
- Configure health checks against the RabbitMQ management API (port 15672, path ``/api/health/checks/alarms``) or a simple TCP check on port 5672
- Ensure the load balancer supports **long-lived connections** — STOMP agent connections are persistent

TLS Configuration
^^^^^^^^^^^^^^^^^

To secure RabbitMQ communications with TLS:

1. Configure RabbitMQ with TLS certificates (see `RabbitMQ TLS documentation <https://www.rabbitmq.com/ssl.html>`_)
2. Use TLS-enabled ports (typically 5671 for AMQPS, 61614 for STOMP over TLS)
3. Update the |morpheus| ``morpheus.rb`` configuration to point at the TLS ports and enable SSL for the connection

Memory and Resource Sizing
^^^^^^^^^^^^^^^^^^^^^^^^^^

RabbitMQ resource requirements depend on message throughput:

- **Small environments** (< 100 agents): 2 GB RAM per node
- **Medium environments** (100–1000 agents): 4 GB RAM per node
- **Large environments** (1000+ agents): 8 GB RAM per node, consider dedicated I/O-optimized storage for message persistence

Monitor queue depths and memory usage via the RabbitMQ Management UI (port 15672, enable with ``rabbitmq-plugins enable rabbitmq_management``).

Troubleshooting
^^^^^^^^^^^^^^^

**Cluster partition (split-brain)**

If network issues cause a cluster partition, RabbitMQ nodes may disagree on cluster state. Resolution:

.. code-block:: bash

   # On the minority-side node(s):
   rabbitmqctl stop_app
   rabbitmqctl reset
   rabbitmqctl join_cluster rabbit@<majority-node>
   rabbitmqctl start_app

**Agent connection failures**

If agents cannot connect to |morpheus| after externalizing RabbitMQ:

- Verify port 61613 (STOMP) is open from agent hosts to the RabbitMQ cluster/load balancer
- Check the appliance URL is correctly configured in |AdmSet| — agents use this to determine the STOMP connection endpoint
- Verify the ``morpheus`` user has permissions on the ``morpheus`` vhost

**High memory watermark**

If RabbitMQ triggers its high memory watermark and blocks publishers:

- Increase the memory limit: ``rabbitmqctl set_vm_memory_high_watermark 0.6``
- Add more RAM to the nodes
- Investigate consumers that may be offline or slow (check queue depths in the Management UI)
