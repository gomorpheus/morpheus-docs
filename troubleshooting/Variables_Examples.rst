.. _Variables Examples:

Variables
=========

A vast number of variables are available for use in Tasks, Scripts, Templates, Resource Names, Cloud-Init User Data and Option List configs.

.. IMPORTANT:: Variables are case sensitive

Pre-Provision Vars
------------------

A subset of variables are available for Instance, Host Name and Hostnames. These can be passed inside ``${ }`` blocks during provisioning or in relevant policy configs. Groovy syntax can be resolved to allow for dynamic name generation as shown in some of the examples below.

Instance Naming Policy example: ``${userInitials}-${cloudCode}-${platform == 'windows' ? 'W' : 'L'}-${sequence}``

Available variables for Naming Policy naming patterns include:

.. code-block:: bash

  ${account}
  ${accountId}
  ${accountName}
  ${accountNumber}
  ${accountType}
  ${cloudCode}
  ${cloudName}
  ${customerNumber}
  ${customOptions.fieldName}
  ${groupCode}
  ${groupName}
  ${instance.instanceContext} # Environment Code
  ${platform == 'windows' ? 'w':'l'} # results in `w` for Windows platforms and `l` for Linux Platforms
  ${platform}
  ${provisionType}
  ${sequence} # results in 1
  ${sequence+100} # results in 101
  ${sequence.toString().padLeft(5,'0')} # results in 00001
  ${tenantId}
  ${tenant} # Tenant Name
  ${tenantSubdomain}
  ${type}
  ${userId}
  ${userInitials}
  ${username}

An example Instance Name Policy using a naming pattern with User Initials, Cloud Code, Instance Type, and a sequential number starting at 3000 is ``${userInitials}-${cloudCode}-${type}-${sequence+3000}``, resulting in an Instance Name of **md-vmwd3-centos-3001** for the first instance, followed by **md-vmwd3-centos-3002** and so on.

.. NOTE:: It's not recommended that users include ">", "<", "%", "$", or "=" in naming policies.

Syntax Examples
---------------

PowerShell Example: ``$app_id = "<%= instance.metadata.app_id %>"``

Bash Example:	``HOSTNAME="<%= container.server.hostname %>"``

Python Example: ``hostname = morpheus['server']['hostname']``

HTTP Body Example: ``{"name": "<%= instance.createdByUsername %>"}``

.. image:: /images/troubleshooting/Metadata-Enviornment-Variable-Spot

.. image:: /images/troubleshooting/Tags-Variable-Spot

.. NOTE:: customOptions values are defined from custom Inputs.

Common Examples
---------------

.. code-block:: bash

			container.configGroup: <%=container.configGroup%>
			container.configId: <%=container.configId%>
			container.configPath: <%=container.configPath%>
			container.configRole: <%=container.configRole%>
			container.containerTypeCode: <%=container.containerTypeCode%>
			container.containerTypeName: <%=container.containerTypeName%>
			container.containerTypeShortName: <%=container.containerTypeShortName%>
			container.cores: <%=container.cores%>
			container.dataPath: <%=container.dataPath%>
			container.dateCreated: <%=container.dateCreated%>
			container.domainName: <%=container.domainName%>
			container.environmentPrefix: <%=container.environmentPrefix%>
			container.externalIp: <%=container.externalIp%>
			container.hostMountPoint: <%=container.hostMountPoint%>
			container.hostname: <%=container.hostname%>
			container.image: <%=container.image%>
			container.internalHostname: <%=container.internalHostname%>
			container.internalIp: <%=container.internalIp%>
			container.logsPath: <%=container.logsPath%>
			container.memory: <%=container.memory%>
			container.planCode: <%=container.planCode%>
			container.provisionType: <%=container.provisionType%>
			container.server: <%=container.server.serverTypeName%>
			container.serverId: <%=container.serverId%>
			container.sshHost: <%=container.sshHost%>
			container.status: <%=container.status%>
			container.storage: <%=container.storage%>
			container.version: <%=container.version%>
			customOptions: <%=customOptions.fieldName%>
			evar: <%=evars.name%>
			evars: <%=evars%>
			group.code: <%=group.code%>
			group.datacenterId: <%=group.datacenterId%>
			group.location: <%=group.location%>
			group.name: <%=group.name%>
			instance.autoScale: <%=instance.autoScale%>
			instance.configGroup: <%=instance.configGroup%>
			instance.configId: <%=instance.configId%>
			instance.configRole: <%=instance.configRole%>
			instance.containers[0]: <%=instance.containers[0].containerTypeName%>
			instance.cores: <%=instance.cores%>
			instance.createdByEmail: <%=instance.createdByEmail%>
			instance.createdByFirstName: <%=instance.createdByFirstName%>
			instance.createdById: <%=instance.createdById%>
			instance.createdByLastName: <%=instance.createdByLastName%>
			instance.createdBYUsername: <%=instance.createdByUsername%>
			instance.deployGroup: <%=instance.deployGroup%>
			instance.description: <%=instance.description%>
			instance.displayName: <%=instance.displayName%>
			instance.domainName: <%=instance.domainName%>
			instance.environmentPrefix: <%=instance.environmentPrefix%>
			instance.expireDate: <%=instance.expireDate%>
			instance.firewallEnabled: <%=instance.firewallEnabled%>
			instance.hostname: <%=instance.hostname%>
			instance.instanceContext: <%=instance.instanceContext%> (tip: instanceContext = Environment)
			instance.instanceLevel: <%=instance.instanceLevel%>
			instance.instanceTypeCode: <%=instance.instanceTypeCode%>
			instance.instanceTypeName: <%=instance.instanceTypeName%>
			instance.instanceVersion: <%=instance.instanceVersion%>
			instance.memory: <%=instance.memory%>
			instance.metadata: <%=instance.metadata%>
			instance.name: <%=instance.name%>
			instance.networkLevel: <%=instance.networkLevel%>
			instance.plan: <%=instance.plan%>
			instance.provisionType: <%=instance.provisionType%>
			instance.status: <%=instance.status%>
			instance.statusMessage: <%=instance.statusMessage%>
			instance.storage: <%=instance.storage%>
			instance.metadata: <%=instance.metadata%>
			instance.userStatus: <%=instance.userStatus%>
			server.agentInstalled: <%=server.agentInstalled%>
			server.agentVersion: <%=server.agentVersion%>
			server.apiKey: <%=server.apiKey%>
			server.category: <%=server.category%>
			server.commType: <%=server.commType%>
			server.configGroup: <%=server.configGroup%>
			server.configId: <%=server.configId%>
			server.configRole: <%=server.configRole%>
			server.consoleHost: <%=server.consoleHost%>
			server.consolePort: <%=server.consolePort%>
			server.consoleType: <%=server.consoleType%>
			server.consoleUsername: <%=server.consoleUsername%>
			server.dataDevice: <%=server.dataDevice%>
			server.dateCreated: <%=server.dateCreated%>
			server.description: <%=server.description%>
			server.displayName: <%=server.displayName%>
			server.domainName: <%=server.domainName%>
			server.externalId: <%=server.externalId%>
			server.externalIp: <%=server.externalIp%>
			server.fqdn: <%=server.fqdn%>
			server.hostname: <%=server.hostname%>
			server.internalId: <%=server.internalId%>
			server.internalIp: <%=server.internalIp%>
			server.internalName: <%=server.internalName%>
			server.internalSshUsername: <%=server.internalSshUsername%>
			server.lastAgentUpdate: <%=server.lastAgentUpdate%>
			server.lvmEnabled: <%=server.lvmEnabled%>
			server.macAddress: <%=server.macAddress%>
			server.managed: <%=server.managed%>
			server.maxCores: <%=server.maxCores%>
			server.maxMemory: <%=server.maxMemory%>
			server.maxStorage: <%=server.maxStorage%>
			server.name: <%=server.name%>
			server.nodePackageVersion: <%=server.nodePackageVersion%>
			server.osDevice: <%=server.osDevice%>
			server.osType: <%=server.osType%>
			server.osTypeCode: <%=server.osTypeCode%>
			server.parentServerId: <%=server.parentServerId%>
			server.plan: <%=server.plan%>
			server.platform: <%=server.platform%>
			server.platformVersion: <%=server.platformVersion%>
			server.powerState: <%=server.powerState%>
			server.serialNumber: <%=server.serialNumber%>
			server.serverModel: <%=server.serverModel%>
			server.serverType: <%=server.serverType%>
			server.serverTypeCode: <%=server.serverTypeCode%>
			server.serverTypeName: <%=server.serverTypeName%>
			server.serverVendor: <%=server.serverVendor%>
			server.softwareRaid: <%=server.softwareRaid%>
			server.sourceImageId: <%=server.sourceImageId%>
			server.sshHost: <%=server.sshHost%>
			server.sshPort: <%=server.sshPort%>
			server.sshUsername: <%=server.sshUsername%>
			server.status: <%=server.status%>
			server.statusMessage: <%=server.statusMessage%>
			server.tags: <%=server.tags%>
			server.toolsInstalled: <%=server.toolsInstalled%>
			server.visibility: <%=server.visibility%>
			task.results (using task code): <%=results.taskCode%>
			task.results (using task name): <%=results["Task Name"]%>
			task.results.value: <%=results.taskCode.key%>
			zone.agentMode: <%=zone.agentMode%>
			zone.cloudTypeCode: <%=zone.cloudTypeCode%>
			zone.cloudTypeName: <%=zone.cloudTypeName%>
			zone.code: <%=zone.code%>
			zone.domainName: <%=zone.domainName%>
			zone.firewallEnabled: <%=zone.firewallEnabled%>
			zone.location: <%=zone.location%>
			zone.name: <%=zone.name%>
			zone.regionCode: <%=zone.regionCode%>
			zone.scalePriority: <%=zone.scalePriority%>
			cypher: <%=cypher.read('secret/hello')%>
      cypher: <%=cypher.read('secret/' + zone.code)%> # Make variables more dynamic based off other variables

