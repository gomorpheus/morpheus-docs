.. _user_settings:

User Settings
=============

User settings are accessed by clicking on your display name in the far upper-right corner of the application window. In this dropdown menu, click on the "USER SETTINGS" link.

User Photo
----------

In this section, you can choose to upload a user photo or avatar to display as you use the application. This image will appear in a small circle immediately to the left of your display name in the upper-right hand corner of the application window.

User Settings
-------------

The fields included in this section are described below. By entering any new values in these fields and clicking :guilabel:`SAVE`, the existing value will be overwritten.

- **Username:** Your |morpheus| username
- **First Name:** Your first name (together with Last Name makes up your display name)
- **Last Name:** Your last name (together with First Name makes up your display name)
- **Email:** Your email address
- **Password:** Enter a value and save changes to update your password. The value in the Confirm field below must match
- **Confirm:** Confirm the new password you've entered

Preferences
-----------

- **Default Group:** If a Group is entered here, you will default to the entered Group when provisioning
- **Default Cloud:** If a Cloud is entered here, you will default to the entered Cloud when provisioning

Linux Settings
--------------

When provisioning a Linux-based resource and opting to have your user created during the provisioning process, the credentials entered in this section will be used to seed that user into the provisioned resource.

- **Username:** The username that will be used with your Linux accounts
- **Password:** The password that will be used with your Linux accounts
- **Confirm:** Confirm your entered password. These must match in order for the new password value to be saved
- **SSH Key:** Select a pre-existing SSH key pair object in Morpheus if you'd like to use one

Windows Settings
----------------

When provisioning a Windows-based resource and opting to have your user created during the provisioning process, the credentials entered in this section will be used to seed that user into the provisioned resource.

- **Username:** The username that will be used with your Windows accounts
- **Password:** The password that will be used with your Windows accounts
- **Confirm:** Confirm your entered password. These must match in order for the new password value to be saved

API Access
----------

Click the API Access link to expand the "API ACCESS" modal. In this modal you can generate or refresh access tokens that can be used with Morpheus API and Morpheus CLI.

If no token yet exists for a particular "CLIENT ID", click :guilabel:`ACTIONS` and then Generate. If a token has expired, we can also regenerate that token by clicking :guilabel:`ACTIONS` and then Regenerate. After regenerating a particular token, you would need to ensure any scripts using those tokens are updated.

After navigating away from the User Settings page, the complete access and refresh tokens will be masked from view. If these are lost or compromised, you can eliminate a token completely by clicking :guilabel:`ACTIONS` and then Clear. If you need to generate a new token for the same Client ID, click :guilabel:`ACTIONS` and then Regenerate.

.. image:: /images/administration/api_access.png
  :width: 80%
