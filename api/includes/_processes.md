# Process History

Provides API interfaces for viewing historical processes for instances.

## Get All Processes

```shell
curl "https://api.gomorpheus.com/api/processes" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "processes": [
    {
      "id": 250,
      "accountId": 1,
      "uniqueId": "cebc47ec-cb2f-417a-886e-dd60cf81db26",
      "processType": {
        "code": "provision",
        "name": "provision"
      },
      "description": null,
      "subType": null,
      "subId": null,
      "zoneId": 34,
      "integrationId": null,
      "instanceId": 238,
      "containerId": 240,
      "serverId": 601,
      "containerName": "apachetest",
      "displayName": "apachetest",
      "timerCategory": "vmware",
      "timerSubCategory": "28",
      "status": "failed",
      "reason": null,
      "percent": 100.0,
      "statusEta": 348246,
      "message": null,
      "output": null,
      "error": null,
      "startDate": "2018-09-28T19:10:56+0000",
      "endDate": "2018-09-28T20:21:49+0000",
      "duration": 4253127,
      "dateCreated": "2018-09-28T19:10:56+0000",
      "lastUpdated": "2018-09-28T20:21:49+0000",
      "createdBy": {
        "username": "admin",
        "displayName": "Admin"
      },
      "updatedBy": {
        "username": "admin",
        "displayName": "Admin"
      },
      "events": [

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

This endpoint retrieves all processes.

### HTTP Request

`GET https://api.gomorpheus.com/api/processes`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
phrase |  | If specified will return a partial match on displayName, message or output
instanceId |  | Filter by instance id(s)
containerId |  | Filter by container id(s)
serverId |  | Filter by server id(s)
zoneId |  | Filter by zone id(s)
appId |  | Filter by app id(s)


## Get a Specific Process

