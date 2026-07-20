software
--------

Inspect installed software packages and manage OS updates.

Commands
````````

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Command
     - Description
   * - ``list``
     - List installed versions for qemu, libvirt, kernel, and hvmcli
   * - ``update``
     - Manage package and OS updates

software list
`````````````

Show installed versions of key HVM components.

.. code-block:: bash

   sudo hvmcli software list

software update
```````````````

Manage OS and package updates with pre-checks, rollback support, and history tracking.

**List available updates:**

.. code-block:: bash

   sudo hvmcli software update list

**Run pre-check before updating:**

.. code-block:: bash

   sudo hvmcli software update precheck
   sudo hvmcli software update precheck --interactive

**Check pre-check status:**

.. code-block:: bash

   sudo hvmcli software update precheck status

**Perform OS update:**

.. code-block:: bash

   sudo hvmcli software update os
   sudo hvmcli software update os --force
   sudo hvmcli software update os --interactive

Options:

- ``--force`` — Skip confirmation and proceed with update
- ``--interactive`` — Run in interactive mode with progress display

**Check update status:**

.. code-block:: bash

   sudo hvmcli software update status

**View update history:**

.. code-block:: bash

   sudo hvmcli software update history
   sudo hvmcli software update history --count 5
   sudo hvmcli software update history --id 2026-04-07T12-15-25Z

Options:

- ``--count <n>`` — Limit to last N entries
- ``--id <timestamp>`` — Show details for a specific update

**Rollback an update:**

.. code-block:: bash

   sudo hvmcli software update rollback --dry-run
   sudo hvmcli software update rollback

Options:

- ``--dry-run`` — Preview what would be rolled back without making changes

**Install a specific package:**

.. code-block:: bash

   sudo hvmcli software update package install --file /tmp/package.deb

Options:

- ``--file <path>`` — Path to the .deb package file to install

.. important:: Always run ``precheck`` before performing an OS update. The pre-check validates that the host is in a safe state for updates (no running VMs, cluster quorum intact, sufficient disk space).
