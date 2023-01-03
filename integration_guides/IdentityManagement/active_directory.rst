Active Directory
----------------

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="//www.youtube.com/embed/jJ6GYRUJfLk" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

|

Overview
^^^^^^^^

Active Directory is Microsoft’s primary authentication service. It is widely used in enterprise organizations and even in Microsoft cloud services. While Active Directory also supports LDAP protocol support (which |morpheus| can integrate with as well), |morpheus| includes a dedicated identity integration type specifically for Active Directory. By integrating Active Directory, |morpheus| administrators can fully offload the work of managing the user lifecycle to Active Directory. Creating new users, applying roles to users, updating basic user data, disabling users, and more can be handled in Active Directory and automatically filtered down to |morpheus|. This section includes an example integration walkthrough as well as additional details on the integration feature set.

How It Works
^^^^^^^^^^^^

In |morpheus|, identity sources (if used) are configured per Tenant. In order to see an identity integration or create a new one, navigate to a Tenant detail page (|AdmTen| > Selected Tenant) and click :guilabel:`IDENTITY SOURCES`. From this page we can add a new identity source or click the pencil (|pencil|) icon next to an existing identity source to view or edit it. Any configured identity source will apply to just one Tenant and they cannot be shared. One scenario where this is especially useful is in an MSP appliance where each Tenant is a siloed environment for a specific customer. The customer's own existing Active Directory server and groups can be leveraged to build |morpheus| user accounts with correct role mapping automatically.

When configuring an Active Directory integration in |morpheus|, AD groups are mapped to |morpheus| roles. When the user logs in for the first time, |morpheus| adds the new user account with correct name, email address, and applies one or more roles depending on configuration. Going forward, |morpheus| will sync down any changes to the user, including any role changes based on changes to the user's associated AD groups or updated passwords. Additionally, disabling a user in AD will prevent them from accessing |morpheus|.

.. IMPORTANT:: |morpheus| will connect over port 389 for non-secure LDAP and port 636 for secure LDAP. Ensure that |morpheus| is able to talk to the AD server on the proper port.

Example Integration
^^^^^^^^^^^^^^^^^^^

In a simple example, we have an Active Directory server which has two groups relevant to |morpheus|, "Morpheus Users" and "Morpheus Admins." We will configure |morpheus| so that only users in the "Morpheus Users" group can access |morpheus| in any capacity. Users who are also in the "Morpheus Admins" group will take on the System Admin role in |morpheus|. We'll see later when the integration is configured how |morpheus| roles can be mapped to AD groups. In the same AD server, I have two users. John Smith is in groups "Morpheus Users" and "Morpheus Admins". John Jones is only in the "Morpheus Users" group.

.. image:: /images/integration_guides/identity_sources/ad/ad.png

Knowing the AD scheme and the requirements for |morpheus| user roles, we can begin the process of creating the integration. Identity integrations are specific to each Tenant so begin by navigating to the Tenant detail page (|AdmTen| > Selected Tenant) and clicking :guilabel:`IDENTITY SOURCES`. On setting the type to "Active Directory," the form will update with the needed fields. Note the following basic fields:

- **AD SERVER:** The IP address or hostname for the Active Directory Server
- **DOMAIN:** The AD domain in which the relevant users and groups reside
- **BINDING USERNAME:** A server user which has access to relevant objects on the AD server. In my example, I've used the in-built Administrator user which is the easiest option. Other users may be used depending on your organization's IT security policies but the integration with |morpheus| will not work properly if the user does not have the needed access
- **BINDING PASSWORD:** The password for the user in the prior field

With the basic configurations completed, the remaining configurations will affect |morpheus| user and role generation. A REQUIRED GROUP is optional and is a group the user *must* be in to have any |morpheus| access. Here we require that users be in the "Morpheus Users" group. A DEFAULT ROLE is required and will be assigned to all users regardless of any additional roles they may be assigned based on their AD group membership. Beyond that, all other |morpheus| roles will be listed here and an AD group name can be associated with as many as you required. In this example, we are giving users in the "Morpheus Admins" group the |morpheus| System Admin role. Though we did not use them, it's worth pointing out that ENABLE ROLE MAPPING PERMISSION will give administrators in the Tenant the ability to update the AD role mappings (though they will not have access to the core integration fields such as AD SERVER, DOMAIN, or binding user details). MANUAL ROLE ASSIGNMENT allows users to manually update |morpheus| roles outside of the automatic mappings created by the AD integration.

