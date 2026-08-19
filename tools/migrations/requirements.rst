Requirements
------------

This section covers requirements for successful migrations from VMware vCenter to HVM Clusters.

Infrastructure Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **HVM Agent version 2.10.0+** — HVM Hosts must be running Agent version 2.10.0 or later. To upgrade, navigate to the host detail page, open the ACTIONS menu, and select "Upgrade Agent." If unsuccessful, select "Download Agent Script" to download a host-specific shell script for manual installation.
- **Name resolution** — If the ESXi hosts are registered in vCenter by fully qualified domain name (FQDN), every participating HVM Host must be able to resolve each ESXi FQDN. From each HVM Host, run ``getent hosts <esxi-fqdn>`` for every source ESXi host. Correct the DNS or host records before migration if a name does not resolve.
- **Network connectivity** — Separately from name resolution, HVM Hosts must be able to reach ESXi hosts and vCenter on the source VMware Cloud via the management network (HTTPS, port 443).
- **Source VMs must be running** — The preparation phase requires the source VM to be powered on. If a VM is powered off, it will be automatically started during the precheck phase.

Source VM Requirements
^^^^^^^^^^^^^^^^^^^^^^

- Source VMs must be capable of having ``qemu-guest-tools`` or ``qemu-guest-agent`` installed (Linux) or VirtIO guest tools (Windows)
- Source VMs **must not** have any attached ISOs or CD-ROMs — detach these before migration or the transfer will fail
- RDM (Raw Device Mappings) are not supported
- VirtIO / VirtIO-SCSI storage must be supported by the guest OS kernel (Linux guests with standard kernels meet this requirement; Windows guests have drivers injected automatically)

Storage Considerations
^^^^^^^^^^^^^^^^^^^^^^

- **GFS2 and NFS targets** — Migrations produce thin-provisioned QCOW2 images, minimizing on-disk footprint
- **Block device targets** (local, Ceph RBD) — Migrations write raw format; ensure the target has sufficient capacity for the full virtual disk size
- **Ceph RBD** — RBD images are mapped to local block devices during transfer and unmapped after completion

Recommendations
^^^^^^^^^^^^^^^

- Start with a small test migration (1–3 VMs) to validate network connectivity, storage performance, and guest OS compatibility in your environment
- Schedule large migrations during maintenance windows — source VMs are powered down during the transfer phase
- Ensure adequate bandwidth between HVM hosts and ESXi hosts — transfer speed is directly proportional to available network throughput
- For Windows workloads, verify the source VM has internet access or ensure the VirtIO ISO is available in a vCenter datastore (the automated driver injection uses network download first, falling back to ISO)
