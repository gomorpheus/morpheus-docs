Appliance Settings
^^^^^^^^^^^^^^^^^^

Appliance URL
  The default URL used for Agent install and Agent functionality. All Instances and Hosts must be able to resolve and reach this URL over 443 for successful agent install and communication.

.. NOTE:: Alternate Appliance URLs can be configured per Cloud in the `Edit Cloud > Advanced Options` section.

Internal Appliance URL (PXE)
  For PXE-Boot your appliance needs to be routable directly with minimal NAT masquerading. This allows one to override the default appliance url endpoint for use by the PXE Server. If this is unset, the default appliance url will be used instead.
API Allowed Origins
  A CORS-related field which specifies the origins that are allowed to access the |morpheus| API. For example, if you were designing a web application which needed to make AJAX calls to |morpheus| API. The origins should be specified here. By default, all origins are allowed. When this field is filled, an exclusive whitelist of allowed origins is established.
Cloud Sync Interval
  Data is refreshed through cloud integrations at the interval specified here in seconds, the default value is 300 seconds (five minutes). Appliances managing a very large number of clouds may be adversely affected by setting this value too low.
Usage Retainment
 Determines how many days to keep account usage (metered costing data) records. Retainment period is not set by default. Usage records will remain indefinitely if Usage Retainment is not set. Note this does not affect generated Invoice records.
Denied Hosts
  A comma-delimited list of IP addresses and/or hostnames which should not be allowed sources for HTTP Tasks or REST-populated Option Lists.
Approved Hosts
  A comma-delimited list of IP addresses and/or hostnames which are the only approved sources for HTTP Tasks or REST-populated Option Lists. By entering any values here, all others are automatically denied.
Enable SSL Verification of Agent (Communications)
  Enabling SSL Verification of Agent Communications requires a valid Certificate be installed on the Appliance.
Disable SSH Password Authentication
  Only allow ssh login using SSH keys. When true, SSH Password Authentication will not be enabled for VM's and Hosts provisioned after the setting is enabled.
Default Appliance Locale
  Sets the default language and region for all users on the |morpheus| appliance. Users with individual language preferences may also override this selection on their User Settings page
Default Console Gateway
  Select a configured |morpheus| Worker as a console gateway or VDI gateway. For more on installation and configuration of a gateway, see the `VDI Gateways section <https://docs.morpheusdata.com/en/latest/tools/vdi_pools.html#vdi-gateways>`_ of |morpheus| documentation.
