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



.. NOTE:: customOptions are user defined as Option Types or Option Lists in custom Library items.

.. code-block:: bash

	cypher: <%=cypher.read('secret/hello')%>
	customOptions: <%=customOptions.fieldName%>
	evar: <%=evars.name%>
	evars: <%=evars%>
	instance.metadata: <%=instance.metadata%>
	instance.instanceTypeName: <%=instance.instanceTypeName%>
	instance.instanceTypeCode: <%=instance.instanceTypeCode%>
	instance.provisionType: <%=instance.provisionType%>
	instance.instanceVersion: <%=instance.instanceVersion%>
	instance.plan: <%=instance.plan%>
	instance.name: <%=instance.name%>
	instance.displayName: <%=instance.displayName%>
	instance.description: <%=instance.description%>
	instance.environmentPrefix: <%=instance.environmentPrefix%>
	instance.hostname: <%=instance.hostname%>
	instance.domainName: <%=instance.domainName%>
	instance.firewallEnabled: <%=instance.firewallEnabled%>
	instance.status: <%=instance.status%>
	instance.userStatus: <%=instance.userStatus%>
	instance.networkLevel: <%=instance.networkLevel%>
	instance.instanceLevel: <%=instance.instanceLevel%>
	instance.deployGroup: <%=instance.deployGroup%>
	instance.instanceContext: <%=instance.instanceContext%>
	instance.autoScale: <%=instance.autoScale%>
	instance.statusMessage: <%=instance.statusMessage%>
	instance.expireDate: <%=instance.expireDate%>
	instance.tags: <%=instance.tags%>
	instance.storage: <%=instance.storage%>
	instance.memory: <%=instance.memory%>
	instance.cores: <%=instance.cores%>
	instance.configId: <%=instance.configId%>
	instance.configGroup: <%=instance.configGroup%>
	instance.configRole: <%=instance.configRole%>
	instance.containers[0]: <%=instance.containers[0].containerTypeName%>
	instance.createdBYUsername: <%=instance.createdByUsername%>
	instance.createdByEmail: <%=instance.createdByEmail%>
	instance.createdByFirstName: <%=instance.createdByFirstName%>
	instance.createdByLastName: <%=instance.createdByLastName%>
	instance.createdById: <%=instance.createdById%>
	container.containerTypeName: <%=container.containerTypeName%>
	container.containerTypeCode: <%=container.containerTypeCode%>
	container.containerTypeShortName: <%=container.containerTypeShortName%>
	container.provisionType: <%=container.provisionType%>
	container.dataPath: <%=container.dataPath%>
	container.logsPath: <%=container.logsPath%>
	container.configPath: <%=container.configPath%>
	container.planCode: <%=container.planCode%>
	container.dateCreated: <%=container.dateCreated%>
	container.status: <%=container.status%>
	container.environmentPrefix: <%=container.environmentPrefix%>
	container.version: <%=container.version%>
	container.image: <%=container.image%>
	container.internalHostname: <%=container.internalHostname%>
	container.hostname: <%=container.hostname%>
	container.domainName: <%=container.domainName%>
	container.storage: <%=container.storage%>
	container.memory: <%=container.memory%>
	container.cores: <%=container.cores%>
	container.internalIp: <%=container.internalIp%>
	container.externalIp: <%=container.externalIp%>
	container.sshHost: <%=container.sshHost%>
	container.hostMountPoint: <%=container.hostMountPoint%>
	container.configId: <%=container.configId%>
	container.configGroup: <%=container.configGroup%>
	container.configRole: <%=container.configRole%>
	container.serverId: <%=container.serverId%>
	container.server: <%=container.server.serverTypeName%>
	server.serverTypeName: <%=server.serverTypeName%>
	server.serverTypeCode: <%=server.serverTypeCode%>
	server.parentServerId: <%=server.parentServerId%>
	server.plan: <%=server.plan%>
	server.visibility: <%=server.visibility%>
	server.osTypeCode: <%=server.osTypeCode%>
	server.sourceImageId: <%=server.sourceImageId%>
	server.name: <%=server.name%>
	server.displayName: <%=server.displayName%>
	server.internalName: <%=server.internalName%>
	server.category: <%=server.category%>
	server.description: <%=server.description%>
	server.internalId: <%=server.internalId%>
	server.externalId: <%=server.externalId%>
	server.platform: <%=server.platform%>
	server.platformVersion: <%=server.platformVersion%>
	server.agentVersion: <%=server.agentVersion%>
	server.nodePackageVersion: <%=server.nodePackageVersion%>
	server.sshHost: <%=server.sshHost%>
	server.sshPort: <%=server.sshPort%>
	server.sshUsername: <%=server.sshUsername%>
	server.consoleType: <%=server.consoleType%>
	server.consoleHost: <%=server.consoleHost%>
	server.consolePort: <%=server.consolePort%>
	server.consoleUsername: <%=server.consoleUsername%>
	server.internalSshUsername: <%=server.internalSshUsername%>
	server.internalIp: <%=server.internalIp%>
	server.externalIp: <%=server.externalIp%>
	server.osDevice: <%=server.osDevice%>
	server.dataDevice: <%=server.dataDevice%>
	server.lvmEnabled: <%=server.lvmEnabled%>
	server.apiKey: <%=server.apiKey%>
	server.softwareRaid: <%=server.softwareRaid%>
	server.status: <%=server.status%>
	server.powerState: <%=server.powerState%>
	server.dateCreated: <%=server.dateCreated%>
	server.lastAgentUpdate: <%=server.lastAgentUpdate%>
	server.serverType: <%=server.serverType%>
	server.osType: <%=server.osType%>
	server.commType: <%=server.commType%>
	server.managed: <%=server.managed%>
	server.agentInstalled: <%=server.agentInstalled%>
	server.toolsInstalled: <%=server.toolsInstalled%>
	server.hostname: <%=server.hostname%>
	server.domainName: <%=server.domainName%>
	server.statusMessage: <%=server.statusMessage%>
	server.maxStorage: <%=server.maxStorage%>
	server.maxMemory: <%=server.maxMemory%>
	server.maxCores: <%=server.maxCores%>
	server.macAddress: <%=server.macAddress%>
	server.serverVendor: <%=server.serverVendor%>
	server.serverModel: <%=server.serverModel%>
	server.serialNumber: <%=server.serialNumber%>
	server.tags: <%=server.tags%>
	server.configId: <%=server.configId%>
	server.configGroup: <%=server.configGroup%>
	server.configRole: <%=server.configRole%>
	task.results (using task code): <%=results.taskCode%>
	task.results (using task name): <%=results["Task Name"]%>
	task.results.value: <%=results.taskCode.key%>
	zone.name: <%=zone.name%>
	zone.code: <%=zone.code%>
	zone.location: <%=zone.location%>
	zone.cloudTypeName: <%=zone.cloudTypeName%>
	zone.cloudTypeCode: <%=zone.cloudTypeCode%>
	zone.domainName: <%=zone.domainName%>
	zone.scalePriority: <%=zone.scalePriority%>
	zone.firewallEnabled: <%=zone.firewallEnabled%>
	zone.regionCode: <%=zone.regionCode%>
	zone.agentMode: <%=zone.agentMode%>
	zone.datacenterId: <%=zone.datacenterId%>
	group.code: <%=group.code%>
	group.name: <%=group.name%>
	group.location: <%=group.location%>
	group.datacenterId: <%=group.datacenterId%>


