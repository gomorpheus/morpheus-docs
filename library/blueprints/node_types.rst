Node Types
----------

Node Types are the link between Images and Layouts.

Node Type Configuration Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following fields are for all Technology types:

Name
  Name of the Node Type in |morpheus|
Short Name
  The short name is a lowercase name with no spaces used for display in your container list
Version
  Version for the Node Type. Examples: 7.5, 2012 R2, latest
Technology
  Select associated Technology. This will filter the available configuration options, images and which Layouts the Node Type can be added to
Environment Variables
  Add pre-set environment variables to the Node Type
Category
  Node Types of differing categories within the same Layout can have differing sizing

Technology-Specific Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Options fields will change depending on the Technology option selected. For VM provisioning technology options, select an image from the VM Image dropdown. This list is populated from the |morpheus| Virtual Images section and will include images uploaded into |morpheus| as well as synced images from added clouds.

.. NOTE:: Amazon and Azure Marketplace Images can be added in the Virtual Images section for use as Node Types in custom library items.

Docker Options
````````````````````

For Docker, type in the name and version of the Docker Image, then select the integrated registry.

Service Ports
  To open ports on the node, enter the name and port to expose. The Load Balancer HTTP, HTTPS, or TCP setting is required when attaching to Load Balancers.

  Defining an Exposed port will also create a hyperlink(s) on the container location (IP) in the VM or Container section of the associated Instance detail page.

Scripts
  Search for and select one or multiple scripts to be executed when the Node Type is provisioned

File Templates
  Search for and select one or multiple File Templates to be written when the Node Type is provisioned

Example port configuration:

.. image:: /images/provisioning/library/node_ports.png

VMware Options
````````````````````

|morpheus| supports VMware-specific configurations related to Node Types targeted for VMware vCenter Clouds. Setting the TECHNOLOGY field on the Node Type to "VMware" reveals these fields.

**vApp Properties**

Some VMware images may expect the user to provide values for vApp properties related to server configuration. |morpheus| allows the user to set values for vApp properties on the Node Type, which can be static values or even |morpheus| variables such as if we wanted to provide the next available IP address from a |morpheus| IP pool or source a password from |morpheus| Cypher. Consider the following example workflow for examining an OVA image, uploading it to |morpheus| as a Virtual Image, and setting vApp properties on the Node Type.

If you have an OVA that doesn't have the properties laid out in a visible format, you can unzip it and inspect the OVF file to help set the vApp properties in |morpheus|. For example, take a look at the screenshot below from an OVF file associated with an F5 image. There are four vApp properties I wish to set related to network and user configuration. The ``userConfigurable`` property should be toggled to ``true`` for any that may be set to ``false``. The key is identified by the ``key`` property and, if desired, default values can be set via the ``value`` property. Save any changes to the OVF file.

.. image:: /images/provisioning/library/vappProps/vappOvf.png

With changes saved, the image can be uploaded to |morpheus| as a Virtual Image from which we can create and configure a Node Type. Below you can see the Virtual Image uploaded and revealed on the Virtual Images list page.

.. image:: /images/provisioning/library/vappProps/vappVirtualImage.png

Next, create a new Node Type. After setting the TECHNOLOGY value to "VMware" the fields related to vApp Property configuration will be revealed. Select the uploaded Virtual Image as the "VM IMAGE" and set the key/value pairs in VAPP PROPERTIES. In this case, I've dynamically loaded the values using |morpheus| variables.

.. image:: /images/provisioning/library/vappProps/vappNodeType.png

The rest of the process is the same as building out any other |morpheus| library item. House the Node Type within a Layout and the Layout within an Instance Type. It should then be provisionable as any other Instance Type.

**Extra Options**

When VMware Technology Type is selected, EXTRA OPTIONS will be available in the VMware VM Options section. These allow defining Advance vmx-file parameters during provisioning.

Some Example include:

.. code-block:: bash

  tools.setinfo.sizeLimit : 1048576
  vmci0.unrestricted : FALSE
  isolation.tools.diskWiper.disable : TRUE

.. NOTE:: Not all parameters can be set using extra config parameters. A sample reference list can be found at http://www.sanbarrow.com/vmx/vmx-advanced.html#vmx

.. IMPORTANT:: Use caution when setting Extra Options. Malformed config files can break provisioning. Troubleshooting issues related to Extra Options defined are beyond the scope of |morpheus| product support.
