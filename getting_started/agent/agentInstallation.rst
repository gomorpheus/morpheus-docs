Agent Installation
==================

There are numerous methods to install the |morpheus| Agent on supported Targets. All Agent Installation Methods are executing a script on the target that calls back to the |morpheus| Appliance over 443.  

.. important:: All Agent Installation Methods require the Target (vm/host) to resolve and reach Appliance URL over 443. In addition to the main appliance_url in Admin -> Settings, additional appliance_urls can be set per cloud in the Advanced options of the cloud configuration pane when creating or editing a cloud. When this field is populated, it will override the main appliance url for anything provisioned into that cloud.

Basic Installation Steps
^^^^^^^^^^^^^^^^^^^^^^^^
#. An Agent Installation Method is used to get the Agent Installation Script on the Target VM or Host
#. The Agent Installation Script is executed on the Target VM or Host, installing the Agent and dependencies.
#. The Agent is started and makes a websocket connection to the configured Appliance URL over 443 using the Target VM/Host API Key.

It is important to note these are 3 separate steps with varying requirements. The first requires a path to get the script on the Target. The second requires successful execution of the Agent Installation Script. The 3rd requires a successful websocket connection. Requirements for the successful execution of each step are covered in the sections below. 

.. TIP:: The |morpheus| UI current log, located at /var/log/morpheus/morpheus-ui/current, is very helpful when troubleshooting agent installations.

Agent Install Modes
^^^^^^^^^^^^^^^^^^^

Agent Installation Method is determined by:
 - AGENT INSTALL MODE setting on Target Cloud
   - SSH / WinRM / Guest Execution 
   - Cloud Init / Unattend (when available)
 - Platform / OS Type on Virtual Image or VM/Host
 - Virtual Image Configuration
 - RPC Mode Setting (VMware Clouds only)  
 
Agent Installation Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Morpheus Agent can be installed with a variety of automated methods. It is important to note these methods simply get the Agent Install Script on the target, and successful execution of the Agent Install Script is not directly related to an Agent Install Method. 

ssh
 Morpheus ssh’s to the VM/Host, curls and executes Agent Install script 
  eg curl -k -s "https://${applianceUrl}/api/server-script/agentInstall?apiKey=${apiKey}" | bash
winRM
 Morpheus winRM’s to VM/Host and executes Agent Install script. 
VMware Tools
 Morpheus executes agentInstall.sh or agentInstall.ps1 via VMware Tools Guest Execution 
Cloud-init
 Morpheus executes agentInstall.sh via cloud-init runcmd
Cloudbase-init
 Morpheus adds WindowsAgentCloudInitInstallScript to CloudbaseInitUserData
Windows Unattend
 Morpheus adds getWindowsAgentDownloadScript to unattend.xml (RunSynchronousCommand)
Manual
 User executes agentInstall.sh or agentInstall.ps1 manually on VM/Host. These scripts can be obtained on the vm or host detail page via ``Actions -> Download Agent Script``


SSH
^^^

Process
```````
Morpheus ssh’s to the VM/Host, curls and executes Agent Install script 
  eg curl -k -s "https://${applianceUrl}/api/server-script/agentInstall?apiKey=${apiKey}" | bash

Requirements
````````````
* Port 22 is open for Linux images, and ssh is enabled
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the Provisioning -> Virtual Images section.

WinRM
^^^^^

Process
```````
Morpheus winRM’s to VM/Host and executes Agent Install script. 

Requirements
````````````
* Port 5985 must be open and winRM enabled for Windows images.
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the Provisioning -> Virtual Images section.
* Administrator User (SID 500) is required for Windows agent install.

VMware Tools
^^^^^^^^^^^^

Process
```````
Morpheus executes agentInstall.sh or agentInstall.ps1 via VMware Tools Guest Execution 

Requirements
````````````
* VMware tools is installed on the template(s)
* Credentials have been entered on the Image if using uploaded or synced image when Cloud-init or Guest Customizations or Sysprep for Windows are not used. Credentials can be entered on Images in the `Provisioning -> Virtual Images` section.
* Administrator User (SID 500) is required for Windows agent install.

Cloud-Init
^^^^^^^^^^

Process
```````
Morpheus executes agentInstall.sh via cloud-init runcmd

Requirements
````````````
* Cloud-init installed on Virtual Image
* "IS CLOUD INIT ENABLED?" checked/true on Virtual Image record
* Cloud-Init User is configured in Admin -> Provisioning section

Cloudbase-init
^^^^^^^^^^^^^^

Process
```````
Morpheus adds WindowsAgentCloudInitInstallScript to CloudbaseInitUserData
Requirements
````````````
* Cloudbase-init installed on Virtual Image
* "IS CLOUD INIT ENABLED?" checked/true on Virtual Image record
* Windows Administrator Password defined in Admin -> Provisioning section

Windows Unattend
^^^^^^^^^^^^^^^^

Process
```````
Morpheus adds getWindowsAgentDownloadScript to unattend.xml (RunSynchronousCommand)

Requirements
````````````
VMware 
  - Windows Administrator Password defined in Admin -> Provisioning section
    - OR ``Administrator`` User (SID 500) and valid Windows password defined on Virtual Image Record 
  - "FORCE GUEST CUSTOMIZATION?" checked/true on Virtual Image Record when using DHCP
  - "IS CLOUD INIT ENABLED?" unchecked/false on Virtual Image record
  
Nutainx/SCVMM/Openstack
  - Windows Administrator Password defined in Admin -> Provisioning section
    - OR ``Administrator`` User (SID 500) and valid Windows password defined on Virtual Image Record 
  - "ENABLED SYSPREP?" checked/true on Virtual Image Record
  - "IS CLOUD INIT ENABLED?" unchecked/false on Virtual Image record
 
Manual
^^^^^^

Process 
```````
#. From the VM/Host record page (``/infrastructure/servers/${id}``) run :guilabel:`ACTIONS` -> ``Download Agent Script``
   - This is will generate an Agent Install Script based of the Target VM/Host OS/Platform, Appliance URL, and API Key.  
#. Manually execute the downloaded script on the Target VM or Host


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
