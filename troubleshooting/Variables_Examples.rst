.. _${variable}:

Variables
=========

The following are the map structures passed to scripts and templates during provisioning inside of a ``<%= %>`` block.

Variables can also be passed in Naming Policies using ``${ }`` block.

.. IMPORTANT:: Variables are case sensitive

PowerShell Example: ``$app_id = "<%= instance.metadata.app_id %>"``

Bash Example:	``HOSTNAME="<%= container.server.hostname %>"``

Python Example: ``hostname = container['server']['hostname']``

HTTP Body Example: ``{"name": "<%= instance.createdByUsername %>"}``

Instance Naming Policy example: ``${userInitials}-${cloudCode}-${platform == 'windows' ? 'W' : 'L'}-${sequence}``

.. TIP:: Variables can be extremely useful when utilized in the environment tab, metadata, and environment variables.

.. image:: /images/troubleshooting/Metadata-Enviornment-Variable-Spot

.. image:: /images/troubleshooting/Tags-Variable-Spot

.. NOTE:: customOptions values are defined from custom Option Types.

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
			instance.instanceContext: <%=instance.instanceContext%>
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
			zone.datacenterId: <%=zone.datacenterId%>
			zone.domainName: <%=zone.domainName%>
			zone.firewallEnabled: <%=zone.firewallEnabled%>
			zone.location: <%=zone.location%>
			zone.name: <%=zone.name%>
			zone.regionCode: <%=zone.regionCode%>
			zone.scalePriority: <%=zone.scalePriority%>
			cypher: <%=cypher.read('secret/hello')%>


.. code-block:: bash

	instance {
		autoScale,
		configGroup,
		configId,
		configRole
		containers:[],
		cores,
		deployGroup,
		description,
		displayName,
		domainName,
		environmentPrefix,
		evars:[],
		expireDate,
		firewallEnabled,
		hostname,
		instanceContext,
		instanceLevel,
		instanceTypeCode,
		instanceVersion,
		memory,
		metadata:[],
		name,
		networkLevel,
		plan,
		provisionType,
		status,
		statusMessage,
		storage,
		tags,
		tenantSubdomain,
		userStatus,
		instanceTypeName
	}

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

.. code-block:: bash

	group {
		code,
		location,
		datacenterId,
		name
	}

.. code-block:: bash

	customOptions {
		customOptions.fieldName
	}
