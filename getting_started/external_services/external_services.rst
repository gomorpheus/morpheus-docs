.. _external-services:

External Services
=================

By default, |morpheus| embeds all required backend services (OpenSearch, MySQL, RabbitMQ) within the appliance. For all-in-one installations and HVM deployments using the HPE Installer, these services start automatically and require no additional configuration.

These pages are relevant when you choose to run one or more backend services **externally** — on dedicated infrastructure separate from the |morpheus| appliance. Common reasons to externalize services include:

- **High Availability** — Running services in a clustered configuration for failover and redundancy
- **Managed Services** — Using cloud-managed offerings (e.g., Amazon RDS, Azure Database for MySQL)
- **Organizational Requirements** — Policies requiring database or messaging infrastructure to be managed by a dedicated team
- **Scaling** — Separating resource-intensive services (search, messaging) from the application tier

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Service
     - Role in |morpheus|
   * - **OpenSearch**
     - Log aggregation, metrics, stats, and full-text search indexing. Stores Instance, container, host, and appliance logs as well as temporal usage/costing data. High write throughput at scale.
   * - **MySQL**
     - Transactional application database. Stores all operational data including Instances, users, tenants, policies, automation configurations, billing records, and integration metadata.
   * - **RabbitMQ**
     - Message queuing for agent communication (STOMP protocol), task orchestration, event processing, and inter-service communication (AMQP protocol).

.. note::

   For guidance on configuring the |morpheus| appliance to *point at* external services (the ``morpheus.rb`` settings), see :ref:`Advanced morpheus.rb Settings <morpheus.rb>`. The pages in this section focus on preparing and managing the external services themselves.

.. toctree::
   :maxdepth: 2

   opensearch
   mysql
   rabbitmq
