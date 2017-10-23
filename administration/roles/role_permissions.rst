Role Permissions
^^^^^^^^^^^^^^^^

.. NOTE:: Permission options for sub-tenant user roles will only list options permitted by the Tenant role applied to the sub-tenant. Sub-Tenant user roles permissions cannot exceed permissions set by the overriding Tenant Role.

FEATURE ACCESS
  Controls Tenant and User access level for sections and features in |morpheus|.
GROUP ACCESS
  Controls User access level for Groups. (Groups are not Multi-Tenant.)
CLOUD ACCESS
  Controls Sub-Tenant access level for Master Tenant publicly visible Clouds.
INSTANCE TYPE ACCESS
  Controls Tenant and User access level for Instance Types.

Feature Access Permissions
``````````````````````````
Feature Access settings control permissions for sections and features in |morpheus|. Permission options include:

None
  Hidden or inaccessible for user
Read
  User can access the section, but cannot edit or create
Full
  User has full access
User
  User only has access to data from the Instances they have created/own.
Remote Console: Auto Login
  RDP and SSH only, controls if user is auto-logged in to Remote Console or presented with login prompt.

- Admin: Appliance Settings (None, Full)
- Admin: Backup Settings (None, Full)
- Admin: Environment Settings	(None, Full)
- Admin: Identity Source	(None, Full)
- Admin: Integrations	(None, Read, Full)
- Admin: License Settings	(None, Full)
- Admin: Log Settings	(None, Full)
- Admin: Monitoring Settings	(None, Full)
- Admin: Provisioning Settings	(None, Full)
- Admin: Roles	(None, Read, Full)
- Admin: Service Plans	(None, Read, Full)
- Admin: Tenant	(None, Full)
- Admin: Tenant - Impersonate Users	(None, Full)
- Admin: Users	(None, Read, Full)
- Admin: Whitelabel Settings	(None, Full)
- Administration: Manage Policies	(None, Read, Full)
- Backups	(None, View, Read, User, Full)
- Billing	(None, Read, Full)
- Infrastructure: Boot	(None, Read, Full)
- Infrastructure: Certificates	(None, Read, Full)
- Infrastructure: Clouds	(None, Read, Full)
- Infrastructure: Groups	(None, Read, Full)
- Infrastructure: Hosts	(None, Read, Full)
- Infrastructure: KeyPairs	(None, Read, Full)
- Infrastructure: Load Balancers	(None, Read, Full)
- Infrastructure: Networks	(None, Read, Full)
- Infrastructure: Security Groups (None, Read, Full)
- Infrastructure: Storage (None, Read, Full)
- Logs (None, Read, User, Full)
- Monitoring (None, Read, User, Full)
- Operations: Analytics (None, Read, Full)
- Operations: Approvals (None, Read, Full)
- Operations: Dashboard (None, Read)
- Operations: Reports (None, Read, Full)
- Operations: Usage (None, Read, Full)
- Provisioning: (None, Read, User, Full)
- Provisioning: Allow Force Delete: (None, Full)
- Provisioning: Apps: (None, Read, User, Full)
- Provisioning: Deployments (None, Read, Full)
- Provisioning: Library (None, Read, Full)
- Provisioning: Migrations (None, Read, Full)
- Provisioning: Tasks (None, Read, Full)
- Provisioning: Tasks - Script Engines (None, Full)
- Provisioning: Virtual Images (None, Read, Full)
- Remote Console (None, Provisioned, Full)
- Remote Console: Auto Login (No, Yes)
- Services: Archives (None, Read, Full)
- Services: Cypher (None, Read, User, Full, Full Decrypted)
