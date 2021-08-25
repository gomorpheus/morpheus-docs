Azure Active Directory SSO (SAML)
---------------------------------

Azure Active Directory Single Sign-on can be added as a Identity Source in |morpheus| using the SAML Identity Source Type. The Azure AD SSO configuration is slightly different than other SAML providers, and this guide will assist in adding a Azure AD SSO Identity Source.

Create a Azure AD SAML Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Azure requires inputting the `Identifier (Entity ID)` and `Reply URL (Assertion Consumer Service URL)` in the Azure SSO configuration before it provides the Endpoints and Certificate necessary to add the Integration into |morpheus|. In order to get the `Identifier (Entity ID)` and `Reply URL (Assertion Consumer Service URL)` to input into Azure SSO config, we need to create a base SAML Integration in |morpheus| first.

To add a base SAML integration:

#. Navigate to ``Administration -> Tenants``
#. Select a tenant.
#. Select IDENTITY SOURCES in the Tenant detail page
#. Select :guilabel:`+ ADD IDENTITY SOURCE`.
#. Select ``SAML SSO`` from the TYPE field
#. Add a Name, optional Description and any value in the LOGIN REDIRECT URL field.
    Since we do not have the LOGIN REDIRECT URL from Azure yet, type any text such as ``test`` into the LOGIN REDIRECT URL field so the Identity Source Integration can be saved and the `Identifier (Entity ID)` and `Reply URL (Assertion Consumer Service URL)` generated. We will edit the Integration with the proper LOGIN REDIRECT URL after configuring SSO in Azure.
#. Select :guilabel:`SAVE CHANGES`.

Upon save, the `Entity ID` (Identifier (Entity ID)) and `SP ACS URL` (Reply URL (Assertion Consumer Service URL)) will be provide in the Identity Source list view. Copy these for use in Azure SSO config.

..
  this needs replaced or just left out
  .. image:: /images/integration_guides/identity_sources/azure_ad_saml/saml_setup.png
    :width: 80%
    :align: center

Configure Azure SSO
^^^^^^^^^^^^^^^^^^^

This guide assumes an Azure AD Application has already been created in Azure with a subscription level high enough to configure SSO in the application. Please refer to Azure documentation if this has not already been configured.

#. Next, in the Azure Active Directory Application details page, select ``Single sign-on``, then enter the following:

   * Single Sign-on Mode dropdown
        Select ``SAML-based Sign-on``
   * Identifier (Entity ID)
        Enter the ``Entity ID`` URL from the |morpheus| Identity Source Integration above.
   * Reply URL (Assertion Consumer Service URL)
        Enter the ``SP ACS URL`` from the |morpheus| Identity Source Integration above.

#. Save and click the `Test SAML Settings` button. Azure will confirm connection with |morpheus|
#. In Azure's `User Attributes & Claims` settings (step 2), select ``Add a group claim`` with value ``user.groups [SecurityGroup]``

   **User Attributes & Claims** config
   
   .. list-table:: **Required Claim**
      :widths: auto
      :header-rows: 1

      * - Claim name
        - Value
      * - Unique User Identifier (Name ID)
        - user.userprincipalname [nameid-format:emailAddress]
   |
    
   .. list-table:: **Additional Claims**
      :widths: auto
      :header-rows: 1

      * - Claim name
        - Value
      * - http://schemas.microsoft.com/ws/2008/06/identity/claims/groups
        - user.groups [SecurityGroup]
      * - http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
        - user.mail
      * - http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname
        - user.givenname
      * - http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name
        - user.userprincipalname
      * - http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname
        - user.surname


