Requirements
============

Provisioning Instances typically involves many steps beyond starting a workload and |morpheus| is centered around automating everything for your application to be fully operational. There is a lot that goes on when spinning up an Instance, and to make the magic happen a few requirements need to be met.

.. IMPORTANT:: By default, Agent Installation is enabled when provisioning unless deselected on the Virtual Image or `SKIP AGENT INSTALL` is selected from the provisioning wizard.

VM Provision Steps
------------------

While many things can happen during an individual provisioning process, the basic order is:

- Look for the Virtual Image

  |morpheus| will check if the Virtual Image set on the Node Type or selected from a list of images during provisioning is already available to the |cluster| or to a vCenter Cloud target. If not and it is an uploaded or local image, |morpheus| will attempt to upload the image to the |cluster| or vCenter target.

  **Upload Image**

  For uploaded or local images that do not exist in the target, |morpheus| will need to upload the Image. Ensure the Virtual Image is valid for the target technology, the image meets the target upload requirements, and |morpheus| has network access and permissions to upload the image.

  .. NOTE:: When uploading an image to a VMware Cloud, the Virtual Image is copied directly to the target ESXi host, NOT through the vCenter server. Ensure the |morpheus| Appliance(s) can resolve target ESXi hostnames and connect on port 443 for successful vmdk/ova uploads.

  **Clone Image**

  Once the Image is confirmed available in the target cloud, |morpheus| will clone the Image to the target Datastore.

  .. NOTE:: The target host must have access to the target Datastore of the Image

- Reconfigure Image

  Once cloned, |morpheus| will resize the Image based off provisioning parameters

- Cloud-init (if enabled)
      Attached cloud-init iso
        When using cloud-init, |morpheus| will attach a tiny metadata iso to the new VM. Network, Machine, User and any other cloud-init metadata will be sourced from this iso.
      VM Tools
        |morpheus| will run guest customizations via VMware VM Tools, including network config when assigning static IP addresses.
- Wait for Power On status and Network info

  |morpheus| will wait to hear back from the target that the VM has successfully started and has an IP address.

  .. NOTE:: If ``VM TOOLS INSTALLED?`` is NOT checked on the source Virtual Image configuration, |morpheus| will skip waiting for network.

- Finalize

    By default, this step will include Agent installation.

    .. IMPORTANT:: If the VM is stuck in finalize for long periods of time, this typically means the Agent cannot be installed or has not been heard back from. This will result in a `!` warning Instance status upon provisioning completion.

    If agent installation is not possible or is not desired, uncheck "Install Agent" on the source Virtual Image configuration or select "Skip Agent Install" during provisioning to speed up provisioning completion.

Virtual Images
--------------

The most common provisioning method within |morpheus| involves Virtual Machines, and the most important part of provisioning a VM is the Virtual Image. When provisioning a VM, |morpheus| will need to do a few things depending on the location of the Virtual Image and if agent install and console access are desired.

Synced Images need to be properly configured
    |morpheus| gathers as much metadata for synced images as possible, but depending on the target (|cluster| or VMware vCenter), OS, image configuration, or agent install settings, the synced Virtual Images may not be ready to provision without some configuration within |morpheus|. The Virtual Image is already at the target Cloud, but datastore selection, credentials, cloud-init settings, networks, and security settings on the Virtual Image can cause provisioning issues.
Local/Uploaded Virtual Images
    Images uploaded to |morpheus| are configured during the `Add Virtual Image` process, however |morpheus| in most scenarios will still need to copy the Virtual Image to the target Hypervisor/Cloud upon the first provision to the target Cloud. In addition to the requirements for provisioning a synced Virtual Image, copying an uploaded Virtual Image to the target Cloud is required. Network and image configurations can cause upload failures, resulting in provisioning issues.

Synced Images
^^^^^^^^^^^^^

