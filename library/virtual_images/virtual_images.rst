Virtual Images
==============

Overview
--------

The Virtual Image section displays a list of all images, local and synced, that are available to deploy. |morpheus| includes a rich catalog of pre-configured System Images available for every cloud type. User Images are automatically synced from Cloud Integrations and added to the Virtual Images section. Images can also be uploaded directly into |morpheus| via local file or url. Amazon and Azure Marketplace images can also be added to the Virtual Images Section.

Understanding the process of prepping images for consumption in |morpheus| is a very important step toward building an effective |morpheus| environment. In addition to the information contained in this section on Virtual Images, it may be helpful to see a complete image prep example walkthrough. Our getting started guide for |morpheus| and VMware includes `a section on preparing images <https://docs.morpheusdata.com/en/latest/getting_started/guides/vmware_guide.html#prepping-an-image>`_ that may provide a helpful example.

.. TIP:: |morpheus| includes a wide catalog of system image types as examples to show how the product can be used and to give users a starting point for implementing their own library. The included images are not intended to be production-ready images. |morpheus| always recommends its users create their own gold images which meet their required specifications.

.. IMPORTANT:: Invalid Image Settings cause provisioning failures. |morpheus| syncs in as much meta-data as possible for synced images, but additional configuration may be needed to ensure successful provisioning.

.. WARNING:: Cloud-init is enabled by default for all Linux images. If your Linux image does not have Cloud-init installed, `Cloud-init Enabled` must be unchecked before provisioning the image or it will fail immediately.

Image Types
-----------

|morpheus| provides a vast *System Image* repo with pre-configured images for every Cloud. All other images are *User Images*. User images can be added directly to |morpheus|, or automatically synced from integrated clouds. It is important to configure synced User Images for metadata, including specifying the Platform and User Credentials, prior to provisioning. Provisioning a User Image that has not been configured may result in failed provisioning.

.. IMPORTANT:: Synced User Images need to be configured prior to provisioning.

Configuring Virtual Images
--------------------------

System Images
^^^^^^^^^^^^^

System Virtual Images are pre-configured with metadata and have Cloud-Init or Cloudbase-Init installed. These images are ready to be provisioned with no configuration necessary, however it is required to populate :menuselection:`Administration --> Settings --> Provisioning`, Cloud-Init section, with user data as well as User Profile(s) users data when creating additional users prior to provisioning, as the user data from these sections is required when provisioning System provided Virtual Images.

.. NOTE:: System Images settings are not editable.

User Images
^^^^^^^^^^^

Typically |morpheus| does not have sufficient metatdata to successfully provision synced User Images. After integrating clouds and User Images have synced, it is highly recommended to configure the images prior to provisioning.

**To edit and configure an existing Virtual Image:**

