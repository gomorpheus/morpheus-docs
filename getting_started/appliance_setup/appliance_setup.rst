Initial Appliance Setup
=======================

Appliance Setup
---------------

After installation, log into the appliance at the URL presented upon completion. An initial setup wizard walks through the first account and user creations.

1. Enter Master Account name

   * Typically, the Master Account name is your Company name.

#. Create Master User

   * First Name
   * Last Name
   * Username
   * Email Address
   * Password
     * Must be at least 8 characters longs and contain one each of the following: Uppercase letter, lowercase letter, Number, Special Character

#. Enter Appliance Name & Appliance URL

   * The Appliance Name is used for white labeling and as a reference for multi-appliance installations.

   * The Appliance URL is the URL all provisioned instances will report back to. Example: https://example.morpheusdata.com. The Appliance URL can be changed later, and also set to different url per cloud integration.

#. Optionally Enable or Disable Backups, Monitoring, or Logs from this screen.

    .. Note:: You may adjust these settings from the Administration section.

    .. NOTE:: The Master Account name is the top-level admin account.

    .. NOTE:: The Master User is the system super user and will have full access privileges.


Upon completing of the initial appliance setup, you will be taken to the Admin -> Settings page, where you will add your License Key.

Login Methods
-------------

Master Tenant

- Enter username or email. and password

Subtenant

To login, subtenants can either use the master tenant URL with ``subtenant\username`` formatting:

Example:
    I have a username ``subuser`` that belongs to a tenant with the subdomain ``subaccount``.
    When logging in from the main login url, I would now need to enter in: ``subaccount\subuser``

Or use the tenant specific URL which can be found and configured under |AdmTen| > Select Tenant > Identity Sources.

.. image:: /images/getting_started/tenant_url.png

.. important:: In 3.4.0+ Subtenant users will no longer be able to login from the main login url without specifying their subdomain.

Configure Cloud-init Global Settings
------------------------------------

When using cloud-init, cloudbase-init, VMware Tools customizations, or Nutanix Sysprep, Global Linux User and Windows Administrator credentials can be set using the settings in `Administraiton - Provisioning`. Its is recommended to define these settings after installation unless credentials are defined per Virtual Image for Provisioning.

Add a License Key
-----------------

In order to provision anything in |morpheus| , a |morpheus| License Key must be applied.

If you do not already have a license key, one may be requested from https://www.morpheushub.com or from your |morpheus| representative.

In the Administration -> Settings section, select the LICENSE tab, paste your License Key and click :guilabel:`UPDATE`

.. image:: /images/getting_started/license_key.png

When the license is accepted, your license details will populate in the Current License section.

If you receive an error message and your license is not accepted, please check it was copied in full and then contact your |morpheus| representative. You can also verify the License Key and expiration at https://www.morpheushub.com.
