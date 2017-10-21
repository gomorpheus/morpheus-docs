Logging Settings
================

Overview
^^^^^^^^

|morpheus| contains a built-in logging solution that aggregates logs from hosts and services. Logs are displayed, searchable, and filterable in the Instance, App, Host and overall Logs sections. Logs can also be forwarded using Syslog Forward rules to any external solution that supports syslogs.

|morpheus| also has built in Integrations with 3rd Party solutions. When configured, the |morpheus| agent will forward logs to the integrated platforms automatically.

Logging Settings for the build-in Logging, Syslog forwards, and 3rd Party Integrations are configurable in the `Administration -> Logs` section.

|morpheus| Logging
^^^^^^^^^^^^^^^^^^

|morpheus| contains a built-in logging solution that aggregates logs from hosts and services. Logs are displayed, searchable, and filterable in the Instance, App, Host and overall Logs sections. Logs can also be forwarded using Syslog Forward rules to any external solution that supports syslogs.

Splunk
^^^^^^

To configure Splunk simply create a syslog listener configuration in Splunk. Then it is simply a matter of expanding the section in Logging settings pertaining to Splunk and filling out the host and port of the appender. Once saved, all hosts managed by |morpheus| will be configured to forward logs to the target Splunk listener.

LogRhythm
^^^^^^^^^

Configuring LogRhythm is much like configuring Splunk. Simply toggle the enabled flag in the LogRhythm section to enabled and fill in the Host, and Port information for the LogRhythm listener.


.. include::splunk.rst
.. include::logrhythm.rst
