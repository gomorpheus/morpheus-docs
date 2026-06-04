Custom External Identity Source
================================

Overview
--------

The Custom External identity source type allows |morpheus| to integrate with external Single Sign-On (SSO) systems that are not natively supported through a dedicated identity source type. This integration supports both interactive (browser redirect) and non-interactive (API-based) authentication modes with configurable response encryption.

Adding a Custom External Identity Source
-----------------------------------------

#. Navigate to |AdmTen|
#. Select the Tenant to add the Identity Source Integration
#. Select :guilabel:`IDENTITY SOURCES`
#. Select :guilabel:`+ IDENTITY SOURCE`
#. Select **Custom External** from the TYPE dropdown
#. Enter the following:

   NAME
     A name for this Identity Source integration in |morpheus|.

   DESCRIPTION
     Optional description of the Identity Source.

   NONINTERACTIVE
     Select the authentication mode:

     - **true** — Non-interactive/API mode. The external system authenticates users without browser redirects. |morpheus| sends credentials directly to the external system's API.
     - **false** — Interactive mode. Users are redirected to the external login URL for authentication, then redirected back to |morpheus| with an authentication response.

   EXTERNAL LOGIN URL
     (Interactive mode only) The URL to which users are redirected for authentication. The external SSO system should redirect back to |morpheus| after successful authentication with the user identity in the response.

   EXTERNAL LOGOUT URL
     (Interactive mode only) The URL to which users are redirected on logout from |morpheus|. This allows single logout across the SSO environment.

   AUTH RESPONSE ENCRYPTION ALGORITHM
     The encryption algorithm used to decrypt the authentication response from the external system:

     - **NONE** — No encryption; the response is sent in plaintext
     - **AES** — Advanced Encryption Standard
     - **DES** — Data Encryption Standard
     - **DESede** — Triple DES
     - **HmacSHA1** — HMAC with SHA-1
     - **HmacSHA256** — HMAC with SHA-256

   ENCRYPTION KEY
     (Required when an encryption algorithm other than NONE is selected) The shared secret key used to decrypt the authentication response.

   DEFAULT ROLE
     The default |morpheus| Role assigned to users authenticated through this identity source when no other role mapping applies.

   REQUIRED ROLE
     (Optional) An external role name that users must possess to be allowed access to |morpheus|. Leave blank to allow all authenticated users.

   ROLE MAPPINGS
     Map external role names to |morpheus| roles. Each existing |morpheus| role is listed with a field to enter the corresponding external role identifier. Users whose authentication response includes matching role values are assigned the mapped |morpheus| role.

#. Select :guilabel:`SAVE CHANGES`

Authentication Flow
-------------------

Interactive Mode
^^^^^^^^^^^^^^^^

#. User navigates to the |morpheus| login page (or Tenant subdomain URL)
#. User is redirected to the configured External Login URL
#. User authenticates with the external SSO system
#. External system redirects back to |morpheus| with an encrypted (or plaintext) authentication response containing user identity and role information
#. |morpheus| decrypts the response (if encrypted), validates the user, and creates/updates the local user account
#. User is logged into |morpheus| with the appropriate role assignments

Non-Interactive Mode
^^^^^^^^^^^^^^^^^^^^

#. User enters credentials on the |morpheus| login page
#. |morpheus| sends credentials to the external system's authentication endpoint
#. External system validates credentials and returns user identity and role information
#. |morpheus| creates/updates the local user account and logs the user in

Response Format
---------------

The external authentication system must return a response that |morpheus| can parse to extract:

- **Username** — The unique identifier for the user
- **Email** — The user's email address
- **Roles** — The roles/groups the user belongs to (for role mapping)

The exact format depends on the external system implementation. When encryption is configured, the response payload must be encrypted with the shared key using the configured algorithm before transmission to |morpheus|.

Security Considerations
-----------------------

- Always use HTTPS for the External Login URL and External Logout URL
- When using interactive mode, use a strong encryption algorithm (AES or HmacSHA256) to protect the authentication response in transit
- Store the Encryption Key securely and rotate it periodically
- Use the Required Role field to limit access to authorized users only
- The unique identity source code is auto-generated and used in the callback URL—do not modify it after users have authenticated

.. IMPORTANT:: Custom External identity source users will not authenticate in |morpheus| if there is an existing |morpheus| user with a matching username or email address that was not created by this identity source.
