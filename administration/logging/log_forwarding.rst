Log Forwarding
==============

|morpheus| supports forwarding logs from managed hosts and VMs to external logging platforms using **Syslog forwarding rules**. This enables integration with centralized logging solutions and SIEM platforms such as Splunk, Datadog, Graylog, or any syslog-compatible receiver.

How Log Forwarding Works
------------------------

The |morpheus| Agent on each managed host watches log files (``/var/log/*.log`` by default, plus any custom log folders configured on Library Node Types). When syslog forwarding rules are configured, the Agent forwards matching log entries directly to the configured syslog destination — logs flow from the managed host to the syslog receiver, not through the |morpheus| appliance.

.. NOTE:: Log forwarding operates independently from log collection. Logs are still collected and stored in OpenSearch on the appliance (unless collection is disabled). Forwarding sends a copy to the external destination.

Configuring Syslog Forwarding Rules
------------------------------------

#. Navigate to |AdmSetLog|
#. Click :guilabel:`+ Add Rule`
#. Configure the forwarding rule:

   .. list-table::
      :widths: 25 75
      :header-rows: 1

      * - Field
        - Description
      * - Name
        - Descriptive name for the rule
      * - Rule
        - The syslog forwarding destination and configuration. Uses standard syslog address format.
      * - Host
        - Hostname or IP address of the syslog receiver
      * - Port
        - Port number on the syslog receiver (common: 514 for UDP, 1514 for TCP, 6514 for TLS)
      * - Protocol
        - Transport protocol: UDP, TCP, or TCP+TLS (secure syslog)

#. Click :guilabel:`Save`

The rule takes effect on the next Agent check-in cycle for all managed hosts.

Supported Transport Protocols
------------------------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Protocol
     - Port (typical)
     - Notes
   * - UDP
     - 514
     - Fastest, no delivery guarantee. Suitable for high-volume, low-criticality logs.
   * - TCP
     - 1514
     - Reliable delivery with connection-oriented transport. Recommended for most deployments.
   * - TCP + TLS
     - 6514
     - Encrypted transport. Required for compliance environments and when log data crosses untrusted networks.

Firewall Requirements
----------------------

For log forwarding to function, the following network paths must be open:

.. list-table::
   :widths: 30 20 20 30
   :header-rows: 1

   * - Source
     - Destination
     - Port
     - Purpose
   * - Managed hosts/VMs
     - Syslog receiver
     - 514/1514/6514
     - Log forwarding (protocol-dependent)
   * - Managed hosts/VMs
     - |morpheus| appliance
     - 443
     - Agent communication (always required)

.. IMPORTANT:: Log forwarding traffic flows directly from managed hosts to the syslog receiver. Ensure all managed hosts have network access to the syslog destination — not just the |morpheus| appliance.

What Gets Forwarded
--------------------

By default, syslog forwarding includes all logs that the |morpheus| Agent collects:

- System logs (``/var/log/syslog``, ``/var/log/messages``)
- Application logs (any ``.log`` file in ``/var/log/``)
- Custom log folders configured on Library Node Types
- HVM hypervisor logs (kernel, libvirt, agent)

Appliance Service Logs
^^^^^^^^^^^^^^^^^^^^^^^

Appliance-level service logs (MySQL, RabbitMQ, OpenSearch, Nginx, application logs) are **not** forwarded by the Agent-based syslog rules. To forward appliance logs, configure syslog forwarding at the OS level using ``rsyslog`` or ``syslog-ng`` on the appliance host, or use the logback SIEM appender configuration. See :doc:`appliance_logs` for details.

Integration with SIEM Platforms
--------------------------------

For SIEM integration (CEF/LEEF format, structured audit events), |morpheus| supports a logback-based audit appender that can write directly to SIEM databases or syslog endpoints in Common Event Format. This is configured at the appliance level rather than through the UI forwarding rules. See the CEF/SIEM Auditing section in :doc:`appliance_logs`.

Troubleshooting Log Forwarding
-------------------------------

**Logs not appearing at the destination:**

- Verify network connectivity from a managed host to the syslog receiver on the configured port
- Confirm the |morpheus| Agent is running on the host (``systemctl status morpheus-node-agent``)
- Check that the forwarding rule protocol matches what the receiver expects (UDP vs TCP vs TLS)
- Verify no firewall is blocking the syslog port between managed hosts and the receiver

**Partial logs forwarded:**

- Only files matching ``.log`` extension in watched directories are forwarded
- Custom application logs require the LOG FOLDER to be configured on the Library Node Type
- Binary log files or files with non-standard extensions are not forwarded