Instance
--------

.. code-block:: bash

	instance {
		adminPassword,
		adminUsername,
		apps.[],
		assignedDomainName,
		autoScale,
		backup.{},
		configGroup,
		configId,
		configRole,
		container.{},
		containers.[],
		cores,
		createBackup,  true/false
		createdByEmail,
		createdByFirstName,
		createdById,
		createdByLastName,
		createdByUser.{
			 username,
			 displayName,
			 firstName,
			 lastName,
			 email,
			 linuxUsername,
			 windowsUsername
		},
		createdByUsername,
		createUser, # true/false
		customOptions,
		deployGroup,
		description,
		displayName,
		domainName,
		environmentPrefix,
		evars:{},
		expireDate, # YYYY-MM-DD-T00:00:00Z
		expireDays,
		expose.[],
		firewallEnabled:true/false,
		hostId,
		hostname,
		id,
		instanceContext,
		instanceLevel,
		instanceTypeCode,
		instanceTypeName,
		instanceVersion,
		isEC2:true/false,
		isVpcSelectable, # true/false
		layoutCode,
		layoutId,
		layoutName,
		layoutSize,
		lbInstances.[],
		memory(bytes),
		memoryDisplay, #MB/GB
		metadata.{},
		name,
		nestedVirtualization,
		networkLevel,
		noAgent,
		plan,
		poolProviderType,
		ports,
		provisionType,
		resourcePoolId,
		scheduleStatus,
		servicePassword,
		serviceUsername,
		smbiosAssetTag,
		sslCertId,
		sslEnabled, # true/false
		status,
		statusMessage,
		storage, # bytes
		tags,
		userStatus,
		vmwareFolderId,
	}

Container
---------

.. code-block:: bash

	container {
		configGroup,
		configId,
		configPath,
		configRole,
		containerTypeCode,
		containerTypeShortName,
		cores,
		dataPath,
		dateCreated,
		domainName,
		environmentPrefix,
		externalIp,
		hostMountPoint,
		hostname,
		image,
		internalHostname,
		internalIp,
		logsPath,
		memory,
		planCode,
		provisionType,
		server:{},
		serverId,
		sshHost,
		status,
		storage,
		version,
		containerTypeName
	}

Server
------

