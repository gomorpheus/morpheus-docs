Azure Active Directory SSO (SAML)
---------------------------------

Azure Active Directory Single Sign-on can be added as a Identity Source in |morpheus| using the SAML Identity Source Type. The Azure AD SSO configuration is slightly different
than other SAML providers, and this guide will assist in adding a Azure AD SSO Identity Source.

Create Azure Enterprise Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Login to the `Azure Portal <https://portal.azure.com>`_
#. Navigate to: ``Azure Active Directory > Enterprise Applications``
#. Click the ``+ New application`` button at the top
#. Click the ``+ Create your own application`` button at the top
#. Ensure ``Integrate any other application you don't find in the gallery (Non-gallery)`` is selected and enter a name for the app.  Common examples are:  ``MorpheusSSO``
#. Click the ``Create`` button at the bottom and wait for it to complete
#. Once created, you'll be in the ``Overview`` of the application created.  Navigate to the ``Single sign-on`` section from the left pane
#. Choose ``SAML`` as the Single sign-on method
#. Copy both the ``Login URL`` and ``Logout URL`` in Step 4, we'll need these in some of the next steps
#. Before we can continue configuring the application, the configuration needs to be generated in |morpheus| for more data

Create an Azure AD SAML Integration in |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Azure requires inputting the ``Identifier (Entity ID)`` and ``Reply URL (Assertion Consumer Service URL)`` in the Azure SSO configuration before it provides the Endpoints and Certificate
necessary to add the Integration into |morpheus|. In order to get the ``Identifier (Entity ID)`` and ``Reply URL (Assertion Consumer Service URL)`` to input into Azure SSO configuration,
we need to create a ``Azure AD SAML SSO`` integration in |morpheus| first.

To add the integration:

#. Login to |morpheus|
#. Navigate to |AdmTen|
#. Click a tenant hyperlink
#. Click the :guilabel:`IDENTITY SOURCES` button in the Tenant detail page
#. Click the :guilabel:`+ ADD IDENTITY SOURCE` button
#. Select ``Azure AD SAML SSO`` from the ``TYPE`` dropdown
#. Add

   * Name

   * (Optional) Description
   
   * Paste the ``Login URL`` copied from Azure into the ``LOGIN REDIRECT URL`` field
   
   * Paste the ``Logout URL`` copied from Azure into the ``SAML LOGOUT REDIRECT URL`` field
 
#. This is the minimum information needed for now, which will let us generate the details needed from |morpheus|.  We'll return to this configuration page later to enter more information.
#. Click the :guilabel:`SAVE CHANGES` button

.. IMPORTANT:: Setting SAML REQUEST to "No Signature" and SAML RESPONSE to "Do Not Validate Assertion Signature" is allowed but not recommended for security reasons.

Upon saving, the `Entity ID` (``Identifier (Entity ID)``) and `SP ACS URL` (``Reply URL (Assertion Consumer Service URL)``) will be provide in the Identity Source list view. Copy these for use in Azure SSO configuration.

  .. image:: /images/integration_guides/identity_sources/azure_ad_saml/saml_setup.png
      :width: 40%

Configure Azure Enterprise Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This guide assumes an Azure AD Enterprise Application has already been created. Please refer to documentation above, if this has not already been configured.

#. Navigate to: ``Azure Active Directory > Enterprise Applications > Single sign-on``
#. Choose ``SAML`` as the Single sign-on method
#. On Step 1 (``Basic SAML Configuration``), click the ``Edit`` button and enter the following:
  
   * Identifier (Entity ID)
      Enter the ``Entity ID`` URL from the |morpheus| Identity Source Integration above
  
   * Reply URL (Assertion Consumer Service URL)
      Enter the ``SP ACS URL`` from the |morpheus| Identity Source Integration above
  
   * Logout URL
      Enter the following format:  ``https://yourUrl/login/``
      If this is a sub tenant, the format may instead be the following:  ``https://yourUrl/login/account/1``
      The login URL can be found under :guilabel:`IDENTITY SOURCES` in the tenant

#. On Step 2 (``Attributes and Claims``), click the ``Edit`` button
#. Click the ``Add a group claim`` button at the top
#. Choose ``All groups`` and ensure ``Group ID`` is selected for the ``Source attribute`` dropdown
  
   .. note:: You can also choose ``Security groups``, which ever makes more sense for the organization

#. Close the pane and return to the Enterprise Application in the ``Single sign-on`` section
#. On Step 3 (``SAML Certificates``), click the ``Download`` link next to ``Certificate (Base64)`` and ``Federation Metadata XML``
  
   .. note::  The files will download, keep them available for later configuation in |morpheus|

#. Navigate to ``Users and Groups`` in the left pane
#. Click the ``Add user/group`` button
#. Add Azure groups to this application that will be able to login to |morpheus|

   .. note:: Note the object ID for each of these groups, as they will be used later when configuring |morpheus| to map the group to roles

#. Once groups have been added, click the ``Assign`` button at the bottom

Configure the Azure AD SAML Integration in |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Login to |morpheus| using ``Username and Password``, as usual
#. Navigate to |AdmTen|
#. Click a tenant hyperlink
#. Select :guilabel:`IDENTITY SOURCES` in the Tenant detail page
#. Click the pencil (edit) next to the integration created previously
#. Ensure the ``SAML REQUEST`` field is set to ``Self Signed``
  
   .. note:: A custom RSA signature can be used here if needed, if required by the orgnaization

#. Ensure the ``SAML RESPONSE`` field is set to ``Validate Assertion Signature``

   .. note:: With this setting, if the assertion signature ever changes in the Azure Enterprise Application, this would need to be updated to match

