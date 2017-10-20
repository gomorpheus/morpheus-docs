PXE Boot
--------
.. add images menu info

Overview
^^^^^^^^

|morpheus| includes a built in PXE Server to enable easy and rapid bare metal provisioning. Simply map your TFTP server port to the |morpheus| sevrer port 6969 and you are ready to PXE boot from the provided images and answer files, or add your own to bring up Bare metal Hosts with ease.

=== Prerequisites

Your network must be configured for PXE boot, and the TFTP server port need to mapped to the |morpheus| TFT server port, UDP 6969.

* Network configured for network boot
* Router UDP 69 mapped to |morpheus| server UDP port 6969
* Router TFT Server set to |morpheus| server IP or resolvable Hostname.
* Mac or IP addresses of PXE target mapped in |morpheus| `Infrastructure -> Boot - Mapping`
* Target host configured for Network boot in BIOS

NOTE: The |morpheus| PXE port is set in `opt/morpheus/conf/application.yml`

=== To PXE Boot

. Click the Infrastructure link in the navigation bar.
. Select the Boot link in the sub navigation bar.

==== Add Mapping

. Select the Mapping tab then click the Add Mapping button.
. From the New Mapping Wizard input the following information:
Match Pattern:: Mac address separated by ':' or an ip address filter
Description(optional):: Description of the new mapping.
Active:: Flag to denote the mapping as active or disabled.
Operating System:: List of operating systems for the mapping.
Boot Image:: Lists available PXE boot images.
Answer File:: Lists available answer files.
Cloud:: Lists the available clouds.
Server Mode: List of server modes:: unmanaged, Managed, Bare metal host, Container host, VM host, and Container & VM host.
Click the Save Changes button to save.

Once the mapping is added, and the target host is powered on, the |morpheus| PXE menu will load and PXE boot will start.

==== Edit Mapping

. Click the Infrastructure link in the navigation bar.
. Click the Boot link in the sub navigation bar.
. Click the edit icon on the row of the mapping you wish to edit.
. Modify information as needed.
. Click the Save Changes button to save.

==== Delete Mapping

. Click the Infrastructure link in the navigation bar.
. Click the Boot link in the sub navigation bar.
. Click the delete icon on the row of the mapping you wish to delete.

=== Answer Files

Answer files are like lists of answers for questions that you know the setup program is going to ask but the user is not prepared to answer. They contain one or more sections, and each section contains one or more properties in the form name=value. Morpheus provides Answer Files for ESXi, CentOS, Ubuntu and XenServer, and user can add their own.

==== Add Answer Files

. Click the Infrastructure link in the navigation bar.
. Click the Boot link in the sub navigation bar
. Select the Answer Files tab then click the Add Answer File button.
. From the New Answer File Wizard input the following information
Name:: Name of the answer file.
Description(optional):: Description of the new answer file.
Active:: Flag to denote the mapping as active or disabled.
Script Name:: Name of the new answer file.
Script Version:: Version of the new answer file.
Script:: The script for the new answer file.
. Click the Save Changes button to save.

==== Edit Answer File

. Click the Infrastructure link in the navigation bar.
. Click the Boot link in the sub navigation bar
. Select the Answer Files tab
. Click the edit icon on the row of the answer file you wish to edit.
. Modify information as needed.
. Click the Save Changes button to save.

==== Delete Answer File

. Click the Infrastructure link in the navigation bar.
. Click the Boot link in the sub navigation bar
. Select the Answer Files tab.
. Click the delete icon on the row of the answer file you wish to delete.

=== Images

Morpheus provides Images for ESXi, CentOS, Ubuntu and XenServer, and user can add their own.

==== Add Images

. Click the Infrastructure link in the navigation bar.
. Click the Boot link in the sub navigation bar
. Select the Images tab then click the Add Image button.
. From the Upload Virtual Image Wizard input the following information
Name:: Name of the answer file.
Operating System:: List of available operating systems.
Menu::
Storage Provider:: List of available storage providers.
Image Path:: Path of the image.
Visibility:: Private or Public
Account:: List of accounts to allow permission to this image.
. Click the Save Changes button to save.

==== Edit Image

. Click the Infrastructure link in the navigation bar.
. Click the Boot link in the sub navigation bar
. Select the Images tab
. Click the actions drop down and select edit.
. Modify information as needed.
. Click the Save Changes button to save.

==== Convert Image

. Click the Infrastructure link in the navigation bar.
. Click the Boot link in the sub navigation bar.
. Select the Images tab
. Click the `Actions` drop and select `Convert`.

==== Download Image

. Click the Infrastructure link in the navigation bar.
. Click the Boot link in the sub navigation bar.
. Select the Images tab
. Click the `Actions` drop and select `Download`.

==== Remove Image

. Click the Infrastructure link in the navigation bar.
. Click the Boot link in the sub navigation bar.
. Select the Image tab.
. Click the `Actions` drop and select `Remove`.
