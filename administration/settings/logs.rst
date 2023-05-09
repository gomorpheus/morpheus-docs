Logging Settings
^^^^^^^^^^^^^^^^

Overview
````````

|morpheus| contains a built-in logging solution that aggregates logs from hosts and services. Logs are displayed, searchable, and filterable in the Instance, App, Host and overall Logs sections. Logs can also be forwarded using Syslog Forward rules to any external solution that supports syslogs.

The logs displayed in the Instance, App, Host and overall Logs sections are only from Managed VMs and Hosts that have the |morpheus| Agent installed. Instances can be configured to show additional logs by configuring the LOG FOLDER in the Library NODE TYPE. Logs from any .log file in the specified folder will be forwarded by the |morpheus| agent to the |morpheus| appliance or forwarded with Syslog Forward rules.

Logging from managed workloads with the |morpheus| Agent installed can be globally enabled or disabled here. Logging can be disabled on a per-server basis from the server detail pages at |InfCom|. If logging is globally disabled, it will be disabled for all servers regardless of the per-server settings.

.. NOTE:: The `Logs` section does not contain |morpheus| appliance logs, which can be found in `/var/log/morpheus/` and in `Administration - Health`.

Logs are stored in ElasticSearch and retention can be set by adjusting the Availability Time Frame in the |AdmSetLog| section.

Logging Settings for the built-in logging and syslog forwards are also configurable in the |AdmSetLog| section.

.. image:: /images/administration/settings/logs.png
