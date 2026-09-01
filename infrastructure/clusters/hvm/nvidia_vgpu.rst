NVIDIA vGPU Slicing
===================

Morpheus 9.1 supports NVIDIA SR-IOV vGPU slicing on HVM/KVM Hosts. A supported physical NVIDIA GPU can expose virtual functions (VFs), and each VF can be programmed with an NVIDIA vGPU profile and assigned to a VM. This allows multiple VMs to share one physical GPU while receiving defined framebuffer and compute resources.

This workflow is different from whole-GPU passthrough. Whole-GPU passthrough detaches the physical GPU from the Host and assigns it to one VM through VFIO. NVIDIA vGPU slicing keeps the physical GPU and its VFs bound to the NVIDIA vGPU Manager on the Host.

.. important::

   Morpheus does not install the NVIDIA vGPU Manager, install NVIDIA guest drivers, create an NVIDIA License System service instance, or deploy NVIDIA client licensing tokens. Obtain the NVIDIA software and license entitlement through the appropriate NVIDIA and HPE channels, and use a host OS, kernel, GPU, vGPU Manager, guest driver, profile, and guest OS combination supported by both HPE and NVIDIA.

Architecture and Terms
----------------------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Term
     - Description
   * - Physical GPU or PF
     - The physical NVIDIA GPU installed in the HVM Host. It remains bound to the NVIDIA Host driver while segmentation is enabled.
   * - Virtual function or VF
     - A child PCI device created through NVIDIA SR-IOV. Morpheus displays VFs beneath the physical GPU on the Host's Devices tab.
   * - Segment Type
     - The NVIDIA vGPU profile programmed on a VF. The profile defines properties such as framebuffer allocation and intended workload class.
   * - Homogeneous Segmentation
     - Uses profiles with the same framebuffer size on one physical GPU. Choose this mode for predictable, uniform VM capacity and simpler placement.
   * - Heterogeneous Segmentation
     - Allows different profile sizes on one physical GPU when the GPU, NVIDIA software, and selected profiles support mixed-size mode. This improves workload flexibility but can reduce placement efficiency.
   * - Service Plan GPU Type
     - The physical GPU type or vGPU Segment Type that every GPU requested by the Service Plan must match.

Morpheus 9.1 manages PCI/SR-IOV VFs. Do not treat NVIDIA MIG or legacy mediated-device inventory as equivalent to the supported SR-IOV workflow; MIG/mdev correlation and lifecycle management are not complete in this release.

Plan the Slicing Model
----------------------

Choose the slicing model before creating VFs and Service Plans:

#. Identify whether workloads require graphics, virtual desktops, virtual applications, or compute acceleration.
#. Select an NVIDIA vGPU profile series and framebuffer size supported by the physical GPU, guest OS, NVIDIA software release, and license entitlement.
#. Determine how many identically sized profiles fit on each GPU and whether homogeneous mode satisfies the workload mix.
#. Use heterogeneous mode only when mixed profile sizes are required and NVIDIA supports mixed-size mode for that GPU and profile combination.
#. Reserve capacity for maintenance and Host failure. Morpheus can place a VM only when a matching, pre-created VF is available on an eligible Host.

The profile list in Morpheus is filtered by the types that the installed NVIDIA vGPU Manager reports as currently creatable. A profile present in the Morpheus catalog might not appear for a Host if the GPU, driver release, current segmentation mode, or remaining framebuffer does not support it.

Host Prerequisites
------------------

Before enabling segmentation, verify all of the following on every GPU Host:

- The HVM Host uses the supported Ubuntu release and kernel for the selected HVM layout.
- The server platform and GPU appear in the NVIDIA support matrix for that exact vGPU software release.
- VT-d/IOMMU, SR-IOV, and Alternative Routing-ID Interpretation (ARI) are enabled in system firmware when required by the GPU architecture. NVIDIA requires these settings for Ampere and later GPUs.
- The GPU is in the display mode required by NVIDIA. Some workstation GPUs require display-off mode for vGPU operation.
- A compatible NVIDIA vGPU Manager is installed on the Host and its required services are enabled.
- The corresponding NVIDIA vGPU guest driver package is available for each supported Windows or Linux guest image.
- DNS, time synchronization, routing, proxy, and firewall configuration permit guest VMs to reach the selected NVIDIA License System service instance.

