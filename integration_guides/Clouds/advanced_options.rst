Advanced Options
^^^^^^^^^^^^^^^^

DOMAIN
  Specify a default domain for instances provisioned to this Cloud.
SCALE PRIORITY
  Only affects Docker Provisioning. Specifies the priority with which an instance will scale into the cloud. A lower priority number means this cloud integration will take scale precedence over other cloud integrations in the group.
APPLIANCE URL
  Alternate Appliance url for scenarios when the default Appliance URL (configured in `admin -> settings`) is not reachable or resolvable for Instances provisioned in this cloud. The Appliance URL is used for Agent install and reporting.
TIME ZONE
  Configures the time zone on provisioned VM's if necessary.
DATACENTER ID
  Used for differentiating pricing among multiple datacenters. Leave blank unless prices are properly configured.
NETWORK MODE
  Unmanaged or Managed
HOST FIREWALL
  On or Off. Enable to managed Host firewall/IP Table rules (linux only)
SECURITY MODE
  Defines if Morpheus will control local firewall of provisioned servers and hosts.

  .. IMPORTANT:: When local firewall management is enabled, Morpheus will automatically set an IP table rule to allow incoming connections on tcp port 22 from the Morpheus Appliance.
SECURITY SERVER
  Select security off or Local Firewall
TRUST PROVIDER
  Select Internal (Morpheus) or an existing Trust Provider Integration
STORAGE MODE
  Single Disk, LVM or Clustered
BACKUP PROVIDER
  Select Internal Backups (Morpheus) or a Backup Integration
REPLICATION PROVIDER
  Sets the default Replication Provider for the Cloud. Select an existing Replication Provider Integration
GUIDANCE
  Enable Guidance recommendations on cloud resources.
COSTING
  Enable for Morpheus to sync Costing data from the Cloud provider, when available.
DNS INTEGRATION
  Records for instances provisioned in this cloud will be added to selected DNS integration.
SERVICE REGISTRY
  Services for instances provisioned in this cloud will be added to selected Service Registry integration.
CONFIG MANAGEMENT
  Select a Chef, Salt, Ansible or Puppet integration to be used with this Cloud.
CMDB
  Select CMDB Integration to automatically update selected CMDB.
CHANGE MANAGEMENT
  Select an existing Change Management Integration to set on the Cloud. ex: Cherwell
AGENT INSTALL MODE
  * SSH / WINRM: |morpheus| will use SSH or WINRM for Agent install.
  * Cloud Init / Unattend (when available): |morpheus| will utilize Cloud-Init or Cloudbase-Init for agent install when provisioning images with Cloud-Init/Cloudbase-Init installed. |morpheus| will fall back on SSH or WINRM if cloud-init is not installed on the provisioned image. Morpheus will also add Agent installation to Windows unattend.xml data when performing Guest Customizaitons or utilizing syspreped images.
API PROXY
  Required when a Proxy Server blocks communication between the |morpheus| Appliance and the Cloud. Proxies can be added in the `Infrastructure -> Networks -> Proxies` tab.
INSTALL AGENT
  Enable to have Agent Installation on by default for all provisioning into this Cloud. Disable for Agent Installation to be off by default for all provisioning into this Cloud.

Provisioning Options
^^^^^^^^^^^^^^^^^^^^

PROXY
  Required when a Proxy Server blocks communication between an Instance and the |morpheus| Appliance. Proxies can be added in the `Infrastructure -> Networks -> Proxies` tab.
Bypass Proxy for Appliance URL
  Enable to bypass proxy settings (if added) for Instance Agent communication to the Appliance URL.
USER DATA (LINUX)
  Add cloud-init user data or scripts. Assumes bash syntax.
