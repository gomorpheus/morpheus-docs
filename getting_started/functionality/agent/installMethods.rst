Agent Install Methods
=====================

|morpheus| Agent installation supports multiple install methods.

- SSH/WinRM
- VM Tools
- Cloud-Init & Cloudbase-Init
- Windows Unattended
- Manual

For All Agent Install Methods
-----------------------------

When an Instance is provisioned and the Agent does not install, verify the following for any Agent install mode:

- The |morpheus| Appliance URL (|AdmSet|) is both reachable and resolvable from the provisioned node
- The Appliance URL begins with https://, not http://

.. note:: Be sure to use https:// even when using an IP address for the appliance.

- Inbound connectivity access to the |morpheus| appliance from provisioned VMs and container hosts on port 443 (needed for Agent communication)
- Private (non-|morpheus| provided) VM images and templates must have their credentials stored. These can be entered or edited in the :menuselection:`Library --> Virtual Images` section by clicking the Actions dropdown on an image detail page and selecting Edit.

.. note:: Administrator user is required for Windows Agent install.

- The Instance does not have an IP address assigned. For scenarios without a DHCP server, static IP information must be entered by selecting the Network Type: Static in the Advanced Options section during provisioning. IP Pools can also be created in the :menuselection:`Infrastructure --> Networks --> IP Pools` section and added to Cloud network sections for IPAM
- DNS is not configured and the node cannot resolve the appliance. If DNS cannot be configured, the IP address of the |morpheus| appliance can be used as the main or Cloud appliance

SSH
---

- Port 22 is open for Linux images, and SSH is enabled
- Credentials set on the image if using a custom or synced image. Credentials can be entered on images in the :menuselection:`Library --> Virtual Images` section

WinRM
-----

- Port 5985 must be open and WinRM enabled for Windows images
- Credentials have been entered on the image if using a custom or synced image. Credentials can be entered on images in the :menuselection:`Library --> Virtual Images` section

.. note:: Administrator user is required for Windows Agent install.

VMware Tools (vmtools)
-----------------------

- VMware Tools is installed on the template(s)
- Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the :menuselection:`Library --> Virtual Images` section
- Sudo privileges required for Linux
- Administrator User required for Windows (SID 500)

Cloud-Init
----------

- Cloud-Init settings configured in :menuselection:`Administration --> Settings --> Provisioning` section
- Cloud-Init installed on Virtual Image
- ``Cloud-Init`` enabled on Virtual Image config

Cloudbase-Init
--------------

- Windows Administrator Password defined in :menuselection:`Administration --> Settings --> Provisioning` section
- Cloudbase-Init installed on Virtual Image
- ``Cloud-Init`` enabled on Virtual Image config
- Cloudbase-Init is only required for OpenStack Cloud types

.. note:: Unattend Agent Installation and customizations are recommended over Cloudbase-Init

Windows Unattended
------------------

- Windows Administrator Password defined in :menuselection:`Administration --> Settings --> Provisioning` section
- VMware: ``Force Guest Customizations`` set to forced on Virtual Image config when using DHCP (Static Assignment will already force Guest Customizations)
- Nutanix & SCVMM: Virtual Image is sysprepped and shutdown, ``Sysprep Enabled`` flagged on Virtual Image config

Manual
------

Agent Install scripts can be downloaded from |morpheus| by selecting :menuselection:`Actions --> Download Agent Script` from a Server detail page, then run manually on the target host when required for a given managed resource. Please note the script will be unique per managed resource and should not be saved to run as needed on any arbitrary resources in the future.

When installing on Windows, continue with the steps below to complete manual installation:

- Open powershell as an administrator
- Run the ``unblock-file cmdlet`` against the download agent installation script:

  .. code-block:: powershell

     Unblock-File -Path C:\Users\User01\Documents\Downloads\agentInstall.ps1
     Get-ExecutionPolicy
     Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

- After running the powershell script, ensure the script downloaded the msi and the Agent service started correctly:

  .. code-block:: powershell

     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Following setup, verify that the Agent is reporting back to the |morpheus| appliance.
