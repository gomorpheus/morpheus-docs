HPE-VM Console Overview
^^^^^^^^^^^^^^^^^^^^^^^

The ``hpe-vm`` console is a text-based user interface (TUI) application that runs directly on the HVM host's physical or virtual console. It provides an interactive menu for initial host configuration and Morpheus appliance deployment without requiring SSH access or a separate workstation.

.. important:: ``hpe-vm`` is only available on **HVM OS Ubuntu 24.04**. On HVM OS Ubuntu 26.04+, this tool is deprecated and replaced by :doc:`/tools/hvmcli/hvmcli` for CLI operations and the :doc:`/getting_started/installation/singleNode/hpe_installer` for graphical deployments.

Accessing the Console
`````````````````````

The ``hpe-vm`` console starts automatically when you log in to the HVM host's local console (physical display, iLO remote console, or serial console). It is the default shell for the ``ubuntu`` user on HVM OS 24.04.

If you need to restart the console manually:

.. code-block:: bash

   sudo hpe-vm

Main Menu
`````````

The main menu provides the following options:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Menu Item
     - Description
   * - **Host Information**
     - Display hardware and OS details about the HVM host
   * - **Configure Network**
     - Edit netplan network configuration (interfaces, bonds, VLANs)
   * - **Virtual Machines**
     - List and manage VMs running on the host
   * - **Keyboard Layout / TimeZone**
     - Configure locale, keymap, and timezone settings
   * - **Install VME Manager**
     - Deploy a Morpheus Enterprise or VM Essentials Manager appliance
   * - **Install VME Worker**
     - Deploy a Morpheus Worker appliance
   * - **iLO**
     - Display HPE iLO hardware and network information (HPE servers only)
   * - **Exit**
     - Exit the console application

Navigation
``````````

- Use **Arrow keys** or **Tab** to move between fields and buttons
- Press **Enter** or **Space** to activate a button or select an item
- Use **Escape** to go back or cancel a dialog
