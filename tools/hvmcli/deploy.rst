deploy
------

Deploy VME (VM Essentials) Manager or Worker virtual machines on the HVM host.

Commands
````````

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Command
     - Description
   * - ``manager``
     - Deploy, manage, or check status of the VME Manager VM
   * - ``worker``
     - Deploy, manage, or check status of a VME Worker VM

deploy manager
``````````````

Deploy or manage the VME Manager appliance virtual machine.

**Deploy a new Manager VM:**

.. code-block:: bash

   sudo hvmcli deploy manager \
     --ip 10.1.1.100 \
     --netmask 255.255.255.0 \
     --gateway 10.1.1.1 \
     --hostname vme-mgr \
     --image file:///mnt/iso/morpheus.qcow2 \
     --interface enp3s0 \
     --admin-user morphadmin \
     --admin-password-stdin

Options:

- ``--ip <address>`` — Static IP address for the Manager VM
- ``--netmask <mask>`` — Subnet mask
- ``--gateway <address>`` — Default gateway
- ``--hostname <name>`` — Hostname for the VM
- ``--image <uri>`` — Path or URL to the QCOW2 image (``file://`` or ``http://``)
- ``--interface <nic>`` — Host interface for the VM network
- ``--admin-user <username>`` — Administrator username for the appliance
- ``--admin-password-stdin`` — Read admin password from stdin (secure, no shell history)

**Run pre-deployment checks:**

.. code-block:: bash

   sudo hvmcli deploy manager precheck \
     --ip 10.1.1.100 \
     --interface enp3s0 \
     --image file:///mnt/iso/morpheus.qcow2 \
     --json

**Check Manager VM status:**

.. code-block:: bash

   sudo hvmcli deploy manager status
   sudo hvmcli deploy manager status --json

**View Manager deployment logs:**

.. code-block:: bash

   sudo hvmcli deploy manager logs
   sudo hvmcli deploy manager logs --lines 100 --diagnostics

Options:

- ``--lines <n>`` — Number of log lines to display
- ``--diagnostics`` — Include diagnostic information

deploy worker
`````````````

Deploy or manage a VME Worker virtual machine.

**Deploy a new Worker VM:**

.. code-block:: bash

   sudo hvmcli deploy worker \
     --ip 10.1.1.110 \
     --netmask 255.255.255.0 \
     --gateway 10.1.1.1 \
     --hostname vme-wkr1 \
     --image file:///mnt/iso/morpheus.qcow2 \
     --interface enp3s0 \
     --worker-url https://10.1.1.100 \
     --worker-key abc123 \
     --apikey def456 \
     --admin-password-stdin

Additional options for Worker:

- ``--worker-url <url>`` — URL of the Manager VM to register with
- ``--worker-key <key>`` — Worker registration key from the Manager
- ``--apikey <key>`` — API key for Manager authentication

**Check Worker VM status:**

.. code-block:: bash

   sudo hvmcli deploy worker status --json

.. tip:: Always run ``deploy manager precheck`` before deploying to validate that network connectivity, image accessibility, and host resources are adequate.
