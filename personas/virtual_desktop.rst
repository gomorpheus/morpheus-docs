Virtual Desktop Persona
=======================

.. vdi_persona

The Morpheus VDI Persona provides a virtual desktop environment to grant users access to workstations and applications in a secure manner. Deploy pools of virtual machines on any supported |morpheus| Cloud for users to reserve and use! |morpheus| leverages open source client technologies, such as Apache Guacamole, to provide a performant and secure virtual desktop client for the end user while wrapping its frontend in a completely new framework. For information on configuring VDI pools for consumption in the Virtual Desktop Persona, see the `Tools section <https://docs.morpheusdata.com/en/latest/tools/vdi_pools.html>`_ of |morpheus| docs.

.. NOTE:: This is not an integration with existing VDI Pool Managers such as VMWare Horizon, Citrix VDI, or Nutanix XiFrame. It is a standalone |morpheus| feature.

.. thumbnail:: /images/personas/vdi/vdPersona2.png

Key Features
------------

- VDI Pool Management
- Virtual Desktop Persona
- RDP/SSH/VNC Console Support
- RDP Remote App Support
- Clipboard Copy/Paste
- HiDPI Support
- Auto Compression Scanning based on User Bandwidth
- Audio Playback (RDP)
- Local Printer (RDP)
- Auto-Resize
- Auto-Login based on |morpheus| User Settings
- Customizable User Background

Configuring Access to the Virtual Desktop Persona
-------------------------------------------------

Access to the Virtual Desktop Persona and individual VDI pools is handled through the user Role and, where applicable, Tenant Role. When creating a new Role, access is restricted to the Virtual Desktop Persona and all VDI pools by default. To grant access:

#. Navigate to the Role (|AdmRol| > Selected Role)
#. Access the Personas tab
#. Toggle the Virtual Desktop permission to "Full" or "None"
#. Access the VDI Pool Access tab
#. Toggle access to selected VDI pools to "Full" or "None", you can also toggle permission on all pools to "Full" or "None" with the Global Access selection
#. Role changes are saved automatically, there is no need to manually save

Launching a VDI Instance
------------------------

VDI Instances are launched from the Virtual Desktops Persona. Depending on Role permissions, your account may default to this view or may even restrict you solely to this view. To access the Virtual Desktops Persona from the standard view or from another Persona, click on the user's name in the upper-right corner of the application window. When available, this dropdown menu will list the standard |morpheus| Persona view as well as any other Personas the user has permission to access. Click on Virtual Desktop to access the Virtual Desktop Persona.

The Virtual Desktop Persona view lists out each of the virtual desktop types they can access. Click on the desired virtual desktop type to launch it. If there are virtual apps available for any listed desktop types, they are presented in a flyout menu alongside a "desktop" option to access the base OS over an individual app. Items categorized as "Desktops" are VDI pools configured in the Tools menu of the Standard Persona. Items categorized as "Instances" are Instances favorited by the current user in the Standard Persona (if they have access and they have favorited any Instances). Clicking on an Instance tile offers quick access to the Instance console.

.. IMPORTANT:: Virtual Desktops are launched in a pop-up window. Be sure your web browser is not blocking pop-ups or create an appropriate exception for |morpheus| virtual desktop pop-ups.

Changing the Virtual Desktop Persona Background
-----------------------------------------------

The |morpheus| Virtual Desktop Persona includes default backgrounds for an elegant look out of the box. If desired, users may change this background to suit personal taste or organizational branding. This change is unique to each individual account. At this time, there is no option for appliance-wide whitelabeling for Virtual Desktop Persona backgrounds.

#. Click on the user's name in the far upper-right corner of the application window
#. Click USER SETTINGS
#. The section for "VDI Settings" is in the lower-right corner of the page
#. Mark the RESET box and click :guilabel:`SAVE` to reset the Virtual Desktop Persona to the default background
#. Click "Browse" and upload a local image to add a custom background
#. Click :guilabel:`SAVE`
