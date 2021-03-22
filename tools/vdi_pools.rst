VDI Pools (beta)
================

.. vdi_pool_config

The VDI Pools section of |morpheus| Tools provides a management area for defining VDI Pools and VDI Apps that a user can consume within the `Virtual Desktop Persona <https://docs.morpheusdata.com/en/latest/personas/personas.html#morpheus-virtual-desktop-environments-beta>`_.

Pools can be either persistent or non-persistent and have various controls pertaining to idle pools and minimum or maximum sizes. The idea here is to make sure a server is always quickly available to accommodate user demand.

|morpheus| leverages its Instance Types concept for provisioning servers within the VDI Pool. All the options available during Instance provisioning is available for setting the base server configuration. This includes Workflows, domain joins, tagging, image selection and more.

A timeout setting can also be applied to release pool allocations from a user once they have disconnected their session. For non-persistent pools, a good recommendation is ten minutes whereas, for a persistent pool, a sensible recommendation would be around one hour.

Pool behavior changes depending on the pool type. In a non-persistent pool, when a timeout period expires, the VM is destroyed and a new one is allocated for use. This functionality will change based on the cloud technology in a future update allowing for potential recycling of the VMs. In a Persistent pool, when the lease timeout expires, the Instance will shutdown until the user requests it again in the future. It is important to note that lease timeouts auto-extend for as long as the user is logged into or browsing any area of the |morpheus| application. Once the user closes their browser or logs out of their session, the timeouts will no longer auto-extend.

Configuring Access to VDI Pools
-------------------------------

Access to the Virtual Desktop Persona and individual VDI pools is handled through the user Role and, where applicable, Tenant Role. When creating a new Role, access is restricted to the Virtual Desktop Persona and all VDI pools by default. To grant access:

#. Navigate to the Role (Administration > Roles > Selected Role)
#. Access the Personas tab
#. Toggle the Virtual Desktop permission to "Full" or "None"
#. Access the VDI Pool Access tab
#. Toggle access to selected VDI pools to "Full" or "None", you can also toggle permission on all pools to "Full" or "None" with the Global Access selection
#. Role changes are saved automatically, there is no need to manually save

Additionally, users should have a Linux and/or Windows username and password configured in their user profiles in order for virtual desktop login to be as seamless as possible. User profiles are accessed by clicking on the user's name in the upper-right corner of the application windows and clicking USER SETTINGS. The section to enter Windows and Linux account credentials is in the right column of the page.

Creating VDI Templates
----------------------

.. NOTE:: The following guide focuses on VMware and Windows but is applicable to most cloud environments. |morpheus| also supports Linux virtual desktops.

#. Create a thin-provisioned VM in the VMware vCenter console. It's recommended you allocate at least 50 GB of storage, at least 2 vCPU and at least 8 GB RAM on the template. Smaller VMs can be deployed from this template later.
#. Install a Windows operating system, there is no need to supply a license during deployment.
#. Supply the initial username and password
#. Install any updates, applications or optimizations. See the next section for recommended optimizations for the most performant virtual desktop experience
#. Shutdown the VM and convert to a template. Optionally, you can also use the Linked Clones (VMware) process which is described in a later section

Suggested Optimizations
^^^^^^^^^^^^^^^^^^^^^^^

Reducing display and input delays is key to providing the best virtual desktop experience for the user. Consider the following optimizations for VDI desktops and servers:

- Disable desktop wallpapers
- Implement Roaming Profiles
- Enforce WDDM remote display driver
- Re-enable local Administrator
- Delete the initial created user profile
- Clean up any unneeded installer packages

Additionally, there are a number of OS optimization tools available on the Internet which are specific to VDI use cases.

Linked Clones
^^^^^^^^^^^^^

Linked Clones are a feature of VMware which references snapshots of a VM to deploy from. This adds the advantage of quicker clone times and the ability to more easily share small modifications to a file system. |morpheus| supports Linked Clones but recommends them for VDI workloads only.

.. NOTE:: Linked Clones are not templates but rather powered down VMs.

#. Locate the VM you desire to have the Linked Clone in |morpheus|. If it's not currently managed by |morpheus|, navigate to the appropriate Cloud (Infrastructure > Clouds), find the VM on the "VMs" tab, and click "Convert to Managed" from the ACTIONS menu
#. In the CONVERT TO INSTANCE modal, select "No Agent Install" in the AGENT field
#. If snapshots are already on the VM, these will now be synced by |morpheus|. If you have not yet created a snapshot, do so in the vCenter console (and refresh the Cloud integration in |morpheus| afterward) or from the ACTIONS menu in |morpheus| itself. Be sure to take a snapshot of a powered-off VM and give the snapshot a name that will be identifiable for administrators
#. From the Instance detail page in |morpheus|, navigate to the Backups tab to find the snapshot
#. Select "More" and create the Linked Clone
#. The Linked Clone will now appear in the |morpheus| Virtual Image repository (Provisioning > Virtual Images), ready to use with your custom Layouts

.. NOTE:: You should modify the Virtual Image to "Force Guest Customization" unless you ``sysprep`` your VM at shutdown time

Creating or Editing a VDI Pool
------------------------------

