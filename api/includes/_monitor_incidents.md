# Monitor Incidents

These entities are incidents that result from [Checks](#monitor-checks). The API provides a means to list all of an account's incidents and also update, mute, close, and reopen them.

## Get All Incidents

```shell
curl "https://api.gomorpheus.com/api/monitoring/incidents"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "incidents": [
    {
      "id": 12,
      "account": {
        "id": 1
      },
      "app": null,
      "autoClose": true,
      "channelId": "cdff5f78-19df-41e0-b6dc-2ab87cedeae5",
      "checkGroups": [

      ],
      "checks": [

      ],
      "comment": "",
      "displayName": "test-mysql",
      "duration": null,
      "endDate": null,
      "inUptime": true,
      "lastCheckTime": "2017-02-22T00:04:56+0000",
      "lastError": "unheard from beyond check interval limit.",
      "lastMessage": null,
      "name": "test-mysql",
      "resolution": "A network outage was resolved.",
      "severity": "critical",
      "severityId": 20,
      "startDate": "2017-02-22T00:04:56+0000",
      "status": "open",
      "visibility": "private"
    }
  ],
  "meta": {
    "offset": 0,
    "max": 25,
    "size": 25,
    "total": 63
  }
}
```

This endpoint retrieves all incidents.

### HTTP Request

`GET https://api.gomorpheus.com/api/monitoring/incidents`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
status | null | Filter by status
severity | null | Filter by severity

## Get a Specific Incident


```shell
curl "https://api.gomorpheus.com/api/monitoring/incidents/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "incident": {
    "id": 1,
    "account": {
      "id": 1
    },
    "app": null,
    "autoClose": true,
    "channelId": "3f2fb251-9f87-4e28-88f7-7e0df24f4d50",
    "checkGroups": [
      {
        "id": 129,
        "name": "test-nginx"
      }
    ],
    "checks": [

    ],
    "comment": null,
    "displayName": "test-nginx",
    "duration": null,
    "endDate": "2018-03-26T11:00:34+0000",
    "inUptime": true,
    "lastCheckTime": "2018-03-23T23:06:03+0000",
    "lastError": "unheard from beyond check interval limit.",
    "lastMessage": null,
    "name": "test-nginx",
    "resolution": null,
    "severity": "critical",
    "severityId": 20,
    "startDate": "2018-03-23T23:06:03+0000",
    "status": "closed",
    "visibility": "private"
  },
  "issues": [
    {
      "id": 178,
      "attachmentType": "Group",
      "app": null,
      "available": false,
      "check": null,
      "checkGroup": {
        "id": 129,
        "name": "test-nginx"
      },
      "checkStatus": null,
      "endDate": "2018-03-26T11:00:33+0000",
      "health": 0,
      "inUptime": true,
      "incident": {
        "id": 41
      },
      "lastCheckTime": null,
      "lastError": null,
      "lastMessage": null,
      "name": "test-nginx",
      "severity": "critical",
      "severityId": 10,
      "startDate": "2018-03-23T23:06:03+0000",
      "status": "closed"
    }
  ]
}
```

This endpoint retrieves a specific incident.


### HTTP Request

`GET https://api.gomorpheus.com/api/monitoring/incidents/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | ID of the incident to retrieve

## Updating an Incident

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/incidents/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"incident":{
    "resolution": "We fixed the problem",
  }}'
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

This endpoint can be used to update certain properties of an incident.

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/incidents/:id`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
resolution | null | Description of the resolution to this incident
comment | null | Comment on this incident
status | null | Set status (open or closed)
severity | null | Set severity (critical, warning or info)
name | null | Set display name(subject)
startDate | null | Set start time
endDate | null | Set end time


## Mute an Incident

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/incidents/1/mute" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"enabled":true}'
```

> The above command returns JSON structure like this:

```json
{
  "muteState": "QUARANTINED",
  "success": true
}
```

This endpoint can be used to toggle the mute state (`inUptime`) of an incident on and off.

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/incidents/:id/mute`

### JSON Parameters

Parameter | Default | Description
--------- | ----------- | -----------
enabled | true | Set to false to unmute


## Mute All Incidents

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/incidents/mute-all" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"enabled":true}'
```

> The above command returns JSON structure like this:

```json
{
  "muteState": "QUARANTINED",
  "updated": 11,
  "success": true
}
```

This endpoint can be used to toggle the mute state (`inUptime`) of all open incidents.

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/incidents/mute-all`

### JSON Parameters

Parameter | Default | Description
--------- | ----------- | -----------
enabled | true | Set to false to unmute

## Close an Incident

```shell
curl -XDELETE "https://api.gomorpheus.com/api/monitoring/incidents/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true,
  "msg": "Incident 1 is closed"
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/monitoring/incidents/:id`


## Reopen an Incident

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/incidents/1/reopen" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{}'
```

> The above command returns JSON structure like this:

```json
{
  "success": true,
  "msg": "Incident 1 is now open again"
}
```

This endpoint can be used to toggle the mute state (`inUptime`) of an incident on and off.

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/incidents/:id/reopen`


