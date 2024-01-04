Microsoft DNS
-------------

Overview
^^^^^^^^

|morpheus| integrates directly with  Microsoft DNS to automatically create DNS entries for Instances provisioned to a configured Cloud or Group. |morpheus| also syncs in Microsoft DNS Domains for easy selection while provisioning, or setting as the default Domain on a Cloud or Network.

Prepare DNS Server(s)
^^^^^^^^^^^^^^^^^^^^^

.. note:: 
    This section will assume a the DNS server is in an Active Directory environment and joined to the domain.  The process may be different for other configurations.

The easiest method to prepare DNS server(s) is to use a service account that is added to the ``DnsAdmins`` and ``Remote Management Users`` groups, either in Active Directory (if DNS is on domain contollers) or the local groups of a member server. 
The ``DnsAdmins`` group will provide permissions for the service account to make DNS changes, such as creating/deleting A and PTR records.  The ``Remote Management Users`` group will allow |morpheus| to connect to the server(s) via WinRM.

Additionally, ensure firewall rules have been updated if needed to allow WinRM through.  In some cases, the default WinRM rules allow ``Private`` and ``Domain`` networks but not ``Public``.  Enable ``Public`` if the network |morpheus| is 
connected is considered ``Public``, or disable the firewall if permitted.  If a jump box is required (discussed below), then ensure the firewall is configured to allow the jump box to connect to the DNS server instead.

Minimum Permissions
```````````````````

Some organizations may require that users cannot be added to the ``DNSAdmin`` group, mentioned previously.  If this is a requirement, the following process/permissions would be required to ensure |morpheus| can connect successfully.  
This process may be required on each DNS server, depending on the environment.  Note if |morpheus| adds additional functionality at a later time, these permissoins may need to be updated to support those features.

  * Run ``dnsmgmt.msc``
  * Right-click the DNS server object and choose ``Properties``
  * Add the service account to the user list and ensure the following permissions are applied:
    * Read
    * Create all child objects
    * Delete all child objects
  * Run ``wmimgmt.msc``
  * Right-click ``WMI Control (Local)`` and choose ``Properties``
  * Click the ``Security`` tab
  * Set the following permissions for each of the below nodes:
    * ``CIMV2``
    * ``MicrosoftDNS``
    * ``Microsoft => Windows => DNS`` (only the DNS node)
  * Hightlight the node and click the ``Security`` button
  * Click the ``Advanced`` button
  * Click the ``Add`` button to add the service account to the list
  * Ensure the ``Applies to`` field is set to ``This namespace and subnamespaces``
  * Set the following permissions:
    * Enable Account
    * Remote Enable
    * Execute Methods
  * Finally, restart Windows Management Instrumentation Service or the server. This is required for the change in permissions to take place.

Additional support reference:  `https://support.morpheusdata.com/s/article/How-to-give-C?language=en_US <https://support.morpheusdata.com/s/article/How-to-give-C?language=en_US>`_

(Optional) Prepare Jump Box
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In some environments, |morpheus| may not be allowed to access the DNS servers directly, as they may be on segregated networks.  In this case, |morpheus| can utilize a member server as a "jump box" that can access the DNS servers directly, the jump box 
will be used to interact with the DNS server instead.  If this is a requirement, follow the below process to prepare the jump box.

  * Add the service account to the ``Remote Management Users`` group of the jump box, which will allow WinRM to access
  * Verify the firewall allows WinRM from |morpheus|
  * Create or edit the following registry key:
    * Navigate to:

      ``HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\Protect\Providers\df9d8cd0-1501-11d1-8c7a-00c04fc297eb``
    
    * Create or edit ``ProtectionPolicy`` DWORD (32-bit) Value
    * Set ``ProtectionPolicy`` value to ``1``

Add Microsoft DNS Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. IMPORTANT:: The |morpheus| Microsoft DNS integration works over http/5985.  If you have turned off the http listener on 5985 and only enabled https/5986 it will fail.

