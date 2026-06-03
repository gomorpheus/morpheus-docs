Known Limitations and Operational Considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 5 15 30 20 15 15

   * - S.No
     - Topic
     - Description
     - Impact
     - Applicability
     - Operational Guidance
   * - 1
     - SATA Controller Initialization Delay During Importing HPE ProLiant Bare Metal Servers
     - During the bare-metal server import and hardware discovery process, if a server has one or more SATA controllers with no attached SATA disks, the system waits a minimum of 5 minutes per SATA controllerbefore continuing.The wait time is cumulative and applies to each SATA controller detected without attached disks.This behavior occurs during the initial hardware probing phase, before the server becomes available for provisioning in Morpheus.
     - Increased time to complete bare-metal server discovery, import, and provisioning.Delay proportional to the number of SATA controllers present without disks.No impact once the server import process has completed.No impact when SATA controllers have SATA disks attached.
     - This condition is typically observed in lab or evaluationenvironments where SATA controllers may be present but not populated with disks.Standard production deployments are not expected to include unused SATA controllers.
     - Disabling an Embedded SATA Controller (HPE ProLiant)Reboot the server.PressF9to enterSystem Utilities.Navigate to:System Configuration→BIOS/Platform Configuration (RBSU)→PCIe Device Configuration.Foreachembedded SATA controller that is not in use:Select the controller (for example, Embedded SATA Controller #1).Change theSATA Device DisablefromAutotoDisabled.Press F12 to save the changes and exit, followed by reboot.
