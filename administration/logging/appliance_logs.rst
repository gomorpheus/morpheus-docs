Appliance Log Configuration
============================

This section covers configuration of |morpheus| appliance-level logs — the application server, services, and internal components. These logs are distinct from the host/VM logs collected by the |morpheus| Agent (see :doc:`log_forwarding`).

Log File Locations
------------------

All appliance logs are located under ``/var/log/morpheus/``:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Path
     - Contents
   * - ``/var/log/morpheus/morpheus-ui/current``
     - Main application log (current)
   * - ``/var/log/morpheus/morpheus-ui/``
     - Rotated application logs
   * - ``/var/log/morpheus/nginx/``
     - Reverse proxy access and error logs
   * - ``/var/log/morpheus/mysql/``
     - Embedded MySQL logs (if using embedded DB)
   * - ``/var/log/morpheus/rabbitmq/``
     - Embedded RabbitMQ logs (if using embedded messaging)
   * - ``/var/log/morpheus/opensearch/``
     - OpenSearch indexing engine logs
   * - ``/var/log/morpheus/check-server/``
     - Health check service logs

Viewing Appliance Logs
-----------------------

**From the CLI:**

.. code-block:: bash

   sudo morpheus-ctl tail morpheus-ui

This tails the live application log. Replace ``morpheus-ui`` with any other service name (``nginx``, ``rabbitmq``, ``opensearch``, ``mysql``) to tail that service's logs.

**From the UI:**

Navigate to |AdmHea| to view appliance health and recent log entries.

Logback Configuration
----------------------

The |morpheus| application uses **Logback** for log management. The configuration file is located at:

``/opt/morpheus/embedded/morpheus-ui/conf/logback.xml``

.. WARNING:: Modifications to logback.xml will be overwritten during appliance upgrades. Back up your custom configuration before upgrading.

For detailed logback configuration options including log levels, appenders, rotation settings, and CEF/SIEM audit export, see the :doc:`/getting_started/additional/logback` reference.

Common Configuration Tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Changing log levels:**

Edit ``logback.xml`` and adjust the ``level`` attribute on the appropriate logger. For example, to enable debug logging for provisioning:

.. code-block:: xml

   <logger name="com.morpheus.provision" level="DEBUG"/>

Changes take effect within 60 seconds (Logback scans for configuration changes automatically).

**CEF/SIEM Audit Export:**

|morpheus| supports exporting audit events in Common Event Format (CEF) for SIEM integration. This is configured by adding a CEF appender to logback.xml. See the :doc:`/getting_started/additional/logback` reference for the full appender configuration.

**Log Rotation:**

Appliance logs are rotated by the ``svlogd`` service (part of the |morpheus| packaging). Default rotation settings keep up to 30 log files of 200MB each per service. These defaults can be adjusted in ``/etc/morpheus/morpheus.rb``:

.. code-block:: ruby

   morpheus_ui['svlogd_size'] = 209715200   # 200MB per file
   morpheus_ui['svlogd_num'] = 30           # 30 rotated files

Run ``sudo morpheus-ctl reconfigure`` after changes.

Forwarding Appliance Logs Externally
--------------------------------------

To forward appliance-level logs (not host/VM logs) to an external syslog or SIEM:

**Option 1: OS-level syslog (rsyslog/syslog-ng)**

Configure the appliance host's system syslog daemon to forward ``/var/log/morpheus/`` entries to your centralized logging platform. This is the simplest approach and works with any syslog receiver.

**Option 2: Logback syslog appender**

Add a syslog appender directly in ``logback.xml`` for application-level log forwarding:

.. code-block:: xml

   <appender name="SYSLOG" class="ch.qos.logback.classic.net.SyslogAppender">
       <syslogHost>your-syslog-host</syslogHost>
       <port>514</port>
       <facility>LOCAL0</facility>
       <suffixPattern>[%thread] %logger %msg</suffixPattern>
   </appender>

**Option 3: CEF appender for SIEM**

For structured audit events in CEF format, see the SIEM auditing section in the :doc:`/getting_started/additional/logback` reference.
