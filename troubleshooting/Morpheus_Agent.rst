|morpheus| Agent Install Troubleshooting
========================================

When provisioning an Instance, there are network and configuration requirements to consider in order to successfully install the |morpheus| Agent. Typically, when a VM Instance is still in the provisioning phase long after the VM is up, the Instance is unable to reach |morpheus|. Depending on the Agent install mode, it could also mean |morpheus| is unable to reach the Instance.

The most common reason an Agent install fails is the provisioned Instance cannot reach the |morpheus| Appliance via the Appliance URL set in Administration > Settings over port 443. When an Instance is provisioned from |morpheus|, it must be able to reach the |morpheus| appliance via the Appliance URL or the Agent will not be installed.

.. image:: /images/agent-7c9a2.png

In addition to the main Appliance URL in Administration > Settings, additional Appliance URLs can be set per Cloud in the Advanced Options section of the Cloud configuration modal when creating or editing a Cloud. When this field is populated, it will override the main Appliance URL for anything provisioned into that Cloud.

.. TIP:: The |morpheus| UI current log, located at /var/log/morpheus/morpheus-ui/current, is very helpful when troubleshooting Agent installations.

Agent Install Modes
-------------------

There are 3 Agent install modes:

- SSH/WinRM
- VMware Tools
- Cloud-Init

For All Agent Install modes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an Instance is provisioned and the Agent does not install, verify the following for any Agent install mode:

* The |morpheus| Appliance URL (Administration > Settings) is both reachable and resolvable from the provisioned node
* The Appliance URL begins with https://, not http://

.. NOTE:: Be sure to use https:// even when using an IP address for the appliance.

* Inbound connectivity access to the |morpheus| appliance from provisioned VMs and container hosts on port 443 (needed for Agent communication)

* Private (non-|morpheus| provided) VM images and templates must have their credentials stored. These can be entered or edited in the Provisioning > Virtual Images section by clicking the Actions dropdown on an imaged detail page and selecting Edit.

.. NOTE:: Administrator user is required for Windows Agent install.

* The Instance does not have an IP address assigned. For scenarios without a DHCP server, static IP information must be entered by selecting the Network Type: Static in the Advanced Options section during provisioning. IP Pools can also be created in the Infrastructure > Networks > IP Pools section and added to Cloud network sections for IPAM

* DNS is not configured and the node cannot resolve the appliance. If DNS cannot be configured, the IP address of the |morpheus| appliance can be used as the main or Cloud appliance

SSH/WinRM
^^^^^^^^^

Linux Agent
```````````

* Port 22 is open for Linux images, and SSH is enabled

* Credentials have been stored on the image if using a custom or synced image. Credentials can be entered on images in the Provisioning > Virtual Images section

Windows Agent
`````````````

* Port 5985 must be open and WinRM enabled for Windows images

* Credentials have been entered on the image if using a custom or synced image. Credentials can be entered on images in the Provisioning > Virtual Images section

.. NOTE:: Administrator user is required for Windows Agent install.

VMware Tools (vmtools) RPC mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* VMware Tools is installed on the template(s)

* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the Provisioning > Virtual Images section

Cloud-Init Agent Install Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Cloud-Init is configured in Administration > Provisioning section

* Provisioned Image or Blueprint has Cloud-Init (Linux) or Cloudbase-Init (Windows) installed

Manually Installing |morpheus| Agent
------------------------------------

While it should not be necessary to manually install an Agent, if the requirements are met, it is possible to manually install the Agent on an Instance. This can also be handy when troubleshooting an Agent install.

Linux
^^^^^

#. In |morpheus|, go to the VM's Host detail page in Infrastructure > Hosts > Virtual Machines you will see an API key that is unique to the Host

#. As root user, run: (replacing ${} with the relevant information)

   .. code-block:: bash

    curl -k -s "${opts.applianceUrl}/api/server-script/agentInstall?apiKey=${opts.apiKey}" | bash

#. This will pull the |morpheus| Agent install script from the |morpheus| appliance and run it

#. Once the Agent is installed, run ``morpheus-node-ctl reconfigure`` to complete the manual process

Windows

* The windows Agent setup can be downloaded at ``https://[morpheus-applaince-url]/msi/morpheus-agent/MorpheusAgentSetup.msi``

* On the |morpheus| appliance package, the windows Agent is located at ``/var/opt/morpheus/package-repos/msi/morpheus-agent``

* WinRM, VMware Tools, or Cloudbase-Init can be used to install the agent from the |morpheus| appliance

* The initial Windows installer is MorpheusAgentSetup.msi

* Once the Windows agent is downloaded and installed with |morpheus| AgentSetup.msi, the Agent is located and runs from ``/Program Files x86/morpheus/morpheus Windows Agent``

