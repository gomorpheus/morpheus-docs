Boot
====

.. add images menu info

Overview
--------

|morpheus| provides a simple-to-use Bare Metal boot capability based on PXE. When a server boots and is redirected to the |morpheus| server for the installation files, they can be configured to be simply passed an OS or Hypervisor (in which case |morpheus| will see them as Bare Metal servers with no further detail) or they can be brought on as Virtual Machines or Docker Hosts. Installation of the |morpheus| Agent can also be done during the initial configuration stage.

Prerequisites
-------------

In order to work with |morpheus| bare metal PXE boot capabilities, some initial setup configuration is required. First, on the |morpheus| server, if you have a firewall enabled, make sure port 69 is open for TFTP. |morpheus| actually uses port 6969 and during installation a redirect should have been set. To check this, SSH onto the Morpheus server and run the following:

.. code-block:: bash

  iptables -t nat -L -n -v

If the redirect is still properly, the response should include the following:

.. code-block:: bash

  Chain PREROUTING (policy ACCEPT 69 packets, 9767 bytes)

  pkts bytes target   prot opt in out source     destination

  0     0 REDIRECT udp  --  *  *   0.0.0.0/0  0.0.0.0/0        udp dpt:69 redir ports 6969

  0     0 DNAT     tcp  --  *  *   0.0.0.0/0  169.254.169.254  tcp dpt:80 to:192.168.1.156

Next, in |morpheus|, set a default PXE root password. This password is set in |AdmSetPro|. With the default root password set, set up the redirect on the DHCP server. In addition to the DNS and Gateway settings, add Boot Server Host Name which will be the name of the |morpheus| Server and Bootfile Name which should be set to ``pxelinux.0``. If you are using a Linux-based DHCP server, for example on CentOS, the dhcpd.conf configuration will look something like the following:

.. code-block:: bash

    allow booting;
    allow bootp;
    option option-128 code 128 = string;
    option option-129 code 129 = text;
    next-server xx.xx.xx.xx;
    filename "pxelinux.0";

.. NOTE:: Replace the dummy IP address in the example dhcpd.conf file above with your |morpheus| appliance IP address.

Once you have done this, when you boot a PXE-enabled machine on the network, it will be told to access the |morpheus| server and request the ``pxelinux.0`` file. It will do this on port 69, the default for TFTP and will be redirected to 6969 once it hits the |morpheus| server. If successful you will see the "|morpheus| PXE Server" menu when you boot a server. This is the default menu defined in |morpheus| and supports the shipped PXE images supplied with the product. By selecting any of the choices from the "|morpheus| PXE Server menu", the install files should be downloaded and the server configured as per the supplied kickstart files. At this point, back on the |morpheus| appliance, you should see the MAC address for the new server appear in the "Discovered MAC Addresses" tab of the |InfBoo| page.

Troubleshooting
---------------

If you do not get the Morpheus boot menu, there are a few things to check:

* First, make sure the filename is correct. It must be ``pxelinux.0``
* Next, check the TFTP server is responding by using a TFTP client to get the ``pxelinux.0`` file from the |morpheus| server using the same host name as you have configured in the DHCP server configuration. Do this test on a machine on the same network as the machines you are trying to boot using PXE
* Leave the port number as 69 (the default) as this will also check the redirect is working
* If a GET call on the default port does not work, and the client allows (most do) try using port 6969. If this works, then the redirect is wrong
* If it will not work on either, check you can access the |morpheus| server from the network you are on and also check there are no firewalls between the test network and the |morpheus| Server 

Mapping
-------

Add Mapping
^^^^^^^^^^^

#. Select the Mapping tab then click the Add Mapping button.
#. From the New Mapping Wizard input the following information:

   Match Pattern
    Mac address separated by ':' or an ip address filter
   Description(optional)
    Description of the new mapping.
   Active
    Flag to denote the mapping as active or disabled.
   Operating System
    List of operating systems for the mapping.
   Boot Image
    Lists available PXE boot images.
   Answer File
    Lists available answer files.
   Cloud
    Lists the available clouds.
   Server Mode
    List of server modes:: unmanaged, Managed, Bare metal host, Container host, VM host, and Container & VM host.