VDI pools are configured from the Tools menu (VDI Pools selection). The following information is displayed in the VDI pools list view, bear in mind some fields may be hidden depending on how you've configured your VDI pools list view (gear icon):

- **TYPE:** An icon indicating the machine type associated with the pool. |morpheus| includes many logos out of the box and also allows users to set their own custom icons
- **NAME:** The friendly name given to the VDI pool
- **PERSISTENT:** A check mark will appear when the VDI pool is configured for persistent virtual desktops
- **ENABLED:** A check mark will appear when the VDI pool is enabled and visible to users whose Role permissions allow them access
- **POOL USAGE:** A graph representing the usage of the VDI pool. The total length of the bar represents the maximum pool size based on the configuration. Green segments represent available virtual desktops, blue segments represent reserved virtual desktops, yellow segments represent virtual desktops which are being prepared, and gray segments represent additional pool capacity which could be made available depending on how many virtual desktops are currently reserved and how many idle machines you've configured the pool to keep available
- **DESCRIPTION:** A description of the virtual desktop type, if provided

.. image:: /images/personas/vdi/vdiPools.png

Create a VDI pool by selecting :guilabel:`+ ADD` from the VDI Pools tab or edit an existing one by clicking on the pencil icon from the appropriate row. Configure the following, fields containing a vertical blue bar along the left edge are required:

- **NAME:** A friendly name for the VDI pool in |morpheus|
- **DESCRIPTION:** A description of the virtual desktop type
- **MIN IDLE:** The minimum number of virtual desktops that should remain idle and ready
- **INITIAL POOL SIZE:** The number of virtual desktops that will be prepared when the pool is created or enabled
- **MAX IDLE:** The maximum number of virtual desktops that remain idle and ready. Machines will be shut down as necessary when this number is exceeded due to users vacating their machines
- **MAX SIZE:** The total number of virtual desktops this pool can have. Additional users will not be able to access machines once this number is reached
- **LEASE TIMEOUT (MINUTES):** The user lease time on a virtual desktop they've reserved. The lease will continue to auto-renew itself as long as the user is logged into |morpheus|. Once the user has logged out and the lease timeout period has expired, the machine will be released as appropriate based on your configuration
- **PERSISTENT:** Pools with persistent virtual desktops will reserve a machine for each user in order to preserve settings, installed applications, work files and more. Machines in persistent pools will be shut down rather than destroyed when they are no longer in use
- **ALLOW HYPERVISOR CONSOLE:** When checked, native cloud console will be enabled (if available) rather than using |morpheus|-native RDP/SSH capability
- **AUTO CREATE LOCAL USER UPON RESERVATION:** When marked, the user configured in |morpheus| user settings will be created when the machine is initially accessed. If unchecked or if there is no user configured in |morpheus| user settings, ensure the machine is joining a domain or there is a known user on the machine image in order to allow access
- **ENABLED:** When marked, the initial pool size will begin to deploy once the VDI pool is saved. The icon for this desktop environment will also be presented to Virtual Desktop Persona users
- **CONFIGURE:** Click this button to configure the deployment configuration each system will use. The wizard is identical to the Instance provisioning wizard meaning all available Instance Types, Workflows, and more are available to virtual desktop machine creation. Consult the steps above to see an example VDI image prep walkthrough
- **LOGO:** Upload or select a logo to represent the virtual desktop type to users
- **VDI APPS:** Optionally select one or more frequently-used applications the user can launch directly. Users will also have the option to launch into the desktop

.. image:: /images/personas/vdi/createVdiPool.png
  :width: 50%

Creating or Editing a VDI Apps
------------------------------

VDI Apps allow users to launch directly into commonly-used apps rather than the OS desktop. Currently, VDI Apps only work with RDP Windows Instances, taking advantage of native Windows Remote Application functionality. Natively-hosted remote desktop applications can only be presented from Windows 10 Enterprise and Education. Other versions of Windows 10 can present remote applications using the procedure below:

#. Open the Windows Registry Editor
#. Locate the following entry: ``HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Terminal Server\TSAppAllowList``
#. Navigate to ``fDisabledAllowList`` and set its value to "1" in the right-hand pane
#. Add a new key under ``TSAppAllowList`` and name it "Applications"
#. Add a new key under "Applications" using any name you'd like
#. Within this new key, create two new string values, one called "Name" and one called "Path"
#. The string value for "Name" should describe the application (ex. "Notepad")
#. The string value for "Path" should be the absolute path to the executable for that application (ex. "C:\Windows\System32\notepad.exe")

VDI Apps are created by selecting :guilabel:`+ ADD` from the VDI Apps tab or edit an existing one by clicking on the pencil icon from the appropriate row. Configure the following, fields containing a vertical blue bar along the left edge are required:

- **NAME:** A friendly name for the VDI App in |morpheus|
- **DESCRIPTION:** A description of the virtual app type
- **LAUNCH PREFIX:** A reference to the remote app registry prepended with two pipes ( || ). For example, we might create a registry "Chrome" for a Chrome browser VDI App and the associated launch prefix would be "||Chrome"
- **LOGO:** Upload or select a logo to represent the virtual app type to users
