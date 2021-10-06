Chef
----

Overview
^^^^^^^^

|morpheus| integrates with one or multiple Chef servers to be used for bootstrapping while provisioning or as tasks in workflows in the Automation section. These workflows can then be run during provisioning in the provisioning wizard Automation pane, or on an existing Instance by selecting Run Workflows from the Actions menu on the Instance detail page. Workflows can also be added to Instances in the blueprint and app sections.


Add Chef Integration
^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Administration -> Integrations` and select `+ New Integration`
#. Select Integration Type "Chef"
#. Populate the following fields:

   * Name: Name of the Chef Integration in |morpheus|
   * Chef Endpoint: url of chef server api endpoint in https://api.example.com format. Do not add /organization/xxxx here, which is populated in the Chef Organization field
   * Chef Version: 12.3.0 by default, can be changed to use a different/more recent version of chef
   * Chef Organization: Chef Server Organization
   * Chef User: Chef Server User
   * User Private Key: The private key of the user with access to this chef server
   * Organization Validator: Validator key for the organization

#. Save Changes

The added Chef Integration is now available for use in |morpheus|. The Chef Integration can be added to Clouds or Groups to auto-bootstrap nodes and specify Environment, Node ID, Runlist, Attributes and Tags when creating instances. The Chef integration can also be selected in the Chef Server dropdown when creating a Chef Bootstrap-type Task.

.. NOTE:: Integrating Chef with |morpheus| enables a user to bootstrap a node using Chef Bootstrap-type Tasks or Chef associations with Clouds or infrastructure Groups. It does not enable users to update run-lists on the Chef server for nodes which have already been bootstrapped.

Scope Chef Integration to a Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Clouds`
#. Edit the target Cloud
#. Expand the `Advanced Options` section
#. In the `Config Management` dropdown, select the Chef Integration.
#. Save Changes

Scope Chef Integration to a Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Groups`
#. Edit the target Group
#. Expand the `Advanced Options` section
#. In the `Config Management` dropdown, select the Chef Integration.
#. Save Changes

Provisioning Options
^^^^^^^^^^^^^^^^^^^^

When provisioning Instances into a Cloud or Group with a Chef Integration added, a `Chef` section will appear in the Config section of the provisioning wizard. By default, Chef is enabled, but can be disabled by expanding the `Chef` section and unchecking `Enable Chef`.

Chef Integration Provisioning options:

Enable Chef
  Select to bootstrap
Chef Environment
  Populate Chef environment, or leave as `_default`
Chef Node ID
  Defaults to instance name, configurable.
Chef Runlist
  Add Runlist
CHEF ATTRIBUTES
  Add Chef Attributes
CHEF TAGS
  Add Chef tags
