Migrations Requirements
-----------------------

This section contains requirements and recommendations that will ensure migrations run successfully. Keep an eye on this section as some requirements will change as this feature is updated over time to become more flexible.

General Requirements
^^^^^^^^^^^^^^^^^^^^

- HVM Hosts must be upgraded to Agent version 2.10.0 at minimum. To upgrade the HVM Host Agent, navigate to the host detail page, open the ACTIONS menu, and select "Upgrade Agent." If this is unsuccessful, you may instead select "Download Agent Script" to download a shell script which may be run manually on the HVM Host. These download scripts are specific to the HVM Host so an individual install script would need to be downloaded for each HVM Host and run on the correct HVM Host.
- HVM Hosts must be able to reach ESXi hosts and vCenter on the target VMware vCenter Cloud via the Management Network
- The source VMs must be running for the preparation phase of the migration to complete successfully. If VMs are not running, they will automatically be restarted

First Release Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^

This section includes requirements for the current version of the migration feature which are subject to change and improvement as road-mapped enhancements are included with subsequent versions of the product.

- If the target datastore is GFS2 or NFS, migrations will be "thin" QCOW2 rather than "thick" to reduce overhead and on-disk footprint. Other target datastore types must have enough "thick" space for each VM
- VMs will power down prior to the transfer meaning service of the source workload will be disrupted during the transfer
- VirtIO / VirtIO-SCSI target storage must be supported by the source VM
- Currently supported operating systems: RedHat, CentOS, Rocky, Alma, SUSE, Ubuntu, Debian, Windows (currently requires manual preparation steps described below)
- Source VMs must be capable of getting the ``qemu-guest-tools`` or ``qemu-guest-agent`` package installed.
- RDM (Raw Device Mappings) are not yet supported
- Source VMs must not have any attached ISOs or cdroms. These are not supported and the migration will fail.

Recommendations
^^^^^^^^^^^^^^^

- Batch limits and bandwidth limitations testing is still in progress. It's currently recommended you migrate no more than 20 VMs at a time. Testing is still ongoing to determine the upper limits of migrations and this recommendation is likely to increase over time
- Begin using this feature with a smaller migration than the limit to make sure your workloads are moving correctly
- When migrating to NFS-backed datastores, setting ``async`` on the NFS server may improve performance