.. code-block:: bash

	instance {
		instanceTypeName,
		instanceTypeCode,
		provisionType,
		instanceVersion,
		tenantSubdomain,
		plan,
		name,
		displayName,
		description,
		environmentPrefix,
		hostname,
		domainName,
		firewallEnabled,
		status,
		userStatus,
		networkLevel,
		instanceLevel,
		deployGroup,
		instanceContext,
		autoScale,
		statusMessage,
		expireDate,
		tags,
		storage,
		memory,
		cores,
		configId,
		configGroup,
		configRole
		containers:[],
		metadata:[],
		evars:[]
	}

.. code-block:: bash

	container {
		containerTypeName,
		containerTypeCode,
		containerTypeShortName,
		provisionType,
		dataPath,
		logsPath,
		configPath,
		planCode,
		dateCreated,
		status,
		environmentPrefix,
		version,
		image,
		internalHostname,
		hostname,
		domainName,
		storage,
		memory,
		cores,
		internalIp,
		externalIp,
		sshHost,
		hostMountPoint,
		configId,
		configGroup,
		configRole,
		serverId,
		server:{}
	}

.. code-block:: bash

	server {
		serverTypeName,
		serverTypeCode,
		parentServerId,
		plan,
		visibility,
		osTypeCode,
		sourceImageId,
		name,
		displayName,
		internalName,
		category,
		description
		internalId,
		externalId,
		platform,
		platformVersion,
		agentVersion,
		nodePackageVersion,
		sshHost,
		sshPort,
		sshUsername,
		consoleType,
		consoleHost,
		consolePort,
		consoleUsername,
		internalSshUsername,
		internalIp,
		externalIp,
		osDevice,
		dataDevice,
		lvmEnabled,
		apiKey,
		softwareRaid,
		status,
		powerState,
		dateCreated,
		lastAgentUpdate,
		serverType,
		osType,
		commType,
		managed,
		agentInstalled,
		toolsInstalled,
		hostname,
		domainName,
		statusMessage,
		maxStorage,
		maxMemory,
		maxCores,
		macAddress,
		serverVendor,
		serverModel,
		serialNumber,
		tags,
		configId,
		configGroup,
		configRole
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
		name,
		code,
		location,
		cloudTypeName,
		cloudTypeCode,
		domainName,
		scalePriority,
		firewallEnabled,
		regionCode,
		agentMode,
		datacenterId
	}

.. code-block:: bash

	group {
		code,
		name,
		location,
		datacenterId
	}

.. code-block:: bash

	customOptions {
		customOptions.fieldName
	}
