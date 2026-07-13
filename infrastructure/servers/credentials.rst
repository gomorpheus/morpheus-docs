Device Credential Management
----------------------------

Overview
^^^^^^^^

|morpheus| provides centralized credential management for infrastructure devices such as iLO (Integrated Lights-Out), ESXi hosts, and network switches. Credentials are securely stored in the Cypher secrets engine rather than in plaintext database fields, enabling secure rotation and auditing of device access credentials.

Device credentials can be linked to one or more infrastructure objects (compute servers, network servers, or storage servers) and are managed from the Infrastructure Credentials interface.

Role Requirements
^^^^^^^^^^^^^^^^^

- ``Infrastructure: Compute`` role permission at **Full** level is required to create, edit, or delete credentials.

Viewing Credentials
^^^^^^^^^^^^^^^^^^^

Navigate to |InfCre| to view all stored device credentials. The list displays:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Column
     - Description
   * - Name
     - Descriptive name for the credential
   * - Type
     - Credential type (e.g., Username/Password)
   * - Status
     - Current status: OK, Warning (partial failure), or Error
   * - Linked Devices
     - Number of devices using this credential

Creating a Credential
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |InfCre|
#. Click :guilabel:`+ Add`
#. Select the credential store (integration) for secret storage
#. Complete the credential form:

   .. list-table::
      :widths: 30 70
      :header-rows: 1

      * - Field
        - Description
      * - Name
        - A descriptive name for the credential
      * - Credential Type
        - Select the type of credential (e.g., Username and Password)
      * - Username
        - The device username (e.g., ``Administrator``, ``root``)
      * - Password
        - The device password

#. Click :guilabel:`Save`

The credential is encrypted and stored in the Cypher secrets engine.

Linking Credentials to Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credentials can be linked to infrastructure devices during server creation or by editing an existing server:

#. Navigate to the server detail page or create a new server
#. In the Credentials section, select a stored credential from the dropdown
#. Save the configuration

A single credential can be linked to multiple devices. When the credential is updated, all linked devices will use the new value on their next connection.

.. NOTE:: When a credential store is configured with ``localCredentials: false``, inline password entry is disabled and users must select a stored credential.

Editing a Credential
^^^^^^^^^^^^^^^^^^^^

#. Navigate to |InfCre|
#. Click the credential name or select :guilabel:`Edit` from the actions menu
#. Update the username, password, or other fields as needed
#. Click :guilabel:`Save`

All devices linked to the updated credential will use the new values on their next connection.

Deleting a Credential
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |InfCre|
#. Select :guilabel:`Delete` from the actions menu
#. Confirm deletion

.. WARNING:: Deleting a credential removes all device links. Devices that relied on this credential will no longer have stored access credentials until a new credential is linked.

Credential Status
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Status
     - Description
   * - OK
     - Credential is healthy and accessible
   * - Warning
     - Some linked devices experienced issues (partial failure)
   * - Error
     - Credential access failed for all linked devices

A background job (``CypherBackedCredentialSyncRetryBackgroundJob``) automatically retries failed credential operations for devices that were unreachable during the last update.
