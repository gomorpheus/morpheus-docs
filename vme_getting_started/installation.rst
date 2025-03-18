Installation
^^^^^^^^^^^^

Having completed a discussion of networking considerations in the previous section, let's now turn to OS installation on the |hosts|. The hosts are recommended to be HPE Proliant Gen 11 physical servers and must be running Ubuntu 22.04. Other OS types are planned for certification in the future but for now you must be running Ubuntu 22.04. The HPE VME hypervisor runs on top of the Ubuntu 22.04 hosts. We'll get to the installation portion in the next section but for now we will discuss the system requirements and recommendations for network and storage configuration during the installation.

.. image:: /images/vmeInstall/host-ubuntu-software.png
  :width: 30%

Host Requirements
`````````````````

- **Operating System:** `Ubuntu 22.04 <https://releases.ubuntu.com/jammy/>`_
- **Hardware:** HPE Proliant Gen 11 Hardware is recommended with additional hardware being tested and certified over time
- **CPU:** One or more 64-bit x86 CPUs, 1.5 GHz minimum with Intel VT or AMD-V enabled
- **Memory:** Minimum of 8GB for non-hyperconverged (HCI) deployments or 8GB plus 4GB for each data disk for HCI deployments
- **Storage:** Minimum of 50GB for operating system storage
- **Network:** 100 Mbps or faster NIC (10 Gbps recommended)
- **IP Addressing:** Static IP address
- **Internet Connectivity:** Internet access is required to download and install the required packages and dependencies

Ubuntu Network Setup
````````````````````

During the networking setup portion of the Ubuntu installation, with some network configurations you might have to create the initial bond for the management network in order to get initial connectivity. Bonds can be created from the Ubuntu deployment wizard itself and a discussion of different bond types and their potential usefulness within an effective |morpheus| networking scheme is described in greater detail in the previous section. In the screenshot below, the host is using a converged management and compute interface bond. The bond was created and a VLAN added to the bond. After creating the VLAN, an IP address was assigned at which the individual host can be managed. Thus, when setting up the cluster later, we can identify the ``bond0.2`` interface for host management traffic and ``bond0`` as the interface to send all compute traffic. Of course, this is a specific caveat that may not apply such as if you're not using converged networking (described in the previous section) or if DHCP is configured.

.. image:: /images/vmeInstall/ub-networking.png

Ubuntu Storage Setup
````````````````````

During the storage setup portion of the Ubuntu installation, keep in mind that Ubuntu won't utilize the entire disk by default when using LVM. You'll need to grow the disk. This guide won't discuss that process in complete detail but there are plenty of guides available on the Internet if they are needed.

.. image:: /images/vmeInstall/ub-storage.png

External Storage Setup
``````````````````````

Though it is possible to utilize local storage on the hosts, more commonly |clusters| will be configured to interface with external storage. Currently, only connecting to external storage over iSCSI is supported but support for Fibre Channel is also planned for the very near future. External storage provides a number of redundancy capabilities that aren't realized through local storage, such as automatic failover when a host is lost and migrating workloads to new hosts with zero downtime.

Configuring connections to external storage must be done on each host at the OS level. This is part of preparing the hosts for installation of the |morpheus| console and manager. This is done by going to the Ubuntu command line on each host and configuring the initiator to talk to the target. Once this is done and the disk is presented up to the OS, the groundwork is laid for configuring the datastore within |manager|. This process of creating a new datastore within the Manager UI is shown later in this guide following installation.

How the storage traffic is routed will depend on networking configuration. Having dedicated storage interfaces, as shown in the network examples from the previous section, is important for optimal throughput and resiliency. After establishing the datastore in the |manager| UI, this will ensure the operating system is utilizing those dedicated routes rather than through other interfaces that might be available.

Console Installation and Configuration
``````````````````````````````````````

It's time to begin the actual installation process on the hosts. From a high level, the process is as follows:

- Install Ubuntu 22.04
- Patch Ubuntu 22.04 with the latest updates and security fixes
- Install |morpheus| Console. This is a light Debian package that is used to configure the hosts and bootstrap initial virtualization capabilities. This is done on all hosts
- Configure the host system for networking, storage, NTP, etc
- Deploy the |manager| using the |morpheus| Console. This is done on only one host
- Launch the |manager| UI

.. image:: /images/vmeInstall/inst-process.png
  :width: 50%

.. IMPORTANT:: Compatibility with GFS2 datastores requires hardware enablement (HWE) packages to be installed. This is a set of software components that enables users to run a longterm support version of Ubuntu yet still use newer hardware that might not be supported by the default kernel. Run ``sudo apt install linux-generic-hwe-22.04`` to install HWE packages.