See the NVIDIA `Virtual GPU Software User Guide <https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html>`_, `Linux with KVM support matrix <https://docs.nvidia.com/vgpu/latest/product-support-matrix/generic-linux-kvm.html>`_, `Ubuntu support matrix <https://docs.nvidia.com/vgpu/latest/product-support-matrix/ubuntu.html>`_, and release notes for the selected NVIDIA vGPU software branch. Do not install a newer generic NVIDIA driver solely because it is available; host kernel and guest driver compatibility must be maintained as a set.

Install the NVIDIA Host Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NVIDIA vGPU software is entitlement-controlled. Download the Linux KVM Host package and matching guest drivers from the NVIDIA Licensing Portal. Sign in to the `NVIDIA Application Hub <https://nvid.nvidia.com/dashboard/>`_ with an NVIDIA Enterprise Account, open the NVIDIA Licensing Portal, and select **Software Downloads**. NVIDIA's `Getting NVIDIA vGPU Software <https://docs.nvidia.com/vgpu/latest/grid-software-quick-start-guide/getting-your-nvidia-grid-software.html>`_ guide describes the account and download process.

Download the NVIDIA vGPU software release for Linux KVM that is authorized for the environment. Confirm GPU, Host OS, and guest OS support in NVIDIA's `Linux with KVM support matrix <https://docs.nvidia.com/vgpu/latest/product-support-matrix/generic-linux-kvm.html>`_ and the `Ubuntu support matrix <https://docs.nvidia.com/vgpu/latest/product-support-matrix/ubuntu.html>`_ for the HVM Host OS. The package includes the NVIDIA vGPU Manager for the Host and matching guest drivers.

#. Place the HVM Host into maintenance and evacuate or stop workloads according to :doc:`host_maintenance`.
#. Confirm the exact HVM OS, kernel, GPU, firmware, and Secure Boot state.
#. Install the HPE-approved NVIDIA vGPU Manager package using the NVIDIA instructions for that Ubuntu and driver release.
#. Complete any required module signing when Secure Boot is enabled.
#. Enable the NVIDIA vGPU Manager services required by the installed release and reboot the Host when directed by NVIDIA.
#. Verify that ``nvidia-smi`` reports the physical GPU and expected vGPU capabilities without driver or Xid errors.
#. Return the Host to service and refresh its inventory in Morpheus.

.. warning::

   Do not copy package names or version numbers from another environment. NVIDIA vGPU Manager modules are kernel-dependent. An unsupported kernel or mismatched host and guest driver branch can prevent VMs from starting or make the GPU unavailable after an upgrade.

Enable Segmentation and Create Profiles
---------------------------------------

Users require **Infrastructure: Server Devices** permission at the **Full** level.

#. Navigate to :menuselection:`Infrastructure --> Hosts`, open the HVM Host, and select :guilabel:`Devices`.
#. Locate the physical NVIDIA GPU. It must have **Attached** Host status; do not detach a GPU that will be segmented.
#. From the GPU's Actions menu, select :guilabel:`Enable Homogeneous Segmentation` or :guilabel:`Enable Heterogeneous Segmentation`.
#. Refresh Host devices if the child VFs do not appear automatically.
#. Expand the physical GPU row to display its virtual functions.
#. For an unprogrammed VF, select :guilabel:`Create Segment Type`.
#. Select a :guilabel:`Segment Type` from the profiles reported as creatable, then click :guilabel:`Execute`.
#. Repeat for each VF that should be available for manual assignment or Service Plan provisioning.

