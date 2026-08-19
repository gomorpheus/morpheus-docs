Audit Logging
=============

|morpheus| maintains a comprehensive audit trail of all administrative and operational actions performed through the UI and API. Audit logs use the industry-standard **Common Event Format (CEF)** and support export to SIEM platforms for compliance and security monitoring.

The audit system satisfies requirements for security frameworks including NIST 800-53 AU (Audit and Accountability) controls, SOC 2 CC7 (System Operations), and PCI-DSS Requirement 10 (Track and Monitor Access).

What Gets Audited
-----------------

The audit system automatically captures:

- **All create operations** (HTTP POST) — resource creation, provisioning, user creation, etc.
- **All update operations** (HTTP PUT) — configuration changes, edits, permission updates
- **All delete operations** (HTTP DELETE) — resource removal, decommissioning
- **Explicit view events** — console access, Cypher decryption, and other sensitive read operations

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Event Category
     - Examples
   * - Authentication
     - User login, logout, failed authentication, impersonation
   * - Resource Management
     - Instance/VM create, update, delete; host add/remove; cluster operations
   * - Configuration Changes
     - Role permission updates, policy changes, integration configuration
   * - Security Events
     - Cypher secret decryption, API token creation, credential access
   * - Console Access
     - Instance console opened, VDI session started
   * - Infrastructure
     - Cloud sync operations, resource pool changes, network modifications
   * - Automation
     - Manual task/workflow execution, Ansible playbook runs

Audit Event Format (CEF)
--------------------------

Every audit event is formatted using the **Common Event Format (CEF)** standard:

.. code-block:: text

   CEF:0|MorpheusData|Morpheus|<version>|<signatureId>|<eventName>|<severity>|<extensions>

**CEF Extension Fields:**

.. list-table::
   :widths: 15 20 65
   :header-rows: 1

   * - Field
     - CEF Key
     - Description
   * - Source IP
     - ``src``
     - Client IP address (respects X-Forwarded-For for proxied requests)
   * - User ID
     - ``suid``
     - Numeric user ID of the actor
   * - Username
     - ``suser``
     - Username of the actor
   * - Request URL
     - ``request``
     - Full URL of the request
   * - HTTP Method
     - ``requestMethod``
     - POST, PUT, DELETE, or GET
   * - Object Type
     - ``cs1``
     - Type of resource affected (e.g., Instance, ComputeServer, Role)
   * - Object ID
     - ``cn1``
     - ID of the affected resource
   * - Object Name
     - ``cs2``
     - Display name of the affected resource
   * - Account ID
     - ``cn2``
     - Tenant/account ID
   * - Original User
     - ``cs4``
     - Real username when action performed via impersonation
   * - Target User
     - ``duser``
     - User being impersonated (impersonation events only)

Where Audit Data Is Stored
---------------------------

Audit data is written to **three locations** simultaneously:

Database (``audit_log`` table)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The primary audit store. All events are persisted to the ``audit_log`` table in the application database with the following retention:

- **Automatic purge after 90 days** — a background job removes entries older than 90 days
- Includes a ``logSignature`` field containing a SHA-256 hash of the audit entry for **tamper detection**

The database audit log is viewable in the |morpheus| UI at |AdmAct|.

Logback (File-based)
^^^^^^^^^^^^^^^^^^^^^

Audit events are logged through the standard Logback framework under the ``com.morpheus.AuditLogService`` logger. By default, these go to the main application log. For a dedicated audit log file, add a rolling file appender to ``logback.xml``:

.. code-block:: xml

   <appender name="AUDIT_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
       <file>/var/log/morpheus/morpheus-ui/audit.log</file>
       <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
           <fileNamePattern>/var/log/morpheus/morpheus-ui/audit.%d{yyyy-MM-dd}.log</fileNamePattern>
           <maxHistory>365</maxHistory>
       </rollingPolicy>
       <encoder>
           <pattern>%date %msg%n</pattern>
       </encoder>
   </appender>

   <logger name="com.morpheus.AuditLogService" level="INFO" additivity="false">
       <appender-ref ref="AUDIT_FILE" />
   </logger>

This provides a file-based audit trail that can be retained longer than the 90-day database purge and forwarded via OS-level syslog.

SIEM / External Forwarding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because audit events use CEF format natively, they can be forwarded directly to SIEM platforms:

- **ArcSight** — CEF is the native format
- **Splunk** — Use the Splunk CEF Add-on for parsing
- **IBM QRadar** — Supports CEF log source type
- **Any syslog-compatible SIEM** — Forward the audit log file via rsyslog/syslog-ng

To forward audit events to a SIEM via syslog, configure a syslog appender in ``logback.xml``:

.. code-block:: xml

   <appender name="SIEM_SYSLOG" class="ch.qos.logback.classic.net.SyslogAppender">
       <syslogHost>your-siem-host</syslogHost>
       <port>6514</port>
       <facility>AUTH</facility>
       <suffixPattern>%msg</suffixPattern>
   </appender>

   <logger name="com.morpheus.AuditLogService" level="INFO" additivity="true">
       <appender-ref ref="SIEM_SYSLOG" />
   </logger>

Tamper Detection
-----------------

Each audit log entry includes a ``logSignature`` field — a **SHA-256 hash** of the full CEF description. This allows security teams to verify that audit records have not been modified after creation:

- Compare the stored hash against a recalculated hash of the description field
- Any discrepancy indicates the record has been tampered with
- This satisfies NIST 800-53 AU-9 (Protection of Audit Information) and AU-10 (Non-repudiation)

Impersonation Tracking
-----------------------

When an administrator impersonates another user, the audit system records **both identities**:

- ``suser`` / ``cs4`` — The original administrator username
- ``duser`` — The impersonated user

This ensures accountability is maintained even during impersonation sessions and provides a clear chain of responsibility.

Compliance Framework Alignment
-------------------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Framework
     - Controls
     - How |morpheus| Satisfies
   * - NIST 800-53
     - AU-2, AU-3, AU-6, AU-9, AU-10, AU-12
     - Automatic event capture, CEF format with required fields, tamper-evident hashing, configurable retention and export
   * - SOC 2
     - CC7.2, CC7.3
     - System activity monitoring, anomaly detection support via SIEM export
   * - PCI-DSS
     - Req 10.1–10.7
     - All access tracked, user identification, timestamping, integrity protection, 90-day online retention
   * - HIPAA
     - §164.312(b)
     - Audit controls for information system activity recording

Viewing Audit Logs
-------------------

**From the UI:**

Navigate to :menuselection:`Operations --> Activity` to view and filter recent product activity. See :doc:`/operations/activity` for the current filters, permission requirements, and the distinction between Activity, Alarms, and process History.

- Timestamp
- User
- Event description
- Object type and ID
- Source IP

**From the API:**

Audit logs are accessible via the |morpheus| API for programmatic access and integration with external reporting tools.

Retention and Archival
-----------------------

- **Database retention:** 90 days (automatic purge)
- **File-based retention:** Configurable via logback rolling policy (recommended: 365 days for compliance)
- **SIEM retention:** Determined by your SIEM platform's retention policy

For compliance requirements that mandate longer retention, configure the file-based audit log with an extended ``maxHistory`` and archive to immutable storage.
