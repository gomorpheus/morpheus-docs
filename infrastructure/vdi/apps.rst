.. _vdi-apps:

VDI Applications
================

Overview
--------

VDI Applications (VDI Apps) are shortcut applications that can be used to launch an RDP session for Windows VDI Desktops into a particular application. They leverage Guacamole's remote-app property to open a specific application rather than a full desktop session.

VDI Apps are managed from ``Tools > VDI Pools > Apps`` tab and are consumed by users within the Virtual Desktop Persona.

.. NOTE:: VDI Apps require the ``services-vdi-pools`` Role permission (Read or Full).

Creating a VDI App
-------------------

#. Navigate to ``Tools > VDI Pools``
#. Select the **Apps** tab
#. Click :guilabel:`+ ADD`
#. Configure the following:

   NAME
     Display name for the application (shown to end users in the Virtual Desktop Persona)
   DESCRIPTION
     Optional description of the application
   LAUNCH PREFIX
     The RemoteApp program identifier. This **must** start with ``||`` followed by the application executable name.

     Examples:

     - ``||notepad`` — Launches Notepad
     - ``||mstsc`` — Launches Remote Desktop Connection
     - ``||winword`` — Launches Microsoft Word
     - ``||excel`` — Launches Microsoft Excel
     - ``||chrome`` — Launches Google Chrome

   LOGO
     Upload a custom icon for the application. Supported formats: PNG, JPEG, SVG. The image is displayed at multiple resolutions (20x20, 42x42, 84x84 for HiDPI).

#. Click :guilabel:`SAVE`

.. IMPORTANT:: The Launch Prefix must begin with ``||`` (double pipe). This is the RemoteApp protocol prefix required by Guacamole. Entries without this prefix will fail validation.

Editing a VDI App
------------------

#. Navigate to ``Tools > VDI Pools > Apps``
#. Click on the App name or select the edit action
#. Modify fields as needed
#. Click :guilabel:`SAVE`

Deleting a VDI App
-------------------

#. Navigate to ``Tools > VDI Pools > Apps``
#. Select the App to delete
#. Click :guilabel:`DELETE`
#. Confirm deletion

Using VDI Apps
--------------

End users access VDI Apps through the Virtual Desktop Persona:

#. User logs into |morpheus| and switches to the Virtual Desktop Persona
#. Available VDI Apps are displayed with their configured icons
#. Clicking an App icon launches an RDP session directly into the specified application
#. The session connects to an available VDI Pool allocation and opens the RemoteApp

VDI Apps work in conjunction with VDI Pools:

- The App defines *what* application to open
- The Pool provides *where* (which VM) the application runs
- Allocations manage *which user* gets *which VM*

Requirements for RemoteApp
---------------------------

For VDI Apps to function correctly, the Windows VDI template must be configured for RemoteApp:

1. The target application must be installed on the VDI template/image
2. The application must be registered as a RemoteApp program on the Windows host
3. The RDP configuration must allow RemoteApp connections

To register an application as a RemoteApp on Windows Server:

.. code-block:: powershell

   # Add a RemoteApp program
   New-RDRemoteApp -CollectionName "VDI" -DisplayName "Notepad" -FilePath "C:\Windows\notepad.exe"

For Windows 10/11 desktops, configure via Group Policy or registry:

.. code-block:: text

   HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Terminal Server\TSAppAllowList

API Reference
--------------

VDI Apps are also manageable via the |morpheus| API:

- ``GET /api/vdi-apps`` — List all VDI Apps
- ``GET /api/vdi-apps/:id`` — Get a specific VDI App
- ``POST /api/vdi-apps`` — Create a VDI App
- ``PUT /api/vdi-apps/:id`` — Update a VDI App
- ``DELETE /api/vdi-apps/:id`` — Delete a VDI App
