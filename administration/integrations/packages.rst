Packages
--------

Overview
^^^^^^^^

Packages are code files used to define |morpheus| resources, which can then be uploaded and used in any |morpheus| appliance they may be needed in. |morpheus| packages (.morpkg, .mpkg, or .mopkg) are added in the |AdmIntPac| section of the UI. |morpheus| packages contain Library and automation objects, such as Instance Types, Layouts, Node Types, Tasks, Spec Temples and Cluster Layouts. Following upload of a valid package, the defined |morpheus| resources are immediately available for use in the appliance.

The addition of ``/administration/packages`` is primarily targeted for uploading future |morpheus|-provided packages, however users can create, distribute and/or import custom |morpheus| packages too. This section goes over the process for writing and preparing packages for upload to a |morpheus| appliance.

Role Permissions
^^^^^^^^^^^^^^^^

Access and capabilities for the **Packages** section is determined by the following role permissions:

Role: Feature Access: ``Admin: Plugins``
  - None: Cannot access Admin: Plugins section
  - Full: Access to Admin: Plugins and ability to upload |morpheus| packages (``.morpkg``, ``.mpkg``, or ``.mopkg``)

Getting Started
^^^^^^^^^^^^^^^

Packages consist of two primary parts, a ``.json`` manifest file (which sets some metadata about the package) and one or more ``.scribe`` files which define the resources to be added. These files are zipped and imported into |morpheus| as one file (``.morpkg``, ``.mpkg``, or ``.mopkg``). Scribe files are written in HCL (Hashicorp Configuration Language) and follow referenced resource naming. In the next section, we will define the required attributes for both the ``.json`` manifest and the scribe files with examples.

When uploading packages to |morpheus|, keep in mind that the same packages can be reinstalled as many times as desired. When the same package is reinstalled, any local changes to those resources made in the |morpheus| appliance will be overwritten. For example, if a Task has been created by package and changes are made locally to the Task config within |morpheus|, subsequent uploads of the packages would overwrite those changes. A better method for making changes to package-sourced resources would be to update the package code, increase the version number, and upload the package once again. This ensures important local changes would not be overwritten by subsequent uploads. There is no warning given in the UI, changes are simply overwritten without notice.

Additionally, it's worth noting that while packages can be deleted (|trash| icon on the packages detail page), you will simply delete the package from the list. |morpheus| will show a helpful list of resources added with the package if cleanup is desired but will not delete them.

Creating Packages
^^^^^^^^^^^^^^^^^

As noted in the last section, a package consists of a ``.json`` manifest file and any number of ``.scribe`` files. We'll first look at the manifest file, its purpose, and attributes that must be included in the JSON map.

A typical package manifest looks like this:

.. code-block:: bash

  {
      "type": "scribe",
      "name": "morpheus-ubuntu-22.04-vmware",
      "code": "morpheus-ubuntu-22.04-vmware",
      "organization": "morpheus",
      "version": "20240415"
  }

The manifest includes each of the following attributes:

- **TYPE:** Tells |morpheus| to process all included files with the package as scribe files. Currently, this is the only supported type
- **NAME:** This is the name for the package that will appear in |morpheus| UI. The example manifest above came from a package that adds resources for an Ubuntu 22.04 library item to |morpheus|, and is named to indicate that
- **CODE:** Not visible in UI but exists for referencing the package via |morpheus| API
- **ORGANIZATION:** Appears only in the database but can be exposed via |morpheus| API
- **VERSION:** Listed in |morpheus| UI and is useful for tracking changes over time to package-sourced resources

Scribe files are quite a bit more complicated and have not yet been fully documented publicly. Nevertheless, we can show a couple examples here and give strategies for extracting additional examples from your own environment. Certain resources will require reference to other resources included with the scribe file. Here's a simple scribe file creating a shell script-type "Hello World" Task:

.. code-block:: bash

  resource "task" "HelloWorld" {
    name = "HelloWorld"
    uuid = "2c2306e0-3b30-4886-b8a3-d1362c9b9490"
    dateCreated = "2024-04-19T19:15:47.000Z"
    executeTarget = "resource"
    labels = [ "export" ]
    lastUpdated = "2024-04-19T19:18:40.000Z"
    options = [
      { optionType = { code = "shell.sudo" }, value = "on" },
      {
        content = { uuid = "ff5de589-75da-48ec-ba66-5fe5905397b0" }
        optionType = { code = "script" }
      }
    ]
    taskType = { code = "script" }
  }

  resource "file-content" "ff5de589-75da-48ec-ba66-5fe5905397b0" {
    uuid = "ff5de589-75da-48ec-ba66-5fe5905397b0"
    content = "echo \"Hello World\""
    dateCreated = "2024-04-19T19:15:47.000Z"
    lastUpdated = "2024-04-19T19:15:47.000Z"
  }

In this case, the Task config was written locally in the Add/Edit Task modal within |morpheus| rather than sourced from elsewhere (such as a Github repository). The Task content itself is a distinct resource and is referenced in the Task resource by UUID. Outside resources can also be referenced by HCL referenced resource naming such as in the following example where a ``workload-type`` resource references a ``virtual-image`` resource:

.. code-block:: bash

  resource "virtual-image" "vmware_vsphere_image_morpheus_almalinux_9_20240324" {
    code = "vmware_vsphere_image_morpheus_almalinux_9_20240324"
    category = "vmware.vsphere.image.morpheus.almalinux"
    name = "Morpheus AlmaLinux 9 XX-DATE-XX"
    imageType = "vmdk"
    remotePath = "https://s3-us-west-1.amazonaws.com/morpheus-images/vmware/20240324/almalinux-9/morpheus-almalinux-9-x86_64-20240324.ovf"
    imagePath = "vmware/20240324/almalinux-9"
    isCloudInit = true
    systemImage = true
    installAgent = true
    osType {
      code = "almalinux.9.64"
    }
    zoneType = "vmware"
  }

  resource "workload-type" "vmware_almalinux_9" {
    code = "vmware-almalinux-9"
    shortName = "almalinux"
    name = "AlmaLinux 9"
    ports = [22]
    containerVersion = "9"
    entryPoint = ""
    mountLogs = "/var/log"
    statTypeCode = "vm"
    logTypeCode = "vm"
    showServerLogs = true
    category = "almalinux"
    cloneType = "almalinux"
    priorityOrder = 0
    serverType = "vm"
    providerType = "vmware"
    containerPorts = [{code = "almalinux.22"}]
    actions = [{code = "generic-remove-node"}]
    checkTypeCode = "containerCheck"
    virtualImage = virtual-image.vmware_vsphere_image_morpheus_almalinux_9_20240324
    provisionType = "vmware"
    backupType = "vmwareSnapshot"

The specific virtual image is referenced as ``virtual-image.vmware_vsphere_image_morpheus_almalinux_9_20240324``.

To go further, you can generate additional examples from your own environments. Use the `Import/Export <https://docs.morpheusdata.com/en/latest/provisioning/code/code.html#import-and-export>`_ feature built into |morpheus| and export your created resources into integrated Git repositories. When viewing the results in your repositories, you'll see the resources are exported as scribe files.

Preparing and Uploading Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To prepare the package, ensure the manifest and scribe files are gathered into one directory. You'll then need to zip the contents of that directory with a valid extension (``.morpkg``, ``.mpkg``, or ``.mopkg``). In Linux, from outside the directory, you can use: ``zip -j <package-name>.mpkg <directory-name>/*``. The package is now ready to be uploaded. Navigate to |AdmIntPac| on any appliance and use the file picker tool to upload your new package file.