#. Select the pencil icon at the right of any row on the Virtual Images list page, or click :guilabel:`EDIT` on a Virtual Image detail page.
#. Configure the following on the Image:

   Name
     Name of the Virtual Image in |morpheus|. This can be changed from the name of the image, but editing will not change the name of the actual image
   Operating System
     Specifies the platform and OS of the image. All Windows images will need to have the operating system specified on the Virtual Image, as |morpheus| will assign Linux as the platform for all images without an operating system specified
   Minimum Memory
    The Minimum Memory setting will filter available Service Plan options during provisioning. Service Plans that do not meet the minimum value set on the Virtual Image will not be provided as Service Plan choices
   Cloud Init Enabled?
     On by default, uncheck for any Image that does not have Cloud-Init installed
   Install Agent?
     On by default, uncheck to skip Agent install. Note this will result in the loss of utilization statistics, logs, script execution, and monitoring. (Some utilization stats are still collected for Agent-less hosts and VMs depending on the cloud)
   Username
     Existing username on the image for authentication. Can be left blank if global default credentials are configured in :menuselection:`Administration --> Settings --> Provisioning` (separate defaults exist for Linux and Windows). If Cloud-Init or Guest Customizations are used, credentials from :menuselection:`Administration --> Settings --> Provisioning` and User Settings are applied. If credentials are defined on the image and Cloud-Init is enabled, |morpheus| will add that user during provisioning, so ensure that user does not already exist on the image (such as ``root``). For Windows, do not define any user other than Administrator. |morpheus| recommends running Guest Customizations for all Windows Images, which is required when joining Domains as the SID will change.
   Password
     Password for the user on the image if username is populated. Can be left blank if global defaults are set in :menuselection:`Administration --> Settings --> Provisioning`.
   Bucket
    Location where the Virtual Image will be stored. Default Virtual Image Storage location is ``/var/opt/morpheus/morpheus-ui/vms``. Additional Storage Providers can be configured in ``Infrastructure > Storage``
   Cloud-Init User Data
     Accepts what would go in ``runcmd`` and can assume Bash syntax. Example use: Script to configure satellite registration at provision time
   Permissions
    Set Tenant permissions in a multi-tenant |morpheus| environment. Select private visibility and select specific Tenants to which the Virtual Image will be made available. Select public visibility to share the Virtual Image with all Tenants
   Auto Join Domain?
    Enable to have Instances provisioned with this image auto-join configured domains (Windows only, domain controller must be configured in ``Infrastructure > Network`` and the configured domain set on the provisioned to Cloud or Network)
   VirtIO Drivers Loaded?
    Enable if VirtIO Drivers are installed on the image for provisioning to KVM-based hypervisors
   FIPS Compliant Image?
    When selected, |morpheus| will install the FIPS-compliant |morpheus| Agent package
   VM Tools Installed?
    On by default, uncheck if guest tools are not installed on the Virtual Image (VMware Tools for VMware, QEMU Guest Agent for HVM). |morpheus| will skip network wait during provisioning when deselected
   Force Guest Customization?
    Forces guest customizations to run during provisioning. On VMware/VME, transfers unattend via VMware Tools and reboots. On HVM, injects unattend via the guest agent. Requires guest tools to be installed on the image.
   Trial Version
    Enable to automatically re-arm the expiration on Windows Trial Images during provisioning
   Enabled Sysprep?
    Applicable to multiple Clouds, including VMware vCenter, SCVMM, Nutanix, Hyper-V, KVM, and Google GCP. Enable if the Windows Image has been sysprepped. If enabled, |morpheus| will inject ``unattend.xml``

3. Click :guilabel:`Save Changes`

.. NOTE:: Cloud-Init is enabled by default on all images. Images without Cloud-Init installed must have the ``cloud-init`` flag disabled on the Virtual Image setting or Provisioning may fail.

.. IMPORTANT:: |morpheus| does not validate or restrict image uploads to certain file types and any type of file may be uploaded as a Virtual Image. For security purposes, these files are stored in a non-executable state so users need not worry about potentially dangerous file types being uploaded (ex. executables).

Provisioning Images
-------------------

When provisioning a system image, |morpheus| will stream the image from Amazon S3 to the target Cloud if the image is not local to the Cloud.

When using images that already exist in the destination Cloud, such as synced, marketplace, or previously copied images, no image stream from S3 through the |morpheus| Appliance to the destination cloud will take place.

.. NOTE:: The |morpheus| Appliance must be able to download from Amazon S3 when provisioning system images.

.. NOTE:: The |morpheus| Appliance must be able reach and resolve the destination Host when provisioning System Images or uploaded Images for the first time. This included being able to resolve ESXi host names in VMware vCenter clouds, and reach the destination ESXi host over port 443.

Add Virtual Image
-----------------

Virtual Images can be upload to |morpheus| from local files or URL's. Amazon and Azure Marketplace metadata can also be added to the Virtual Images library, enabling the creation of custom catalog Instance Type from Marketplace images (no image is transferred to |morpheus| when adding Marketplace images).

