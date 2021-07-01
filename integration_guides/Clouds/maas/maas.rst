Canonical MAAS
--------------

MAAS from Canonical is an open-source server orchestration tool. It's designed to allow administrators to build a datacenter from on-premises, bare-metal servers where large networks of individual units can be discovered, deployed, and reconfigured.

Integrating MAAS and |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Integrating MAAS with |morpheus| is a simple process requiring the MAAS API URL and API Key. We'll start by gathering what we need from the MAAS UI, then move back into |morpheus| to store the required details.

We can gather the API key by clicking on the username in the upper-right corner of the MAAS UI window. From this preferences page, click on "API keys" as shown in the screenshot:

.. image:: /images/integration_guides/clouds/maas/1prefPage.png

From the API keys page, select the displayed key and copy it. Alternatively, you can click the copy button in the UI to add the full key to your clipboard. Store this key in an accessible location for a later step.

.. image:: /images/integration_guides/clouds/maas/2maasApi.png

In addition to the API key, we need the MAAS API URL. As entered in |morpheus|, the value will be like the following example: ``http://<maas-hostname-or-ip>:5240``. We'll enter the API URL into |morpheus| duriong the next step.

In |morpheus|, navigate to the list of integrated Clouds and start a new MAAS Cloud integration:

#. Infrastructure > Clouds
#. Click :guilabel:`+ ADD`
#. Select "MAAS"
#. Click :guilabel:`NEXT`

On the "CREATE CLOUD" modal, you must at least give a friendly name for the Cloud in |morpheus|, MAAS API URL and API KEY. An example is shown below:

.. image:: /images/integration_guides/clouds/maas/3createCloud.png
  :width: 50%

.. TIP:: You'll know the credentials are entered correctly when your list of MAAS resource pools is synced in as you can see in the example screenshot.

Click :guilabel:`NEXT` and add this new Cloud to an existing Group or create a new Group for it. Once you advanced past the end of the wizard, the Cloud is added and |morpheus| begins to inventory (if you've opted to inventory when adding the Cloud).

.. image:: /images/integration_guides/clouds/maas/4cloudDetail.png
