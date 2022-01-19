Variables
=========

A vast number of variables are available for use in Tasks, Scripts, Templates, Resource Names, Cloud-Init User Data and Option List configs.

.. IMPORTANT:: Variables are case sensitive

Pre-Provision Vars
------------------

A subset of variables are available for Instance, Host Name and Hostnames. These can be passed inside ``${ }`` blocks during provisioning or in relevant policy configs.

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
		  ${sequence.toString().padLeft(5,'0')} #results in 00001
		${tenantId}
		${tenant} # Teant Name
		${tenantSubdomain}
		${type}
		${userId}
		${userInitials}
		${username}

An example Instance Name Policy using a naming pattern with User Initials, Cloud Code, Instance Type, and a sequential number starting at 3000 is ``${userInitials}-${cloudCode}-${type}-${sequence+3000}``, resulting in an Instance Name of **md-vmwd3-centos-3001** for the first instance, followed by **md-vmwd3-centos-3002** and so on.

Syntax Examples
---------------

PowerShell Example: ``$app_id = "<%= instance.metadata.app_id %>"``

Bash Example:	``HOSTNAME="<%= container.server.hostname %>"``

Python Example: ``hostname = morpheus['server']['hostname']``

HTTP Body Example: ``{"name": "<%= instance.createdByUsername %>"}``

.. image:: /images/troubleshooting/Metadata-Enviornment-Variable-Spot

.. image:: /images/troubleshooting/Tags-Variable-Spot

.. NOTE:: customOptions values are defined from custom Option Types.

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
			instance.createdByUsername: <%=instance.createdByUsername%>
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
			instance.tags: <%=instance.tags%>
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

Group (Site)
------------

.. code-block:: bash

	group {
		code,
		location,
		datacenterId,
		name
	}

Custom Options (Option Types)
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
			      "enabled":true/fase,
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

Instance Map Example
--------------------

