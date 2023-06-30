Onelogin SAML SSO Guide
^^^^^^^^^^^^^^^^^^^^^^^

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
         
         .. image:: /images/integration_guides/identity_sources/saml_sso/morpheus_saml_minimal_setup.png
           :scale: 50%

      #. Navigate and login to the OneLogin Administration Portal
      #. Navigate to ``Applications > Applications``
      #. Select the ``Add App`` button
         
         .. image:: /images/integration_guides/identity_sources/onelogin/add_app_button.png
           :scale: 75%

      #. In the search box, search for **SAML Custom Connector (Advanced)**
      #. Select the **SAML Custom Connector (Advanced)** option displayed
      #. Enter a ``Display Name`` and then select the ``Save`` button
         
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
           This is your |morpheus| login URL, so you are redirected back to |morpheus| after logging out.  Example:  https://morpheus.test.local/login
         SAML initiator
           Set to **Service Provider**
         SAML nameID format
           Set to **Unspecified**
         SAML signature element
           Set to **Both**
          
           Example root/primary tenant URL format:  https://morpheus.test.local/login

           Example subtenant URL format:  https://morpheus.test.local/login/account/2

         .. image:: /images/integration_guides/identity_sources/onelogin/application_config1.png
           :scale: 50%
         
         .. image:: /images/integration_guides/identity_sources/onelogin/application_config2.png
           :scale: 50%

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
           :scale: 50%

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
           :scale: 75%

      #. Enter your OneLogin username and password (or any other authentication required)
         
         .. image:: /images/integration_guides/identity_sources/onelogin/login.png
           :scale: 50%

      #. At this point, you should be successfully logged in.  Note that your specific permissions will depend on the settings configured in the ``ROLE MAPPINGS`` section when editing the Identity Source in |morpheus|