```shell
curl "https://api.gomorpheus.com/api/processes/250" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "process": {
    "id": 250,
    "accountId": 1,
    "uniqueId": "cebc47ec-cb2f-417a-886e-dd60cf81db26",
    "processType": {
      "code": "provision",
      "name": "provision"
    },
    "description": null,
    "subType": null,
    "subId": null,
    "zoneId": 34,
    "integrationId": null,
    "instanceId": 238,
    "containerId": 240,
    "serverId": 601,
    "containerName": "apachetest",
    "displayName": "apachetest",
    "timerCategory": "vmware",
    "timerSubCategory": "28",
    "status": "failed",
    "reason": null,
    "percent": 100.0,
    "statusEta": 348246,
    "message": null,
    "output": null,
    "error": null,
    "startDate": "2018-09-28T19:10:56+0000",
    "endDate": "2018-09-28T20:21:49+0000",
    "duration": 4253127,
    "dateCreated": "2018-09-28T19:10:56+0000",
    "lastUpdated": "2018-09-28T20:21:49+0000",
    "createdBy": {
      "username": "admin",
      "displayName": "Admin"
    },
    "updatedBy": {
      "username": "admin",
      "displayName": "Admin"
    },
    "events": [
      {
        "id": 940,
        "processId": 250,
        "accountId": 1,
        "uniqueId": "54bf6265-1e86-45b4-b1a7-d4b198b13c45",
        "processType": {
          "code": "provisionResources",
          "name": "prepare resources"
        },
        "description": null,
        "refType": "container",
        "refId": 240,
        "subType": null,
        "subId": null,
        "zoneId": 34,
        "integrationId": null,
        "instanceId": 238,
        "containerId": 240,
        "serverId": 601,
        "containerName": "apachetest",
        "displayName": "apachetest",
        "status": "complete",
        "reason": null,
        "percent": 100.0,
        "statusEta": 348246,
        "message": null,
        "output": null,
        "error": null,
        "startDate": "2018-09-28T19:10:56+0000",
        "endDate": "2018-09-28T19:10:57+0000",
        "duration": 921,
        "dateCreated": "2018-09-28T19:10:56+0000",
        "lastUpdated": "2018-09-28T19:10:57+0000",
        "createdBy": {
          "username": "admin",
          "displayName": "Admin"
        },
        "updatedBy": {
          "username": "admin",
          "displayName": "Admin"
        }
      },
      {
        "id": 941,
        "processId": 250,
        "accountId": 1,
        "uniqueId": "9a9791b7-0091-4ba7-be4d-e1586be3078c",
        "processType": {
          "code": "provisionImage",
          "name": "prepare image"
        },
        "description": null,
        "refType": "container",
        "refId": 240,
        "subType": null,
        "subId": null,
        "zoneId": 34,
        "integrationId": null,
        "instanceId": 238,
        "containerId": 240,
        "serverId": 601,
        "containerName": "apachetest",
        "displayName": "apachetest",
        "status": "complete",
        "reason": null,
        "percent": 100.0,
        "statusEta": 348246,
        "message": null,
        "output": null,
        "error": null,
        "startDate": "2018-09-28T19:10:57+0000",
        "endDate": "2018-09-28T19:11:01+0000",
        "duration": 3645,
        "dateCreated": "2018-09-28T19:10:57+0000",
        "lastUpdated": "2018-09-28T19:11:01+0000",
        "createdBy": {
          "username": "admin",
          "displayName": "Admin"
        },
        "updatedBy": {
          "username": "admin",
          "displayName": "Admin"
        }
      },
      {
        "id": 942,
        "processId": 250,
        "accountId": 1,
        "uniqueId": "f1905796-9387-4983-ae0d-0fee5bb81f56",
        "processType": {
          "code": "provisionConfig",
          "name": "configure instance"
        },
        "description": null,
        "refType": "container",
        "refId": 240,
        "subType": null,
        "subId": null,
        "zoneId": 34,
        "integrationId": null,
        "instanceId": 238,
        "containerId": 240,
        "serverId": 601,
        "containerName": "apachetest",
        "displayName": "apachetest",
        "status": "complete",
        "reason": null,
        "percent": 100.0,
        "statusEta": 348246,
        "message": null,
        "output": null,
        "error": null,
        "startDate": "2018-09-28T19:11:01+0000",
        "endDate": "2018-09-28T19:11:01+0000",
        "duration": 28,
        "dateCreated": "2018-09-28T19:11:01+0000",
        "lastUpdated": "2018-09-28T19:11:01+0000",
        "createdBy": {
          "username": "admin",
          "displayName": "Admin"
        },
        "updatedBy": {
          "username": "admin",
          "displayName": "Admin"
        }
      },
      {
        "id": 943,
        "processId": 250,
        "accountId": 1,
        "uniqueId": "599a0c2d-491c-4178-8b86-55b6d019d48c",
        "processType": {
          "code": "provisionDeploy",
          "name": "deploy instance"
        },
        "description": null,
        "refType": "container",
        "refId": 240,
        "subType": null,
        "subId": null,
        "zoneId": 34,
        "integrationId": null,
        "instanceId": 238,
        "containerId": 240,
        "serverId": 601,
        "containerName": "apachetest",
        "displayName": "apachetest",
        "status": "complete",
        "reason": null,
        "percent": 100.0,
        "statusEta": 348246,
        "message": null,
        "output": null,
        "error": null,
        "startDate": "2018-09-28T19:11:01+0000",
        "endDate": "2018-09-28T19:11:33+0000",
        "duration": 32219,
        "dateCreated": "2018-09-28T19:11:01+0000",
        "lastUpdated": "2018-09-28T19:11:33+0000",
        "createdBy": {
          "username": "admin",
          "displayName": "Admin"
        },
        "updatedBy": {
          "username": "admin",
          "displayName": "Admin"
        }
      },
      {
        "id": 944,
        "processId": 250,
        "accountId": 1,
        "uniqueId": "4f4088b0-7043-4a35-82c1-00456643beaa",
        "processType": {
          "code": "provisionResize",
          "name": "resize instance"
        },
        "description": null,
        "refType": "container",
        "refId": 240,
        "subType": null,
        "subId": null,
        "zoneId": 34,
        "integrationId": null,
        "instanceId": 238,
        "containerId": 240,
        "serverId": 601,
        "containerName": "apachetest",
        "displayName": "apachetest",
        "status": "complete",
        "reason": null,
        "percent": 100.0,
        "statusEta": 348246,
        "message": null,
        "output": null,
        "error": null,
        "startDate": "2018-09-28T19:11:33+0000",
        "endDate": "2018-09-28T19:11:36+0000",
        "duration": 2896,
        "dateCreated": "2018-09-28T19:11:33+0000",
        "lastUpdated": "2018-09-28T19:11:36+0000",
        "createdBy": {
          "username": "admin",
          "displayName": "Admin"
        },
        "updatedBy": {
          "username": "admin",
          "displayName": "Admin"
        }
      },
      {
        "id": 945,
        "processId": 250,
        "accountId": 1,
        "uniqueId": "10559e2a-6980-4443-afd4-37b7471492ba",
        "processType": {
          "code": "provisionCloudInit",
          "name": "configure cloud init"
        },
        "description": null,
        "refType": "container",
        "refId": 240,
        "subType": null,
        "subId": null,
        "zoneId": 34,
        "integrationId": null,
        "instanceId": 238,
        "containerId": 240,
        "serverId": 601,
        "containerName": "apachetest",
        "displayName": "apachetest",
        "status": "complete",
        "reason": null,
        "percent": 100.0,
        "statusEta": 348246,
        "message": null,
        "output": null,
        "error": null,
        "startDate": "2018-09-28T19:11:36+0000",
        "endDate": "2018-09-28T19:11:42+0000",
        "duration": 6152,
        "dateCreated": "2018-09-28T19:11:36+0000",
        "lastUpdated": "2018-09-28T19:11:42+0000",
        "createdBy": {
          "username": "admin",
          "displayName": "Admin"
        },
        "updatedBy": {
          "username": "admin",
          "displayName": "Admin"
        }
      },
      {
        "id": 946,
        "processId": 250,
        "accountId": 1,
        "uniqueId": "0081e523-bfea-4664-b582-d68076943a46",
        "processType": {
          "code": "provisionLaunch",
          "name": "power on"
        },
        "description": null,
        "refType": "container",
        "refId": 240,
        "subType": null,
        "subId": null,
        "zoneId": 34,
        "integrationId": null,
        "instanceId": 238,
        "containerId": 240,
        "serverId": 601,
        "containerName": "apachetest",
        "displayName": "apachetest",
        "status": "complete",
        "reason": null,
        "percent": 100.0,
        "statusEta": 348246,
        "message": null,
        "output": null,
        "error": null,
        "startDate": "2018-09-28T19:11:42+0000",
        "endDate": "2018-09-28T19:11:45+0000",
        "duration": 2549,
        "dateCreated": "2018-09-28T19:11:42+0000",
        "lastUpdated": "2018-09-28T19:11:45+0000",
        "createdBy": {
          "username": "admin",
          "displayName": "Admin"
        },
        "updatedBy": {
          "username": "admin",
          "displayName": "Admin"
        }
      },
      {
        "id": 947,
        "processId": 250,
        "accountId": 1,
        "uniqueId": "de66729e-9580-43b0-950c-f2769cd86790",
        "processType": {
          "code": "provisionNetwork",
          "name": "network wait"
        },
        "description": null,
        "refType": "container",
        "refId": 240,
        "subType": null,
        "subId": null,
        "zoneId": 34,
        "integrationId": null,
        "instanceId": 238,
        "containerId": 240,
        "serverId": 601,
        "containerName": "apachetest",
        "displayName": "apachetest",
        "status": "failed",
        "reason": null,
        "percent": 100.0,
        "statusEta": 348246,
        "message": null,
        "output": null,
        "error": null,
        "startDate": "2018-09-28T19:11:45+0000",
        "endDate": "2018-09-28T20:21:49+0000",
        "duration": 4204122,
        "dateCreated": "2018-09-28T19:11:45+0000",
        "lastUpdated": "2018-09-28T20:21:49+0000",
        "createdBy": {
          "username": "admin",
          "displayName": "Admin"
        },
        "updatedBy": {
          "username": "admin",
          "displayName": "Admin"
        }
      }
    ]
  }
}
```

