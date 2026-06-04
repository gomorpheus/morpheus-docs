.. _private_keys:

Private Key Management
======================

Overview
--------

|morpheus| securely stores and manages private keys associated with SSL/TLS certificates. Private keys are encrypted at rest and access is controlled through role-based permissions. This section covers best practices and operational procedures for key management within |morpheus|.

Key Storage Security
--------------------

All private keys stored in |morpheus| are protected by multiple layers of security:

- **Encryption at Rest:** Keys are stored using AES-256 encryption in the |morpheus| database
- **Access Control:** Only users with the appropriate role permissions can view or manage certificates containing private keys
- **Masked Display:** Private keys are never displayed in plain text in the UI after upload
- **Audit Trail:** Key access and modifications are logged in the |morpheus| activity feed

Supported Key Types
-------------------

|morpheus| supports the following private key formats:

- **RSA:** 2048-bit and 4096-bit RSA keys (most common)
- **ECDSA:** Elliptic Curve keys (P-256, P-384, P-521)
- **PEM Format:** Base64-encoded DER format enclosed in ``-----BEGIN PRIVATE KEY-----`` / ``-----END PRIVATE KEY-----`` headers

Key Passphrases
---------------

|morpheus| supports passphrase-protected private keys:

- When uploading a key with a passphrase, enter the passphrase in the **KEY PASSPHRASE** field
- The passphrase is stored encrypted alongside the key
- |morpheus| automatically decrypts the key when needed for operations (e.g., SSL termination)

.. NOTE:: It is recommended to use passphrase-protected keys for an additional layer of security, particularly when keys are shared across multiple systems.

Uploading Private Keys
----------------------

Private keys are uploaded as part of a certificate record:

#. Navigate to |InfTruCer|
#. Click :guilabel:`+ ADD` or edit an existing certificate
#. In the **PRIVATE KEY (PEM)** field, paste the full PEM-encoded private key content
#. If the key is passphrase-protected, enter the passphrase in the **KEY PASSPHRASE** field
#. Click :guilabel:`SAVE`

Key Rotation
------------

To rotate a private key (e.g., for security compliance):

#. Generate a new key pair and obtain a new certificate signed with the new key
#. Edit the existing certificate record in |morpheus|
#. Replace the certificate content and private key with the new values
#. Save the updated record
#. Verify services using the certificate continue to function correctly

.. TIP:: For zero-downtime key rotation on load balancers, add the new certificate as a separate entry first, update the load balancer configuration to use the new certificate, then remove the old entry.

Key Export Restrictions
-----------------------

By design, |morpheus| does not provide a mechanism to export or download private keys once uploaded. This is a security measure to prevent unauthorized key extraction. If a private key is needed outside of |morpheus|, it must be retrieved from the original source or regenerated.

SSH Key Pairs
-------------

SSH key pairs for server authentication are managed separately in the **Key Pairs** section of Infrastructure > Trust. See the Key Pairs documentation for details on managing SSH keys used during provisioning.
