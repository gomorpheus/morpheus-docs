Remote Console
==============

|morpheus| has a built in Remote Console for Instances, Hosts, Virtual Machines and Bare Metal.  The following information reviews the Roles Settings, Protocols, and Requirements necessary to configure and troubleshoot Remote Console access.

Role Settings
-------------

User Role settings determine if the Console tab or ``Open Console`` Action appear for a user, and if a login prompt is presented or the user is automatically logged in when using the Console.

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
      |morpheus| will automatically login to the remote console using the credentials defined on the VM or Host. For provisioned Instances, the credentials are defined either from the credentials defined on the Virtual Image used, added via cloud-init or VMware Tools using the global cloud-init settings (Administration - Provisioning) or the Linux or Windows settings defined in User Settings. For Instances created when converting a VM or Host to managed, the credentials are entered when converting to managed. These credentials can be changed by editing the underlying VM or Host of the Instance.

      .. NOTE:: If the credentials defined on the VM or Host are not valid, and the ``Remote Console: Auto Login`` Role setting is set to ``Yes``, the console will not be able to connect and no console window or login prompt will be presented. The credentials on the underlying VM or Host must be edited or ``Remote Console: Auto Login`` Role setting can be set to ``No`` for a login prompt to present in the console. Credentials cannot be changed from an Instance view, only in the Infrastructure VM or Host view.

Protocols
---------

Platform Type and Cloud Settings determines the protocol and port used for Remote Console connections.

- SSH
   The SSH protocol will be used for Linux and OSX platform types, and 22 is the default port used.
- RDP
   The RDP (Remote Desktop) protocol will be used for Windows platform types over port 3389 by default.
- VNC (VMware Hypervisor Console)
   The VNC protocol will be used for all platform types in VMware Clouds with the ``Hypervisor Console`` option enabled in cloud settings. A unique port is assigned per per Virtual Machine starting at 5900.

.. NOTE:: Alternative ports can be configured per VM or Host by editing the VM or Host and editing the Port field in the RPC host section.

SSH
^^^

For all Linux and OSX platform types, |morpheus| will use the SSH protocol via port 22 by default for Remote Console connections, unless the `Hypervisor Console`` option is enabled for VMware type clouds.

|morpheus| will SSH using the username, password, RPC Host IP address and Port defined in the VM or Host record.

Default Requirements for SSH Connectivity

- SSH Enabled on the target VM or Host
- Port 22 incoming open on the target VM or Host firewalls and security groups from the |morpheus| Appliance (not from the users IP address)
- An IP address defined on the VM or Host record that is routable from the |morpheus| Appliance.
- Valid credentials defined on the VM or Host record in the RPC host field.
- `Remote Console` Role Permissions set to `Provisioned` or `Full` if the User provisioned the instance, or `Full` if the user did not provision the instance.

RDP
^^^

For all Windows platform types, |morpheus| will use the RDP protocol via port 3389 by default for Remote Console connections, unless the `Hypervisor Console`` option is enabled for VMware type clouds.

|morpheus| will RDP using the username, password, RPC Host IP address and Port defined in the VM or Host record.

Default Requirements for RDP Connectivity

- Remote Access enabled on the target VM or Host and Remote Desktop enabled in the Windows Firewall settings. If the VM or Host is on a different network than the |morpheus| appliance, public access for Remote Desktop must be enabled in the Firewall settings.
- Port 3389 incoming open on the target VM or Host firewalls and security groups from the |morpheus| Appliance (not from the users IP address)
- An IP address defined on the VM or Host record that is routable from the |morpheus| Appliance.
- Valid credentials defined on the VM or Host record in the RPC host field.
- `Remote Console` Role Permissions set to `Provisioned` or `Full` if the User provisioned the instance, or `Full` if the user did not provision the instance.

.. NOTE:: If `Remote Console: Auto Login` is set to `No` in a users Role permissions, `Allow connections only from computers running Remote Desktop with Network Level Authentication` in the `Windows System Properties -> Remote` settings must be DISABLED for Remote Console to connect.


VNC (VMware Hypervisor Console)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the ``Hypervisor Console`` option is enabled in VMware cloud settings, the VNC protocol will be used for all platform types that VMware Cloud.

When using VNC Hypervisor Console, the |morpheus| Appliance connects directly to the ESXi host the VM is on, not directly to the VM. A VNC port is assigned per Virtual Machine starting at 5900 and a complex VNC password is generated. VNC is then enabled and the port and password are set on the VMs settings in vSphere.

|morpheus| features Remote Console support directly to VMware ESXi hypervisors. To enable this feature a few prerequisites must be met:

* The gdbserver Firewall setting needs to be enabled on each ESXi host the console will connect to. This can be done in vSphere under firewall configuration on the ESXi hosts by checking the gdbserver option on each required host, This will open up the necessary ports VNC ports on the ESXi host(s), starting at port 5900.

.. NOTE:: The most common cause of Remote Console connection issues when using hypervisor console is gdbserver not being enabled on the ESXi hosts firewall settings.

* The |morpheus| Appliance must have network access to the ESXi hosts within vCenter, specifically to the host the VM is on when using Remote Console, over the VNC port range, typically 5900-6000. The connection does not go through the vCenter server(s).

* The |morpheus| Appliance must be able to resolve the ESXi hostnames.

* VMware tools or equivalent must be installed on the VM.

Unlike SSH and RDP, valid credentials do not need to be set on the VM or Host records in |morpheus| for VNC hypervisor console connections. An IP address is also not required on the VM or Host for VNC hypervisor console connections. |morpheus| will be able to connect to the VVM or Host as soon as the ``Host (Hypervisor)`` record is set, which can be viewed in the Info section on the VM or Host detail page.

