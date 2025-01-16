|morpheus| Agent Key Features
-----------------------------

While optional, |morpheus| Agent provides many benefits and features in areas of log aggregation, security, automation, monitoring, and more. This page contains the complete summary of its key features and benefits.

**Logging**

The installed |morpheus| Agent captures application logs and sends them back to the |morpheus| appliance. The Agent buffers and compresses logs, sending them in chunks to minimize packet transfers. If desired, users may set up forwarding to an external syslog platform though for most users |morpheus| internal logging functionality is sufficient. Agent logs can be viewed in the UI at |MonLog|. Filtering and search tools are available, even supporting `Lucene search query syntax <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. Logs may also be exported.

**Monitoring and Guidance**

|morpheus| provides robust monitoring into the workloads it manages. For example, from Instance detail pages, usage metrics are tracked on the Summary and Monitoring tabs. The available metrics are significantly improved when |morpheus| Agent is installed on the workload. |morpheus| will make a best effort to gather this information in the absence of an installed Agent but for some Cloud types this is not possible. The table below shows the usage metrics |morpheus| can gather with and without the Agent (though the exact metric available without the Agent will vary by Cloud).

+---------------------------+-------------------------+----------------+-------------------+
| **Category**              | **Statistic**           | **With Agent** | **Without Agent** |
+---------------------------+-------------------------+----------------+-------------------+
| Memory                    | Max Memory              | Yes            | Yes               |
+---------------------------+-------------------------+----------------+-------------------+
| Memory                    | Used Memory             | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| Memory                    | Cache Memory            | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| Storage                   | Max Storage             | Yes            | Yes               |
+---------------------------+-------------------------+----------------+-------------------+
| Storage                   | Used Memory             | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| Processing                | System CPU %            | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| Processing                | User CPU %              | Yes            | Yes               |
+---------------------------+-------------------------+----------------+-------------------+
| IOPS                      | Total IOPS              | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| IOPS                      | IOPS Read               | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| IOPS                      | IOPS Write              | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| Networking                | Net TX Rate             | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| Networking                | Net RX Rate             | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| Other                     | Agent Command Bus       | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| Other                     | Log Aggregation         | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+
| Other                     | Health & Monitoring     | Yes            | No                |
+---------------------------+-------------------------+----------------+-------------------+

In addition to usage and monitoring, |morpheus| also provides a useful guidance feature (|OpeGui|). Guidance analyzes your managed workloads and makes cost-saving or performance recommendations. The effectiveness of this feature is greatly enhanced when |morpheus| Agent is installed on your workloads.

**Script Execution**

The |morpheus| Agent initiates an outbound connection from the managed workload to the appliance over TCP port 443. This establishes a bidirectional command bus which allows |morpheus| to orchestrate automation on managed machines without stored credentials. Many different `Task types <https://docs.morpheusdata.com/en/latest/library/automation/automation.html#tasks>`_ are supported and Tasks can be stacked into Operational or Provisioning Workflows to create logical automation routines. SSH or WinRM connectivity, as well as credentials, are required for Task execution when |morpheus| Agent is not installed.

**Setting File Templates**

File Templates are stored templated text files, primarily config files (for example, ``my.cnf`` or ``morpheus.rb``). Users have access to the full map of |morpheus| variables for injecting values custom to the specific workload at provision time. |morpheus| Agent can transfer files generated from templates to managed nodes.

**Firewall Management**

When "Local Firewall" is enabled for a Cloud (see the Advanced Options section on the Add/Edit Cloud modal), the |morpheus| Agent can manage host or VM IP Table (firewall) rules for Linux workloads.

**Summary and Additional benefits:**

* Installation is optional for provisioned and managed VMs
* The Linux agent can be shrunk and should be less then 0.2% peak
* Provides a command bus such that |morpheus| doesn't need credentials to access a box
* Can still manage workflows if credentials are changed
* SSH agent can be disabled and still get access to the box
* Agent can be installed over Cloud-init, Windows unattend.xml, VMware Tools, SSH, WinRM, Cloudbase-Init, or manually
* Makes a single, persistent connection over HTTPS websocket and runs as a service
* Buffers and compresses logs, then sends them in chunks to minimize packets
* Supports syslog forwarding
* Accepts commands, executes commands, writes files, and manipulates firewalls
* Significantly enhances Guidance recommendations through enhanced statistics

.. NOTE:: The |morpheus| Agent is required for managed Docker, Kubernetes, SCVMM, Hyper-V, KVM, and ESXi Hosts (for ESXi-only Cloud, not vCenter Clouds).
