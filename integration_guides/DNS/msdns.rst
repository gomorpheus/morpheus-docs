Microsoft DNS
-------------

The |morpheus| Microsoft DNS integration is developed as an official plugin separate from the core product. It is easily added and uploaded to any |morpheus| appliance. Download the plugin from the `official plugin repository <share.morpheusdata.com>_` and add it to the appliance from the plugin management UI section (|AdmIntPlu|).

The MSDSN integration automates DNS record creation and DNS record cleanup both manually or automatically during workload provisioning to a configured Cloud or Group. It should be noted that this integration is typically not needed when joining a Windows VM to an Active Directory Domain as typically this automatically creates a DNS record.

Prepare DNS Server(s)
^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: This section will assume a the DNS server is in an Active Directory environment and joined to the domain.  The process may be different for other configurations.

The easiest method to prepare DNS server(s) is to use a service account that is added to the ``DnsAdmins`` and ``Remote Management Users`` groups, either in Active Directory (if DNS is on domain controllers) or the local groups of a member server. The ``DnsAdmins`` group will provide permissions for the service account to make DNS changes, such as creating/deleting A and PTR records.  The ``Remote Management Users`` group will allow |morpheus| to connect to the server(s) via WinRM.

Additionally, ensure firewall rules have been updated if needed to allow WinRM through.  In some cases, the default WinRM rules allow ``Private`` and ``Domain`` networks but not ``Public``.  Enable ``Public`` if the network |morpheus| is
connected is considered ``Public``, or disable the firewall if permitted.  If a jump box is required (discussed below), then ensure the firewall is configured to allow the jump box to connect to the DNS server instead.

Finally, ``winrm quickconfig`` may need to be run to enable WinRM, if the server is an older operating system.

