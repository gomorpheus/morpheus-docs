SAML Integration
----------------

Overview
^^^^^^^^

The |morpheus| SAML identity source integration allows customers to add user SSO to |morpheus|, authenticated by external login SAML providers.

.. image:: /images/samlLoginGeneric.png

Adding a SAML Integration
^^^^^^^^^^^^^^^^^^^^^^^^^

To add a SAML integration:

#. Navigate to |AdmTen|
#. Select a tenant.
#. Select :guilabel:`IDENTITY SOURCES` in the Tenant detail page
#. Select :guilabel:`+ ADD IDENTITY SOURCE`.
#. Select `SAML SSO` from the `TYPE` field
#. Add a Name and optional Description for the SAML integration

.. image:: /images/integration_guides/identity_sources/saml_sso/saml.png

There are 4 sections with fields that need to be populated depending on the desired configuration:

- SAML Configuration
- Role Mappings
- Role Options
- Assertion Attribute Mappings

SAML Configuration
^^^^^^^^^^^^^^^^^^

LOGIN REDIRECT URL
  This is the SAML endpoint |morpheus| will redirect to when a user signs into |morpheus| via SAML
SAML LOGOUT REDIRECT URL
  The URL |morpheus| will POST to when a SAML user logs out of |morpheus|
INCLUDES SAML REQUEST PARAMETER
  **Yes** (recommended) - the AuthN request will be sent via the ?SAMLRequest= parameter in the URL (GET)

  **No** - the AuthN request will be submitted in the body of the request (POST)

  .. NOTE:: The SAML SP documentation should mention which binding to use but GET is most common
SAML REQUEST
  **No Signature** - No signature is used on the SAML request

  **Self Signed** - A self-signed X.509 Certificate is gentered after clicking :guilabel:`SAVE CHANGES`. This signature value can be used by the SAML SP to verify the authenticity of the request

  **Custom RSA Signature** - Import a custom RSA Private Key and respective X.509 Certificate. This signature value can be used by the SAML SP to verify the authenticity of the request
SAML RESPONSE
  **Do Not Validate Assertion Signature** - The SAML response signature from the SAML SP will not be validated

  **Validate Assertion Signature** - The SAML reponse signature from the SAML SP will be validated.  Enter the SAML SP X.509 certificate in the **Public Key** field

.. IMPORTANT:: Setting SAML REQUEST to "No Signature" and SAML RESPONSE to "Do Not Validate Assertion Signature" is allowed but not recommended for security reasons.

Role Mappings
^^^^^^^^^^^^^

DEFAULT ROLE
  Role any SAML user will be assigned by default
ROLE ATTRIBUTE NAME
  The name of the attribute/assertion field that will map to |morpheus| roles, such a MemberOf
REQUIRED ROLE ATTRIBUTE VALUE
  Attribute/assertion value that a user must be assigned/a member of to be authorized, such as group or role in the SAML SP. This is obtained from the attribute/assertion defined in the ROLE ATTRIBUTE NAME field
<|morpheus| ROLE NAME>
  Additional roles that can be mapped to a user, which will add to the DEFAULT ROLE. Attribute value that a user must be assigned/a member of to be authorized, such as group or role in the SAML SP. This is obtained from the attribute/assertion defined in the ROLE ATTRIBUTE NAME field

.. NOTE:: For more on Identity Source role mapping permissions, see the `associated guide <https://support.morpheusdata.com/s/article/How-to-enable-Subtenant-admins-to-edit-Identity-Source-role-mapping?language=en_US>`_ in our KnowledgeBase.

Role Options
^^^^^^^^^^^^

ENABLE ROLE MAPPING PERMISSION
  When selected, Tenant users with appropriate rights to view and edit Roles will have the ability to set role mapping for the Identity Source integration. This allows the Tenant user to edit only the role mappings without viewing or potentially editing the Identity Source configuration.
MANUAL ROLE ASSIGNMENT
  When selected, administrators can manually edit Roles for users created through this identity source integration from the user detail page (|AdmUse| > Selected user).

Assertion Attribute Mappings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GIVEN NAME ATTRIBUTE NAME
  SAML SP field value to map to |morpheus| user First Name