* Logs can be viewed in the Event Viewer under Applications and Services Logs -> |morpheus| Windows Agent

#. Replace the values for ``$apiKey`` and ``$applianceUrl`` in the script below

#. Execute this script on the Windows box in Powershell:

   .. code-block:: bash

       $apiKey = "add VM apiKey here"
       $applianceUrl = "https://your_appliance_url.com/"

       $client = New-Object System.Net.WebClient
       $client.DownloadFile($applianceUrl + "/msi/morpheus-agent/MorpheusAgentSetup.msi", "C:\Program Files (x86)\Common Files\MorpheusAgentSetup.msi")
       Start-Sleep -Seconds 10
       cd ${env:commonprogramfiles(x86)}
       $serviceName = "Morpheus Windows Agent"
       if(Get-Service $serviceName -ErrorAction SilentlyContinue) {
       Stop-Service -displayname $serviceName -ErrorAction SilentlyContinue
       Stop-Process -Force -processname Morpheus* -ErrorAction SilentlyContinue
       Stop-Process -Force -processname Morpheus* -ErrorAction SilentlyContinue
       Start-Sleep -s 5
       $serviceId = (get-wmiobject Win32_Product -Filter "Name = 'Morpheus Windows Agent'" | Format-Wide -Property IdentifyingNumber | Out-String).Trim()
       cmd.exe /c "msiexec /x $serviceId /q"
       }
       [Console]::Out.Flush()
       [gc]::collect()
       try {
       Write-VolumeCache C
       }
       Catch {
       }
       $MSIArguments= @(
       "/i"
       "MorpheusAgentSetup.msi"
       "/qn"
       "/norestart"
       "/l*v"
       "morpheus_install.log"
       "apiKey=$apiKey"
       "host=$applianceUrl"
       "username=`".\LocalSystem`""
       "vmMode=`"true`""
       "logLevel=`"1`""
       )
       $installResults = Start-Process msiexec.exe -Verb runAs -Wait -ArgumentList $MSIArguments
       [Console]::Out.Flush()
       [gc]::collect()
       try {
       Write-VolumeCache C
       }
       Catch {
       }
       start-sleep -s 10
       $attempts = 0
       Do {
       try {
               Get-Service $serviceName -ea silentlycontinue -ErrorVariable err
               if([string]::isNullOrEmpty($err)) {
                       Break
               } else {
                       start-sleep -s 10
                       $attempts++
               }
       }
       Catch {
               start-sleep -s 10
               $attempts++
       }
       }
       While ($attempts -ne 6)
       Set-Service $serviceName -startuptype "automatic"
       $service = Get-WmiObject -Class Win32_Service -Filter "Name='$serviceName'"
       if ($service -And $service.State -ne "Running") {Restart-Service -displayname $serviceName}
       exit $installResults.ExitCode

#. If the Agent doesn't install, logs can be found in the morpheus_install.log file located at ``C:\Program Files (x86)\Common Files\``

Restarting the |morpheus| Agent
--------------------------------

In some situations, it may necessary to restart the |morpheus| Agent on the host to re-sync communication from the Agent to the |morpheus| appliance.

Linux
^^^^^

On the target host, run ``sudo morpheus-node-ctl restart morphd`` and the |morpheus| agent will restart. ``morpheus-node-ctl status`` will also show the agent status.

Windows
^^^^^^^

The |morpheus| Windows Agent service can be restarted in Administrative Tools -> Services.

.. TIP:: The |morpheus| Remote Console is not dependent on Agent communication and can be used to install or restart the |morpheus| agent on an Instance.

Uninstall |morpheus| Agent
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the following to uninstall the linux agent:

.. code-block:: bash

  sudo rm /etc/apt/sources.list.d/morpheus.list
  sudo morpheus-node-ctl kill
  sudo apt-get -y purge morpheus-node
  sudo apt-get -y purge morpheus-vm-node
  sudo systemctl stop morpheus-node-runsvdir
  sudo rm -f /etc/systemd/system/morpheus-node-runsvdir.service
  sudo systemctl daemon-reload
  sudo rm -rf /var/run/morpheus-node
  sudo rm -rf /opt/morpheus-node
  sudo rm -rf /etc/morpheus/
  sudo rm -rf /var/log/morpheus-node
  sudo pkill runsv
  sudo pkill runsvdir
  sudo pkill morphd
  sudo usermod -l morpheus-old morpheus-node

CentOS/RHEL 7 Images
--------------------

For custom CentOS 7 images we highly recommend setting up Cloud-Init and fixing the network device names. More information for custom CentOS images can be found in the CentOS 7 image guide.
