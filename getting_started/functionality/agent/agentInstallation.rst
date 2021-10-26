Agent Installation
------------------

There are many methods to install the |morpheus| Agent on supported targets. All Agent installation methods are executing a script on the target that calls back to the |morpheus| appliance over port 443.

.. important:: All Agent installation methods require the Target (VM or Host) to resolve and reach the appliance URL over port 443. In addition to the main Appliance URL (in |AdmSet|), additional Appliance URLs can be set per cloud in the Advanced Options section of the Create/Edit Cloud modal. When this field is populated, it will override the main Appliance URL for anything provisioned into that Cloud.

Basic Installation Steps
^^^^^^^^^^^^^^^^^^^^^^^^
#. An Agent installation method is used to get the install script onto the target VM or Host
#. The Agent installation script is executed on the target VM or Host, installing the Agent and all dependencies
#. The Agent is started and makes a websocket connection to the configured Appliance URL over port 443 using the target VM or Host API key

It is important to note these are three separate steps with varying requirements. The first requires a path to get the script on the target. The second requires successful execution of the Agent installation script. The third requires a successful websocket connection. Requirements for the successful execution of each step are covered in the sections below.

.. TIP:: The |morpheus| UI current log, located at /var/log/morpheus/morpheus-ui/current, is very helpful when troubleshooting Agent installations.

Agent Install Modes
^^^^^^^^^^^^^^^^^^^

Agent Installation Method is determined by:

- The AGENT INSTALL MODE setting on target Cloud:
  - SSH / WinRM / Guest Execution
  - Cloud Init / Unattend (when available)
- Platform / OS type on Virtual Image or target (VM or Host)
- Virtual Image configuration
- RPC Mode setting (VMware Clouds only)

Agent Installation Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Morpheus Agent can be installed with a variety of automated methods. It is important to note these methods simply get the Agent install script to the target. Successful execution of the Agent install script is not directly related to the Agent install method.

SSH
 |morpheus| makes an SSH connection to the VM or Host, CURLs, and executes the Agent install script:

 ``curl -k -s "https://${applianceUrl}/api/server-script/agentInstall?apiKey=${apiKey}" | bash``

WinRM
 |morpheus| makes a WinRM connection to the VM or Host and executes the Agent install script

VMware Tools
 |morpheus| executes agentInstall.sh or agentInstall.ps1 via VMware Tools Guest Execution

Cloud-Init
 |morpheus| executes agentInstall.sh via cloud-init runcmd

Cloudbase-Init
 |morpheus| adds WindowsAgentCloudInitInstallScript to CloudbaseInitUserData

Windows Unattend
 |morpheus| adds getWindowsAgentDownloadScript to unattend.xml (RunSynchronousCommand)

Manual
 User executes agentInstall.sh or agentInstall.ps1 manually on the VM or Host. These scripts can be obtained on the VM or Host detail page via Actions > Download Agent Script

SSH
```

Process
.......

|morpheus| makes an SSH connection to the VM or Host, CURLs, and executes the Agent install script:

``curl -k -s "https://${applianceUrl}/api/server-script/agentInstall?apiKey=${apiKey}" | bash``

Requirements
............

* Port 22 is open for Linux images, and SSH is enabled
* Credentials have been entered on the image if using a custom or synced image. Credentials can be entered on images in the |LibVir| section

WinRM
`````

Process
.......

|morpheus| makes a WinRM connection to the VM or Host and executes the Agent install script

Requirements
............

* Port 5985 must be open and winRM enabled for Windows images
* Credentials have been entered on the image if using a custom or synced image. Credentials can be entered on images in the |LibVir| section
* Administrator User (SID 500) is required for Windows Agent install

VMware Tools
````````````

Process
.......

|morpheus| executes agentInstall.sh or agentInstall.ps1 via VMware Tools Guest Execution

Requirements
............

* VMware Tools is installed on the template(s)
* Credentials have been entered on the Image if using an uploaded or synced image when Cloud-init, Guest Customizations, or Sysprep for Windows are not used. Credentials can be entered on Images in the |LibVir| section
* Administrator User (SID 500) is required for Windows Agent install.

Cloud-Init
``````````

Process
.......

|morpheus| executes agentInstall.sh via Cloud-Init runcmd

Requirements
............

* Cloud-Init is installed on Virtual Image
* "IS CLOUD INIT ENABLED?" is checked (true) on the |morpheus| Virtual Image record
* Cloud-Init User is configured in the Admin > Provisioning section

Cloudbase-init
``````````````

Process
.......
|morpheus| adds WindowsAgentCloudInitInstallScript to CloudbaseInitUserData

Requirements
............

* Cloudbase-Init is installed on the Virtual Image
* "IS CLOUD INIT ENABLED?" is checked (true) on the |morpheus| Virtual Image record
* Windows Administrator password defined in the Administration -> Provisioning section

