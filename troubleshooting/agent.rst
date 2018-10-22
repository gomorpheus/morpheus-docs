|morpheus| Agent Install Troubleshooting
========================================

When provisioning an instance, there are some network and configuration requirements to successfully install the morpheus agent.  Typically when a vm instance is still in the provisioning phase long after the vm is up, the instance is unable to reach |morpheus| , or depending on agent install mode, |morpheus| is unable to reach the instance.

The most common reason an agent install fails is the provisioned instance cannot reach the |morpheus| Appliance via the appliance_url set in Admin -> Settings over both 443 and 80. When an instance is provisioned from |morpheus|, it must be able to reach the |morpheus| appliance via the appliance_url or the agent will not be installed.

.. image:: /images/agent-7c9a2.png

In addition to the main appliance_url in Admin -> Settings, additional appliance_urls can be set per cloud in the Advanced options of the cloud configuration pane when creating or editing a cloud. When this field is populated, it will override the main appliance url for anything provisioned into that cloud.

.. TIP:: The |morpheus| UI current log, located at /var/log/morpheus/morpheus-ui/current, is very helpful when troubleshooting agent installations.

Agent Install Modes
-------------------

There are 3 Agent install modes:

- ssh/winrm
- VMware Tools
- cloud-init

For All Agent Install modes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an instance is provisioned and the agent does not install, verify the following for any agent install mode:

* The |morpheus| appliance_url (Admin -> Settings) is both reachable and resolvable from the provisioned node.
* The appliance_url begins with to https://, not http://.

.. NOTE:: Be sure to use https:// even when using an ip address for the appliance.

* Inbound connectivity access to the |morpheus| Appliance from provisioned VM's and container hosts on port 443 (needed for agent communication)

* Private (non-morpheus provided) vm images/templates must have their credentials entered. These can be entered/edited in the Provisioning - Virtual Images section but clicking the Actions dropdown of an image and selecting Edit.

.. NOTE:: Administrator user is required for Windows agent install.

* The instance does not have an IP address assigned. For scenarios without a dhcp server, static IP information must be entered by selecting the Network Type: Static in the Advanced section during provisioning. IP Pools can also be created in the Infrastructure -> Networks -> IP Pools section and added to clouds network sections for IPAM.

* DNS is not configured and the node cannot resolve the appliance. If dns cannot be configure, the ip address of the |morpheus| appliance can be used as the main or cloud appliance.

SSH/Winrm
^^^^^^^^^

Linux Agent
```````````

* Port 22 is open for Linux images, and ssh is enabled
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the Provisioning -> Virtual Images section.

Windows Agent
`````````````

* Port 5985 must be open and winRM enabled for Windows images.
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the Provisioning -> Virtual Images section.

.. NOTE:: Administrator user is required for Windows agent install.

VMware tools (vmtools) rpc mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* VMware tools is installed on the template(s)
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the Provisioning -> Virtual Images section.

Cloud-Init agent install mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Cloud-Init is configured in Admin -> Provisioning section
* Provisioned image/blueprint has Cloud-Init (linux) or Cloudbase-Init (windows) installed

Manually Installing a |morpheus| Agent
--------------------------------------

While it should not be necessary to manually install an agent if the requirements are met, it is possible to manually install an agent on an instance. This can also be handy when troubleshooting an agent install.

Linux
^^^^^

#. In |morpheus| , go to the VM's host detail page in Infrastructure->Hosts->Virtual Machines you will see an API Key that is unique to that host.

#. As root user, run: (replacing ${} with the relevant information)

   .. code-block:: bash

    curl -k -s "${opts.applianceUrl}api/server-script/agentInstall?apiKey=${opts.apiKey}" | bash

#. This will pull the |morpheus| Agent install script from the |morpheus| appliance and run it.

#. Once the agent is installed, run morpheus-node-ctl reconfigure to complete the manual process.

Windows

* The windows agent setup can be downloaded at ``https://[morpheus-applaince-url]/msi/morpheus-agent/MorpheusAgentSetup.msi``

* On the |morpheus| appliance package the windows agent is located at ``/var/opt/morpheus/package-repos/msi/morpheus-agent``

* WinRM, VMware Tools, or Cloudbase-Init can be used to install the agent from the |morpheus| appliance

* The initial windows installer is MorpheusAgentSetup.msi

* Once the Windows agent is downloaded and installed with |morpheus| AgentSetup.msi the agent is located and runs from `/Program Files x86/Morphues/|morpheus| Windows Agent`

* Logs can be viewed in the Event Viewer under Applications and Services Logs  -> |morpheus| Windows Agent

#. Replace the values for $apiKey and $applianceUrl in the script below.

#. Execute this script on the Windows box in Powershell.

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

#. If the agent doesn't install, logs can be found in the morpheus_install.log file located at ``C:\Program Files (x86)\Common Files\``

Restarting the |morpheus| Agent
--------------------------------

In some situations is may necessary to restart the morpheus agent on the host to re-sync communication from the agent to the |morpheus| appliance.

Linux
^^^^^

On the target host, run ``sudo morpheus-node-ctl restart morphd`` and the |morpheus| agent will restart. ``morpheus-node-ctl status`` will also show the agent status.

Windows
^^^^^^^

The |morpheus| Windows Agent service can be restarted in Administrative Tools -> Services.

.. TIP:: The |morpheus| Remote Console is not dependent on agent communication and can be used to install or restart the |morpheus| agent on an instance.

Uninstall |morpheus| Agent

You can use the following to uninstall the linux agent:

.. code-block:: bash

  sudo rm /etc/apt/sources.list.d/morpheus.list
  sudo morpheus-node-ctl stop rsyslogd
  sudo apt-get -y purge morpheus-vm-node
  sudo rm -rf /opt/morpheus-node
  sudo usermod -l morpheus-old morpheus-node
  sudo killall runsv
  sudo killall runsvdir
  sudo killall morphd

centOS/RHEL 7 Images
--------------------

For custom centOS 7 images we highly recommend setting up cloud-init and fixing the network device names. More information for custom centOS images can be found in the centOS 7 image guide.
