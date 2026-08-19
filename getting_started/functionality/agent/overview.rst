Overview
--------

The |morpheus| Agent is an important and powerful facet of |morpheus| as an orchestration tool.  Though it is not required, which is one unique capability of our platform versus some of our competitors, it is recommended for use as it brings many benefits.  Not only does it provide statistics for the guest operating system and resource utilization, it also brings along with it monitoring and log aggregation capabilities.  After an initial brownfield discovery, Users can decide to convert unmanaged VMs to managed.

.. NOTE::
      **Agent installation is not required to manage an Instance.**  If you don't have the Agent installed, we make every effort to aggregate stats. These will vary based on the Cloud and can be more limited or less accurate without utilizing |morpheus| Agent.

The |morpheus| Agent does not listen on an inbound management port. It initiates an outbound HTTPS/WSS connection to the configured |morpheus| appliance on TCP 443. The persistent connection carries inventory, statistics, monitoring and log data to the appliance and carries Manager-requested actions back to the workload. This design removes the need for the Manager to initiate SSH or WinRM sessions after installation, but it is not a read-only telemetry channel.

Agent Security Boundary
^^^^^^^^^^^^^^^^^^^^^^^

Treat control of the |morpheus| Manager and an Agent's API key as a remote-shell-equivalent trust boundary. An authorized Manager action can ask the Agent to execute a command, write or transfer files, and perform workload-management operations. On Linux, the Agent runs as the ``morpheus-node`` service account and uses configured ``sudo`` permissions for privileged operations. HVM Host Agents have additional privileged storage, virtualization, fencing, mount, and reboot responsibilities. Apply least privilege to |morpheus| roles, protect Agent keys and Manager administrator access, and review activity/audit records for administrative actions.

The principal Linux locations and processes to include in host monitoring are:

- ``/opt/morpheus-node`` for Agent binaries and runtime files
- ``/etc/morpheus/morpheus-node.yaml`` for Agent configuration
- ``/var/log/morpheus-node`` for Agent logs
- ``morphd``, supervised by the ``morpheus-node-runsvdir`` service

The Agent's ``verifyPeer`` configuration controls certificate-chain verification for its outbound connection. When ``verifyPeer`` is ``true``, the appliance endpoint must present a certificate trusted by the Agent host. When it is absent or ``false``, the Agent runtime does not validate the peer certificate chain. Use a trusted appliance certificate and enable peer verification where required by organizational policy; test certificate trust before enforcing the setting broadly.

Agent packages and scripts must come from the configured |morpheus| appliance or an HPE-published package source for the applicable release. Package availability is release-, OS-, and architecture-specific; successful execution on an unlisted platform does not establish support. Upgrade Agents through the Manager's **Upgrade Agent** action or a newly downloaded, resource-specific Agent script, and verify that the Agent reconnects and reports the expected version.

Customer security controls should allow only the required Manager-to-Agent administration and Agent-to-Manager path. Monitor changes under the Agent paths, restrict who can request Agent actions, protect backups containing Agent configuration, and investigate unexpected Agent command or file activity as privileged remote administration.
