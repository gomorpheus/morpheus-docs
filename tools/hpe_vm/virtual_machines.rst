Virtual Machines
^^^^^^^^^^^^^^^^

The **Virtual Machines** menu option lists and manages VMs running on the HVM host.

VM List
```````

Displays all VMs from ``virsh list --all``, including:

- VM name
- Current state (running, shut off, paused, etc.)

The list refreshes periodically to reflect current state.

VM Details
``````````

Selecting a VM shows its detailed information (from ``virsh dominfo``):

- Name, UUID, state
- CPU count, memory allocation
- Autostart setting

The state refreshes every 5 seconds.

VM Actions
``````````

Depending on the VM's current state, the following actions are available:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Action
     - Available When
     - Description
   * - **Start**
     - Shut off / Paused
     - Boot or resume the VM
   * - **Shutdown**
     - Running
     - Graceful ACPI shutdown
   * - **Reboot**
     - Running
     - Graceful ACPI reboot
   * - **Suspend**
     - Running
     - Pause the VM (freeze state in memory)
   * - **Destroy**
     - Running / Paused
     - Force power off (equivalent to pulling the power cord)
   * - **Undefine**
     - Shut off
     - Remove the VM definition from libvirt (does not delete disk images)

.. warning:: **Destroy** immediately kills the VM without graceful shutdown. Use only when the VM is unresponsive.
