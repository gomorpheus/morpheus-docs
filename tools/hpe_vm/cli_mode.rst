CLI (Non-Interactive) Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to the interactive TUI, ``hpe-vm`` supports a fully non-interactive command-line mode for automated or scripted deployments.

Usage
`````

.. code-block:: bash

   sudo hpe-vm --install [options]        # Deploy VME Manager
   sudo hpe-vm --install-worker [options]  # Deploy VME Worker

If ``--install`` or ``--install-worker`` is specified, the TUI is not launched. The deployment runs to completion and exits.

Options
```````

**Required for Manager install:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option
     - Description
   * - ``--address``
     - Static IP address for the appliance
   * - ``--netmask``
     - Subnet mask
   * - ``--gateway``
     - Default gateway
   * - ``--dns``
     - DNS server(s)
   * - ``--hostname``
     - FQDN of the appliance
   * - ``--password``
     - Admin password
   * - ``--imageUrl``
     - Path or URL to the QCOW2 image
   * - ``--applianceUrl``
     - Appliance access URL
   * - ``--interface``
     - Management network interface

**Additional options for Worker install:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option
     - Description
   * - ``--workerUrl``
     - Worker access URL
   * - ``--workerKey``
     - Distributed worker key from the Manager
   * - ``--apikey``
     - API key for worker authentication

**Optional:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option
     - Description
   * - ``--user``
     - Admin username (default: ``admin``)
   * - ``--size``
     - VM size (memory/CPU profile)
   * - ``--compute``
     - Compute network interface
   * - ``--vlan``
     - Compute VLAN tag
   * - ``--nopasswd``
     - Skip password confirmation prompt
   * - ``--debug``
     - Enable verbose logging
   * - ``--help``
     - Show usage information

Example
```````

Deploy a VME Manager non-interactively:

.. code-block:: bash

   sudo hpe-vm --install \
     --address 192.168.1.100 \
     --netmask 255.255.255.0 \
     --gateway 192.168.1.1 \
     --dns 192.168.1.1 \
     --hostname morpheus.example.com \
     --applianceUrl https://morpheus.example.com \
     --password 'SecurePass123!' \
     --imageUrl file:///mnt/iso/hpe-vm-essentials-9.0.0-1.qcow2 \
     --interface eno1 \
     --size large

Deploy a VME Worker:

.. code-block:: bash

   sudo hpe-vm --install-worker \
     --address 192.168.1.101 \
     --netmask 255.255.255.0 \
     --gateway 192.168.1.1 \
     --dns 192.168.1.1 \
     --hostname worker01.example.com \
     --workerUrl https://worker01.example.com \
     --applianceUrl https://morpheus.example.com \
     --password 'SecurePass123!' \
     --imageUrl file:///mnt/iso/hpe-vm-essentials-9.0.0-1.qcow2 \
     --interface eno1 \
     --workerKey 'abc123-worker-key' \
     --apikey 'xyz789-api-key'

Exit Codes
``````````

- ``0`` — Deployment completed successfully
- Non-zero — Deployment failed; check console output for error details
