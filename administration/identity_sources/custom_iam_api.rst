Custom IAM API Identity Source
================================

Overview
--------

The Custom IAM API identity source allows |morpheus| to authenticate users against an external Identity and Access Management (IAM) system through a custom API endpoint. This is useful for organizations with proprietary or uncommon IAM systems that provide a REST or HTTP-based authentication API.

|morpheus| sends user credentials to the configured endpoint and processes the response to authenticate users and optionally assign roles.

Adding a Custom IAM API Identity Source
----------------------------------------

#. Navigate to |AdmTen|
#. Select the Tenant to add the Identity Source Integration
#. Select :guilabel:`IDENTITY SOURCES`
#. Select :guilabel:`+ IDENTITY SOURCE`
#. Select **Custom API** from the TYPE dropdown
#. Enter the following:

   NAME
     A name for this Identity Source integration in |morpheus|.

   DESCRIPTION
     Optional description of the Identity Source.

   API ENDPOINT
     The full URL of the external IAM authentication API endpoint (e.g., ``https://iam.example.com/api/authenticate``).

   API STYLE
     The HTTP method and encoding format for sending credentials to the endpoint:

     - **Form URL Encoded [GET]** — Credentials sent as URL query parameters via GET request
     - **Form URL Encoded [POST]** — Credentials sent as form-encoded body via POST request
     - **JSON [POST]** — Credentials sent as JSON body via POST request
     - **XML [POST]** — Credentials sent as XML body via POST request
     - **HTTP Basic [GET]** — Credentials sent via HTTP Basic Authentication header on a GET request

   VALUE ENCRYPTION ALGORITHM
     (Not available for HTTP Basic style) The algorithm used to encrypt credential values before sending them to the API:

     - **NONE** — Credentials sent in plaintext (use only with HTTPS)
     - **AES** — Advanced Encryption Standard
     - **DES** — Data Encryption Standard
     - **DESede** — Triple DES
     - **HmacSHA1** — HMAC with SHA-1
     - **HmacSHA256** — HMAC with SHA-256

   ENCRYPTION KEY
     (Required when an encryption algorithm other than NONE is selected) The shared secret key used to encrypt credential values before transmission.

   DEFAULT MORPHEUS ROLE
     The default |morpheus| Role assigned to users authenticated through this identity source. Select NONE to require explicit role mapping for all users.

#. Select :guilabel:`SAVE CHANGES`

Authentication Flow
-------------------

#. User enters credentials on the |morpheus| login page
#. |morpheus| formats the credentials according to the configured API Style
#. If encryption is configured, credential values are encrypted with the shared key
#. |morpheus| sends the request to the configured API Endpoint
#. The external IAM system validates credentials and returns a success/failure response
#. On success, |morpheus| creates or updates the local user account and logs the user in with the Default Role
#. On failure, the login is denied with an authentication error

API Response Expectations
-------------------------

The external IAM API endpoint should:

- Return an HTTP 200 status code on successful authentication
- Return an HTTP 401 or 403 status code on failed authentication
- Optionally include user attributes (email, display name) in the success response for user account population
- Respond within a reasonable timeout (recommended under 10 seconds)

API Style Details
-----------------

**Form URL Encoded [GET]**

Sends credentials as query parameters::

  GET https://iam.example.com/api/authenticate?username=user&password=pass

**Form URL Encoded [POST]**

Sends credentials as form body::

  POST https://iam.example.com/api/authenticate
  Content-Type: application/x-www-form-urlencoded

  username=user&password=pass

**JSON [POST]**

Sends credentials as JSON::

  POST https://iam.example.com/api/authenticate
  Content-Type: application/json

  {"username": "user", "password": "pass"}

**XML [POST]**

Sends credentials as XML::

  POST https://iam.example.com/api/authenticate
  Content-Type: application/xml

  <auth><username>user</username><password>pass</password></auth>

**HTTP Basic [GET]**

Sends credentials in the Authorization header::

  GET https://iam.example.com/api/authenticate
  Authorization: Basic dXNlcjpwYXNz

Security Considerations
-----------------------

- Always use HTTPS for the API Endpoint to protect credentials in transit
- Use value encryption (AES or HmacSHA256) as an additional layer when the API requires it
- HTTP Basic [GET] mode does not support additional value encryption (credentials are Base64-encoded in the header)
- Rotate the encryption key periodically if using value encryption
- Ensure the external IAM system implements rate limiting and account lockout to prevent brute-force attacks

.. IMPORTANT:: Custom IAM API identity source users will not authenticate in |morpheus| if there is an existing |morpheus| user with a matching username or email address that was not created by this identity source.
