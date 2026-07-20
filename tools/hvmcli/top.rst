top
---

Real-time host and VM resource monitoring. Similar to the Linux ``top`` command but focused on virtualization metrics.

Commands
````````

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Command
     - Description
   * - ``cpu``
     - Per-VM CPU utilisation, vCPUs, and state
   * - ``memory``
     - Per-VM memory allocated, used, and balloon
   * - ``network``
     - Per-vNIC packet/byte rates and drops
   * - ``disk``
     - Per-block-device IOPS and throughput
   * - ``hba``
     - FC/iSCSI adapter performance
   * - ``host``
     - Host summary (uptime, load, VM count)

top (default)
`````````````

Run the interactive top view showing an overview of all resources.

.. code-block:: bash

   sudo hvmcli top

.. code-block:: bash

   sudo hvmcli top --json

top cpu
```````

Show per-VM CPU utilisation, vCPU count, and power state.

.. code-block:: bash

   sudo hvmcli top cpu --json

Filter by VM name:

.. code-block:: bash

   sudo hvmcli top cpu --filter web-vm --json

top memory
``````````

Show per-VM memory allocation, actual usage, and balloon driver status.

.. code-block:: bash

   sudo hvmcli top memory --json

top network
```````````

Show per-vNIC packet rates, byte throughput, and drop counts.

.. code-block:: bash

   sudo hvmcli top network --json

top disk
````````

Show per-block-device IOPS and throughput for VMs.

.. code-block:: bash

   sudo hvmcli top disk --json

top hba
```````

Show Fibre Channel and iSCSI adapter performance metrics.

.. code-block:: bash

   sudo hvmcli top hba --json

top host
````````

Show a host-level summary including uptime, load averages, and VM count.

.. code-block:: bash

   sudo hvmcli top host --json

.. code-block:: json

   {
     "errorCode": 0,
     "messages": "",
     "data": {
       "uptime": "5 days, 12 hours, 45 minutes",
       "vmCount": 12,
       "totalVcpus": 48,
       "loadAvg1": 2.15,
       "loadAvg5": 1.89,
       "loadAvg15": 1.72
     }
   }

Options (all subcommands):

- ``--json`` — Output in JSON format
- ``--filter <vm-name>`` — Filter results to a specific VM