.. image:: /images/integration_guides/identity_sources/ad/intConfig.png

With the above integration steps completed, users can now log into |morpheus| and a user account with correct roles will automatically be created. In our example case, John Smith has logged in and we can see he is assigned the default role as well as the System Admin role based on his AD group associations. Going forward, |morpheus| will continue to sync any changes to these users. For example, |morpheus| roles may be updated based on changing AD groups or user access may be completely revoked by disabling the user in AD.

.. image:: /images/integration_guides/identity_sources/ad/user.png

Adding an Active Directory Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmTen|
#. Select a Tenant
#. Select :guilabel:`IDENTITY SOURCES`
#. Select :guilabel:`+ ADD IDENTITY SOURCE`
#. Set the TYPE to "Active Directory"
#. Populate the following:

   Name
    A friendly name in |morpheus| for the AD integration
   AD Server
    The Hostname or IP address of AD Server
   Domain
    The AD domain in which the relevant user and group objects reside
   USE SSL
    Indicates whether SSL should be used for communication with the AD server. |morpheus| will connect over port 389 for non-secure LDAP and port 636 for secure LDAP, ensure |morpheus| can connect to the AD server over the correct port
   Binding Username
    A username for a service account which has access to relevant objects (users, groups, etc.). For ease, the "Administrator" user may be used
   Binding Password
    The password for the above account
   Required Group
    The AD group users must be in to have access (optional, see example in the prior section)
   Default Role
    The default role a user is assigned when they are in the required group or if no specific group mapping applies to the user (see example in prior section)
   ENABLE ROLE MAPPING PERMISSION
    When selected, Tenant users with appropriate rights to view and edit Roles will have the ability to set role mapping for the Identity Source integration. This allows the Tenant user to edit only the role mappings without viewing or potentially editing the basic Identity Source configuration (AD server, domain, binding user details, etc)
   MANUAL ROLE ASSIGNMENT
    When selected, administrators can manually edit Roles for users created through this identity source integration from the user detail page (|AdmUse| > Selected user)

  .. NOTE:: For more on Identity Source role mapping permissions, see the `associated guide <https://support.morpheusdata.com/s/article/How-to-enable-Subtenant-admins-to-edit-Identity-Source-role-mapping?language=en_US>`_ in our KnowledgeBase.

#. Select :guilabel:`SAVE CHANGES`.

Now allowed AD users can login to |morpheus| via their Active Directory credentials and a User will be automatically generated to |morpheus| with matching metadata and mapped Role permissions.

.. NOTE:: Sub-tenant |morpheus| API authentication for Active Directory generated users is not currently supported.

Troubleshooting
^^^^^^^^^^^^^^^

If you're unable to get the Active Directory integration to work, the following troubleshooting steps may be useful to ensure your appliance can talk to the Active Directory server.

1. Open firewall ports

  **Source:** |morpheus| appliance

  **Destination:** AD server's FQDN or IP address

  **Non-SSL AD integration:** TCP-389

  **SSL AD integration:** TCP-636

2. Checking open LDAP connections from the |morpheus| appliance

  Connect to a |morpheus| appliance box and run the following:

  .. code-block:: bash

    $ sudo lsof i- | grep :ldap

3. Check LDAP connectivity from the |morpheus| appliance

  Connect to a |morpheus| appliance box and run the following. Be sure to replace the placeholder values in the command with the correct values for your environment:

  .. code-block:: bash

    $ ldapsearch   -x -h xx.xx.xx.xx -D "binding-user@acme.com" -W -b "cn=users,dc=acme,dc=com"

4. Run tcpflow from the |morpheus| appliance for non-SSL enabled AD identity Integrations

  Use tcpflow from the |morpheus| appliance and then start the identity source configuration once again. Keep in mind this will only work for AD servers which are not SSL enabled:

  .. code-block:: bash

    $ sudo tcpflow -i any -c -v port 389

5. Check the AD and domain controllers event logs

  Check the event logs for LDAP queries from the |morpheus| appliance to ensure network connectivity.