#. Save

Once the mapping is added, and the target host is powered on, the {morpheus} PXE menu will load and PXE boot will start.

Edit Mapping
^^^^^^^^^^^^

#. Click the edit icon on the row of the mapping you wish to edit.
#. Modify information as needed.
#. Click the Save Changes button to save.

Delete Mapping

#. Click the delete icon on the row of the mapping you wish to delete.

Boot Menus
----------

System-seeded Boot Menus are displayed and user-created Boot Menus can be edited and deleted. User-created Boot Menus are edited or deleted by clicking on the pencil or trash can icon in the appropriate row.

Adding a Boot Menu
^^^^^^^^^^^^^^^^^^

To begin, click :guilabel:`+ ADD`. Available fields include:

- NAME: Name of the Boot Menu
- DESCRIPTION: Description of the Boot Menu
- TYPE: Select between **bios, uefi, ipxe and grub**
- ENABLED: Determines if the Boot Menu is active
- DEFAULT MENU
- ROOT MENU
- MENU NAME
- BOOT IMAGE
- ANSWER FILE
- MENU CONTENT
- SUB MENUS

Click :guilabel:`SAVE CHANGES`

Answer Files
------------

Answer files are like lists of answers for questions that you know the setup program is going to ask but the user is not prepared to answer. They contain one or more sections, and each section contains one or more properties in the form name=value. Morpheus provides Answer Files for ESXi, CentOS, Ubuntu and XenServer, and user can add their own.

Add Answer Files
^^^^^^^^^^^^^^^^

#. Click the Infrastructure link in the navigation bar.
#. Click the Boot link in the sub navigation bar
#. Select the Answer Files tab then click the Add Answer File button.
#. From the New Answer File Wizard input the following information

   Name
    Name of the answer file.
   Description(optional)
    Description of the new answer file.
   Active
    Flag to denote the mapping as active or disabled.
   Script Name
    Name of the new answer file.
   Script Version
    Version of the new answer file.
   Script
    The script for the new answer file.

#. Save

Edit Answer File
^^^^^^^^^^^^^^^^

#. Click the Infrastructure link in the navigation bar.
#. Click the Boot link in the sub navigation bar
#. Select the Answer Files tab
#. Click the edit icon on the row of the answer file you wish to edit.
#. Modify information as needed.
#. Save Changes

Delete Answer File
^^^^^^^^^^^^^^^^^^

#. Click the Infrastructure link in the navigation bar.
#. Click the Boot link in the sub navigation bar
#. Select the Answer Files tab.
#. Click the delete icon on the row of the answer file you wish to delete.

Images
------

Morpheus provides Images for ESXi, CentOS, Ubuntu and XenServer, and user can add their own Images.

Add Images
^^^^^^^^^^

#. Click the Infrastructure link in the navigation bar.
#. Click the Boot link in the sub navigation bar
#. Select the Images tab then click the Add Image button.
#. From the Upload Virtual Image Wizard input the following information

   Name
    Name of the Image.
   Operating System
    List of available operating systems.
   Storage Provider
    List of available storage providers.
   Image Path
    Path of the image.
   Visibility
    Private or Public
   Account
    List of accounts to allow permission to this image.

#. Save Changes

Edit Image
^^^^^^^^^^

#. Click the Infrastructure link in the navigation bar.
#. Click the Boot link in the sub navigation bar
#. Select the Images tab
#. Click the actions drop down and select edit.
#. Modify information as needed.
#. Click the Save Changes button to save.

Convert Image
^^^^^^^^^^^^^

#. Click the Infrastructure link in the navigation bar.
#. Click the Boot link in the sub navigation bar.
#. Select the Images tab
#. Click the `Actions` drop and select `Convert`.

Download Image
^^^^^^^^^^^^^^

#. Click the Infrastructure link in the navigation bar.
#. Click the Boot link in the sub navigation bar.
#. Select the Images tab
#. Click the `Actions` drop and select `Download`.

Remove Image
^^^^^^^^^^^^

#. Click the Infrastructure link in the navigation bar.
#. Click the Boot link in the sub navigation bar.
#. Select the Image tab.
#. Click the `Actions` drop and select `Remove`.
