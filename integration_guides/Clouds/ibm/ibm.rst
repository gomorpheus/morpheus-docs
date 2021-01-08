IBM Cloud
---------

IBM Cloud offers a wide set of cloud computing services including compute, storage, database, networking, and more. It is deployed in data centers across the world and its services can scale to meet the needs of small development teams as well as large-scale enterprises. |morpheus| integrates with IBM Cloud to offer virtual machine provisioning, brownfield discovery, and lifecycle management.

Integrating IBM Cloud with |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connecting an IBM Cloud account with |morpheus| is a simple process requiring only an API key. You can create an API key from the IBM Cloud web console if you don't currently have access to one.

#. Navigate to Infrastructure > Clouds
#. Click :guilabel:`+ ADD`
#. Complete the following required fields:

    - **NAME:** A friendly name for the cloud inegration in |morpheus|
    - **USERNAME:** The name given to the API key you're using the authenticate the connection
    - **API Key:** The API key value
    - **DATACENTER:** Select the IBM Cloud data center

#. Click :guilabel:`NEXT`
#. Select a Group for this Cloud
#. Complete the wizard to save the new integration

.. image:: /images/integration_guides/clouds/ibm/1createCloud.png
  :width: 50%

Once the wizard has completed, the new IBM Cloud integration will appear alongside other Clouds currently available in |morpheus|. If you've selected to automatically onboard existing resources, those will appear shortly.

IBM Cloud integrations also support a number of advanced options which were not discussed as part of the initial integration set up discussed above. For more information on the advanced options, consult the section below.

.. include:: /integration_guides/Clouds/advanced_options.rst
