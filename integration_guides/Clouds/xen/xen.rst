Xen Server
----------

Add a Xen Server Cloud
^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure -> Clouds``
#. Select :guilabel:`+ CREATE CLOUD`, select Xen, and then click :guilabel:`Next`.
#. Enter the following into the Create Cloud modal:

   .. include:: /integration_guides/Clouds/base_options.rst

   **Details**

   API URL
      IP or URL of Xen Host. ex: `xenserver.domain.com`
   CUSTOM PORT
      Port for non standard xen server clouds
   USERNAME
      Xen Host Username
   PASSWORD
      Xen Host Password
   Inventory Existing Instances
      If enabled, existing Virtual Machines will be inventoried and appear as unmanaged Virtual Machines in |morpheus| .

#. The Cloud can now be added to a Group or configured with additional Advanced options.

.. include:: /integration_guides/Clouds/advanced_options.rst
