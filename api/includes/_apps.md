# Apps

Apps are groupings of instances that are linked together to form a full application stack. They can be created with existing templates or new templates, as well as from existing instances.

## Get All Apps

```shell
curl "https://api.gomorpheus.com/api/apps"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "apps": [
    {
      "id": 1,
      "name": "My Test App",
      "description": "Sample Description",
      "accountId": 1,
      "account": {
        "id": 1,
        "name": "root"
      },
      "siteId": 1,
      "group": {
        "id": 1,
        "name": "My Group"
      },
      "blueprint": {
        "id": 135,
        "name": "Grails Example",
        "type": "morpheus"
      },
      "status": "running",
      "instanceCount": 2,
      "containerCount": 2,
      "dateCreated": "2015-06-09T20:59:17Z",
      "lastUpdated": "2015-06-09T21:00:19Z",
      "appTiers": [
        {
          "tier": {
            "id": 2,
            "name": "App"
          },
          "appInstances": [
            {
              "instance": {
                "id": 53,
                "name": "Test App - Grails"
              }
            }
          ]
        },
        {
          "tier": {
            "id": 5,
            "name": "Database"
          },
          "appInstances": [
            {
              "instance": {
                "id": 54,
                "name": "Test App - MySQL"
              }
            }
          ]
        }
      ],
      "stats": {
        "usedMemory": 0,
        "maxMemory": 1073741824,
        "usedStorage": 0,
        "maxStorage": 21474836480,
        "running": 0,
        "total": 0,
        "cpuUsage": 0,
        "instanceCount": 2
      }
    }
  ],
  "meta": {
    "offset": 0,
    "max": 25,
    "size": 1,
    "total": 1
  }
}
```

This endpoint retrieves all apps and the correlated instances. Server data is encrypted in the database.

### HTTP Request

`GET https://api.gomorpheus.com/api/apps`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
name | null | Filter by name
phrase | null | Filter by wildcard search of name and description
createdBy | null | Filter by Created By (User) ID. Accepts multiple values.

## Get a Specific App


```shell
curl "https://api.gomorpheus.com/api/apps/4" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "app": {
    "id": 1,
    "name": "My Test App",
    "description": "Sample Description",
    "accountId": 1,
    "account": {
      "id": 1,
      "name": "root"
    },
    "siteId": 1,
    "group": {
      "id": 1,
      "name": "My Group"
    },
    "blueprint": {
      "id": 135,
      "name": "Grails Example",
      "type": "morpheus"
    },
    "status": "running",
    "instanceCount": 2,
    "containerCount": 2,
    "dateCreated": "2015-06-09T20:59:17Z",
    "lastUpdated": "2015-06-09T21:00:19Z",
    "appTiers": [
      {
        "tier": {
          "id": 2,
          "name": "App"
        },
        "appInstances": [
          {
            "instance": {
              "id": 53,
              "name": "Test App - Grails"
            }
          }
        ]
      },
      {
        "tier": {
          "id": 5,
          "name": "Database"
        },
        "appInstances": [
          {
            "instance": {
              "id": 54,
              "name": "Test App - MySQL"
            }
          }
        ]
      }
    ],
    "stats": {
      "usedMemory": 0,
      "maxMemory": 1073741824,
      "usedStorage": 0,
      "maxStorage": 21474836480,
      "running": 0,
      "total": 0,
      "cpuUsage": 0,
      "instanceCount": 2
    }
  }
}
```

This endpoint retrieves a specific app.

### HTTP Request

`GET https://api.gomorpheus.com/api/apps/:id`


## Create an App

```shell
curl -XPOST "https://api.gomorpheus.com/api/apps" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"app":{
    "name": "sampleapp",
    "description": "A sample app",
    "group": {
      "id": 1
    }
  }}'
```

> The above command returns JSON structured like getting a single app.

### HTTP Request

`POST https://api.gomorpheus.com/api/apps`

### JSON App Parameters

Parameter | Default | Description
--------- | ------- | -----------
name  | null | A name for the app
description     | null | Optional description field
group | null | A Map containing the id of the Group


## Updating an App Name or Description

```shell
curl -XPUT "https://api.gomorpheus.com/api/apps/2" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"app":{
    "name": "My Sample App",
    "description": "A new description of this app",
  }}'
```

> The above command returns JSON structured like getting a single app.

### HTTP Request

`PUT https://api.gomorpheus.com/api/apps/:id`

### JSON App Parameters

Parameter | Default | Description
--------- | ------- | -----------
name  | null | A name for the app
description     | null | Optional description field


## Add Existing Instance to App

```shell
curl -XPOST "https://api.gomorpheus.com/api/apps/1/add-instance" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"instanceId": 55, tierName: "App"}'
```

> The above command returns JSON structured like getting a single app.

### HTTP Request

`POST https://api.gomorpheus.com/api/apps/:id/add-instance`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
instanceId  | null | The ID of the instance being added
tierName     | null | The Name of the Tier


## Remove Instance from App

```shell
curl -XPOST "https://api.gomorpheus.com/api/apps/1/remove-instance" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"instanceId": 55}'
```

> The above command returns JSON structured like getting a single app.

### HTTP Request

`POST https://api.gomorpheus.com/api/apps/:id/remove-instance`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
instanceId  | null | The ID of the instance being removed


## Get Security Groups

```shell
curl -XGET "https://api.gomorpheus.com/api/apps/1/security-groups" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true,
  "firewallEnabled": true,
  "securityGroups": [
    {
      "id": 19,
      "accountId": 1,
      "name": "All Tomcat Access",
      "description": "Allow everyone to access Tomcat"
    }
  ]
}
```

This returns a list of all of the security groups applied to an app and whether the firewall is enabled.

### HTTP Request

`GET https://api.gomorpheus.com/api/apps/:id/security-groups`


## Set Security Groups

```shell
curl -XPOST "https://api.gomorpheus.com/api/apps/1/security-groups" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "securityGroupIds": [19, 2] }'
```

> The above command returns JSON structure similar to the 'get' of security groups.

### HTTP Request

`POST https://api.gomorpheus.com/api/apps/:id/security-groups`

### JSON Parameters

Parameter   | Default | Description
---------   | ------- | -----------
securityGroupIds | null | List of all security groups ids which should be applied.  If no security groups should apply, pass '[]'

## Delete an App

```shell
curl -XDELETE "https://api.gomorpheus.com/api/apps/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete an app. 
Use `removeInstances=on` to also delete the instances in the app and all associated monitors and backups.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/apps/:id`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
removeInstances | off | Remove Instances
preserveVolumes | off | Preserve Volumes
keepBackups | off | Preserve copy of backups
releaseEIPs | on | Release EIPs
force | off | Force Delete
