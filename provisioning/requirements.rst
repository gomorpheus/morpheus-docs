Requirements
============

Provisioning Instances and Apps typically involves many steps beyond starting a workload. |morpheus| is centered around automating everything desired for your application to be fully operational, including networking, storage, hostnames, domains, dns, licenses, scripts/automation, scaling, load balancers, security, accessibility, governance, auditing, monitoring, backups, costs, sizing and on and on. Point being there is a lots that goes on when spinning up an instance or app, and to make the magic happen a few requirements need to be met.

.. IMPORTANT:: By default, Agent Installation is enabled when provisioning unless deselected on the Virtual Images or `SKIP AGENT INSTALL` is selected when provisioning.

VM Provision Steps
------------------

While an infinite number of steps can happen when provisioning an Instance or App using a VM(s) in |morpheus|, the basic order is:

- Look for Virtual Image
  |morpheus| will check if the Virtual Image set on the Node Type or selected during provisioning is already available in the source Cloud. If not and it is an Uploaded/Local Image, |morpheus| will attempt to upload the Image to the target Cloud.

  Upload Image
    For Uploaded/Local Images that do not exist in the target cloud, |morpheus| will need to upload the Image.
      Ensure the Virtual Image is valid for the target Cloud, the Image meets the target cloud upload requirements, and |morpheus| has network access and permissions to upload the image.

      .. NOTE:: When uploading an image to a VMware Cloud, the Virtual Image is copied directly to the target ESXi host, NOT through the vCenter server. Ensure the |morpheus| Appliance(s) can resolve target ESXi hostnames and connect on port 443 for successful vmdk/ova uploads.

  Clone Image
  Once the Image is confirmed available in the target cloud, |morpheus| will clone the Image to the target Datastore.

  .. NOTE:: The target host must have access to the target Datastore of the Image

- Reconfigure Image
  Once cloned |morpheus| will resize the Image based off provisioning parameters
- Cloud-init (if enabled)
      Attached cloud-init iso
        When using cloud-init, |morpheus| will attach a tiny metadata iso to new VM. Network, Machine, User and any other cloud-init metadata will be sourced from this iso.
      VM Tools
        |morpheus| will run Guest Customizations via VMware VM Tools, including network config when assigning static IP's.
- Wait for Power On status and Network info
  |morpheus| will wait to hear back from the target cloud/hypervisor that the VM has successfully started and has an IP address.

  .. NOTE::

     If ``VM TOOLS INSTALLED?`` is NOT checked on the source Virtual Image configuration, |morpheus| will skip waiting for network.

- Finalize
    By default this will include Agent Installation and any post-provison scripts or workflows or integration automation steps.

    .. IMPORTANT:: If the VM is stuck in finalize for longs periods of time, this typically means the Agent cannot be installed or has not been heard back from. This will result in a `!` warning Instance status upon provisioning completion.

    If agent installation is not possible or desired, uncheck "Install Agent" on the source Virtual Image configuration or select "Skip Agent Install" during provisioning to speed up provisioning completion.

Virtual Images
--------------

While containers are the future, the most common provisioning method involves Virtual Machines, and the most important part of Provisioning a VM is the Virtual Image. When provisioning a VM, |morpheus| will need to do a few things depending on the location of the Virtual Image and if agent install, console access, and scrip execution is desired.

Synced Images need to be properly configured
    |morpheus| gathers as much metadata for synced images as possible, but depending on the cloud, os, image configuration, agent install settings, by default the synced Virtual Images may not be ready to provision until configured. The Virtual Image is already at the target Cloud, but datastore selection, credentials, cloud-init settings, and networks and security settings on the Virtual Image can cause provisioning issues.
Local/Uploaded Virtual Images
    Images uploaded to |morpheus| are configured during the `Add Virtual Image` process, however |morpheus| in most scenarios will still need to copy the Virtual Image to the target Hypervisor/Cloud upon the first provision to the target Cloud. In addition to the requirements for provisioning a synced Virtual Image, copying an uploaded Virtual Image to the target Cloud upon is required and network and image configurations can cause upload failures, resulting in provisioning issues.
Marketplace Images
  AWS and Azure marketplace Images can be provisioned using the generic Amazon or Azure Instance Types, or added as Virtual Images as scoped to Node Types for custom Instance Types. Marketplace items provisioned/added to |morpheus| still fall upon the requirements of the target Cloud, such as matching the region with the Image and licensing.