In homogeneous mode, the first programmed VF establishes the framebuffer size for the remaining profiles on that physical GPU. The creatable-types list narrows to profiles in the same family. In heterogeneous mode, profiles from different families and framebuffer sizes can coexist on the same physical GPU until framebuffer capacity is exhausted.

To switch between homogeneous and heterogeneous mode, use the GPU's Actions menu and select :guilabel:`Switch to Heterogeneous` or :guilabel:`Switch to Homogeneous`. Switching mode or disabling segmentation is blocked while any child VF is assigned to a VM. Unassign all VFs from their VMs first; you do not have to manually destroy every programmed Segment Type to switch modes or disable segmentation.

.. warning::

   Do not detach a physical NVIDIA GPU while segmentation is enabled, and do not detach a programmed NVIDIA VF from the Host driver. Segmented VFs must remain NVIDIA-bound. Detaching the physical GPU can destabilize libvirt or the Host.

Create a vGPU Service Plan
--------------------------

#. Navigate to :menuselection:`Administration --> Plans` and add or edit an HVM/KVM Service Plan.
#. Set :guilabel:`GPU Count` to the number of GPU devices required by each VM. The selected GPU Type applies uniformly to every device in this count.
#. Select :guilabel:`GPU Type` from the grouped typeahead picker:

   - **Any GPU** — Accepts any assignable GPU unit on the target Host, whether a whole physical card or a programmed vGPU VF. Use this when the workload does not require a specific GPU model or profile.
   - **Physical GPU type** (bold, top-level row) — Requests whole-device passthrough of that exact GPU model. The physical card must be detached from the Host driver and not segmented. Selecting a physical type scopes the plan to the **Device Type**: only whole cards whose ``ComputeDeviceType`` matches are eligible.
   - **Segment Type** (indented row beneath a physical GPU type) — Requests a pre-created VF programmed with that exact NVIDIA vGPU profile. The VF must already exist and have the matching Segment Type assigned. Selecting a Segment Type scopes the plan to the **Segment Type**: only VFs whose ``ComputeDeviceSegmentType`` matches are eligible.

   A Service Plan cannot combine a physical GPU type and a Segment Type. The picker groups Segment Types beneath their parent physical GPU type so the relationship is visible. GPU types with no defined Segment Types appear as standalone selectable rows for whole-card passthrough only.

#. Save the Service Plan and configure its Group and Tenant access.

GPU-bearing plans remain visible in the provisioning wizard even when no live capacity is available. Provisioning fails fast if the selected HVM Cluster has fewer matching, assignable devices than the requested GPU Count. Morpheus does not auto-create VFs or program profiles on demand.

Provision or Manually Assign a vGPU
-----------------------------------

When a GPU-bearing Service Plan is selected during provisioning, Morpheus filters eligible Hosts for matching devices, reserves pre-created VFs, and assigns them to the VM. Morpheus does not create a VF or program a profile on demand. Prepare enough matching VFs before exposing the plan to consumers.

To assign a pre-created VF manually:

#. Open the HVM Host's :guilabel:`Devices` tab and expand the physical GPU.
#. From the programmed VF's Actions menu, select :guilabel:`Assign Device`.
#. Select a VM on that Host and click :guilabel:`Execute`.

GPU devices are not hot-pluggable in this workflow. Assigning or removing a device from a running VM can stop, redefine, and restart the VM. Schedule the operation as disruptive work.

Install and License the Guest Driver
------------------------------------

Install the NVIDIA vGPU guest driver from the same NVIDIA vGPU software release downloaded for the Host. Guest drivers are included with the Linux KVM package on the NVIDIA Licensing Portal. Follow NVIDIA's Windows or Linux guest instructions and verify the vGPU with ``nvidia-smi`` inside the VM.

NVIDIA vGPU licensing is separate from the Morpheus appliance license. NVIDIA vGPU software automatically selects the license edition from the profile series:

