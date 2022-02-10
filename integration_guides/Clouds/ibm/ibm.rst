IBM Cloud
---------

IBM Cloud offers a wide set of cloud computing services including compute, storage, database, networking, and more. It is deployed in data centers across the world and its services can scale to meet the needs of small development teams as well as large-scale enterprises. |morpheus| integrates with IBM Cloud to offer virtual machine provisioning, brownfield discovery, and lifecycle management.

Integrating IBM Cloud with |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connecting an IBM Cloud account with |morpheus| is a simple process requiring only an API key. You can create an API key from the IBM Cloud web console if you don't currently have access to one. Integrating with |morpheus| requires a user API key. If needed, create one by clicking "Manage" in the upper menu bar of the IBM Cloud web console and clicking "Access (IAM)". Select "Users" from the left navigation menu and click on the desired user. Create a new API Key from within the API Keys section and store the API Key in a secure place to retrieve in the next step. It's recommended that you integrate |morpheus| using an IBM Cloud admin account to ensure you won't run into any blockers while working in |morpheus|. Using |morpheus| role-based access you can limit which IBM Cloud constructs and capabilities are accessible to your users.

With the API key created, head back to |morpheus| and continue with the following steps:

#. Navigate to Infrastructure > Clouds
#. Click :guilabel:`+ ADD`
#. Complete the following required fields:

  - **NAME:** A friendly name for the cloud inegration in |morpheus|
  - **USERNAME:** Enter "apikey" (Do not enter your IBM Cloud username or anything other than "apikey")
  - **API Key:** The API key value
  - **DATACENTER:** Select the IBM Cloud data center
  - **OBJECT STORE:** If desired and if any are found, select an object store

#. Click :guilabel:`NEXT`
#. Select a Group for this Cloud or create a new one if desired
#. Complete the wizard to save the new integration

.. image:: /images/integration_guides/clouds/ibm/1createCloud.png
  :width: 50%

Once the wizard has completed, the new IBM Cloud integration will appear alongside other Clouds currently available in |morpheus|. If you've selected to automatically onboard existing resources, those will appear shortly.

IBM Cloud integrations also support a number of advanced options which were not discussed as part of the initial integration set up discussed above. For more information on the advanced options, consult the section below.

.. include:: /integration_guides/Clouds/advanced_options.rst
