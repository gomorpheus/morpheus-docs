Softlayer
---------

Add a Softlayer Cloud
^^^^^^^^^^^^^^^^^^^^^

.. include:: /integration_guides/Clouds/base_options.rst

Details
```````
Username
  Softlayer Username
API Key
  Softlayer User API Key, accessible in the Softlayer Portal under ```Account > Users > View API Key``
Datacenter
  Datacenters will auto-populate upon successful authentication with the above credentials. Select appropriate Datacenter for this Cloud.
Object Store
  Select the destination Object Store
Inventory Existing Instances
  If enabled, existing Softlayer Instances will be inventoried and appear as unmanaged Virtual Machines in |morpheus| .

The Cloud can now be added to a Group or configured with additional Advanced options.

.. include:: /integration_guides/Clouds/advanced_options.rst
