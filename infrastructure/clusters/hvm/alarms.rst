Cluster Alarms
==============

|morpheus| continuously monitors HVM cluster health and raises alarms when thresholds are exceeded or critical conditions are detected. Alarms appear in the cluster detail page and in the Operations > Health section.

Alarms are evaluated every **5 minutes** during the cluster sync cycle. Threshold-based alarms use a **sustained average** over a configurable time window (default: 15 minutes) to avoid alerting on brief spikes.

Alarm Types
-----------

Host Alarms
^^^^^^^^^^^

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Alarm
     - Severity
     - Description
   * - Host CPU Usage Warning
     - Warning
     - Host CPU usage is averaging above the warning threshold (default: 85%) over the monitoring window
   * - Host CPU Usage Critical
     - Critical
     - Host CPU usage is averaging above the critical threshold (default: 95%) over the monitoring window
   * - Host Memory Usage Warning
     - Warning
     - Host memory usage is averaging above the warning threshold (default: 90%) over the monitoring window
   * - Host Memory Usage Critical
     - Critical
     - Host memory usage is averaging above the critical threshold (default: 95%) over the monitoring window
   * - Host Memory Over-Committed
     - Warning
     - Total allocated VM memory exceeds the host's physical memory capacity (adjusted by overcommit percent). See :doc:`vm_placement` for overcommit configuration.
   * - Host Unreachable
     - Error
     - Host has not reported in over 5 minutes and may be offline or experiencing network issues
   * - Multiple Heartbeat Datastores Detected
     - Warning
     - More than one datastore was configured as a heartbeat datastore. The system has auto-selected one. Review the Datastores tab to verify the selection.

Datastore Alarms
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Alarm
     - Severity
     - Description
   * - Datastore Usage Warning
     - Warning
     - Datastore capacity usage exceeds the warning threshold (default: 80%)
   * - Datastore Usage Critical
     - Critical
     - Datastore capacity usage exceeds the critical threshold (default: 90%)
   * - Datastore Offline
     - Error
     - Datastore is offline and not accessible from any host

VM Alarms
^^^^^^^^^

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Alarm
     - Severity
     - Description
   * - VM CPU Usage Warning
     - Warning
     - VM CPU usage is averaging above the warning threshold (default: 85%) over the monitoring window
   * - VM CPU Usage Critical
     - Critical
     - VM CPU usage is averaging above the critical threshold (default: 95%) over the monitoring window
   * - VM Memory Usage Warning
     - Warning
     - VM memory usage is averaging above the warning threshold (default: 90%) over the monitoring window
   * - VM Memory Usage Critical
     - Critical
     - VM memory usage is averaging above the critical threshold (default: 95%) over the monitoring window

Operational Alarms
^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Alarm
     - Severity
     - Description
   * - Unable to Remove Host
     - Warning
     - A host removal operation could not safely complete. Follow :doc:`managing_hosts`; do not manually edit cluster membership, and contact HPE Support if safe isolation or ring departure cannot be established.

Default Thresholds
------------------

.. list-table::
   :widths: 30 20 20 30
   :header-rows: 1

   * - Metric
     - Warning
     - Critical
     - Notes
   * - Host CPU
     - 85%
     - 95%
     - Sustained average over window
   * - Host Memory
     - 90%
     - 95%
     - Sustained average over window
   * - Host Overcommit
     - 100%
     - —
     - Total allocated vs physical capacity
   * - Datastore Usage
     - 80%
     - 90%
     - Real-time capacity check
   * - VM CPU
     - 85%
     - 95%
     - Sustained average over window
   * - VM Memory
     - 90%
     - 95%
     - Sustained average over window

Alarm Behavior
--------------

Monitoring Window
^^^^^^^^^^^^^^^^^^

Threshold-based alarms (CPU, memory) use a rolling time window (default: **15 minutes**) of averaged metrics from OpenSearch. This prevents short spikes from triggering false alarms.

Clear Margin
^^^^^^^^^^^^^

Alarms automatically clear when the metric drops below the threshold minus a **clear margin** (default: 10 percentage points). For example, a CPU warning alarm triggered at 85% will clear when usage drops below 75%. This hysteresis prevents alarm flapping.

Idempotent Evaluation
^^^^^^^^^^^^^^^^^^^^^^

The alarm system is idempotent — if an alarm is already active, re-evaluating the same condition does not create duplicate alarms. Similarly, clearing an already-cleared alarm is a no-op.

Customizing Thresholds
-----------------------

Alarm thresholds can be overridden at the **cluster level** through the cluster configuration. Custom thresholds are merged with the defaults — you only need to specify the values you want to change.

Datastore-level threshold overrides are also supported, allowing different capacity warning levels for different datastores within the same cluster.

.. NOTE:: Alarms can be disabled entirely for a cluster by setting ``enabled: false`` in the alarm thresholds configuration.

Viewing and Acknowledging Alarms
---------------------------------

Alarms are visible in:

- **Cluster detail page** — Summary panel shows active alarm count and status
- **Operations > Health** — Global view of all active alarms across the appliance

To acknowledge an alarm:

#. Navigate to the alarm in Operations > Health
#. Click the alarm to view details
#. Click :guilabel:`Acknowledge` to mark it as seen

Acknowledged alarms remain visible but no longer contribute to the cluster's overall health status indicator. Alarms automatically clear when the underlying condition resolves.
