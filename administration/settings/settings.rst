Appliance Settings
==================

The `Administration -> Settings` section sets global configuration parameters for the Appliance, Tenant Registration, Email, Proxy and sets which Cloud types are enabled.

Appliance Settings
------------------

Host Level Firewall Enabled
  Enables or Disables the host level firewall. This must be Enabled to use |morpheus| Security Groups.
Appliance URL
  The default URL used for Agent install and Agent functionality. All Instances and Hosts must be able to resolve and reach this URL over 443 for successful agent install and communication.

.. NOTE:: Alternate Appliance URLs can be configured per Cloud in the `Edit Cloud -> Advanced Options` section.

Internal Appliance URL (PXE)
  For PXE-Boot your appliance needs to be routable directly with minimal NAT masquerading. This allows one to override the default appliance url endpoint for use by the PXE Server. If this is unset, the default appliance url will be used instead.
API Allowed Origins
  Specifies which origins are allowed to access the |morpheus| API.
Enable SSL Verification of Agent (Communications)
  Enabling SSL Verification of Agent Communications requires a valid Certificate be installed on the Appliance.
Disable SSH Password Authentication
  Only allow ssh login using SSH keys. When true, SSH Password Authentication will not be enabled for VM's and Hosts provisioned after the setting is enabled.

Tenant Management Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^

Registration Enabled
  If enabled, the appliance login screen will have a "NEED AN ACCOUNT? SIGN UP HERE" link added, enabling new Tenant registration.
Default Tenant Role
  Sets the default Tenant Role applied to Tenants created from Tenant Registration.
Default User Role
  Sets the default User Role applied to the User created from a Tenant Registration.

.. Docker Privileged Mode::

User Management Settings
^^^^^^^^^^^^^^^^^^^^^^^^

Expire Password After (Days)
  User account passwords will expire after the entered number of days. Enter 0 or leave the field empty to opt out of this feature.
Disable User After Attempts (Number of Attempts)
  Disable a User account after a specified number of failed login attempts. Enter 0 or leave the field empty to opt out of this feature.
Disable User If Inactive For (Days)
  Disable a User account if inactive for the entered number of days. The User will not be able to log into the appliance again until another User with sufficient rights enables the account. Enter 0 or leave the field empty to opt out of this feature.
Send warning email before deactivating (Days)
  Enter the number of days prior to account deactivation that a warning email should be sent. For example, enter "5" to warn the User when they are five days short of the deactivation time entered in the prior field. Enter 0 or leave the field empty to opt out of this feature.

Email Settings
^^^^^^^^^^^^^^

A default installation of Morpheus uses a online service called postmarkapp. Morpheus api requests to the postmarkapp service to send notification e-mails.

To add your own SMTP server you will need to go to the Administration and Settings of your Morpheus appliance. You will then need to provide Morpheus the following information, your mail server systems administrator should provide you with the below information and the preferred encryption method.

* From Address
* SMTP Server
* SMTP Port
* SSL Enabled
* TLS Encryption
* SMTP User
* SMTP Password

We recommend that you add your Morpheus server to your SMTP white list as well as using user authentication as an additional security measure.

Once you have added your SMTP server information into Morpheus scroll down the Administration and Settings page and press the blue save button which can be found under enabled clouds.

When you have saved your SMTP server settings in the Morpheus appliance you will then need to restart the Morpheus-ui. To restart the Morpheus-ui connection to your Morpheus server via ssh and run the below command.

``sudo morpheus-ctl restart morpheus-ui``

.. IMPORTANT:: If you do not restart the Morpheus-ui the notifications will be sent by the original notification service postmarkapp. Please note it can take up to 3 minutes for the ui to become reachable again.
 has a built in SMTP server for email notifications and alerts. An alternate SMTP server can be specified below:

Add an alternate SMTP Server:

* From Address
* SMTP Server
* SMTP Port
* SSL Enabled
* TLS Encryption
* SMTP User
* SMTP Password

Proxy Settings
^^^^^^^^^^^^^^

The |morpheus| Appliance can be configured to communicate through a Proxy server for Cloud API's and Agent communication back to the Appliance.

.. NOTE:: Additional Proxy configuration is available in the `Infrastructure -> Network -> Proxies` section. Added Proxies can be scoped to Clouds in the `Edit Cloud -> Advanced Options` section of the Cloud.

Add a Global Proxy server by entering the following:

* Proxy Host
* Proxy Port
* Proxy User
* Proxy Password
* Proxy Domain
* Proxy Workstation

Enabled Clouds (Types)
^^^^^^^^^^^^^^^^^^^^^^^

Controls which types of Cloud can be created.

- When a Cloud type is disabled, it will be removed from the available options when adding new Clouds in ``Infrastructure``. Existing Clouds will not be affected.

.. include:: whitelabel.rst
.. include:: license.rst
.. include:: utilities.rst
