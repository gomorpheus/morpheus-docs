.. _clients:

Overview
^^^^^^^^

|morpheus| includes pre-configured OAuth clients and allows the user to create as many additional clients as they'd like. The pre-configured clients are editable but cannot be deleted. Once configured, access tokens may be generated or re-generated from the :ref:`API Access section <api-access>`. Their expiration times may be viewed as well. Client settings are available only in the Primary Tenant and affect all Tenants.

Creating an OAuth Client
^^^^^^^^^^^^^^^^^^^^^^^^

To create a new OAuth Client, click :guilabel:`+ ADD` and configure the following:

- **CLIENT ID:** A reference name for the client in |morpheus|
- **SECRET:** An optional OAuth client secret
- **ACCESS TOKEN VALIDITY INTERVAL (SECONDS):** The length of time (in seconds) during which the token should be enabled
- **REFRESH TOKEN VALIDITY INTERVAL (SECONDS):** The length of time (in seconds) during which the refresh token should be enabled

Once the client is configured, click :guilabel:`SAVE CHANGES`.

Editing and Deleting OAuth Clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the OAuth client list view (|AdmSetCli|), click the pencil (|pencil|) or trash can (|trash|) icons to edit or delete the OAuth Client.

.. NOTE:: Pre-configured |morpheus|-default clients may be edited but not deleted. User-created clients may be edited or deleted.
