# Power Schedules

Power Schedules can be configured to automatically power on and off your instances and servers.

## Get All Power Schedules

```shell
curl "https://api.gomorpheus.com/api/power-schedules" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "schedules": [
    {
      "id": 1,
      "name": "weekday daytime",
      "description": "weekday daytime hours",
      "enabled": true,
      "scheduleType": "power",
      "scheduleTimezone": "America/New_York",
      "sundayOn": 0.0,
      "sundayOff": 0.0,
      "mondayOn": 7.0,
      "mondayOff": 19.0,
      "tuesdayOn": 7.0,
      "tuesdayOff": 19.0,
      "wednesdayOn": 7.0,
      "wednesdayOff": 19.0,
      "thursdayOn": 7.0,
      "thursdayOff": 19.0,
      "fridayOn": 7.0,
      "fridayOff": 19.0,
      "saturdayOn": 0.0,
      "saturdayOff": 0.0,
      "totalMonthlyHoursSaved": 463.32,
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

This endpoint retrieves all power schedules associated with the account.

### HTTP Request

`GET https://api.gomorpheus.com/api/power-schedules`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name | null | If specified will return an exact match on name
phrase | null | If specified will return a partial match on name

## Get a Specific Power Schedule

```shell
curl "https://api.gomorpheus.com/api/power-schedules/2" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "schedule": {
    "id": 2,
    "name": "my hours",
    "description": null,
    "enabled": true,
    "scheduleType": "power",
    "scheduleTimezone": "America/New_York",
    "sundayOn": 5.5,
    "sundayOff": 24.0,
    "mondayOn": 0.0,
    "mondayOff": 24.0,
    "tuesdayOn": 0.0,
    "tuesdayOff": 24.0,
    "wednesdayOn": 0.0,
    "wednesdayOff": 24.0,
    "thursdayOn": 0.0,
    "thursdayOff": 24.0,
    "fridayOn": 0.0,
    "fridayOff": 24.0,
    "saturdayOn": 0.0,
    "saturdayOff": 24.0,
    "totalMonthlyHoursSaved": 23.595,
    "dateCreated": "2018-03-07T18:34:08+0000",
    "lastUpdated": "2018-03-07T18:34:08+0000"
  },
  "instances": [

  ],
  "servers": [

  ]
}
```

This endpoint retrieves a specific power schedule.


### HTTP Request

`GET https://api.gomorpheus.com/api/power-schedules/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the power schedule to retrieve

## Create a Power Schedule

```shell
curl -XPOST "https://api.gomorpheus.com/api/power-schedules" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "schedule": {
    "name": "business hours only",
    "description": null,
    "enabled": true,
    "scheduleType": "power",
    "scheduleTimezone": "UTC",
    "sundayOn": 0,
    "sundayOff": 0,
    "mondayOn": 7,
    "mondayOff": 19,
    "tuesdayOn": 7,
    "tuesdayOff": 19,
    "wednesdayOn": 7,
    "wednesdayOff": 19,
    "thursdayOn": 7,
    "thursdayOff": 19,
    "fridayOn": 7,
    "fridayOff": 19,
    "saturdayOn": 0,
    "saturdayOff": 0,
    "enabled": true
  }
}'
```

> The above command returns JSON structured like getting a single power schedule: 

### HTTP Request

`POST https://api.gomorpheus.com/api/power-schedules`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | A name for the power schedule
description      |  | A description for the power schedule
scheduleType      |  | Type of schedule: Power (power), Power Off (power off)
scheduleTimezone      | UTC | Time Zone eg. America/New_York, Europe/Amsterdam, etc.
enabled      | true | Enabled
sundayOn | 0 | Saturday Start
sundayOff | 24 | Saturday End
mondayOn | 0 | Monday Start
mondayOff | 24 | Monday Stop
tuesdayOn | 0 | Tuesday Start
tuesdayOff | 24 | Tuesday Stop
wednesdayOn | 0 | Wednesday Start
wednesdayOff | 24 | Wednesday Stop
thursdayOn | 0 | Thursday Start
thursdayOff | 24 | Thursday Stop
fridayOn | 0 | Friday Start
fridayOff | 24 | Friday Stop
saturdayOn | 0 | Saturday Start
saturdayOff | 24 | Saturday Stop


## Update a Power Schedule

```shell
curl -XPUT "https://api.gomorpheus.com/api/power-schedules/2" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "schedule": {
    "mondayOff": 20,
    "tuesdayOff": 20,
    "wednesdayOff": 20,
    "thursdayOff": 20,
    "fridayOff": 15
  }
}'
```

> The above command returns JSON structured like getting a single power schedule: 

### HTTP Request

`PUT https://api.gomorpheus.com/api/power-schedules/:id`

### JSON Parameters

See [Create](#create-a-power-schedule).


## Delete a Power Schedule

```shell
curl -XDELETE "https://api.gomorpheus.com/api/power-schedules/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

Will delete a power schedule from the system and make it no longer usable.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/power-schedules/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the power schedule

## Add Instances to a Power Schedule

```shell
curl -XPUT "https://api.gomorpheus.com/api/power-schedules/2/add-instances" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "instances": [
    231, 232
  ]
}'
```

> The above command returns JSON structured like this:

```json
{
  "success": true
}
```

Add one or many instances to a power schedule.

### HTTP Request

`PUT https://api.gomorpheus.com/api/power-schedules/:id/add-instances`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the power schedule

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
instances      |  | Array of Instance IDs to add

## Remove Instances from a Power Schedule

```shell
curl -XPUT "https://api.gomorpheus.com/api/power-schedules/2/remove-instances" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "instances": [
    232
  ]
}'
```

> The above command returns JSON structured like this:

```json
{
  "success": true
}
```

Remove one or many instances from a power schedule.

### HTTP Request

`PUT https://api.gomorpheus.com/api/power-schedules/:id/remove-instances`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the power schedule

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
instances      |  | Array of Instance IDs to remove

## Add Servers to a Power Schedule

```shell
curl -XPUT "https://api.gomorpheus.com/api/power-schedules/2/add-servers" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "servers": [
    6,7,8
  ]
}'
```

> The above command returns JSON structured like this:

```json
{
  "success": true
}
```

Add one or many servers to a power schedule.

### HTTP Request

`PUT https://api.gomorpheus.com/api/power-schedules/:id/add-servers`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the power schedule

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
servers      |  | Array of Server IDs to add

## Remove Servers from a Power Schedule

```shell
curl -XPUT "https://api.gomorpheus.com/api/power-schedules/2/remove-servers" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "servers": [
    7,8
  ]
}'
```

> The above command returns JSON structured like this:

```json
{
  "success": true
}
```

Remove one or many servers from a power schedule.

### HTTP Request

`PUT https://api.gomorpheus.com/api/power-schedules/:id/remove-servers`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the power schedule

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
servers      |  | Array of Server IDs to remove
