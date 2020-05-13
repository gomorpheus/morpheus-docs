|morpheus| Agent Key Features
-----------------------------

**Key Enhanced Statistics and Benefits**

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
| Processing                | System CPU %            | Yes            | Yes               |
+---------------------------+-------------------------+----------------+-------------------+
| Processing                | User CPU %              | Yes            | No                |
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

**Additional benefits:**

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

.. NOTE:: The |morpheus| Agent is required for managed Docker, Kubernetes, SCVMM, Hyper-V, KVM, and ESXi Hosts (for ESXi-only Cloud, not vCenter Clouds).
