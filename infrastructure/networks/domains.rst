.. _domains:

Domains
-------

``Infrastructure > Network > Domains``

Overview
^^^^^^^^

The Domains section is for creating and managing domains for use in |morpheus|. Domains are used for setting FQDNs, joining Domains, and creating DNS records. The Domains section is also a multi-tenant endpoint for managing domain settings across multiple tenants.

* Domains are synced in from Cloud, DNS and Network Integrations. Domains can also be user created.
* Active Domains are available for selection in the Domain dropdown when provisioning an Instance
* Default Domains can be set for Clouds and Networks in their Advanced Options sections.
* Images can be flagged to Auto-Join Domains in the ``Infrastructure > Network > Domains`` section

.. IMPORTANT:: For an Instance to auto-join a Domain, a Domain must set in the Advanced Options section of the Cloud or Network used when provisioning

Adding Domains
^^^^^^^^^^^^^^

1. Navigate to ``Infrastructure > Network > Domains``
2. Select :guilabel:`+ ADD`
3. Enter the following:

   :Domain Name: Ex. demo.example.com
   :Description: Descriptive metadata for use in |morpheus|
   :Display Name: Overrides the displayed name in domain selection components, which is useful when using many OU paths
   :Public Zone: Check for Public Zones, leave uncheck for Private Zones
   :Workflow: Select an existing Workflow which will be applied to Instances at provision time when they are associated with the domain. This is useful for any domain-related scripting you may currently use. For example, you may want to ensure a machine is removed from the domain when it's torn down which could be accomplished by creating a Provisioning Workflow (with teardown phase Tasks) and associating the Workflow with the domain
   :Active: Active Domains are available for selection in Domain selection fields across |morpheus|. Inactive Domains are removed from Domain selection fields.
   :Join Domain Controller: Check to have Windows instances join a Domain Controller
   :Username: Admin user for Domain Controller. ``domain\username`` format required when specifying OU Path
   :Password: Password for DC user account
   :DC Server: (optional) Specify the URL or Path of the DC Server
   :OU Path: (optional) Enter the OU Path for the connection string.
   :Guest Username: (optional) If set, this will change the provisioned hosts RPC Service User after domain join. Useful when a domain policy disables the  Administrator account that typically would be set as the RPC user on a host record. |morpheus| will update the RPC username and password on the host(s) record after domain join with the specified Guest Username and Guest Password. The RPC username and password are used for auth during Remote Procedure Call (RPC) executions over winrm, ssh and guest tools. 
   :Guest Password: (optional) The password for the Guest User account indicated in the prior field

4. Click :guilabel:`Save Changes`

The Domain has been added and will be selectable in the Domain dropdown during provisioning, and in Cloud and Network settings.

Editing Domain Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^

To edit visibility permissions for a domain, navigate to ``Infrastructure > Network > Domains``. In the row for the selected domain, click MORE > Permissions. Within the Permissions modal, set Group and Tenant access permissions.

.. NOTE:: Only resources assigned to the Master Tenant can be set as Publicly visible. If the Tenant assigned is not the Master Tenant, visibility will automatically change to private. Additionally, only Master Tenant users can set visibility for domains. Domains originating in a subtenant will always be private to that subtenant.

Group Access
````````````

Configure the domain to be visible to all Infrastructure Groups or only to selected Groups. If the domain is scoped to specific Groups, Users whose Roles do not give them Group access will not have access to the domain. Additionally, users will not be able to set the domain as the default on a Cloud which is not a part of the selected Groups.

Tenant Permissions
``````````````````

When set to public, all Tenants will have visibility into the domain and can join their Instances to the domain. When set to private, users can select specific Tenants which should have access to the domain.

Editing and Removing Domains
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Domains can be edited by selecting the `Actions` dropdown for the Domain and selecting `Edit`, or by selecting the |pencil| icon in list views.
* Added Domains can be removed from |morpheus| by selecting the `Actions` dropdown for the Domain and selecting `Remove`, or the |trash| icon in list views.

Setting the default domain on a Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Clouds`.
#. Edit the target Cloud.
#. Expand `Advanced Options` section.
#. In the *Domain* dropdown, select the Domain.
#. Save Changes

Setting the default domain on a Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Network`.
#. Edit the target Network.
#. Expand `Advanced Options` section.
#. In the *Domain* dropdown, select the Domain.
#. Save Changes

Selecting a Domain while provisioning an instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. While creating an instance, in the `Configure` section, expand the `DNS Options`.
#. Select Domain from the *Domain* dropdown.