.. code-block:: bash

	server {
		agentInstalled,
		agentVersion,
		apiKey,
		category,
		commType,
		configGroup,
		configId,
		configRole
		consoleHost,
		consolePort,
		consoleType,
		consoleUsername,
		dataDevice,
		dateCreated,
		description,
		displayName,
		domainName,
		externalId,
		externalIp,
		fqdn,
		hostname,
		internalId,
		internalIp,
		internalName,
		internalSshUsername,
		lastAgentUpdate,
		lvmEnabled,
		macAddress,
		managed,
		maxCores,
		maxMemory,
		maxStorage,
		name,
		nodePackageVersion,
		osDevice,
		osType,
		osTypeCode,
		parentServerId,
		plan,
		platform,
		platformVersion,
		powerState,
		serialNumber,
		serverModel,
		serverType,
		serverTypeCode,
		serverTypeName,
		serverVendor,
		softwareRaid,
		sourceImageId,
		sshHost,
		sshPort,
		sshUsername,
		status,
		statusMessage,
		tags,
		toolsInstalled,
		visibility,
		volumes {
			name
			id
			deviceName
			maxStorage
			unitNumber
			displayOrder
			rootVolume
		}
	}

Zone (Cloud)
------------

.. code-block:: bash

			zone {
				agentMode,
				cloudTypeCode,
				cloudTypeName,
				code,
				datacenterId,
				domainName,
				firewallEnabled,
				location,
				name,
				regionCode,
				scalePriority
			}

networkConfig
-------------

.. code-block:: json

    'networkConfig': {
      'primaryInterface': {
        'doDhcp': false,
        'dnsServers': [],
        'dnsDomain': "",
        'netmask': "",
        'gateway': "",
        'ipAddress': "",
        'doDhcp6': false,
        'gateway6': "",
        'ipv6Address': "",
        'cidr6Suffix': "",
        'dnsServers6': ""
      },
      'extraInterfaces': [
        {
          'doDhcp': false,
          'dnsServers': [],
          'dnsDomain': "",
          'netmask': "",
          'gateway': "",
          'ipAddress': "",
          'doDhcp6': false,
          'gateway6': "",
          'ipv6Address': "",
          'cidr6Suffix': "",
          'dnsServers6': ""
        },
        {
          'doDhcp': false,
          'dnsServers': [],
          'dnsDomain': "",
          'netmask': "",
          'gateway': "",
          'ipAddress': "",
          'doDhcp6': false,
          'gateway6': "",
          'ipv6Address': "",
          'cidr6Suffix': "",
          'dnsServers6': ""
        }
      ]
    }

Group (Site)
------------

.. code-block:: bash

	group {
		code,
		location,
		datacenterId,
		name
	}

Custom Options (Inputs)
-----------------------------

.. code-block:: bash

			customOptions {
				customOptions.fieldName
			}

Global
------

ex: ``<%= morpheus.user.id %>``

.. code-block:: bash

			"morpheus":{
			   "user":{
			      "id":value,
			      "account":{
			         "id":value
			      },
			      "username":"value",
			      "displayName":"value",
			      "email":"value",
			      "firstName":"value",
			      "lastName":"value",
			      "dateCreated":0000-00-00T00:00:00Z,
			      "lastUpdated":0000-00-00T00:00:00Z,
			      "enabled":true/false,
			      "accountExpired":true/false,
			      "accountLocked":false,
			      "passwordExpired":false,
			      "defaultGroupId":value,
			      "defaultZoneId":value,
			      "hasLinuxUser":true/false,
			      "hasWindowsUser":true/false,
			      "role":{
			         "id":value
			      },
			      "instanceLimits":value
			   },
			}

User
----

