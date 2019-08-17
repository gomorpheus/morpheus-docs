# Tasks

Provides API interfaces for managing the creation and modification of automation tasks.  Tasks are used in workflows for automation.

## Get All Tasks

```shell
curl "https://api.gomorpheus.com/api/tasks"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "tasks": [
     {
      "id": 5,
      "accountId": 1,
      "name": "aptitude upgrade",
      "taskType": {
        "id": 1,
        "code": "script",
        "name": "Shell Script"
      },
      "taskOptions": {
        "script": "apt-get upgrade -y"
      }
    },
  ],
  "meta": {
    "offset": 0,
    "max": 25,
    "size": 1,
    "total": 1
  }
}
```

This endpoint retrieves all tasks.

### HTTP Request

`GET https://api.gomorpheus.com/api/tasks`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase |  | Filter by matching name
name |  | Filter by name
taskTypeCodes |  | Filter by task type code(s).

## Get a Specific Task

```shell
curl "https://api.gomorpheus.com/api/tasks/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "task": {
      "id": 5,
      "accountId": 1,
      "name": "aptitude upgrade",
      "taskType": {
        "id": 1,
        "code": "script",
        "name": "Shell Script"
      },
      "taskOptions": {
        "script": "apt-get upgrade -y"
      }
    }
}
```

This endpoint will retrieve a specific task by id

### HTTP Request

`GET https://api.gomorpheus.com/api/tasks/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the task

## Create a Task

```shell
curl -XPOST "https://api.gomorpheus.com/api/tasks" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"task": {
    "name": "cleanup tmp files",
    "taskType": {
      "code": "script"
    },
    "taskOptions": {
      "script": "rm -rf /var/www/app1/tmp/*\nrm -rf /var/www/app2/tmp/*"
    }
  }}'
```

> The above command returns JSON structured like getting a single task:

### HTTP Request

`POST https://api.gomorpheus.com/api/tasks`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name for the task
code      | null | A unique code for the task
taskType.code      | null | The type of task
taskOptions | {} | Map of options specific to each type. eg. script
resultType      | null | The result type eg. value, exitCode, keyValue, json
executeTarget      | <variable> | The execution target. eg. local,remote,resource. The default value varies by task type.
retryable      | false | If the task should be retried or not.
retryCount      | null | The number of times to retry.
retryDelaySeconds      | null | The delay, between retries.

### JSON Parameters for Execute Target: Local

Parameter | Default | Description
--------- | ------- | -----------
taskOptions.localScriptGitId      | null | The Git Repo ID
taskOptions.localScriptGitRef      | null | The Git Repo Ref eg. master

These additional task options are available when using executeTarget of `local`.

### JSON Parameters for Execute Target: Remote

Parameter | Default | Description
--------- | ------- | -----------
taskOptions.host      | null | Host or IP Address for remote execution
taskOptions.port      | 22 | Port for remote execution
taskOptions.username      | null | Username for remote execution
taskOptions.password      | null | Password for remote execution

These additional task options are available when using executeTarget of `remote`.

## Updating a Task

```shell
curl -XPUT "https://api.gomorpheus.com/api/tasks/5" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"task":{
    "name": "my task",
  }}'
```

> The above command returns JSON structured like getting a single task:

### HTTP Request

`PUT https://api.gomorpheus.com/api/tasks/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the task

### JSON Parameters

Same as [Create](#create-a-task).

## Delete a Task

```shell
curl -XDELETE "https://api.gomorpheus.com/api/tasks/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/tasks/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the task

If a task is still tied to workflows, the delete will fail.
