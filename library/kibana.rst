Library Example: Kibana
-----------------------

Overview
^^^^^^^^

In this example we will build out a new Kibana Library item to automate the installation and configuration of Kibana. This simple example utilizes all sections of the Library including Inputs, File Templates and Scripts.

#. Configure Virtual Image
#. Add Kibana Instance Type
#. Add Input for ElasticSearch URL
#. Add Input for Kibana Version
#. Add File Template for kibana.yml
#. Add Script for Kibana installation
#. Add Kibana Node Type(s)
#. Add Kibana Layout(s)
#. Provision

Configure Virtual Image
^^^^^^^^^^^^^^^^^^^^^^^

For our Kibana Instance we will use base OS images and install Kibana at provision time. This allows us to determine the version and configuration while using any OS. Pre-installing Kibana on the image is an option but using a base image can be more flexible and limit the number of Virtual Images required across our catalog.

The first image used is a base CentOS 7.5 image synced from a Nutanix cloud. Cloud-init is installed on the image, so little configuration is necessary other than ensuring the Operating System is set properly and ``Is Cloud Init Enabled?`` is checked. If the image does not have cloud-init installed the username and password would need to be defined so |morpheus| can auth on the VM with existing credentials. Defining ```Minimum Memory`` ensures only Plans meeting the minimum memory requirement will be options when provisioning.

.. image:: /images/provisioning/library/kibana_image.png

Add Kibana Instance Type
^^^^^^^^^^^^^^^^^^^^^^^^

We do not have an existing Kibana Instance Type, so we will need to create one. If we already had a Kibana Instance Type and wanted to add additional Node Types and Layouts to it, creating an instance Type would not be necessary.

NAME
  Kibana
CODE
  kibana
DESCRIPTION
  Kibana is an open source analytics and visualization platform designed to work with Elasticsearch.
CATEGORY
  Apps
ICON
  Kibana-Logo-Color-H.png
VISIBILITY
  Private, as at this time we will only offer this Instance Type for the master Tenant. If we wanted to offer it to all Tenants, Visibility should be set to Public and then exposed on the Tenant Roles for access.
Inputs
  We could set the ``ElasticSearch URL`` and ``Kibana Version`` Inputs on this Instance Type, but we will set them on the layout instead in case we want to define the version and/or leave the Elasticsearch URL unconfigured with different layout options.
ENVIRONMENT PREFIX
  We will add a ``kibana`` Environment Prefix to identify evars
ENVIRONMENT VARIABLES
  We will leave blank but we could define config options for Kibana in a different config scenario.
Enable Settings
  Enabling ``Enable Settings`` will allow us to expose the ``kibana.yml`` in the Settings Tab on the Instance.
Enable Scaling (Horizontal)
  Disabling as we will not be scaling Kibana at this time
Support Deployments
  Disabling as we do not intend to use deployments for this instance type

.. image:: /images/provisioning/library/kibana_instance_type.png

Add Input for ElasticSearch URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When provisioning Kibana, we want to define the Elasticsearch url in the ``kibana.yml``. To allow the user to define which Elasticsearch instance Kibana will connect with, we will define an Input that will be a variable in the ``kibana.yml``, which we will be defining with a File Template.

NAME
  kibana es host
DESCRIPTION
  Elasticsearch Host for Kibana
FIELD NAME
  esurl

  .. NOTE:: Not this field name as it will be used when adding the varibale to the ``kibana.yml`` File Template, which will be ``<%= customOptions.esurl %>``.
TYPE
  Text, as we will allow the user to define the Elasticsearch host url.
LABEL
  Defined as ``elasticsearch.url:``, which will be the label of the input field for the Elasticsearch URL
PLACEHOLDER
  Added ``http://elaticsearch_host:9200`` so users know the proper format for entering the Elasticsearch URL at provision time.
DEFAULT VALUE
  Left blank as we will not know the Elasticsearch URL required
Required
  Enabled to ensure user defines the Elasticsearch URL

.. image:: /images/provisioning/library/kibana_eshost_option.png

Add Input for Kibana Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For this example we will be offering version selection at provision time through an Input. While we could add version selection by adding Node Types and/or Layouts for each version, because we will be installing Kibana with a script, we can grab the version though an Input and inject the associated url into the script using an Input variable.

NAME
  kibana version
DESCRIPTION
  kibana version
FIELD NAME
  kibversion

  .. NOTE:: Not this field name as it will be used when adding the variable to the Kibana installation script, which will be ``<%= customOptions.kibversion %>``.

TYPE
  We will use TYPE type to allow the user to input the version required. Using `Select` is also an option, which would be associated with an OPTION LIST with pre-populated version options defined via a CSV or JSON dataset, or from a REST source query, however to remain flexible and leave all future version options available, we will use TEXT type in this example.
LABEL
  Defined as ``Kibana Version``, which will be the label of the input field for the Kibana Version
PLACEHOLDER
    Added ``5.4.1`` so users know the proper format for entering the Elasticsearch URL at provision time.
DEFAULT VALUE
  Defined as ``5.4.1`` as this is the default version of Elasticsearch installed by |morpheus|
Required
  Enabled to ensure user defines the Kibana version to be installed

.. image:: /images/provisioning/library/kibana_version_option.png

Add File Template for kibana.yml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
