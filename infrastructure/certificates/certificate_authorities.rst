.. _certificate_authorities:

Certificate Authorities
=======================

Overview
--------

|morpheus| integrates with external Certificate Authority (CA) services to automate certificate issuance, renewal, and lifecycle management. CA integrations are managed from |InfTruSer| (Infrastructure > Trust > Services).

When a CA integration is active, |morpheus| can request certificates directly from the CA, eliminating manual CSR submission workflows and enabling automated certificate provisioning during Instance creation.

Supported CA Integrations
--------------------------

|morpheus| supports the following Certificate Authority integrations:

- **Venafi Trust Protection Platform:** Enterprise certificate lifecycle management
- **Microsoft Active Directory Certificate Services (ADCS):** Windows PKI infrastructure
- **HashiCorp Vault PKI:** Vault PKI secrets engine for dynamic certificate generation
- **Let's Encrypt (ACME):** Free, automated SSL certificates via ACME protocol

Adding a CA Integration
-----------------------

To add a Certificate Authority integration:

#. Navigate to |InfTruSer|
#. Click :guilabel:`+ ADD`
#. Select the CA integration type
#. Complete the configuration fields (vary by type):

   **Common Fields:**

   - **NAME:** A descriptive name for the integration
   - **ENABLED:** Toggle to enable or disable the integration

   **Venafi:**

   - **URL:** Venafi TPP server URL
   - **USERNAME:** API username
   - **PASSWORD:** API password
   - **POLICY FOLDER:** Certificate policy folder path

   **HashiCorp Vault PKI:**

   - **VAULT URL:** Vault server address
   - **VAULT TOKEN:** Authentication token or AppRole credentials
   - **PKI PATH:** Mount path for the PKI engine (e.g., ``pki``)
   - **ROLE:** Vault PKI role name for certificate issuance

#. Click :guilabel:`SAVE`

Once saved, |morpheus| will validate connectivity to the CA service and display the integration status.

Requesting Certificates from a CA
----------------------------------

With an active CA integration, certificates can be requested directly:

#. Navigate to |InfTruCer|
#. Click :guilabel:`+ ADD`
#. Select the certificate type associated with your CA integration
#. Fill in the certificate subject information:

   - **COMMON NAME:** FQDN for the certificate
   - **ORGANIZATION / OU / LOCALITY / STATE / COUNTRY:** Subject fields
   - **KEY SIZE:** Desired key length
   - **CA INTEGRATION:** Select the target CA

#. Click :guilabel:`REQUEST CERTIFICATE`

|morpheus| submits the request to the CA and, upon approval, stores the issued certificate automatically.

Certificate Renewal
-------------------

For certificates issued through CA integrations, |morpheus| tracks expiration dates and can facilitate renewal:

- Certificates approaching expiration are flagged in the certificate list
- Renewal can be triggered manually by signing the existing CSR again through the CA integration
- Automated renewal policies depend on the specific CA integration capabilities

Refreshing CA Data
------------------

To refresh certificates and metadata from a CA integration:

#. Navigate to |InfTruSer|
#. Select the CA integration
#. Click :guilabel:`REFRESH` from the Actions menu

This synchronizes the latest certificate inventory and status from the external CA.

Deleting a CA Integration
-------------------------

#. Navigate to |InfTruSer|
#. Click the trash icon or select :guilabel:`DELETE` from the Actions menu on the integration row
#. Confirm deletion

.. NOTE:: Removing a CA integration does not delete certificates that were previously issued through it. Those certificates remain in |morpheus| until manually removed.
