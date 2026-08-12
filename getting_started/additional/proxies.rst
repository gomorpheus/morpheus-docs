Proxies
-------

Overview
^^^^^^^^

In many situations,companies deploy virtual machines in proxy restricted environments for things such as PCI Compliance, or just general security. As a result of this |morpheus| provides out of the box support for proxy connectivity. Proxy authentication support is also provided with both Basic Authentication capabilities as well as NTLM for Windows Proxy environments. |morpheus| is even able to configure virtual machines it provisions to utilize these proxies by setting up the operating systems proxy settings directly (restricted to cloud-init based Linux platforms for now, but can also be done on windows based platforms in a different manner).

To get started with Proxies, it may first be important to configure the |morpheus| appliance itself to have access to proxy communication for downloading service catalog images. To configure this, visit the |AdmSet| page where a section labeled "Proxy Settings" is located. Fill in the relevant connection info needed to utilize the proxy. It may also be advised to ensure that the Linux environment's ``http_proxy``, ``https_proxy``, and ``no_proxy`` are set appropriately.

For optional Central Service or Remote Data Access connectivity, use the canonical endpoint requirement in :doc:`/getting_started/requirements/requirements`. Do not copy proposed tunnel hostnames into proxy rules unless HPE has supplied the current endpoint registry for the enabled service and release.

Defining Proxies
^^^^^^^^^^^^^^^^
Proxies can be used in a few different contexts and optionally scoped to specific networks with which one may be provisioning into or on a cloud integration as a whole. To configure a Proxy for use by the provisioning engines within |morpheus| we must go to ``Infrastructure > Networks > Proxies``. Here we can create records representing connection information for various proxies. This includes the host ip address, proxy port, and any credentials (if necessary) needed to utilize the proxy. Now that these proxies are defined we can use them in various contexts.

Cloud Communication
^^^^^^^^^^^^^^^^^^^

When |morpheus| needs to connect to cloud APIs to issue provisioning commands or sync existing environments, those API endpoints must be accessible by the appliance. In some cases, the appliance may be behind a proxy for public Cloud access such as Azure or AWS. After defining a Proxy, add or edit a compatible Cloud and select it under ``Connection Options > API Proxy``. The Connection Options section appears when at least one Proxy or Distributed Worker is available to the Tenant. The API Proxy controls communication between |morpheus| and the Cloud API; it does not configure proxy settings inside provisioned workloads.

Provisioning with Proxies
^^^^^^^^^^^^^^^^^^^^^^^^^

Proxy configurations can vary from operating system to operating system and in some cases it is necessary for these to be configured in the blueprints as a prerequisite. In other cases it can also be configured automatically. Mostly with the use of cloud-init (which all of our out of the box service catalog utilizes on all clouds). When editing/creating a cloud there is a setting for "Provisioning Proxy" in "Provisioning Options". If this proxy is set, |morpheus| will automatically apply these proxy settings to the guest operating system.

Overriding proxy settings can also be done on the Network record. Networks (or subnets) can be configured in ``Infrastructure > Networks`` or on the Networks tab of the relevant Cloud detail page. Here, a proxy can also be assigned as well as additional options like the ``No Proxy`` rules for proxy exceptions.

Docker
^^^^^^

When provisioning Docker based hosts within a Proxy environment it is up to the user to configure the docker host proxy configuration manually. There are workflows that can be configured via the Automation engine to make this automatic when creating docker based hosts. Please see documentation on Docker and proxies for specific information.

Proxy setups can vary widely from company to company, and it may be advised to contact support for help configuring morpheus to work in the proxy environment.