When a provisioning target (Cloud) is added, all available image and template records from that Cloud will be synced in regardless of Inventory settings on the Cloud. These image records will be available in the Virtual Images section and can be provisioned by using the target clouds generic Instance Type (ex. By selecting the HPE VM or VMware Instance Type from the provisioning wizard).

.. NOTE:: Synced Virtual Images are just metadata records in |morpheus| pointing to the image in the target Cloud. The actual image files are not copied/imported to |manager|.

Before provisioning a synced Virtual Image, ensure the image is configured properly:

Name
  Name of the Virtual Image in |morpheus|. This can be changed from the name of the image, but editing will not change the name of the actual image file.
Operating System
  Specifies the platform and OS of the image. All Windows images will need to have Operating System specified on the Virtual Image, as |morpheus| will assign Linux as the platform for all images without an operating system specified.
Minimum Memory
 The Minimum Memory setting will filter available Plan options during provisioning. Plans that do not meet the minimum memory value set on the Virtual Image will not be provided as Plan choices by the provisioning wizard.
Cloud Init Enabled?
  On by default, uncheck for any image that does not have Cloud-Init or Cloudbase-Init installed.

  .. IMPORTANT:: Provisioning a Virtual Image that has `Cloud Init Enabled?` checked on the Virtual Record in |morpheus| but does not have cloud-init installed will result in immediate provisioning failure.

Install Agent
  On by default, uncheck to skip Agent install. Note this will result in the loss of utilization statistics, logs, Task execution, and monitoring (Some utilization stats are still collected by Agent-less workloads).
Username
  An existing Username on the Image. This is required for authentication, unless |morpheus| is able to add user data, Cloud-Init, Cloudbase-Init or Guest Customizations. If Cloud-Init, Cloudbase-Init Guest Customizations or Nutanix Sysprep are used, credentials are defined in |AdmSetPro| and User Settings. If credentials are defined on the Image and Cloud-Init is enabled, |morpheus| will add that user during provisioning, so ensure that user does not already exist in the image (aka ``root``). For Windows Guest Customizations, |morpheus| will set the Administrator password to what is defined on the image if Administrator user is defined. Do not define any other user than Administrator for Windows Images unless using Cloudbase-init. |morpheus| recommends running Guest Customizations for all Windows Images, which is required when joining Domains as the SID will change.
Password
  Password for the existing user on the image if the Username field is populated.
Storage Provider
 Location where the Virtual Image will be stored. Default Virtual Image Storage location is ``/var/opt/morpheus/morpheus-ui/VMs``. Additional storage providers can be configured in |InfSto|.
Cloud-Init User Data
  Accepts what would go in ``runcmd`` and can assume bash syntax. Example use: Script to configure satellite registration at provision time.
Auto Join Domain?
 Enable to have Instances provisioned with this image auto-join configured domains (Windows only, domain controller must be configured in |InfNet| and the configured domain set on the provisioned to Cloud or Network).
VirtIO Drivers Loaded?
 Enable if VirtIO Drivers are installed on the image for provisioning to KVM-based hypervisors, such as |cluster|
VM Tools Installed?
 On by default, uncheck if VMware Tools (including OpenVMTools) are not installed on the Virtual Image. |morpheus| will skip network wait during provisioning when deselected.
Force Guest Customization?
 VMware only, forces guest customizations to run during provisioning, typically when provisioning to a DHCP network where guest customizations would not run by default. This is required for host/computer name definitions. domain joining, licenses and user definitions when using DHCP.
Trial Version
 Enable to automatically re-arm the expiration on Windows Trial Images during provisioning.

.. IMPORTANT:: Provisioning a Virtual Image that has `Cloud Init Enabled?` checked on the Virtual Record in |morpheus| but does not have cloud-init installed will result in immediate provisioning failure.

.. IMPORTANT:: For Linux images without cloud-init, an existing username and password must be defined on the Virtual Image record for Agent Install, Domain joining, licensing, script execution and other automation, and SSH or RDP Console access.