Minimum Permissions
```````````````````

Some organizations may require that users cannot be added to the ``DNSAdmin`` group, mentioned previously.  If this is a requirement, the following process/permissions would be required to ensure |morpheus| can connect successfully.
This process may be required on each DNS server, depending on the environment.  Note that if |morpheus| adds additional functionality at a later time, these permissions may need to be updated to support those features.

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

In some environments, |morpheus| may not be allowed to access the DNS servers directly, as they may be on segregated networks.  In this case, |morpheus| can utilize a member server as a "jump box" that can access the DNS servers directly, the jump box will be used to interact with the DNS server instead.  If this is a requirement, follow the below process to prepare the jump box.

  * Add the service account to the ``Remote Management Users`` group of the jump box, which will allow WinRM to access
  * Verify the firewall allows WinRM from |morpheus|
  * Create or edit the following registry key by running ``regedit``:

    * Navigate to: ``HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\Protect\Providers\df9d8cd0-1501-11d1-8c7a-00c04fc297eb``
    * Create or edit ``ProtectionPolicy`` DWORD (32-bit) Value
    * Set ``ProtectionPolicy`` value to ``1``

  * Finally, ``winrm quickconfig`` may need to be run to enable WinRM, if the server is an older operating system.

Adding a Microsoft DNS integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For appliances with the MSDNS plugin installed, the option to create an integration is available. Navigate to |AdmInt| and click :guilabel:`+ NEW INTEGRATION` to create a new one.

- **NAME:** A friendly name for the integration in |morpheus|
- **RPC SERVER** Enter the name of the server brokering access to the Microsoft DNS Services. This is the Windows server |morpheus| will connect to directly. In most cases, the RPC SERVER will be a Windows domain-joined server with the DNS Server tools installed. |morpheus| will use this server to connect and manage DNS
- **RPC PORT:** This configuration is visible if "USE AGENT FOR RPC" is unmarked. The WinRM port number 5985/5986, default is 5985
- **USE AGENT FOR RPC:** Select this option to have the plugin use a configured agent to handle the |morpheus| to Windows RPC connection. The RPC SERVER should be an Instance (in other words, a managed VM) which is part of the same |morpheus| environment where the integration is added. The |morpheus| Agent must also be configured to logon as the DNS Service user account. In most cases, customers would only use this option when using an intermediate server to access DNS services
- **CREDENTIALS:** Provide account credentials for a service account. You may use credentials already stored in |morpheus| or create new Username/Password credentials
- **DNS SERVER:** If the RPC SERVER is not the server hosting DNS Services, then add the FQDN name of the DNS server here. Leave blank if the RPC SERVER is also the DNS Server
- **ZONE FILTER:** The ZONE FILTER is a comma separated list of glob-style filters which can be used to specify the zones that |morpheus| will import and sync. Glob style filters apply to the zone name only and at a domain level. The ``\*`` character matches any legal DNS character [a-zA-Z0-9_-] 0 or more times. Wildcarding stops at the . (period), leave blank to import all forward and reverse zones
- **SERVICE TYPE:** This configuration is visible if the DNS SERVER is not blank. This option informs the plugin how the RPC SERVER should contact the DNS SERVER. There are 3 supported options: **local** when the RPC SERVER is the DNS Server (ie when DNS SERVER is blank in which case local is the default and only option), **wmi** which is used when the RPC SERVER contacts the DNS Server over WMI (Windows RPC, this is the recommended and default option when using an intermediate RPC SERVER), and **winrm** which is used when the RPC SERVER connects to DNS SERVER over a WinRM session (this is not often used due to WinRM restrictions on domain controllers)
- **INVENTORY EXISTING:** Have the integration import and sync all DNS records for the matching Zones. Using this option is not recommended for installations with large namespaces
- **CREATE POINTERS:** Have DNS create a PTR record when the forward record is created

.. NOTE:: If you're not using an intermediate server, the RPC SERVER will also be the DNS Server. The |morpheus| Windows Agent should be set to log in using these credentials.

Domains
^^^^^^^

Once the integration is added, Microsoft DNS Domains will sync and listed under |InfNetDom|.

.. NOTE:: Default Domains can be set on Networks and Clouds, and can be selected when provisioning. Additional configuration options are available by editing a domain in |InfNetDom|

Configuring Microsoft DNS with Clouds and Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DNS Integrations are available in the ``DNS Integration`` dropdown in Cloud and Group settings. |morpheus| will register Instances with the DNS provider when provisioned into a Cloud or Group with a DNS Integration added.

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

Using Zone Filters
^^^^^^^^^^^^^^^^^^

In this example a ZONE FILTER string of

``*.morpheus.com, *.10.in-addr.arpa, d*.us.morpheus.com``

would

**IMPORT** ``test.morpheus.com, prod.morpheus.com`` but **NOT** ``mydomain.test.morpheus.com`` which has a 4th level

**IMPORT** ``32.10.in-addr.arpa, 33.10.in-addr.arpa`` but **NOT** ``12.11.in-addr.arpa`` or ``10.in-addr.arpa`` (which has 3 levels)

**IMPORT** ``denver.us.morpheus.com`` and ``delaware.us.morpheus.com`` but **NOT** ``ohio.us.morpheus.com`` (wildcard at 4th level)

Improved Integration Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recent versions of this integration have improved the error handling and validation. RPC connectivity and access to DNS Services is tested at the time the integration dialog is saved. The dialog will not save unless validation is passed successfully. The integration dialog will hint where problems occur but you should check the |morpheus| Health logs (|AdmHeaMorLog|) to see detailed messages.

.. TIP:: To force the integration to save you can uncheck the ENABLED checkbox. Doing this disables the validation testing allowing you to save the integration dialog contents and perform troubleshooting without having to reenter configurations. When the issue is resolved, edit the integration and set the integration to ENABLED. Validation will then be performed on the save.

Custom Powershell Module Script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recent versions of this integration include a custom Powershell Module script (.ps1 file) which is maintained by the plugin and transferred to the RPC SERVER when the integration is added. The Powershell script file contains functions designed to handle the interface between Morpheus and DNS. The script uses the standard Windows DNS-Server module (Windows feature RSAT-DNS-Server). The script file is MD5 checked each time the integration syncs and the module is refreshed from the plugin if the checksum fails. The custom script is stored in the **%LOCALAPPDATA%** folder for the integration service account user.

The module contains custom functions designed to interface with the MSDNS plugin via JSON.

- Having the Powershell module installed on the RPC SERVER offers some performance benefits as |morpheus| now can call on the modules functions to perform tasks
- The Powershell functions test RPC connectivity and DNS service connectivity on each sync refresh ensuring the integration is healthy
- The module uses a standard JSON interface between Windows RPC SERVER and |morpheus|
- The module overcomes restrictions imposed on |morpheus| WinRM connections authenticating with NTLM

.. IMPORTANT:: For version 2.1.3, the script file is named ``%LOCALAPPDATA%\morpheusDnsPluginHelper_v32.ps1`` and for version 2.3.3, the script file is named ``%LOCALAPPDATA%\morpheusDnsPluginHelper_v34.ps1``. The |morpheus| health logs will log the status of the |morpheus| Powershell file on each refresh. For example: ``INFO  c.m.m.MicrosoftDnsPluginHelper - testHelperFileScript - Checking for valid Helper script fileName: morpheusDnsPluginHelper_v32.ps1 - MD5: 698d8e6ad0bf7f64d9e9ccac962e4ab1``

Secure credential cache file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The |morpheus| Powershell functions use a technique where script blocks are executed with Invoke-Command passing a credential object. This effectively creates a new session from RPC SERVER using kerberos overcoming the restrictions imposed by Windows on the original Morpheus NTLM connection. Credentials are cached using the Windows Data Protection API meaning only the user account who created the credential can decrypt it and only on the original Windows server. The credential cache is stored in ``%LOCALAPPDATA%\S-1-5-21-nnnnnnnnnn-nnnnnnnnnn-nnnnnnnnnn-nnnn-dnsPlugin.ss`` where ``S-1-5-21-nnnnnnnnnn-nnnnnnnnnn-nnnnnnnnnn-nnnn-dnsPlugin.ss`` is the Service Account SID.

.. NOTE:: If "USE AGENT FOR RPC" is checked, there is no need to create a new session since the original session is already Kerberos, however the credentials are still cached.

Troubleshooting Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Service Account Requirements**

The service account used to access DNS via the plugin must meet the following requirements:

- If using an intermediate server as the RPC SERVER, the service account should be a member of local ``administrators`` group on the RPC SERVER
- If "USE AGENT FOR RPC" is checked, the |morpheus| Windows Agent service must be configured to login as the service account. The service account will require ``Log on as a Service`` rights in the RPC SERVER local policy
- If not using an intermediate server, the service account must be a member of ``Remote Management Users`` on the RPC SERVER as a minimum in order to access the RPC SERVER from |morpheus| via WinRM. Membership of ``administrators`` however, is recommended
- The service account must be a member of the domain global group ``DNS Admins``
- To Access Microsoft DNS WMI namespaces, the service account must be granted access to the DNS WMI classes

**RPC SERVER requirements**

When using an intermediate server as the RPC SERVER, the following requirements must be met:

- The RPC SERVER must be a Windows Server which is a member of a domain or forest which is trusted to access the DNS namespace
- The RPC SERVER must have the Microsoft Windows feature RSAT-DNS-Server installed
- If planning to "USE AGENT FOR RPC" then the Windows server must have a |morpheus| Windows Agent installed and this agent must report into the |morpheus| environment where the DNS Integration is being added or configured. Ideally, |morpheus| will have deployed the RPC SERVER as an Instance
- If not planning to "USE AGENT FOR RPC" then the RPC server must have WinRM configured and must be reachable over WinRM from the |morpheus| appliance
- When using an intermediate server to access DNS Services, the computer account of the RPC SERVER must be configured for delegation ``Trusted for Delegation to any service (Kerberos only)``. Use Active Directory Users and Computers, locate the computer account for RPC SERVER. Click properties and select the Delegation tab and choose the option ``Trust this computer for delegation to any service (Kerberos only)``

Using the plugin test Service page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recent versions of this integration have the ability to run a connection test via the |morpheus| appliance. Users must have full access to the Integrations permission to test a Microsoft DNS plugin connection. For example, to test connectivity to an integration with id value of 5, browse to the following URL in |morpheus|: ``https://my.morpheus.appliance/plugin/msdns/service?integrationId=5``

The plugin will run a series of tests using details from the integration dialog.

.. NOTE:: Tests can be run even if the integration ENABLED checkbox is unmarked allowing troubleshooting with the integration offline.

The results are output in the browser in JSON.

In the example below, inspect the ``serviceProfile``. Here, the ``rpcType`` is "agent" so "USE AGENT FOR RPC" is checked and the ``serviceType`` is "wmi". The ``rpcSession`` and ``serviceSession`` show the connection details, logon types and group membership for the RPC and service sessions. The ``dnsServer`` section shows the FQDN and version of the DNS server and if populated indicates a successful test (status = 0).

If the test is unsuccessful, a status code other than 0 is returned and any error will be listed in the "Errors" section

.. code-block:: JSON

  Morpheus Microsoft DNS Integration Service Profile
  Discovered service profile for Microsoft DNS integration : 5
  Rpc Connection Status true

  Successful rpc response from spie-mo-w-3011 via agent: Command completed successfully

  Errors

  {

  }

  Rpc Output

  {
      "status": 0,
      "cmdOut": {
          "serviceProfile": {
              "rpcHost": "SPIE-MO-W-3011",
              "rpcType": "agent",
              "serviceHost": "ip-c61302.myad.net",
              "serviceType": "wmi",
              "useCachedCredential": false
          },
          "dnsServer": {
              "computerName": "IP-C61302.myad.net",
              "version": "10.0.17763"
          },
          "rpcSession": {
              "userId": "myad\\spsvcdns",
              "computerName": "SPIE-MO-W-3011",
              "authenticationType": "Kerberos",
              "impersonation": "None",
              "isAdmin": true,
              "localProfile": "C:\\Users\\spsvcdns\\AppData\\Local",
              "tokenGroups": [
                  "myad\\Domain Users",
                  "Everyone",
                  "BUILTIN\\Users",
                  "BUILTIN\\Administrators",
                  "NT AUTHORITY\\SERVICE",
                  "CONSOLE LOGON",
                  "NT AUTHORITY\\Authenticated Users",
                  "NT AUTHORITY\\This Organization",
                  "LOCAL",
                  "Authentication authority asserted identity",
                  "myad\\AWS Delegated Domain Name System Administrators",
                  "myad\\AWS Delegated Server Administrators",
                  "myad\\AWS Delegated Add Workstations To Domain Users",
                  "myad\\DnsAdmins",
                  "myad\\AWS Delegated Kerberos Delegation Administrators"
              ],
              "isSystem": false,
              "isService": true,
              "isNetwork": false,
              "isBatch": false,
              "isInteractive": false,
              "isNtlmToken": false
          },
          "serviceSession": {
              "userId": "myad\\spsvcdns",
              "computerName": "SPIE-MO-W-3011",
              "authenticationType": "Kerberos",
              "impersonation": "None",
              "isAdmin": true,
              "localProfile": "C:\\Users\\spsvcdns\\AppData\\Local",
              "tokenGroups": [
                  "myad\\Domain Users",
                  "Everyone",
                  "BUILTIN\\Users",
                  "BUILTIN\\Administrators",
                  "NT AUTHORITY\\SERVICE",
                  "CONSOLE LOGON",
                  "NT AUTHORITY\\Authenticated Users",
                  "NT AUTHORITY\\This Organization",
                  "LOCAL",
                  "Authentication authority asserted identity",
                  "myad\\AWS Delegated Domain Name System Administrators",
                  "myad\\AWS Delegated Server Administrators",
                  "myad\\AWS Delegated Add Workstations To Domain Users",
                  "myad\\DnsAdmins",
                  "myad\\AWS Delegated Kerberos Delegation Administrators"
              ],
              "isSystem": false,
              "isService": true,
              "isNetwork": false,
              "isBatch": false,
              "isInteractive": false,
              "isNtlmToken": false
          },
          "domainSOAServers": {
              "nameToQuery": "ip-c61302.myad.net",
              "fqdn": "ip-c61302.myad.net",
              "dcList": [
                  {
                      "zone": "myad.net",
                      "dnsServer": "ip-c61301.myad.net"
                  },
                  {
                      "zone": "myad.net",
                      "dnsServer": "ip-c61302.myad.net"
                  }
              ]
          }
      },
      "errOut": null
  }

DNS Record validation and Error Handling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- DNS records are now fully validated before they are created. Only record types A, AAAA, CNAME and PTR are currently supported
- Adding a DNS Record which already exists (ie FQDN and IP address match an existing record in DNS) would normally return an error (code 9711), this is masked to a success to prevent |morpheus| aborting the provision
- Removing a |morpheus| DNS Record that does not exist in DNS (error 9714) is also masked to success to have |morpheus| delete its copy
- If a fwd record is created but the PTR record fails (due to missing PTR zone error 9715), this is also masked to success to prevent |morpheus| aborting the Provision
- All errors are logged to the |morpheus| health logs (|AdmHeaMorLog|).

AWS Directory Services Support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Support is included for AWS Active Directory service.

- Access is only possible via a correctly configured intermediate server (RPC SERVER) hosted in AWS and having the DNS Management Tools installed
- The DNS SERVER must be the fully qualified name of one of the AWS Domain controllers
- The Service Account should be a member of AWS Delegated Domain Name System Administrators, AWS Delegated Kerberos Delegation Administrators and AWS Delegated Server Administrators (for access to RPC SERVER)
- The RPC SERVER computer object should be trusted for delegation for all Kerberos Services on the AWS Directory Service domain controllers. This can be performed using AD Users and Computers to modify the properties of the RPC SERVER Computer object. Right click the computer object, select properties and open the Delegation tab. Select the Radio button ``Trust this computer for delegation to any service (Kerberos Only)``. Click OK to Save

.. NOTE:: It is possible to finely tune the delegation so that the RPC SERVER computer object can only delegate to specific services if this is required.
