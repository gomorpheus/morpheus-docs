|morpheus| Agent Key Features
-----------------------------

Key Enhanced Statistics:

**Memory**

  - Max Memory
  - Used Memory
  - Cache Memory

**Storage**

  - Max Storage
  - Used Storage

**Processing**

  - System CPU %
  - User CPU %

**IOPS**

  - Total IOPS
  - IOPS Read
  - IOPS Write

**Networking**

  - Net TX Rate
  - Net RX Rate

* Log aggregation
* Provides a command bus such that |morpheus| doesn't need credentials to access a box
* Can still manage workflows if credentials are changed
* SSH agent can be disabled and still get access to the box
* Agent can be installed over Cloud-init, Windows unattend.xml, VMware Tools, SSH, WinRM, Cloudbase-Init, or manually
* Makes a single, persistent connection over HTTPS websocket and runs as a service
* Health and monitoring checks
* Buffers and compresses logs, then sends them in chunks to minimize packets
* Supports syslog forwarding
* The Linux agent can be shrunk and should be less then 0.2% peak
* Accepts commands, executes commands, writes files, and manipulates firewalls
* Installation is optional for provisioned and managed VMs

.. NOTE:: The |morpheus| Agent is required for managed Docker, Kubernetes, SCVMM, Hyper-V, KVM, and ESXi Hosts (for ESXi-only Cloud, not vCenter Clouds).
