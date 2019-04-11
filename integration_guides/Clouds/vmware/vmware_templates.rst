Creating a |morpheus| VMware Image
-------------------------------------

Overview
^^^^^^^^^

|morpheus| comes out of the box with a default set of blueprints for use in many modern deployment scenarios. These consist mostly of base operating system images with a few additional adjustments. These adjustments typically include the addition of cloud-init (which is highly recommended to be used in most environments, but not mandatory). However, in many on-premise deployments there are custom image requirements as well as networking requirements. This guide will go over how to create a VMware Images for use within |morpheus|.

Creating a Windows Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Supported
^^^^^^^^^

2008R2,2012,2012R2,2016,2019

Steps
^^^^^^^^^

Create a new machine in VMware vCenter and install a base version of your preferred Windows build.  The smaller the VMDK drive, typically the faster you can clone and deploy.  Utilizing |morpheus|, provisioning and post deploy scripts can expand drives to desired sizing.

1.  Ensure VMtools is installed on the operating system.
2.  Apply any service packs / updates to the operating system.
3.  Configure WinRM to allow remote management and open the firewall. This is optional if using VMtools RPC mode for agent install and Morpheus Agent for guest exec.  To enable this, under local computer Administrator, open a command prompt and run 
    .. code-block:: PowerShell

      winrm quickconfig
      
4.	Install .Net at least 4.5
5.	Ensure Windows Firewall will allow WinRM connections.
6.  Shutdown the virtual machine and convert to a template.

.. NOTE:: Morpheus will sysprep images based on the "Enabled Sysprep?" flag under the Virtual Image's settings. Ensure a sysprep has not been performed on the template if this flag is enabled.



Creating a CentOS/RHEL Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Steps
^^^^^^^^^

Create a new machine in VMware vCenter and install a base version of your preferred Linux distro build. If you are using cloud init as part of your image you will need to ensure your virtual machine has a cdrom.

#.	Before installing the operating system setup a single ``ext`` or ``xfs`` partition without a swap disk (This is so that growpart can extend the disk. growpart currently does not support lvm)
#.	Install the distro and apply any updates to the operating system and security updates
#.	Install cloud-init using command ``yum install cloud-init``
#.	Install cloud-utils-growpart using command ``yum install cloud-utils-growpart``
#.	Install open-vm-tools using command ``yum install open-vm-tools``
#.	Install git by running ``yum install git``
#.	Install epel-release repo using command ``yum install epel-release``
#.	selinux set to permissive (enforced can cause problems with cloud-init) ``sudo vi /etc/selinux/config``


Cloud-Init
^^^^^^^^^^^

To get started with a base CentOS image we first install cloud-init. This is a relatively simple process using yum:

.. code-block:: bash

  yum -y install epel-release
  yum -y install git wget ntp curl cloud-init dracut-modules-growroot
  rpm -qa kernel | sed 's/^kernel-//'  | xargs -I {} dracut -f /boot/initramfs-{}.img {}

There are two parts to this yum installation. We are first ensuring some core dependencies are installed for automation as well as cloud-init. git for example is installed for use by ansible playbook automation down the line and is therefore optional if not using ansible. The dracut-modules-growroot is responsible for resizing the root partition upon first boot to match the virtual disk size that was potentially adjusted during provisioning.

A great benefit to using cloud-init is credentials don't have to be locked into the blueprint. It is advisable, within |morpheus| , to configure the default cloud-init user that gets created when the vm boots automatically by cloud-init. This is located in the `Administration -> Provisioning -> Cloud-Init` Settings section.

Network Interfaces
^^^^^^^^^^^^^^^^^^

A slightly annoying change with centOS 7 is that the network interfaces have changed naming convention. You may notice when running ifconfig that the primary network interface is set to something like ens2344 or some other random number. This naming is dynamic typically by hardware id and we don't want this to fluctuate when provisioning the blueprint in various VMware environments. Fortunately, there is a way to turn this functionality off and restore the interface back to eth0.

Firstly we need to adjust our bootloader to disable interface naming like this.

.. code-block:: bash

  sed -i -e 's/quiet/quiet net.ifnames=0 biosdevname=0/' /etc/default/grub
  grub2-mkconfig -o /boot/grub2/grub.cfg


The above command adds a few arguments to the kernel args list (namely ``net.ifnames=0`` and ``biosdevname=0``. It may be useful to view the ``/etc/default/grub`` file and ensure these settings were indeed applied.

The next step is to adjust the network-scripts in centOS. we need to ensure we have a file called ``/etc/sysconfig/network-scripts/ifcfg-eth0``

Below is a script that we run on our packer builds to prepare the machines network configuration files.

.. code-block:: bash

  export iface_file=$(basename "$(find /etc/sysconfig/network-scripts/ -name 'ifcfg*' -not -name 'ifcfg-lo' | head -n 1)")
  export iface_name=${iface_file:6}
  echo $iface_file
  echo $iface_name
  sudo mv /etc/sysconfig/network-scripts/$iface_file /etc/sysconfig/network-scripts/ifcfg-eth0
  sudo sed -i -e "s/$iface_name/eth0/" /etc/sysconfig/network-scripts/ifcfg-eth0
  sudo bash -c 'echo NM_CONTROLLED=\"no\" >> /etc/sysconfig/network-scripts/ifcfg-eth0'


This script tries to ensure there is a new ifcfg-eth0 config created to replace the old ens config file. Please do verify this config exists after running. If it does not you will have to be sure to build one on your own.

.. code-block:: bash

  TYPE=Ethernet
  DEVICE=eth0
  NAME=eth0
  ONBOOT=yes
  NM_CONTROLLED="no"
  BOOTPROTO="dhcp"
  DEFROUTE=yes


Gotyas
^^^^^^^

SELinux can cause issues with cloud-init when in enforced mode. It may be advisable to set this to permissive unless it is mandatory within your organization to use an enforced SELinux configuration. If that is the case please see the documentation for the cloud_init_t security policies.

Network Manager will also prevent the required restart of the Network Service when assigning static IP's. Disable Network Manager when possible or Static IP assignment may not work until the Network Service is restarted manually.

A Note on Proxies
^^^^^^^^^^^^^^^^^^

Proxy configurations are known to vary in some organizations and makes building a base blueprint a little more difficult. In order to fully configure proxies a few environment variables must be set in the `/etc/environment` file (This can be done automatically in a default user-data script for cloud-init as well in edit cloud).

.. code-block:: bash

  http_proxy="http://myproxyaddress:8080"
  https_proxy="http://myproxyaddress:8080"
  ftp_proxy="http://myproxyaddress:8080"
  no_proxy=127.0.0.1,localhost,applianceUrl
  https_no_proxy=127.0.0.1,localhost,applianceUrl


.. IMPORTANT:: It is very important to properly set the no_proxy list (applianceUrl) should be replaced with the actual appliance url. In future releases, morpheus plans to automatically take care of this.

.. NOTE:: If using cloud-init agent install mode these settings need to be set in the custom Cloud-Init User data section of “Edit Cloud” or “Edit Virtual Image”

.. IMPORTANT:: If using this virtual machine as a docker host, proxy settings must also be configured in the docker config. See Docker guides for instructions on how to properly set this. If necessary this can be wrapped in a task automation workflow for your own use.

To create an Ubuntu Image
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



We also recommend disabling network manager and setting the network adapter to eth0 rather than the automatically assigned name as described in the CentOS/RHEL section above.
