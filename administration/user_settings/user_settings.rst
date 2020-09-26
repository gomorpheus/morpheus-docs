.. _user_settings:

User Settings
=============
User settings are accessed by clicking on your display name in the far upper-right corner of the application window. In this dropdown menu, click on the "USER SETTINGS" link.

User Photo
----------
Upload a custom image for your user avatar that is displayed in the top header and user administration sections. **Suggested Photo Dimensions: 128 x 128**

User Settings
-------------
The fields included in this section are described below. By entering any new values in these fields and clicking :guilabel:`SAVE`, the existing value will be overwritten.

- **Username:** Your |morpheus| username
- **First Name:** Your first name (together with Last Name makes up your display name)
- **Last Name:** Your last name (together with First Name makes up your display name)
- **Email:** Your email address
- **Password:** Enter a value and save changes to update your password. The value in the Confirm field below must match
- **Confirm:** Confirm the new password you've entered
- **RECEIEVE NOTIFICATIONS** Determines if Provisioning notifications are emailed to this Users.

.. image:: /images/administration/settings/user_settings500.png

Preferences
-----------
- **Default Group:** Sets the default Group selection when provisioning.
- **Default Cloud:** Sets the default Cloud selection when provisioning.
- **Default Persona:** Sets the default Persona used when logging in.

.. image:: /images/administration/settings/user_settings_preferences_500.png

Linux Settings
--------------
When provisioning a Linux-based resource and opting to have your user created during the provisioning process, the credentials entered in this section will be used to seed that user into the provisioned resource.

- **Username:** The username that will be used with your Linux user
- **Password:** The password that will be used with your Linux user (optional if specifying key)
- **Confirm:** Confirm your entered password. These must match in order for the new password value to be saved
- **SSH Key:** Select a pre-existing SSH key pair object in Morpheus. Required of not specifying password and creating your user during provisioning, or required if ssh password authentication has been disabled.

.. warning:: If your users Linux Settings password and/or key are not defined, and 'Create User" is enabled during provisioning (default), a random password will be generated but not exposed and you will not be able to login with your user. 


.. image:: /images/administration/settings/user_settings_linux_500.png

Windows Settings
----------------
When provisioning a Windows-based resource and opting to have your user created during the provisioning process, the credentials entered in this section will be used to seed that user into the provisioned resource.

- **Username:** The username that will be used with your Windows accounts
- **Password:** The password that will be used with your Windows accounts
- **Confirm:** Confirm your entered password. These must match in order for the new password value to be saved

.. warning:: If your users Windows Settings password is not defined, and 'Create User" is enabled during provisioning (default), a random password will be generated but not exposed and you will not be able to login with your user.

.. image:: /images/administration/settings/user_settings_windows_500.png


API Access
----------
Click the :guilabel:`API Access` button to expand the "API ACCESS" modal. In this modal you can generate or refresh access tokens that can be used with Morpheus API and Morpheus CLI.

If no token yet exists for a particular "CLIENT ID", click :guilabel:`ACTIONS` and then Generate. If a token has expired, we can also regenerate that token by clicking :guilabel:`ACTIONS` and then Regenerate. After regenerating a particular token, you would need to ensure any scripts using those tokens are updated.

After navigating away from the User Settings page, the complete access and refresh tokens will be masked from view. If these are lost or compromised, you can eliminate a token completely by clicking :guilabel:`ACTIONS` and then Clear. If you need to generate a new token for the same Client ID, click :guilabel:`ACTIONS` and then Regenerate.

.. image:: /images/administration/settings/user-tokens.png
  :width: 80%
  
.. note:: Access Tokens are only displayed/available after generation. Copy new Tokens and store appropriately before navigating from ``/user-settings``, they will not be displayed again. 