This guide won't go much deeper than what was already stated above regarding Ubuntu 22.04 installation and the process of applying the latest patches. We will pick up at this point with the process of installing the |morpheus| console which enables virtualization capability on cluster hosts by installing KVM, OVS, and other packages. This process is repeated on each host that will be part of the |cluster|. Continuing with this installation guide will require downloading packages from My HPE Software Center. If you are unable to log into the software center or if you believe you are missing software entitlements that should be present, contact your account representative.

Once logged into My HPE Software Center, click on the "Software" section from the side navigation.

.. image:: /images/vmeInstall/softwareCenter.png

Within the "Software" section, search for |software| amongst your other software entitlements. A "Product Info" type search for the term "hpe vm essentials" may work but depending on the entitlements present in the account and future changes to search functionality, a slightly different search might be required. Once HPE VM Essentials is successfully returned, click on the dropdown menu under "Action" and click on "Get License."

.. image:: /images/vmeInstall/getLicense.png

From the download page, you'll see software packages, signature files and license files. For a fresh installation, the ``.iso`` file is the primary download that you need. It contains a debian package and a QCOW2 image which will prep your hypervisor hosts and spin up your |manager| VM for the first time. Mark the box next to any files you wish to download and then click "Download." You do not need the separate debian packages offered outside of the ``.iso`` as those are only for upgrading a pre-installed |manager|.

.. image:: /images/vmeInstall/listFiles.png

.. NOTE:: Some commands listed in this installation guide will require superuser privileges.

Mount the ISO to your computer. The exact process will vary by software platform. On Linux, first select a temporary mount point (such as ``/mnt/iso``) or create a temporary mount point if it doesn't exist (``sudo mkdir /mnt/iso``). Next, mount the ISO to your temporary mount point (``sudo mount -o loop /path/to/file.iso /mnt/iso``). Take stock of the files by changing into the proper directory (``cd /mnt/iso``) and listing them out (``ls``).

Now that the packages are downloaded and the files contained in the ISO are accessible, copy them over to the hosts. You'll need to copy the ``.deb`` file over to each host but the QCOW image needs to only be copied to the host which will eventually run the |manager| VM. On Linux, this could be done with ``scp`` (``scp /path/to/file.deb username@hpevmhost_hostname_or_ip:/path/to/desired/location/``) but the copy process will be slightly different for other operating system platforms.

With the Debian package now available to the hosts, go ahead and install it with ``apt install -f hpe-vm.deb``. The "-f" option indicates that a file will be installed. Note that the Debian file name listed here is an example placeholder and the name of your downloaded file will likely be different. When asked if you wish to install all of the packages provided, confirm that you do and then wait for installation to complete. This process is installing on the host all of the packages needed to be part of a virtualization server, including KVM, Libvirt, Ceph, and more.

.. IMPORTANT:: The rest of this section describes the configuration process within the console for a specific network configuration. Your network configuration may be different and certainly interfaces and VLANs will be differently named. This is meant to illustrate the tools that are available within the console for performing various networking configurations. You may or may not need all of these steps and the specific configurations within these steps may be different in your environment.

With that, the |morpheus| console installation is complete. Enter the console with the following command: ``hpe-vm``.

.. image:: /images/vmeInstall/vme-console.png
  :width: 50%

First, enter the section for keyboard layouts and timezones. Set the time and make any changes to the keyboard layout, if needed.

.. image:: /images/vmeInstall/timezone.png
  :width: 50%

Next, enter the section for network configuration. The first thing that I've going to do is set the MTU for relevant interfaces to 9000 (jumbo frames). This has a number of benefits including improved efficiency, reduced latency, and optimization for storage networks. Open the "Device Type" dropdown and choose "vlan". In my example case, there's one VLAN which is the "bond0.2" VLAN shown in a prior section. Once selected, mark the box next to "mtu" and enter "9000" in the resulting box. Then, save changes.

.. image:: /images/vmeInstall/set-mtu-bond.png
  :width: 50%

Next, use the "Device Type" dropdown to once again select "ethernet" which you saw earlier before switching into the "vlan" section. Using the same process, I will also set the MTU to 9000 on both ethernet devices that make up my bond as well as on the bond itself. To get to the bond, you'd access the bond section from the "Device Type" dropdown in the same way that VLANs and ethernets were accessed. Now that I've set MTU of 9000 across the board, I'll go back to the ethernets section to work with my other two devices (the storage interfaces).

I'll continue this example by opening each of the two storage interfaces in turn. Three configurations I'll point out here are "addresses", "nameservers", and "mtu". In this case, I'll mark the box for "addresses" and provide an address in the pop-up modal that appears. I don't need to make any other configurations within that modal (lifetime, etc). A nameserver is not needed because the storage network are isolated and don't need to route out anywhere. Finally, I'm marking the box for "mtu" and setting the value at 9000 as I have with other interfaces. Next, tab over the DHCP section and disable DHCP for this interface. Save the changes and repeat the process for the other storage interface.

