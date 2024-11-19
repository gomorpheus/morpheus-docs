OneLogin
--------

By integrating OneLogin with |morpheus|, users can access |morpheus| with their existing credentials set up within the OneLogin platform. Additionally, administrators can manage user access including Role assignment and enabling or disabling users from within the OneLogin platform. As employees are onboarded, change positions, or leave the company, additional user management within the |morpheus| platform is not necessary.

Adding OneLogin Identity Source Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To begin, log into OneLogin with an administrator account to gather some needed pieces of information. From the top menu bar, select Administration. From the admin panel, click Developers > API Credentials. Click the button labeled "New Credential". Provide a name for the new API credentials and select "Manage Users" as the permissions type. Store the credentials somewhere they can be retrieved in the next step.

.. image:: /images/integration_guides/identity_sources/oneLogin/oneLoginKey.png
  :width: 50%

Back in |morpheus|, navigate to the Users list page (|AdmUse|) and click :guilabel:`IDENTITY SOURCES`. The list of currently-integrated identity providers is here. Click :guilabel:`+ ADD IDENTITY SOURCE` to start a new integration for OneLogin. Fill in the fields below:

- **TYPE:** OneLogin
- **NAME:** A name for the identity source integration in |morpheus|
- **DESCRIPTION:** An optional description for the identity source
- **ONELOGIN SUBDOMAIN:** The subdomain from your OneLogin portal URL. For example, "morpheus-dev" if your portal is accessed at morpheus-dev.onelogin.com. Incorrect subdomains will cause login attempts to |morpheus| to fail
- **ONELOGIN REGION:** Specify US or EU region
- **API CLIENT SECRET:** OneLogin API client secret which was gathered earlier in this walkthrough
- **API CLIENT ID:** OneLogin API client ID which was gathered earlier in this walkthrough
- **REQUIRED ROLE:** Enter a role which OneLogin users logging into |morpheus| must have to gain access to |morpheus|
- **DEFAULT ROLE:** The default |morpheus| Role applied to users created from the OneLogin integration if no other role mapping is specified in other Role Mappings fields
- **ROLE MAPPINGS:** All existing |morpheus| Roles will be listed with fields to enter OneLogin Roles to create a mapping. Users with OneLogin roles matching the role mappings will be assigned the appropriate Role(s) in |morpheus| when signing in
- **ENABLE ROLE MAPPING PERMISSION:** When selected, users with appropriate rights to view and edit Roles will have the ability to set role mapping for the Identity Source integration. This allows the user to edit only the role mappings without viewing or potentially editing the core integration fields (such as the API keys)
- **MANUAL ROLE ASSIGNMENT:** When selected, administrators can manually edit Roles for users created through this identity source integration from the user detail page (|AdmUse| > Selected user).

Select :guilabel:`SAVE CHANGES` and the OneLogin Integration will be added.

Users can now login to |morpheus| with OneLogin credentials. The first login will create a user in |morpheus| matching the username, email and password from OneLogin. If a REQUIRED ROLE is specified in the Identity Source settings, only users with that Role in OneLogin will be able to login to |morpheus|.

.. IMPORTANT:: OneLogin users will not authenticate in |morpheus| if there is an existing |morpheus| User with matching username or email address.

You can now test the integration by logging in with user credentials which have been configured in OneLogin. On the first login, a new user will be created with the same username, email address, and password as contained in OneLogin. On subsequent logins, |morpheus| will sync with OneLogin to make sure the user hasn't been disabled or if its Role(s) have changed in OneLogin which would affect its corresponding Roles in |morpheus|.

The |morpheus| identity source integration is interacting with the OneLogin APIs in the list below. This reference may be needed to ensure |morpheus| is integrating using an API key with sufficient privileges. In a situation where troubleshooting is needed, first confirm these APIs can be accessed using the provided key.

- ``/auth/oauth2/token`` - Generate Token
- ``/api/1/users/$user_id/roles`` - Get Roles
- ``/api/1/login/auth`` - Create Session
- ``/api/1/users/$user_id`` - Get User
- ``/api/1/roles/$role_id`` - Get Role
- ``/api/1/roles?name=$role_name`` - Find Role