.. note::
    Depending on the version of |morpheus|, some settings may only be available by installing the Microsoft DNS plugin from `https://share.morpheusdata.com/msdns-plugin/about <https://share.morpheusdata.com/msdns-plugin/about>`_.  Newer versions of Morpheus should contain this plugin by default.

Microsoft DNS can be added in the ``Administration`` or ``Infrastructure`` sections:

#. In |AdmInt|, select :guilabel:`+ New Integration`
#. In ``Infrastructure > Networks > Integrations``, select :guilabel:`+ Add`
#. Provide the following:

   TYPE
    Microsoft DNS
   NAME
    Name for the Integration in |morpheus|
   WINRM PORT
    Port WinRM should use.  By default, HTTP (port 5985) is used, which is the default on Windows Server.  If HTTPS has been configured by the organization, then specifying port 5986 may be appropriate.
   DNS SERVER
    IP or resolvable hostname of DNS server ``morpheus`` will connect to. If using a jump box, specify the IP or resolvable hostname of the jump box here, and the main DNS Server in the COMPUTER NAME field below.
   USERNAME
    DNS provider username
   PASSWORD
    DNS provider user password
   ZONE FILTER
    Comma separated filter for specific zones to be imported.  Example entries: ``example.morpheus.com, *.morpheus.com, *.10.in-addr.arpa, d*.us.morpheus.com``.  Additional explanations can be found at `https://github.com/gomorpheus/morpheus-msdns-plugin?tab=readme-ov-file#configuring <https://github.com/gomorpheus/morpheus-msdns-plugin?tab=readme-ov-file#configuring>`_
   COMPUTER NAME
    If the DNS SERVER specified is not the main DNS server but rather a jump box, enter the Computer Name of the main DNS Server here. If the DNS SERVER specified above is the main DNS server and not a jump box, leave COMPUTER NAME blank.
   CREATE POINTERS
    Enable to create PTR (Pointer/Reverse Lookup) records during provisioning

#. Once saved the Integration will be added and visible in both |AdmInt| and ``Infrastructure > Networks > Services``

.. NOTE:: All fields can be edited after saving.

Domains
^^^^^^^

Once the integration is added, Microsoft DNS Domains will sync and listed under ``Infrastructure > Networks > Domains``.

.. NOTE:: Default Domains can be set on Networks and Clouds, and can be selected when provisioning. Additional configuration options are available by editing a domain in `Networks > Domains`

Configuring Microsoft DNS with Clouds and Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DNS Integrations are available in the `DNS Integration` dropdown in Cloud and Group settings. |morpheus| will register Instances with the DNS provider when provisioned into a Cloud or Group with a DNS Integration added.

To take full advantage of the |morpheus| Microsoft DNS integration, a service account in the Admins group is not required. However, an account must have the following minimum access to use all features:

- Read, Create, and Delete rights on objects
- Belongs to the local group ``WinRMRemoteWMIUsers__``
- WinRM Quickconfig must be run on the DNS server
- CIMv2 needs access according to instructions in our `KnowledgeBase <https://support.morpheusdata.com/s/article/How-to-give-C?language=en_US>`_

Add DNS Integration to a Cloud
``````````````````````````````

#. In ``Infrastructure > Clouds`` edit the target Cloud.
#. Expand the ``Advanced Options`` section.
#. In the ``DNS Integration`` dropdown, select an available DNS Integration.
#. Save Changes

Add DNS Integration to a Group
``````````````````````````````

#. In ``Infrastructure > Groups`` select the target Group.
#. Select the ``Edit`` button for the Group
#. Expand the ``Advanced Options`` section.
#. In the ``DNS Integration`` dropdown, select an available DNS Integration.
#. Save Changes

.. NOTE:: Instances provisioned into a Cloud or Group with a DNS Integration added will be registered as instancename.domain with the DNS Provider during provisioning, and de-registered at teardown.
