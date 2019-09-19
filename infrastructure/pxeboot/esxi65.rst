Adding ESXi 6.5 PXE Image
-------------------------

When adding a PXE Image for ESXi 6.5, a few requirements must be met for a successful PXE Boot.

- Image/iso must be expanded and added to a Bucket or File Share in Morpheus
- The ESXi ``BOOT.CFG`` needs to be edited to be PXE compatible:
  - The ESXi ``BOOT.CFG`` uses lowercase file references, while the actual file names are CAPS. Change all file reference names to CAPS.
  - The ESXi ``BOOT.CFG`` references empty files, which while cause PXE checksum failures, and the file references need to be removed.
  - The ESXi ``BOOT.CFG`` has ``\``'s in front of all filenames that need to be removed

Create ESXi 6.5 PXE Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Extract ESXi 6.5 iso file
#. Update ``BOOT.CFG`` file.

   #. Delete ``jumpstrt.gz``, ``useropts.gz``, and ``features.gz`` references.
      - These are blank by default and cause PXE checksum to fail
   #. Change file references to ALL CAPS to match file names.
   #. Remove ``/``'s in front of file references in ``BOOT.CFG``
      - example: ``sed -i 's/\///g' BOOT.CFG``

   Example updated BOOT.CFG

   .. code-block:: bash
      :name: Updated BOOT.CFG

      bootstate=0
      title=Loading ESXi installer
      timeout=5
      kernel=TBOOT.B00
      kernelopt=runweasel
      MODULES=B.B00 --- K.B00 --- CHARDEVS.B00 --- A.B00 --- USER.B00 --- UC_INTEL.B00 --- UC_AMD.B00 --- SB.V00 --- S.V00 --- ATA_LIBA.V00 --- ATA_PATA.V00 --- ATA_PATA.V01 --- ATA_PATA.V02 --- ATA_PATA.V03 --- ATA_PATA.V04 --- ATA_PATA.V05 --- ATA_PATA.V06 --- ATA_PATA.V07 --- BLOCK_CC.V00 --- CHAR_RAN.V00 --- EHCI_EHC.V00 --- ELXNET.V00 --- HID_HID.V00 --- I40EN.V00 --- IGBN.V00 --- IMA_QLA4.V00 --- IPMI_IPM.V00 --- IPMI_IPM.V01 --- IPMI_IPM.V02 --- IXGBEN.V00 --- LPFC.V00 --- LSI_MR3.V00 --- LSI_MSGP.V00 --- LSI_MSGP.V01 --- MISC_CNI.V00 --- MISC_DRI.V00 --- MTIP32XX.V00 --- NE1000.V00 --- NENIC.V00 --- NET_BNX2.V00 --- NET_BNX2.V01 --- NET_CDC_.V00 --- NET_CNIC.V00 --- NET_E100.V00 --- NET_E100.V01 --- NET_ENIC.V00 --- NET_FCOE.V00 --- NET_FORC.V00 --- NET_IGB.V00 --- NET_IXGB.V00 --- NET_LIBF.V00 --- NET_MLX4.V00 --- NET_MLX4.V01 --- NET_NX_N.V00 --- NET_TG3.V00 --- NET_USBN.V00 --- NET_VMXN.V00 --- NHPSA.V00 --- NMLX4_CO.V00 --- NMLX4_EN.V00 --- NMLX4_RD.V00 --- NMLX5_CO.V00 --- NTG3.V00 --- NVME.V00 --- NVMXNET3.V00 --- OHCI_USB.V00 --- PVSCSI.V00 --- QEDENTV.V00 --- QFLE3.V00 --- QFLGE.V00 --- QLNATIVE.V00 --- SATA_AHC.V00 --- SATA_ATA.V00 --- SATA_SAT.V00 --- SATA_SAT.V01 --- SATA_SAT.V02 --- SATA_SAT.V03 --- SATA_SAT.V04 --- SCSI_AAC.V00 --- SCSI_ADP.V00 --- SCSI_AIC.V00 --- SCSI_BNX.V00 --- SCSI_BNX.V01 --- SCSI_FNI.V00 --- SCSI_HPS.V00 --- SCSI_IPS.V00 --- SCSI_ISC.V00 --- SCSI_LIB.V00 --- SCSI_MEG.V00 --- SCSI_MEG.V01 --- SCSI_MEG.V02 --- SCSI_MPT.V00 --- SCSI_MPT.V01 --- SCSI_MPT.V02 --- SCSI_QLA.V00 --- SHIM_ISC.V00 --- SHIM_ISC.V01 --- SHIM_LIB.V00 --- SHIM_LIB.V01 --- SHIM_LIB.V02 --- SHIM_LIB.V03 --- SHIM_LIB.V04 --- SHIM_LIB.V05 --- SHIM_VMK.V00 --- SHIM_VMK.V01 --- SHIM_VMK.V02 --- UHCI_USB.V00 --- USB_STOR.V00 --- USBCORE_.V00 --- VMKATA.V00 --- VMKPLEXE.V00 --- VMKUSB.V00 --- VMW_AHCI.V00 --- XHCI_XHC.V00 --- EMULEX_E.V00 --- WEASELIN.T00 --- ESX_DVFI.V00 --- ESX_UI.V00 --- LSU_HP_H.V00 --- LSU_LSI_.V00 --- LSU_LSI_.V01 --- LSU_LSI_.V02 --- LSU_LSI_.V03 --- NATIVE_M.V00 --- RSTE.V00 --- VMWARE_E.V00 --- VSAN.V00 --- VSANHEAL.V00 --- VSANMGMT.V00 --- TOOLS.T00 --- XORG.V00 --- IMGDB.TGZ --- IMGPAYLD.TGZ
      BUILD=
      updated=0


