Efficient IP
------------

Features
^^^^^^^^

* Network Pools synchronization
* DNS Zone & Zone record synchronization
* Host Record synchronization
* Total & Free IP status bar for networks
* Network Grid and List view with IP Status and records, date and user tracking
* Automatic and manual IP Reservations, DNS A/PTR record creation and deletion

Adding EfficientIP SOLIDserver Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The EfficientIP SOLIDserver integration type is a plugin that must be added to |morpheus| before the option to create one will be available. In the future, users will be able to download this and other plugin types from a centralized marketplace. For now, the plugin jar file can be compiled from a public Github repository or can be requested from your account team. See the `Plugins Section <https://docs.morpheusdata.com/en/latest/administration/integrations/integrations.html#plugins>`_ of |morpheus| documentation for more on the process of uploading the plugin JAR to your appliance.

#. Navigate to |InfNetInt| and click :guilabel:`+ ADD`
#. Under the IPAM section, select EfficientIP SOLIDserver
#. Configure the following:

    - **NAME:** Friendly name for this EfficientIP SOLIDserver integration
    - **ENABLED:** When checked, this integration will be accessible in |morpheus|
    - **API URL:** The FQDN for the EfficientIP server, not a specific path
    - **USERNAME:** The username for an EfficientIP service account. Bear in mind this account will need API access as well as the rights to work with pools, zones, and records you wish to consume from |morpheus|
    - **PASSWORD:** The password for the above named account
    - **THROTTLE RATE:** In larger environments, it may be necessary to introduce a rate limit on calls to the EfficientIP API from |morpheus|. If the EfficientIP console UI becomes less responsive than it was prior to integration with |morpheus|, it may be due to a high number of API calls in the background from |morpheus|. In such a case, start with a 50ms throttle rate and adjust accordingly depending on performance
    - **DISABLE SSL SNI VERIFICATION:** If necessary, disable the check for a valid SSL certificate on the EfficientIP server
    - **INVENTORY EXISTING:** 