.. image:: /images/vmeInstall/set-mtu-storage.png
  :width: 50%

Once all of the necessary networking configurations are made, you'll want to save all changes. This will cause the changes to be applied and take us back to the main screen where we first accessed the timezone section and the networking configuration section. The console will show you that changes are being applied and will respond with a confirmation if they are successful.

.. image:: /images/vmeInstall/apply-changes.png
  :width: 50%

At this point, I am done configuring my example interfaces through the |morpheus| console. It does have some additional functionality not shown here which may be needed depending on your specific network configuration. Make sure to complete this process on all hosts before moving on to the next section which covers the installation of |manager| onto one of the prepared |hosts|.

Manager Installation
````````````````````

Having configured the |hosts| through the |morpheus| Console in the prior step, we'll now install |manager|. Unlike the console, the manager is only installed on one of the hosts and serves as the control plane for the server in addition to providing a provisioning engine, automation functionality, monitoring, secrets management, and a lot more. Before starting, make sure you've already downloaded the QCOW image for the manager and are aware of its full path on the host you've chosen to work from. In fact, it will be beneficial in the next step to go ahead and copy the full path into your paste buffer. The image is available in the HPE software center. Contact your account representative if you are unable to download it using the steps in the previous section.

Before you begin, the following information should be readily at hand:

- IP address to give to the |manager|
- URL for the web server
- DNS resolution for the URL (points the URL to the manager IP address)
- VLAN the manager should be deployed on
- Management interface name
- Compute interface name

To install the manager, go back into the console as we did in the previous step using the ``hpe-vm`` command. This time use the selection labeled "Install Morpheus". Morpheus was the original name for |manager|. Here we are given a modal containing some configuration options we must set in order to stand up |manager|.

.. image:: /images/vmeInstall/install-morph.png
  :width: 50%

Let's first paste in the path to the manager image since it's already in the paste buffer from a step earlier in this section. In the "Image URI" field, first type "file://" and then paste in the file path. Since the path begins with a leading "/" the final configuration value will look something like "file:///path/to/file.qcow2". After entering the URI, configure the following fields using the information mentioned previously you should have available for this step:

- IP Address
- Netmask
- Gateway
- DNS Server
- Appliance URL
- Hostname (same as the appliance URL without the FQDN)

.. NOTE:: Once a host is initially set up over SSH, communication to the |manager| is mostly handled through an outbound connection from an agent running on the host to the Manager VM. This makes the Appliance URL configuration very important. This is the HTTPS URL the agent will connect to from within each hypervisor host. The one exception are hypervisor console sessions which still go through SSH.

After filling in those fields, enter a username and password for an SSH user that can be used to get into the manager machine. Following that, if necessary, configure any proxy details.

The final configuration to make here involves specifying the size of the manager machine, either small, medium, or large. Each of the respective sizes consumes the following amount of resources:

- **Small:** 2 vCPUs and 12 GB RAM
- **Medium:** 4 vCPUs and 16 GB RAM
- **Large:** 4 vCPUs and 32 GB RAM

The greater the capacity, the greater amount of resources and cluster sizes the |manager| can manage. For large production environments, it's recommended you select a large manager. After selecting the size, you'll need to identify the management interface and (if using) the compute interface and compute VLAN tag. Following all of these configurations, select "Install".

.. image:: /images/vmeInstall/starting-services.png
  :width: 50%

At a certain phase in the install process, you'll see a message in the progress bar modal stating "Starting Morpheus Services...". At this point, you can direct a web browser to the appliance URL and see if you can access the appliance. If you get a response returned, even if it's just telling you the appliance is still loading, that's a good sign the web server is installed and things are working. Once all is well, you will arrive at a setup page which leads us into the next section on setting up |manager|.

Manager Initialization
``````````````````````

With |manager| up and running, you can now access the UI frontend by pointing your web browser to the appliance URL that you set in a previous step. You should see a registration screen like the one below.

.. image:: /images/vmeInstall/register.png

You'll need a license to go much further with the product. If you've followed this guide up to this point, you should already have your license key downloaded from My HPE Software Center. If not, you can log back in any time an re-download the file containing the license key. If you choose to skip entering a license key at this time, a short-term evaluation license will be applied. This can be upgraded to a full license at any time from the global settings section of the application.

The rest of the process involves naming the account on the manager and entering the details for your initial administrator user. Next, provide a name for the appliance, confirm the appliance URL is correct as entered, and choose from a few global enablements (for backups, monitoring, and logs).

.. image:: /images/vmeInstall/appliance-name.png

