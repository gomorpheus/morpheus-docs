.. _plugin_dns:

Plugin DNS Providers
====================

Overview
--------

|morpheus| supports a plugin-based DNS provider framework that allows extending DNS management capabilities beyond the built-in providers. DNS plugins implement a standard interface enabling |morpheus| to manage DNS zones and records through custom or third-party DNS services.

Plugin DNS providers appear alongside built-in providers when configuring DNS integrations and can be used anywhere DNS management is invoked, including:

- Automatic DNS record creation during Instance provisioning
- Manual DNS record management through the Domains interface
- DNS record cleanup during Instance teardown
- Integration with naming policies for automated DNS naming

Architecture
------------

The plugin DNS framework is built on the |morpheus| Plugin API:

- Plugins implement the ``DnsProvider`` interface
- Each plugin registers one or more DNS provider types
- Providers handle zone and record CRUD operations
- |morpheus| manages the lifecycle and invocation of plugin operations

Available plugin DNS providers are determined by which plugins are installed on the |morpheus| appliance (Administration > Integrations > Plugins).

Configuring a Plugin DNS Provider
----------------------------------

To add a plugin-based DNS integration:

#. Ensure the DNS plugin is installed (|AdmIntPlu|)
#. Navigate to |InfNetSer| (Infrastructure > Network > Services)
#. Click :guilabel:`+ ADD`
#. Select the plugin DNS provider type from the dropdown
#. Complete the provider-specific configuration fields:

   - **NAME:** Descriptive name for the DNS integration
   - **Additional fields vary by plugin** (e.g., API URL, credentials, zone filters)

#. Click :guilabel:`SAVE`

|morpheus| validates the connection and synchronizes available DNS zones from the provider.

Using Plugin DNS with Provisioning
-----------------------------------

Once configured, plugin DNS providers integrate with the provisioning workflow:

#. Associate the DNS integration with a Cloud or Network Domain
#. Configure naming policies that include DNS domain suffixes
#. During provisioning, |morpheus| automatically:

   - Creates A/AAAA records for the provisioned Instance
   - Creates PTR records if reverse zones are configured
   - Applies hostname based on naming policies

#. During Instance teardown, DNS records are automatically removed

Managing Records
----------------

DNS records managed through plugin providers are accessible in the standard Domains interface:

#. Navigate to Infrastructure > Network > Domains
#. Select the domain associated with the plugin DNS provider
#. View, add, edit, or delete records as with any DNS integration

Supported record types depend on the specific plugin implementation. Common types include:

- **A:** IPv4 address records
- **AAAA:** IPv6 address records
- **CNAME:** Canonical name aliases
- **TXT:** Text records
- **MX:** Mail exchange records
- **PTR:** Pointer (reverse DNS) records
- **SRV:** Service locator records

Developing DNS Plugins
-----------------------

DNS plugins are developed using the |morpheus| Plugin API. A DNS plugin must:

#. Extend the appropriate base class (``DnsProvider``)
#. Implement zone listing and record management methods
#. Package as a JAR file with a plugin descriptor
#. Register provider types and option types for configuration

For plugin development details, refer to the `Morpheus Plugin Developer Guide <https://developer.morpheusdata.com>`_.

Example plugin structure:

.. code-block:: groovy

  class MyDnsProvider extends DnsProvider {
      // Zone operations
      ServiceResponse listZones(Map opts)
      ServiceResponse createZone(Map zoneConfig)
      ServiceResponse deleteZone(Map zoneConfig)

      // Record operations
      ServiceResponse listRecords(String zone, Map opts)
      ServiceResponse createRecord(String zone, Map recordConfig)
      ServiceResponse updateRecord(String zone, Map recordConfig)
      ServiceResponse deleteRecord(String zone, Map recordConfig)
  }

Troubleshooting
---------------

**Plugin not appearing in provider list:**

- Verify the plugin JAR is uploaded in Administration > Integrations > Plugins
- Check the plugin status shows as "Active"
- Review |morpheus| application logs for plugin loading errors

**DNS records not creating during provisioning:**

- Confirm the DNS integration is associated with the Cloud or Network Domain
- Verify naming policies include the correct DNS domain
- Check the plugin integration status (green = connected)
- Review activity logs for API errors from the plugin

**Zone synchronization issues:**

- Click :guilabel:`REFRESH` on the DNS integration to force re-sync
- Verify API credentials and connectivity to the DNS service
- Check for permission issues on the external DNS service
