Domains
-------

``Infrastructure -> Network -> Domains``

Overview
^^^^^^^^

The Domains section is for creating and managing domains for use in |morpheus| . Domains are used for setting FQDNs, joining Windows Instances to Domains, and creating A Records with DNS Integrations. The Domains section is also a multi-tenant endpoint for managing domain settings across multiple accounts

* Added and synced Domains are available for selection in the Domain dropdown when provisioning an Instance.
* Default domains can be set for Clouds and Networks in their Advanced Options sections.
* Images can be flagged to Auto-Join Domains in the `Provisioning -> Virtual Images` section.

.. IMPORTANT:: For an Instance to auto-join a Domain, a Domain must set in the Advanced Options section of the Cloud or Network used when provisioning.

Adding Domains
^^^^^^^^^^^^^^

1. Navigate to `Infrastructure -> Network -> Domains`
2. Select *+ Add*
3. Enter the following:
   * Domain Name:: Example demo.example.com
   * Description:: Descriptive meta-data for use in |morpheus| 
   * Public Zone:: Check for Public Zones, leave uncheck for Private Zones.
   * Join Domain Controller:: Enable to have Windows instances join a Domain Controller
   * Username:: Admin user for Domain Controller
   * Password:: Password for DC Username
   * DC Server:: (optional) Specify the URL or Path of the DC Server
   * OU Path:: (optional) Enter the OU Path for the connection string.
   * Permissions:: Configure Tenant permissions in |morpheus| for the Domain (only applicable in Multi-tenant |morpheus| setups)
   * Tenant:: Select the Tenant to set permissions to for the Domain.
   * Visibility:

     * Private: Only Accessible by the select Tenant
     * Public: Available for use by all Tenants.
     
4. Save Changes

The Domain has been added and will be selectable in Domain dropdown during provisioning, and in Cloud and Network settings.

.. NOTE:: Only resources assigned to the Master Tenant can be set as Publicly visible. If the Tenant assigned is not the master tenant, visibility will automatically change to private.

Editing and Removing Domains
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Domains can be edited by selecting the `Actions` dropdown for the Domain and selecting `Edit`.
* Added Domains can be removed from |morpheus| by selecting the `Actions` dropdown for the Domain and selecting `Remove`.

Setting the default domain on a Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Clouds`.
#. Edit the target Cloud.
#. Expand `Advanced Options` section.
#. In the *Domain* dropdown, select the Domain.
#. Save Changes

Setting the default domain on a Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Network`.
#. Edit the target Network.
#. Expand `Advanced Options` section.
#. In the *Domain* dropdown, select the Domain.
#. Save Changes

Selecting a Domain while provisioning an instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. While creating an instance, in the `Configure` section, expand the `DNS Options`.
#. Select Domain from the *Domain* dropdown.
