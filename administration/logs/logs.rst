Logging Settings
================

Overview
^^^^^^^^

|morpheus| contains a built-in logging solution that aggregates logs from hosts and services. Logs are displayed, searchable, and filterable in the Instance, App, Host and overall Logs sections. Logs can also be forwarded using Syslog Forward rules to any external solution that supports syslogs.

The logs displayed in the Instance, App, Host and overall Logs sections are only from Managed VM's and Hosts that have the |morpheus| agent installed. Instances can be configured to show additional logs by configuring the LOG FOLDER in the Library NODE TYPE. Logs from any .log file in the specified folder will be forwarded by the |morpheus| agent to the |morpheus| appliance or forwarded with Syslog Forward rules.

.. NOTE:: The `Logs` section does not contain |morpheus| appliance logs, which can be found in `/var/log/morpheus/` and in 3.5.2+ in `Operations - Health`.

Logs are stored in ElasticSearch and retention can be set by adjusting the Availability Time Frame in the `Administration -> Logs` section.

|morpheus| also has built in Integrations with 3rd Party solutions. When configured, the |morpheus| agent will forward logs to the integrated platforms automatically.

Logging Settings for the build-in Logging, Syslog forwards, and 3rd Party Integrations are configurable in the `Administration -> Logs` section.

|morpheus| Logging
^^^^^^^^^^^^^^^^^^

|morpheus| contains a built-in logging solution that aggregates logs from hosts and services. Logs are displayed, searchable, and filterable in the Instance, App, Host and overall Logs sections. Logs can also be forwarded using Syslog Forward rules to any external solution that supports syslogs.

Splunk
^^^^^^

To configure Splunk create a syslog listener configuration in Splunk. Then it is simply a matter of expanding the section in Logging settings pertaining to Splunk and filling out the host and port of the appender. Once saved, all hosts managed by |morpheus| will be configured to forward logs to the target Splunk listener.

LogRhythm
^^^^^^^^^

Configuring LogRhythm is much like configuring Splunk. Simply toggle the enabled flag in the LogRhythm section to enabled and fill in the Host, and Port information for the LogRhythm listener.
