# Workflows

Provides API interfaces for managing the creation and modification of automation workflows. Workflows, also called Task Sets, are a collection of tasks that are organized in phases. A task phase determines if/when each task runs.

<aside class="notice">Last modified in version 3.4.1</aside>

## Get All Workflows

```shell
curl "https://api.gomorpheus.com/api/task-sets"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "taskSets": [
    {
      "id": 13,
      "name": "my workflow",
      "description": null,
      "dateCreated": "2017-06-26T15:36:19+0000",
      "lastUpdated": "2017-06-26T15:44:38+0000",
      "accountId": 1,
      "tasks": [
        8
      ],
      "taskSetTasks": [
        {
          "id": 51,
          "taskPhase": "provision",
          "taskOrder": 2,
          "task": {
            "id": 8,
            "name": "my task",
            "taskType": {
              "id": 1,
              "code": "script",
              "name": "Shell Script"
            },
            "taskOptions": {
              "script": "echo  \"hello\""
            }
          }
        }
      ]
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

This endpoint retrieves all workflows.

### HTTP Request

`GET https://api.gomorpheus.com/api/task-sets`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase | null | Filter by matching name
name | null | Filter by name

## Get a Specific Workflow

```shell
curl "https://api.gomorpheus.com/api/task-sets/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "taskSet": {
    "id": 8,
    "name": "uname",
    "description": "",
    "dateCreated": "2017-05-24T20:24:02+0000",
    "lastUpdated": "2017-05-24T20:24:02+0000",
    "accountId": 1,
    "tasks": [
      10
    ],
    "taskSetTasks": [
      {
        "id": 33,
        "taskPhase": "postProvision",
        "taskOrder": 0,
        "task": {
          "id": 10,
          "name": "uname",
          "taskType": {
            "id": 1,
            "code": "script",
            "name": "Shell Script"
          },
          "taskOptions": {
            "script": "echo `uname a`"
          }
        }
      }
    ]
  }
}
```

This endpoint will retrieve a specific workflow by id

### HTTP Request

`GET https://api.gomorpheus.com/api/task-sets/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the workflow

## Create a Workflow

```shell
curl -XPOST "https://api.gomorpheus.com/api/task-sets" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"taskSet": {
    "name": "my workflow",
    "tasks": [
      {
        "taskId": 3
      },
      {
        "taskId": 8
      },
      {
        "taskId": 9,
        "taskPhase": "postProvision"
      }
    ]
  }}'
```

> The above command returns JSON structured like getting a single workflow:

### HTTP Request

`POST https://api.gomorpheus.com/api/task-sets`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name for the workflow
description      | null | A description of the workflow
tasks      | [] | List of task objects in order
tasks.taskId | null | Task ID
tasks.taskPhase | provision | Task Phase.


## Updating a Workflow

```shell
curl -XPUT "https://api.gomorpheus.com/api/task-sets/5" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"taskSet":{
    "tasks": [
      {
        "taskId": 3
      }
    ]
  }}'
```

> The above command returns JSON structured like getting a single workflow:

### HTTP Request

`PUT https://api.gomorpheus.com/api/task-sets/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the workflow

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name for the workflow
description      | null | A description of the workflow
tasks      | [] | List of task objects in order
tasks.taskId | null | Task ID
tasks.taskPhase | provision | Task Phase.

## Delete a Workflow

```shell
curl -XDELETE "https://api.gomorpheus.com/api/task-sets/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/task-sets/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the workflow

