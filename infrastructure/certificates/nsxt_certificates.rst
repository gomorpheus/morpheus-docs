.. _nsxt_certificates:

NSX-T Certificate Management
=============================

Overview
--------

|morpheus| provides integrated certificate management for VMware NSX-T environments. NSX-T requires certificates for securing communications between its management plane, control plane, and transport nodes. |morpheus| can manage the lifecycle of these certificates, including uploading certificates to NSX-T managers and associating them with NSX-T services.

This feature is available when an NSX-T integration has been configured in |morpheus|.

Prerequisites
-------------

- An active NSX-T integration configured in |morpheus| (Infrastructure > Network > Integrations)
- NSX-T Manager version 2.5 or higher
- Appropriate NSX-T API permissions for certificate management
- Valid SSL/TLS certificates compatible with NSX-T requirements

NSX-T Certificate Requirements
-------------------------------

NSX-T has specific requirements for certificates:

- **Format:** PEM-encoded X.509 certificates
- **Key Size:** Minimum 2048-bit RSA or 256-bit ECDSA
- **Subject Alternative Names (SANs):** Must include the FQDN and IP address of the NSX-T Manager nodes
- **Extended Key Usage:** Server Authentication (1.3.6.1.5.5.7.3.1) and Client Authentication (1.3.6.1.5.5.7.3.2) as appropriate
- **Validity:** Certificates should have sufficient validity period (recommended minimum 1 year)

Managing NSX-T Certificates
----------------------------

Uploading Certificates to NSX-T
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a certificate is uploaded to |morpheus| and associated with an NSX-T integration, |morpheus| handles pushing the certificate to the NSX-T Manager:

#. Navigate to |InfTruCer|
#. Click :guilabel:`+ ADD`
#. Select the NSX-T certificate type
#. Complete the certificate fields:

   - **NAME:** Descriptive name for the certificate
   - **NSX-T INTEGRATION:** Select the target NSX-T integration
   - **CERTIFICATE (PEM):** The certificate content
   - **PRIVATE KEY (PEM):** The private key content
   - **CERTIFICATE CHAIN (PEM):** Intermediate and root CA certificates

#. Click :guilabel:`SAVE`

|morpheus| uploads the certificate to the NSX-T Manager and stores the external reference for ongoing management.

Viewing NSX-T Certificates
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Certificates synced from NSX-T integrations appear in the certificate list with their NSX-T association visible. Details include:

- NSX-T Manager reference ID
- Certificate purpose (e.g., API, Cluster Communication)
- Expiration status
- Associated NSX-T services

Replacing NSX-T Certificates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To replace an expiring certificate on an NSX-T Manager:

#. Upload the new certificate to |morpheus| as described above
#. Associate the new certificate with the same NSX-T service
#. |morpheus| coordinates the replacement with the NSX-T Manager API
#. Verify the NSX-T Manager is using the new certificate

.. WARNING:: Replacing certificates on NSX-T management and cluster services requires careful planning. Incorrect certificate replacement can disrupt NSX-T operations. Always verify certificate compatibility in a test environment first.

Certificate Synchronization
----------------------------

|morpheus| periodically synchronizes certificate data from NSX-T integrations:

- Existing certificates on NSX-T are discovered and displayed in |morpheus|
- Certificate expiration dates are tracked
- Status changes (e.g., revocation) are reflected in the |morpheus| UI

To force a synchronization, refresh the NSX-T integration from Infrastructure > Network > Integrations.

Troubleshooting
---------------

**Certificate upload fails:**

- Verify the certificate and key are in valid PEM format
- Ensure the private key matches the certificate (modulus check)
- Confirm NSX-T API connectivity from the |morpheus| appliance

**Certificate not appearing on NSX-T:**

- Check the |morpheus| integration status for the NSX-T instance
- Review the |morpheus| activity log for API errors
- Verify NSX-T API user has certificate management permissions
