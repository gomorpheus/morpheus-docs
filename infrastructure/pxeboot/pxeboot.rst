PXE Boot
========

Overview
--------

|morpheus| includes a built in PXE Server to enable easy and rapid bare metal provisioning.

Prerequisites
-------------

* DHCP server with following config added to dhcpd.conf

.. code-block:: bash

    allow booting;
    allow bootp;
    option option-128 code 128 = string;
    option option-129 code 129 = text;
    next-server morpheus-appliance-ip;
    filename "pxelinux.0";

.. NOTE:: Replace ``morpheus-appliance-ip`` in the dhcpd.conf file with your |morpheus| appliance IP address.

* ``Internal Appliance URL (PXE)`` set in `Administration - Settings`. For PXE-Boot your appliance needs to be routable directly with minimal NAT masquerading. This allows one to override the default appliance url endpoint for use by the PXE Server. If this is unset, the default appliance url will be used instead.
* Mac or IP addresses of PXE target mapped in {morpheus} `Infrastructure -> Boot - Mapping`
* Target host configured for Network boot in BIOS

.. NOTE:: On the |Morpheus| Appliance, PXE is enabled by default and port 69 is forwarded to the Internal PXE port 6969. These settings are configurable in in the ``pxe:`` section of ``/opt/morpheus/conf/application.yml``.


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
   MENU
     Paste in PXE Menu
      Example PXE 6.5.0 Menu:

      .. important:: Ensure the case of file references match actual file names.

      .. code-block:: bash
         :name: PXE 6.5.0 Menu

       DEFAULT vesamenu.c32
       TIMEOUT 300
       ONTIMEOUT esxi
       PROMPT 0
       MENU INCLUDE pxelinux.cfg/pxe.conf
       NO ESCAPE 1
       LABEL local
         menu LABEL Boot to local disk
         localboot 0
         TEXT HELP
         Boot to local hard disk
         ENDTEXT
       LABEL esxi
         menu LABEL ESXI 6.5.0 u1
         kernel tftp://${bootUrl}/image/${imageId}/MBOOT.C32
         append -c tftp://${bootUrl}/image/${imageId}/BOOT.CFG ks=${answerFile}
         TEXT HELP
           Boot the ESXI 6.5.0 u1 install
         ENDTEXT
       MENU END
   Bucket
    Select Bucket or File Share where PXE Image files exist
   Image Path
    Path of the image relative to the selected Bucket or Storage Provider

#. Save Changes

Edit Image
^^^^^^^^^^

#. Click the Infrastructure link in the navigation bar.
#. Click the Boot link in the sub navigation bar
#. Select the Images tab
#. Click the actions drop down and select edit.
#. Modify information as needed.
#. Click the Save Changes button to save.


Remove Image
^^^^^^^^^^^^

#. Click the Infrastructure link in the navigation bar.
#. Click the Boot link in the sub navigation bar.
#. Select the Image tab.
#. Click the `Actions` drop and select `Remove`.

.. include:: /infrastructure/pxeboot/esxi65.rst
