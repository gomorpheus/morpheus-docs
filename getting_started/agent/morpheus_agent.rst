Morpheus Agent
==============

Overview
--------

The |morpheus| Agent is an important and powerful facet of |morpheus| as a orchestration tool.  Though it is not required (one unique capability of our platform vs. some of the competitors out there), it is recommended for use as it brings with it a lot of insightful benefits.  Not only does it provide statistics of the guest operating system and resource utilization, it also brings along with it monitoring and log aggregation capabilities.  After an initial brownfield discovery users can decide to convert unmanaged vms to managed.  The |morpheus| Agent is very lightweight and secure.

.. NOTE::
      **The agent is not required** by |morpheus| to become a managed instance.  If you don't have the agent installed we try to aggregate stats but it can vary based on the cloud and can be limited or inaccurate.

The |morpheus| Agent does not open any inbound network ports but rather only opens an outbound connection back to the Morpheus appliance over port 443 (https or wss protocol). This allows for a bidirectional command bus where instructions can be sent to orchestrate a workload without needing access to things like SSH or WinRM. The tool can even be installed at provision time via things like cloud-init, such that the |morpheus| appliance itself doesn't even need direct network access to the VLAN under which the workload resides. By doing this we address many of the network security concerns that come up with regards to the agent while demonstrating its security benefits as well as analytics benefits. We can even use this statistical data at the guest OS level rather than the hypervisor level to provide extremely precise right-sizing recommendations.

.. toctree::
  :maxdepth: 2

  agent/features.rst
  agent/agentInstallation.rst
  agent/osSupport.rst
