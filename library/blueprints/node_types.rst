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

When VMware Technology Type is selected, EXTRA OPTIONS will be available in the VMware VM Options section. These allow defining Advance vmx-file parameters during provisioning.

Some Example include:

.. code-block:: bash

  tools.setinfo.sizeLimit : 1048576
  vmci0.unrestricted : FALSE
  isolation.tools.diskWiper.disable : TRUE

.. NOTE:: Not all parameters can be set using extra config parameters. A sample reference list can be found at http://www.sanbarrow.com/vmx/vmx-advanced.html#vmx

.. IMPORTANT:: Use caution when setting Extra Options. Malformed config files can break provisioning. Troubleshooting issues related to Extra Options defined are beyond the scope of |morpheus| product support.
