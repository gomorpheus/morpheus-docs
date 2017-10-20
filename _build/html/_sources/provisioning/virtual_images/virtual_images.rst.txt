Virtual Images
==============

`Provisioning -> Virtual Images`

Overview
--------

The Virtual Image section displays a list of all images, local and synced, that are available to deploy. |morpheus| includes a rich catalog of pre-configured System Images available for every cloud type. User Images are automatically synced from Cloud Integrations and added to the Virtual Images section. Images can also be uploaded directly into |morpheus| via local file or url. Amazon and Azure Marketplace images can also be added to the Virtual Images Section.

Image Types
-----------

|morpheus| provides a vast *System Image* repo with pre-configured images for every Cloud. All other images are *User Images*. User images can be added directly to |morpheus| , or automatically synced from integrated clouds. It is important to configure synced User Images for metadata, including specifying the Platform and User Credentials, prior to provisioning. Provisioning a User Image that has not been configured may result in failed provisioning.

.. IMPORTANT:: Synced User Images need to be configured prior to provisioning.

Configuring Virtual Images
--------------------------

System Images
^^^^^^^^^^^^^

System Images are pre-configured with metadata and have Cloud-Init or Cloudbase-Init installed. These images are ready to be provisioned with no configuration necessary. It is highly recommended to populated the `Administration -> Provisioning -> Cloud-Init` section with user data prior to provisioning, as the user and password/key will be added to all Instances provisioned from System Images. Users can also be added during provisioning in the `Add User` provisioning wizard section.

.. NOTE:: Editing System Images is disabled.

User Images
^^^^^^^^^^^

Typically |morpheus| does not have sufficient metatdata to successfully provision synced User Images. After integrating clouds and User Images have synced, it is highly recommended to configure the images prior to provisioning.

**To edit and configure an existing Virtual Image:**

1. Select `Actions - Edit` in the Virtual Images list, or `Edit` on a Virtual Image detail page.
2. Configure the following on the Image:

Name
  Name of the Virtual Image in |morpheus| . This can be changed from the name of the Image, but editing will not change the name of the actual Image.
Operating System
  Specifies the Platform and OS of the image. All Windows images will need to have Operating System specified on the Virtual Image, as |morpheus| will assign Linux as the Platform for all Images without Operating System specified.
Cloud Init Enabled?
  On by default, uncheck for any Image that does not have Cloud-Init or Cloudbase-Init installed.
Install Agent
  On by default, uncheck to skip Agent install. Note this will result in the loss of utilization statistics, logs, script execution, and monitoring. (Some utilization stats are collected for agent-less hosts and vm's from VMware and AWS clouds).
Username
  Existing Username on the Image. This is required for authentication, unless |morpheus| is able to add user data via Cloud-Init, Cloudbase-Init, or guest processes (VMware).
Password
  Password for the Existing User on the image.
Cloud-Init User Data
  Accepts what would go in runcmd and can assume bash syntax.
Permissions
  Set Tenant permissions in a multi-tenant |morpheus| environment. No impact on single-tenant environments.
Auto Join Domain?
  Enable to have instances provisioned with this image auto-join configured domains (Windows only).
VirtIO Drivers Loaded?
  Enable if VirtIO Drivers are installed on the image for provisioning to KVM based Hypervisors.
Force Guest Customization?
  VMware only, forces sys-prep on image during provisioning.
Trial Version
  Enable to automatically re-arm the expiration on Windows Trial Images during provisioning.

3. Save Changes

.. NOTE:: Cloud-Init is enabled by default on all Images. Images without Cloud-Init or Cloudbase-Init installed must have the `cloud-init` flag disabled on the Virtual Image setting or Provisioning may fail.

Provisioning Images
-------------------

When provisioning a System Image for the first time, |morpheus| will download and stream the image from S3 to the source Cloud if the image is not local to the Cloud. The Image will also be cached on the |morpheus| Appliance under /var/opt/morpheus/vm/vmcache. Subsequent provisions of the image will use the created template in the Cloud or the cached local Image if the images does not exist in the selected Cloud, in which case the cached Image will be copied to the Cloud.

When using Images that already exist in the destination cloud, such as synced, marketplace, or previously copied images, no image transfer between the |morpheus| Appliance and destination cloud will take place.

.. NOTE:: The |morpheus| Appliance must be able to download from Amazon S3 when provisioning System Images for the first time.

.. NOTE:: The |morpheus| Appliance must be able reach and resolve the destination Host when provisioning System Images or uploaded Images for the first time. This included being able to resolve ESXi host names in VMware VCenter clouds, and reach the destination ESXi host over port 443.

Add Virtual Images
------------------

Virtual Images can be upload to |morpheus| from local files or URL's. Amazon and Azure Marketplace metadata can also be added to the Virtual Images library, enabling the creation of custom catalog Instance Type from Marketplace images (no image is transferred to |morpheus| when adding Marketplace images).

To Add Virtual Image:

1. Select `+ Add Virtual Image` in the Virtual Images page.
2. Select Image format:
  * Amazon AMI
  * Azure Marketplace
  * Digital Ocean
  * ISO
  * PXE Boot
  * QCOW2
  * RAW
  * VHD
  * VirtualBox
  * VirtualBox (vdi)
  * VMware (vmdk/ovf/ova)

3. Configure the following on the Virtual Image:

Name
  Name of the Virtual Image in |morpheus| . This can be changed from the name of the Image, but editing will not change the name of the actual Image.
Operating System
  Specifies the Platform and OS of the image. All Windows images will need to have Operating System specified on the Virtual Image, as {norpheus} will assign Linux as the Platform for all Images without Operating System specified.
Cloud Init Enabled?
  On by default, uncheck for any Image that does not have Cloud-Init or Cloudbase-Init installed.
Install Agent
  On by default, uncheck to skip Agent install. Note this will result in the loss of utilization statistics, logs, script execution, and monitoring. (Some utilization stats are collected for agent-less hosts and vm's from VMware and AWS clouds).
Username
  Existing Username on the Image. This is required for authentication, unless |morpheus| is able to add user data via Cloud-Init, Cloudbase-Init, or guest processes (VMware).
Password
  Password for the Existing User on the image.
Storage Provider
  Location where the Virtual Image will be stored. Default Virtual Image Storage location is /var/opt/morpheus/morpheus-ui/vms. Additional Storage Providers can be configured in `Infrastructure -> Storage`.
Cloud-Init User Data
  Accepts what would go in runcmd and can assume bash syntax.
Permissions
  Set Tenant permissions in a multi-tenant |morpheus| environment. No impact on single-tenant environments.
Auto Join Domain?
  Enable to have instances provisioned with this image auto-join configured domains (Windows only).
VirtIO Drivers Loaded?
  Enable if VirtIO Drivers are installed on the image for provisioning to KVM based Hypervisors.
Force Guest Customization?
  VMware only, forces sys-prep on image during provisioning.
Trial Version
  Enable to automatically re-arm the expiration on Windows Trial Images during provisioning.

.. NOTE:: Default Storage location is /var/opt/morpheus/morpheus-ui/vms. Additional Storage Providers can be configured in `Infrastructure -> Storage`. Ensure local folders are owned by morpheus-app.morpheus-app if used.

4. Upload Image

  Images can be uploaded by File or URL:

  *File*
    Drag and Drop the image file, or select "Add File" to select the image file.

  *Url*
    Select the URL radio button, and enter URL of the Image.

.. NOTE:: |morpheus| provides a file upload progress. The Virtual Image configuration can be saved while the upload is in progress, and the upload will finish in the background.
