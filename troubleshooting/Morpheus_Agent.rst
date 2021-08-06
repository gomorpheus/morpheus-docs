|morpheus| Agent Install Troubleshooting
========================================

When provisioning an Instance, there are network and configuration requirements to consider in order to successfully install the |morpheus| Agent. Typically, when a VM Instance is still in the provisioning phase long after the VM is up, the Instance is unable to reach |morpheus|. Depending on the Agent install mode, it could also mean |morpheus| is unable to reach the Instance.

The most common reason an Agent install fails is the provisioned Instance cannot reach the |morpheus| Appliance via the Appliance URL set in Administration > Settings over port 443. When an Instance is provisioned from |morpheus|, it must be able to reach the |morpheus| appliance via the Appliance URL or the Agent will not be installed.

.. image:: /images/agent-7c9a2.png

In addition to the main Appliance URL in Administration > Settings, additional Appliance URLs can be set per Cloud in the Advanced Options section of the Cloud configuration modal when creating or editing a Cloud. When this field is populated, it will override the main Appliance URL for anything provisioned into that Cloud.

.. TIP:: The |morpheus| UI current log, located at /var/log/morpheus/morpheus-ui/current, is very helpful when troubleshooting Agent installations.

Agent Install Methods
---------------------

Morpheus Agent installation supports multiple install methods.

- SSH/WinRM
- VM Tools
- Cloud-Init & Cloudbase-Init
- Windows Unattended
- Manual

For All Agent Install Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an Instance is provisioned and the Agent does not install, verify the following for any Agent install mode:

* The |morpheus| Appliance URL (Administration > Settings) is both reachable and resolvable from the provisioned node
* The Appliance URL begins with https://, not http://

.. NOTE:: Be sure to use https:// even when using an IP address for the appliance.

* Inbound connectivity access to the |morpheus| appliance from provisioned VMs and container hosts on port 443 (needed for Agent communication)

* Private (non-|morpheus| provided) VM images and templates must have their credentials stored. These can be entered or edited in the Provisioning > Virtual Images section by clicking the Actions dropdown on an imaged detail page and selecting Edit.

.. NOTE:: Administrator user is required for Windows Agent install.

* The Instance does not have an IP address assigned. For scenarios without a DHCP server, static IP information must be entered by selecting the Network Type: Static in the Advanced Options section during provisioning. IP Pools can also be created in the Infrastructure > Networks > IP Pools section and added to Cloud network sections for IPAM

* DNS is not configured and the node cannot resolve the appliance. If DNS cannot be configured, the IP address of the |morpheus| appliance can be used as the main or Cloud appliance

SSH
^^^

* Port 22 is open for Linux images, and SSH is enabled

* Credentials set on the image if using a custom or synced image. Credentials can be entered on images in the Provisioning > Virtual Images section

WinRM
^^^^^

* Port 5985 must be open and WinRM enabled for Windows images
* Credentials have been entered on the image if using a custom or synced image. Credentials can be entered on images in the Provisioning > Virtual Images section

.. NOTE:: Administrator user is required for Windows Agent install.

VMware Tools (vmtools)
^^^^^^^^^^^^^^^^^^^^^^

* VMware Tools is installed on the template(s)
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the Provisioning > Virtual Images section
* Sudo priveleges required for Linux
* Administrator User required for Windows (SID 500)

Cloud-Init
^^^^^^^^^^

* Cloud-Init settings configured in Administration > Provisioning section
* Cloud-Init installed on Virtual Image
* ``Cloud-Init`` enabled on Virtual Image config

Cloudbase-Init
^^^^^^^^^^^^^^

* Windows Administrator Password defined in ``Administration > Provisioning`` section
* Cloudbase-Init installed on Virtual Image
* ``Cloud-Init`` enabled on Virtual Image config

.. note:: Unattend Agent Installation and customizations are recommended over Cloudbase-Init

Windows Unattended
^^^^^^^^^^^^^^^^^^

* Windows Administrator Password defined in ``Administration > Provisioning`` section
* VMware: ``Force Guest Customizations`` set to forced on Virtual Image config when using DHCP (Static Assignment will already force Guest Customizations)
* Nutanix & SCVMM: Virtual Image is sysprepped and shutdown, ``Sysprep Enabled`` flagged on Virtual Image config

Manual
^^^^^^

Agent Install scripts can be downloaded from |morpheus| by selecting ``Actions > Download Agent Script`` from an Instance detail page, then run manually on the target host when required for a given managed resource. Please note the script will be unique per managed resource and should not be saved to run as needed on any arbitrary resources in the future.

When installing on Windows, continue with the steps below to complete manual installation:

* Open powershell as an administrator
* Run the ``unblock-file cmdlet`` against the download agent installation script:

  .. code-block:: bash

    Unblock-File -Path C:\Users\User01\Documents\Downloads\agentInstall.ps1

    Get-ExecutionPolicy

    Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

* After running the powershell script, ensure the script downloaded the msi and the Agent service started correctly:

  .. code-block:: bash

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Following setup, verify that the Agent is reporting back to the |morpheus| appliance.

Restarting the |morpheus| Agent
-------------------------------

In some situations, it may necessary to restart the |morpheus| Agent on the host to re-sync communication from the Agent to the |morpheus| appliance.

Linux
^^^^^

On the target host, run ``sudo morpheus-node-ctl restart morphd`` and the |morpheus| agent will restart. ``morpheus-node-ctl status`` will also show the agent status.

Windows
^^^^^^^

The |morpheus| Windows Agent service can be restarted in Administrative Tools -> Services.

.. TIP:: The |morpheus| Remote Console is not dependent on Agent communication and can be used to install or restart the |morpheus| agent on an Instance.

Uninstall |morpheus| Agent
--------------------------

Linux Agents
^^^^^^^^^^^^

You can use the following to uninstall the linux agent (contains commands for both rpm and deb agents)

.. code-block:: bash

  sudo rm /etc/apt/sources.list.d/morpheus.list \
  sudo morpheus-node-ctl kill \
  sudo apt-get -y purge morpheus-node \
  sudo apt-get -y purge morpheus-vm-node \
  sudo yum -y remove morpheus-node \
  sudo yum -y remove morpheus-vm-node \
  sudo yum clean all \
  sudo systemctl stop morpheus-node-runsvdir \
  sudo rm -f /etc/systemd/system/morpheus-node-runsvdir.service \
  sudo systemctl daemon-reload \
  sudo rm -rf /var/run/morpheus-node \
  sudo rm -rf /opt/morpheus-node \
  sudo rm -rf /etc/morpheus \
  sudo rm -rf /var/log/morpheus-node \
  sudo pkill runsv \
  sudo pkill runsvdir \
  sudo pkill morphd \
  sudo usermod -l morpheus-old morpheus-node \

Windows Agents
^^^^^^^^^^^^^^

.. code-block:: bash

  $app = Get-WmiObject -Class Win32_Product
                -Filter "Name = 'Morpheus Windows Agent'"
  $app.Uninstall()


CentOS/RHEL 7 Images
--------------------

For custom CentOS 7 images we highly recommend setting up Cloud-Init and fixing the network device names. More information for custom CentOS images can be found in the CentOS 7 image guide.
