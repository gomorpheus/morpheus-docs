Softlayer
=========

Add a Softlayer Cloud
---------------------

Name
  Name of the Cloud in |morpheus| 
Location
  Description field for adding notes on the cloud, such as location.
Visibility
  For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
Username
  Softlayer Username
API Key
  Softlayer User API Key, accessible in the Softlayer Portal under `Account -> Users -> View API Key`
Datacenter
  Datacenters will auto-populate upon successful authentication with the above credentials. Select appropriate Datacenter for this Cloud.
Object Store
  Select the destination Object Store
Inventory Existing Instances
  If enabled, existing Softlayer Instances will be inventoried and appear as unmanaged Virtual Machines in |morpheus| .

The Cloud can now be added to a Group or configured with additional Advanced options.

.. .. include:: /integration_guides/advanced_options.rst
