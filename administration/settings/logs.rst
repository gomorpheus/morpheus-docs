Logging Settings
^^^^^^^^^^^^^^^^

Overview
````````

|morpheus| contains a built-in logging solution that aggregates logs from hosts and services. Logs are displayed, searchable, and filterable in the Instance, App, Host and global Logs (|MonLog|) sections. Logs can also be forwarded using Syslog forward rules to any external solution that supports Syslogs.

The logs displayed in the Instance, App, Host and overall Logs (|MonLog|) sections are only from managed VMs and Hosts that have the |morpheus| Agent installed. |morpheus| Agent will watch ``/var/logs`` for any .log file and report them back accordingly. Containerized Instances can be configured to show additional logs by configuring the LOG FOLDER in the Library NODE TYPE. Logs from any .log file in the specified folder will be forwarded by the |morpheus| Agent to the |morpheus| appliance or forwarded with Syslog forward rules.

.. NOTE:: The `Logs` section does not contain |morpheus| appliance logs, which can be found in `/var/log/morpheus/` and in |AdmHea|.

Logs are stored in ElasticSearch and retention can be set by adjusting the Availability Time Frame in the |AdmSetMon| section. Logging can also be disabled with a simple toggle switch just above the Availability Time Frame configuration.

.. image:: /images/administration/settings/logSettings.png
