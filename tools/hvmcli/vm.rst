vm
--

Manage virtual machines on the HVM host.

Commands
````````

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Command
     - Description
   * - ``list``
     - List VMs with name, power state, CPU, memory, and disk count
   * - ``start``
     - Start a virtual machine
   * - ``stop``
     - Stop a virtual machine (graceful or forced)
   * - ``restart``
     - Restart a virtual machine
   * - ``reboot``
     - Reboot a virtual machine

vm list
```````

List all virtual machines on the host with their current status.

.. code-block:: bash

   sudo hvmcli vm list

.. code-block:: text

   VM Name       Power State  CPUs  Memory(GB)  Disks
   ----------    -----------  ----  ----------  -----
   web-server    running      4     8.0         2
   db-server     running      8     32.0        4
   test-vm       shut off     2     4.0         1

Use ``--details`` for extended information:

.. code-block:: bash

   sudo hvmcli vm list --details

vm start
````````

Start a stopped virtual machine.

.. code-block:: bash

   sudo hvmcli vm start --name my-vm

Options:

- ``--name <vm>`` — Name of the virtual machine to start (required)

vm stop
```````

Stop a running virtual machine. By default performs a graceful ACPI shutdown.

.. code-block:: bash

   sudo hvmcli vm stop --name my-vm

Force an immediate power-off (equivalent to pulling the power cord):

.. code-block:: bash

   sudo hvmcli vm stop --name my-vm --force

Options:

- ``--name <vm>`` — Name of the virtual machine to stop (required)
- ``--force`` — Force immediate power-off without graceful shutdown

.. warning:: Using ``--force`` may cause data loss or filesystem corruption if the guest OS has pending writes.

vm restart
``````````

Restart a virtual machine (stop then start).

.. code-block:: bash

   sudo hvmcli vm restart --name my-vm

Options:

- ``--name <vm>`` — Name of the virtual machine to restart (required)

vm reboot
`````````

Send a reboot signal to the virtual machine's guest OS.

.. code-block:: bash

   sudo hvmcli vm reboot --name my-vm

Options:

- ``--name <vm>`` — Name of the virtual machine to reboot (required)
