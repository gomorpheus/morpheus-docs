Server Devices
--------------

Overview
^^^^^^^^

Server Devices in |morpheus| represent physical or virtual hardware peripherals (such as GPUs, PCIe devices, USB devices, or other passthrough hardware) that can be attached to or detached from virtual machines. Device management is used for hardware passthrough scenarios where VMs need direct access to physical devices on the host.

Role Requirements
^^^^^^^^^^^^^^^^^

- ``Infrastructure: Compute`` role permission at **Full** level is required to attach, detach, or assign devices.

Viewing Devices
^^^^^^^^^^^^^^^

#. Navigate to the server detail page
#. Select the **DEVICES** tab (where available)

The Devices tab displays all hardware devices currently associated with the server, including:

- **Name** — Device name or identifier
- **Type** — Device type (GPU, PCIe, USB, etc.)
- **Status** — Connection status (attached/detached)

Attaching a Device
^^^^^^^^^^^^^^^^^^

#. Navigate to the server detail page
#. Click :guilabel:`ACTIONS`
#. Select **Attach Device**
#. In the device dialog, configure:

   DEVICE
     Select from available devices on the host. Only unassigned devices compatible with the VM are shown.

#. Click :guilabel:`SAVE`

.. NOTE:: Attaching a device may require the VM to be powered off, depending on the device type and hypervisor capabilities.

Detaching a Device
^^^^^^^^^^^^^^^^^^

#. Navigate to the server detail page
#. Select the **DEVICES** tab
#. Click the detach icon next to the device
#. Confirm the detachment

Assigning a Device to a Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For scenarios where a device needs to be pre-assigned to a server (reserving it for future use):

#. Navigate to the server detail page
#. Click :guilabel:`ACTIONS`
#. Select **Assign Device**
#. Select the device to assign
#. Click :guilabel:`SAVE`

Assigned devices are reserved for the specified server and will not be available for other VMs.

.. WARNING:: Detaching a device from a running VM may cause application errors if software inside the VM is actively using the device. Always ensure workloads are quiesced before detaching passthrough devices.

Supported Device Types
^^^^^^^^^^^^^^^^^^^^^^

The availability of device management depends on the cloud and hypervisor type:

- **VMware vSphere** — PCI/PCIe passthrough, vGPU, DirectPath I/O devices
- **HVM/KVM** — PCI passthrough, USB devices, whole-GPU passthrough, and NVIDIA SR-IOV vGPU profiles. See :doc:`/infrastructure/clusters/hvm/nvidia_vgpu` for vGPU prerequisites and lifecycle constraints
- **Nutanix AHV** — GPU passthrough devices

.. NOTE:: Device availability is determined by the host's hardware configuration and the hypervisor's passthrough settings. Devices must be properly configured for passthrough at the host level before they appear as available in |morpheus|.
