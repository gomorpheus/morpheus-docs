# Check Groups

These entities define a collection of checks.

## Get All Check Groups

```shell
curl "https://api.gomorpheus.com/api/monitoring/groups"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "checkGroup": {
    "id": 191,
    "account": {
      "id": 1
    },
    "instance": {
      "id": 273,
      "name": "testapache100"
    },
    "name": "testapache100",
    "description": null,
    "inUptime": true,
    "lastCheckStatus": null,
    "lastWarningDate": null,
    "lastErrorDate": null,
    "lastSuccessDate": null,
    "lastRunDate": "2018-02-08T06:41:00+0000",
    "lastError": null,
    "outageTime": 0,
    "lastTimer": 6,
    "health": 0,
    "history": null,
    "minHappy": 1,
    "lastMetric": null,
    "severity": "critical",
    "createIncident": true,
    "createdBy": {
      "id": 1,
      "username": "james"
    },
    "dateCreated": "2018-02-01T07:24:21+0000",
    "lastUpdated": "2018-02-11T07:38:28+0000",
    "availability": 99.77698404,
    "checkType": {
      "id": 1,
      "code": "webGetCheck",
      "name": "Web Check",
      "metricName": "response"
    }
  },
  "checks": [
    {
      "id": 195,
      "account": {
        "id": 1
      },
      "active": true,
      "availability": 99.77698403,
      "checkAgent": null,
      "checkInterval": 300000,
      "checkSpec": null,
      "checkType": {
        "id": 1,
        "code": "webGetCheck",
        "name": "Web Check",
        "metricName": "response"
      },
      "config": {
        "webUrl": "http://localhost:80"
      },
      "container": {
        "id": 271
      },
      "createIncident": true,
      "createdBy": {
        "id": 1,
        "username": "james"
      },
      "dateCreated": "2018-02-01T07:24:21+0000",
      "description": null,
      "endDate": null,
      "health": 0,
      "inUptime": true,
      "lastBoxStats": null,
      "lastCheckStatus": "error",
      "lastError": "unheard from beyond check interval limit.",
      "lastErrorDate": "2018-02-08T06:41:00+0000",
      "lastMessage": null,
      "lastMetric": null,
      "lastRunDate": "2018-02-08T06:41:00+0000",
      "lastStats": null,
      "lastSuccessDate": "2018-02-08T06:33:52+0000",
      "lastTimer": 6,
      "lastUpdated": "2018-02-11T07:38:28+0000",
      "lastWarningDate": null,
      "name": "testapache100",
      "nextRunDate": "2018-02-08T06:46:00+0000",
      "outageTime": 0,
      "severity": "critical",
      "startDate": null
    }
  ]
}

```

This endpoint retrieves all check groups.

### HTTP Request

`GET https://api.gomorpheus.com/api/monitoring/groups`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
lastUpdated | null | Date filter, restricts query to only load checks updated  timestamp is more recent or equal to the date specified
deleted | undefined | Used to specify you can load previously deleted checks. Useful for synchronizing deleted records in your client side store.


<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>

## Get a Specific Check Group