.. WARNING:: Be conscious of your Storage Provider selection. The default Storage Provider is the |morpheus| Appliance at ``/var/opt/morpheus/morpheus-ui/vms``. Uploading large images to the |morpheus| Appliance when there is inadequate space will cause upload failures and impact Appliance functionality. Ensure there is adequate space on your selected Storage Provider. Additional Storage Provider can be added at `Infrastructure > Storage`, which can be configured as the default Virtual Image Store or selected when uploading Images.

.. NOTE:: VMware-type OVF Virtual Images do not support mounted ISO uploads

To Add Virtual Image:

1. Select :guilabel:`+ Add` in the Virtual Images page.
2. Select Image format:

   * Alibaba
   * Amazon AMI
   * Azure Marketplace
   * Digital Ocean
   * ISO
   * PXE Boot
   * QCOW2
   * RAW
   * VHD
   * VMware (vmdk/ovf/ova)

3. Configure the Virtual Image settings (see `Configuring Virtual Images`_ above for a description of each option).

4. Upload Image

    Images can be uploaded by File or URL:
      *File*
       Drag and Drop the image file, or select :guilabel:`Add File` to select the image file.
      *Url*
       Select the URL radio button, and enter URL of the Image.

    .. NOTE:: The Virtual Image configuration can be saved when using a URL and the upload will finish in the background. When selecting/drag and dropping a file, the image files must upload completely before saving the Virtual Image record or the Image will not be valid.

5. Save Changes.

.. NOTE:: Default Storage location is ``/var/opt/morpheus/morpheus-ui/vms``. Additional Storage Providers can be configured in `Infrastructure > Storage`. Ensure local folders are owned by morpheus-app.morpheus-app if used.

.. WARNING:: Provisioning will fail if `Cloud init Enabled` is checked and Cloud-Init is not installed on the Image.

.. NOTE:: Existing Image credentials are required for Linux Images that are not Cloud-Init enabled and for Windows Images when Guest Customizations are not used. Cloud-Init and Windows user settings need to be configured in :menuselection:`Administration --> Settings --> Provisioning` when using Cloud-Init or Guest Customizations and new credentials are not set on the Virtual Image.

.. _multi-disk-qcow2-images-for-hvm-kvm:

Multi-Disk QCOW2 Images for HVM/KVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HVM/KVM supports Virtual Images containing multiple QCOW2 disks. Upload every QCOW2 file and a JSON manifest named exactly ``metadata.json`` as files on the same Virtual Image. The manifest maps each QCOW2 file to its guest device, disk size, and order.

Without ``metadata.json``, |morpheus| treats a QCOW2 Virtual Image as a single-disk image even when multiple QCOW2 files have been uploaded.

The following example defines a 50 GiB boot disk and a 100 GiB data disk:

.. code-block:: json

   {
     "disks": [
       {
         "file": "root.qcow2",
         "capacity": 53687091200,
         "guestDeviceName": "vda",
         "position": 0,
         "name": "root",
         "boot": true
       },
       {
         "file": "data.qcow2",
         "capacity": 107374182400,
         "guestDeviceName": "vdb",
         "position": 1,
         "name": "data"
       }
     ]
   }

.. list-table:: Multi-disk QCOW2 metadata fields
   :widths: 24 14 62
   :header-rows: 1

   * - Field
     - Required
     - Description
   * - ``disks``
     - Yes
     - Top-level array containing one object for each uploaded disk.
   * - ``file``
     - Yes
     - Exact, unique filename of the uploaded QCOW2 file, including the ``.qcow2`` extension. Filename matching is case-insensitive.
   * - ``capacity``
     - Recommended
     - Virtual disk capacity in bytes. Convert GiB to bytes with ``GiB × 1073741824``. For example, 50 GiB is ``53687091200`` bytes.
   * - ``guestDeviceName``
     - Recommended
     - Device name presented to the guest, such as ``vda`` for the root disk and ``vdb`` for the first data disk.
   * - ``position``
     - Recommended
     - Zero-based disk order. Use unique, sequential values beginning with ``0``.
   * - ``name``
     - No
     - Descriptive source-disk label, such as ``root`` or ``data``. The displayed image-volume name can be derived from the Virtual Image name instead.
   * - ``boot``
     - No
     - Set to ``true`` on the boot disk. If no disk is marked as bootable, |morpheus| selects the first disk after sorting.
   * - ``unitNumber``
     - No
     - Unit number on a referenced storage controller. Omit for a basic VirtIO disk set.
   * - ``storageController``
     - No
     - Controller reference used when a specific imported controller topology must be preserved. It requires a matching object in a top-level ``storageControllers`` array. Omit both for a basic VirtIO disk set.

