.. _preseed_scripts:

Preseed/Kickstart Scripts
=========================

Overview
--------

Preseed Scripts (|TooPre|) manage Kickstart and Preseed configuration files for automated operating system installation during bare-metal and image build workflows. These scripts provide the unattended installation answers that configure partitioning, networking, packages, and post-installation steps.

Preseed scripts are served over HTTP by the |morpheus| appliance and referenced from boot scripts or image build configurations.

.. NOTE:: Preseed files are publicly accessible by filename via HTTP URL. The filename serves as the access identifier. A future enhancement may add temporary URL support for provisioning-phase-only access.

Role Permissions
----------------

Access to Preseed Scripts is controlled by the following role permission:

- **Tools: Image Builder** — ``None``, ``Read``, or ``Full``

  - **None:** Cannot access Preseed Scripts
  - **Read:** Can view preseed scripts
  - **Full:** Can create, edit, and delete preseed scripts

Viewing Preseed Scripts
-----------------------

#. Navigate to |TooPre| (Tools > Preseed Scripts)
#. The list displays all preseed scripts with:

   - **File Name:** The script filename (must be unique)
   - **Description:** Script description
   - **Created By:** User who created the script

Creating a Preseed Script
--------------------------

#. Navigate to |TooPre|
#. Click :guilabel:`+ ADD`
#. Complete the form:

   - **FILE NAME:** Unique filename for the script (e.g., ``centos9-ks.cfg``, ``ubuntu-22.04.seed``). This determines the URL where the script is served.
   - **DESCRIPTION:** Optional description
   - **CONTENT:** The preseed or kickstart file content

#. Click :guilabel:`SAVE`

Kickstart Format (RHEL/CentOS/Rocky)
--------------------------------------

Kickstart files automate Red Hat-based installations:

.. code-block:: text

  # System authorization
  auth --enableshadow --passalgo=sha512

  # Installation source
  url --url="http://mirror.example.com/centos/9-stream/BaseOS/x86_64/os/"

  # Disk partitioning
  clearpart --all --initlabel
  autopart --type=lvm

  # Network
  network --bootproto=dhcp --device=eth0 --onboot=on

  # Root password (encrypted)
  rootpw --iscrypted $6$rounds=656000$...

  # Timezone
  timezone America/New_York --utc

  # Packages
  %packages
  @^minimal-environment
  open-vm-tools
  curl
  %end

  # Post-installation
  %post
  # Install Morpheus Agent
  curl -k https://<%=morpheus.applianceUrl%>/api/server-script/agentInstall?type=centos | bash
  %end

Preseed Format (Debian/Ubuntu)
-------------------------------

Preseed files automate Debian-based installations:

.. code-block:: text

  # Locale and keyboard
  d-i debian-installer/locale string en_US.UTF-8
  d-i keyboard-configuration/xkb-keymap select us

  # Network
  d-i netcfg/choose_interface select auto
  d-i netcfg/get_hostname string unassigned-hostname

  # Mirror
  d-i mirror/country string manual
  d-i mirror/http/hostname string archive.ubuntu.com
  d-i mirror/http/directory string /ubuntu

  # Partitioning
  d-i partman-auto/method string lvm
  d-i partman-auto/choose_recipe select atomic
  d-i partman/confirm_write_new_label boolean true
  d-i partman/confirm boolean true

  # User account
  d-i passwd/root-login boolean true
  d-i passwd/root-password-crypted password $6$rounds=656000$...

  # Packages
  tasksel tasksel/first multiselect standard
  d-i pkgsel/include string openssh-server open-vm-tools curl

  # Post-install
  d-i preseed/late_command string \
    in-target curl -k https://<%=morpheus.applianceUrl%>/api/server-script/agentInstall?type=ubuntu | in-target bash

  # Finish
  d-i finish-install/reboot_in_progress note

Using Morpheus Variables
-------------------------

Preseed and Kickstart scripts support |morpheus| variable injection:

.. code-block:: text

  # Reference Morpheus appliance URL
  <%=morpheus.applianceUrl%>

  # Reference PXE root password from settings
  rootpw --iscrypted <%=morpheus.pxeRootPassword%>

  # Reference custom variables
  <%=customOptions.myVar%>

Variables are resolved at serve-time when the installing system requests the preseed file.

Editing a Preseed Script
-------------------------

#. Navigate to |TooPre|
#. Click the pencil icon on the script row
#. Modify the content or metadata
#. Click :guilabel:`SAVE`

Deleting a Preseed Script
--------------------------

#. Navigate to |TooPre|
#. Click the trash icon on the script row
#. Confirm deletion

Integration with Boot Process
------------------------------

Preseed scripts are referenced from Boot Scripts in the kernel parameters:

**Kickstart:**

.. code-block:: text

  imgargs vmlinuz inst.ks=http://${morpheus-appliance}/preseed/centos9-ks.cfg

**Preseed:**

.. code-block:: text

  imgargs vmlinuz auto=true url=http://${morpheus-appliance}/preseed/ubuntu-22.04.seed

The workflow is:

#. Boot script loads kernel and initrd
#. Kernel parameters point to the preseed/kickstart URL on |morpheus|
#. The installer downloads and processes the preseed/kickstart file
#. Installation proceeds unattended with the configured answers

API
---

Preseed scripts can be managed via the |morpheus| API:

.. code-block:: bash

  # List preseed scripts
  curl "$MORPHEUS_API_URL/api/preseed-scripts" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN"

  # Create a preseed script
  curl -X POST "$MORPHEUS_API_URL/api/preseed-scripts" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "preseedScript": {
        "fileName": "ubuntu-22.04.seed",
        "description": "Ubuntu 22.04 preseed for production",
        "content": "d-i debian-installer/locale string en_US.UTF-8\n..."
      }
    }'
