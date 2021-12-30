Cisco ACI
---------

Overview
^^^^^^^^

.. image:: /images/aci1.png
   :alt: ACI summary tab

Add ACI as a network and security integration. Inventory your existing ACI configurations. Create networks, bridge domains, application profiles, tenants, endpoint groups, contexts, filters and contracts.  Provision instances into new endpoint groups and define security groups that apply contracts on provision.

From Morpheus below can be created:

- Tenants
- ANP's
- EPG’s
- Contexts
- Bridge Domains
- Filters
- Contracts

.. note:: Morpheus to ACI Sync Job Schedule: Every 5 minutes

.. note:: Morpheus connects to ACI APIC over port 443

Add Network Integration
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Networks > Integrations``
#. Select :guilabel:`+ADD` > `Networking` > ``Cisco ACI``
#. Populate the following:

   NAME
      ACI Integration Name/Label in |morpheus|
        This is unique to |morpheus| and not part of authentication
   URL
      ACI fabric url, eg ``https://apicdc.company.com``
   USERNAME
      ACI ``aaaUser`` name attribute
   PASSWORD
      ACI ``aaaUser`` pwd attribute
   TENANT
      Populates upon authentication, tenant selection not required

#. Select :guilabel:`ADD NETWORK INTEGRATION`

Configure Cloud Network Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For your ACI Integration to be available during provisioning, ACI needs to be defined on a Cloud or multiple Clouds ``NETWORK MODE`` advanced options.

#. Select an existing VMware vCenter Cloud
#. Select :guilabel:`EDIT`
#. Expand the *Advanced Options* section
#. Select ACI Integration in ``NETWORK MODE`` dropdown
#. Select :guilabel:`SAVE`


Instance Provisioning
^^^^^^^^^^^^^^^^^^^^^

.. image:: /images/aci2.png
   :alt: ACI Instance provisioning options

Once ACI is integration to a cloud, it can be used during instance provisioning:

#. From the EPG drop down, either an existing EPG can be selected or a new one can be created. It is the same for ANP, either create a new one or choose an existing.
#. Under ACI security consumes and provides, contracts can be searched when you enter a name. When the provisioning wizard is completed, it will provision the instance and apply the ACI options and Security. This can be viewed under the instance page, or via REST API and CLI.

Blueprint Configuration
^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /images/aci2.png
   :alt: ACI Blueprint options

- In a Blueprint, you can define the ANP and EPG of each Tier
- Variables can be used for EPG and ANP names.
- This could be useful to create blueprints for dev testing to isolate from prod networks.
- This can be hybrid based on the VMM domains in APIC.
