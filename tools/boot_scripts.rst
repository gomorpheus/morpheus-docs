.. _boot_scripts:

Boot Scripts
============

Overview
--------

Boot Scripts (|TooBot|) provide iPXE boot script management for bare-metal provisioning workflows. Boot scripts define the iPXE command sequences that direct bare-metal servers through the PXE boot process, including downloading kernels, initrd images, and specifying installation parameters.

Boot scripts are served over HTTP by the |morpheus| appliance during the PXE boot process and can be customized for different hardware configurations, operating systems, and deployment scenarios.

Role Permissions
----------------

Access to Boot Scripts is controlled by the following role permission:

- **Tools: Image Builder** — ``None``, ``Read``, or ``Full``

  - **None:** Cannot access Boot Scripts
  - **Read:** Can view boot scripts
  - **Full:** Can create, edit, and delete boot scripts

Viewing Boot Scripts
--------------------

#. Navigate to |TooBot| (Tools > Boot Scripts)
#. The list displays all available boot scripts including:

   - **File Name:** The script file name (used in the boot URL)
   - **Description:** Script description
   - **Visibility:** Public (available to all tenants) or Private

System-provided boot scripts (no account owner) with public visibility are available to all tenants but cannot be modified.

Creating a Boot Script
-----------------------

#. Navigate to |TooBot|
#. Click :guilabel:`+ ADD`
#. Complete the form:

   - **FILE NAME:** The filename for the boot script (must be unique). This determines the URL path where the script is served (e.g., ``myboot.ipxe``)
   - **DESCRIPTION:** Optional description of the script's purpose
   - **CONTENT:** The iPXE script content

#. Click :guilabel:`SAVE`

iPXE Script Format
------------------

Boot scripts use iPXE scripting syntax. Example scripts:

**Basic Linux Installation:**

.. code-block:: text

  #!ipxe
  kernel http://${morpheus-appliance}/images/vmlinuz
  initrd http://${morpheus-appliance}/images/initrd.img
  imgargs vmlinuz inst.repo=http://${morpheus-appliance}/repo inst.ks=http://${morpheus-appliance}/preseed/ks.cfg
  boot

**Ubuntu Cloud Image:**

.. code-block:: text

  #!ipxe
  set base-url http://${morpheus-appliance}/images/ubuntu
  kernel ${base-url}/vmlinuz
  initrd ${base-url}/initrd
  imgargs vmlinuz auto=true url=http://${morpheus-appliance}/preseed/ubuntu.seed
  boot

**Menu-Based Selection:**

.. code-block:: text

  #!ipxe
  menu Boot Options
  item centos CentOS Stream 9
  item ubuntu Ubuntu 22.04 LTS
  item shell iPXE Shell
  choose os && goto ${os}

  :centos
  kernel http://${morpheus-appliance}/images/centos/vmlinuz
  initrd http://${morpheus-appliance}/images/centos/initrd.img
  boot

  :ubuntu
  kernel http://${morpheus-appliance}/images/ubuntu/vmlinuz
  initrd http://${morpheus-appliance}/images/ubuntu/initrd
  boot

  :shell
  shell

Editing a Boot Script
---------------------

#. Navigate to |TooBot|
#. Click the pencil icon on the script row or click the script name to view, then click :guilabel:`EDIT`
#. Modify the script content or metadata
#. Click :guilabel:`SAVE`

Deleting a Boot Script
-----------------------

#. Navigate to |TooBot|
#. Click the trash icon on the script row
#. Confirm deletion

.. WARNING:: Do not delete boot scripts that are actively referenced by PXE configurations or Image Builds. Verify no active workflows depend on the script before removal.

Integration with PXE Boot
---------------------------

Boot scripts work in conjunction with the |morpheus| PXE boot infrastructure:

#. The DHCP server directs booting servers to the |morpheus| TFTP/HTTP server
#. The boot loader (iPXE) requests the configured boot script
#. |morpheus| serves the boot script content
#. The booting server executes the iPXE commands (download kernel, initrd, boot)
#. The server proceeds with OS installation using the specified preseed/kickstart configuration

For PXE infrastructure setup, see the Boot section of the Infrastructure documentation.

API
---

Boot scripts can be managed via the |morpheus| API:

.. code-block:: bash

  # List boot scripts
  curl "$MORPHEUS_API_URL/api/boot-scripts" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN"

  # Create a boot script
  curl -X POST "$MORPHEUS_API_URL/api/boot-scripts" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "bootScript": {
        "fileName": "myboot.ipxe",
        "description": "Custom boot script",
        "content": "#!ipxe\nkernel http://server/vmlinuz\nboot"
      }
    }'
