XCP-ng
------

Add an XCP-ng Cloud
^^^^^^^^^^^^^^^^^^^^

.. important::

   The current compatibility matrix retains XenServer 7.x as the previously published qualified value. XCP-ng 8.2.x, including 8.2.1, is not approved by the evidence bundled with this documentation. Do not treat testing activity as a support statement. Verify a planned XCP-ng release with HPE Support before deployment.

#. Navigate to ``Infrastructure > Clouds``
#. Select :guilabel:`+ CREATE CLOUD`, select XCP-ng, and then click :guilabel:`Next`.
#. Enter the following into the Create Cloud modal:

   .. include:: /integration_guides/Clouds/base_options.rst

   **Details**

   API URL
      IP or URL of XCP-ng Host. ex: `xcpng.domain.com`
   CUSTOM PORT
      Port for non standard XCP-ng clouds
   USERNAME
      XCP-ng Host Username
   PASSWORD
      XCP-ng Host Password
   Inventory Existing Instances
      If enabled, existing Virtual Machines will be inventoried and appear as unmanaged Virtual Machines in |morpheus| .

#. The Cloud can now be added to a Group or configured with additional Advanced options.

.. include:: /integration_guides/Clouds/advanced_options.rst

Feature Boundaries
^^^^^^^^^^^^^^^^^^

The XCP-ng integration is classified as a **Tier 3 — Essential Provisioning** integration. The following capabilities are not currently supported:

**Networking**

- Network creation or deletion from |morpheus|
- Security group management
- IPAM / IP pool management
- Load balancer integration

**Provisioning & Lifecycle**

- Guest customization (cloud-init is supported but Windows guest customization is not)
- Auto scaling
- VM migrations
- Clone to image

**Costing & Governance**

- Price synchronization or billing integration
- Costing or right-sizing recommendations
- Tag synchronization
- Multitenancy / resource pool scoping

**Other**

- Remote console via |morpheus|
- Kubernetes or Docker host provisioning
- Third-party backup integrations

.. note:: XCP-ng is delivered as an external plugin. It can be installed from the `Morpheus Marketplace <https://share.morpheusdata.com>`_ via |AdmIntPlu|.

For a full feature comparison across all supported clouds, see :doc:`/integration_guides/Clouds/cloudCoverage/cloudCoverage`.
