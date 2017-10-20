Advanced Options
----------------

DOMAIN
  Specify a default domain for instances provisioned to this Cloud.
SCALE PRIORITY
  Specifies the priority with which an instance will scale into the cloud. A lower priority number means this cloud integration will take scale precedence over other cloud integrations in the group.
APPLIANCE URL
  Alternate Appliance url for scenarios when the default Appliance URL (configured in `admin -> settings`) is not reachable or resolvable for Instances provisioned in this cloud. The Appliance URL is used for Agent install and reporting.
TIME ZONE
  Configures the time zone on provisioned VM's if necessary.
DATACENTER ID
  Used for differentiating pricing among multiple datacenters. Leave blank unless prices are properly configured.
DNS INTEGRATION
  Records for instances provisioned in this cloud will be added to selected DNS integration.
SERVICE REGISTRY
  Services for instances provisioned in this cloud will be added to selected Service Registry integration.
CONFIG MANAGEMENT
  Select a Chef, Salt, Ansible or Puppet integration to be used with this Cloud.
AGENT INSTALL MODE
  * SSH / WINRM: |morpheus| will use SSH or WINRM for Agent install.
  * Cloud-Init (when available): |morpheus| will utilize Cloud-Init or Cloudbase-Init for agent install when provisioning images with Cloud-Init/Cloudbase-Init installed. |morpheus| will fall back on SSH or WINRM if cloud-init is not installed on the provisioned image.

API PROXY
  Required when a Proxy Server blocks communication between the |morpheus| Appliance and the Cloud. Proxies can be added in the `Infrastructure -> Networks -> Proxies` tab.

Provisioning Options
--------------------

API PROXY
  Required when a Proxy Server blocks communication between an Instance and the |morpheus| Appliance. Proxies can be added in the `Infrastructure -> Networks -> Proxies` tab.
Bypass Proxy for Appliance URL
  Enable to bypass proxy settings (if added) for Instance Agent communication to the Appliance URL.
USER DATA (LINUX)
  Add cloud-init user data using bash syntax.