Windows Unattend
````````````````

Process
.......

|morpheus| adds getWindowsAgentDownloadScript to unattend.xml (RunSynchronousCommand)

Requirements
............

VMware
  - Windows Administrator password defined in the |AdmSetPro| section OR Administrator User (SID 500) and valid Windows password are defined on the |morpheus| Virtual Image record
  - "FORCE GUEST CUSTOMIZATION?" is checked (true) on the |morpheus| Virtual Image record when using DHCP
  - "IS CLOUD INIT ENABLED?" is unchecked (false) on the |morpheus| Virtual Image record

Nutainx/SCVMM/Openstack
  - Windows Administrator password defined in the |AdmSetPro| section OR Administrator User (SID 500) and valid Windows password are defined on the |morpheus| Virtual Image record
  - "ENABLED SYSPREP?" is checked (true) on the |morpheus| Virtual Image record
  - "IS CLOUD INIT ENABLED?" is unchecked (false) on the |morpheus| Virtual Image record

Manual
``````

Process
.......

- From the VM or Host record page (``/infrastructure/servers/${id}``) run :guilabel:`ACTIONS` -> ``Download Agent Script``
- This is will generate an Agent install script based off the target OS and platform, Appliance URL, and API key
- Manually execute the downloaded script on the Target VM or Host


Agent Install Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Agent Installation Requirements                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Requirement                                                                              | Agent Installation Method                                                                                                                                                                                     |
|                                                                                          +------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
|                                                                                          | SSH                                      | WINRM | VMWARE TOOLS                             | CLOUD-INIT                               | CLOUDBASE-INIT | UNATTEND | MANUAL                                   |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Target (vm/host) to resolve and reach Appliance URL over 443                             | YES                                      | YES   | YES                                      | YES                                      | YES            | YES      | YES                                      |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Target (vm/host) to resolve and reach Appliance URL over 80                              | Ubuntu 14.04 Only                        |       | Ubuntu 14.04 Only                        | Ubuntu 14.04 Only                        |                |          | Ubuntu 14.04 Only                        |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Websockets enabled when using load balancer                                              | YES                                      | YES   | YES                                      | YES                                      | YES            | YES      | YES                                      |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Access to Target VM/Host on port 22                                                      | YES                                      | NO    | NO                                       | NO                                       | NO             | NO       | NO                                       |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Access to Target VM/Host on port 5985                                                    | NO                                       | YES   | NO                                       | NO                                       | NO             | NO       | NO                                       |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Vmware Tools installed and flagged on Virtual Image                                      | NO                                       | NO    | YES                                      | NO                                       | NO             | YES      | NO                                       |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Syspreped Image and Sysprep Enabled flagged on Virtual Image (Nutanix, Openstack, SCVMM) | NO                                       | NO    | NO                                       | NO                                       | NO             | YES      | NO                                       |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Force Guest Customizaitons flagged on Virtual Image                                      | NO                                       | NO    | DHCP                                     | NO                                       | NO             | DHCP     | NO                                       |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Cloud-Init installed and flagged on Virtual Image                                        | NO                                       | NO    | NO                                       | YES                                      | YES            | NO       | NO                                       |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Global Cloud-Init user populated in /admin/provisioning                                  | NO                                       | NO    | NO                                       | YES                                      | NO             | NO       | NO                                       |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Windows Administrator Password populated in /admin/provisioning                          | NO                                       | NO    | NO                                       | NO                                       | YES            | YES      | NO                                       |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Access to configured YUM or APT repos                                                    | NO but will cause delay in Agent Install | N/A   | NO but will cause delay in Agent Install | NO but will cause delay in Agent Install | N/A            | N/A      | NO but will cause delay in Agent Install |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| .net >=4.5.2 (Windows, Morpheus >= 4.1.2)                                                | N/A                                      | YES   | YES                                      | N/A                                      | YES            | YES      | YES                                      |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| User with Sudo Access set on Virtual Image (Greenfield)                                  | YES                                      | N/A   | YES                                      | NO                                       | N/A            | N/A      | N/A                                      |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Adminsitrator User (SID 500) set on Virtual Image  (Greenfield)                          | N/A                                      | YES   | YES                                      | N/A                                      | NO             | N/A      | N/A                                      |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| User with Sudo Access set on VM/Host Record (Brownfield)                                 | YES                                      | N/A   | YES                                      | N/A                                      | N/A            | N/A      | N/A                                      |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+
| Adminsitrator User (SID 500) set on VM/Host Record (Brownfield)                          | N/A                                      | YES   | YES                                      | N/A                                      | N/A            | N/A      | N/A                                      |
+------------------------------------------------------------------------------------------+------------------------------------------+-------+------------------------------------------+------------------------------------------+----------------+----------+------------------------------------------+



.. include:: /troubleshooting/Morpheus_Agent.rst
