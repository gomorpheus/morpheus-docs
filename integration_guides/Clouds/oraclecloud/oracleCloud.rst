Oracle Cloud
------------

Add Oracle Public Cloud
^^^^^^^^^^^^^^^^^^^^^^^

.. important:: A Keypair (both public and private keys) must be added to |morpheus| with the Public Key in ssh-rsa format added to Oracle Cloud users keys in Oracle Cloud console for authentication.

.. note:: Information on uploading the Public Key and generating Tenancy's OCID and User's OCID can be found at https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm

NAME
 Internal name for the Cloud in |morpheus|
CODE
  Short code used for api and variables (Optional)
LOCATION
  Can be used to specify the location of the Cloud or add a description. (Optional)
VISIBILITY
 Determines Tenant visibility for the Cloud.
   * Private: Access to the Cloud is limited to the assigned Tenant (Master Tenant by default)
   * Public: Access to the Cloud can be configured for Tenants in their Tenant Role permissions.
TENANT
  Assigned Tenant when VISIBILITY is set to Private.
ENABLED
  When unchecked, the cloud will not sync and is not accessible for provisioning actions.
AUTOMATICALLY POWER ON VMS
  When checked, provisioned VMs are automatically powered on
TENANCY OCID
  The OCID string from `Tenancy Information` section in Oracle Cloud
USER OCID
  OCID String for the OPC API user
SELECT KEY PAIR
  Select a keypair added to |morpheus| matching the public key added to specified OPC API user
REGION
  Select the OPC region (populates after successful account authentication)
COMPARTMENT
  Select Compartment (populates after successful account authentication)
INVENTORY
  Turn on for |morpheus| to discover and sync existing VMs

.. include:: /integration_guides/Clouds/advanced_options.rst
