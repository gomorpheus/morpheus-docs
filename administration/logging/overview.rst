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