SURNAME ATTRIBUTE NAME
  SAML SP field value to map to |morpheus| user Last Name
EMAIL ATTRIBUTE
  SAML SP field value to map to |morpheus| user email address

.. image:: /images/integration_guides/identity_sources/saml_sso/saml_assertion_attribute_mappings.png

Once populated, select :guilabel:`SAVE CHANGES` and the SAML identity source integration will be added.

In the :guilabel:`Identity Sources` section, important information for configuration of the SAML integration is provided. Use the SP ENTITY ID and SP ACS URL for configuration on the external login SAML provider side.

.. NOTE:: In some cases, the SAML provider may need these values before providing the LOGIN REDIRECT URL and other values.  When creating the integration, the NAME and LOGIN REDIRECT URL can contain any values, then selecting SAVE CHANGES will generate the above values.  The NAME and LOGIN REDIRECT URL can be edited later, once the SAML configuration is created in the SAML provider.

* ENTITY ID
* SP ACS URL
* LOGIN REDIRECT URL
* SP METADATA

.. image:: /images/integration_guides/identity_sources/saml_sso/identity_sources_info.png

Sample Metadata code output:

.. code-block:: bash

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?><EntityDescriptor entityID="https://someip.com/saml/eDKL60P25" xmlns="urn:oasis:names:tc:SAML:2.0:metadata"><SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol"><NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</NameIDFormat><AssertionConsumerService index="0" isDefault="true" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://someip.com/externalLogin/callback/eDKL60P25"/></SPSSODescriptor></EntityDescriptor>

.. NOTE:: Different SAML providers will have different field names and requirements. An Okta SAML Dev environment was used for the example integration in this article.

Okta SAML SSO
^^^^^^^^^^^^^

For Okta SAML integration, the following fields are mapped:

* LOGIN REDIRECT URL : Identity Provider Single Sign-On URL
* ENTITY ID: Audience URI (SP Entity ID)
* SP ACS URL: Single sign on URL

