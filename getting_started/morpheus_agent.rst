Morpheus Agent
===============

The |morpheus| agent is an important and powerful facet of |morpheus| as a orchestration too.  Though it is not required (one unique capability of our platform vs. some of the competitors out there), it is recommended for use as it brings with it a lot of insightful benefits.  Not only does it provide statistics of the guest operating system and resource utilization, it also brings along with it monitoring and log aggregation capabilities.  After an initial brownfield discovery users can decided to convert unmanaged vms to managed.  The |morpheus| agent is very lightweight and secure.


  .. NOTE::
      **The agent is not required** by |morpheus| to become a managed instance. Once a vm is managed it can run workflows, have expiration/shutdown   policies and can help reign in environments amongst other things.

 The Morpheus agent does not open any inbound network ports but rather only opens an outbound connection back to the Morpheus appliance over port 443 (https or wss protocol). This allows for a bidirectional command bus where instructions can be sent to orchestrate a workload without needing access to things like SSH or WinRM. The tool can even be installed at provision time via things like cloud-init such that the Morpheus appliance itself doesn't even need direct network access to the VLAN under which the workload resides. By doing this we address many of the network security concerns that come up with regards to the agent and also demonstrate its security benefits as well as analytics benefits. We can even use this statistical data at the guest OS level rather than the hypervisor level to provide even better right-sizing recommendations than a tool like turbonomics could.


Key Agent Features
-------------------
* Provides key statics (disc usage, CPU usage)
* Handles log aggregation
* Very secure and does not require credentials to get into box.
* SSH agent can be disabled and still get access to the box.
* Agent can be installed over Cloud Init for internetless situations
*  **The |morpheus| agent is optional**
* Makes a single connect over HTTPs and runs as a service
* Health checks for Linux (not available on windows)
* **No inbound Ports**
