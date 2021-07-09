|morphver| Highlights
=====================

Terraform Instance Types
------------------------

- Combine Terraform Spec Templates into Layouts and Instance Types
- Easily provision new infrastructure into your existing Clouds based on Terraform Instance Types
- Monitor Terraform Instances for state drift
- Make or sync changes to Terraform spec, then apply new state to existing Terraform Instances
- Get started with our `Terraform Instance Type guide <https://docs.morpheusdata.com/en/5.3.1/getting_started/guides/terraform_instances.html>`_

.. image:: /images/integration_guides/terr_inst_guide/12historyTab.png

Deepened Google Cloud Platform (GCP) Integration
------------------------------------------------

- Scope Google Clouds to all regions or one selected region
- Create and manage GCP Projects
- Create and manage networks and subnets
- Create and manage routers and firewalls
- Take a look at our `GCP integration guide <https://docs.morpheusdata.com/en/5.3.1/integration_guides/Clouds/google/google.html>`_ for more details

|morpheus| VDI Gateways and Jump Hosts
--------------------------------------

- Configure Jump Hosts for |morpheus| to tunnel through when connecting to VDI guest console sessions
- Link a VDI Gateway to your |morpheus| appliance
- VDI sessions connect directly to the gateway rather than to the |morpheus| appliance directly when a VDI Gateway is configured for the VDI pool

Resources UI
------------

- The |morpheus| resources UI offers new visibility into non-VM and non-container object types
- Accessed through Infrastructure > Compute (which replaces Infrastructure > Hosts)
- In addition to VMs, hypervisors and bare metal hosts, containers associated with |morpheus| Instances and IaC resources are also surfaced

Two-factor Authentication
-------------------------

- Enable `two-factor authentication <https://docs.morpheusdata.com/en/5.2.5/administration/user_settings/user_settings.html#factor-authentication>`_ on a per-user basis
- Once enabled, users will use their two factor auth app of choice (such as Google Authenticator) to obtain the access code
- Compatible with local |morpheus| accounts as well as Active Directory and LDAP-sourced accounts

.. image:: /images/releases/531/2fa_new.gif
