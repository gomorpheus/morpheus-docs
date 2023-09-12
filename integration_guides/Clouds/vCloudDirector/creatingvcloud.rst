How to create vCloud Director templates for Morpheus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a Windows Template
`````````````````````````````

Create a new machine in VMware vCenter and install a base version of your preferred Windows build.

1.  Apply any service packs / updates to the operating system.
2.	Set the Network location to Private the below PowerShell will set the location.

    .. code-block:: PowerShell

      Get-NetConnectionProfile | Set-NetconnectionProfile -NetworkCategory private

3.  Configure WinRM to allow remote management and open the firewall.

    - To do this, under local computer Administrator, open a command prompt and run ``winrm quickconfig``

4.	Install VMware tools
5.	Install .Net at least 4.5
6.  Enable remote PowerShell this can be done in PowerShell.

    .. code-block:: PowerShell

      Enable-PSremoting

7.	Shutdown the virtual machine and convert to a template.

.. NOTE:: Do not run sysprep


To create a Linux Centos template
``````````````````````````````````

Create a new machine in VMware vCenter and install a base version of your preferred Linux distro build. If you are using cloud init as part of your image you will need to ensure your virtual machine has a cdrom.

#.	Before installing the operating system setup a single ``ext`` or ``xfs`` partition without a swap disk (This is so that growpart can extend the disk. growpart currently does not support lvm)
#.	Install the distro and apply any updates to the operating system and security updates
#.	Install cloud-init using command ``yum install cloud-init``
#.	Install cloud-utils-growpart using command ``yum install cloud-utils-growpart``
#.	Install vmware tools
#.	Install git by running ``yum install git``
#.	epel-release
#.	selinux set to permissive (enforced can cause problems with cloud-init)

To create a Linux Ubuntu template
``````````````````````````````````

Create a new machine in VMware vCenter and install a base version of your preferred Linux distro build. If you are using cloud init as part of your image you will need to ensure your virtual machine has a cdrom.

#.	Before installing the operating system setup a single ``ext`` partition without a swap disk (This is so that growpart can extend the disk. growpart currently does not support lvm)
#.	Install the distro and apply any updates to the operating system and security updates
#.	Ensure you have set a root password
#.	Install cloud-init by running ``sudo apt install cloud-init``
#.	Install cloud-utils-growpart ``sudo apt install cloud-utils``
#.	Install desired hypervisor drivers (Virto, Open-VM Tools)
#.	Install git by running ``sudo apt install git``
#.	As Debian 9 includes network manager ensure this is disabled. Change the below file

      .. code-block:: bash

        /etc/NetworkManager/NetworkManager.conf

 to the following:

      .. code-block:: bash

        managed=false



We also recommend disabling network manager and setting the network adapter to eth0 rather than the automatically assigned name. See a more detailed guide on VMware image prep `here <https://docs.morpheusdata.com/en/latest/integration_guides/Clouds/vmware/vmware_templates.html?highlight=vmware%20image%20prep#creating-a-centos-rhel-7-image>`_

To import your template into vCloud director you will need to login as either an administrator or organisation administrator.

Once logged into vCloud director you will then need select ``Manage Organizations`` and then select your organization.

From within the organisation click on ``Catalogues`` > select an existing catalogue or create a new catalogue.

.. note::
  Please note once you connect |morpheus| to your vCD environment, it will create a catalogue called Auto |morpheus|. This is a working catalogue and is ignored by |morpheus| when searching for images, so any images in the catalogue will not be synced into |morpheus|

Open the catalogue and select the import template from vCenter and then browse the data stores for your templates. Select your template and the type in a new name and description then check the copy template into vCloud director.

Once you click ok the import process will begin. When the import has completed the template will appear in |morpheus| within |LibVir|

If the image does not appear within the virtual images you may need to use the filters to filter the virtual images by the vmware ( vmdk / ovf / ova) type.

You may also need to refresh the cloud. To do this go to ``Infrastructure > Clouds``
>	select the vCloud Director cloud > select Refresh.
