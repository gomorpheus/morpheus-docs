Morpheus Agent
===============

The |morpheus| Agent is an important and powerful facet of |morpheus| as a orchestration tool.  Though it is not required (one unique capability of our platform vs. some of the competitors out there), it is recommended for use as it brings with it a lot of insightful benefits.  Not only does it provide statistics of the guest operating system and resource utilization, it also brings along with it monitoring and log aggregation capabilities.  After an initial brownfield discovery users can decide to convert unmanaged VMs to managed.  The |morpheus| Agent is very lightweight and secure.


.. NOTE::
      **The agent is not required** by |morpheus| to become a managed instance.  If you don't have the agent installed we try to aggregate stats but it can vary based on the cloud and can be limited or inaccurate.

The |morpheus| Agent does not open any inbound network ports but rather only opens an outbound connection back to the Morpheus appliance over port 443 (https or wss protocol). This allows for a bidirectional command bus where instructions can be sent to orchestrate a workload without needing access to things like SSH or WinRM.

The tool can even be installed at provision time via things like cloud-init, such that the |morpheus| appliance itself doesn't even need direct network access to the VLAN under which the workload resides. By doing this we address many of the network security concerns that come up with regards to the agent while demonstrating its security benefits as well as analytics benefits. We can even use this statistical data at the guest OS level rather than the hypervisor level to provide extremely precise right-sizing recommendations.


Key Agent Features
-------------------
* Provides key enhanced statistics (disc usage, CPU usage, network, disc IO)
* Handles log aggregation
* Provides a command bus to where |morpheus| doesn't need to get credentials to access a box. Can still run workflows if credentials are changed
* SSH agent can be disabled and still get access to the box
* Agent can be installed over Cloud Init for internetless situations
*  **The Morpheus agent is optional**
* Makes a single connect that's persistence over HTTPs web socket and runs as a service
* Health checks for Linux (not available on windows)
* **No inbound Ports**
* Agent buffers and compresses logs and sends them in chunks to minimize packets
* Can be configured to collect logs and send them somewhere
* Linux agent can be shrunk and should be less then .2% peak (Windows less 97 kb)
* Run workflows, Have expiration/shutdown policies and can help reign in environments amongst other things
* Accepts commands, can execute commands, write files, and manipulate firewall

Agent Install Modes
-------------------
There are 5 Agent install modes:

- SSH / WinRM /Guest Execution
- VMware Tools / guest execution
- cloud-init / cloudbase-init
- Unattend
- Manual installation

On each cloud, you can select between two options for your preferred agent installation method under advanced options.  The recommended method to install the |morpheus| agent is cloud init / Unattend (when available).  If this fails it will call back to SSH / WinRM / Guest Execution.  


.. IMPORTANT::
    For |morpheus| agent installation issues please consult our troubleshooting guide :ref:`Agent Troubleshooting`

Morpheus Agent Support
------------------------

Microsoft Windows
^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: if you require tls 1.2 then .net 4.5 should be installed.

* Windows Server 2008R2 (Requires .Net 4.3 framework)
* Windows Server 2012
* Windows Server 2012R2
* Windows Server 2016
* Windows Server 2019
* Windows 10 PRO

Redhat Based linux Distrubution:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Redhat 6.6
* Redhat 7.x
* CentOS 6.x
* CentOS 7.x
* Oracle 6.x
* Oracle 7.x

.. important:: Amazon Linux is not supported by the Morpheus Agent

Debian Based linux Distrubutions:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Ubuntu 14.04.x (Only supported for VMs, not Docker hosts)
* Ubuntu 16.04.x
* Ubuntu 18.04.x
* Debian 8.x
* Debian 9.x

Unix Based Operating Systems:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* MacOS Mojave
* MacOS High Sierra
* MacOS Sierra
