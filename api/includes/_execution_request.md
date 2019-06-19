# Execution Request

Provides API interfaces for executing an arbitrary script or command on an instance, container or host.

## Create an Execution Request

```shell
curl -XPOST "https://api.gomorpheus.com/api/execution-request/execute?instanceId=256" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "script": "uname -a"
}'
```

> The above command returns JSON structured like this:

```
{
  "executionRequest": {
    "id": 24,
    "uniqueId": "f22e1292-4407-44c0-b2c7-698ee2241491",
    "containerId": null,
    "serverId": null,
    "instanceId": 256,
    "stdOut": null,
    "stdErr": null,
    "exitCode": null,
    "status": "pending",
    "expiresAt": "2018-11-30T18:23:01+0000",
    "createdById": 1
  }
}
```

### HTTP Request

`POST https://api.gomorpheus.com/api/execution-request/execute`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
instanceId | null | Instance ID to execute request on
containerId | null | Container ID to execute request on
serverId | null | Host ID to execute request on

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
script      |  | A script or command to be executed

This endpoint executes the provided script on the specified instance, container or server.


## Get a Specific Execution Request

```shell
curl "https://api.gomorpheus.com/api/execution-request/f22e1292-4407-44c0-b2c7-698ee2241491" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "executionRequest": {
    "id": 24,
    "uniqueId": "f22e1292-4407-44c0-b2c7-698ee2241491",
    "containerId": null,
    "serverId": null,
    "instanceId": 256,
    "stdOut": "Linux apachetest 3.19.0-69-generic #77~14.04.1-Ubuntu SMP Tue Aug 30 01:29:21 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux\n",
    "stdErr": null,
    "exitCode": 0,
    "status": "complete",
    "expiresAt": "2018-11-30T18:23:02+0000",
    "createdById": 1
  }
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/execution-request/:uniqueId`

### URL Parameters

Parameter | Description
--------- | -----------
uniqueId | The Unique ID of the execution request

This endpoint retrieves a specific execution request.
