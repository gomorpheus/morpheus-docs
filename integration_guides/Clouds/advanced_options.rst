**Advanced Options**

DOMAIN
  Specify a default domain for instances provisioned to this Cloud.
SCALE PRIORITY
  Only affects Docker Provisioning. Specifies the priority with which an instance will scale into the cloud. A lower priority number means this cloud integration will take scale precedence over other cloud integrations in the group.
APPLIANCE URL
  Alternate Appliance url for scenarios when the default Appliance URL (configured in `admin > settings`) is not reachable or resolvable for Instances provisioned in this cloud. The Appliance URL is used for Agent install and reporting.
TIME ZONE
  Configures the time zone on provisioned VM's if necessary.
DATACENTER ID
  Used for differentiating pricing among multiple datacenters. Leave blank unless prices are properly configured.
NETWORK MODE
  Unmanaged or select a Network Integration (NSX, ACI etc)
LOCAL FIREWALL
  On or Off. Enable to managed Host and VM firewall/IP Table rules (linux only)
SECURITY SERVER
  Security Server setting is for Security Service Integrations such as ACI
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
  Enable for |morpheus| to sync Costing data from the Cloud provider, when available. For on-prem Clouds, enabling costing activates a costing service designed to mirror the live costing experience of public clouds, including invoicing with line items and real-time cost data (Operations > Costing > Invoices). If your organization utilizes reserved instances and you want to pull in related pricing data, select `Costing and Reservations`. If this is not relevant, select `Costing` to save money on additional calls to the AWS Cost Explorer API or similar service for other clouds.
DNS INTEGRATION
  Records for instances provisioned in this cloud will be added to selected DNS integration.
SERVICE REGISTRY
  Services for instances provisioned in this cloud will be added to selected Service Registry integration.
CONFIG MANAGEMENT
  Select a Chef, Salt, Ansible or Puppet integration to be used with this Cloud.
CMDB
  Select CMDB Integration to automatically update selected CMDB.
CMDB DISCOVERY
  When checked, any automatically discovered (unmanaged) servers onboarded into |morpheus| from this Cloud will also have CMDB records created for them.
CHANGE MANAGEMENT
  Select an existing Change Management Integration to set on the Cloud. ex: Cherwell
AGENT INSTALL MODE
  * SSH / WINRM: |morpheus| will use SSH or WINRM for Agent install.
  * Cloud Init / Unattend (when available): (DEFAULT) |morpheus| will utilize Cloud-Init or Cloudbase-Init for agent install when provisioning images with Cloud-Init/Cloudbase-Init installed. |morpheus| will fall back on SSH or WINRM if cloud-init is not installed on the provisioned image. Morpheus will also add Agent installation to Windows unattend.xml data when performing Guest Customizations or utilizing syspreped images.
API PROXY
  Set a proxy for outbound communication from the |morpheus| Appliance to the Cloud endpoints. Proxies can be added in the `Infrastructure > Networks > Proxies` tab.
INSTALL AGENT
  Enable to have Agent Installation on by default for all provisioning into this Cloud. Disable for Agent Installation to be off by default for all provisioning into this Cloud.

**Provisioning Options**

PROXY
  Set a proxy for inbound communication from Instances to the |morpheus| Appliance. Proxies can be added in the `Infrastructure > Networks > Proxies` tab.
Bypass Proxy for Appliance URL
  Enable to bypass proxy settings (if added) for |morpheus| Agent communication to the Appliance URL.
NO PROXY
  Include a list of IP addresses or name servers to exclude from proxy traversal
USER DATA (LINUX)
  Add cloud-init user data. |morpheus| 4.1.0 and earlier assumes bash syntax. |morpheus| 4.1.1 and later supports all User Data formats. Refer to https://cloudinit.readthedocs.io/en/latest/topics/format.html for more information.