Disk records are sorted by controller bus number, unit number, and then ``position``. For a basic manifest without controller fields, ``position`` determines the order. Use distinct filenames, positions, and guest device names to avoid ambiguous mappings.

Only ``disks`` and a resolvable ``file`` value are strictly needed for file discovery, but include the recommended fields shown above so |morpheus| can build predictable disk capacities, devices, and ordering.

To upload a multi-disk QCOW2 image:

#. Navigate to |LibVir| and click :guilabel:`+ ADD`.
#. Select :guilabel:`QCOW2` as the image format.
#. Configure the Virtual Image, including Operating System, Cloud-Init, Agent, credentials, VirtIO, and guest tools settings as appropriate for the image.
#. Select **File** upload. Multi-disk upload requires adding multiple files to the same Virtual Image.
#. Upload every referenced ``.qcow2`` file and wait for each upload to complete.
#. Upload ``metadata.json`` last. Uploading the manifest triggers disk-map processing, so all referenced disk files must already be present.
#. Confirm the file list contains ``metadata.json`` and every filename referenced by its ``disks`` array.
#. Save the Virtual Image and wait for its status to become Active.
#. Open the Virtual Image details and verify that every disk is present with the expected capacity, device order, and root disk before provisioning.

.. IMPORTANT:: Do not upload ``metadata.json`` before the QCOW2 files. If the manifest is processed while referenced files are missing, the resulting disk records can be incomplete. Remove and re-upload the manifest after all disk files are present, or recreate the Virtual Image if the stored volume map is incorrect.

Troubleshooting multi-disk uploads:

- **Only one disk is shown:** Confirm the file is named exactly ``metadata.json``, contains a top-level ``disks`` array, and was uploaded after all QCOW2 files.
- **A disk is missing:** Confirm its ``file`` value exactly matches a unique uploaded filename and includes the ``.qcow2`` extension.
- **Disk capacity is wrong:** Confirm ``capacity`` is in bytes rather than GiB. Multiply GiB by ``1073741824``.
- **Wrong disk boots:** Set ``boot`` to ``true`` on the intended root disk and ensure its ordering fields do not conflict with another disk.
- **Device order is wrong:** Use sequential ``position`` values and matching ``guestDeviceName`` values such as ``vda``, ``vdb``, and ``vdc``.
- **Manifest is ignored or the image remains invalid:** Validate the file as JSON, ensure there are no comments or trailing commas, and upload the corrected manifest after the disk files.

Virtual Image Options — Cloud Applicability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Not all Virtual Image settings apply to all cloud types. The following matrix clarifies which options have an effect depending on the target cloud. Options marked as having no effect are ignored during provisioning to that cloud type.

