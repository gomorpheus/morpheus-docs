# Policies

Provides API interfaces for managing Policies.

## Get All Policies

```shell
curl "https://api.gomorpheus.com/api/policies"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "policies": [
    {
      "id": 1,
      "name": null,
      "description": "global max containers",
      "policyType": {
        "id": 5,
        "code": "maxContainers",
        "name": "Max Containers"
      },
      "zone": null,
      "site": null,
      "user": null,
      "refType": null,
      "refId": null,
      "config": {
        "maxContainers": 999
      },
      "enabled": true,
      "owner": {
        "id": 1,
        "name": "root"
      },
      "accounts": [

      ]
    },
    {
      "id": 2,
      "name": null,
      "description": "dev budget",
      "policyType": {
        "id": 16,
        "code": "maxPrice",
        "name": "Budget"
      },
      "zone": null,
      "site": null,
      "user": null,
      "refType": null,
      "refId": null,
      "config": {
        "maxPrice": 1500,
        "maxPriceCurrency": "USD",
        "maxPriceUnit": "month"
      },
      "enabled": true,
      "owner": {
        "id": 1,
        "name": "root"
      },
      "accounts": [
        {
          "id": 2,
          "name": "dev"
        }
      ]
    },
    {
      "id": 3,
      "name": "test group maxcores",
      "description": null,
      "policyType": {
        "id": 3,
        "code": "maxCores",
        "name": "Max Cores"
      },
      "zone": null,
      "site": {
        "id": 2,
        "name": "test group"
      },
      "user": null,
      "refType": "ComputeSite",
      "refId": 1,
      "config": {
        "maxCores": 20
      },
      "enabled": true,
      "owner": {
        "id": 1,
        "name": "root"
      },
      "accounts": [

      ]
    },
    {
      "id": 4,
      "name": null,
      "description": "hulk max storage",
      "policyType": {
        "id": 2,
        "code": "maxStorage",
        "name": "Max Storage"
      },
      "zone": null,
      "site": null,
      "user": {
        "id": 26,
        "username": "hulk"
      },
      "refType": "User",
      "refId": 26,
      "config": {
        "maxStorage": 10000
      },
      "enabled": true,
      "owner": {
        "id": 1,
        "name": "root"
      },
      "accounts": [

      ]
    }
  ],
  "meta": {
    "size": 4,
    "total": 4,
    "offset": 0,
    "max": 25
  }
}
```

This endpoint retrieves all policies associated with the account.

### HTTP Request

`GET https://api.gomorpheus.com/api/policies`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name |  | If specified will return an exact match on name
phrase |  | If specified will return a partial match on name


## Get a Specific Policy


```shell
curl "https://api.gomorpheus.com/api/policies/4" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "policy": {
    "id": 4,
    "name": "hulk max storage",
    "description": "Limit the hulkster",
    "policyType": {
      "id": 2,
      "code": "maxStorage",
      "name": "Max Storage"
    },
    "zone": null,
    "site": null,
    "user": {
      "id": 26,
      "username": "hulk"
    },
    "refType": "User",
    "refId": 26,
    "config": {
      "maxStorage": "10000"
    },
    "enabled": true,
    "owner": {
      "id": 1,
      "name": "root"
    },
    "accounts": [
    ]
  }
}
```

This endpoint retrieves a specific policy.


### HTTP Request

`GET https://api.gomorpheus.com/api/policies/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the policy to retrieve


## Policy Types

```shell
curl "https://api.gomorpheus.com/api/policy-types" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "policyTypes": [
    {
      "id": 15,
      "code": "createBackup",
      "name": "Backup Creation",
      "description": "",
      "category": "provision",
      "loadMethod": "loadBackupCreation",
      "enforceMethod": "enforceBackupCreation",
      "prepareMethod": "prepareBackupCreation",
      "validateMethod": "validateBackupCreation",
      "enforceOnProvision": true,
      "enforceOnManaged": false,
      "optionTypes": [
        {
          "code": "policyType.createBackupType",
          "name": "Enforcement Type",
          "description": null,
          "type": "select",
          "displayOrder": 1,
          "optionSource": "policyGenericType",
          "defaultValue": "",
          "placeHolder": null,
          "helpBlock": "",
          "required": true,
          "fieldLabel": "Enforcement Type",
          "fieldName": "createBackupType",
          "fieldContext": "config"
        },
        {
          "code": "policyType.createBackup",
          "name": "Create Backup",
          "description": null,
          "type": "checkbox",
          "displayOrder": 2,
          "optionSource": null,
          "defaultValue": "",
          "placeHolder": null,
          "helpBlock": "",
          "required": true,
          "fieldLabel": "Create Backup",
          "fieldName": "createBackup",
          "fieldContext": "config"
        }
      ]
    }
  ],
  "meta": {
    "size": 16,
    "total": 16,
    "offset": 0,
    "max": 1000
  }
}
```

This endpoint returns a list of all policy types.

### HTTP Request

`GET https://api.gomorpheus.com/api/policy-types`

