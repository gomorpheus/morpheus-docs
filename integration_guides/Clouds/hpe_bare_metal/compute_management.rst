Compute Management
^^^^^^^^^^^^^^^^^^

The topic section describes how HPE |morpheus| Enterprise orchestrates on-premises and HPE BMaaS Cloud resources. It covers the end-to-end lifecycle for physical servers, including installation, cloud configuration, on-boarding, and workload migration.

 Administrators perform the following tasks: 
- Define a Bare Metal Cloud

 
- Configure unmanaged networks and resource pools

 
- Import
- HPE
- ProLiant servers for centralized visibility

 
- Manage greenfield (new) and brownfield (existing) server deployment

 
- Convert Pre-Provisioned servers into managed
- HPE
- Morpheus instances

Administrators use these procedures to enable consistent provisioning, lifecycle management, and governance for HPE ProLiant infrastructure within HPE Morpheus.

Creating Resource Pools
-----------------------

  This section describes how to create a resource pool within your HPE ProLiant Bare Metal Cloud in Morpheus. Resource pools help you organize and allocate servers for provisioning and management.


#. Navigate to
#. Navigate to **Infrastructure > Clouds**. Select the cloud and click the
#. Resources
#. tab. 
#. Click the
#. + Add Resource Pool.
#. Enter a name and complete any additional required details for the resource pool and then click
#. Next.
#. Click
#. Save Changes
#. to finalize resource pool creation.

Image Management
----------------

The topic describes about image catalog and uploading various images.

Image Catalog
^^^^^^^^^^^^^

This section describes how to upload Bare Metal (BM) operating system images into Morpheus using a configurable image repository.HPE Morpheus supports multiple backend storage options, allowing administrators to centrally manage OS images and reuse them across bare metal provisioning workflows.

 Uploaded images are registered underLibrary>Virtual Imagesand are made available for bare metal instance provisioning.

  Supported OS Image Sources
  HPE Morpheus supports uploading Bare Metal OS images from the following storage backends: 
* Local storage on the
* HPE Morpheus appliance

* S3-compatible object storage

* CIFS (Samba) file shares

* NFS (v3) file shares

Each backend option is configured as a File Share or Storage Bucket and referenced during image upload.

Uploading OS Images
^^^^^^^^^^^^^^^^^^^

Prerequisites

* Image upload and deployment performance depend on network bandwidth and storage backend performance. 
* File permissions on shared storage must allow Morpheus read access. 
* OS images must be bootable and compatible with the target bare metal hardware. 
* Server reboots and virtual media behavior depend on hardware management interfaces (for example, iLO).

Uploading OS Images Using Local Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prerequisites

* Ensure that Morpheus-app user owns the storage directory.

* Ensure that Morpheus-app user has access to the storage path.

Local storage allows OS images to be uploaded directly to the Morpheus appliance filesystem and is suitable for smaller environments or evaluation use cases.


#. Configure a Local Storage file share under
#. Infrastructure
#. >
#. Storage
#. >
#. File Shares.
#. Upload the OS ISO using
#. Library
#. >
#. Virtual Images
#. >
#. Add
#. >
#. ISO.
#. Verify the image status is
#. Active.
Uploading OS Images Using S3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-Compatible Object Storage
      S3-compatible object storage (such as MinIO) provides scalable and durable storage for OS images.


#. Configure an S3 storage bucket under
#. Infrastructure
#. >
#. Storage
#. >
#. Buckets.
#. Provide access credentials with read/write permissions. 
#. Upload the OS ISO using
#. Library
#. >
#. Virtual Images
#. >
#. Add
#. >
#. ISO.
#. Confirm successful upload and activation.

Uploading OS Images Using CIFS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(Samba)
CIFS (Samba) allows OS images to be stored on a shared Windows or Linux file server.


#. Configure a CIFS file share under
#. Infrastructure
#. >
#. Storage
#. >
#. File Shares.
#. Provide valid credentials for the Samba share. 
#. Upload the OS ISO through
#. Library
#. >
#. Virtual Images
#. >
#. Add
#. >
#. ISO.
#. Verify the image is accessible for provisioning.

Uploading OS Images Using NFS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  NFS allows OS images to be stored on a shared Linux file server.


