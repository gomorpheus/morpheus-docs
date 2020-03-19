Overview
--------

The |morpheus| Agent is an important and powerful facet of |morpheus| as an orchestration tool.  Though it is not required, which is one unique capability of our platform versus some of our competitors, it is recommended for use as it brings many benefits.  Not only does it provide statistics for the guest operating system and resource utilization, it also brings along with it monitoring and log aggregation capabilities.  After an initial brownfield discovery, Users can decide to convert unmanaged VMs to managed.

.. NOTE::
      **|morpheus| does not require Agent installation to manage an Instance.**  If you don't have the Agent installed, we make every effort to aggregate stats. These will vary based on the Cloud and can be more limited or less accurate without utilizing |morpheus| Agent.

The |morpheus| Agent is very lightweight and secure. It does not open any inbound network ports but rather only opens an outbound connection back to the |morpheus| appliance over port 443 (HTTPS or WSS protocol). This allows for a bidirectional command bus where instructions can be sent to orchestrate a workload without needing access to things like SSH or WinRM. The tool can even be installed at provision time via technologies like Cloud-Init, such that the |morpheus| appliance itself doesn't even need direct network access to the VLAN under which the workload resides. By doing this we address many of the network security concerns that come with the use of an agent while demonstrating its security and analytics benefits. We can even use this statistical data at the guest OS level rather than the hypervisor level to provide extremely precise right-sizing recommendations.
