Consul
------

|morpheus| can integrate with Consul to automatically install the Consul Agent in Client Mode on Instances and configure communication with the Consul host.

Add Consul Integration
^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Administration -> Integrations` and select `+ New Integration`
#. Select Integration Type `Consul Service Registry`
#. Populate the following fields:

   Name
    Name of the Consul Integration in |morpheus| 
   Enabled
    Enabled by default
   Consul Host
    IP or Url of the Consul Host
   Consul Http Port
    Http port of the Consul Host
   Username
    Consul Host User
   Password
    Consul Host User Password
   Datacenter ID
    Validator key for the organization

#. Save Changes

The added Consul Integration is now available for use in |morpheus| , but must be scoped to a Cloud or Group to automatically install the Consul Agent while provisioning.

Scope Consul Integration to a Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Clouds`
#. Edit the target Cloud
#. Expand the `Advanced Options` section
#. In the `Service Registry` dropdown, select the Consul Integration.
#. Save Changes

Scope Consul Integration to a Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Groups`
#. Edit the target Group
#. Expand the `Advanced Options` section
#. In the `Service Registry` dropdown, select the Consul Integration.
#. Save Changes

And that's it.  After your integration is set up, all containers deployed within the Group or Cloud integrated will provision with the Consul Agent in Client Mode, gossiping to your Consul Server!