Synced Images
^^^^^^^^^^^^^

When a Cloud is added to |morpheus|, all available Images/Templates records from that Cloud will be synced in regardless of Inventory settings on the Cloud. These Image records will be available in the Virtual Images section and can be provisioned by using the target clouds generic Instance Type, ie VMware, Amazon, Azure, Openstack etc Instance Types, or by creating custom Instance Types and selecting the Image on a Node Type.

.. NOTE:: Synced Virtual Images are just meta-data records in |morpheus| pointing to the Image in the target Cloud. The actual Image files are not copied/imported to |morpheus|.

Before provisioning a synced Virtual Images, ensure the image is configured properly:

Name
  Name of the Virtual Image in |morpheus| . This can be changed from the name of the Image, but editing will not change the name of the actual Image.
Operating System
  Specifies the Platform and OS of the image. All Windows images will need to have Operating System specified on the  Virtual Image, as |morpheus| will assign Linux as the Platform for all Images without Operating System specified.
Minimum Memory
 The Minimum Memory setting will filter available Service Plans options during provisioning. Service Plans that do not meet the Minimum Memory value set on the Virtual Image will not be provided as Service Plan choices.
Cloud Init Enabled?
  On by default, uncheck for any Image that does not have Cloud-Init or Cloudbase-Init installed.

  .. IMPORTANT:: Provisioning a Virtual Images that has `Cloud Init Enabled?` checked on the Virtual Record in |morpheus| but does not have cloud-init install will result in immediate provisioning failure.

