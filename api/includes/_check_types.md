# Check Types

A set of APIs for fetching a list of available check types is also provided. This API can make it useful for associating a check type code to an ID for check `GET` and `POST` requests.

## Get All Check Types

```shell
curl "https://api.gomorpheus.command/api/monitoring/check-types"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
{
  "checkTypes": [
    {
      "id": 1,
      "code": "webGetCheck",
      "createIncident": true,
      "defaultInterval": 60000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "response",
      "name": "Web Check",
      "tunnelSupported": true
    },
    {
      "id": 2,
      "code": "mysqlCheck",
      "createIncident": true,
      "defaultInterval": 60000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "result",
      "name": "MySQL Check",
      "tunnelSupported": true
    },
    {
      "id": 3,
      "code": "mongoCheck",
      "createIncident": true,
      "defaultInterval": 300000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "result",
      "name": "Mongo Check",
      "tunnelSupported": true
    },
    {
      "id": 4,
      "code": "elasticSearchCheck",
      "createIncident": true,
      "defaultInterval": 60000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "cluster status",
      "name": "Elastic Search Check",
      "tunnelSupported": true
    },
    {
      "id": 5,
      "code": "riakCheck",
      "createIncident": true,
      "defaultInterval": 300000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "write time",
      "name": "Riak Check",
      "tunnelSupported": true
    },
    {
      "id": 6,
      "code": "redisCheck",
      "createIncident": true,
      "defaultInterval": 300000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "key count",
      "name": "Redis Check",
      "tunnelSupported": true
    },
    {
      "id": 7,
      "code": "rabbitCheck",
      "createIncident": true,
      "defaultInterval": 60000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "queue count",
      "name": "Rabbit MQ Check",
      "tunnelSupported": true
    },
    {
      "id": 9,
      "code": "postgresCheck",
      "createIncident": true,
      "defaultInterval": 300000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "result",
      "name": "Postgres Check",
      "tunnelSupported": true
    },
    {
      "id": 10,
      "code": "sqlCheck",
      "createIncident": true,
      "defaultInterval": 300000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "result",
      "name": "Microsoft SQL Server",
      "tunnelSupported": true
    },
    {
      "id": 11,
      "code": "socketCheck",
      "createIncident": true,
      "defaultInterval": 60000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "response",
      "name": "Socket Check",
      "tunnelSupported": true
    },
    {
      "id": 12,
      "code": "pushCheck",
      "createIncident": true,
      "defaultInterval": 300000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "result",
      "name": "Push API Check",
      "tunnelSupported": false
    },
    {
      "id": 13,
      "code": "pingCheck",
      "createIncident": true,
      "defaultInterval": 300000,
      "iconPath": null,
      "iconType": "upload",
      "inUptime": true,
      "metricName": "result",
      "name": "Ping Check",
      "tunnelSupported": true
    }
  ]
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/monitoring/check-types`

## Get Specific Check Type

```shell
curl "https://api.gomorpheus.com/api/monitoring/check-types/10"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
{
  "success": true,
  "checkType": {
    "id": 10,
    "code": "sqlCheck",
    "createIncident": true,
    "defaultInterval": 300000,
    "iconPath": null,
    "iconType": "upload",
    "inUptime": true,
    "metricName": "result",
    "name": "Microsoft SQL Server",
    "tunnelSupported": true
  }
}
```
### HTTP Request

`GET https://api.gomorpheus.com/api/monitoring/check-types/1`