.. list-table::
   :widths: 20 35 45
   :header-rows: 1

   * - Profile Series
     - NVIDIA License
     - Typical Use
   * - Q-series
     - NVIDIA RTX Virtual Workstation (vWS)
     - Professional graphics and workstation applications
   * - B-series
     - NVIDIA Virtual PC (vPC), or vWS
     - Business virtual desktops
   * - A-series
     - NVIDIA Virtual Applications (vApps)
     - Application streaming and session-based workloads

The customer is responsible for purchasing sufficient NVIDIA entitlements and complying with NVIDIA licensing terms. Configure a Cloud License Service (CLS) or Delegated License Service (DLS) instance in NVIDIA License System, generate a Client Configuration Token, and deploy the token inside each guest VM according to the NVIDIA `Client Licensing User Guide <https://docs.nvidia.com/vgpu/latest/grid-licensing-user-guide/index.html>`_.

For current NVIDIA releases, licensed clients require the NVIDIA guest driver, a valid token, and network access to the CLS or DLS service instance. NVIDIA documents TCP ports 443 and 80 for current CLS/DLS client communication. On Linux, configure ``FeatureType=1`` for NVIDIA vGPU and place the token in ``/etc/nvidia/ClientConfigToken``; on Windows, place it in the NVIDIA vGPU licensing ClientConfigToken directory. Restart the NVIDIA licensing service as directed by NVIDIA, then verify license acquisition in the guest.

.. note::

   Morpheus does not store the NVIDIA client token or display NVIDIA license checkout status. Automate token deployment as part of secure image preparation or provisioning automation without placing the token in public scripts, logs, or broadly shared images.

Lifecycle and Placement Constraints
-----------------------------------

- A vGPU VF is tied to its physical GPU and Host. Morpheus 9.1 does not provide vGPU live migration or automatic cross-Host VF remapping.
- A VM with an assigned GPU device is not eligible for normal HVM live migration or automatic evacuation. Remove the assignment or provide an approved cold-migration procedure before Host maintenance.
- A programmed VF that is assigned to or reserved for a VM cannot have its Segment Type destroyed. Unassign it from the VM before destroying the Segment Type.
- Segmentation cannot be disabled, and homogeneous/heterogeneous mode cannot be switched, while any child VF is assigned to a VM. Unassign all VFs first. You do not need to destroy every programmed Segment Type to change modes or disable segmentation.
- Whole-GPU passthrough is unavailable while segmentation is enabled on the physical GPU.
- Service Plan capacity is based on currently discovered assignable devices. Keep spare matching VFs on other Hosts for planned maintenance, but do not assume automatic failover will reattach them.
- NVIDIA MIG/mdev slicing and non-NVIDIA GPU slicing are not supported by this Morpheus 9.1 workflow.

Troubleshooting
---------------

- **No segmentation actions:** Confirm the GPU maps to a segmentation-capable Morpheus device type, remains attached to the Host driver, and the user has Full Server Devices permission.
- **No virtual functions after enabling segmentation:** Verify SR-IOV, ARI, the NVIDIA vGPU Manager services, and Host driver logs, then refresh Host devices.
- **No creatable Segment Types:** Confirm the driver reports creatable vGPU types for the physical GPU, current mode, and remaining framebuffer. A seeded profile is not necessarily available on every driver release.
- **Provisioning reports insufficient GPUs:** Pre-create enough VFs with the exact Segment Type selected by the Service Plan on eligible Hosts.
- **VM starts without usable NVIDIA acceleration:** Install a compatible guest driver, confirm the VF is visible, and inspect ``nvidia-smi`` and guest driver logs.
- **Guest performance is degraded:** Confirm that the VM acquired the correct NVIDIA license from CLS or DLS. NVIDIA degrades licensed features when a software-enforced license is not acquired.
- **Mode change or disable segmentation is blocked:** Unassign all child VFs from their VMs. You do not need to destroy every Segment Type first — only VM assignments block the operation.

For driver, profile, guest OS, licensing, and known-issue details, use the NVIDIA documentation for the exact installed vGPU software release rather than the unversioned latest behavior alone.
