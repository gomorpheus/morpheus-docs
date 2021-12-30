Integrations
------------

Overview
^^^^^^^^

The Network Integrations section allows you to add and manage IPAM, DNS, and Service Registry integrations. These services can also be added in the |AdmInt| section.

The following integrations are currently supported:

Networking

* Cisco ACI
* VMWare NSX

IPAM

* Infoblox
* Bluecat
* phpIPAM

Security

* Cisco ACI

DNS

* Microsoft DNS
* PowerDNS
* Route 53


Scoping Services
^^^^^^^^^^^^^^^^
NETWORKING
  Networking integrations are available in the `NETWORK MODE` dropdown located under the `Advanced Options` section in Cloud configurations.
IPAM
  IPAM integrations will populate pools in the IP Pool section, which are available for assignment to networks in the `NETWORK POOL` dropdown when configuring a network.
SECURITY
  Security integrations are available in the `SECURITY SERVER` dropdown located under the `Advanced Options` section in Cloud configurations.
DNS
  DNS integrations will populate domains in the `Infrastructure > Network > Domains` section, and are available in the `DOMAIN` dropdown located under the `Advanced Options` section in Cloud, Group, and Network configurations, as well as in the `Configure` section of the Create Instance wizard.  DNS integrations are also available in the `DNS SERVICE` dropdown located under the `Advanced Options` section in Cloud and Group configurations.
Service Registry
  Service Registry integrations are available in the `SERVICE REGISTRY` dropdown located under the `Advanced Options` section in Cloud and Group configurations.

.. note:: Infoblox will also appear as a DNS INTEGRATION option in Clouds and Groups after adding Infoblox IPAM Integration.