### Policy Type Options

##### Backup Creation (createBackup)

Parameter | Default | Description
--------- | ------- | -----------
config.createBackupType |  | Enforcement Type - [user, fixed]
config.createBackup | false | Create Backup [true, false]

##### Budget (maxPrice)

Parameter | Default | Description
--------- | ------- | -----------
config.maxPrice |  | Max Price: Maximum total price for all instances
config.maxPriceCurrency | USD | Currency code
config.maxPriceUnit | month | Unit of time [month, hour]

##### Expiration (lifecycle)

Parameter | Default | Description
--------- | ------- | -----------
config.lifecycleType | user | Expiration Type - [user, fixed]
config.lifecycleAge | 30 | Expiration Days - Configures the number of days the instance is allowed to exist before being removed.
config.lifecycleRenewal | 7 | Renewal Days - If the instance is renewed, this is the number of day increments the expiration date is increased by.
config.lifecycleNotify | 1 | Notification Days - This allows an email notice to be sent out x days before the instance is going to expire.
config.lifecycleMessage | Instance ${instance?.name} is set to expire on ${instance?.expireDate} | Notification Message
config.lifecycleAutoRenew | on | Allow Auto Extensions
config.lifecycleExtensionsBeforeApproval | 0 | Configures the number of extensions allowed before approval is required.
config.accountIntegrationId |  | Approval Integration ID
config.lifecycleWorkflowId |  | Approval Workflow ID

##### Host Name (serverNaming)

Parameter | Default | Description
--------- | ------- | -----------
config.serverNamingType |  | Naming Type - [user, fixed]
config.serverNamingPattern |  | Name pattern - uses ${variable} string interpolation.  Available variables are:<br>groupName, groupCode, cloudName, cloudCode, type, accountId, account, accountType, platform, username, userId, userInitials, provisionType
config.serverNamingConflict | false | Resolve Conflicts

##### Hostname (hostNaming)

Parameter | Default | Description
--------- | ------- | -----------
config.hostNamingType |  | Naming Type - [user, fixed]
config.hostNamingPattern |  | Name Pattern - uses ${variable} string interpolation.  Available variables are:<br>groupName, groupCode, cloudName, cloudCode, type, accountId, account, accountType, platform, username, userId, userInitials, provisionType

##### Instance Name(naming)

Parameter | Default | Description
--------- | ------- | -----------
config.namingType |  | Naming Type - [user, fixed]
config.namingPattern |  | Name pattern - uses ${variable} string interpolation.  Available variables are:<br>groupName, groupCode, cloudName, cloudCode, type, accountId, account, accountType, platform, username, userId, userInitials, provisionType
config.namingConflict | false | Resolve Conflicts

##### Max Containers (maxContainers)

Parameter | Default | Description
--------- | ------- | -----------
config.maxContainers |  | The max number of containers

##### Max Cores (maxCores)

Parameter | Default | Description
--------- | ------- | -----------
config.maxCores |  | The max number of cores

##### Max Hosts (maxHosts)

Parameter | Default | Description
--------- | ------- | -----------
config.maxHosts |  | The max number of hosts


##### Max Memory (maxMemory)

Parameter | Default | Description
--------- | ------- | -----------
config.maxMemory |  | The max number of memory (GB)

##### Max Storage (maxStorage)

Parameter | Default | Description
--------- | ------- | -----------
config.maxStorage |  | The max number of memory (GB)

##### Max VMs (maxVms)

Parameter | Default | Description
--------- | ------- | -----------
config.maxVms |  | The max number of virtual machines

##### Power Schedule (powerSchedule)

Parameter | Default | Description
--------- | ------- | -----------
config.powerScheduleType |  | Enforcement Type - [user, fixed]
config.powerSchedule |  | Power Schedule ID

##### Provision Approval (provisionApproval)

Parameter | Default | Description
--------- | ------- | -----------
config.accountIntegrationId |  | Account Integration ID
config.workflowId |  | Workflow ID

##### Shutdown (shutdown)

Parameter | Default | Description
--------- | ------- | -----------
config.shutdownType | user | Shutdown Type - [user, fixed]
config.shutdownAge | 30 | Shutdown Days - Configures the number of days the instance is allowed to exist before being removed.
config.shutdownRenewal | 7 | Renewal Days - If the instance is renewed, this is the number of day increments the expiration date is increased by.
config.shutdownNotify | 1 | Notification Days - This allows an email notice to be sent out x days before the instance is going to expire.
config.shutdownMessage | Instance ${instance?.name} is set to shutdown on ${instance?.shutdownDate} | Notification Message
config.shutdownAutoRenew | on | Allow Auto Extensions
config.shutdownExtensionsBeforeApproval | 0 | Configures the number of extensions allowed before approval is required.
config.accountIntegrationId |  | Approval Integration ID
config.lifecycleWorkflowId |  | Approval Workflow ID