#. Copy or keep available for reference the the Claim Names/Namespace URLs for entering Role Attribute Values in the |morpheus| Identity Source Integration.
#. In Azure SSO config, if one has not been generated, select ``Create new certificate`` to generate a new SAML Signing Certificate.
#. Enter a valid email address to receive certificate expiration notifications (these are not |morpheus|-generated email).
#. In Azure SSO config, select ```Configure {AD App Name}``
#. In the `Configure sign-on` pane, copy the following:

   * SAML Single Sign-On Service URL
      This will be used for the LOGIN REDIRECT URL in the |morpheus| Identity Source Integration settings
   * Sign-Out URL
      This will be used for the LOGOUT REDIRECT URL in the |morpheus| Identity Source Integration settings
   * Click on the ``SAML XML Metadata`` link, open the xml file, and copy the key between the ``<X509Certificate>`` and ``</X509Certificate>``.
      This will be used for the `Public Key` value in the SAML RESPONSE section of the |morpheus| Identity Source Integration settings

      Example Key (this key is an example and is not valid):

     .. code-block:: bash

      MIIC8ECCAdigAwIBAgIQEOZXlNx5wY9Dc6OwlsKEMzANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0xODAyMTYxNTU4NTlaFw0yMTAyMTYxNTU4NTlaMDQxMjAwBgNVBAMTTU1pY3Jvc29mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnRpZmljYXRlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2k/V6GcBpRkoxJd0DLbhubwd0kp65LD9IIh5PUY2ohBHvrFAy3SZ04mXoH7LWvY3oNrqxaNAksbYF6phOkONf/XeTdzor14xdGnTuD9zRqPsJHHisyfFBUG/CxYxzO6w9fAPzJGLzc0Y7o5lMW2OjINaqI4R/pqp3qw+nYf7DXSzY6tf1Sspk64jfZDt1jSVjD7upMItKPeOCRmeBUcnebjzwXqFBO7l4Vf5g1oEJvftT7Wpr4VVmoLh8rFGWbQ1wlmtsK9RrWTqdt3su2H9uNrEjWiZ62x6ate2fs0dXnz17KoV7RQOpqYtjom76jNUzorcl73D5AGwW6x+2wIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQCSjf2IOG6O3wdOmkfJ/pH6xzQVRz0GZQpol9ViQJJbJJqhLm4LjWT9VU2lYqdi0NdgtK7QthZo4J0ZFdUG6qfFTfPKqVn0AEHxiM4JWxfigzdMJUutHcRRoaJ8VvywZYJKE91e4TDuBOw8XqdBiBx627ZybXCuR/y56+ksYSRP87XdOcVvTftHYmQnDOf0qKrpgMK7LtmsEwqc7rKX7nTCenZnBEBOCFDBVH4QEzMrAznEPdJnQs9nJZBNCYJUrCRXbPKpXE9u8MlTVq4swFm96xsXkfeP8NFsgrXmzOn3BsHaBXqdhrrkbwq85VPWUaoIomlhAWQq/seC

#. Save the SSO config in Azure AD app and return to |morpheus|

Edit the existing Azure AD SAML Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Now that we have the required information, we can finalize the Azure AD SAML Integration in |morpheus|

#. Edit the existing Azure AD SAML Integration created in the first step and populate the following:

   LOGIN REDIRECT URL
      Add the SAML Single Sign-On Service URL copied from Azure SSO config.
   LOGOUT REDIRECT URL
      Add the Sign-Out URL copied from Azure SSO config.
   SAML RESPONSE
      Set to "Validate Assertion Signature", then in the "Public Key" field enter the Public Key value we discussed in the last section
   GIVEN NAME ATTRIBUTE NAME (May have to click "show" to see hidden SAML Assertion Attribute Names fields)
      Enter the ``givenname`` Namespace url from Azure SSO config: http://schemas.xmlsoap.org/ws/2005/05/identity/claims
   SURNAME ATTRIBUTE NAME
    Enter the ``emailaddress`` Namespace url from Azure SSO config: http://schemas.xmlsoap.org/ws/2005/05/identity/claims
   EMAIL ATTRIBUTE NAME (May need to scroll down within the SAML Assertion Attribute Names section see this field)
    Enter the ``surname`` Namespace url from Azure SSO config: http://schemas.xmlsoap.org/ws/2005/05/identity/claims

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
  When selected, administrators can manually edit Roles for users created through this identity source integration from the user detail page (Administration > Users > Selected user).

.. NOTE:: For more on Identity Source role mapping permissions, see the `associated guide <https://support.morpheusdata.com/s/article/How-to-enable-Subtenant-admins-to-edit-Identity-Source-role-mapping?language=en_US>`_ in our KnowledgeBase.

Once populated, select :guilabel:`SAVE CHANGES` and the SAML identity source integration will be added. The Identity Source can be edited anytime to deactivate or change Role Mappings or other values.

.. NOTE:: If Role mappings are edited after Azure AD SSO users have signed into |morpheus|, currently logged in users will need to log out of |morpheus| for the new Role mappings to take effect, when applicable.

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


Signing In to |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^

When there is an active SAML/Azure AD SSO Identity Source Integration, a new button will appear on the |morpheus| login page with the name of the Identity Source Integration as the button title. Example: :guilabel:`MORPHEUS SSO`. Another button titled "USERNAME AND PASSWORD" is also added for |morpheus| account authentication outside of an Identity Source.

.. image:: /images/integration_guides/identity_sources/azure_ad_saml/sign_in_page.png
  :width: 60%
  :align: center

* SAML/Azure AD SSO users can log into |morpheus| by clicking the SAML button
      This will redirect the User to Azure AD app sign in url. If they are currently signed into Azure and authorized, the user will be instantly signed into |morpheus|.
* Local |morpheus| users can select "USERNAME AND PASSWORD" to sign in with their local credentials as before.

.. NOTE:: If no local users other than the System Admin have been created, "USERNAME AND PASSWORD" option will not be displayed, only the SAML option.
