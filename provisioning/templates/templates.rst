Templates
=========

Overview
--------

App Templates allow to pre-configure full multi-tier application deployments for multiple environments. Templates can be provisioned from the ``Provisioning -> Apps`` section and can be fully configured for one click provisioning. Templates can be built within the Builder section or by code in the Raw section. Templates can also be exported as YAML or JSON and created with the |morpheus| API and CLI.

Creating App Templates
----------------------

#. Navigate to ``Provisioning -> Templates``
#. Select ``+ ADD TEMPLATE``
#. Enter a NAME for the Template and select ``NEXT``
#. Optionally add a Description, Category, and Image for the Template.

Add Tiers
^^^^^^^^^

#. In the STRUCTURE section, select + to add a Tier
#. Select or enter a Tier Name.
#. Select the Tier to set Boot Order, rename, or once multiple Tiers are added, connect the Tier to other Tiers.

Add Instances to Tiers
^^^^^^^^^^^^^^^^^^^^^^

#. In the STRUCTURE section, select + in a Tier to add an Instance
#. Select an Instance Type
#. Optionally add a name for the Instance. Instances with blank names will automatically be named based off the App name.

Add Configurations to Instances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In the STRUCTURE section, select + in an Instance to add a Configuration
#. Select at least one option from Group, Cloud or Environment.
#. Select ``ADD CONFIG`` to create the configuration
#. Populate the Configuration
   * Configurations can be fully partially or populated
   * Fields can be locked by selecting the Lock icon next to the Field. Locking prevent the field from being editable when provisioning an App using the Template.
   * ALLOW EXISTING INSTANCE will allow users to add existing Instances to the App when using the template

Save
^^^^

Once all desired Tiers, Instances and Configurations are added, select Save. The Template will be created, can be edited after saving, and will available in the Apps section for provisioning.

.. NOTE:: Templates are not provisioned when created. To provision a Template, use ``Provisioning -> Apps``.

RAW
^^^

Templates can be create, edited or Exported in the RAW section when creating or editing a template.

To Export a Template a Template as JSON or YAML:

#. Create or Edit a Template
#. Select the RAW section on the top of the APP TEMPLATE modal.
#. Select JSON or YAML in the top right of the RAW section.
#. Select the EXPORT button.
#. Select the Configurations to include in the Export by clicking on a Configuration. Selected Configurations will be highlighted.
#. Select the DOWNLOAD CONFIGURATION button.
#. The Template Export file will be downloaded to your computer as {template_name}-config.json or {template_name}-config.yaml.

Preview
^^^^^^^

In the APP TEMPLATE modal, select the Preview section to display a graphical representation of your Templates Tiers, Instances and Tier Connections.

.. IMPORTANT:: When Tiers are connected, the Instances in a Tier will import the evars from Instances in connected Tiers, and if |morpheus] is managing the Instance Firewalls, communication between the Instances will be facilitated based on the Instances port configurations.

Provisioning
^^^^^^^^^^^^

To provision a Template, navigate to ``Provisioning -> Apps`` and select the Template when creating an App.
