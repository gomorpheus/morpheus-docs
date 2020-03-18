Morpheus Agent Features
-----------------------

* Provides key enhanced statistics
  - Memory
    - Max Memory
    - Used Memory
    - Cache Memory
  - Storage
    - Max Storage
    - Used Storage
  - CPU 
    - System CPU % 
    - User CPU %
  - IOPS 
    - Total IOPS
    - IOPS Read 
    - IOPS Write 
  - Network 
    - Net TX Rate 
    - Net RX Rate 
    
* Handles log aggregation
* Provides a command bus to where |morpheus| doesn't need to get credentials to access a box. Can still run workflows if credentials are changed
* SSH agent can be disabled and still get access to the box
* Agent can be installed over Cloud-init, Windows unattend.xml, VMware Tools, SSH, WinRM, Cloudbase-init, or manually.
* Makes a single connect that's persistence over HTTPs web socket and runs as a service
* Health and Monitoring Checks
* Agent buffers and compresses logs and sends them in chunks to minimize packets
* Supports syslog forwarding
* Linux agent can be shrunk and should be less then 0.2% peak
* Accepts commands, can execute commands, write files, and manipulate firewalls
* Agent installation is optional for provisioned and managed VM's.
  - The |morpheus| Agent is required for managed Docker, Kubernetes, SCVMM, Hyper-V, KVM and ESXi Hosts (for ESXi only cloud, not vCenter Clouds). 