##### User Creation (createUser)

Parameter | Default | Description
--------- | ------- | -----------
config.createUserType |  | Enforcement Type - [user, fixed]
config.createUser | false | Create User [true, false]


## Create a Policy

```shell
curl -XPOST "https://api.gomorpheus.com/api/policies" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "policy": {
    "name": "max hosts",
    "description": null,
    "policyType": {
      "code": "maxHosts"
    },
    "config": {
      "maxHosts": 99
    },
    "enabled": true,
    "accounts": []
  }
}'
```

> The above command returns JSON structured like getting a single policy: 

### HTTP Request

`POST https://api.gomorpheus.com/api/policies`


### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | A name for the policy
description      |  | A description for the policy
policyType.code      |  | The policy type.  [maxMemory, maxStorage, maxCores, maxContainers, etc.]
config      |  | A map of config values. The expected values vary by policyType. See [Policy Types](#policy-types).
enabled      | true | Enabled. Set to false to disable.
refType      |  | Scope object type. [ComputeSite, ComputeZone, User, Role]
refId      |  | Scope object ID, of group, cloud, user, etc.
accounts      |  | Array of tenants to scope the policy to.
eachUser      | false | Apply individually to each user in role, Only for policies scoped to a Role

### Create a Policy For a Group

Policies can be scoped to a group by passing the following:

Parameter | Value
--------- | -------
refType      | ComputeSite
refId      | The ID of the group

Alternatively, the [Group Policies](#group-policies) endpoint can be used.

### Create a Policy For a Cloud

Policies can be scoped to a cloud by passing the following:

Parameter | Value
--------- | -------
refType      | ComputeZone
refId      | The ID of the cloud

Alternatively, the [Cloud Policies](#cloud-policies) endpoint can be used.

### Create a Policy For a User

Policies can be scoped to a cloud by passing the following:

Parameter | Value
--------- | -------
refType      | User
refId      | The ID of the user

## Update a Policy

```shell
curl -XPUT "https://api.gomorpheus.com/api/policies/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "policy": {
    "name": "max containers 1000",
    "config": {
      "maxContainers": 1000
    },
  }
}'
```

> The above command returns JSON structured like getting a single policy: 

### HTTP Request

`PUT https://api.gomorpheus.com/api/policies/1`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the policy

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | A name for the policy
description      |  | A description for the policy
config      |  | A map of config values. The expected values vary by policyType.
enabled      | true | Enabled. Set to false to disable.
accounts      |  | Array of tenants to scope the policy to.

## Delete a Policy

```shell
curl -XDELETE "https://api.gomorpheus.com/api/policies/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

Will delete a policy from the system and make it no longer usable.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/policies/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the policy

## Group Policies

Policies scoped to a specific group can also be managed at another endpoint. 

```shell
curl "https://api.gomorpheus.com/api/groups/1/policies"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "policies": [
    {
      "id": 19,
      "name": "smallgroup max cores",
      "description": null,
      "policyType": {
        "id": 3,
        "code": "maxCores",
        "name": "Max Cores"
      },
      "zone": null,
      "site": {
        "id": 1,
        "name": "smallgroup"
      },
      "user": null,
      "refType": "ComputeSite",
      "refId": 1,
      "config": {
        "maxCores": 20
      },
      "enabled": true,
      "owner": {
        "id": 1,
        "name": "root"
      },
      "accounts": [
        
      ]
    }
  ],
  "meta": {
    "size": 1,
    "total": 1,
    "offset": 0,
    "max": 25
  }
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/groups/:groupId/policies`

### URL Parameters

Parameter | Description
--------- | -----------
groupId | The ID of the group

<aside class="info">
This resource also provides endpoints for GET, POST, PUT and DELETE that work just like the global policies endpoints.
</aside>

## Cloud Policies

Policies scoped to a specific cloud can also be managed at another endpoint. 

```shell
curl "https://api.gomorpheus.com/api/zones/1/policies"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "policies": [
    {
      "id": 19,
      "name": "bigcloud max cores",
      "description": null,
      "policyType": {
        "id": 3,
        "code": "maxCores",
        "name": "Max Cores"
      },
      "zone": {
        "id": 1,
        "name": "bigcloud"
      },
      "site": null,
      "user": null,
      "refType": "ComputeZone",
      "refId": 1,
      "config": {
        "maxCores": 1500
      },
      "enabled": true,
      "owner": {
        "id": 1,
        "name": "root"
      },
      "accounts": [
        
      ]
    }
  ],
  "meta": {
    "size": 1,
    "total": 1,
    "offset": 0,
    "max": 25
  }
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/zones/:cloudId/policies`

### URL Parameters

Parameter | Description
--------- | -----------
cloudId | The ID of the cloud

<aside class="info">
This resource also provides endpoints for GET, POST, PUT and DELETE that work just like the global policies endpoints.
</aside>
