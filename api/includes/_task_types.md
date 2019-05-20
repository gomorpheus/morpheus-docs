# Task Types

A Task Type is a type of automation task. Each type defines its own set of options to be configured for each task.

## Get All Task Types

```shell
curl "https://api.gomorpheus.com/api/task-types"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "taskTypes": [
    {
      "id": 1,
      "code": "script",
      "name": "Shell Script",
      "category": "script",
      "description": null,
      "optionTypes": [
        {
          "id": 254,
          "name": "Script",
          "code": "script",
          "description": null,
          "fieldName": "script",
          "fieldLabel": "Script",
          "fieldContext": "taskOptions",
          "fieldGroup": null,
          "fieldClass": null,
          "fieldAddOn": null,
          "placeHolder": null,
          "helpBlock": null,
          "defaultValue": null,
          "optionSource": null,
          "type": "code-editor",
          "advanced": false,
          "required": false,
          "editable": false,
          "config": {
          },
          "displayOrder": 5,
          "wrapperClass": null,
          "enabled": true,
          "noBlank": null,
          "dependsOnCode": null,
          "contextualDefault": null
        }
      ]
    },
    {
      "id": 2,
      "code": "sshTask",
      "name": "SSH Script",
      "category": "script",
      "description": null,
      "optionTypes": [
        {
          "id": 258,
          "name": "Key",
          "code": "sshKey",
          "description": null,
          "fieldName": "sshKey",
          "fieldLabel": "Key",
          "fieldContext": "taskOptions",
          "fieldGroup": null,
          "fieldClass": null,
          "fieldAddOn": null,
          "placeHolder": null,
          "helpBlock": null,
          "defaultValue": null,
          "optionSource": "keyPairs",
          "type": "select",
          "advanced": false,
          "required": false,
          "editable": false,
          "config": {
          },
          "displayOrder": 2,
          "wrapperClass": null,
          "enabled": true,
          "noBlank": null,
          "dependsOnCode": null,
          "contextualDefault": null
        },
        {
          "id": 254,
          "name": "Script",
          "code": "script",
          "description": null,
          "fieldName": "script",
          "fieldLabel": "Script",
          "fieldContext": "taskOptions",
          "fieldGroup": null,
          "fieldClass": null,
          "fieldAddOn": null,
          "placeHolder": null,
          "helpBlock": null,
          "defaultValue": null,
          "optionSource": null,
          "type": "code-editor",
          "advanced": false,
          "required": false,
          "editable": false,
          "config": {
          },
          "displayOrder": 5,
          "wrapperClass": null,
          "enabled": true,
          "noBlank": null,
          "dependsOnCode": null,
          "contextualDefault": null
        },
        {
          "id": 259,
          "name": "IP Address",
          "code": "host",
          "description": null,
          "fieldName": "host",
          "fieldLabel": "IP Address",
          "fieldContext": "taskOptions",
          "fieldGroup": null,
          "fieldClass": null,
          "fieldAddOn": null,
          "placeHolder": null,
          "helpBlock": null,
          "defaultValue": null,
          "optionSource": null,
          "type": "text",
          "advanced": false,
          "required": false,
          "editable": false,
          "config": {
          },
          "displayOrder": 0,
          "wrapperClass": null,
          "enabled": true,
          "noBlank": null,
          "dependsOnCode": null,
          "contextualDefault": null
        },
        {
          "id": 257,
          "name": "Password",
          "code": "password",
          "description": null,
          "fieldName": "password",
          "fieldLabel": "Password",
          "fieldContext": "taskOptions",
          "fieldGroup": null,
          "fieldClass": null,
          "fieldAddOn": null,
          "placeHolder": null,
          "helpBlock": null,
          "defaultValue": null,
          "optionSource": null,
          "type": "password",
          "advanced": false,
          "required": false,
          "editable": false,
          "config": {
          },
          "displayOrder": 4,
          "wrapperClass": null,
          "enabled": true,
          "noBlank": null,
          "dependsOnCode": null,
          "contextualDefault": null
        },
        {
          "id": 260,
          "name": "Port",
          "code": "port",
          "description": null,
          "fieldName": "port",
          "fieldLabel": "Port",
          "fieldContext": "taskOptions",
          "fieldGroup": null,
          "fieldClass": null,
          "fieldAddOn": null,
          "placeHolder": null,
          "helpBlock": null,
          "defaultValue": null,
          "optionSource": null,
          "type": "text",
          "advanced": false,
          "required": false,
          "editable": false,
          "config": {
          },
          "displayOrder": 1,
          "wrapperClass": null,
          "enabled": true,
          "noBlank": null,
          "dependsOnCode": null,
          "contextualDefault": null
        },
        {
          "id": 256,
          "name": "Username",
          "code": "username",
          "description": null,
          "fieldName": "username",
          "fieldLabel": "Username",
          "fieldContext": "taskOptions",
          "fieldGroup": null,
          "fieldClass": null,
          "fieldAddOn": null,
          "placeHolder": null,
          "helpBlock": null,
          "defaultValue": null,
          "optionSource": null,
          "type": "text",
          "advanced": false,
          "required": false,
          "editable": false,
          "config": {
          },
          "displayOrder": 3,
          "wrapperClass": null,
          "enabled": true,
          "noBlank": null,
          "dependsOnCode": null,
          "contextualDefault": null
        }
      ]
    }
  ]
}
```


### HTTP Request

`GET https://api.gomorpheus.com/api/task-types`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name |  | If specified will return an exact match on name or code
code |  | If specified will return an exact match on code


## Get a Specific Task Type

```shell
curl "https://api.gomorpheus.com/api/task-types/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "success": true,
  "taskType": {
      "id": 1,
      "code": "script",
      "name": "Shell Script",
      "category": "script",
      "description": null,
      "optionTypes": [
        {
          "id": 254,
          "name": "Script",
          "code": "script",
          "description": null,
          "fieldName": "script",
          "fieldLabel": "Script",
          "fieldContext": "taskOptions",
          "fieldGroup": null,
          "fieldClass": null,
          "fieldAddOn": null,
          "placeHolder": null,
          "helpBlock": null,
          "defaultValue": null,
          "optionSource": null,
          "type": "code-editor",
          "advanced": false,
          "required": false,
          "editable": false,
          "config": {
          },
          "displayOrder": 5,
          "wrapperClass": null,
          "enabled": true,
          "noBlank": null,
          "dependsOnCode": null,
          "contextualDefault": null
        }
      ]
    }
}
```
This endpoint will retrieve a specific task type by id

### HTTP Request

`GET https://api.gomorpheus.com/api/task-types/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the task type
