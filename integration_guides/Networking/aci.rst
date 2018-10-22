Cisco ACI
----------

Morpheus now integrates with Cisco ACI.  Add ACI as a network and security integration. Inventory your existing ACI configurations - Tenants, Application Network Profile, EndPoint Groups, Contexts, Bridge Domains, Filters and Contracts. 
Create networks, bridge domains, application profiles, tenants, endpoint groups and contexts. Provision instances into new/existing application network profile, endpoint groups and define security groups that apply contracts on provision.

ADD ACI NETWORK INTEGRATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Administration -> Integrations` and select `+ New Integration`
#. Select Integration Type "Cisco ACI"
#. Populate the following fields:
  NAME
  URL
  USERNAME
  PASSWORD
  TENANT

#. Save Changes

Once you have completed this section and saved your changes you can set up a Cloud to utilize this integration.

Scope Cisco ACI Integration to a Network.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Navigate to `Infrastructure -> Cloud -> Netwoks`
  Edit the target Network
  Expand the `Advanced Options` section
  In the `Config Management` dropdown, select the Ansible Tower Integration.

#. Save Changes

