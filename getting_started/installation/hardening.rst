Appliance Security & Hardening
===============================

This section covers security considerations for the |morpheus| appliance installation, including database encryption, key rotation, and hardening recommendations.

Database Encryption
-------------------

|morpheus| automatically encrypts all sensitive data stored in the application database using **AES-256-GCM** encryption. This includes:

- Cloud integration credentials (service passwords, API keys)
- Compute server access passwords and console passwords
- Integration and storage provider credentials
- Container registry passwords
- Security endpoint credentials
- All credential store entries

Encryption is transparent — data is encrypted on write and decrypted on read at the application layer. The database itself only stores ciphertext.

Encryption Key Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The encryption system uses a two-part key:

- **Base key** — Built into the application
- **Key suffix** — A customer-configurable value set in ``/etc/morpheus/morpheus.rb``

When a key suffix is configured, it is appended to the base key before deriving the AES-256 encryption key. Each encrypted value also includes a unique random salt, ensuring that identical plaintext values produce different ciphertext.

Configuring the Encryption Key Suffix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To set or change the encryption key suffix:

#. Edit ``/etc/morpheus/morpheus.rb``
#. Add or update the encryption key suffix setting:

   .. code-block:: ruby

      morpheus['encryptionKeySuffix'] = 'your-unique-secret-value'

#. Run reconfigure to apply:

   .. code-block:: bash

      sudo morpheus-ctl reconfigure

#. Restart the application:

   .. code-block:: bash

      sudo morpheus-ctl restart morpheus-ui

On the next application startup, |morpheus| automatically **re-encrypts all sensitive database fields** using the new key. This process runs once during bootstrap and covers all credential types across the system.

.. IMPORTANT:: Store the encryption key suffix securely. If this value is lost and the database needs to be restored to a new appliance, encrypted credentials cannot be recovered without the original key suffix.

.. WARNING:: In a high-availability (HA) deployment, all application nodes must have the same ``encryptionKeySuffix`` value in their ``morpheus.rb``. Mismatched keys between nodes will cause decryption failures.

Rotating the Encryption Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To rotate the encryption key:

#. Choose a new key suffix value
#. Update ``/etc/morpheus/morpheus.rb`` on all appliance nodes with the new value
#. Restart the application on each node

The application will detect the key change and re-encrypt all sensitive fields with the new key on startup. No manual migration is required.

.. NOTE:: Key rotation requires a brief application restart. During the re-encryption process (which runs at startup), the application is not serving requests. For large deployments with many stored credentials, this may take a few minutes.

Cypher Secrets Engine
----------------------

In addition to database-level encryption, |morpheus| provides a dedicated secrets engine called **Cypher** (accessible at |TooCyp|). Cypher provides:

- Per-secret encryption with unique per-item keys
- TTL-based lease management with automatic expiration
- Mount-path-based access control
- Integration with infrastructure credential management (see :doc:`/infrastructure/servers/credentials`)

Cypher secrets are encrypted independently from database field encryption and use their own key material.

Hardening Recommendations
--------------------------

Network Access
^^^^^^^^^^^^^^^

- Restrict management access (ports 443, 80) to authorized networks only
- Use a firewall or security group to limit access to the appliance
- Place the appliance behind a load balancer with TLS termination for HA deployments
- Restrict SSH access (port 22) to administrative users only

TLS Configuration
^^^^^^^^^^^^^^^^^^

- Replace the self-signed certificate with a valid CA-signed certificate
- Configure TLS in ``/etc/morpheus/morpheus.rb``:

  .. code-block:: ruby

     nginx['ssl_certificate'] = '/etc/morpheus/ssl/cert.pem'
     nginx['ssl_certificate_key'] = '/etc/morpheus/ssl/key.pem'

- Run ``sudo morpheus-ctl reconfigure`` after certificate changes

Authentication
^^^^^^^^^^^^^^^

- Integrate with an enterprise identity provider (Active Directory, LDAP, SAML, or OIDC) rather than relying solely on local accounts
- Enforce MFA through your identity provider
- Set strong password policies for any local accounts
- Disable or lock unused default accounts
- Use API tokens with appropriate expiration for service integrations

Role-Based Access
^^^^^^^^^^^^^^^^^^

- Apply the principle of least privilege — assign the minimum permissions required for each role
- Use Tenant Roles to restrict Subtenant capabilities
- Audit role assignments regularly
- Set sensitive permissions (Admin: Appliance Settings, Admin: Backup Settings) to None or Read for non-administrator roles

Service Account Security
^^^^^^^^^^^^^^^^^^^^^^^^^

- Always configure the ``encryptionKeySuffix`` in production deployments (do not rely on the default key alone)
- Use Cypher or an external credential store for integration passwords rather than entering them inline
- Rotate cloud integration credentials periodically
- Audit integration credential access through the activity log

Appliance Updates
^^^^^^^^^^^^^^^^^^

- Keep the |morpheus| appliance on the latest supported release
- Subscribe to security advisories for timely awareness of vulnerabilities
- Test updates in a non-production environment before applying to production

Backup Security
^^^^^^^^^^^^^^^^

- Encrypt appliance backups at rest
- Store backups in a separate location from the appliance
- Protect backup storage with access controls — backups contain encrypted credentials that could be targeted
- Test backup restoration periodically to verify encryption key availability
