hardware
--------

Inspect host hardware inventory and platform telemetry.

Commands
````````

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Command
     - Description
   * - ``cpu``
     - Show CPU topology, model, cores, and threads
   * - ``memory``
     - Show memory modules, total capacity, and speed
   * - ``pci``
     - List PCI devices (network adapters, GPUs, storage controllers)
   * - ``bootvolume``
     - Show boot volume details and mount points
   * - ``ipmi``
     - Show IPMI/BMC sensor readings (requires ipmitool)

hardware cpu
````````````

Display CPU architecture, topology, and virtualization details.

.. code-block:: bash

   sudo hvmcli hardware cpu list

.. code-block:: text

   Architecture           x86_64
     CPU(s)                 64
     Thread(s) per core     2
     Core(s) per socket     16
     Socket(s)              2
     Model Name             AMD EPYC 9334 32-Core Processor
     Vendor ID              AuthenticAMD
     Virtualization         AMD-V
     Logical CPU Threads    64
     Hyperthreading Active  yes
     Physical CPU Cores     32

hardware memory
```````````````

Display memory capacity, usage, NUMA, and HugePages information.

.. code-block:: bash

   sudo hvmcli hardware memory list

.. code-block:: text

     Physical Memory   512.00 GiB
     Reliable Memory   512.00 GiB
     NUMA Node Count   2
     Total Memory      512.00 GiB
     Used Memory       128.50 GiB
     Available Memory  383.50 GiB
     Free Memory       256.00 GiB
     Swap Total        4.00 GiB
     Swap Free         4.00 GiB
     HugePages Total   0
     HugePages Free    0
     HugePage Size     2.00 MiB

hardware pci
````````````

List all PCI devices including network adapters, GPUs, and storage controllers.

.. code-block:: bash

   sudo hvmcli hardware pci list

.. code-block:: text

   Slot     Class                    Device                                               Vendor:Device
   -------  -----------------------  ---------------------------------------------------  -------------
   03:00.0  Ethernet controller      Mellanox ConnectX-6 Dx 25GbE Dual Port SFP28         15b3:101d
   04:00.0  Ethernet controller      Mellanox ConnectX-6 Dx 25GbE Dual Port SFP28         15b3:101d
   41:00.0  RAID bus controller      HPE Smart Array P408i-a SR Gen10                     9005:028f
   ...

hardware bootvolume
```````````````````

Show boot volume details including disk type, filesystem, and size.

.. code-block:: bash

   sudo hvmcli hardware bootvolume list

.. code-block:: text

     Root Device             /dev/ubuntu--vg-ubuntu--lv
     Boot Device Identifier  /dev/sda2
     Boot Device Type        part
     Root Filesystem         ext4
     Root Type               lvm
     Root Size               480G
     Boot Device             /dev/sda2
     Boot Filesystem         ext4
     Boot Size               2G
     Boot Disk               /dev/sda
     Boot Disk Size          480G
     Boot Disk Model         MO000480JWTBR
     Boot Disk Serial        PHYG123456
     Boot Disk Transport     sata
     Boot Disk Rotational    no
     Boot Disk Read-Only     no

hardware ipmi
`````````````

Show IPMI/BMC sensor readings for platform telemetry.

.. code-block:: bash

   sudo hvmcli hardware ipmi

.. note:: Requires ``ipmitool`` to be installed on the host. Only available on physical servers with a BMC/iLO.