.. code-block:: bash

		"instance":{
		   "poolProviderType":value,
		   "isVpcSelectable":true/false,
		   "smbiosAssetTag":value,
		   "isEC2":true/false,
		   "resourcePoolId":value,
		   "hostId":value,
		   "createUser":true/false,
		   "nestedVirtualization":value,
		   "vmwareFolderId":value,
		   "expose":[

		   ],
		   "noAgent":value,
		   "customOptions":value,
		   "createBackup":true/false,
		   "memoryDisplay":"MB/GB",
		   "backup":{
		      "veeamManagedServer":,
		      "createBackup":true/false,
		      "jobAction":"value",
		      "jobRetentionCount":value
		   },
		   "expireDays":value,
		   "layoutSize":value,
		   "lbInstances":[

		   ],
		   "evars":{
		      "evar1":{
		         "value":value,
		         "export":true/false,
		         "masked":true/false,
		         "name":"value"
		      },
		      "evar2":{
		         "value":value,
		         "export":true/false,
		         "masked":true/false,
		         "name":"value"
		      }
		   },
		   "id":value,
		   "instanceTypeName":"value",
		   "instanceTypeCode":"value",
		   "provisionType":"value",
		   "layoutId":value,
		   "layoutCode":value,
		   "layoutName":"value",
		   "instanceVersion":"value",
		   "plan":value,
		   "name":value,
		   "displayName":value,
		   "description":value,
		   "environmentPrefix":value,
		   "hostname":value,
		   "domainName":"value",
		   "assignedDomainName":,
		   "firewallEnabled":true/false,
		   "status":"value",
		   "userStatus":"value",
		   "scheduleStatus":"value",
		   "networkLevel":"value",
		   "instanceLevel":"value",
		   "deployGroup":value,
		   "instanceContext":value,
		   "autoScale":true/false,
		   "statusMessage":value,
		   "expireDate":0000-00-00T00:00:00Z,
		   "tags":"value",
		   "storage":value(bytes),
		   "memory":value(bytes),
		   "cores":1,
		   "configId":value,
		   "configGroup":value,
		   "configRole":value,
		   "ports":value,
		   "sslEnabled":true/false,
		   "sslCertId":value,
		   "serviceUsername":value,
		   "servicePassword":value,
		   "adminUsername":value,
		   "adminPassword":value,
		   "createdByUsername":"value",
		   "createdByEmail":"value",
		   "createdByFirstName":"value",
		   "createdByLastName":"value",
		   "createdById":value,
		   "metadata":{

		   },
		   "createdByUser":{
		      "username":"value",
		      "displayName":"value",
		      "firstName":"value",
		      "lastName":"value",
		      "email":"value",
		      "linuxUsername":"value",
		      "windowsUsername":"value"
		   },
		   "containers":[
		      {
		         "maxMemory":value(bytes),
		         "maxStorage":value(bytes),
		         "maxCpu":value,
		         "maxCores":value,
		         "coresPerSocket":value,
		         "poolProviderType":value,
		         "isVpcSelectable":true/false,
		         "smbiosAssetTag":value,
		         isEC2:true/false,
		         "resourcePoolId":value,
		         "hostId":value,
		         "createUser":true/false,
		         "nestedVirtualization":value,
		         "vmwareFolderId":value,
		         "expose":[

		         ],
		         "noAgent":true/false,
		         "vm":true/false,
		         "networkInterfaces":[
		            {
		               "id":value,
		               "network":{
		                  "id":value,
		                  "group":value,
		                  "subnet":value,
		                  "dhcpServer":true/false,
		                  "name":value,
		                  "pool":{
		                     "id":value,
		                     "name":value
		                  }
		               },
		               "ipAddress":value,
		               "networkInterfaceTypeId":value,
		               "ipMode":
		            }
		         ],
		         "volumes":[
		            {
		               "volumeCustomizable":true/false,
		               "readonlyName":true/false,
		               "controllerId":value,
		               "maxIOPS":value,
		               "displayOrder":value,
		               "unitNumber":value,
		               "minStorage":value(bytes),
		               "configurableIOPS":true/false,
		               "controllerMountPoint":0000:0:00:0,
		               "vId":value,
		               "size":value,
		               "name":"root",
		               "rootVolume":true/false,
		               "storageType":value,
		               "typeId":value,
		               "id":value,
		               "resizeable":true/false,
		               "datastoreId":"value",
		               "maxStorage":value(bytes)
		            }
		         ],
		         "storageController":value,
		         "datastoreId":value,
		         "networkId":value,
		         "cpuCount":value,
		         "memorySize":value,
		         "osDiskSize":value,
		         "publicKeyId":value,
		         "storagePodId":value,
		         "vmwareUsr":value,
		         "vmwarePwd":value,
		         "domainName":"value",
		         "hostname":value,
		         "networkType":value,
		         "ipAddress":value,
		         "netmask":value,
		         "gateway":value,
		         "dnsServers":value,
		         "resourcePool":value,
		         "folder":value,
		         "vmwareCustomSpec":value,
		         "hosts":{
		            value
		         },
		         "evars":{

		         },
		         "id":value,
		         "name":value,
		         "containerTypeName":value,
		         "containerTypeCode":value,
		         "containerTypeShortName":"value",
		         "containerTypeCategory":"value",
		         "provisionType":"value",
		         "dataPath":"value",
		         "logsPath":"value",
		         "configPath":"value",
		         "planCode":value,
		         "dateCreated":0000-00-00T00:00:00Z,
		         "status":"running",
		         "environmentPrefix":"value",
		         "version":"value",
		         "image":"value",
		         "internalHostname":value,
		         "storage":value(bytes),
		         "memory":value(bytes),
		         "cores":value,
		         "internalIp":value,
		         "externalIp":value,
		         "sshHost":value,
		         "hostMountPoint":value,
		         "configId":value,
		         "configGroup":value,
		         "configRole":value,
		         "certificatePath":value,
		         "certificateStyle":value,
		         "changeManagementExtId":value,
		         "changeManagementServiceId":value,
		         "serverId":value,
		         "server":{
		            "poolProviderType":value,
		            "isVpcSelectable":true/false,
		            "smbiosAssetTag":value,
		            isEC2:true/false,
		            "resourcePoolId":value,
		            "hostId":value,
		            "createUser":true/false,
		            "nestedVirtualization":value,
		            "vmwareFolderId":value,
		            "noAgent":value,
		            "id":value,
		            "uuid":value,
		            "serverTypeName":"value",
		            "serverTypeCode":"value",
		            "computeTypeName":"value",
		            "computeTypeCode":"value",
		            "parentServerId":value,
		            "plan":value,
		            "visibility":"value",
		            "osTypeCode":value,
		            "sourceImageId":value,
		            "name":value,
		            "displayName":value,
		            "internalName":value,
		            "category":value,
		            "description":value,
		            "internalId":value,
		            "externalId":value,
		            "platform":"value",
		            "platformVersion":value,
		            "agentVersion":value,
		            "nodePackageVersion":value,
		            "sshHost":value,
		            "sshPort":value,
		            "sshUsername":"value",
		            "consoleType":value,
		            "consoleHost":value,
		            "consolePort":value,
		            "consoleUsername":value,
		            "internalSshUsername":"value",
		            "internalIp":value,
		            "externalIp":value,
		            "osDevice":"value",
		            "dataDevice":"value",
		            "lvmEnabled":true/false,
		            "apiKey":value,
		            "softwareRaid":true/false,
		            "status":"value",
		            "powerState":"value",
		            "dateCreated":0000-00-00T00:00:00Z,
		            "lastAgentUpdate":0000-00-00T00:00:00Z,
		            "serverType":"value",
		            "osType":"value",
		            "commType":"value",
		            "managed":true/false,
		            "agentInstalled":true/false,
		            "toolsInstalled":true/false,
		            "hostname":value,
		            "domainName":value,
		            "fqdn":value,
		            "statusMessage":value,
		            "maxStorage":value(bytes),
		            "maxMemory":value(bytes),
		            "maxCores":value,
		            "macAddress":value,
		            "serverVendor":value,
		            "serverModel":value,
		            "serialNumber":value,
		            "tags":value,
		            "configId":value,
		            "configGroup":value,
		            "configRole":value,
		            "createdByUser":{
		               "username":"value",
		               "displayName":"value",
		               "firstName":"value",
		               "lastName":"value",
		               "email":"value",
		               "linuxUsername":"value",
		               "windowsUsername":"value"
		            },
		            "volumes":[
		               {
		                  "id":value,
		                  "name":"value",
		                  "deviceName":"value",
		                  "maxStorage":value(bytes),
		                  "unitNumber":value,
		                  "displayOrder":value,
		                  "rootVolume":true/false
		               }
		            ]
		         },
		         "ports":[
		            {
		               "index":value,
		               "external":value,
		               "internal":value,
		               "link":true/false,
		               "loadBalance":true/false,
		               "loadBalanceProtocol":value,
		               "export":true/false,
		               "exportName":value,
		               "displayName":"value",
		               "visible":true/false,
		               "primaryPort":true/false,
		               "protocol":value,
		               "name":"value"
		            }
		         ],
		         "portMap":{
		            "rpc":{
		               "index":value,
		               "external":value,
		               "internal":value,
		               "link":true/false,
		               "loadBalance":true/false,
		               "loadBalanceProtocol":value,
		               "export":true/false,
		               "exportName":value,
		               "displayName":"value",
		               "visible":true/false,
		               "primaryPort":true/false,
		               "protocol":value,
		               "name":"value"
		            }
		         },
		         "internalPort":value,
		         "externalPort":value
		      }
		   ],
		   "container":{
		      "maxMemory":value(bytes),
		      "maxStorage":value,
		      "maxCpu":value,
		      "maxCores":value,
		      "coresPerSocket":value,
		      "poolProviderType":value,
		      "isVpcSelectable":true/false,
		      "smbiosAssetTag":value,
		      isEC2:true/false,
		      "resourcePoolId":value,
		      "hostId":value,
		      "createUser":true/false,
		      "nestedVirtualization":value,
		      "vmwareFolderId":value,
		      "expose":[

		      ],
		      "noAgent":true/false,
		      "vm":true/false,
		      "networkInterfaces":[
		         {
		            "id":value,
		            "network":{
		               "id":value,
		               "group":value,
		               "subnet":value,
		               "dhcpServer":true/false,
		               "name":value,
		               "pool":{
		                  "id":value,
		                  "name":value
		               }
		            },
		            "ipAddress":value,
		            "networkInterfaceTypeId":value,
		            "ipMode":
		         }
		      ],
		      "volumes":[
		         {
		            "volumeCustomizable":true/false,
		            "readonlyName":true/false,
		            "controllerId":value,
		            "maxIOPS":value,
		            "displayOrder":value,
		            "unitNumber":value,
		            "minStorage":value,
		            "configurableIOPS":true/false,
		            "controllerMountPoint":value,
		            "vId":value,
		            "size":value,
		            "name":"root",
		            "rootVolume":true/false,
		            "storageType":value,
		            "typeId":value,
		            "id":value,
		            "resizeable":true/false,
		            "datastoreId":"autoCluster",
		            "maxStorage":value(bytes)
		         }
		      ],
		      "storageController":value,
		      "datastoreId":value,
		      "networkId":value,
		      "cpuCount":value,
		      "memorySize":value,
		      "osDiskSize":value,
		      "publicKeyId":value,
		      "storagePodId":value,
		      "vmwareUsr":value,
		      "vmwarePwd":value,
		      "domainName":"value",
		      "hostname":value,
		      "networkType":value,
		      "ipAddress":value,
		      "netmask":value,
		      "gateway":value,
		      "dnsServers":value,
		      "resourcePool":value,
		      "folder":value,
		      "vmwareCustomSpec":value,
		      "hosts":{
		         value
		      },
		      "evars":{

		      },
		      "id":value,
		      "name":value,
		      "containerTypeName":value,
		      "containerTypeCode":value,
		      "containerTypeShortName":"value",
		      "containerTypeCategory":"value",
		      "provisionType":"vmware",
		      "dataPath":"value",
		      "logsPath":"value",
		      "configPath":"value",
		      "planCode":value,
		      "dateCreated":0000-00-00T00:00:00Z,
		      "status":"value",
		      "environmentPrefix":"value",
		      "version":"value",
		      "image":"value",
		      "internalHostname":value,
		      "storage":value(bytes),
		      "memory":value(bytes),
		      "cores":value,
		      "internalIp":value,
		      "externalIp":value,
		      "sshHost":value,
		      "hostMountPoint":value,
		      "configId":value,
		      "configGroup":value,
		      "configRole":value,
		      "certificatePath":value,
		      "certificateStyle":value,
		      "changeManagementExtId":value,
		      "changeManagementServiceId":value,
		      "serverId":value,
		      "server":{
		         "poolProviderType":value,
		         "isVpcSelectable":true/false,
		         "smbiosAssetTag":value,
		         isEC2:true/false,
		         "resourcePoolId":value,
		         "hostId":value,
		         "createUser":true/false,
		         "nestedVirtualization":value,
		         "vmwareFolderId":value,
		         "noAgent":value,
		         "id":value,
		         "uuid":value,
		         "serverTypeName":"value",
		         "serverTypeCode":"value",
		         "computeTypeName":"value",
		         "computeTypeCode":"value",
		         "parentServerId":value,
		         "plan":value,
		         "visibility":"value",
		         "osTypeCode":value,
		         "sourceImageId":value,
		         "name":value,
		         "displayName":value,
		         "internalName":value,
		         "category":value,
		         "description":value,
		         "internalId":value,
		         "externalId":value,
		         "platform":"value",
		         "platformVersion":value,
		         "agentVersion":value,
		         "nodePackageVersion":value,
		         "sshHost":value,
		         "sshPort":value,
		         "sshUsername":"value",
		         "consoleType":value,
		         "consoleHost":value,
		         "consolePort":value,
		         "consoleUsername":value,
		         "internalSshUsername":"value",
		         "internalIp":value,
		         "externalIp":value,
		         "osDevice":"value",
		         "dataDevice":"value",
		         "lvmEnabled":true/false,
		         "apiKey":value,
		         "softwareRaid":true/false,
		         "status":"provisioned",
		         "powerState":"on",
		         "dateCreated":0000-00-00T00:00:00Z,
		         "lastAgentUpdate":0000-00-00T00:00:00Z,
		         "serverType":"value",
		         "osType":"value",
		         "commType":"value",
		         "managed":true/false,
		         "agentInstalled":true/false,
		         "toolsInstalled":true/false,
		         "hostname":value,
		         "domainName":value,
		         "fqdn":value,
		         "statusMessage":value,
		         "maxStorage":value,
		         "maxMemory":value,
		         "maxCores":value,
		         "macAddress":value,
		         "serverVendor":value,
		         "serverModel":value,
		         "serialNumber":value,
		         "tags":value,
		         "configId":value,
		         "configGroup":value,
		         "configRole":value,
		         "createdByUser":{
		            "username":"value",
		            "displayName":"value",
		            "firstName":"value",
		            "lastName":"value",
		            "email":"value",
		            "linuxUsername":"value",
		            "windowsUsername":"value"
		         },
		         "volumes":[
		            {
		               "id":value
		               "name":"root",
		               "deviceName":"value",
		               "maxStorage":value(bytes),
		               "unitNumber":value,
		               "displayOrder":value,
		               "rootVolume":true/false
		            }
		         ]
		      },
		      "ports":[
		         {
		            "index":0,
		            "external":value,
		            "internal":value,
		            "link":true/false,
		            "loadBalance":true/false,
		            "loadBalanceProtocol":value,
		            "export":true/false,
		            "exportName":value,
		            "displayName":"value",
		            "visible":true/false,
		            "primaryPort":true/false,
		            "protocol":value,
		            "name":"value"
		         }
		      ],
		      "portMap":{
		         "rpc":{
		            "index":0,
		            "external":value,
		            "internal":value,
		            "link":true/false,
		            "loadBalance":true/false,
		            "loadBalanceProtocol":value,
		            "export":true/false,
		            "exportName":value,
		            "displayName":"value",
		            "visible":true/false,
		            "primaryPort":true/false,
		            "protocol":value,
		            "name":"value"
		         }
		      },
		      "internalPort":value,
		      "externalPort":value
		   },
		   "apps":[

		   ]
		}