#. Add expanded iso contents to Morpheus Bucket or File share.

   The iso contents can be added to the bucket/file share form morpheus, or already exist in the bucket/file share.

   #. Navigate to ``Infrastructure -> Storage``
   #. Select Bucket or File Share Tab
   #. Select target Bucket or File Share
      #. If a bucket or File Share does not exist, select :guilabel:`+ ADD` to create one.
   #. If the iso contents are already in the file share/bucket, skip to next step
      #. To add 6.5 iso contents, click :guilabel:`+ ADD` and drag the expanded ESXi ISO folder to the upload modal
      #. One call files have been uploaded, select :guilabel:`DONE`
   #. Note the path to the ESXi 6.5 files, relative to the bucket/file share.
       - For example, the screenshot below shows an iso expanded into a folder called ``VMware-6.5.0`` which was added to ``pxe-images`` folder inside ``morpheus-ui local images`` local file share. The path to the files from the file share is ``/pxe-images/VMware-6.5.0/``

       .. image:: /images/infrastructure/boot/ESXi650fileshare.png

   #. The Bucket or File Share and path to the iso files will be used when adding a PXE image.


#. Create PXE Image

   #. Navigate to ``Infrastructure -> Boot``
   #. Select Images tab
   #. Select :guilabel:`+ ADD IMAGE`
   #. Populate the following:

      NAME
        Name of the Image in Morpheus
      OPERATING SYSTEM
        Select ``esxi 6``
      MINIMUM MEMORY
       n/a leave default ``0``
      MENU
       Paste in PXE Menu
        Example PXE 6.5.0 Menu:

        .. important:: Ensure the case of file references match actual file names.


        .. code-block:: bash
           :name: PXE 6.5.0 Menu

         DEFAULT vesamenu.c32
         TIMEOUT 300
         ONTIMEOUT esxi
         PROMPT 0
         MENU INCLUDE pxelinux.cfg/pxe.conf
         NO ESCAPE 1
         LABEL local
           menu LABEL Boot to local disk
           localboot 0
           TEXT HELP
           Boot to local hard disk
           ENDTEXT
         LABEL esxi
           menu LABEL ESXI 6.5.0 u1
           kernel tftp://${bootUrl}/image/${imageId}/MBOOT.C32
           append -c tftp://${bootUrl}/image/${imageId}/BOOT.CFG ks=${answerFile}
           TEXT HELP
             Boot the ESXI 6.5.0 u1 install
           ENDTEXT
         MENU END

      BUCKET
       Select the Bucket or File Share from step 2.3
      CLOUD-INIT USER DATA
       N/A
      IMAGE PATH
       Enter the path to the iso files relative to the Bucket or File Share, eg ``/pxe-images/VMware-6.5.0/``

      #. Select :guilabel:`SAVE CHANGES`

#. Your ESXi 6.5 PXE image is ready to be added to a mapping.
