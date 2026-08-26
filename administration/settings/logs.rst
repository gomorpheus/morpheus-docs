Logging Settings
^^^^^^^^^^^^^^^^

Overview
````````

Open these settings at :menuselection:`Administration --> Settings --> Monitoring --> Logging Settings`.

|morpheus| contains a built-in logging solution that aggregates logs from hosts and services. Logs are displayed, searchable, and filterable in the Instance, App, Host and global Logs (|MonLog|) sections. Logs can also be forwarded using Syslog forward rules to any external solution that supports Syslogs.

The logs displayed in the Instance, App, Host and overall Logs (|MonLog|) sections are only from managed VMs and Hosts that have the |morpheus| Agent installed. |morpheus| Agent will watch ``/var/logs`` for any .log file and report them back accordingly. Containerized Instances can be configured to show additional logs by configuring the LOG FOLDER in the Library NODE TYPE. Logs from any .log file in the specified folder will be forwarded by the |morpheus| Agent to the |morpheus| appliance or forwarded with Syslog forward rules.

.. NOTE:: The `Logs` section does not contain |morpheus| appliance logs, which can be found in `/var/log/morpheus/` and in |AdmHea|.

Logs are stored in ElasticSearch and retention can be set by adjusting the Availability Time Frame in the |AdmSetMon| section. Logging can also be disabled with a simple toggle switch just above the Availability Time Frame configuration.

.. image:: /images/administration/settings/logSettings.png

Advanced Options
````````````````

Expand :guilabel:`Advanced Options` beneath the standard logging settings to access Agent Log Throttle and Agent Log Deduplication controls.

Agent Log Throttle Policy
'''''''''''''''''''''''''

The Agent Log Throttle Policy protects the |morpheus| appliance from being overwhelmed when a single server agent sends logs at an excessive rate. When a server's cumulative log volume exceeds a configurable ceiling, |morpheus| can raise an alarm, actively disable logging on the offending server, or both. All settings default to **Off** on new installations.

.. list-table::
   :widths: 22 50 14 14
   :header-rows: 1

   * - Setting
     - Description
     - Default
     - Constraints
   * - Policy
     - Controls the throttle response. **Off** performs no throttling. **Monitor** raises an alarm but continues storing logs. **Enforce** disables logging on the server and drops subsequent log batches.
     - Off
     -
   * - Threshold
     - Maximum log volume allowed per minute before a breach is triggered (KB/min).
     - 2048
     - Minimum 100
   * - Window
     - Rolling time window used to measure cumulative log volume. The effective ceiling is ``threshold × window``.
     - 30 minutes
     - 5–60 minutes
   * - Auto Re-enable
     - When enabled, automatically re-enables logging on enforced servers and clears alarms after the cooldown period. When disabled, manual re-enablement is required.
     - On
     -
   * - Cooldown
     - Time to wait after a breach before re-enabling logging or clearing alarms. Resets if the server re-breaches.
     - 60 minutes
     - Must be ≥ Window

**How the ceiling is calculated:** The effective byte ceiling for a window is ``threshold (KB/min) × window (minutes) × 1024``. With defaults (2048 KB/min, 30-minute window), the ceiling is approximately 60 MB per 30-minute window.

**Monitor mode:** Log volume is tracked per server in a rolling window. When a server exceeds the ceiling, an alarm is raised on :menuselection:`Operations --> Alarms` with category ``log.throttle.monitor``. Logs continue to be stored. If auto re-enable is on, the alarm is cleared after the cooldown period elapses without a new breach.

**Enforce mode:** Same volume tracking as Monitor. When breached, logging is disabled on the server (``enable_logs = false``), subsequent log batches are dropped at the WebSocket layer, and the agent is commanded to stop transmitting. An alarm with category ``log.throttle.enforce`` is raised. If auto re-enable is on, a background job re-enables logging after the cooldown period. If auto re-enable is off, an administrator must manually re-enable logging on the server.

**Per-server override:** Individual servers can override the global policy via :menuselection:`Infrastructure --> Compute --> [Server] --> Edit --> Log Throttle Policy`. The per-server policy takes precedence over the global setting. Threshold, window, and cooldown values always use the global configuration.

**Alarms:** Log throttle alarms appear on :menuselection:`Operations --> Alarms` and can be acknowledged from that page or from the server detail page. Alarms include the server name, cloud, and breach details.

Agent Log Deduplication
'''''''''''''''''''''''

When enabled, |morpheus| suppresses duplicate agent log messages per server within a rolling 30-second window. Only the first occurrence of each unique message is stored; repeats are discarded until the window resets. When the window resets, a summary entry records how many duplicates were suppressed.

This setting addresses scenarios where a single server floods identical syslog messages (for example, a repeated error condition) that can contribute to Elasticsearch pressure and queue exhaustion.

A per-server signature cap of 100 unique messages bounds memory usage during the deduplication window.

API
'''

Log throttle and deduplication settings are available via the log settings API:

- ``GET /api/log-settings`` — Returns current throttle and deduplication settings.
- ``PUT /api/log-settings`` — Update settings.

Fields: ``logThrottlePolicy``, ``logThrottleThreshold``, ``logThrottleWindow``, ``logThrottleAutoReEnable``, ``logThrottleCooldown``, ``logDeduplication``.

To query log throttle alarms across all tenants (master tenant only):

.. code-block:: bash

   morpheus health alarms --query category="log.throttle" --query global=true
