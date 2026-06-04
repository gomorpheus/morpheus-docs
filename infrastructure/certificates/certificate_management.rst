.. _certificate_management:

Certificate Management
======================

Overview
--------

|morpheus| provides centralized SSL/TLS certificate management for securing communications across your infrastructure. Certificates stored in |morpheus| can be used for SSL termination on load balancers, securing container communications, authenticating to integrations, and provisioning encrypted endpoints.

Certificate management is found in |InfTruCer| (Infrastructure > Trust > Certificates). From this section, administrators can upload existing certificates, generate certificate signing requests (CSRs), and manage the full lifecycle of SSL/TLS certificates.

Role Permissions
----------------

Access to certificate management is controlled by the following role permission:

- **Infrastructure: Trust (Certificates)** — ``None``, ``Read``, or ``Full``

  - **None:** Cannot access the Certificates section
  - **Read:** Can view certificates but cannot create, edit, or delete
  - **Full:** Full management access to certificates

Certificate Types
-----------------

|morpheus| supports several certificate types:

- **SSL Certificate (PEM):** Standard PEM-encoded SSL/TLS certificate with private key and optional certificate chain
- **x509 Client Certificate:** Client certificates used for mutual TLS authentication
- **x509 Device Certificate:** Device certificates for IoT or machine-to-machine authentication
- **Self-Signed Certificate:** Certificates generated and signed by |morpheus| internal CA
- **Root CA Certificate:** Trusted root certificate authority certificates
- **Certificate Signing Request (CSR):** Pending certificate requests awaiting signing by a CA

Adding a Certificate
--------------------

To upload or create a certificate:

#. Navigate to |InfTruCer|
#. Click :guilabel:`+ ADD`
#. Select the certificate type
#. Complete the form fields:

   - **NAME:** A descriptive name for the certificate
   - **DOMAIN NAME:** The domain or common name the certificate covers (e.g., ``*.example.com``)
   - **CERTIFICATE (PEM):** Paste the PEM-encoded certificate content
   - **PRIVATE KEY (PEM):** Paste the PEM-encoded private key
   - **CERTIFICATE CHAIN (PEM):** Paste intermediate and root CA certificates (optional but recommended)

#. Click :guilabel:`SAVE`

.. NOTE:: Private keys are encrypted at rest using |morpheus| internal encryption. They are never exposed in plain text through the UI after upload.

Generating a Certificate Signing Request
-----------------------------------------

To generate a CSR for signing by an external Certificate Authority:

#. Navigate to |InfTruCer|
#. Click :guilabel:`+ ADD`
#. Select the appropriate certificate type that supports CSR generation
#. Fill in the subject fields:

   - **COMMON NAME (CN):** The fully qualified domain name (e.g., ``app.example.com``)
   - **ORGANIZATION:** Your organization name
   - **ORGANIZATION UNIT:** Department or unit name
   - **CITY/LOCALITY:** City
   - **STATE/PROVINCE:** State or province
   - **COUNTRY:** Two-letter country code (e.g., ``US``)
   - **KEY SIZE:** Key length in bits (2048, 4096)
   - **KEY ALGORITHM:** RSA or ECDSA

#. Click :guilabel:`GENERATE REQUEST`

The CSR can then be submitted to your Certificate Authority for signing. Once signed, upload the resulting certificate back to |morpheus| to complete the process.

Certificate Details
-------------------

Selecting a certificate from the list displays its details:

- **Status:** Active, Expired, or Pending
- **Issued To / Issued By:** Subject and issuer information
- **Serial Number:** Certificate serial number
- **Fingerprint:** SHA-256 fingerprint for verification
- **Issue Date / Expiration Date:** Certificate validity period
- **Key Algorithm / Key Size:** Cryptographic details
- **Wildcard:** Whether the certificate covers wildcard domains

Certificate Usage
-----------------

Certificates stored in |morpheus| can be applied in various contexts:

- **Load Balancers:** SSL termination and re-encryption profiles
- **Network Routers:** NSX-T and other router SSL configurations
- **Provisioning:** Applied during Instance provisioning for SSL-enabled services
- **Integrations:** Authentication with external services requiring client certificates

Editing Certificates
--------------------

#. Navigate to |InfTruCer|
#. Click the pencil icon on the certificate row or select the certificate and click :guilabel:`EDIT`
#. Modify the certificate fields as needed
#. Click :guilabel:`SAVE`

.. NOTE:: Certificate content (PEM data) can be updated, for example when renewing a certificate with the same name.

Deleting Certificates
---------------------

#. Navigate to |InfTruCer|
#. Click the trash icon on the certificate row or select the certificate and choose :guilabel:`DELETE` from the Actions menu
#. Confirm deletion

.. WARNING:: Deleting a certificate that is actively in use by load balancers or other services may cause service disruptions. Verify the certificate is not referenced before removal.

API
---

Certificates can also be managed via the |morpheus| API:

.. code-block:: bash

  # List certificates
  curl "$MORPHEUS_API_URL/api/certificates" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN"

  # Create a certificate
  curl -X POST "$MORPHEUS_API_URL/api/certificates" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "certificate": {
        "name": "My SSL Cert",
        "certFile": "-----BEGIN CERTIFICATE-----\n...",
        "keyFile": "-----BEGIN PRIVATE KEY-----\n...",
        "chainFile": "-----BEGIN CERTIFICATE-----\n..."
      }
    }'
