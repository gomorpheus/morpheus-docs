Services
--------

Overview
^^^^^^^^

The Network Services section allows you to add and manage IPAM, DNS, and Service Registry integrations. These services can also be added in the `Administration -> Integrations` section.

The following integrations are currently supported:

IPAM
  * Infoblox
  * Bluecat (2.11)

DNS
  * Microsoft DNS
  * Power DNS
  * Route 53
  * Bind DNS

Service Registry
  * Consul

Add a Service
^^^^^^^^^^^^^

To configure any of the services, select `ADD SERVICE`, and fill out the required fields.

Infoblox
  * Name
  * URL (wapi url + version)

    - example `https://x.x.x.x/wapi/v2.2.1`

  * Username
  * Password

Bluecat
  * Name
  * URL
  * Username
  * Password

Microsoft DNS
  * Name
  * DNS Server
  * Username
  * Password
  * Zone

PowerDNS
  * Name
  * API Host
  * Token

BindDNS
  * Host
  * Username
  * Password
  * BindKey

Route 53
  * Region
  * Access Key
  * Secret Key

After Saving, your Network Service integrations will be available for use. These integrations must be scoped to the appropriate sections in |morpheus| :

Scoping Services
^^^^^^^^^^^^^^^^

IPAM
  IPAM integrations will populate pools in the IP Pool section, which are available for assignment to networks in the `NETWORK POOL` dropdown when configuring a network.
DNS
  DNS integrations will populate domains in the `Infrastructure -> Network -> Domains` section, and are available in the `DOMAIN` dropdown located under the `Advanced Options` section in Cloud, Group, and Network configurations, as well as in the `Configure` section of the Create Instance wizard.  DNS integrations are also available in the `DNS SERVICE` dropdown located under the `Advanced Options` section in Cloud and Group configurations.
Service Registry
  Service Registry integrations are available in the `SERVICE REGISTRY` dropdown located under the `Advanced Options` section in Cloud and Group configurations.