.. NOTE::
  - Auto-login is not supported for Hypervisor Console. Auto-login role settings do not apply to console connecting when using Hypervisor Console. Please note Hypervisor Console sessions persist on the ESXi host and once a user manually logs in to the VM they will continue to be logged in, even if the console tab/window in |morpheus| is closed, until they manually log out.
  - Copy and Paste and Text selection in Linux terminals is not supported when using VNC (VMware Hypervisor Console).
  - In |morpheus| versions 3.2.0 and higher, a newer Guacamole version is installed that is not compatible with MacOS Platform Types over VNC. The

.. IMPORTANT:: All VMs that are inventoried or provisioned into a VMware cloud with Hypervisor Console enabled will have their Console Type set to VNC. Disabling Hypervisor Console will only apply to newly inventoried or provisioned VM's. VM's inventoried or provisioned when Hypervisor Console was enabled will continue to use the VNC protocol even after Hypervisor Console is disabled. To revert a VM


Copy and Paste
--------------

Copy and Paste for Text is supported for SSH and RDP protocols only.

To Copy text from the console:

#. Select text in the Console window.
#. Click the COPY button at the top of the Console window.
#. The selected text is copied to the users clipboard.

To Paste text into console:

#. Copy text on the local computer to you clipboard
#. Right click into the "Paste Text Here" field at the top of the Console window. The field will the display "Text Copied, Use Console to Paste."
#. Right click into the console window.
#. The text is pasted into the VM.

Guacamole
---------

Overview
^^^^^^^^

|morpheus| uses Apache Guacamole, a clientless remote console. Guacamole is installed on the |morpheus| Appliance during the initial reconfigure. In |morpheus| versions 3.2.0 and higher, Guacamole 0.9.14 is automatically installed. On |morpheus| versions older than 3.2.0, 0.9.9 is installed. The 0.9.14 version is required for VNC Hypervisor Console functionality on ESXi v6.5 and later.

The Guacamole proxy daemon, guacd, is used for all Remote Console connections and must be running for Remote Console functionality.

Troubleshooting guacd
^^^^^^^^^^^^^^^^^^^^^

If all console connections are not functioning, the Guacamole proxy daemon (guacd) process may not be running or have a stuck process preventing console connections. This is evident when only the header appears in the console tab/window, and no console window appears below the header and no connection status is show in the console header. The following commands can be used on the |morpheus| Appliance to restore console functionality.

``morpheus-ctl status``
  Lists all local |morpheus| services including guacd and their states. If guacd is stopped, it will need to be started again for Remote Console to function.
``morpheus-ctl start guacd``
  Starts the guacd process
``morpheus-ctl stop guacd``
  Stops the guacd process
``morpheus-ctl kill guacd``
  Forcefully kills the guacd process
``morpheus-ctl restarts guacd``
  Restarts the guacd process
``morpheus-ctl tail guacd``
    Tails the guacd current and state logs, located by default at ``/var/log/morpheus/guacd/``. This log is useful when troubleshooting console connections, guacamole service status, and to determine the protocol being used for the Remote Console connection.

If guacd continues to stop even after being started, or if guacd is running and no properly configured console connections are functioning, there may be a stuck guacd or multiple guacd processes running, which will need to killed and guacd started again.

To kill all guacd processes on the |morpheus| Appliance and start guacd again:

#. Kill the morpheus gaucd proccess: ``morpheus-ctl kill guacd``
#. Grep for all running guacd processes: ``sudo ps -aux | grep guacd`` and note the guacd pid(s) (minus the process from the grep)
#. Kill all running guacd processes: ``kill -9 pid`` replacing `pid` with the pid(s) of the target processes
#. Start guacd again: ``morpheus-ctl start guacd``
#. Tail the guacd logs to verify guacd is started and listening: ``morpheus-ctl tail guacd`` The log output will resemble below when guacd is properly running:

   .. code-block:: bash

      guacd[16899]: INFO:	Guacamole proxy daemon (guacd) version 0.9.14 started
      guacd[16899]: INFO:	Listening on host 127.0.0.1, port 4822

#. Additional information in the guacd logs appears when |morpheus| is making a console connection. A successful conneciton will resemble:

   .. code-block:: bash

    guacd[24725]: INFO:	Creating new client for protocol "ssh"
    guacd[24725]: INFO:	Connection ID is "$24f67856-f050-4a17-83eb-9101g0cd8869"
    guacd[24743]: INFO:	Current locale does not use UTF-8. Some characters may not render correctly.
    guacd[24743]: INFO:	User "@63102f19-eff4-412e-b1f9-718405f55782" joined connection "$24f67856-f050-4a17-83eb-9101g0cd8869" (1 users now present)
    guacd[24743]: INFO:	Auth key successfully imported.
    guacd[24743]: INFO:	SSH connection successful.

Guacamole Version
^^^^^^^^^^^^^^^^^

In |morpheus| versions 3.2.0 and higher, Guacamole version 0.9.14 is automatically installed. On |morpheus| versions older than 3.2.0, 0.9.9 is installed. The 0.9.14 version is required for VNC Hypervisor Console functionality on ESXi v6.5 and later.

Note Guacamole version 0.9.14 is not compatible with MacOS Platform Types over VNC on ESXi v6.0 or prior (6.5 is supported). If necessary, the guacamole version can be reverted to 0.9.9.

To revert the guacamole version from 0.9.14 to 0.9.9.

#. Kill guacd - ``morpheus-ctl kill guacd``
#. Check if any guacd processes are still running ``ps -aux | grep guac``
#. If so, kill the processes ``kill -9 pid`` with id being the actual process id, like 16101.
#. Go to the guac 0.9.9 directory: ``cd /var/opt/morpheus/guacamole-server-0.9.9``
#. Run: ``make install``
#. Start guacd: ``morpheus-ctl start guacd``