Onelogin SAML SSO Guide
^^^^^^^^^^^^^^^^^^^^^^^

  .. toggle-header::
      :header: **Click to expand**

      Adding SAML integration in |morpheus|

      #. Navigate to |AdmTen|
      #. Select the Tenant to add the Identity Source Integration
      #. Select :guilabel:`IDENTITY SOURCES`
      #. Select :guilabel:`+ IDENTITY SOURCE`
      #. Enter the following **minimal** settings to generate the SSO details needed in |morpheus|:
        TYPE
          SAML SSO
        NAME
          Name of the Identity Source Integration in |morpheus|
        LOGIN REDIRECT URL
          Enter any value in this location, **it does not need to be correct**

          .. IMPORTANT::
            We will return later and enter the correct information, once it is generated from the SAML Identity Provider (IdP)

      #. Select :guilabel:`SAVE CHANGES`
      #. After saving the changes, a new Identity Source will appear with an ``ENTITY ID``, ``SP ACS URL``, and the value entered for the ``LOGIN REDIRECT URL``.  These details will be needed when configuring the SAML Identity Provider (IdP)
        .. image:: /images/integration_guides/identity_sources/onelogin/morpheus_saml_minimal_setup.png
          :scale: 50%
      #. Navigate and login to the OneLogin Administration Portal
      #. Navigate to ``Applications > Applications``
      #. Select the ``Add App`` button
        .. image:: /images/integration_guides/identity_sources/onelogin/add_app_button.png
          :scale: 75%
      #.  In the search box, search for **SAML Custom Connector (Advanced)**
      #.  Select the **SAML Custom Connector (Advanced)** option displayed
      #.  Enter a ``Display Name`` and then select the ``Save`` button
        .. image:: /images/integration_guides/identity_sources/onelogin/display_name.png
          :scale: 50%
      #. Once the Application is created, you are placed in the settings of the new application
      #. Select ``Configuration`` from the left menu and enter the following, from the |morpheus| Identity Source that was generated previously
        Audience (EntityID)
          This is the ``ENTITY ID`` from the |morpheus| Identity Source
        Recipient
          This is the ``SP ACS URL`` from the |morpheus| Identity Source
        ACS (Consumer) URL Validator
          This a RegEx of the ``SP ACS URL`` from the |morpheus| Identity Source.

          Using the example URL of ``https://morpheus.test.local/externalLogin/callback/YMCOa27tb``, this would be the format to match it ``^https:\/\/morpheus\.test\.local\/externalLogin\/callback\/YMCOa27tb$``
        ACS (Consumer) URL
          This is the ``SP ACS URL`` from the |morpheus| Identity Source
        Single Logout URL
          This is your |morpheus| login URL, so you are redirected back to |morpheus| after logging out.
          
          Example root/primary tenant URL format:  https://morpheus.test.local/login

          Example subtenant URL format:  https://morpheus.test.local/login/account/2

          .. image:: /images/integration_guides/identity_sources/onelogin/application_config1.png
            :scale: 75%
        SAML initiator
          Set to **Service Provider**
        SAML nameID format
          Set to **Unspecified**
        SAML signature element
          Set to **Both**
        .. image:: /images/integration_guides/identity_sources/onelogin/application_config2.png
          :scale: 75%
      #. Select the ``Save`` button
        .. image:: /images/integration_guides/identity_sources/onelogin/save_button.png
          :scale: 50%
      #. Select ``Parameters`` from the left menu
      #. Below is an example of default recommended parameters
        Paramters overview
          .. image:: /images/integration_guides/identity_sources/onelogin/parameters.png
            :scale: 50%
        roles parameter configuration
          .. image:: /images/integration_guides/identity_sources/onelogin/parameters_roles.png
            :scale: 50%
        .. IMPORTANT::
          These are example parameters that can be created to send as assertions to |morpheus|, using the default values |morpheus| expects.  The ``SAML Custom Connector (Advanced) Field`` can be changed but the field name will need to be configured from the default in |morpheus|.

        .. IMPORTANT::
          OneLogin can have roles (like groups in other IdPs) that can be mapped to |morpheus| Roles.  Alternate assertions can be used as well but in this guide, we'll map the ``roles`` field to the |morpheus| Roles.  Examples of Roles in OneLogin and |morpheus| could be ``SystemAdmins``, ``ReadOnlyUsers``, etc.
      #. Assign users to the application 
      #. Assign users to OneLogin Roles, if mapping the OneLogin Roles to |morpheus| Roles
      #. Select ``SSO`` from the left menu
      #. Copy or note the ``SAML 2.0 Endpoint (HTTP)`` and the ``SLO Endpoint (HTTP)`` URLs
      #. Switch back to |morpheus| and edit the Identity Source previously created, to enter the details generated by OneLogin
        #. In the ``LOGIN REDIRECT URL`` field, paste the value from the ``SAML 2.0 Endpoint (HTTP)`` in OneLogin (overwriting the temporary value you initially entered)
        #. In the ``SAML LOGOUT REDIRECT URL`` field, paste the value from the ``SLO Endpoint (HTTP)`` in OneLogin
        .. image:: /images/integration_guides/identity_sources/onelogin/morpheus_saml_configuration.png
      #. Under ``ROLE MAPPINGS``
        #. Enter ``roles`` for the ``ROLE ATTRIBUTE NAME``
        #. Type the name of a role in OneLogin to map to a role in |morpheus|
        .. image:: /images/integration_guides/identity_sources/onelogin/morpheus_saml_roles1.png
          :scale: 50%

        .. image:: /images/integration_guides/identity_sources/onelogin/morpheus_saml_roles2.png
          :scale: 50%
      #. Select :guilabel:`SAVE CHANGES`
      #. Navigate to your |morpheus| URL
      #. Select the :guilabel:`OneLogin` button
         .. image:: /images/integration_guides/identity_sources/onelogin/morpheus_login.png
      #. Enter your OneLogin username and password (or any other authentication required)
         .. image:: /images/integration_guides/identity_sources/onelogin/login.png
      #. At this point, you should be successfully logged in.  Note that your specific permissions will depend on the settings configured in the ``ROLE MAPPINGS`` section when editing the Identity Source in |morpheus|