#. Configure an NFSv3 file share under
#. Infrastructure
#. >
#. Storage
#. >
#. File Shares.
#. Provide valid credentials for the NFS share. 
#. Upload the OS ISO through
#. Library
#. >
#. Virtual Images
#. >
#. Add
#. >
#. ISO.
#. Verify the image is accessible for provisioning.

Windows OS Imaging
^^^^^^^^^^^^^^^^^^

This section provides guidance and requirements for deployingWindows Server on bare metalusing |morpheus| Enterprise. It covers required virtual image settings, Windows-specific boot considerations, current licensing limitations, and high-level troubleshooting guidance for failed installations.

 The following Windows distributions are supported for deployment: 
* Windows Server 2019

* Windows Server 2022

* Windows Server 2025

Virtual Image Configuration
 When adding a Windows ISO to theMorpheus Virtual Images Library, the following settingsmustbe configured: 
* Is Cloud Init Enabled: Unchecked

* Cloud Guest Customization: Checked

* Sysprepped / Generalized Image: Checked

* Install Agent: Checked

  
* Advanced 
  - VM Tools Installed: Checked

Windows Install Image Index
 By default, Morpheus installs Image Index 2, which typically corresponds to Windows Server Standard (Desktop Experience).

 To deploy a different Windows edition: 
#. Navigate to
#. Library
#. >
#. Operating Systems.
#. Add a new Operating System entry with
#. Platform = Windows.
#. Specify the desired
#. Windows Install Index.
#. Complete the required fields (Vendor, OS Version, Category, OS Name, Codename, OS Family).

 
#. Associate the Windows Virtual Image with this Operating System.

You can use the existing Windows Operating System as reference templates.

