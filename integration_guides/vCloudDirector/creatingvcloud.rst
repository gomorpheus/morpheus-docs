How to create vCloud Director templates for Morpheus
-----------------------------------------------------

To create a Windows template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new machine in VMware vCenter and install a base version of your preferred Windows build.

  1.  Apply any service packs / updates to the operating system.
  2.	Set the Network location to Private the below PowerShell will set the location.
    	- Get-NetConnectionProfile | Set-NetconnectionProfile -NetworkCategory private
  3.  Configure WinRM to allow remote management and open the firewall.
      - To do this, under local computer Administrator, open a command prompt and run ``winrm quickconfig``
  4.	Install VMware tools
  5.	Install .Net at least 4.5
  6.  Enable remote PowerShell this can be done in PowerShell.
      - Enable-PSremoting
  7.	Shutdown the virtual machine and convert to a template. (Do not run sysprep)


To create a Linux template
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new machine in VMware vCenter and install a base version of your preferred Linux distro build. If you are using cloud init as part of your image you will need to ensure your virtual machine has a cdrom.

  1.	Before installing the operating system setup a single ``ext`` or ``xfs`` partition without a swap disk (This is so that growpart can extend the disk. growpart currently does not support lvm)
  2.	Install the distro and apply any updates to the operating system and security updates
  3.	Install cloud-init
  4.	Install cloud-utils-growpart
  5.	Install vmware tools
  6.	Install git
  7.	epel-release (This is for centos only)
  8.	selinux set to permissive (enforced can cause problems with cloud-init)


We also recommend disabling network manager and setting the network adapter to eth0 rather than the automatically assigned name. https://support.morpheusdata.com/hc/en-us/articles/115002881228-Creating-a-CentOS-7-Morpheus-VMware-Image

To import your template into vCloud director you will need to login as either an administrator or organisation administrator.

Once logged into vCloud director you will then need select ``Manage Organizations`` and then select your organization.

From within the organisation click on ``Catalogues`` > select an existing catalogue or create a new catalogue.

.. note::
  Please note once you connect Morpheus to your vCD environment, it will create a catalogue called Auto Morpheus. This is a working catalogue and is ignored by Morpheus when searching for images, so any images in the catalogue will not be synced into Morpheus

Open the catalogue and select the import template from vCenter and then browse the data stores for your templates. Select your template and the type in a new name and description then check the copy template into vCloud director.

Once you click ok the import process will begin. When the import has completed the template will appear in Morpheus within ``Provisioning`` > ``Virtual Images``

If the image does not appear within the virtual images you may need to use the filters to filter the virtual images by the vmware ( vmdk / ovf / ova) type.

You may also need to refresh the cloud. To do this go to ``Infrastructure`` > ``Clouds``
>	select the vCloud Director cloud > select Refresh.
