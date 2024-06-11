NSX Cloud
---------

NSX Cloud is a networking solution that allows administrators to define networking and security policies for applications running in private and public clouds. When integrated with |morpheus| users can apply an NSX Cloud integration with either VMware vCenter or VMware on AWS Cloud types. This offers robust syncing and manipulation of NSX Cloud constructs as well as the ability to consume those networks when provisioning to VMware and VMware on AWS Cloud targets.

Features
--------

- Sync and manage DHCP servers
- Sync and manage DHCP relays
- Sync and manage network segments
- Sync and manage distributed firewall rules
- Sync and manage tier-1 routers
- Sync and manage groups, including management groups and compute groups
- Integration with VMware and VMware on AWS-type Clouds

Integrating with VMware Clouds
------------------------------

Integration with a VMware Cloud requires the Cloud integration to be pre-existing. If you need to integrate a VMware Cloud first, refer to the `VMware Cloud integration guide <https://docs.morpheusdata.com/en/7.0.3/integration_guides/Clouds/vmware/vmware.html>`_ in |morpheus| UI documentation for full details.

To begin a new NSX Cloud integration, navigate to |InfNetInt|. Click :guilabel:`+ ADD` and then click "NSX Cloud". Make the following configurations to create the integration with NSX Cloud:

- **NAME:** A friendly name for the NSX Cloud integration in |morpheus|
- **VISIBILITY:** This option is only available from the |mastertenant|. Select "Public" to make the NSX Cloud integration available to all Tenants. Select "Private" to reserve the integration for the |mastertenant|
- **API HOST:** The API access URL for NSX Cloud
- **API KEY:** An API token granting sufficient access for |morpheus| to work with all relevant NSX constructs
- **CLOUD:** Select the VMware Cloud integration that NSX Cloud should integrate with

Once done, click :guilabel:`ADD NETWORK INTEGRATION`. After a brief moment, the new integration will be created and will appear alongside other network integrations on the network integration list page. We can verify that NSX Cloud and the VMware Cloud are integrated by editing the VMware Cloud (|InfClo| > Selected VMware Cloud > EDIT button). Expand the Advanced Options panel of the EDIT CLOUD modal and the NSX Cloud integration should be set under the NETWORK MODE configuration.

Integrating with VMware on AWS Clouds
-------------------------------------

Integration with a VMware on AWS Cloud requires the Cloud integration to be pre-existing. If you still need to integrate VMware on AWS with |morpheus|, navigate to |InfClo| and create that Cloud integration first. If you are creating the VMware on AWS Cloud now, bear in mind that you will need to update firewall inbound rules to allow the |morpheus| appliance to connect with VMware on AWS. If this step is not done, any attempts to create that Cloud integration will fail. Log into the NSX Cloud web console and click on the Security tab. Within the security tab, go to the Gateway Firewall section and the Management Gateway tab within it. Edit the list of sources for your vCenter inbound rules. The IP address for the |morpheus| appliance should be among the allowed inbound addresses.

After confirming the VMware on AWS Cloud is created, we can go back into |morpheus| to create the NSX Cloud integration. Navigate to |InfNetInt|. Click :guilabel:`+ ADD` and then click "NSX Cloud". Make the following configurations to create the integration with NSX Cloud:

- **NAME:** A friendly name for the NSX Cloud integration in |morpheus|
- **VISIBILITY:** This option is only available from the |mastertenant|. Select "Public" to make the NSX Cloud integration available to all Tenants. Select "Private" to reserve the integration for the |mastertenant|
- **API HOST:** The API access URL for NSX Cloud
- **API KEY:** An API token granting sufficient access for |morpheus| to work with all relevant NSX constructs
- **CLOUD:** Select the VMware on AWS Cloud integration that NSX Cloud should integrate with

Once done, click :guilabel:`ADD NETWORK INTEGRATION`. After a brief moment, the new integration will be created and will appear alongside other network integrations on the network integration list page. We can verify that NSX Cloud and the VMware Cloud are integrated by editing the VMware Cloud (|InfClo| > Selected VMware Cloud > EDIT button). Expand the Advanced Options panel of the EDIT CLOUD modal and the NSX Cloud integration should be set under the NETWORK MODE configuration.

Managing NSX Cloud
------------------

With the integration complete, you can now examine the detail section for the new integration. From the network integration list page (|InfNetInt|), select the NSX Cloud integration that was just created. From this section, we can create, manage, and delete DHCP servers and relays, network segments, firewall rules, tier-1 routers, and groups.
