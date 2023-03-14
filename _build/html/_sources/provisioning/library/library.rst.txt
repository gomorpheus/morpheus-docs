Library
=======

Overview
--------

The Library section is used to add virtual images as custom instances to the provisioning catalog. The Library Section is composed of:

* Instance Types
* Layouts
* Node Types
* Option Types
* Option Lists
* Templates
* Scripts

Uploaded or synced images from the virtual images section are added to nodes, a node or multiple nodes are added to layouts, and layouts are added to Instance Types. Scripts and Templates can be attached to nodes, with phased execution options for scripts.

Instance Types
--------------

Types___Library___|morpheus| _salt_library_item.png

Adding an Instance Type creates a new Library Item category. Multiple layouts can be added to an instance type, and these layout can have different nodes attached. The instance wizard will present the layout options compatible with the selected cloud. If cloud selection is turned off, all layouts will be presented for all cloud types accessible by the user.

Name::
Name of the Instance Type in the Provisioning Library
Code::
Useful shortcode for provisioning naming schemes and export reference.
Description::
The description of the Instance Type shown in the Provisioning Library.
255 characters max
Category::
For filtering in Instance sections and Provisioning Wizard
* Web
* SQL
* NoSLQ
* Apps
* Network
* Messaging
* Cache
* OS
* Cloud
* Utility
Icon::
Suggested Dimensions: 150 x 51
Visibility::
* Private- Only accessibly by assigned Accounts/Tenants
* Public- accessible by all Accounts/Tenants
Environment Prefix::
Used for exportable environment variables when tying instance types together environment Variables in app contexts. If not specified a name will be generated
Enable Scaling (Horizontal)::
Enables load balancer assignment and auto-scaling features
Supports Deployments::
Enables deployment features
(Requires a data volume be configured on each version. Files will be copied into this location)

Upon saving, this Instance Type will be available in the Provisioning Catalog, per user role access. However we still need to add layouts to the Instance Type, and prior to creating a layout, we will add a node type.

Node Types
----------

salt_node_type.png

The following fields are for all node technology types:

* Name
* Short Name
* Version
* Category
* Technology
** Azure
** Docker
** Google
** Hyper-V
** KVM
** Nutanix
** OpenStack
** VMware
** Xen
* Environment Variables

The Options fields will change depending on the Technology option selected.

For VM provisioning technology options, select an image from the VM Image dropdown, which is populated from the Virtual Images Section and will include images uploaded into |morpheus| , and synced images from added clouds.

.. NOTE:: Azure Marketplace images and Amazon AMI's can now be added in the Virtual Images section for use as node types in custom library items.

For Docker, type in the name and version of the Docker Image and select the integrated registry.

Expose Ports
  To open port on the node, select "Add Port" and enter the name and port to expose. The Load Balancer http, https or tcp setting is only required when attaching to load balancers.

Example port configuration:

node_ports.png

Scripts & Templates
-------------------

To attach scripts and templates that have been added to the Library to a node type, start typing the name and then select the script(s) and/or template(s).

** Multiple scripts and templates can be added to a node type
** Scripts and Templates can be added/shared among multiple node types
** The Execution Phase can be set for scripts in the Scripts section.
** Search will populate Scripts or Templates containing the characters entered anywhere in their name, not just the first letter(s) of the name.

Upon save the Node Type will be created, and available for adding to layouts.

Layouts
-------

salt_new_layout.png

Layouts are added to Instance types, and will be presented under the Configuration Options dropdown in the Provisioning Wizard for that Instance type.

Instance Type::
Select the Instance Type to add the new Layout to. Custom Instance Types must already be created and one layout cannot be added to multiple instance types, or change Instance Types after creation.

.. NOTE:: Layouts cannot be added to |morpheus| provided library items at this time.

Name::
The name the layout will present as in the Configuration Options dropdown in the provisioning wizard
Version::
The version number or name for the Layout. Layouts in an Instance Type with the same version will all show under the Configuration Options dropdown when that version in selected while provisioning.
Description:: Description of the layout
Technology::
Technology determines which cloud this layout will be available for.
Environment Variables::
Nodes::
Single or multiple nodes can be added to a Layout by searching for and selecting the node(s). An example of a layout with multiple nodes is the Hyper-V MySQL Master/Slave layout pictured below (note this is the Layout detail screen after the layout has been created.)
Multi-node Layout example:

hyper-v_master_slave.png



Upon save, the layout will be attached to the selected Instance Type, and available when provisioning that Instance Type for the appropriate cloud technology.

salt_instance_type_layout_detail.png



Option Types
------------

Option Types allow you to create additional fields within the provisioning wizard.

OptionType.png

These field entries can then be used in scripts and templates using our variable naming convention (more here).

variable.png



Option List
-----------

Much like Option Types, Option Lists allow you to give the user more choices during provisioning to then be passed to scripts and/or automation.  Option Lists, however, are pre-defined insofar as they are not free-form. They can either be manually entered CSV or JSON or they can be dynamically compiled from REST calls via GET or POST requests.

optionlist.png



OptionListREST.png



Your new Library Item is now ready for provisioning. Multiple Layouts with multiple technologies can be added to a single Instance Type. For example, the Layouts for the |morpheus| Apache Instance Type, with multiple layouts for many different cloud technologies and nodes is pictured below:
