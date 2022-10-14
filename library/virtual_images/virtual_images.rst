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

System Virtual Images are pre-configured with metadata and have Cloud-Init or Cloudbase-Init installed. These images are ready to be provisioned with no configuration necessary, however it is required to populate |AdmSetPro|, Cloud-Init section, with user data as well as User Profile(s) users data when creating additional users prior to provisioning, as the user data from these sections is required when provisioning System provided Virtual Images.

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
     On by default, uncheck for any Image that does not have Cloud-Init or Cloudbase-Init installed
   Install Agent?
     On by default, uncheck to skip Agent install. Note this will result in the loss of utilization statistics, logs, script execution, and monitoring. (Some utilization stats are still collected for Agent-less hosts and VMs depending on the cloud)
   Username
     Existing username on the image. This is required for authentication, unless |morpheus| is able to add user data, Cloud-Init, Cloudbase-Init or Guest Customizations. If Cloud-Init, Cloudbase-Init or Guest Customizations are used, credentials are defined in |AdmSetPro| and User Settings. If credentials are defined on the image and Cloud-Init is enabled, |morpheus| will add that user during provisioning, so ensure that user does not already exist on the image (such as ``root``). For Windows Guest Customizations, |morpheus| will set the Administrator password to what is defined on the image if Administrator user is defined. Do not define any other user than Administrator for Windows Images unless using Cloudbase-init. |morpheus| recommends running Guest Customizations for all Windows Images, which is required when joining Domains as the SID will change
   Password
     Password for the user on the image if username is populated
   Bucket
    Location where the Virtual Image will be stored. Default Virtual Image Storage location is ``/var/opt/morpheus/morpheus-ui/vms``. Additional Storage Providers can be configured in ``Infrastructure > Storage``
   Cloud-Init User Data
     Accepts what would go in ``runcmd`` and can assume Bash syntax. Example use: Script to configure satellite registration at provision time
   Create Image ID
    Select FILE to browse locally for an image or drop an image file into the dropzone. Alternatively, select URL to download the image from an accessible URL. It is recommend to configure the rest of the settings below prior to uploading the source Image File(s)
   Permissions
    Set Tenant permissions in a multi-tenant |morpheus| environment. Select private visibility and select specific Tenants to which the Virtual Image will be made available. Select public visibility to share the Virtual Image with all Tenants
   Auto Join Domain?
    Enable to have Instances provisioned with this image auto-join configured domains (Windows only, domain controller must be configured in ``Infrastructure > Network`` and the configured domain set on the provisioned to Cloud or Network)
   VirtIO Drivers Loaded?
    Enable if VirtIO Drivers are installed on the image for provisioning to KVM-based hypervisors
   FIPS Compliant Image?
    When selected, |morpheus| will install the FIPS-compliant |morpheus| Agent package
   VM Tools Installed?
    On by default, uncheck if VMware Tools (including OpenVMTools) are not installed on the Virtual Image. |morpheus| will skip network wait during provisioning when deselected
   Force Guest Customization?
    VMware only, forces guest customizations to run during provisioning, typically when provisioning to a DHCP network where guest customizations would not run by default.  This options requires that VMware Tools is installed on the image
   Trial Version
    Enable to automatically re-arm the expiration on Windows Trial Images during provisioning
   Enabled Sysprep?
    Applicable to multiple Clouds, including VMware vCenter, SCVMM, Nutanix, Hyper-V, KVM, and Google GCP. Enable if the Windows Image has been sysprepped. If enabled, |morpheus| will inject ``unattend.xml``

3. Click :guilabel:`Save Changes`

.. NOTE:: Cloud-Init is enabled by default on all images. Images without Cloud-Init or Cloudbase-Init installed must have the ``cloud-init`` flag disabled on the Virtual Image setting or Provisioning may fail.

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

