# Execute Schedules

Execute Schedules are definitions for recurring schedules. These schedules can be used in your backup jobs.

## Get All Execute Schedules

```shell
curl "https://api.gomorpheus.com/api/execute-schedules" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "schedules": [
    {
      "id": 1,
      "name": "daily",
      "description": "Daily at Midnight",
      "enabled": true,
      "scheduleType": "execute",
      "scheduleTimezone": "America/New_York",
      "cron": "0 0 * * *"
      "dateCreated": "2018-03-01T07:56:38+0000",
      "lastUpdated": "2018-09-13T21:38:19+0000"
    },
    {
      "id": 2,
      "name": "weekly",
      "description": "Weekly on Sunday at Midnight",
      "enabled": true,
      "scheduleType": "execute",
      "scheduleTimezone": "America/New_York",
      "cron": "0 0 * * 7"
      "dateCreated": "2018-03-01T07:56:38+0000",
      "lastUpdated": "2018-09-13T21:38:19+0000"
    }
  ],
  "meta": {
    "size": 1,
    "total": 1,
    "max": 25,
    "offset": 0
  }
}
```

This endpoint retrieves all execute schedules associated with the account.

### HTTP Request

`GET https://api.gomorpheus.com/api/execute-schedules`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name | null | If specified will return an exact match on name
phrase | null | If specified will return a partial match on name

## Get a Specific Execute Schedule

```shell
curl "https://api.gomorpheus.com/api/execute-schedules/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "schedule": {
    "id": 1,
    "name": "daily",
    "description": "Daily at Midnight",
    "enabled": true,
    "scheduleType": "execute",
    "scheduleTimezone": "America/New_York",
    "cron": "0 0 * * *"
    "dateCreated": "2018-03-01T07:56:38+0000",
    "lastUpdated": "2018-09-13T21:38:19+0000"
  }
}
```

This endpoint retrieves a specific execute schedule.


### HTTP Request

`GET https://api.gomorpheus.com/api/execute-schedules/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the execute schedule to retrieve

## Create an Execute Schedule

```shell
curl -XPOST "https://api.gomorpheus.com/api/execute-schedules" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "schedule": {
    "name": "Friday at Midnight",
    "description": null,
    "enabled": true,
    "scheduleType": "execute",
    "scheduleTimezone": "UTC",
    "cron": "0 0 * * 5"
  }
}'
```

> The above command returns JSON structured like getting a single execute schedule: 

### HTTP Request

`POST https://api.gomorpheus.com/api/execute-schedules`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | A name for the execute schedule
description      |  | A description for the execute schedule
scheduleType      |  | Type of schedule: Execute (execute)
scheduleTimezone      | UTC | Time Zone eg. America/New_York, Europe/Amsterdam, etc.
cron | 0 0 * * * | Cron Expression. The default is daily at midnight
enabled      | true | Enabled


## Update an Execute Schedule

```shell
curl -XPUT "https://api.gomorpheus.com/api/execute-schedules/2" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "schedule": {
    "description": "Daily at 2AM",
    "cron": "0 2 * * *"
  }
}'
```

> The above command returns JSON structured like getting a single execute schedule: 

### HTTP Request

`PUT https://api.gomorpheus.com/api/execute-schedules/:id`

### JSON Parameters

See [Create](#create-an-execute-schedule).


## Delete an Execute Schedule

```shell
curl -XDELETE "https://api.gomorpheus.com/api/execute-schedules/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

Will delete an execute schedule from the system and make it no longer usable.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/execute-schedules/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the execute schedule