```shell
curl "https://api.gomorpheus.com/api/monitoring/groups/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "checkGroup": {
    "id": 191,
    "account": {
      "id": 1
    },
    "instance": {
      "id": 273,
      "name": "testapache100"
    },
    "name": "testapache100",
    "description": null,
    "inUptime": true,
    "lastCheckStatus": null,
    "lastWarningDate": null,
    "lastErrorDate": null,
    "lastSuccessDate": null,
    "lastRunDate": "2018-02-08T06:41:00+0000",
    "lastError": null,
    "outageTime": 0,
    "lastTimer": 6,
    "health": 0,
    "history": null,
    "minHappy": 1,
    "lastMetric": null,
    "severity": "critical",
    "createIncident": true,
    "createdBy": {
      "id": 1,
      "username": "james"
    },
    "dateCreated": "2018-02-01T07:24:21+0000",
    "lastUpdated": "2018-02-11T07:38:28+0000",
    "availability": 99.77698404,
    "checkType": {
      "id": 1,
      "code": "webGetCheck",
      "name": "Web Check",
      "metricName": "response"
    }
  },
  "checks": [
    {
      "id": 195,
      "account": {
        "id": 1
      },
      "active": true,
      "availability": 99.77698403,
      "checkAgent": null,
      "checkInterval": 300000,
      "checkSpec": null,
      "checkType": {
        "id": 1,
        "code": "webGetCheck",
        "name": "Web Check",
        "metricName": "response"
      },
      "config": {
        "webUrl": "http://localhost:80"
      },
      "container": {
        "id": 271
      },
      "createIncident": true,
      "createdBy": {
        "id": 1,
        "username": "james"
      },
      "dateCreated": "2018-02-01T07:24:21+0000",
      "description": null,
      "endDate": null,
      "health": 0,
      "inUptime": true,
      "lastBoxStats": null,
      "lastCheckStatus": "error",
      "lastError": "unheard from beyond check interval limit.",
      "lastErrorDate": "2018-02-08T06:41:00+0000",
      "lastMessage": null,
      "lastMetric": null,
      "lastRunDate": "2018-02-08T06:41:00+0000",
      "lastStats": null,
      "lastSuccessDate": "2018-02-08T06:33:52+0000",
      "lastTimer": 6,
      "lastUpdated": "2018-02-11T07:38:28+0000",
      "lastWarningDate": null,
      "name": "testapache100",
      "nextRunDate": "2018-02-08T06:46:00+0000",
      "outageTime": 0,
      "severity": "critical",
      "startDate": null
    }
  ]
}
```

This endpoint retrieves a specific check.


### HTTP Request

`GET https://api.gomorpheus.com/api/monitoring/groups/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | ID of the check to retrieve

## Create a Check Group

```shell
curl -XPOST "https://api.gomorpheus.com/api/monitoring/groups" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"check":{
    "name": "My Check Group",
    "description": "A collection of checks",
    "checks": [5,6,7]
  }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single check 

### HTTP Request

`POST https://api.gomorpheus.com/api/monitoring/groups`

### JSON Check Group Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | Unique name scoped to your account for the check group
description |  | Optional description field
minHappy | 1 | Min Happy.  This specifies the minimum number of checks within the group that must be happy to keep the group from becoming unhealthy.
inUptime  | true | Used to determine if check should affect account wide availability calculations
severity  | critical | Determines the maximum severity level this group can incur on an incident when failing. Default is critical. They can be `info`, `warning`, or `critical`
active    | true | Used to determine if check group is active
checks | [] | Array of [Check](#checks) IDs

## Updating a Check Group

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/groups/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"checkGroup":{
    checks: [5,6,7,8,9]
  }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single check 

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/groups/:id`

### JSON Check Group Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | Unique name scoped to your account for the check group
description | null | Optional description field
inUptime  | true | Used to determine if check should affect account wide availability calculations
active    | true | Used to determine if check should be scheduled to execute
severity  | critical | Severity level of incidents that are created when this check fails. They can be `info`, `warning`, or `critical`
checks |  | Array of [Check](#checks) IDs

## Mute a Check Group

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/groups/1/mute" \
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

This endpoint can be used to toggle the mute state of a check on and off.

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/groups/:id/mute`

### JSON Parameters

Parameter | Default | Description
--------- | ----------- | -----------
enabled | true | Set to false to unmute


## Mute All Check Groups

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/groups/mute-all" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"enabled":true}'
```

> The above command returns JSON structure like this:

```json
{
  "muteState": "QUARANTINED",
  "updated": 20,
  "success": true
}
```

This endpoint can be used to toggle the mute state on and off for all checks.

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/groups/mute-all`

### JSON Parameters

Parameter | Default | Description
--------- | ----------- | -----------
enabled | true | Set to false to unmute

## Delete a Check Group

```shell
curl -XDELETE "https://api.gomorpheus.com/api/monitoring/groups/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

A deleted check group can be fetched from the API using the GET method to synchronize client side views, but can not be executed or updated.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/monitoring/groups/:id`