.. code-block:: bash

    'user': {'accountId': int,
            'attributes': {samlAttributes},
            'displayName': 'string',
            'email': 'string',
            'firstName': 'string',
            'id': int,
            'lastName': 'string',
            'linuxUsername': 'string',
            'username': 'string',
            'windowsUsername': 'string',


Script Variables Example
------------------------

Below is an example of the variables available to a script running against an Instance context.

.. note:: Variable maps are determined by context, configurations and permissions, actual maps may contain additional or fewer options.

.. code-block:: bash

      'account': 'string',
      'accountId': int,
      'accountType': 'string',
      'allowExisting': boolean,
      'apps': [{'appContext': 'string',
                'description': 'string',
                'id': int,
                'name': 'string',
      'cloud': 'string',
      'cloudCode': 'string',
      'cloudName': 'string',
      'container': {'allowExisting': boolean,
                    'certificatePath': string,
                    'certificateStyle': string,
                    'changeManagementExtId': int,
                    'changeManagementServiceId': int,
                    'cloud': 'string',
                    'cloudConfig': {'agentInstall': agentInstallScript,
                                    'finalizeServer': finalizeServerScript,
                                    'meta': metaData,
                                    'user': userData},
                    'configGroup': int,
                    'configId': int,
                    'configPath': 'string',
                    'configRole': int,
                    'containerTypeCategory': 'string',
                    'containerTypeCode': 'string',
                    'containerTypeName': 'string',
                    'containerTypeShortName': 'string',
                    'cores': int,
                    'coresPerSocket': int,
                    'createUser': boolean,
                    'customOptions': {'morph_ver': 'string',
                    'dataPath': 'string',
                    'dateCreated': 'string',
                    'domainName': 'string',
                    'environmentPrefix': 'string',
                    'evars': {},
                    'expireDays': 'string',
                    'expose': ['string'],
                    'exposedPorts': [{'loadBalanceProtocol': 'string',
                                      'name': 'string',
                                      'port': int}],
                    'externalIp': 'string',
                    'externalPort': int,
                    'hostMountPoint': 'string',
                    'hostName': 'string',
                    'hostname': 'string',
                    'hosts': {'containerName': 'string',
                              'containerName': 'string',
                              'containerName': 'string',
                    'id': int,
                    'image': 'string',
                    'instanceContext': 'string',
                    'instanceType': {'code': 'string',
                    'internalHostname': 'string',
                    'internalIp': 'string',
                    'internalPort': int,
                    'layout': {'code': 'string',
                              'id': int},
                    'logsPath': 'string',
                    'maxCores': int,
                    'maxCpu': int,
                    'maxMemory': int,
                    'maxStorage': int,
                    'memory': int,
                    'memoryDisplay': 'string',
                    'mounts': [],
                    'name': 'string',
                    'networkId': int,
                    'networkInterfaces': [{'id': 'string',
                                          'ipAddress': 'string',
                                          'ipMode': 'string',
                                          'network': {'dhcpServer': int,
                                                      'group': int,
                                                      'id': int,
                                                      'name': 'string',
                                                      'pool': int},
                                          'networkInterfaceTypeId': int}],
                    'noAgent': boolean,
                    'planCode': 'string',
                    'portMap': {},
                    'ports': [{'displayName': 'string',
                              'export': boolean,
                              'exportName': 'string',
                              'external': int,
                              'index': int,
                              'internal': int,
                              'link': boolean,
                              'loadBalance': boolean,
                              'loadBalanceProtocol': 'string',
                              'name': 'string',
                              'primaryPort': boolean,
                              'protocol': 'string',
                              'visible': boolean},
                              {'displayName': 'string',
                              'export': boolean,
                              'exportName': 'string',
                              'external': int,
                              'index': int,
                              'internal': int,
                              'link': boolean,
                              'loadBalance': boolean,
                              'loadBalanceProtocol': 'string',
                              'name': 'string',
                              'primaryPort': boolean,
                              'protocol': 'string',
                              'visible': boolean}],
                    'provisionType': 'string',
                    'publicKeyId': int,
                    'server': {}
                    'serverId': int,
                    'shutdownDays': 'string',
                    'site': {'accountId': int,
                            'active': boolean,
                            'id': int,
                            'integrations': [],
                            'location': 'string',
                            'name': 'string',
                            'visibility': 'string',
                            'zones': [{}],
                    'sshHost': 'string',
                    'status': 'string',
                    'storage': int,
                    'storageController': int,
                    'type': 'string',
                    'userGroup': {'id': '',
                    'version': 'string',
                    'vm': boolean,
                    'volumes': [{'datastoreId': int,
                                'id': int,
                                'maxIOPS': int,
                                'maxStorage': int,
                                'name': 'string',
                                'rootVolume': boolean,
                                'size': int,
                                'storageType': int,
                                'vId': int}]},
      'containerName': 'string',
      'coresPerSocket': int,
      'createUser': boolean,
      'customOptions': {'morph_ver': 'string',
      'deployOptions': {},
      'evars': {},
      'expireDays': 'string',
      'expose': ['string'],
      'exposedPorts': [{'loadBalanceProtocol': 'string',
                        'name': 'string',
                        'port': int}],
      'externalIp': 'string',
      'group': {'code': 'string',
                'configCmdbId': 'string',
                'configManagementId': 'string',
                'datacenterId': int,
                'dnsIntegrationId': 'string',
                'location': 'string',
                'name': 'string',
                'serviceRegistryId': 'string',
      'groupCode': 'string',
      'groupName': 'string',
      'host': ,
      'hostMountPoint': 'string',
      'hostName': 'string',
      'hosts': {},
      'input': {'backup': ,
                'cloud': {},
                'computedHostName': 'string',
                'computedName': 'string',
                'copies': int,
                'domainOptions': {}},
                'environmentVariables': {},
                'executionId': int,
                'expireDays': int,
                'group': {},
                'hostName': 'string',
                'instanceContext': 'string',
                'layout': {},
                'metadata': {}},
                'name': 'string',
                'plan': {},
                'powerScheduleType': int,
                'securityGroups': {},
                'shutdownDays': int,
                'type': 'string',
                'version': 'string'},
      'instance': {'adminPassword': 'maskedString',
                  'adminUsername': 'string',
                  'allowExisting': boolean,
                  'apps': [{}],
                  'assignedDomainName': 'string',
                  'autoScale': boolean,
                  'backup': {'backupRepository': int,
                              'createBackup': boolean,
                              'enabled': boolean,
                              'jobAction': 'string',
                              'jobRetentionCount': 'string',
                              'providerBackupType': int,
                              'showScheduledBackupWarning': boolean},
                  'cloud': 'string',
                  'cloudConfig': {'agentInstall': agentInstallScript,
                                  'finalizeServer': finalizeServerScript,
                                  'meta': metaData,
                                  'user': userData
                                          },
                  'configGroup': int,
                  'configId': int,
                  'configRole': int,
                  'container': {},
                  'containers': [{}],
                  'cores': int,
                  'createBackup': boolean,
                  'createUser': boolean,
                  'createdByEmail': 'string',
                  'createdByFirstName': 'string',
                  'createdById': int,
                  'createdByLastName': 'string',
                  'createdByUser': {'accountId': int,
                                    'displayName': 'string',
                                    'email': 'string',
                                    'firstName': 'string',
                                    'id': int,
                                    'lastName': 'string',
                                    'linuxUsername': 'string',
                                    'username': 'string',
                                    'windowsUsername': 'string',
                  'createdByUsername': 'string',
                  'customOptions': {'morph_ver': 'string',
                  'deployGroup': ,
                  'description': 'string',
                  'displayName': 'string',
                  'domainName': 'string',
                  'environmentPrefix': 'string',
                  'evars': {
                  'expireDate': date,
                  'expireDays': 'string',
                  'expose': ['string'],
                  'firewallEnabled': boolean,
                  'hostName': 'string',
                  'hostname': 'string',
                  'id': int,
                  'instanceContext': 'string',
                  'instanceLevel': 'string',
                  'instanceType': {'code': 'string',
                  'instanceTypeCode': 'string',
                  'instanceTypeName': 'string',
                  'instanceVersion': 'string',
                  'layout': {'code': 'string',
                              'id': int},
                  'layoutCode': 'string',
                  'layoutId': int,
                  'layoutName': 'string',
                  'lbInstances': [{'balanceMode': 'string',
                                    'enabled': boolean,
                                    'externalAddress': 'string',
                                    'id': int,
                                    'instanceId': int,
                                    'loadBalancer': {'id': int},
                                    'loadBalancerId': int,
                                    'name': 'string',
                                    'port': int,
                                    'protocol': 'string',
                                    'sslCert': 'string',
                                    'sslRedirectMode': 'string',
                                    'stickyMode': 'string',
                                    'vipAddress': 'string',
                                    'vipDirectAddress': 'string',
                                    'vipHostname': 'string',
                                    'vipName': 'string',
                                    'vipPort': int,
                                    'vipProtocol': 'string',
                                    'vipScheme': 'string',
                                    'vipShared': 'string',
                  'loadBalancerId': int,
                  'memory': int,
                  'memoryDisplay': 'string',
                  'metadata': {'ver': 'string',
                  'name': 'string',
                  'networkLevel': 'string',
                  'plan': 'string',
                  'ports': {},
                  'powerScheduleType': ,
                  'provisionType': 'string',
                  'scheduleStatus': 'string',
                  'servicePassword': 'maskedString',
                  'serviceUsername': 'string',
                  'shutdownDays': 'string',
                  'site': {'accountId': int,
                            'active': boolean,
                            'id': int,
                            'integrations': [],
                            'location': 'string',
                            'name': 'string',
                            'visibility': 'string',
                            'zones': [{}]
                  'sslCertId': int,
                  'sslEnabled': boolean,
                  'status': 'string',
                  'statusMessage': 'string',
                  'storage': int,
                  'tags': 'string',
                  'type': ,
                  'userGroup': {'id': 'string',
                  'userStatus': 'string',
      'instanceContext': 'string',
      'instanceType': {'code': 'string',
      'internalIp': 'string',
      'isDocker': boolean,
      'layout': {'code': 'string',
      'localScriptGitId': int,
      'localScriptGitRef': 'string',
      'logTag': 'string',
      'maxCores': int,
      'maxCpu': int,
      'maxMemory': int,
      'maxStorage': int,
      'memoryDisplay': 'string',
      'morpheus': {'apiAccessToken': 'string',
                  'applianceHost': 'string',
                  'appliancePort': 'string',
                  'applianceScheme': 'string',
                  'applianceSsl': boolean,
                  'applianceUrl': 'string',
      'morpheusUser': 'string',
      'mounts': [],
      'name': 'string',
      'networkId': int,
      'networkInterfaces': [{'id': 'string',
                            'ipAddress': 'string',
                            'ipMode': 'string',
                            'network': {'dhcpServer': ,
                                        'group': int,
                                        'Id': int,
                                        'name': 'string',
                                        'pool': int},
                            'networkInterfaceTypeId': int}],
      'noAgent': boolean,
      'platform': 'string',
      'port': int,
      'ports': [{'code': 'string',
                'displayName': 'string',
                'export': boolean,
                'exportName': 'string',
                'external': int,
                'index': int,
                'internal': int,
                'link': boolean,
                'loadBalance': boolean,
                'primaryPort': boolean,
                'protocol': 'string',
                'visible': boolean}],
      'provisionType': 'string',
      'publicKeyId': int,
      'pythonAdditionalPackages': ,
      'pythonArgs': ,
      'pythonBinary': 'string',
      'pythonScript': ,
      'results': {},
      'sequence': int,
      'server': {'agentInstalled': boolean,
                'agentVersion': 'string',
                'apiKey': 'string',
                'category': ,
                'cloudConfig': {'agentInstall': agentInstallScript,
                                'finalizeServer': finalizeServerScript,
                                'meta': metaData,
                                'user': userData
                                        },
                'commType': 'string',
                'computeTypeCode': 'string',
                'computeTypeName': 'string',
                'configGroup': int,
                'configId': int,
                'configRole': 'string',
                'consoleHost': 'string',
                'consolePort': int,
                'consoleType': 'string',
                'consoleUsername': 'string',
                'createdByUser': {'accountId': int,
                                  'displayName': 'string',
                                  'email': 'string',
                                  'firstName': 'string',
                                  'id': int,
                                  'lastName': 'string',
                                  'linuxUsername': 'string',
                                  'username': 'string',
                                  'windowsUsername': 'string',
                'dataDevice': 'string',
                'dateCreated': 'string',
                'description': 'string',
                'displayName': 'string',
                'domainName': 'string',
                'externalId': 'string',
                'externalIp': 'string',
                'fqdn': 'string',
                'hostname': 'string',
                'id': int,
                'interfaces': [{'dhcp': boolean,
                                'domain': {'fqdn': 'string',
                                            'name': 'string',
                                            'ouPath': 'string'},
                                'interfaceId': int,
                                'ipAddress': 'string',
                                'ipMode': 'string',
                                'ipSubnet': 'string',
                                'ipv6Address': 'string',
                                'ipv6Subnet': 'string',
                                'macAddress': 'string',
                                'network': {'cidr': 'string',
                                            'cidrMask': 'string',
                                            'gateway': 'string',
                                            'name': 'string',
                                            'netmask': 'string',
                                            'vlanId': int},
                                'networkPosition': 'string',
                                'vlanId': int}],
                'internalId': int,
                'internalIp': 'string',
                'internalName': 'string',
                'internalSshUsername': 'string',
                'lastAgentUpdate': 'string',
                'lvmEnabled': boolean,
                'macAddress': 'string',
                'managed': boolean,
                'maxCores': int,
                'maxMemory': int,
                'maxStorage': int,
                'name': 'string',
                'nodePackageVersion': 'string',
                'osDevice': 'string',
                'osPassword': 'maskedString',
                'osType': 'string',
                'osTypeCode': 'string',
                'osUsername': 'string',
                'parentServerId': int,
                'plan': 'string',
                'platform': 'string',
                'platformVersion': 'string',
                'powerScheduleType': ,
                'powerState': 'string',
                'publicKeyId': int,
                'serialNumber': 'string',
                'serverModel': 'string',
                'serverType': 'string',
                'serverTypeCode': 'string',
                'serverTypeName': 'string',
                'serverVendor': 'string',
                'softwareRaid': boolean,
                'sourceImageId': int,
                'sshHost': 'string',
                'sshPort': int,
                'sshUsername': 'string',
                'status': 'string',
                'statusMessage': 'string',
                'tags': {},
                'toolsInstalled': boolean,
                'uniqueId': int,
                'uuid': 'string',
                'visibility': 'string',
                'volumes': [{'deviceName': 'string',
                              'displayOrder': int,
                              'id': int,
                              'maxStorage': int,
                              'name': 'string',
                              'rootVolume': boolean,
                              'unitNumber': 'string',
      'serverId': 'string',
      'serverName': 'string',
      'shutdownDays': 'string',
      'site': {'accountId': int,
              'active': boolean,
              'id': int,
              'integrations': [],
              'location': 'string',
              'name': 'string',
              'visibility': 'string',
              'zones': [{}],
      'sshKey': 'string',
      'state': {},
      'storageController': int,
      'tenant': 'string',
      'tenantId': int,
      'tenantSubdomain': 'string',
      'type': 'string',
      'user': {'accountId': int,
              'attributes': {samlAttributes},
              'displayName': 'string',
              'email': 'string',
              'firstName': 'string',
              'id': int,
              'lastName': 'string',
              'linuxUsername': 'string',
              'username': 'string',
              'windowsUsername': 'string',
      'userGroup': {'id': 'string',
      'userId': int,
      'userInitials': 'string',
      'username': 'string',
      'vm': boolean,
      'volumes': [{'datastoreId': int,
                  'id': int,
                  'maxIOPS': int,
                  'maxStorage': int,
                  'name': 'string',
                  'rootVolume': boolean,
                  'size': int,
                  'storageType': int,
                  'vId': int}],
      'zone': {'agentMode': 'string',
              'cloudTypeCode': 'string',
              'cloudTypeName': 'string',
              'code': 'string',
              'datacenterId': int,
              'domainName': 'string',
              'firewallEnabled': boolean,
              'location': 'string',
              'name': 'string',
              'regionCode': 'string',
              'scalePriority': int}}


.. note:: Variable maps are determined by context, configurations and permissions, actual maps may contain additional or fewer options.

Spec Template Variables
-----------------------

.. raw:: html

    <div class="info-modal">
    <h3 class="info-title">Spec Template Variables</h3>
    <div class="row break-container-sm">
    </div>
    <div class="row type-instance">
    <!--iterate the key set-->
    <ul class="resource-detail-list info-detail-list drag-list">
      <!--get morpheus, cypher, and archives-->
        <li>
          <strong>morpheus</strong>
          <ul class="modal-view-list">
            <li data-value="morpheus.getApiAccessToken()">getApiAccessToken()</li>
            <li data-value="morpheus.formatMemory(0, '')">formatMemory(size, unit)</li>
            <li data-value="morpheus.applianceUrl">applianceUrl</li>
            <li data-value="morpheus.applianceHost">applianceHost</li>
            <li data-value="morpheus.appliancePort">appliancePort</li>
            <li data-value="morpheus.applianceScheme">applianceScheme</li>
            <li data-value="morpheus.applianceSsl">applianceSsl</li>
            <li data-value="morpheus.morpheusHome">morpheusHome</li>
            <li data-value="morpheus.morpheusUser">morpheusUser</li>
            <li data-value="morpheus.publicKey">publicKey</li>
            <li data-value="morpheus.privateKey">privateKey</li>
            <li data-value="morpheus.cloudConfig">cloudConfig</li>
          </ul>
        </li>
        <li>
          <strong>cypher</strong>
          <ul class="modal-view-list">
            <li data-value="cypher.read('')">read(key)</li>
            <li data-value="cypher.write('', '')">write(key, value)</li>
            <li data-value="cypher.delete('')">delete(key)</li>
            <li data-value="cypher.readUuid('')">readUuid(key)</li>
            <li data-value="cypher.readEncyptionKey('')">readEncyptionKey(key)</li>
            <li data-value="cypher.readPassword('')">readPassword(key)</li>
          </ul>
        </li>
        <li>
          <strong>archives</strong>
          <ul class="modal-view-list">
            <li data-value="archives.link('', '')">link(bucketName, filePath)</li>
          </ul>
        </li>
      <!--add other keys-->
            <li data-value="account">account</li>
            <li data-value="accountId">accountId</li>
            <li data-value="accountType">accountType</li>
            <li data-value="apps[0]">
              <strong>apps - []</strong>
                  <ul class="modal-view-list">
                      <li data-value="apps[0].appContext">appContext</li>
                      <li data-value="apps[0].description">description</li>
                      <li data-value="apps[0].id">id</li>
                      <li data-value="apps[0].name">name</li>
                  </ul>
            </li>
            <li data-value="cloudConfig.">
              <strong>cloudConfig</strong>
              <ul class="modal-view-list">
                    <li data-value="cloudConfig.agentInstall">agentInstall</li>
                    <li data-value="cloudConfig.finalizeServer">finalizeServer</li>
              </ul>
            </li>
            <li data-value="customOptions.">
              <strong>customOptions</strong>
              <ul class="modal-view-list">
                    <li data-value="customOptions.key">key</li>
              </ul>
            </li>
            <li data-value="deployOptions.">
              <strong>deployOptions</strong>
              <ul class="modal-view-list">
                    <li data-value="deployOptions.key">key</li>
              </ul>
            </li>
            <li data-value="evars.">
              <strong>evars</strong>
              <ul class="modal-view-list">
                    <li data-value="evars."></li>
                    <li data-value="evars.key">key</li>
              </ul>
            </li>
            <li data-value="group.">
              <strong>group</strong>
              <ul class="modal-view-list">
                    <li data-value="group.code">code</li>
                    <li data-value="group.datacenterId">datacenterId</li>
                    <li data-value="group.location">location</li>
                    <li data-value="group.name">name</li>
              </ul>
            </li>
            <li data-value="groupCode">groupCode</li>
            <li data-value="groupName">groupName</li>
            <li data-value="input.">
              <strong>input</strong>
              <ul class="modal-view-list">
                    <li data-value="input.backup">backup</li>
                    <li data-value="input.cloud.">cloud
                      <ul class="modal-view-list">
                      </ul>
                    </li>
                    <li data-value="input.computedHostName">computedHostName</li>
                    <li data-value="input.computedName">computedName</li>
                    <li data-value="input.copies">copies</li>
                    <li data-value="input.domainOptions">domainOptions</li>
                    <li data-value="input.environmentVariables">environmentVariables</li>
                    <li data-value="input.executionId">executionId</li>
                    <li data-value="input.expireDays">expireDays</li>
                    <li data-value="input.group.">group
                      <ul class="modal-view-list">
                      </ul>
                    </li>
                    <li data-value="input.hostName">hostName</li>
                    <li data-value="input.instanceContext">instanceContext</li>
                    <li data-value="input.layout.">layout
                      <ul class="modal-view-list">
                      </ul>
                    </li>
                    <li data-value="input.metadata">metadata</li>
                    <li data-value="input.name">name</li>
                    <li data-value="input.plan.">plan
                      <ul class="modal-view-list">
                      </ul>
                    </li>
                    <li data-value="input.powerScheduleType">powerScheduleType</li>
                    <li data-value="input.securityGroups">securityGroups</li>
                    <li data-value="input.shutdownDays">shutdownDays</li>
                    <li data-value="input.type">type</li>
                    <li data-value="input.version">version</li>
              </ul>
            </li>
            <li data-value="instance.">
              <strong>instance</strong>
              <ul class="modal-view-list">
                    <li data-value="instance.adminPassword">adminPassword</li>
                    <li data-value="instance.adminUsername">adminUsername</li>
                      <li data-value="instance.apps[0]">apps - []</li>
                        <ul class="modal-view-list">
                            <li data-value="instance.apps.appContext">appContext</li>
                            <li data-value="instance.apps.description">description</li>
                            <li data-value="instance.apps.id">id</li>
                            <li data-value="instance.apps.instances">instances</li>
                            <li data-value="instance.apps.name">name</li>
                        </ul>
                    <li data-value="instance.assignedDomainName">assignedDomainName</li>
                    <li data-value="instance.autoScale">autoScale</li>
                    <li data-value="instance.cloudConfig.">cloudConfig
                      <ul class="modal-view-list">
                          <li data-value="instance.cloudConfig.agentInstall">agentInstall</li>
                          <li data-value="instance.cloudConfig.finalizeServer">finalizeServer</li>
                      </ul>
                    </li>
                    <li data-value="instance.configGroup">configGroup</li>
                    <li data-value="instance.configId">configId</li>
                    <li data-value="instance.configRole">configRole</li>
                    <li data-value="instance.container.">container
                      <ul class="modal-view-list">
                          <li data-value="instance.container.certificatePath">certificatePath</li>
                          <li data-value="instance.container.certificateStyle">certificateStyle</li>
                          <li data-value="instance.container.changeManagementExtId">changeManagementExtId</li>
                          <li data-value="instance.container.changeManagementServiceId">changeManagementServiceId</li>
                          <li data-value="instance.container.cloudConfig">cloudConfig</li>
                          <li data-value="instance.container.configGroup">configGroup</li>
                          <li data-value="instance.container.configId">configId</li>
                          <li data-value="instance.container.configPath">configPath</li>
                          <li data-value="instance.container.configRole">configRole</li>
                          <li data-value="instance.container.containerTypeCategory">containerTypeCategory</li>
                          <li data-value="instance.container.containerTypeCode">containerTypeCode</li>
                          <li data-value="instance.container.containerTypeName">containerTypeName</li>
                          <li data-value="instance.container.containerTypeShortName">containerTypeShortName</li>
                          <li data-value="instance.container.cores">cores</li>
                          <li data-value="instance.container.dataPath">dataPath</li>
                          <li data-value="instance.container.dateCreated">dateCreated</li>
                          <li data-value="instance.container.domainName">domainName</li>
                          <li data-value="instance.container.environmentPrefix">environmentPrefix</li>
                          <li data-value="instance.container.externalIp">externalIp</li>
                          <li data-value="instance.container.hostMountPoint">hostMountPoint</li>
                          <li data-value="instance.container.hostname">hostname</li>
                          <li data-value="instance.container.id">id</li>
                          <li data-value="instance.container.image">image</li>
                          <li data-value="instance.container.internalHostname">internalHostname</li>
                          <li data-value="instance.container.internalIp">internalIp</li>
                          <li data-value="instance.container.logsPath">logsPath</li>
                          <li data-value="instance.container.memory">memory</li>
                          <li data-value="instance.container.name">name</li>
                          <li data-value="instance.container.planCode">planCode</li>
                          <li data-value="instance.container.portMap">portMap</li>
                          <li data-value="instance.container.ports">ports</li>
                          <li data-value="instance.container.provisionType">provisionType</li>
                          <li data-value="instance.container.server">server</li>
                          <li data-value="instance.container.serverId">serverId</li>
                          <li data-value="instance.container.sshHost">sshHost</li>
                          <li data-value="instance.container.status">status</li>
                          <li data-value="instance.container.storage">storage</li>
                          <li data-value="instance.container.version">version</li>
                      </ul>
                    </li>
                      <li data-value="instance.containers[0]">containers - []</li>
                        <ul class="modal-view-list">
                            <li data-value="instance.containers.certificatePath">certificatePath</li>
                            <li data-value="instance.containers.certificateStyle">certificateStyle</li>
                            <li data-value="instance.containers.changeManagementExtId">changeManagementExtId</li>
                            <li data-value="instance.containers.changeManagementServiceId">changeManagementServiceId</li>
                            <li data-value="instance.containers.cloudConfig">cloudConfig</li>
                            <li data-value="instance.containers.configGroup">configGroup</li>
                            <li data-value="instance.containers.configId">configId</li>
                            <li data-value="instance.containers.configPath">configPath</li>
                            <li data-value="instance.containers.configRole">configRole</li>
                            <li data-value="instance.containers.containerTypeCategory">containerTypeCategory</li>
                            <li data-value="instance.containers.containerTypeCode">containerTypeCode</li>
                            <li data-value="instance.containers.containerTypeName">containerTypeName</li>
                            <li data-value="instance.containers.containerTypeShortName">containerTypeShortName</li>
                            <li data-value="instance.containers.cores">cores</li>
                            <li data-value="instance.containers.dataPath">dataPath</li>
                            <li data-value="instance.containers.dateCreated">dateCreated</li>
                            <li data-value="instance.containers.domainName">domainName</li>
                            <li data-value="instance.containers.environmentPrefix">environmentPrefix</li>
                            <li data-value="instance.containers.externalIp">externalIp</li>
                            <li data-value="instance.containers.hostMountPoint">hostMountPoint</li>
                            <li data-value="instance.containers.hostname">hostname</li>
                            <li data-value="instance.containers.id">id</li>
                            <li data-value="instance.containers.image">image</li>
                            <li data-value="instance.containers.internalHostname">internalHostname</li>
                            <li data-value="instance.containers.internalIp">internalIp</li>
                            <li data-value="instance.containers.logsPath">logsPath</li>
                            <li data-value="instance.containers.memory">memory</li>
                            <li data-value="instance.containers.name">name</li>
                            <li data-value="instance.containers.planCode">planCode</li>
                            <li data-value="instance.containers.portMap">portMap</li>
                            <li data-value="instance.containers.ports">ports</li>
                            <li data-value="instance.containers.provisionType">provisionType</li>
                            <li data-value="instance.containers.server">server</li>
                            <li data-value="instance.containers.serverId">serverId</li>
                            <li data-value="instance.containers.sshHost">sshHost</li>
                            <li data-value="instance.containers.status">status</li>
                            <li data-value="instance.containers.storage">storage</li>
                            <li data-value="instance.containers.version">version</li>
                        </ul>
                    <li data-value="instance.cores">cores</li>
                    <li data-value="instance.createdByEmail">createdByEmail</li>
                    <li data-value="instance.createdByFirstName">createdByFirstName</li>
                    <li data-value="instance.createdById">createdById</li>
                    <li data-value="instance.createdByLastName">createdByLastName</li>
                    <li data-value="instance.createdByUser.">createdByUser
                      <ul class="modal-view-list">
                          <li data-value="instance.createdByUser.accountId">accountId</li>
                          <li data-value="instance.createdByUser.attributes">attributes</li>
                          <li data-value="instance.createdByUser.displayName">displayName</li>
                          <li data-value="instance.createdByUser.email">email</li>
                          <li data-value="instance.createdByUser.firstName">firstName</li>
                          <li data-value="instance.createdByUser.id">id</li>
                          <li data-value="instance.createdByUser.lastName">lastName</li>
                          <li data-value="instance.createdByUser.linuxUsername">linuxUsername</li>
                          <li data-value="instance.createdByUser.username">username</li>
                          <li data-value="instance.createdByUser.windowsUsername">windowsUsername</li>
                      </ul>
                    </li>
                    <li data-value="instance.createdByUsername">createdByUsername</li>
                    <li data-value="instance.customOptions.">customOptions
                      <ul class="modal-view-list">
                          <li data-value="instance.customOptions.key">key</li>
                      </ul>
                    </li>
                    <li data-value="instance.deployGroup">deployGroup</li>
                    <li data-value="instance.description">description</li>
                    <li data-value="instance.displayName">displayName</li>
                    <li data-value="instance.domainName">domainName</li>
                    <li data-value="instance.environmentPrefix">environmentPrefix</li>
                    <li data-value="instance.evars.">evars
                      <ul class="modal-view-list">
                          <li data-value="instance.evars.key">key</li>
                      </ul>
                    </li>
                    <li data-value="instance.expireDate">expireDate</li>
                    <li data-value="instance.firewallEnabled">firewallEnabled</li>
                    <li data-value="instance.hostname">hostname</li>
                    <li data-value="instance.id">id</li>
                    <li data-value="instance.instanceContext">instanceContext</li>
                    <li data-value="instance.instanceLevel">instanceLevel</li>
                    <li data-value="instance.instanceTypeCode">instanceTypeCode</li>
                    <li data-value="instance.instanceTypeName">instanceTypeName</li>
                    <li data-value="instance.instanceVersion">instanceVersion</li>
                    <li data-value="instance.layoutCode">layoutCode</li>
                    <li data-value="instance.layoutId">layoutId</li>
                    <li data-value="instance.layoutName">layoutName</li>
                    <li data-value="instance.memory">memory</li>
                    <li data-value="instance.metadata.">metadata
                      <ul class="modal-view-list">
                      </ul>
                    </li>
                    <li data-value="instance.name">name</li>
                    <li data-value="instance.networkLevel">networkLevel</li>
                    <li data-value="instance.plan">plan</li>
                    <li data-value="instance.ports">ports</li>
                    <li data-value="instance.provisionType">provisionType</li>
                    <li data-value="instance.scheduleStatus">scheduleStatus</li>
                    <li data-value="instance.servicePassword">servicePassword</li>
                    <li data-value="instance.serviceUsername">serviceUsername</li>
                    <li data-value="instance.sslCertId">sslCertId</li>
                    <li data-value="instance.sslEnabled">sslEnabled</li>
                    <li data-value="instance.status">status</li>
                    <li data-value="instance.statusMessage">statusMessage</li>
                    <li data-value="instance.storage">storage</li>
                    <li data-value="instance.tags">tags</li>
                    <li data-value="instance.templateOutput.">templateOutput
                      <ul class="modal-view-list">
                          <li data-value="instance.templateOutput."></li>
                      </ul>
                    </li>
                    <li data-value="instance.userStatus">userStatus</li>
              </ul>
            </li>
            <li data-value="platform">platform</li>
            <li data-value="provisionType">provisionType</li>
            <li data-value="results.">
              <strong>results</strong>
              <ul class="modal-view-list">
              </ul>
            </li>
            <li data-value="sequence">sequence</li>
            <li data-value="state.">
              <strong>state</strong>
              <ul class="modal-view-list">
                    <li data-value="state.iacDrift">iacDrift</li>
                    <li data-value="state.stateDate">stateDate</li>
                      <li data-value="state.stateList[0]">stateList - []</li>
                        <ul class="modal-view-list">
                            <li data-value="state.stateList.category">category</li>
                            <li data-value="state.stateList.code">code</li>
                            <li data-value="state.stateList.contentPath">contentPath</li>
                            <li data-value="state.stateList.errorMessage">errorMessage</li>
                            <li data-value="state.stateList.iacDrift">iacDrift</li>
                            <li data-value="state.stateList.id">id</li>
                            <li data-value="state.stateList.input">input</li>
                            <li data-value="state.stateList.name">name</li>
                            <li data-value="state.stateList.output">output</li>
                            <li data-value="state.stateList.planPath">planPath</li>
                            <li data-value="state.stateList.resourceVersion">resourceVersion</li>
                            <li data-value="state.stateList.stateContext">stateContext</li>
                            <li data-value="state.stateList.stateDate">stateDate</li>
                            <li data-value="state.stateList.stateId">stateId</li>
                            <li data-value="state.stateList.statePath">statePath</li>
                            <li data-value="state.stateList.stateType">stateType</li>
                            <li data-value="state.stateList.status">status</li>
                            <li data-value="state.stateList.statusMessage">statusMessage</li>
                            <li data-value="state.stateList.tags">tags</li>
                            <li data-value="state.stateList.workingPath">workingPath</li>
                        </ul>
                    <li data-value="state.stateType">stateType</li>
              </ul>
            </li>
            <li data-value="tenant">tenant</li>
            <li data-value="tenantId">tenantId</li>
            <li data-value="tenantSubdomain">tenantSubdomain</li>
            <li data-value="type">type</li>
            <li data-value="userId">userId</li>
            <li data-value="userInitials">userInitials</li>
            <li data-value="username">username</li>
    </ul>
    </div>
    </