This endpoint retrieves a specific process.

### HTTP Request

`GET https://api.gomorpheus.com/api/processes/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the process


## Get a Specific Process Event

```shell
curl "https://api.gomorpheus.com/api/processes/events/940" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "processEvent": {
    "id": 940,
    "processId": 250,
    "accountId": 1,
    "uniqueId": "54bf6265-1e86-45b4-b1a7-d4b198b13c45",
    "processType": {
      "code": "provisionResources",
      "name": "prepare resources"
    },
    "description": null,
    "refType": "container",
    "refId": 240,
    "subType": null,
    "subId": null,
    "zoneId": 34,
    "integrationId": null,
    "instanceId": 238,
    "containerId": 240,
    "serverId": 601,
    "containerName": "apachetest",
    "displayName": "apachetest",
    "status": "complete",
    "reason": null,
    "percent": 100.0,
    "statusEta": 348246,
    "message": null,
    "output": null,
    "error": null,
    "startDate": "2018-09-28T19:10:56+0000",
    "endDate": "2018-09-28T19:10:57+0000",
    "duration": 921,
    "dateCreated": "2018-09-28T19:10:56+0000",
    "lastUpdated": "2018-09-28T19:10:57+0000",
    "createdBy": {
      "username": "admin",
      "displayName": "Admin"
    },
    "updatedBy": {
      "username": "admin",
      "displayName": "Admin"
    }
  }
}
```

This endpoint retrieves a specific process event.

### HTTP Request

`GET https://api.gomorpheus.com/api/processes/events/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the process event


