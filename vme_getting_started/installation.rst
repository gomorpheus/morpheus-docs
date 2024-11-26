Installation
^^^^^^^^^^^^

Having completed a discussion of networking considerations in the previous section, let's now turn to OS installation on the |hosts|. The hosts are recommended to be HPE Proliant Gen 11 physical servers and must be running Ubuntu 22.04. Other OS types are planned for certification in the future but for now you must be running Ubuntu 22.04. The HPE VME hypervisor runs on top of the Ubuntu 22.04 hosts. We'll get to the installation portion in the next section but for now we will discuss the system requirements and recommendations for network and storage configuration during the installation.

IMAGE of host-ubuntu-software stack

Host Requirements
`````````````````

- **Operating System:** Ubuntu 22.04
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

IMAGE

Ubuntu Storage Setup
````````````````````

During the storage setup portion of the Ubuntu installation, keep in mind that Ubuntu won't utilize the entire disk by default when using LVM. You'll need to grow the disk. This guide won't discuss that process in complete detail but there are plenty of guides available on the Internet if they are needed.

IMAGE

Console Installation and Configuration
``````````````````````````````````````

It's time to begin the actual installation process on the hosts. From a high level, the process is as follows:

- Install Ubuntu 22.04
- Patch Ubuntu 22.04 with the latest updates and security fixes
- Install |morpheus| Console. This is a light Debian package that is used to configure the hosts and bootstrap initial virtualization capabilities. This is done on all hosts
- Configure the host system for networking, storage, NTP, etc
- Deploy the |manager| using the |morpheus| Console. This is done on only one host
- Launch the |manager| UI

IMAGE - Installation process graphic

.. NOTE:: Compatibility of some hardware with |morpheus| requires hardware enablement (HWE) packages to be installed. This is a set of software components that enables users to run a longterm support version of Ubuntu yet still use newer hardware that might not be supported by the default kernel. Run ``sudo apt install linux-generic-hwe-20.04`` to install HWE packages.

This guide won't go much deeper than what was already stated above regarding Ubuntu 22.04 installation and the process of applying the latest patches. We will pick up at this point with the process of installing the |morpheus| console which enables virtualization capability on cluster hosts by installing KVM, OVS, and other packages. This process is repeated on each host that will be part of the |cluster|. Before you begin, make sure you've downloaded the Debian package from the HPE software center or contact your account representative if you're unsure about how to access it.

.. NOTE:: Some commands listed in this installation guide will require superuser privileges.

With the Debian package downloaded, go ahead and install it with ``apt install -f hpe-vm.deb``. The "-f" option indicates that a file will be installed. Note that the Debian file name listed here is an example placeholder and the name of your downloaded file will likely be different. When asked if you wish to install all of the packages provided, confirm that you do and then wait for installation to complete. This process is installing on the host all of the packages needed to be part of a virtualization server, including KVM, Libvirt, Ceph, and more.

.. IMPORTANT:: The rest of this section describes the configuration process within the console for a specific network configuration. Your network configuration may be different and certainly interfaces and VLANs will be differently named. This is meant to illustrate the tools that are available within the console for performing various networking configurations. You may or may not need all of these steps and the specific configurations within these steps may be different in your environment.

With that, the |morpheus| console installation is complete. Enter the console with the following command: ``hpe-vm``.

IMAGE - the HPE VM console

First, enter the section for keyboard layouts and timezones. Set the time and make any changes to the keyboard layout, if needed.

IMAGE - timezone

Next, enter the section for network configuration. The first thing that I've going to do is set the MTU for relevant interfaces to 9000 (jumbo frames). This has a number of benefits including improved efficiency, reduced latency, and optimization for storage networks. Open the "Device Type" dropdown and choose "vlan". In my example case, there's one VLAN which is the "bond0.2" VLAN shown in a prior section. Once selected, mark the box next to "mtu" and enter "9000" in the resulting box. Then, save changes.

IMAGE - setting MTU

Next, use the "Device Type" dropdown to once again select "ethernet" which you saw earlier before switching into the "vlan" section. Using the same process, I will also set the MTU to 9000 on both ethernet devices that make up my bond as well as on the bond itself. To get to the bond, you'd access the bond section from the "Device Type" dropdown in the same way that VLANs and ethernets were accessed. Now that I've set MTU of 9000 across the board, I'll go back to the ethernets section to work with my other two devices (the storage interfaces).

I'll continue this example by opening each of the two storage interfaces in turn. Three configurations I'll point out here are "addresses", "nameservers", and "mtu". In this case, I'll mark the box for "addresses" and provide an address in the pop-up modal that appears. I don't need to make any other configurations within that modal (lifetime, etc). A nameserver is not needed because the storage network are isolated and don't need to route out anywhere. Finally, I'm marking the box for "mtu" and setting the value at 9000 as I have with other interfaces. Next, tab over the DHCP section and disable DHCP for this interface. Save the changes and repeat the process for the other storage interface.

IMAGE - the storage interface settings

Once all of the necessary networking configurations are made, you'll want to save all changes. This will cause the changes to be applied and take us back to the main screen where we first accessed the timezone section and the networking configuration section. The console will show you that changes are being applied and will respond with a confirmation if they are successful.

IMAGE - saving changes

At this point, I am done configuring my example interfaces through the |morpheus| console. It does have some additional functionality not shown here which may be needed depending on your specific network configuration. Make sure to complete this process on all hosts before moving on to the next section which covers the installation of |manager| onto the prepared |hosts|.

Manager Installation
````````````````````

Having configured the |hosts| through the |morpheus| Console in the prior step, we'll now install |manager|. Unlike the console, the manager is only installed on one of the hosts and serves as the control plane for the server in addition to providing a provisioning engine, automation functionality, monitoring, secrets management, and a lot more. Before starting, make sure you've already downloaded the QCOW image for the manager and are aware of its full path on the host you've chosen to work from. In fact, it will be beneficial in the next step to go ahead and copy the full path into your paste buffer. The image is available in the HPE software center. Contact your account representative if you're unsure about how or where to access it.

Before you begin, the following information should be readily at hand:

- IP address to give to the |manager|
- URL for the web server
- DNS resolution for the URL (points the URL to the manager IP address)
- VLAN the manager should be deployed on
- Management interface name
- Compute interface name

To install the manager, go back into the console as we did in the previous step using the ``hpe-vm`` command. This time use the selection labeled "Install Morpheus". Morpheus was the original name for |manager|. Here we are given a modal containing some configuration options we must set in order to stand up |manager|.

IMAGE - The manager screen

Let's first paste in the path to the manager image since it's already in the paste buffer from a step earlier in this section. In the "Image URI" field, first type "file://" and then paste in the file path. Since the path begins with a leading "/" the final configuration value will look something like "file:///path/to/file.qcow2". After entering the URI, configure the following fields using the information mentioned previously you should have available for this step:

- IP Address
- Netmask
- Gateway
- DNS Server
- Appliance URL
- Hostname (same as the appliance URL without the FQDN)

After filling in those fields, enter a username and password for an SSH user that can be used to get into the manager machine. Following that, if necessary, configure any proxy details.

The final configuration to make here involves specifying the size of the manager machine, either small, medium, or large. Each of the respective sizes consumes the following amount of resources:

- **Small:** 2 vCPUs and 12 GB RAM
- **Medium:** 4 vCPUs and 16 GB RAM
- **Large:** 4 vCPUs and 32 GB RAM

The greater the capacity, the greater amount of resources and cluster sizes the |manager| can manage. For large production environments, it's recommended you select a large manager. After selecting the size, you'll need to identify the management interface and (if using) the compute interface and compute VLAN tag. Following all of these configurations, select "Install".

IMAGE - install progress bar

At a certain phase in the install process, you'll see a message in the progress bar modal stating "Starting Morpheus Services...". At this point, you can direct a web browser to the appliance URL and see if you can access the appliance. If you get a response returned, even if it's just telling you the appliance is still loading, that's a good sign the web server is installed and things are working. Once all is well, you will arrive at a setup page which leads us into the next section on setting up |manager|.

Manager Initialization
``````````````````````
