Logging Overview
================

|morpheus| provides a comprehensive logging system that captures, aggregates, and forwards logs from the appliance, managed hosts, and virtual machines.

Log Sources
-----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Source
     - Location
     - Description
   * - Application Logs
     - ``/var/log/morpheus/morpheus-ui/``
     - |morpheus| application server logs (Tomcat/Grails). Includes API requests, provisioning operations, and application errors.
   * - Audit Logs
     - Application database + UI
     - User actions, login events, and configuration changes. Viewable in |AdmAct|.
   * - API Logs
     - ``/var/log/morpheus/morpheus-ui/``
     - REST API request/response logging (when enabled via logback configuration).
   * - Nginx Logs
     - ``/var/log/morpheus/nginx/``
     - Web server access and error logs for the appliance reverse proxy.
   * - MySQL Logs
     - ``/var/log/morpheus/mysql/``
     - Database server logs (embedded MySQL). Not present when using an external database.
   * - RabbitMQ Logs
     - ``/var/log/morpheus/rabbitmq/``
     - Message queue logs. Not present when using an external RabbitMQ cluster.
   * - OpenSearch Logs
     - ``/var/log/morpheus/opensearch/``
     - Search and log indexing engine logs.
   * - Agent Logs
     - Managed hosts: ``/var/log/morpheus/morpheus-node/``
     - |morpheus| Agent logs on managed Linux hosts and HVM hypervisors.
   * - Host/VM Logs
     - Managed hosts: ``/var/log/*.log``
     - Application and system logs collected by the |morpheus| Agent from managed VMs and hosts.

Log Storage
-----------

Logs collected from managed hosts and VMs are stored in **OpenSearch** on the appliance. These logs are searchable and viewable in the following locations:

- **Instance Logs** — Logs tab on an Instance detail page
- **Host Logs** — Logs tab on a Host detail page
- **Global Logs** — |MonLog| for cross-instance log search

Log retention is controlled by the **Availability Time Frame** setting in |AdmSetMon|. Logs older than the configured retention period are automatically purged.

.. NOTE:: Appliance service logs (MySQL, RabbitMQ, OpenSearch, Nginx) are stored on the local filesystem and are not indexed in OpenSearch. Use the appliance log configuration to manage rotation and retention for these logs. See :doc:`appliance_logs` for details.

Disabling Logging
-----------------

Log collection from managed hosts can be disabled globally in |AdmSetMon| using the logging toggle. When disabled:

- The |morpheus| Agent stops forwarding logs from managed hosts
- Existing logs remain searchable until they expire per the retention policy
- Appliance service logs continue to be written to disk regardless of this setting

Distributed Trace IDs
---------------------

|morpheus| includes a **trace ID** in all application log entries to correlate operations that span multiple threads, background jobs, or agent interactions. This is essential for troubleshooting complex operations like provisioning, migration, or failover that involve multiple asynchronous steps.

**How it works:**

- Each incoming request or scheduled job is assigned a unique trace ID (W3C traceparent format)
- The trace ID propagates automatically across thread boundaries, background jobs, parallel tasks, and agent communication
- All log entries produced during the operation include the same trace ID in the log output

**Using trace IDs for troubleshooting:**

To follow a single operation through the logs, search for the trace ID value. For example, a provisioning operation that triggers cloud sync, network configuration, and agent installation will share the same trace ID across all log entries, even if they execute on different threads or at different times.

When configured in the logback pattern (see :doc:`appliance_logs`), the trace ID appears as the ``traceId`` MDC field:

.. code-block:: text

   2026-07-13 10:15:32.001 [traceId=abc123def456] INFO  c.m.provision.KvmProvisionService - Starting VM provisioning
   2026-07-13 10:15:32.150 [traceId=abc123def456] INFO  c.m.network.NetworkService - Configuring network for VM
   2026-07-13 10:15:33.200 [traceId=abc123def456] INFO  c.m.agent.CommandService - Sending agent install command

.. NOTE:: Trace IDs are also passed to the |morpheus| Agent via W3C traceparent headers, allowing end-to-end correlation from the appliance through to host-level operations.