After clicking through to the next section, you will paste in your license key. Click "Complete Setup" and you will be dropped into the UI for the first time. Installation is now complete!

At this point, you are ready to move on to the next section which goes over the initial environmental setup steps that must be undertaken to add the first |cluster| to the |manager|.

Upgrading the Manager
`````````````````````

To upgrade the |manager|, you'll need to obtain the ``.deb`` upgrade package(s) from the HPE Software Center. Reach out to your account manager if you're unable to access the downloads as described in the next paragraphs. For an upgrade, you'll need the debian package (not the ISO, which is for first-time installation). If you are performing an offline upgrade, you will also need the "supplemental" debian package.

.. begin_download_packages

Once logged into My HPE Software Center, click on the "Software" section from the side navigation.

.. image:: /images/vmeInstall/softwareCenter.png

Within the "Software" section, search for |software| amongst your other software entitlements. A "Product Info" type search for the term "hpe vm essentials" may work but depending on the entitlements present in the account and future changes to search functionality, a slightly different search might be required. Once HPE VM Essentials is successfully returned, click on the dropdown menu under "Action" and click on "Get License."

.. image:: /images/vmeInstall/getLicense.png

From the download page, you'll see software packages, signature files and license files. Mark the checkbox next to any that you need and download them to your computer.

.. image:: /images/vmeInstall/listFiles.png

.. end_download_packages

.. begin_mount_iso

For an upgrade, we only need the ``.deb`` file available in the software center (and potentially the "supplemental" debian package as well if this will be an offline upgrade). To continue, copy the ``.deb`` file(s) over to the |cluster| host containing the |manager| VM. On Linux, this could be done with ``scp`` (``scp /path/to/file.deb username@hpevmhost_hostname_or_ip:/path/to/desired/location/``). Next, connect to the remote HPE VM host and confirm the VM name of the |manager| (``virsh list``). The host should already have ``virt-copy-in`` from the ``libvirt`` suite installed. Use it to copy the ``.deb`` file onto the VM file system: ``virt-copy-in -d <vm_name> /path/to/file.deb /path/to/remote/directory``.

With the ``.deb`` file in place, we need to open a console connection to the |manager| VM to perform the actual upgrade. There are a number of methods to accomplish this but below are two examples from either an HPE VM host or from your own computer.

.. begin_vm_console_connection

**From the HPE VM Host**

Confirm the manager VM name (``virsh list``) and connect with ``virsh console <vm name>``. This starts a local VNC serial connection. This method only works if the host has GUI capabilities installed, which means the host must be running Ubuntu Desktop or Ubuntu Server with GUI services installed.

**From another computer**

Confirm the manager VM name (run ``virsh list`` on the HPE VM host). Next, make note of the VNC port and password for the |manager| VM. This is done by running ``virsh edit <vm name>`` on the HPE VM host and finding it within the block beginning ``<graphics``. This block is typically near the bottom of the XML. Having obtained this information, move back over to your own computer (must be a computer with a desktop terminal, access to the VME host, and GUI capabilities). Connect to the SSH tunnel: ``ssh -L <VNC PORT>:127.0.0.1:<VNC PORT> <VME Host User>@<Host IP/hostname>``. Then, using a VNC viewer (for example, VNCViewer64), connect to ``localhost:<VNCPort>``. Use the password obtained from the VM XML viewed earlier.

.. end_vm_console_connection

Having copied over the needed files and connected to the |manager| VM, the upgrade is completed in just a few commands. These commands will stop the current services, install the package, and then reconfigure the Manager. Replace the placeholder ``.deb`` file in the commands below with the correct path and file name of the package you've copied over.

.. IMPORTANT:: Upgrading |manager| will result in downtime of at least a few minutes. Ensure users are not doing critical work during the upgrade window. This downtime applies only to the Manager itself and has no effect on the hypervisor host(s) or any provisioned VMs currently running.

.. code-block:: Bash

  sudo morpheus-ctl stop morpheus-ui
  sudo dpkg -i xxxx.deb
  sudo dpkg -i xxxx.supplemental.deb  # Optional -- Only for offline upgrades
  sudo morpheus-ctl reconfigure

All services will automatically start during the reconfigure process. After the reconfigure has succeeded, tail the UI service to watch UI startup logs with ``morpheus-ctl tail morpheus-ui``. Once the UI service is up and running, the upgrade process is complete. Attempt to reach your appliance normally through a web browser to confirm success.

.. NOTE:: Services will be stopped during package installation and started during the reconfigure process, including the ``morpheus-ui`` service. If the reconfigure process is interrupted or fails, the ``morpheus-ui`` service may need to be manually started or restarted. In certain situations if another service hangs on starting during reconfigure, run ``systemctl restart morpheus-runsvdir`` then reconfigure and restart ``morpheus-ui`` if successful.