3. Configure the following on the Virtual Image:

  Name
    Name of the Virtual Image in |morpheus|. This can be changed from the name of the image, but editing will not change the name of the actual image
  Operating System
    Specifies the platform and OS of the image. All Windows images will need to have the operating system specified on the Virtual Image, as |morpheus| will assign Linux as the platform for all images without an operating system specified
  Minimum Memory
   The Minimum Memory setting will filter available Service Plan options during provisioning. Service Plans that do not meet the minimum value set on the Virtual Image will not be provided as Service Plan choices
  Cloud Init Enabled?
    On by default, uncheck for any Image that does not have Cloud-Init or Cloudbase-Init installed
  Install Agent?
    On by default, uncheck to skip Agent install. Note this will result in the loss of utilization statistics, logs, script execution, and monitoring. (Some utilization stats are still collected for Agent-less hosts and VMs depending on the cloud)
  Username
    Existing username on the image. This is required for authentication, unless |morpheus| is able to add user data, Cloud-Init, Cloudbase-Init or Guest Customizations. If Cloud-Init, Cloudbase-Init or Guest Customizations are used, credentials are defined in |AdmSetPro| and User Settings. If credentials are defined on the image and Cloud-Init is enabled, |morpheus| will add that user during provisioning, so ensure that user does not already exist on the image (such as ``root``). For Windows Guest Customizations, |morpheus| will set the Administrator password to what is defined on the image if Administrator user is defined. Do not define any other user than Administrator for Windows Images unless using Cloudbase-init. |morpheus| recommends running Guest Customizations for all Windows Images, which is required when joining Domains as the SID will change
  Password
    Password for the user on the image if username is populated
  Bucket
   Location where the Virtual Image will be stored. Default Virtual Image Storage location is ``/var/opt/morpheus/morpheus-ui/vms``. Additional Storage Providers can be configured in ``Infrastructure > Storage``
  Cloud-Init User Data
    Accepts what would go in ``runcmd`` and can assume Bash syntax. Example use: Script to configure satellite registration at provision time
  Create Image ID
   Select FILE to browse locally for an image or drop an image file into the dropzone. Alternatively, select URL to download the image from an accessible URL. It is recommend to configure the rest of the settings below prior to uploading the source Image File(s)
  Permissions
   Set Tenant permissions in a multi-tenant |morpheus| environment. Select private visibility and select specific Tenants to which the Virtual Image will be made available. Select public visibility to share the Virtual Image with all Tenants
  Auto Join Domain?
   Enable to have Instances provisioned with this image auto-join configured domains (Windows only, domain controller must be configured in ``Infrastructure > Network`` and the configured domain set on the provisioned to Cloud or Network)
  VirtIO Drivers Loaded?
   Enable if VirtIO Drivers are installed on the image for provisioning to KVM-based hypervisors
  FIPS Compliant Image?
   When selected, |morpheus| will install the FIPS-compliant |morpheus| Agent package
  VM Tools Installed?
   On by default, uncheck if VMware Tools (including OpenVMTools) are not installed on the Virtual Image. |morpheus| will skip network wait during provisioning when deselected
  Force Guest Customization?
   VMware only, forces guest customizations to run during provisioning, typically when provisioning to a DHCP network where guest customizations would not run by default.  This options requires that VMware Tools is installed on the image
  Trial Version
   Enable to automatically re-arm the expiration on Windows Trial Images during provisioning
  Enabled Sysprep?
   Applicable to multiple Clouds, including VMware vCenter, SCVMM, Nutanix, Hyper-V, KVM, and Google GCP. Enable if the Windows Image has been sysprepped. If enabled, |morpheus| will inject ``unattend.xml``

.. NOTE:: Default Storage location is ``/var/opt/morpheus/morpheus-ui/vms``. Additional Storage Providers can be configured in `Infrastructure > Storage`. Ensure local folders are owned by morpheus-app.morpheus-app if used.

.. WARNING:: Provisioning will fail if `Cloud init Enabled` is checked and Cloud-Init is not installed on the Image.

.. NOTE:: Existing Image credentials are required for Linux Images that are not Cloud-Init enabled and for Windows Images when Guest Customizations are not used. Cloud-Init and Windows user settings need to be configured in |AdmSetPro| when using Cloud-Init or Guest Customizations and new credentials are not set on the Virtual Image.

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

In a VMware environemnt, you may have a single VM template that you use across different vCenters.  Uploading an image to Morpheus, mentioned in the **Add Virtual Image** section, is one method to solve this.  Alternatively, 
an organization may decide to create a VM template in one vCenter and then transfer it to other vCenters, which then could be sync'd into Morpheus.  If all of the vCenters are added as clouds into Morpheus and the templates 
are named the same in each vCenter, they will be aggregated under a single virtual image in Morpheus.  This means that as you deploy to the various vCenter clouds in Morpheus, using a this virtual image, it will choose the 
correct VM template to use based on the cloud deployed to.

This eliminates the need for creating multiple node types for each virtual image, if the templates were named differently in each vCenter.  This can reduce the overhead of maintaing multiple node types and reduces user selections. 
As well, this can reduce the cloning time of VMs by avoiding network transfers of images between geographic locations, ensuring the closest VM template is selected.

.. NOTE:: VM templates are a **Data Center** level object.  The same process above applies to a single VMware cloud with multiple logical data centers.  It will not apply to clusters, as a template is not associated with a cluster, only when it is converted to a VM.
