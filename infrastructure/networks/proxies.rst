Proxies
-------
.. //temp

Overview
^^^^^^^^

In many situations , companies deploy virtual machines in proxy restricted environments for things such as PCI Compliance, or just general security. As a result of this |morpheus| provides out of the box support for proxy connectivity. Proxy authentication support is also provided with both Basic Authentication capabilities as well as NTLM for Windows Proxy environments. |morpheus| is even able to configure virtual machines it provisions to utilize these proxies by setting up the operating systems proxy settings directly (restricted to cloud-init based Linux platforms for now, but can also be done on windows based platforms in a different manner).

To get started with Proxies, it may first be important to configure the |morpheus| appliance itself to have access to proxy communication for downloading service catalog images. To configure this, visit the Admin > Settings page where a section labeled "Proxy Settings" is located. Fill in the relevant connection info needed to utilize the proxy. It may also be advised to ensure that the Linux environment's `http_proxy`, `https_proxy`, and `no_proxy` are set appropriately.

Defining Proxies
^^^^^^^^^^^^^^^^

Proxies can be used in a few different contexts and optionally scoped to specific networks with which one may be provisioning into or on a cloud integration as a whole. To configure a Proxy for use by the provisioning engines within |morpheus| we must go to `Infrastructure > Networks > Proxies`. Here we can create records representing connection information for various proxies. This includes the host ip address, proxy port, and any credentials (if necessary) needed to utilize the proxy. Now that these proxies are defined we can use them in various contexts.

Cloud Communication
^^^^^^^^^^^^^^^^^^^

When morpheus needs to connect to various cloud APIs to issue provisioning commands or to sync in existing environments, we need to ensure that those api endpoints are accessible by the appliance. In some cases the appliance may be behind a proxy when it comes to public cloud access like Azure and AWS. To configure the cloud integration to utilize a proxy, when adding or editing a cloud there is a setting called "API Proxy" under "Advanced Options". This is where the proxy of choice can be selected to instruct the Provisioning engine how to communicate with the public cloud. Simply adjust this setting and the cloud should start being able to receive/issue instructions.

Provisioning with Proxies
^^^^^^^^^^^^^^^^^^^^^^^^^

Proxy configurations can vary from operating system to operating system and in some cases it is necessary for these to be configured in the blueprint as a prerequisite. In other cases it can also be configured automatically. Mostly with the use of cloud-init (which all of our out of the box service catalog utilizes on all clouds). When editing/creating a cloud there is a setting for "Provisioning Proxy" in "Provisioning Options". If this proxy is set, |morpheus| will automatically apply these proxy settings to the guest operating system.

Overriding proxy settings can also be done on the Network record. Networks (or subnets) can be configured in `Infrastructure > Networks` or on the Networks tab of the relevant Cloud detail page. Here, a proxy can also be assigned as well as additional options like the `No Proxy` rules for proxy exceptions.

Docker
^^^^^^

When provisioning Docker based hosts within a Proxy environment it is up to the user to configure the docker hosts proxy configuration manually. There are workflows that can be configured via the Automation engine to make this automatic when creating docker based hosts. Please see documentation on Docker and proxies for specific information.

Proxy setups can vary widely from company to company, and it may be advised to contact support for help configuring morpheus to work in the proxy environment.
