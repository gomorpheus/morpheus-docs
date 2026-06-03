Configuring Windows Workloads (Windows 2022 or later) for Migration
--------------------------------------------------------------------

Migrating Windows workloads from VMware vCenter Clouds to HVM Clusters using the bulk Migrations feature requires some initial configurations checks. This section goes through an example preparation process for a Windows VM running on vCenter.

This guide makes the following assumptions about the workload to be migrated:

- Configured to boot as EFI or BIOS
- Virtualization Based Security (VBS) is enabled
- Secure Boot is enabled
- Trusted Platform Module (TPM) is disabled
- The VM has access to the recovery partition (if not, a Windows Recovery Environment disc or installation media may be required to access some of the menus referenced in this section)

Inject VirtIO Drivers
^^^^^^^^^^^^^^^^^^^^^

To begin, restart the VMware Windows guest in the `Windows Recovery Environment (Windows RE) <https://support.microsoft.com/en-us/windows/windows-recovery-environment-0eb14733-6301-41cb-8d26-06a12b42770b>`_. In Windows RE, choose a keyboard layout if prompted. Then, select the **Troubleshoot** option. From the Troubleshoot menu, select **Command Prompt**.

Within the Command Prompt session, enter **diskpart** using this command: ``diskpart``. Check the disks that are available with ``list disk``. At this point, you may receive the message that "There are no fixed disks to show." or the disk with Windows OS might not be listed. If that is the case, follow the steps in the next section to mount the drives. If that is not the case, skip to the following section to continue the process of injecting the VirtIO drivers.

Mounting the Drives
^^^^^^^^^^^^^^^^^^^

From vCenter, mount the VMware Tools installer to the VM using the "Install VMware Tools..." option (**Actions > Guest OS > Install VMware Tools...**). Then, back in diskpart, use the following command to find the CD/DVD-ROM drive letter: ``list volume``. Make note of the CD-ROM drive letter, which in the case of this example is drive "D." Exit diskpart with the ``exit`` command.

Enter the following command to load the storage drivers which will enable you to see the hard disks: ``drvload "D:\Program Files\VMware\VMware Tools\Drivers\pvscsi\Win10\amd64\pvscsi.inf"``. Note that the prior command references Windows 10 as the operating system but choose the most appropriate or the latest available. It also references drive "D" which may vary from case to case.

With the driver loaded, once again confirm the disks are mounted with ``diskpart`` and ``list disk``. They're now mounted but the partitions/volumes need drive letters so, while still in diskpart, list the volumes with: ``list volume``. In this example case, "Volume 1" is the primary Windows volume. Select the volume and assign a drive letter, in the example case the assigned letter will be "C": ``select volume 1`` and ``assign letter=c``. Check your work by listing the volumes again, the primary Windows volume should be assigned the correct drive letter: ``list volume``.

Exit diskpart once again (``exit``) and unmount the VMware Tools installer from the VM back in the vCenter console (**Actions > Guest OS > Unmount VMware Tools Installer**).

Inject VirtIO drivers (cont.)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download the `latest <https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/latest-virtio/>`_ or `stable <https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/>`_ VirtIO drivers ISO to your local workstation. The latest is recommended but often they are the same. Add the ISO to vCenter either by uploading it to a datastore or to the Content Library. Still in vCenter, mount the ISO using a CD-ROM device on the VM and make sure it's connected. Enter the following commands to inject the VirtIO storage drivers into the Windows boot-start drivers from the mounted ISO: ``dism /image:C:\ /add-driver:D:\viostor\2k22\amd64\viostor.inf`` and ``dism /image:C:\ /add-driver:D:\vioscsi\2k22\amd64\vioscsi.inf``. Note once again that the OS volume will not be assigned the "C" drive letter and the CD-ROM device will not be assigned the "D" drive letter in every case. Similarly, in this example "2k22" is used but that won't be appropriate in every case. If successful, a message will be received that the driver packages were successfully installed. Close the Command Prompt window and click **Continue** to boot Windows once again.

Prepare the OS
^^^^^^^^^^^^^^

Once logged back in, install the VirtIO drivers in the OS using the ISO, which is still mounted, by navigating to the CD-ROM/DVD-ROM drive. Install ``virtio-win-gt-x64.msi`` and ``virtio-win-guest-tools.exe`` from the root of the ISO. Maintain all default selections during the installation. Next, unmount any ISOs still attached to the VM, either by ejecting in Windows or by setting the CD-ROM drive to "Client Device" in vCenter.

Now, shut down the VM. Keep in mind that the VMware Cloud integration may be configured to automatically maintain power state of associated VMs. Navigate to :menuselection:`Infrastructure --> Clouds` and edit the Cloud. Make note of the "AUTOMATICALLY POWER ON VMS" configuration. If checked, you will need to shut down the VM via the product UI tools rather than from the vCenter console or from within the guest OS. Alternatively, you could uncheck "AUTOMATICALLY POWER ON VMS", save changes to the Cloud, and then power down the VM from vCenter or from the guest OS but bear in mind changing this configuration would affect all VMs associated with the Cloud in the product.

Migrating
^^^^^^^^^

This completes the preparation steps. From here, create a new Migration Plan that includes the prepared VM and run it. Take a look at the previous section for more information on creating and running Migration Plans.

Post-Conversion
^^^^^^^^^^^^^^^

As a final note, bear in mind that the migration tool does not uninstall VMware Tools following conversion, which can lead to start-up errors being surfaced in migrated VMs. In some cases, the VMware Tools installation may become corrupted which prevents simply uninstalling using the Control Panel.

To prevent VMware Tools from executing at startup, within the Windows guest navigate to :menuselection:`Settings --> Apps --> Startup` and turn off VMware Tools Core Service.

Additionally, you can attempt to uninstall VMware Tools completely using Microsoft recommended processes and tooling for uninstalling stuck programs. See `this article <https://support.microsoft.com/en-us/topic/fix-problems-that-block-programs-from-being-installed-or-removed-cca7d1b6-65a9-3d98-426b-e9f927e1eb4d>`_ from the Microsoft Support for procedure and links to a helpful tool.
