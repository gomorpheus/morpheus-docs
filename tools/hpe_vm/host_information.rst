Host Information
^^^^^^^^^^^^^^^^

The **Host Information** menu option displays basic details about the HVM host hardware and operating system.

Displayed Information
`````````````````````

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Source
   * - **OS Name / Version**
     - Operating system release information
   * - **Product Name**
     - DMI product name (``/sys/class/dmi/id/product_name``)
   * - **Vendor**
     - DMI system vendor (``/sys/class/dmi/id/sys_vendor``)
   * - **CPU Model**
     - Processor model from ``/proc/cpuinfo``

This screen is read-only and provides a quick way to verify the host hardware without dropping to a shell.
