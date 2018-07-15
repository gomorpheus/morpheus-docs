Console not connecting
==========================

Protocols
---------

- SSH
    The SSH protocol will be used for Linux and OSX platform types
- RDP
    The RDP (Remote Desktop) protocol will be used for Windows platform types
- VNC (VMware Hypervisor Console)
    The VNC protocol will be used for all platform types in VMware Clouds with the ```Hypervisor Console`` option enabled in cloud settings.

Role Settings
-------------

- Remote Console (None, Provisioned, Full)
   None
    The user will not have access to remote console.
   Provisioned
    The user will only have remote console access for Instances they provisioned.
   Full
    The user will have remote console access for all instances they have access to.
- Remote Console: Auto Login (No, Yes)
   No
    A login prompt will be present in the console for Linux platforms, and the main login screen will present for Windows platforms.
   Yes
    

SSH
------------













VMware Hypervisor Console

|morpheus| features Remote Console support directly to VMware ESXi hypervisors. To enable this feature a few prerequisites must be met:

* The |morpheus| appliance must have network access to the ESXi hosts within vCenter.

* Firewall settings need to be adjusted on each ESXi host. This can be done in vSphere under firewall configuration on the ESXi hosts. Simply check the gdbserver option for each required host, which will open up the necessary ports (starting at the 5900 range).

* The |morpheus| must be able to resolve the ESXi hostnames.

Now that the ESXi hosts are ready to utilize remote console, simply edit the cloud in |morpheus| via `Infrastructure → Clouds`. Check the option that says Use Hypervisor Console. |morpheus| is now able to use the VMware Remote Console without opening any ports on the Virtual Machines.