Local Virtual Images
^^^^^^^^^^^^^^^^^^^^
A Local Virtual Image means it has been uploaded to |morpheus|. To provision, |morpheus| will need to upload the image to the provisioning target upon first provision.

- Ensure the Virtual Image is valid for the target Cloud, the Image meets the target cloud upload requirements, and |morpheus| has network access and permissions to upload the image.

.. NOTE:: When uploading an image to a VMware Cloud, the Virtual Image is copied directly to the target ESXi host, NOT through the vCenter server. Ensure the |morpheus| Appliance(s) can resolve target ESXi hostnames and connect on port 443 for successful vmdk/ova uploads.

Once a local Virtual Image has been uploaded to a provisioning target, subsequent provisions will use the image local to the target instead of uploading again as long as the copied image is still available.

Agent Install
--------------

When provisioning an Instance, there are some network and configuration requirements to successfully install the Agent. Typically when a VM Instance is still in the provisioning phase long after the VM is up, the Instance is unable to reach |morpheus|, or depending on Agent install mode, |morpheus| is unable to reach the Instance.

The most common reason an Agent install fails is the provisioned Instance cannot reach the |morpheus| Appliance via the ``appliance_url`` set in |AdmSet| over both 443 and 80. When an Instance is provisioned from |morpheus|, it must be able to reach the |morpheus| appliance via the ``appliance_url`` or the Agent will not be installed.

In addition to the main ``appliance_url`` in |AdmSet|, additional ``appliance_urls`` can be set per Cloud in the Advanced options of the Cloud configuration pane when creating or editing a Cloud. When this field is populated, it will override the main appliance URL for anything provisioned into that Cloud.

.. TIP:: The |morpheus| current log, located at ``/var/log/morpheus/morpheus-ui/current``, is very helpful when troubleshooting Agent installations.

Agent Install Modes
^^^^^^^^^^^^^^^^^^^^

There are 3 Agent install modes:

- SSH/WinRM
- VMware Tools
- Cloud-init

For All Agent Install modes
```````````````````````````

When an Instance is provisioned and the Agent does not install, verify the following for any agent install mode:

* The |morpheus| ``appliance_url`` (|AdmSet|) is both reachable and resolvable from the provisioned node.
* The ``appliance_url`` begins with to ``https://``, not ``http://``.

.. NOTE:: Be sure to use ``https://`` even when using an IP address for the appliance.

* Inbound connectivity access to the |morpheus| Appliance from provisioned VMs and |cluster| hosts on port 443 (needed for Agent communication)

* Private images (those not provided with |morpheus| by default) must have their credentials entered. These can be entered or edited in the |LibVir| section by clicking the edit button (pencil icon) next to the appropriate image.

.. NOTE:: Administrator user is required for Windows agent install.

* The Instance does not have an IP address assigned. For scenarios without a DHCP server, static IP information must be entered by selecting the Network Type: Static in the Advanced section during provisioning. IP Pools can also be created in the |InfNetIP| section and added any Cloud's network section for IPAM.

* DNS is not configured and the node cannot resolve the appliance. If DNS cannot be configured, the IP address of the |morpheus| appliance can be used.

SSH/Winrm
^^^^^^^^^

Linux Agent
```````````

* Port 22 is open for Linux images, and SSH is enabled
* Credentials have been entered on the image if using a custom or synced image. Credentials can be entered on images in the |LibVir| section.

Windows Agent
`````````````

* Port 5985 must be open and WinRM enabled for Windows images.
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the |LibVir| section.

.. NOTE:: Administrator user is required for Windows agent install.

VMware tools (vmtools) RPC mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* VMware tools is installed on the template(s)
* Credentials have been entered on the Image if using an uploaded or synced image when Cloud-init or Guest Customizations or Sysprep for Windows are not used. Credentials can be entered on Images in the |LibVir| section.

Cloud-Init Agent install mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Cloud-Init is configured in |AdmSetPro| section
* Provisioned image has Cloud-Init (Linux) or Cloudbase-Init (Windows) installed