Install Agent
  On by default, uncheck to skip Agent install. Note this will result in the loss of utilization statistics, logs, script execution, and monitoring. (Some utilization stats are collected for agent-less hosts and vm's from VMware and AWS clouds).
Username
  Existing Username on the Image. This is required for authentication, unless |morpheus| is able to add user data, Cloud-Init, Cloudbase-Init or Guest Customizations. If Cloud-Init, Cloudbase-Init Guest Customizations or Nutanix Sysprep are used, credentials are defined in |AdmSetPro| and User Settings. If credentials are defined on the Image and Cloud-Init is enabled, |morpheus| will add that user during provisioning, so ensure that user does not already exist n the image (aka ``root``). For Windows Guest Customizations, |morpheus| will set the Administrator password to what is defined on the image if Administrator user is defined. Do not define any other user than Administrator for Windows Images unless using Cloudbase-init. |morpheus| recommends running Guest Customizations for all Windows Images, which is required when joining Domains as the SID will change.
Password
  Password for the Existing User on the image if Username is populated.
Storage Provider
 Location where the Virtual Image will be stored. Default Virtual Image Storage location is /var/opt/morpheus/morpheus-ui/vms. Additional Storage Providers can be configured in `Infrastructure > Storage`.
Cloud-Init User Data
  Accepts what would go in runcmd and can assume bash syntax. Example use: Script to configure satellite registration at provision time.
Permissions
  Set Tenant permissions in a multi-tenant |morpheus| environment. No impact on single-tenant environments.
    Visibility
      Private
        Image is only available in the specified Tenants below.
      Public
        Image is available to all Tenants.
    Tenant
      If Visibility is set to Private, specify Tenants the Image will be available for.

Auto Join Domain?
 Enable to have instances provisioned with this image auto-join configured domains (Windows only, domain controller must be configure in `Infrastructure > Network` and the configured domain set on the provisioned to Cloud or Network).
VirtIO Drivers Loaded?
 Enable if VirtIO Drivers are installed on the image for provisioning to KVM based Hypervisors.
VM Tools Installed?
 On by default, uncheck if VMware Tools (including OpenVMTools) are not installed on the Virtual Image. |morpheus| will skip network wait during provisioning when deselected.
Force Guest Customization?
 VMware only, forces guest customizations to run during provisioning, typically when provisioning to a DHCP network where guest customizations would not run by default. This is required for host/computer name definitions. domain joining, licenses and user definitions when using DHCP.
Trial Version
 Enable to automatically re-arm the expiration on Windows Trial Images during provisioning.
Enabled Sysprep?
 Applicable to Nutanix Only. Enable of the Windows Image has been sys-prepped. If enabled Morpheus will inject Unattend.xml through the Nutanix API (v3+ only)

.. IMPORTANT:: Provisioning a Virtual Images that has `Cloud Init Enabled?` checked on the Virtual Record in |morpheus| but does not have cloud-init install will result in immediate provisioning failure.

.. IMPORTANT:: For Linux images without CLoud-Init, and existing username and password must be defined on the Virtual Image record for Agent Install, Domain joining, licensing, script execution and other automation, and ssh or RDP Console access.


Local Virtual Images
^^^^^^^^^^^^^^^^^^^^
A Local Virtual Image means it has been uploaded to |morpheus|.  To provision, |morpheus| will need to upload the Image to the target Cloud upon first provision.

- Ensure the Virtual Image is valid for the target Cloud, the Image meets the target cloud upload requirements, and |morpheus| has network access and permissions to upload the image.

.. NOTE:: When uploading an image to a VMware Cloud, the Virtual Image is copied directly to the target ESXi host, NOT through the vCenter server. Ensure the |morpheus| Appliance(s) can resolve target ESXi hostnames and connect on port 443 for successful vmdk/ova uploads.

Once a Local Virtual Image has been uploaded to a Cloud, subsequent provisions will use the Image local to the cloud instead of uploading again as long as the copied image is still available in the source Cloud.

Agent Install
--------------

When provisioning an instance, there are some network and configuration requirements to successfully install the morpheus agent.  Typically when a vm instance is still in the provisioning phase long after the vm is up, the instance is unable to reach |morpheus| , or depending on agent install mode, |morpheus| is unable to reach the instance.

The most common reason an agent install fails is the provisioned instance cannot reach the |morpheus| Appliance via the appliance_url set in Admin > Settings over both 443 and 80. When an instance is provisioned from |morpheus|, it must be able to reach the |morpheus| appliance via the appliance_url or the agent will not be installed.

.. image:: /images/agent-7c9a2.png
    :align: center


In addition to the main appliance_url in Admin > Settings, additional appliance_urls can be set per cloud in the Advanced options of the cloud configuration pane when creating or editing a cloud. When this field is populated, it will override the main appliance url for anything provisioned into that cloud.

.. TIP:: The |morpheus| UI current log, located at /var/log/morpheus/morpheus-ui/current, is very helpful when troubleshooting agent installations.

Agent Install Modes
^^^^^^^^^^^^^^^^^^^^

There are 3 Agent install modes:

- ssh/winrm
- VMware Tools
- cloud-init

For All Agent Install modes
```````````````````````````

When an instance is provisioned and the agent does not install, verify the following for any agent install mode:

* The |morpheus| appliance_url (Admin > Settings) is both reachable and resolvable from the provisioned node.
* The appliance_url begins with to https://, not http://.

.. NOTE:: Be sure to use https:// even when using an ip address for the appliance.

* Inbound connectivity access to the |morpheus| Appliance from provisioned VM's and container hosts on port 443 (needed for agent communication)

* Private (non-morpheus provided) vm images/templates must have their credentials entered. These can be entered/edited in the Provisioning - Virtual Images section but clicking the Actions dropdown of an image and selecting Edit.

.. NOTE:: Administrator user is required for Windows agent install.

* The instance does not have an IP address assigned. For scenarios without a dhcp server, static IP information must be entered by selecting the Network Type: Static in the Advanced section during provisioning. IP Pools can also be created in the Infrastructure > Networks > IP Pools section and added to clouds network sections for IPAM.

* DNS is not configured and the node cannot resolve the appliance. If dns cannot be configure, the ip address of the |morpheus| appliance can be used as the main or cloud appliance.

SSH/Winrm
^^^^^^^^^

Linux Agent
```````````

* Port 22 is open for Linux images, and ssh is enabled
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the |LibVir| section.

.. image:: /images/provisioning/agent_ssh.gif


Windows Agent
`````````````

* Port 5985 must be open and WinRM enabled for Windows images.
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the |LibVir| section.

.. NOTE:: Administrator user is required for Windows agent install.

VMware tools (vmtools) rpc mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* VMware tools is installed on the template(s)
* Credentials have been entered on the Image if using uploaded or synced image when Cloud-init or Guest Customizations or Sysprep for Windows are not used. Credentials can be entered on Images in the |LibVir| section.

Cloud-Init agent install mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Cloud-Init is configured in Admin > Provisioning section
* Provisioned image/blueprint has Cloud-Init (linux) or Cloudbase-Init (windows) installed