.. list-table::
   :widths: 25 12 12 12 12 12 15
   :header-rows: 1

   * - Option
     - HVM (KVM)
     - VMware / VME
     - AWS
     - Azure
     - Nutanix
     - Notes
   * - Cloud Init Enabled
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Must be unchecked if cloud-init is not installed on the image
   * - Install Agent
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Universal — works on all clouds
   * - Force Guest Customization
     - **Yes**
     - **Yes**
     - No effect
     - No effect
     - No effect
     - Triggers guest customization during provisioning. On VMware/VME, transfers unattend via VMware Tools and reboots. On HVM, injects unattend and triggers customization via the guest agent.
   * - VirtIO Drivers Loaded
     - **Yes**
     - No effect
     - No effect
     - No effect
     - No effect
     - HVM/KVM only. When unchecked, |morpheus| uses IDE/SATA bus instead of VirtIO.
   * - VM Tools Installed
     - **Yes**
     - **Yes**
     - No effect
     - No effect
     - No effect
     - Indicates guest tools are present (VMware Tools for VMware, QEMU Guest Agent for HVM). When unchecked, |morpheus| skips network wait during provisioning.
   * - Enabled Sysprep
     - Yes
     - Yes
     - No effect
     - No effect
     - Yes
     - Windows images. |morpheus| injects unattend.xml when enabled. Works on VMware, HVM, Nutanix, SCVMM, Hyper-V, GCP.
   * - Auto Join Domain
     - Yes
     - Yes
     - No effect
     - No effect
     - Yes
     - Windows only. Requires Network Domain with Domain Controller configured.
   * - Trial Version
     - Yes
     - Yes
     - No effect
     - No effect
     - Yes
     - Windows trial re-arm. Applicable to any on-prem cloud.
   * - FIPS Compliant Image
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Universal — controls which Agent package is installed.

.. important::

   The most common source of confusion is **Force Guest Customization** — this setting works on VMware/VME (via VMware Tools) and HVM (via the guest agent). On public clouds (AWS, Azure), customization is handled by the cloud provider's metadata service and this setting has no effect.

.. note::

   **ISO image types** — When uploading ISO images (used for manual OS installations or boot media), disable both **Cloud Init Enabled** and **Enabled Sysprep**. ISO-based images are typically booted interactively for OS installation and do not use cloud-init or sysprep-based guest customization. Leaving these options enabled on an ISO image will cause provisioning failures or unexpected behavior.

4. Upload Image
    Images can be uploaded by File or URL:
      *File*
       Drag and Drop the image file, or select :guilabel:`Add File` to select the image file.
      *Url*
       Select the URL radio button, and enter URL of the Image.

    .. NOTE:: The Virtual Image configuration can be saved when using a URL and the upload will finish in the background. When selecting/drag and dropping a file, the image files must upload completely before saving the Virtual Image record or the Image will not be valid.

5. Save Changes.

VMware - VM Templates Copies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a VMware environment, you may have a single VM template that you use across different vCenters. Uploading an image to |morpheus|, mentioned in the Add Virtual Image section, is one method to solve this. Alternatively, an organization may decide to create a VM template in one vCenter and then transfer it to other vCenters, which then could be sync’d into |morpheus|.

If all the vCenters are added as Clouds into |morpheus| and the templates are named the same in each vCenter, they will be aggregated under a single virtual image in |morpheus|. This means that as you deploy to the various vCenter Clouds in |morpheus| using this virtual image, it will choose the correct VM template to use based on the Cloud deployed to.

This eliminates the need for creating multiple Node Types for each virtual image if the templates were named differently in each vCenter. This can reduce the overhead of maintaining multiple Node Types and reduces user selections. As well, this can reduce the cloning time of VMs by avoiding network transfers of images between geographic locations, ensuring the closest VM template is selected.

|morpheus| supports VMware Content Libraries storing VM templates and syncing into |morpheus|, the same as a template in a folder. Additionally, the Content Library can be used to house the same template in multiple libraries. If they have the same name, these templates will be aggregated under a single virtual image. If the Content Library is stored on a datastore that the target host/cluster has access to, it will use that library first, to reduce the cloning time. If the Content Library is not stored in a datastore accessible by the cluster/host, a copy of the VM template will be performed to the target host/cluster instead.

.. NOTE:: VM templates are a **Data Center** level object.  The same process above applies to a single VMware cloud with multiple logical data centers.  It will not apply to clusters, as a template is not associated with a cluster, only when it is converted to a VM.
