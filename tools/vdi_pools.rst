VDI Pools (beta)
================

The VDI Pools section of the Tools section provides a management area for defining VDI Pools and VDI Apps that a user can consume within the VDI Persona.

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
- **ALLOW HYPERVISOR CONSOLE:** When checked, virtual desktop users have the ability to access the hypervisor console through a dropdown menu in the upper-right corner of the virtual desktop display window
- **AUTO CREATE LOCAL USER UPON RESERVATION:** When marked, the user configured in |morpheus| user settings will be created when the machine is initially accessed. If unchecked or if there is no user configured in |morpheus| user settings, ensure the machine is joining a domain or there is a known user on the machine image in order to allow access
- **CONFIGURE:** Click this button to configure the machines that will be created when reserved by users. The wizard is identical to the Instance provisioning wizard meaning all available Instance Types, Workflows, and more are available to virtual desktop machine creation
- **LOGO:** Upload or select a logo to represent the virtual desktop type to users
- **VDI APPS:** Optionally select one or more frequently-used applications the user can launch directly. Users will also have the option to launch into the desktop

.. image:: /images/personas/vdi/createVdiPool.png
  :width: 50%

Creating or Editing a VDI Apps
------------------------------

VDI Apps allow users to launch directly into commonly-used apps rather than the OS desktop. Currently, VDI Apps only work with RDP Windows Instances. Create remote app registries for the needed applications and configure associated VDI Apps in |morpheus| as described below. See our associated KnowledgeBase article for more information on getting started with remote app registries.

VDI Apps are created by selecting :guilabel:`+ ADD` from the VDI Apps tab or edit an existing one by clicking on the pencil icon from the appropriate row. Configure the following, fields containing a vertical blue bar along the left edge are required:

- **NAME:** A friendly name for the VDI App in |morpheus|
- **DESCRIPTION:** A description of the virtual app type
- **LAUNCH PREFIX:** A reference to the remote app registry prepended with two pipes ( || ). For example, we might create a registry "Chrome" for a Chrome browser VDI App and the associated launch prefix would be "||Chrome"
- **LOGO:** Upload or select a logo to represent the virtual app type to users
