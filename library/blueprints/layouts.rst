Layouts
-------

Layouts are attached to Instance Types. A Layout can only be attached to a single Instance Type and a single Technology. An Instance Type can have one or many Layouts attached to it, allowing for a single Instance Type to work with any Technology type. Node Types are added to Layouts. A Layout can have one or many node types attached to it. Node types can be shared across Layouts of matching Technology types.

.. important:: Once an Instance Type is defined on a Layout and saved, the Instance Type setting and Technology selections on the Layout cannot be changed.

Layout List View
^^^^^^^^^^^^^^^^

The default page for Layouts is the Layout list view. Select :guilabel:`+ ADD` to create a new Layout. Layouts can also be created from an Instance Type detail page.

The following fields are displayed for each Layout:

- **NAME:** Links to the Layout detail page
- **VERSION**
- **INSTANCE TYPE:** Links to the associated Instance Type
- **DESCRIPTION**

The Actions menu in each row reveals the following options:

- **Permissions:** Scope the Layout to Group(s) to narrow the list of available groups for a chosen Instance Type at provision time
- **Edit:** Edit the Layout
- **Delete:** Delete the Layout

.. note:: A Layout that is in use cannot be deleted.

Available Filters:

- **Technology:** Display Layouts by selected Cloud technology
- **Instance Type:** Display Layouts by the associated Instance Type

Layout Detail View
^^^^^^^^^^^^^^^^^^

The Layout Detail view shows details on the Layout including Name, Short Name, Version, and Category. It also lists all associated Node Types.

- Select a Layout Name from the list page or Instance Type detail page to get to a Layout detail page.

Layout Configuration Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instance Type
  Select the Instance Type to add to the new Layout. Custom Instance Types must already be created and one Layout cannot be added to multiple instance types. The Instance Type also cannot be changed after creation.

  .. NOTE:: Layouts cannot be added to Morpheus pre-defined Instance Types

Name
  The name the Layout presents as in the Configuration Options dropdown of the provisioning wizard
Version
  The version number or name for the Layout. Layouts in an Instance Type with the same version will all show under the Configuration Options dropdown when that version is selected while provisioning
Description
  Description of the Layout, viewable on the Layout list view
Creatable
  When checked, this Layout will be selectable at provision time for the associated Instance Type (assuming the Layout is otherwise compatible with provisioning conditions). Instance Types with no Creatable Layouts will not be selectable from the provisioning wizard
Technology
  Technology determines which Cloud this layout will be available for and which Node Types can be added to it
Minimum Memory
  Defines the minimum amount of memory required for this Layout. Only Service Plans that meet the defined memory minimum will be available during provisioning when this Layout is selected. Custom memory values must also meet this minimum. Entering a minimum memory value of zero (the default value) indicates no minimum. This minimum memory value will override any Virtual Image minimum memory requirements
Workflow
  Select a Workflow to automatically run and be attached to associated Instances using this Layout. If a Workflow is defined, it is not presented in the provisioning wizard and is not user configurable
Supports Convert to Managed
  Enabled to allow users to select this layout when converting a Discovered workload to Managed
Enable Scaling (Horizontal)
  Enables Instances with this layout to use scaling features
Environment Variables
  Custom environment variables to be added to the Instance when provisioned
Inputs
  Search for and select one or multiple Inputs to add to the Layout. Inputs (except for Hidden Inputs) will appear in Provisioning, App, Blueprint, and Cloning wizards when this layout is selected
Nodes
  Single or multiple nodes can be added to a Layout by searching for and selecting the Node(s)