#. Edit/view the downloaded ``Federation Metadata XML`` (``.xml`` extension) file from the previous section

   .. note:: It is recommended to use ``Microsoft Edge``, or another browser, to view the contents

#. In the ``Federation Metadata XML`` file, locate the ``<X509Certificate> </X509Certificate>`` under the ``<Signature>`` section.  Copy the entire contents between the ``<X509Certificate>`` and ``</X509Certificate>``, it is very long
#. Paste the value copied from the ``Federation Metadata XML`` file into the ``Public Key (Optional)`` box, below the ``SAML RESPONSE`` dropdown

Configure Role Mappings
^^^^^^^^^^^^^^^^^^^^^^^

Role mappings will map Azure AD Groups to Morpheus Roles. Azure AD users will be assigned Roles in |morpheus| upon signing in based on their Group Membership in Azure AD.

.. IMPORTANT:: Use an Azure Groups ``Object ID``, not Group name, when entering Role Mappings. Example: ``7626a4a2-b388-4d9b-a228-72ce9a33bd4b``

DEFAULT ROLE
  Role a Azure AD user will be assigned by default upon signing in to |morpheus| using this Identity Source.
REQUIRED AZURE AD GROUP OBJECT ID
  Object ID of Azure AD Group a user must be a member of to be authorized to sign in to |morpheus|. Users not belonging to this Group will not be authorized to login to |morpheus|. This field is optional, and if left blank, any user from the Azure AD App will be able to sign in to |morpheus| and will be assigned the Default Role if no Role Mappings match AD Group membership.
GROUP ASSERTION ATTRIBUTE NAME
  Enter ``http://schemas.microsoft.com/ws/2008/06/identity/claims/groups`` for Azure AD SSO
Additional Role Mappings
  The existing Roles in |morpheus| will be listed. To map a |morpheus| Role to an Azure AD Group, enter the Object ID of the desired Azure AD Group in the `Role Attribute Value` field for the corresponding |morpheus| Role.

.. IMPORTANT:: Use an Azure Groups ``Object ID``, not Group name, when entering Role Mappings. Example: ``7626a4a2-b388-4d9b-a228-72ce9a33bd4b``

ENABLE ROLE MAPPING PERMISSION
  When selected, Tenant users with appropriate rights to view and edit Roles will have the ability to set role mapping for the Identity Source integration. This allows the Tenant user to edit only the role mappings without viewing or potentially editing the Identity Source configuration.
MANUAL ROLE ASSIGNMENT
  When selected, administrators can manually edit Roles for users created through this identity source integration from the user detail page (|AdmUse| > Selected user).

.. NOTE:: For more on Identity Source role mapping permissions, see the `associated guide <https://support.morpheusdata.com/s/article/How-to-enable-Subtenant-admins-to-edit-Identity-Source-role-mapping?language=en_US>`_ in our KnowledgeBase.

Once populated, select :guilabel:`SAVE CHANGES` and the SAML identity source integration will be added. The Identity Source can be edited anytime to deactivate or change Role Mappings or other values.

.. NOTE:: If Role mappings are edited after Azure AD SSO users have signed into |morpheus|, currently logged in users will need to log out of |morpheus| for the new Role mappings to take effect, when applicable.

#. Under the ``Role Azure Group Mappings`` secton, verify the ``DEFAULT ROLE`` dropdown has the role in |morpheus| selected that all users will be assigned by default

   * It is recommended that this role contains no permissions, which ensures that anyone who authenticates gets no access

#. Under the ``Role Azure Group Mappings`` secton, you will see role names listed.  Next to these are text boxes with ``Assertion Attribute Mappings`` inside.  Enter group object IDs from Azure into these text boxes.  This will map the Azure AD groups to specific roles in Morpheus
#. Finally, click ``Save Changes`` at the bottom of the page

Here is an example of the configuration above:

  .. image:: /images/integration_guides/identity_sources/azure_ad_saml/saml_setup_complete.png
    :width: 20%

Azure Group Lookups
^^^^^^^^^^^^^^^^^^^

When a user in azure ad has more that 150 group attributes, Azure does not include the group claims in the SAML response, and |morpheus| is required to query Microsoft Graph to obtain the users group attribute values. When there are users that are members of more that 150 groups, populate the ``Azure Group Lookups`` section in order for those users to be able to use the Azure AD SAML SSO integration, otherwise no groups will be obtained and proper role mappings cannot occur.

AZURE TENANT ID
  Add Azure AD Tenant ID if user group membership will exceed 150. See :ref:`azure_ids` for information on obtaining an Azure AD Tenant ID
AZURE APP ID
  Add Azure AD Application (Client) ID if user group membership will exceed 150. See :ref:`azure_ids` for information on obtaining an Azure AD Application (Client) ID
AZURE APP SECRET
  Add Azure Application (Client) Secret if user group membership will exceed 150. See :ref:`azure_secret` for information on creating an Azure Application (Client) Secret
ROLE LINK ATTRIBUTE NAME
  default: http://schemas.microsoft.com/claims/groups.link. This is not normally changed.

Logging Into |morpheus| with Azure AD SAML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the |morpheus| URL
#. A new button will appear to allow sign-in using Azure AD SAML, with the same name as the integration.  Click the button
   .. image:: /images/integration_guides/identity_sources/azure_ad_saml/sign_in_page.png
     :width: 30%

#. Sign-in with your Microsoft/Azure account
   .. image:: /images/integration_guides/identity_sources/azure_ad_saml/ms_signin.png
     :width: 20%

.. NOTE:: If no local users other than the System Admin have been created, "USERNAME AND PASSWORD" option will not be displayed, only the SAML option.