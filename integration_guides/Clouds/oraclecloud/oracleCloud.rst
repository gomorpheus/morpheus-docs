Oracle Cloud
------------

Required Permissions
^^^^^^^^^^^^^^^^^^^^

Integrating Oracle Public Cloud with |morpheus| requires access to a service account with at least the permission set listed below. When creating an Oracle Cloud integration scoped to a specific compartment, the service account needs access only to the listed resource families within the chosen compartment. If the Cloud will be scoped to all compartments, the service account will need access to the listed resource families at the root compartment.

- Allow group <GROUP CONTAINING SERVICE USER> to manage cluster-family in compartment <CHOSEN COMPARTMENT OR ROOT COMPARTMENT>
- Allow group <GROUP CONTAINING SERVICE USER> to manage compute-management-family in compartment <CHOSEN COMPARTMENT OR ROOT COMPARTMENT>
- Allow group <GROUP CONTAINING SERVICE USER> to manage data-catalog-family in compartment <CHOSEN COMPARTMENT OR ROOT COMPARTMENT>
- Allow group <GROUP CONTAINING SERVICE USER> to manage dns in compartment <CHOSEN COMPARTMENT OR ROOT COMPARTMENT>
- Allow group <GROUP CONTAINING SERVICE USER> to manage file-family in compartment <CHOSEN COMPARTMENT OR ROOT COMPARTMENT>
- Allow group <GROUP CONTAINING SERVICE USER> to manage instance-family in compartment <CHOSEN COMPARTMENT OR ROOT COMPARTMENT>
- Allow group <GROUP CONTAINING SERVICE USER> to manage object-family in compartment <CHOSEN COMPARTMENT OR ROOT COMPARTMENT>
- Allow group <GROUP CONTAINING SERVICE USER> to manage virtual-network-family in compartment <CHOSEN COMPARTMENT OR ROOT COMPARTMENT>
- Allow group <GROUP CONTAINING SERVICE USER> to manage volume-family in compartment <CHOSEN COMPARTMENT OR ROOT COMPARTMENT>

Add Oracle Public Cloud
^^^^^^^^^^^^^^^^^^^^^^^

.. important:: A Keypair (both public and private key) must be added to |morpheus| with the Public Key in ssh-rsa format. The Public Key in PEM format needs to be added to Oracle Cloud users keys in Oracle Cloud console for authentication.

.. note:: Information on uploading the Public Key and generating Tenancy's OCID and User's OCID can be found at https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm

To get started, navigate to |InfClo|. Click :guilabel:`+ ADD` and select Oracle Public Cloud to begin a new one. Configure the following options for the new Cloud:

.. include:: /integration_guides/Clouds/base_options.rst

Details
```````

TENANCY OCID
  The OCID string from `Tenancy Information` section in Oracle Cloud
USER OCID
  OCID String for the OPC API user
SELECT KEY PAIR
  Select a keypair added to |morpheus| matching the public key added to specified OPC API user
REGION
  Select the OPC region (populates after successful account authentication)
COMPARTMENT
  Choose to scope the Cloud to all compartments or to one specific compartment (populates after successful account authentication)
INVENTORY
  Turn on for |morpheus| to discover and sync existing VMs

.. include:: /integration_guides/Clouds/advanced_options.rst

Enable Live Costing for Oracle Public Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Morpheus version 4.2.1 and higher support live costing data from the Oracle Cloud metering API. In order to authenticate with this API, edit your existing Oracle Cloud account integration or begin the process of newly integrating an account that wasn’t previously consumable in |morpheus| (Infrastructure > Clouds > +ADD).

In the advanced options section of the add/edit cloud modal for Oracle Public Cloud, the COSTING KEY and COSTING SECRET fields must be completed to work with metering API data in |morpheus|. Unlike the OCI API authentication used to initially integrate Oracle Cloud, the metering API uses token-based authentication. We must access a Client ID and Client Secret value from the Oracle Public Cloud console to complete these fields.

.. image:: /images/integration_guides/clouds/oraclepubliccloud/1editcloud.png

Navigate to Oracle cloud sign in page, the URL for which is similar to the following example:

``https://idcs-00a0xxxxxxxxxxxxx.identity.oraclecloud.com/ui/v1/signin``

If you’re not redirected to the admin console similar to the one pictured below, log out and replace ‘signin’ at the end of the URL with ‘adminconsole’ as in the following example:

``https:// idcs-00a0xxxxxxxxxxxxx.identity.oraclecloud.com/ui/v1/adminconsole``

You’ll immediately be redirected back to the same signin page but in doing that you should be taken to the admin console after authenticating your session once again.

.. image:: /images/integration_guides/clouds/oraclepubliccloud/2adminconsole.png

Create a new application and select the type “Confidential Application”.

.. image:: /images/integration_guides/clouds/oraclepubliccloud/3confapp.png

On the Details tab, enter a “Name” value and click “Next”.

.. image:: /images/integration_guides/clouds/oraclepubliccloud/4appdetails.png

On the Client tab, choose to “Configure this application as a client now” to reveal additional fields. Then, in the Authorization section, mark the boxes for “Client Credentials” and “JWT Assertion”.

.. image:: /images/integration_guides/clouds/oraclepubliccloud/5appauth.png

In the Token Issuance Policy section, click the “+Add Scope” button. Click the right-facing arrow button in the row for “CloudPortalResourceApp”. Mark the box to give read access for metering and click “Add”.

.. image:: /images/integration_guides/clouds/oraclepubliccloud/6meteringread.png

Click “Next” until the “Finish” button is shown, then click “Finish”

The Client ID and Client Secret value will be shown at this point. If these values need to be referenced in the future, simply edit the application and go to the Configuration tab. The Client ID and Client Secret are shown in the General Information section.

.. image:: /images/integration_guides/clouds/oraclepubliccloud/7secretvalues.png

Back in |morpheus|, enter these values in the COSTING KEY and COSTING SECRET fields of the add/edit cloud modal for your Oracle Public Cloud integration. You also need to fill in the IDENTITY SERVICE value. This value can be found in the URL for your Oracle admin console as shown in the image below. It will be in a format ``idcs-xxxxxx``.

.. image:: /images/integration_guides/clouds/oraclepubliccloud/8identityservice.png

Save changes to the Cloud.