Boot Prompt Configuration
`````````````````````````

Unmodified Microsoft Windows Server ISOs display aPress any key to boot CD/DVD…prompt, which will interrupt unattended bare metal deployments.

 Two approaches are supported: 
* Option 1: Use a Modified ISO (Recommended)

* Option 2: Manual Console Interaction

Option 1: Use a Modified ISO (Recommended)
 Use a Windows ISO with the boot prompt removed. A script to generate such an ISO is available athttps://github.com/HewlettPackard/hpegl-metal-os-windows-iso

 Only the resulting ISO is required. A prebuilt Windows Server 2022 Evaluation ISO with this modification is also available and suitable for testing environments.

Option 2: Manual Console Interaction
 If using an unmodified ISO:

  
#. Create the instance as usual. 
#. When the instance enters provisioning, open the Remote Console. 
#. Press Enter when prompted to boot from the installation media.    Windows Licensing Considerations
 At present, Windows licensing is not supported during bare metal provisioning.

 Only Evaluation editions or versions that do not require a Product Key in AutoUnattend.xml can be deployed.

 The modified Windows Server 2022 ISO referenced above is an Evaluation edition and is suitable for testing.

Linux OS Imaging
^^^^^^^^^^^^^^^^

This section describes the supported Linux distributions and guides for deploying Linux on bare metal using Morpheus. It includes validated OS versions, required virtual image settings, boot loader configuration for unattended installation, and troubleshooting steps for common deployment issues (see Section Troubleshooting for more details).

 The following Linux distributions have been validated for deployment: 
* Red Hat Enterprise Linux (RHEL) and derivatives

  
  - RHEL 9.5

 
  - Oracle Linux 8.10

 
  - Oracle Linux 9.5

  
* Ubuntu Server

  
  - Ubuntu Server 22.04.5 LTS

 
  - Ubuntu Server 24.04.3 LTS

Virtual Image Configuration
 When adding a Linux ISO toLibrary>Virtual Images, ensure the following settings: 
* Operating System: Select the appropriate OS (e.g., RHEL 9, Oracle Linux 9, Ubuntu 22.04, Ubuntu 24.04)

* Is Cloud Init Enabled: Checked

* Advanced

  
  - VM Tools Installed: Checked

Boot Prompt Configuration - RHEL and Oracle Linux
 Unmodified RHEL and Oracle Linux ISOs include a default boot menu entry:Test this media & install OS.

 This entry performs afull media verificationbefore installation.

  NOTE  
* The media check does not cause installation failure. 
* It can, however, delay deployment by 30–60 minutes, particularly in remote or virtual media environments. 
* Skipping the media check is recommended to reduce installation time.   Supported Options


* Preferred: Modify the ISO 
  - Adjust the ISO boot loader to remove or bypass the media check from the default boot entry. 
  - Ensures faster, fully unattended deployment.  
* Alternative: Manual Boot Selection 
  - At boot: Select
  - Install OS
  - (without media test). 
  - Do NOT select
  - Test this media & install OS
  - .  
* Reference  
  - Grub menu example (for clarity): 
  - 0 → Install Red Hat Enterprise Linux 9.5

 
  - 1 → Test this media & install Red Hat Enterprise Linux 9.5

 
  - Default entry index
  - 1
  - triggers the media check.  
* Changing the default to
* 0
* or manually selecting
* Install OS
* skips verification. 

Boot Prompt Configuration - Ubuntu Server
 Ubuntu Server requires kernel boot parameters to enable unattended installation using cloud-init autoinstall.

 Unmodified ISOs do not automatically perform unattended installation.

Required Manual Step (Unmodified ISO)
 At the GRUB boot menu: 
* Highlight the default Ubuntu entry. 
* Press
* e
* to edit.

* Append the following kernel parameters:
* autoinstall ds=nocloud

* Boot with the modified entry.

  
* Example Boot Entry:
* menuentry \"Ubuntu\" {

* set gfxpayload=keep

* linux   /casper/vmlinuz quiet autoinstall ds=nocloud ---

* initrd  /casper/initrd

* }
    This enables cloud-init–based unattended installation.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Distribution
     - Registration Reference
     - Notes
   * - RHEL
     - Red Hat Subscription-Manager Registration Guide
     - Usesubscription-managerto register and attach subscriptions.
   * - Oracle Linux
     - Registering Oracle Linux System with ULN
     - Use theuln_registertool to register with Oracle Unbreakable Linux Network.
   * - Ubuntu
     - Ubuntu 24.04 LTS Release Notes
     - Ubuntu does not require mandatory registration. An optional Ubuntu Pro subscription provides extended security maintenance and support.

Provisioning a New Server
-------------------------

Provisioning a new server allows onboarding new, unmanagedHPE ProLiant servers into a Bare Metal Cloud environment, enablingHPE Morpheus to manage their lifecycle, including automated OS deployment and hardware monitoring.

Importing HPE ProLiant Bare Metal Servers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ImportingHPE ProLiant Bare Metal Servers
Perform the following procedure to importHPE ProLiant Bare Metal Servers:


#. Navigate to
#. Infrastructure
#. >
#. Compute
#. , then select the
#. Bare Metal
#. tab. 
#. Click the
#. + Bare Metal
#. button, then select
#. HPE
#. Server. 
#. Select the
#. Group
#. you created earlier from the drop-down list and click
#. Next.
#. Enter a Name for the server and click
#. Next.
#. Enter the following iLO (Integrated Lights Out) details for the server:   
  - iLO IP Address

 
  - iLO Username (typically \"Administrator\")

 
  - iLO Administrator Password

 

  
#. Leave the Pre-Provisioned Server option unselected, then click
#. Next.
#. Click
#. Next
#. to review your host configuration details. 
#. Click
#. Complete
#. to finalize the host creation.

  
#. The below image shows list of clouds available.

Results
 the HPE ProLiant Bare Metal plugin automatically discovers and records all hardware details from the server using its Integrated Lights Out (iLO) management interface. This discovery process may take a few minutes, depending on the server and network conditions. After completion, the server becomes available (STATUS =available) in Morpheus for further provisioning and lifecycle operations.

Provisioning an Instance
^^^^^^^^^^^^^^^^^^^^^^^^

  Perform the following steps to provision an instance:


#. Navigate to
#. Provisioning
#. >
#. Instances.
#. Click the
#. + ADD.
#. In the
#. TYPE
#. tab, select the
#. Instance Type
#. as
#. HPE
#. Bare Metal (ILO) SERVER.

 
#. In the
#. GROUP
#. tab, complete the Instance Summary fields.

 
#. In the
#. CONFIGURE
#. tab, complete the Configuration Options:   
  0. Layout
  1. : Select the appropriate layout from the drop-down list (for example, Single iLO Server).

 
  2. Plan
  3. : Choose one of the following:

  
    - Generic Plan
    - : Any iLO

 
    - Specific Plan
    - : For example, DL360.Gen10Plus.1-32C.129-256GiB

  
  4. Resource Pool
  5. : Select the required resource pool from the drop-down list.


  6. Volumes
  7. : Configure storage volumes as required. Refer to the Storage section for details. 
    - Enter the name of the volume in the first field.

 
    - Select the volume type from the drop down list.

  
    - NOTE
    - When you select any other option apart from RAID, the system shows additional field to specify storage capacity. Enter the required storage. Ensure that you configure more than 16 GB storage. You cannot specify more than one volume for Windows environment.   
  8. Networks
  9. : Configure network settings as required. Refer to the Networking section for details.

 
  10. Image
  11. : Select the Bare Metal OS image from the drop-down list.

 
  12. Baremetal Host(s)
  13. : Select the target Bare Metal host(s) from the drop-down list if specific server(s) are desired.

 

  
#. In the
#. AUTOMATION
#. tab, select the appropriate options, then click
#. Next.
#. In the
#. REVIEW
#. tab, verify the configuration summary and click
#. Complete.
Post-Provisioning
^^^^^^^^^^^^^^^^^

After provisioning the instance:


* The new instance appears under
* Provisioning
* >
* Instances
* .

  
* To monitor provisioning progress, select the instance from the list.

* Once provisioning completes successfully, review the tabs as required.

* To access the instance console, click the
* Console
* tab

  
* After successful provisioning, verify that the instance and its corresponding bare metal host are listed in:  
  - Under
  - Provisioning
  - >
  - Instances
  - .


  - Under
  - Infrastructure
  - >
  - Bare Metal
  - .


  - Go to the Instances page to view the instance Status, Health, CPU, Memory, and Storage details.

Importing Pre-Provisioned Server
--------------------------------

Importing a Pre-Provisioned server enables administrators to bring existing physical servers and associated resources (networks and storage) into HPE Morpheus. This is the initial step in migrating an existing workload cluster into Morpheus management. It is completed in two phases: 
* Import
* : Import existing servers as Pre-Provisioned resources.

* Convert to Managed
* : Convert imported servers into managed instances, creating Morpheus instances with associated network and storage attachments.

This process is performed one workload cluster at a time, and each cluster can contain one or more servers. Once the initial server is converted, additional imported servers can be added to the same instance using theAdd Nodeoperation.

Import Pre-Provisioned Servers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Perform the following to add a bare metal server:


#. Navigate to
#. Infrastructure
#. >
#. Compute
#. >
#. Bare Metal.
#. Click
#. Add Bare Metal Server.
#. Select the
#. Pre-Provisioned
#. server. 
#. Complete the remaining server details and click
#. Save.
#. NOTE 
#. For Windows
#. : When importing a Pre-Provisioned Windows server, select Windows OS. This is required because some import operations are specific to Windows.

 
#. During import, the
#. HPE
#. BMaaS validates the association between the provided iLO IP and OS IP by executing commands on the host OS. The supplied OS credentials must have elevated privileges: 
  - Linux OS
  - : The user must have sudo privileges.

 
  - Windows OS
  - : The user must be in the Administrators group.

Results
 Once the server is imported, it should be ready to be converted into a fully provisioned node.

Convert to Provisioned Node
```````````````````````````

  Perform the following to convert to Managed or create a new instance:


#. After the server is imported, go to
#. Infrastructure
#. >
#. Compute
#. >
#. Bare Metal.
#. Select the imported server. 
#. Click
#. Convert to Managed.
#. Confirm the server details and click
#. Execute.
#. NOTE
#. Use the same OS credentials that were provided during the import step.      Results
 TheConvert to Managedaction creates a new instance, makes the selected server a fully provisioned node, and adds it to the new instance. It creates the association of this server with networks and volumes inHPE Morpheus, as present in the network switches and the storage array, respectively. In addition, it creates the association of the VLAN interfaces with the IP addresses on the host OS on the server.

Add Additional Nodes
^^^^^^^^^^^^^^^^^^^^

to the Instance
To convert a Pre-Provisioned server into a fully provisioned node, and to make it part of an existing instance, the Add Node action is used, from the context of the Instance to which it is desired to be added.

 Once an instance is created with the first converted node, you can add other imported servers to the same instance:


#. Navigate to
#. Provisioning
#. >
#. Instances.
#. Select the newly created instance. 
#. Click
#. Add Node.
#. Select
#. Pre-Provisioned.
#. Choose the imported server and provide the required details. 
#. Click
#. Execute
#. .     Results
 This converts the selected imported server into a managed node and adds it to the existing instance.

