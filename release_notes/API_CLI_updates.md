|version| API and CLI Updates

# Whitelabel Settings

Provides API interfaces for managing whitelabel settings within Morpheus

## Get Whitelabel Settings

```shell
curl "https://api.gomorpheus.com/api/whitelabel-settings" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "whitelabelSettings": {
    "enabled": true,
    "applianceName": "My Appliance",
    "disableSupportMenu": false,
    "headerLogo": "http://localhost:8080/storage/uploads/uploads/ApplianceInstance/1/headerLogo/header_logo_original.png",
    "footerLogo": "http://localhost:8080/storage/uploads/uploads/ApplianceInstance/1/footerLogo/footer_logo_original.png",
    "loginLogo": "http://localhost:8080/storage/uploads/uploads/ApplianceInstance/1/loginLogo/login_logo_original.png",
    "favicon": "http://localhost:8080/storage/uploads/uploads/ApplianceInstance/1/favicon/favicon_original.ico",
    "headerBgColor": "#ffffff",
    "headerFgColor": "black",
    "navBgColor": "#ffffff",
    "navFgColor": "pink",
    "navHoverColor": "green",
    "primaryButtonBgColor": "red",
    "primaryButtonFgColor": "blue",
    "primaryButtonHoverBgColor": "orange",
    "primaryButtonHoverFgColor": "gray",
    "footerBgColor": "brown",
    "footerFgColor": "yellow",
    "loginBgColor": "aqua",
    "overrideCss": "div {\r\n    font-size: 16px;\r\n}",
    "copyrightString": "My copywriter",
    "termsOfUse": "These are my terms of use.",
    "privacyPolicy": "Here is my privacy policy.",
    "supportMenuLinks": [
      {
        "url": "http://helpmenu.com",
        "label": "Help",
        "labelCode": "help"
      }
    ]
  }
}    
```

This endpoint retrieves whitelabel settings.

### HTTP Request

`GET https://api.gomorpheus.com/api/whitelabel-settings`


## Update Whitelabel Settings

```shell
curl -XPUT "https://api.gomorpheus.com/api/whitelabel-settings" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"whitelabelSettings": {
        "navBgColor": "#fff",
        "enabled": true,
        "applianceName": "My Appliance",
        "disableSupportMenu": false,
        "resetHeaderLogo": true,
        "resetFooterLogo": true,
        "resetLoginLogo": true,
        "resetFavicon": true,
        "headerBgColor": "#fff",
        "headerFgColor": "black",
        "navFgColor": "pink",
        "navHoverColor": "green",
        "primaryButtonBgColor": "red",
        "primaryButtonFgColor": "blue",
        "primaryButtonHoverBgColor": "orange",
        "primaryButtonHoverFgColor": "gray",
        "footerBgColor": "brown",
        "footerFgColor": "yellow",
        "loginBgColor": "cyan",
        "copyrightString": "My copywriter",
        "overrideCss": "div {\n    font-size: 16px;\n}",
        "termsOfUse": "These are my terms of use.",
        "privacyPolicy": "Here is my privacy policy.",
        "supportMenuLinks": [
          {
            "url": "http://helpme.com",
            "label": "Help Label",
            "labelCode": "help-code"
          },
          {
            "url": "http://helpmemore.com",
            "label": "Help More Label",
            "labelCode": "help-more-code"
          }
        ]
      }}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/whitelabel-settings`

### JSON Parameters

Parameter | Description
--------- | -----------
active | Can be used to enable / disable whitelabel feature [on&#124;off]
applianceName | Appliance name. Master account only
disableSupportMenu | Can be used to disable support menu [on&#124;off]
resetHeaderLogo | Resets header logo to default header logo
resetFooterLogo | Resets footer logo to default footer logo
resetLoginLogo | Resets login logo to default login logo
resetFavicon | Resets favicon to default favicon
headerBgColor | Header background color
headerFgColor | Header foreground color
navBgColor | Nav background color
navFgColor | Nav foreground color
navHoverColor | Nav hover color
primaryButtonBgColor | Primary button background color
primaryButtonFgColor | Primary button foreground color
primaryButtonHoverBgColor | Primary button hover background color
primaryButtonHoverFgColor | Primary button hover foreground color
footerBgColor | Footer background color
footerFgColor | Footer foreground color
loginBgColor | Login background color
copyrightString | Copyright String
overrideCss | Override CSS
termsOfUse | Terms of use content
privacyPolicy | Privacy policy content
supportMenuLinks | Support menu links. See [Support Menu Links](#support-menu-links)

#### Support Menu Links

Parameter | Description
--------- | -----------
url | URL to support menu link
label | Label for support menu link
labelCode | Label code for support menu link


## Update Images

```shell
curl -XPOST "https://api.gomorpheus.com/api/whitelabel-settings/images" \
  -H "Authorization: BEARER access_token" \
  -F 'headerLogo.file=@filename' \
  -F 'footerLogo.file=@filename' \
  -F 'loginLogo.file=@filename' \
  -F 'favicon.file=@filename'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`POST https://api.gomorpheus.com/api/whitelabel-settings/images`

### Parameters

Parameter | Required | Description
--------- | -------- | -----------
headerLogo.file | N | Header logo image file, valid image types png,jpg,svg)
resetHeaderLogo | N | Resets header logo to default
footerLogo.file | N | Footer logo image file, valid image types png,jpg,svg)
resetFooterLogo | N | Resets footer logo to default
loginLogo.file | N | Login logo image file, valid image types png,jpg,svg)
resetLoginLogo | N | Resets login logo to default
favicon.file | N | Favicon image file, valid image type ico
resetFavicon | N | Resets favicon logo to default

Uploads whitelabel images.  Expects multipart form data as the request format, not JSON.


## Reset Image

```shell
curl -XDELETE "https://api.gomorpheus.com/api/whitelabel-settings/images/:imageType" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/whitelabel-settings/images/:imageType`

Resets the specified image to the morpheus default. See [Valid Image Types](#valid-image-types)

#### Valid Image Types
* headerLogo
* footerLogo
* loginLogo
* favicon


## Download Image

```shell
curl -XGET "https://api.gomorpheus.com/api/whitelabel-settings/images/:imageType" \
  -H "Authorization: BEARER access_token"
```

> The above command returns binary output of the specified image

### HTTP Request

`GET https://api.gomorpheus.com/api/whitelabel-settings/images/:imageType`

Downloads the specified image. See [Valid Image Types](#valid-image-types)

# Provisioning Settings

Provides API interfaces for managing provisioning settings within Morpheus

## Get Provisioning Settings

```shell
curl "$MORPHEUS_API_URL/api/provisioning-settings" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "provisioningSettings": {
    "allowZoneSelection": true,
    "allowServerSelection": true,
    "requireEnvironments": true,
    "showPricing": true,
    "hideDatastoreStats": true,
    "crossTenantNamingPolicies": false,
    "reuseSequence": true,
    "cloudInitUsername": "root",
    "cloudInitPassword": "****",
    "cloudInitKeyPair": {
      "id": 3,
      "name": "stubby.toes"
    },
    "windowsPassword": null,
    "pxeRootPassword": null,
    "defaultTemplateType": {
      "id": 1,
      "name": "morpheus",
      "code": "morpheus"
    },
    "deployStorageProvider": {
      "id": 42,
      "name": "morpheus-deployments"
    }
  }
}
```

This endpoint retrieves provisioning settings.

### HTTP Request

`GET https://api.gomorpheus.com/api/provisioning-settings`


## Update Provisioning Settings

```shell
curl -XPUT "$MORPHEUS_API_URL/api/provisioning-settings" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
        "provisioningSettings": {
          "allowZoneSelection": true,
          "allowServerSelection": true,
          "requireEnvironments": true,
          "showPricing": true,
          "hideDatastoreStats": true,
          "crossTenantNamingPolicies": true,
          "reuseSequence": true,
          "cloudInitUsername": "stubbytoes",
          "cloudInitPassword": "supersecret",
          "deployStorageProvider": {
            "id": 42
          },
          "defaultTemplateType": {
            "id": 2
          }
        }
      }'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/provisioning-settings`

### JSON Parameters

Parameter | Description
--------- | -----------
allowZoneSelection | Use this to enable / disable allowing cloud selection
allowServerSelection | Use this to enable / disable allowing host selection
requireEnvironments | Use this to enable / disable requiring environment selection
showPricing | Use this to enable / disable showing pricing
hideDatastoreStats | Use this to enable / disable hiding datastore stats
crossTenantNamingPolicies | Use this to enable / disable cross-tenant naming policies
reuseSequence | Use this to enable / disable reusing naming sequence numbers
cloudInitUsername | Cloud-init username
cloudInitPassword | Cloud-init password
cloudInitKeyPair.id | Cloud-init key pair ID
deployStorageProvider.id | Deployment archive storage provider ID
windowsPassword | Windows administrator password
pxeRootPassword | PXE Boot default root password
defaultTemplateType.id | Default blueprint type ID

# Jobs

Provides API interfaces for managing jobs within Morpheus

## Get All Jobs

```shell
curl "$MORPHEUS_API_URL/api/jobs" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "jobs": [
    {
      "id": 5,
      "name": "task 2",
      "type": {
        "id": 3,
        "name": "Task Job",
        "code": "morpheus.task"
      },
      "task": {
        "id": 2
      },
      "jobSummary": "echo hello",
      "scheduleMode": "manual",
      "status": null,
      "namespace": null,
      "category": null,
      "description": null,
      "enabled": true,
      "dateCreated": "2019-11-13T19:17:50+0000",
      "lastUpdated": "2019-11-13T19:17:50+0000",
      "lastRun": null,
      "lastResult": null,
      "createdBy": {
        "id": 1,
        "username": "root"
      },
      "targetType": "server",
      "targets": [
        {
          "id": 8,
          "name": "server 1",
          "targetType": "server",
          "refId": 20
        }
      ],
      "customConfig": null
    }
  ],
  "stats": {
    "jobCount": 17,
    "todayCount": 7,
    "execCount": 17,
    "execSuccess": 0,
    "execSuccessRate": 0,
    "execFailed": 7,
    "execFailedRate": 41.17647059,
    "executionsPerDay": [
      0,
      1,
      1,
      3,
      2,
      3,
      7
    ]
  },
  "meta": {
    "size": 1,
    "total": 1,
    "max": 25,
    "offset": 0
  }
}

```

This endpoint retrieves all jobs.

### HTTP Request

`GET https://api.gomorpheus.com/api/jobs`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase |  | Name or external ID filter, restricts query to only load jobs which contain the phrase specified
itemSource |  | Source filter, restricts query to only load jobs of specified source: [all, user, sync]

## Get a Specific Job

```shell
curl "$MORPHEUS_API_URL/api/jobs/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "job": {
    "id": 14,
    "name": "Task 1",
    "type": {
      "id": 3,
      "name": "Task Job",
      "code": "morpheus.task"
    },
    "task": {
      "id": 1
    },
    "jobSummary": "echo hello",
    "scheduleMode": "1",
    "status": null,
    "namespace": null,
    "category": null,
    "description": null,
    "enabled": true,
    "dateCreated": "2019-11-16T18:29:35+0000",
    "lastUpdated": "2019-11-16T19:46:36+0000",
    "lastRun": "2019-11-16T19:45:20+0000",
    "lastResult": "error",
    "createdBy": {
      "id": 1,
      "username": "root"
    },
    "targetType": "server",
    "targets": [
      {
        "id": 35,
        "name": "Server 1",
        "targetType": "server",
        "refId": 55
      }
    ],
    "customConfig": null
  },
  "executions": {
    "jobExecutions": [
      {
        "id": 25,
        "name": "Task 1",
        "process": {
          "id": 181,
          "accountId": 1,
          "uniqueId": "6d1388d0-2482-429a-81e5-92afad192c5c",
          "processType": {
            "code": "serverWorkflow",
            "name": "workflow"
          },
          "description": "Task 1",
          "subType": null,
          "subId": null,
          "zoneId": 3,
          "integrationId": null,
          "instanceId": null,
          "containerId": null,
          "serverId": 55,
          "containerName": null,
          "displayName": "Server 1",
          "timerCategory": "Task 1",
          "timerSubCategory": "99",
          "status": "failed",
          "reason": null,
          "percent": 100.0,
          "statusEta": 180000,
          "message": "unknown error",
          "output": null,
          "error": null,
          "startDate": "2019-11-16T19:45:20+0000",
          "endDate": "2019-11-16T19:46:35+0000",
          "duration": 75585,
          "dateCreated": "2019-11-16T19:45:20+0000",
          "lastUpdated": "2019-11-16T19:46:36+0000",
          "createdBy": {
            "username": "root",
            "displayName": "Stubby Toes"
          },
          "updatedBy": {
            "username": "root",
            "displayName": "Stubby Toes"
          },
          "events": [
            {
              "id": 23,
              "processId": 166,
              "accountId": 1,
              "uniqueId": "8401ac1f-fc02-475d-a3ec-f61ea49e668b",
              "processType": {
                "code": "executeTask",
                "name": "execute task"
              },
              "description": "echo hello",
              "refType": "instance",
              "refId": 3,
              "subType": null,
              "subId": null,
              "zoneId": null,
              "integrationId": null,
              "instanceId": 3,
              "containerId": null,
              "serverId": null,
              "containerName": null,
              "displayName": "name",
              "status": "failed",
              "reason": null,
              "percent": 100.0,
              "statusEta": 180000,
              "message": "Task Execution Failed on Attempt 1\n",
              "output": null,
              "error": "Task Execution Failed on Attempt 1\n",
              "startDate": "2019-11-14T08:00:14+0000",
              "endDate": "2019-11-14T08:00:16+0000",
              "duration": 1800,
              "dateCreated": "2019-11-14T08:00:14+0000",
              "lastUpdated": "2019-11-14T08:00:16+0000",
              "createdBy": {
                "username": "root",
                "displayName": "Stubby Toes"
              },
              "updatedBy": {
                "username": "root",
                "displayName": "Stubby Toes"
              }
            }
          ]
        },
        "job": {
          "id": 14,
          "name": "Task 1",
          "description": null,
          "type": {
            "id": 3,
            "code": "morpheus.task",
            "name": "Task Job"
          }
        },
        "description": null,
        "dateCreated": "2019-11-16T19:45:20+0000",
        "startDate": "2019-11-16T19:45:20+0000",
        "endData": "2019-11-16T19:46:36+0000",
        "duration": 75513,
        "resultData": "{\"data\":{\"results\":[],\"processId\":181},\"errorCode\":null,\"errors\":{},\"inProgress\":false,\"msg\":\"\",\"success\":false}",
        "status": "error",
        "statusMessage": null
      }
    ],
    "meta": {
      "size": 1,
      "total": 1,
      "max": 3,
      "offset": 0
    }
  }
}
```

This endpoint retrieves a specific job.

### HTTP Request

`GET https://api.gomorpheus.com/api/jobs/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the job
includeExecCount | Number of most recent job executions to include in response


## Create a Job

Use this command to create a job. This command requires either a task `task.id` or workflow `workflow.id` (not both).

```shell
curl -XPOST "$MORPHEUS_API_URL/api/jobs" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"job": {
        "name": "Job 1",
        "workflow": {
          "id": 3
        },
        "targetType": "server",
        "targets": [
          {
            "refId": 2
          },
          {
            "refId": 3
          }
        ],
        "scheduleMode": "manual",
        "customConfig": "foo=bar"
     }}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`POST https://api.gomorpheus.com/api/jobs`

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
name | Y | Job name
enabled | N | Use this to set enabled state, defaults to true
task.id | Y if workflow.id not used | Use this to assign task to job. Not compatible with workflow
workflow.id | Y if task.id not used | Use this to assign workflow to job. Not compatible with task
targetType | Y | Target type where job will execute: appliance, instance, server
targets | 1..n for instance or server target types | Key for targets configuration, see [Targets](#targets)
scheduleMode | Y | Job execution schedule type ID or 'manual'
customConfig | N | Job custom configuration

#### Targets

The `targets` parameter is list of targets where job will execute.

Parameter | Required | Description
--------- | -------- | -----------
refId | Y | ID for instance or server depending on target type


## Update a Job

```shell
curl -XPUT "$MORPHEUS_API_URL/api/jobs/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"job": {
        "name": "Job 1",
        "workflow": {
          "id": 3
        },
        "targetType": "server",
        "targets": [
          {
            "refId": 2
          },
          {
            "refId": 3
          }
        ],
        "scheduleMode": "manual",
        "customConfig": "foo=bar",
        "run": true
     }}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/jobs/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the job

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
name | N | Job name
enabled | N | Use this to set enabled state
task.id | N | Use this to assign task to job. Not compatible with workflow
workflow.id | N | Use this to assign workflow to job. Not compatible with task
targetType | N | Target type where job will execute: appliance, instance, server
targets | N | Key for targets configuration, see [Targets](#targets)
scheduleMode | N | Job execution schedule type ID or 'manual'
customConfig | N | Job custom configuration
run | N | If true executes job


## Execute a Job

Use this command to execute a job.

```shell
curl -XPUT "$MORPHEUS_API_URL/api/jobs/3/execute" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/jobs/:id/execute?customConfig=%7Bfoo%3Abar%7D`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the job
customConfig | Optional custom config


## Delete a Job

Use this command to delete a job.

```shell
curl -XDELETE "$MORPHEUS_API_URL/api/jobs/3" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/jobs/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the job


## Get Job Executions

```shell
curl "$MORPHEUS_API_URL/api/job-executions" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "jobExecutions": [
    {
      "id": 30,
      "name": "name",
      "process": {
        "id": 190,
        "accountId": 1,
        "uniqueId": "2d959a94-0db6-427d-94b0-440737e9a485",
        "processType": {
          "code": "serverWorkflow",
          "name": "workflow"
        },
        "description": "name",
        "subType": null,
        "subId": null,
        "zoneId": 3,
        "integrationId": null,
        "instanceId": null,
        "containerId": null,
        "serverId": 21,
        "containerName": null,
        "displayName": "cluster resource name-master",
        "timerCategory": "name",
        "timerSubCategory": "191",
        "status": "failed",
        "reason": null,
        "percent": 100.0,
        "statusEta": 180000,
        "message": "unknown error",
        "output": null,
        "error": null,
        "startDate": "2019-11-17T14:27:08+0000",
        "endDate": "2019-11-17T14:28:23+0000",
        "duration": 75584,
        "dateCreated": "2019-11-17T14:27:08+0000",
        "lastUpdated": "2019-11-17T14:28:23+0000",
        "createdBy": {
          "username": "root",
          "displayName": "Stubby Toes"
        },
        "updatedBy": {
          "username": "root",
          "displayName": "Stubby Toes"
        },
        "events": [

        ]
      },
      "job": {
        "id": 3,
        "name": "name",
        "description": null,
        "type": {
          "id": 2,
          "code": "morpheus.workflow",
          "name": "Workflow Job"
        }
      },
      "description": null,
      "dateCreated": "2019-11-17T14:25:52+0000",
      "startDate": "2019-11-17T14:25:52+0000",
      "endData": "2019-11-17T14:28:23+0000",
      "duration": 151421,
      "resultData": "{\"data\":{\"results\":[],\"processId\":190},\"errorCode\":null,\"errors\":{},\"inProgress\":false,\"msg\":\"\",\"success\":false}",
      "status": "error",
      "statusMessage": null
    }
  ],
  "meta": {
    "size": 1,
    "total": 29,
    "max": "1",
    "offset": 0
  }
}
```

This endpoint retrieves job executions.

### HTTP Request

`GET https://api.gomorpheus.com/api/job-executions`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
jobId |  | Job ID filter, restricts query to only load executions for specified job
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase |  | Name or external ID filter, restricts query to only load job executions which contain the phrase specified


## Get a Specific Job Execution

```shell
curl "$MORPHEUS_API_URL/api/job-executions/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "jobExecution": {
    "id": 26,
    "name": "Task 1",
    "process": {
      "id": 187,
      "accountId": 1,
      "uniqueId": "9872270f-1a0f-4c5e-9ae8-8afb692da0fa",
      "processType": {
        "code": "serverWorkflow",
        "name": "workflow"
      },
      "description": "Task 1",
      "subType": null,
      "subId": null,
      "zoneId": 3,
      "integrationId": null,
      "instanceId": null,
      "containerId": null,
      "serverId": 55,
      "containerName": null,
      "displayName": "docker1",
      "timerCategory": "Task 1",
      "timerSubCategory": "99",
      "status": "failed",
      "reason": null,
      "percent": 100.0,
      "statusEta": 180000,
      "message": "unknown error",
      "output": null,
      "error": null,
      "startDate": "2019-11-17T08:41:48+0000",
      "endDate": "2019-11-17T08:43:42+0000",
      "duration": 113862,
      "dateCreated": "2019-11-17T08:41:48+0000",
      "lastUpdated": "2019-11-17T08:43:42+0000",
      "createdBy": {
        "username": "root",
        "displayName": "Stubby Toes"
      },
      "updatedBy": {
        "username": "root",
        "displayName": "Stubby Toes"
      },
      "events": [

      ]
    },
    "job": {
      "id": 14,
      "name": "Task 1",
      "description": null,
      "type": {
        "id": 3,
        "code": "morpheus.task",
        "name": "Task Job"
      }
    },
    "description": null,
    "dateCreated": "2019-11-17T08:41:47+0000",
    "startDate": "2019-11-17T08:41:47+0000",
    "endData": "2019-11-17T08:43:42+0000",
    "duration": 115226,
    "resultData": "{\"data\":{\"results\":[],\"processId\":187},\"errorCode\":null,\"errors\":{},\"inProgress\":false,\"msg\":\"\",\"success\":false}",
    "status": "error",
    "statusMessage": null
  }
}
```

This endpoint retrieves a specific job execution.

### HTTP Request

`GET https://api.gomorpheus.com/api/job-executions/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the job


## Get a Specific Job Execution Event

```shell
curl "$MORPHEUS_API_URL/api/job-executions/1/events/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "processEvent": {
    "id": 32,
    "processId": 201,
    "accountId": 1,
    "uniqueId": "82368308-045e-40c8-ad41-faf7ecd6320e",
    "processType": {
      "code": "executeTask",
      "name": "execute task"
    },
    "description": "echo goodbye",
    "refType": "instance",
    "refId": 3,
    "subType": null,
    "subId": null,
    "zoneId": null,
    "integrationId": null,
    "instanceId": 3,
    "containerId": null,
    "serverId": null,
    "containerName": null,
    "displayName": "echo goodbye",
    "status": "failed",
    "reason": null,
    "percent": 100.0,
    "statusEta": 10568,
    "message": "Task Execution Failed on Attempt 1\n",
    "output": null,
    "error": "Task Execution Failed on Attempt 1\n",
    "startDate": "2019-11-19T08:00:25+0000",
    "endDate": "2019-11-19T08:00:27+0000",
    "duration": 1712,
    "dateCreated": "2019-11-19T08:00:25+0000",
    "lastUpdated": "2019-11-19T08:00:27+0000",
    "createdBy": {
      "username": "root",
      "displayName": "Stubby Toes"
    },
    "updatedBy": {
      "username": "root",
      "displayName": "Stubby Toes"
    }
  }
}
```

This endpoint retrieves a specific job execution event.

### HTTP Request

`GET https://api.gomorpheus.com/api/job-executions/:id/events/:eventId`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the job execution
eventId | ID of the job execution event

## Workflows

Provides API interfaces for managing the creation and modification of automation workflows. Workflows, also called Task Sets, are a collection of tasks that are organized in phases. A task phase determines if/when each task runs.

A Workflow may also be referred to as a *Task Set* or *taskSet*.

<!--## Get All Workflows-->

```shell
curl "$MORPHEUS_API_URL/api/task-sets" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
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
phrase |  | Filter by matching name
name |  | Filter by name

## Get a Specific Workflow

```shell
curl "$MORPHEUS_API_URL/api/task-sets/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
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
curl -XPOST "$MORPHEUS_API_URL/api/task-sets" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
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
name      |  | A unique name for the workflow
description      |  | A description of the workflow
type      | provision | Workflow type. Pass `operation` for operational workflows.
optionTypes      | [] | List of option type IDs for use with operational workflow configuration.
tasks      | [] | List of task objects in order
tasks.taskId |  | Task ID
tasks.taskPhase | provision | Task Phase. Pass `operation` for operational workflows.

## Create an Operational Workflow

```shell
curl -XPOST "$MORPHEUS_API_URL/api/task-sets" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"taskSet": {
    "name": "test workflow",
    "type": "operation",
    "optionTypes": [3,4,5],
    "tasks": [
      {
        "taskId": 3,
        "phase": "operation"
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
name      |  | A unique name for the workflow
description      |  | A description of the workflow
type      | provision | Workflow type. Pass `operation` for operational workflows.
optionTypes      | [] | List of option type IDs for use with operational workflow configuration.
tasks      | [] | List of task objects in order
tasks.taskId |  | Task ID
tasks.taskPhase | provision | Task Phase. Pass `operation` for operational workflows

## Updating a Workflow

```shell
curl -XPUT "$MORPHEUS_API_URL/api/task-sets/5" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
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
name      |  | A unique name for the workflow
description      |  | A description of the workflow
tasks      | [] | List of task objects in order
tasks.taskId |  | Task ID
tasks.taskPhase | provision | Task Phase.

## Delete a Workflow

```shell
curl -XDELETE "$MORPHEUS_API_URL/api/task-sets/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
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

## Execute a Workflow

```shell
curl -XPOST "$MORPHEUS_API_URL/api/task-sets/5/execute" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"job":{
    "targetType": "instance",
    "instances": [1],
    "customOptions": {
      "mysqlVersion":"5.7"
    }
  }}'
```

> The above command returns JSON structured like this:

```json
{
  "success": true
}
```

This endpoint executes a workflow on the specified `instances` or `servers`, depending on which `targetType` is specified.  The [History API](#get-all-processes) can be used to retrieve information about the execution results.

### HTTP Request

`POST https://api.gomorpheus.com/api/task-sets/:id/execute`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the workflow

### JSON Parameters

The following parameters are passed inside an object named `job`.

Parameter | Default | Description
--------- | ------- | -----------
name      | (workflow name) | A name for the execution job. Can be used to find execution results with `/api/processes?name=`.
targetType      | | The type of object to execute on. Pass either `instance` or `server`.
instances      | | Array of Instance IDs. Only applicable for `targetType` is `instance`.
servers      | | Array of Server IDs. Only applicable for `targetType` is `server`.
customOptions | | Map of options to be used as values in the workflow tasks. These correspond to option types.
customConfig | | String of custom configuration values as JSON.

# Servers : Convert To Managed
## Convert To Managed

```shell
curl -XPUT "$MORPHEUS_API_URL/api/servers/1/make-managed" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{ "server": {
  "sshUsername": "admin",
  "sshPassword": "asafepassword",
  "serverOs": {"id": 1}
  }, "installAgent": true}'
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

This will make the host a managed server, and install the agent.

### HTTP Request

`PUT https://api.gomorpheus.com/api/servers/:id/make-managed`


### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
server      |  | Object containing server configuration parameters
installAgent | true | Install agent. Set to false to manually install agent instead.

### JSON Server Parameters

Parameter | Default | Description
--------- | ------- | -----------
sshUsername      |  | ssh username to use when provisioning
sshPassword |  | ssh password to use, if not specified the account public key can be used
serverOs.id |  | The ID os the OS Type for this server. See GET /api/options/osTypes


# Clusters : Datastores
## Get Datastores

```shell
curl "$MORPHEUS_API_URL/api/clusters/:id/datastores"
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "datastores": [
    {
      "id": 4,
      "name": "vsanDatastore",
      "code": null,
      "type": "vsan",
      "visibility": "privates",
      "storageSize": 3000483446784,
      "freeSpace": 1634729396798,
      "drsEnabled": false,
      "active": true,
      "allowWrite": true,
      "defaultStore": false,
      "online": true,
      "allowRead": true,
      "allowProvision": true,
      "refType": "ComputeServerGroup",
      "refId": 3,
      "externalId": "datastore-58601",
      "zone": {
        "id": 4
      },
      "zonePool": {
        "id": 9
      },
      "owner": {
        "id": 1
      },
      "tenants": [
        {
          "id": 1,
          "name": "Stubby Toes Inc."
        }
      ],
      "datastores": [

      ]
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

This endpoint retrieves datastores of a specified cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/datastores`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cluster

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
order | asc | Sort direction, use 'desc' to reverse sort
phrase |  | Name filter, restricts query to only load datastores which contain the phrase specified
name |  | Name filter, restricts query to only load datastore of specified name
code |  | Code filter, restricts query to only load datastore of specified code
hideInactive | false | If true restricts query to only load active datastores


## Get a Specific Datastore

```shell
curl "$MORPHEUS_API_URL/api/clusters/1/datastores/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "datastore": {
    "id": 4,
    "name": "vsanDatastore",
    "code": null,
    "type": "vsan",
    "visibility": "privates",
    "storageSize": 3000483446784,
    "freeSpace": 1634729396798,
    "drsEnabled": false,
    "active": true,
    "allowWrite": true,
    "defaultStore": false,
    "online": true,
    "allowRead": true,
    "allowProvision": true,
    "refType": "ComputeServerGroup",
    "refId": 3,
    "externalId": "datastore-58601",
    "zone": {
      "id": 4
    },
    "zonePool": {
      "id": 9
    },
    "owner": {
      "id": 1
    },
    "tenants": [
      {
        "id": 1,
        "name": "Stubby Toes Inc."
      }
    ],
    "permissions": {
      "resourcePermissions": {
        "allGroups": true,
        "defaultStore": false,
        "allPlans": false,
        "defaultTarget": false,
        "morpheusResourceType": "Datastore",
        "morpheusResourceId": 4,
        "canManage": false,
        "all": true,
        "account": {
          "id": 1
        },
        "sites": [],
        "plans": []
      },
      "tenantPermissions": {
        "accounts": [           
          1
        ]
      }
    },
    "datastores": [

    ]
  }
}
```

This endpoint retrieves a specific cluster datastore.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:clusterId/datastores/:id`

### URL Parameters

Parameter | Description
--------- | -----------
Cluster ID | ID of the cluster
ID | ID of datastore


## Update Datastore

```shell
curl -XPUT "$MORPHEUS_API_URL/api/clusters/1/datastores/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"datastore": {
        "active": true,
        "permissions": {
          "resourcePermissions": {
            "all": true,
            "sites": [
              {
                "id": 2
              }
            ]
          },
          "tenantPermissions": {
            "accounts": [
              1
            ]
          }
        },
        "visibility": "private"
      }}'
```         

> The above command returns same JSON structure  [Get Datastore](#get-a-specific-datastore)

### HTTP Request

`PUT https://api.gomorpheus.com/api/clusters/:clusterId/datastores/:id`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the datastore

### JSON Cluster Parameters

Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
visibility | N | private | Visibility for datastore
active | N | true | Datastore active
permissions | N |  | Key for resource permission configuration, see [Permissions](#permissions)  

# Appliance Settings

Provides API interfaces for managing appliance settings within Morpheus

## Get Appliance Settings

```shell
curl "$MORPHEUS_API_URL/api/appliance-settings" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "applianceSettings": {
    "applianceUrl": "http://foo.com",
    "internalApplianceUrl": "172.16.0.1",
    "corsAllowed": "bar.com",
    "registrationEnabled": true,
    "defaultRoleId": "2",
    "defaultUserRoleId": "4",
    "dockerPrivilegedMode": true,
    "expirePwdDays": "1000",
    "disableAfterAttempts": "100",
    "disableAfterDaysInactive": "2000",
    "warnUserDaysBefore": "10",
    "smtpMailFrom": "dan.devilbiss@gmail.com",
    "smtpServer": "smtp.gmail.com",
    "smtpPort": "465",
    "smtpSSL": true,
    "smtpTLS": true,
    "smtpUser": "dan.devilbiss@gmail.com",
    "smtpPassword": "************",
    "proxyHost": "proxy.com",
    "proxyPort": "8080",
    "proxyUser": "ddevilbiss",
    "proxyPassword": "************",
    "proxyDomain": "proxy.com",
    "proxyWorkstation": "work",
    "currencyProvider": "openexchange",
    "currencyKey": "1234",
    "enabledZoneTypes": [
      {
        "id": 12,
        "name": "Amazon"
      }
    ]
  }
}     
```

This endpoint retrieves appliance settings.

### HTTP Request

`GET https://api.gomorpheus.com/api/appliance-settings`


## Update Appliance Settings

```shell
curl -XPUT "$MORPHEUS_API_URL/api/appliance-settings" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"applianceSettings": {
        "registrationEnabled": true,
        "applianceUrl": "http://10.0.2.2:8080/",
        "internalApplianceUrl": null,
        "corsAllowed": null,
        "dockerPrivilegedMode": true,
        "expirePwdDays": 30,
        "disableAfterAttempts": 5,
        "disableAfterDaysInactive": 90,
        "warnUserDaysBefore": 10,
        "smtpMailFrom": "stubby.toes@gmail.com",
        "smtpServer": "smtp.gmail.com",
        "smtpPort": 465,
        "smtpSSL": true,
        "smtpTLS": true,
        "smtpUser": "stubby.toes@gmail.com",
        "smtpPassword": "password",
        "proxyHost": null,
        "proxyPort": null,
        "proxyUser": "stubbytoes",
        "proxyPassword": "password",
        "proxyDomain": null,
        "proxyWorkstation": null,
        "currencyProvider": "openexchange",
        "currencyKey": null,
        "enableZoneTypes": [1, 2],
        "disableZoneTypes": [9],
        "defaultRoleId": 2,
        "defaultUserRoleId": 4
      }}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/appliance-settings`

### JSON Parameters

Parameter | Description
--------- | -----------
applianceUrl | Appliance URL
internalApplianceUrl | Internal Appliance URL (PXE)
corsAllowed | API Allowed Origins
registrationEnabled  | Registration enabled (true, false)
defaultRoleId | Default tenant role ID
defaultUserRoleId | Default user role ID
dockerPrivilegedMode | Docker privileged mode (true, false)
expirePwdDays | Expire password after days. Setting to 0 disabled this feature
disableAfterAttempts | Disable user after number of attempts. Set to 0 to disable this feature
disableAfterDaysInactive | Disable user if inactive for specified days. Set to 0 to disable this feature
warnUserDaysBefore | Send warning email number of days in advance before deactivating. Set to 0 to disable this feature
smtpFromEmail | From email address
stmpServer | SMTP server / host
smtpPort | SMTP port
smtpSSL | Use SSL for SMTP connection
smtpTLS | Use TLS for SMTP connections
smtpUser | SMTP username
smtpPassword | SMTP password
proxyHost | Proxy host
proxyPort | Proxy port
proxyUser | Proxy username
proxyPassword | Proxy password
proxyDomain | Proxy domain
proxyWorkstation | Proxy workstation
currencyProvider | Currency provider
currencyKey | Currency provider API key
enableAllZoneTypes | Set all cloud types enabled status on, overrides enableZoneTypes and disableZoneTypes parameters
enableZoneTypes | List of cloud type IDs to set enabled status on
disableZoneTypes | List of cloud type IDs to set enabled status off
disableAllZoneTypes | Set all cloud types enabled status off, can be used in conjunction with enableZoneTypes


# Service Plans

Provides API interfaces for managing service plans within Morpheus

## Get All Service Plans

```shell
curl "$MORPHEUS_API_URL/api/service-plans" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "servicePlans": [
    {
      "id": 1,
      "name": "Amazon T2 Nano - 1 Core, 0.5GB Memory",
      "code": "amazon-t2.nano",
      "active": true,
      "sortOrder": 0,
      "description": "Amazon T2 Nano - 1 Core, 0.5GB Memory",
      "maxStorage": 10737418240,
      "maxMemory": 536870912,
      "maxCpu": null,
      "maxCores": 1,
      "maxDisks": null,
      "customCpu": true,
      "customCores": true,
      "customMaxStorage": true,
      "customMaxDataStorage": true,
      "customMaxMemory": true,
      "addVolumes": true,
      "memoryOptionSource": null,
      "cpuOptionSource": null,
      "dateCreated": "2019-07-23T00:38:02+0000",
      "lastUpdated": "2019-07-23T00:38:02+0000",
      "regionCode": null,
      "visibility": "public",
      "editable": false,
      "provisionType": {
        "id": 6,
        "name": "Amazon",
        "code": "amazon",
        "rootDiskCustomizable": true,
        "addVolumes": true,
        "customizeVolume": true,
        "hasConfigurableCpuSockets": false
      },
      "tenants": "",
      "priceSets": [
        {
          "id": 43,
          "name": "Amazon - t2.nano - US West (N. California)",
          "code": "amazon.t2.nano.ec2.us-west-1.amazonaws.com",
          "priceUnit": "hour"
        }
      ],
      "config": {
      },
      "zones": [
        {
          "id": 3,
          "name": "dans aws cloud",
          "code": "dans_aws_cloud"
        },
        {
          "id": 5,
          "name": "dans aws cloud 2",
          "code": "amazon"
        }
      ]
    }
  ],
  "meta": {
    "size": 1,
    "total": 184,
    "max": 1,
    "offset": 0
  }
}
```

This endpoint retrieves all service plans.

### HTTP Request

`GET https://api.gomorpheus.com/api/service-plans`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase |  | Name, description and provision type name, restricts query to only load service plans which contain the phrase specified
includeZones | false | Indicates including zones in the service plan response payload
provisionTypeId |  | Provision type filter, restricts query to only load service plans of specified provision type
includeInactive | false | Can be used to include inactive service plans


## Get a Specific Service Plan

```shell
curl "$MORPHEUS_API_URL/api/service-plans/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "servicePlan": {
    "id": 1,
    "name": "Amazon T2 Nano - 1 Core, 0.5GB Memory",
    "code": "amazon-t2.nano",
    "active": true,
    "sortOrder": 0,
    "description": "Amazon T2 Nano - 1 Core, 0.5GB Memory",
    "maxStorage": 10737418240,
    "maxMemory": 536870912,
    "maxCpu": null,
    "maxCores": 1,
    "maxDisks": null,
    "customCpu": true,
    "customCores": true,
    "customMaxStorage": true,
    "customMaxDataStorage": true,
    "customMaxMemory": true,
    "addVolumes": true,
    "memoryOptionSource": null,
    "cpuOptionSource": null,
    "dateCreated": "2019-07-23T00:38:02+0000",
    "lastUpdated": "2019-07-23T00:38:02+0000",
    "regionCode": null,
    "visibility": "public",
    "editable": false,
    "provisionType": {
      "id": 6,
      "name": "Amazon",
      "code": "amazon",
      "rootDiskCustomizable": true,
      "addVolumes": true,
      "customizeVolume": true,
      "hasConfigurableCpuSockets": false
    },
    "tenants": "",
    "priceSets": [
      {
        "id": 43,
        "name": "Amazon - t2.nano - US West (N. California)",
        "code": "amazon.t2.nano.ec2.us-west-1.amazonaws.com",
        "priceUnit": "hour"
      }
    ],
    "config": {
    },
    "zones": [
      {
        "id": 3,
        "name": "dans aws cloud",
        "code": "dans_aws_cloud"
      },
      {
        "id": 5,
        "name": "dans aws cloud 2",
        "code": "amazon"
      }
    ],
    "permissions": {
    }
  }
}
```

This endpoint retrieves a specific service plan.

### HTTP Request

`GET https://api.gomorpheus.com/api/service-plans/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the service plan


## Create a Service Plan

Use this command to create a service plan.

```shell
curl -XPOST "$MORPHEUS_API_URL/api/service-plans" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"servicePlan": {
        "name": "stubby toes plan 1",
        "code": "stubby.toes.plan.1",
        "description": null,
        "provisionType": {
          "id": 1
        },
        "customCores": true,
        "config": {
          "ranges": {
              "maxStorage": null,
              "minMemory": 1073741824,
              "maxMemory": 1073741824,
              "minCores": 1,
              "maxCores": 4
          }
        },
        "maxStorage": 1073741824,
        "maxMemory": 1073741824,
        "priceSets": [
          {
              "id": 43
          }
        ],
        "visibility": "private",
        "permissions": {
          "resourcePermissions": {
              "all": true,
              "sites": [
                  {
                      "id": 4,
                      "default": true
                  }
              ]
          },
          "tenantPermissions": {
              "accounts": [
                  1,
                  2
              ]
          }
        }
      }}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`POST https://api.gomorpheus.com/api/service-plans`

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
name | Y | Service plan name
code | Y | Service plan code, must be unique
description | N | Service plan description
editable | N | Can be used to enable / disable the editability of the service plan. Default is on
maxStorage | Y | Max storage size in bytes
maxMemory | Y | Max memory size in bytes
maxCores | N | Max cores
maxDisks | N | Max disks allowed
provisionType.id | Y | Provision type ID
customCores | N | Can be used to enable / disable customizable cores. Default is off
customMaxStorage | N | Can be used to enable / disable customizable storage. Default is off
customMaxDataStorage | N | Can be used to enable / disable customizable extra volumes. Default is off
customMaxMemory | N | Can be used to enable / disable customizable memory. Default is off
addVolumes | N | Can be used to enable / disable ability to add volumes. Default is off
sortOrder | N | Sort order
priceSets.id | N | List of price sets to include in service plan
config.ranges | N | Key for service plan custom configuration, see [Config](#config)

#### Config

The `config` parameter is for custom ranges for the service plan.

Parameter | Required | Description
--------- | -------- | -----------
storageSizeType | N | Specifies range min / max storage multiplier [gb, mb]. Defaults to gb
memorySizeType | N | Specifies range min / max memory multiplier [mb, gb]. Defaults to mb.
range.minStorage | N | Custom min storage in GB (unless storageSizeType set to mb)  
range.maxStorage | N | Custom max storage in GB (unless storageSizeType set to mb)  
range.minMemory | N | Custom min memory in bytes
range.maxMemory | N | Custom max memory in bytes
range.minCores | N | Custom min cores
range.maxCores | N | Custom max cores


## Update a Service Plan

```shell
curl -XPUT "$MORPHEUS_API_URL/api/service-plans/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
  -H "Content-Type: application/json" \
  -d '{"servicePlan": {  
      "name": "stubby toes plan 1",
      "code": "stubby.toes.plan.1",
      "description": null,
      "editable": true,
      "maxStorage": 10737418240,
      "config": {
        "storageSizeType": "gb",
        "memorySizeType": "mb",
        "ranges": {
          "minStorage": 1000,
          "maxStorage": 100000,
          "minMemory": 536870912,
          "maxMemory": 1073741824,
          "minCores": 1,
          "maxCores": 3
        }
      },
      "maxMemory": 536870912,
      "maxCores": 3,
      "maxDisks": 5,
      "customCores": true,
      "customMaxStorage": true,
      "customMaxDataStorage": true,
      "customMaxMemory": true,
      "sortOrder": 5,
      "priceSets": [
        {
          "id": 170
        }
      ],
      "addVolumes": true,
      "provisionType": {
        "id": 1
      },
      "visibility": "private",
      "permissions": {
        "resourcePermissions": {
          "all": true,
          "sites": [
            {
              "id": 2
            },
            {
              "id": 4
            }
          ]
        },
        "tenantPermissions": {
          "accounts": [
            1
          ]
        }
      }
    }}'
```

> The above command returns JSON structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/service-plans/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the service plan

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
name | Y | Service plan name
code | Y | Service plan code, must be unique
description | N | Service plan description
editable | N | Can be used to enable / disable the editability of the service plan. Default is on
maxStorage | Y | Max storage size in bytes
maxMemory | Y | Max memory size in bytes
maxCores | N | Max cores
maxDisks | N | Max disks allowed
provisionType.id | Y | Provision type ID
customCores | N | Can be used to enable / disable customizable cores. Default is off
customMaxStorage | N | Can be used to enable / disable customizable storage. Default is off
customMaxDataStorage | N | Can be used to enable / disable customizable extra volumes. Default is off
customMaxMemory | N | Can be used to enable / disable customizable memory. Default is off
addVolumes | N | Can be used to enable / disable ability to add volumes. Default is off
sortOrder | N | Sort order
priceSets.id | N | List of price sets to include in service plan
config.ranges | N | Key for service plan custom configuration, see [Config](#config)


## Deactivate a Service Plan

```shell
curl -XPUT "$MORPHEUS_API_URL/api/service-plans/1/deactivate" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will deactivate a service plan

### HTTP Request

`PUT https://api.gomorpheus.com/api/service-plans/:id/deactivate`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the service plan

# Price Sets

Provides API interfaces for managing price sets within Morpheus

## Get All Price Sets

```shell
curl "$MORPHEUS_API_URL/api/price-sets" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "priceSets": [
    {
      "id": 25,
      "name": "Amazon - c1.medium - US West (N. California)",
      "code": "amazon.c1.medium.ec2.us-west-1.amazonaws.com",
      "active": true,
      "priceUnit": "hour",
      "type": "compute_plus_storage",
      "regionCode": "ec2.us-west-1.amazonaws.com",
      "systemCreated": false,
      "zone": null,
      "zonePool": null,
      "account": null,
      "prices": [
        {
          "id": 3,
          "name": "Amazon - EBS (gp2) - US West (N. California)",
          "code": "amazon.storage.ebs.ec2.us-west-1.amazonaws.com",
          "priceType": "storage",
          "priceUnit": "month",
          "additionalPriceUnit": "GB",
          "price": 0.12,
          "customPrice": 0.0,
          "markupType": null,
          "markup": 0.0,
          "markupPercent": 0.0,
          "cost": 0.12,
          "currency": "usd",
          "incurCharges": "always",
          "platform": null,
          "software": null,
          "volumeType": {
            "id": 10,
            "code": "amazon-gp2",
            "name": "gp2"
          },
          "datastore": null,
          "crossCloudApply": null,
          "account": null
        }
      ]
    }
  ],
  "meta": {
    "size": 1,
    "total": 169,
    "offset": 0,
    "max": 1
  }
}
```

This endpoint retrieves all price sets.

### HTTP Request

`GET https://api.gomorpheus.com/api/price-sets`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase |  | Restricts query to only load price sets with name or code containing the phrase specified
includeInactive | false | If true, include inactive prices in the results


## Get a Specific Price Set

```shell
curl "$MORPHEUS_API_URL/api/price-sets/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "priceSet": {
    "id": 25,
    "name": "Amazon - c1.medium - US West (N. California)",
    "code": "amazon.c1.medium.ec2.us-west-1.amazonaws.com",
    "active": true,
    "priceUnit": "hour",
    "type": "compute_plus_storage",
    "regionCode": "ec2.us-west-1.amazonaws.com",
    "systemCreated": false,
    "zone": null,
    "zonePool": null,
    "account": null,
    "prices": [
      {
        "id": 3,
        "name": "Amazon - EBS (gp2) - US West (N. California)",
        "code": "amazon.storage.ebs.ec2.us-west-1.amazonaws.com",
        "priceType": "storage",
        "priceUnit": "month",
        "additionalPriceUnit": "GB",
        "price": 0.12,
        "customPrice": 0.0,
        "markupType": null,
        "markup": 0.0,
        "markupPercent": 0.0,
        "cost": 0.12,
        "currency": "usd",
        "incurCharges": "always",
        "platform": null,
        "software": null,
        "volumeType": {
          "id": 10,
          "code": "amazon-gp2",
          "name": "gp2"
        },
        "datastore": null,
        "crossCloudApply": null,
        "account": null
      }
    ]
  }
}
```

This endpoint retrieves a specific price set.

### HTTP Request

`GET https://api.gomorpheus.com/api/price-sets/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the price set


## Create a Price Set

Use this command to create a price set.

```shell
curl -XPOST "$MORPHEUS_API_URL/api/price-sets" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"priceSet": {
        "name": "price set 1",
        "code": "price.set.1",
        "regionCode": "region.code.1",
        "zone": {
          "id": 3
        },
        "zonePool": {
          "id": 7
        },
        "priceUnit": "hour",
        "type": "compute_plus_storage",
        "prices": [
          {
            "id": 409
          },
          {
            "id": 124
          }
        ]
     }}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true,
  "id": 1
}
```

### HTTP Request

`POST https://api.gomorpheus.com/api/price-sets`

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
name | Y | Price set name
code | Y | Price set code, must be unique
regionCode | N | Price set region code
zone.id | N | Cloud ID
zonePool.id | N | Resource pool ID
priceUnit | Y | Price unit: minute, hour, day, month, year, two year, three year, four year, five year
type | Y | Price set type: fixed, compute_plus_storage, component
prices | N | List of price IDs to associate with price set


## Update a Price Set

```shell
curl -XPUT "$MORPHEUS_API_URL/api/price-sets/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
  -H "Content-Type: application/json" \
  -d '{"priceSet": {
          "name": "new price set name",
          "restartUsage": true,
          "prices": [
            {
              "id": 409
            },
            {
              "id": 124
            }
          ]
        }
      }
```

> The above command returns JSON structured like this:

```json
{
  "success": true
}'
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/price-sets/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the price set

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
name | N | Price set new name
restartUsage | N | Can be used to apply price changes to usage: true, false
prices | N | List of price IDs to associate with price set


## Deactivate a Price Set

```shell
curl -XPUT "$MORPHEUS_API_URL/api/price-sets/1/deactivate" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will deactivate a price set

### HTTP Request

`PUT https://api.gomorpheus.com/api/price-sets/:id/deactivate`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the price set

# Prices

Provides API interfaces for managing prices within Morpheus

## Get All Prices

```shell
curl "$MORPHEUS_API_URL/api/prices" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "prices": [
    {
      "id": 124,
      "name": "Amazon - c1.medium - US West (N. California) - Linux",
      "code": "amazon.c1.medium.ec2.us-west-1.amazonaws.com.Linux",
      "active": true,
      "priceType": "compute",
      "priceUnit": "hour",
      "additionalPriceUnit": null,
      "price": 0.148,
      "customPrice": 0.0,
      "markupType": null,
      "markup": 0.0,
      "markupPercent": 0.0,
      "cost": 0.148,
      "currency": "usd",
      "incurCharges": "running",
      "platform": "Linux",
      "software": null,
      "volumeType": null,
      "datastore": null,
      "crossCloudApply": null,
      "account": null
    }
  ],
  "meta": {
    "size": 1,
    "total": 411,
    "offset": 0,
    "max": 1
  }
}
```

This endpoint retrieves all prices.

### HTTP Request

`GET https://api.gomorpheus.com/api/prices`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase |  | Restricts query to only load prices with name or code containing the phrase specified
includeInactive | false | If true, include inactive prices in the results


## Get a Specific Price

```shell
curl "$MORPHEUS_API_URL/api/prices/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "price": {
    "id": 124,
    "name": "Amazon - c1.medium - US West (N. California) - Linux",
    "code": "amazon.c1.medium.ec2.us-west-1.amazonaws.com.Linux",
    "active": true,
    "priceType": "compute",
    "priceUnit": "hour",
    "additionalPriceUnit": null,
    "price": 0.148,
    "customPrice": 0.0,
    "markupType": null,
    "markup": 0.0,
    "markupPercent": 0.0,
    "cost": 0.148,
    "currency": "usd",
    "incurCharges": "running",
    "platform": "Linux",
    "software": null,
    "volumeType": null,
    "datastore": null,
    "crossCloudApply": null,
    "account": null
  }
}
```

This endpoint retrieves a specific price.

### HTTP Request

`GET https://api.gomorpheus.com/api/prices/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the price


## Create a Price

Use this command to create a price.

```shell
curl -XPOST "$MORPHEUS_API_URL/api/prices" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
        "price": {
          "name": "dan",
          "code": "dan",
          "account": {
            "id": 1
          },
          "priceType": "fixed",
          "priceUnit": "month",
          "incurCharges": "running",
          "currency": "USD",
          "cost": 10.5,
          "markupType": "fixed",
          "markup": 1.25
        }
      }'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true,
  "id": 1
}
```

### HTTP Request

`POST https://api.gomorpheus.com/api/prices`

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
name | Y | Price name
code | Y | Price code, must be unique
account.id | N | Assign to specified tenant account
priceType | Y | Price type **code**, see [Price Types](#price-types)
priceUnit | Y | Price unit: minute, hour, day, month, year, two year, three year, four year, five year
incurCharges | Y | Indicates when to incur charges: running, stopped, always
currency | Y | ISO Currency code
cost | Y | Cost
markupType | N | Price adjustment type: fixed, percent, custom
markup | N | Amount for fixed price adjustment type
markupPercent | N | Percent for percent price adjustment type
customPrice | N | Custom price for custom price adjustment type
platform | N | Platform, required for platform price type
software | N | Software, required for software price type
volumeType.id | N | Volume type ID, required for storage price type
datastore.id | N | Datastore ID, required for datastore price type
crossCloudApply | N | Apply price across clouds, optional true/false flag for datastore price type

#### Price Types
Type | Code
---- | ----
Everything | fixed
Memory + CPU | compute
Memory Only | memory
Cores Only | cores
Disk Only | storage
Datastore | datastore
Platform | platform
Software | software


## Update a Price

```shell
curl -XPUT "$MORPHEUS_API_URL/api/prices/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
        "price": {
          "name": "dan",
          "code": "dan",
          "account": {
            "id": 1
          },
          "priceType": "fixed",
          "priceUnit": "month",
          "incurCharges": "running",
          "currency": "USD",
          "cost": 10.5,
          "markupType": "fixed",
          "markup": 1.25
        }
      }'
```

> The above command returns JSON structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/prices/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the price

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
name | Y | Price name
priceType | Y | Price type **code**, see [Price Types](#price-types)
priceUnit | Y | Price unit: minute, hour, day, month, year, two year, three year, four year, five year
incurCharges | Y | Indicates when to incur charges: running, stopped, always
currency | Y | ISO Currency code
cost | Y | Cost
markupType | N | Price adjustment type: fixed, percent, custom
markup | N | Amount for fixed price adjustment type
markupPercent | N | Percent for percent price adjustment type
customPrice | N | Custom price for custom price adjustment type
platform | N | Platform, required for platform price type
software | N | Software, required for software price type
volumeType.id | N | Volume type ID, required for storage price type
datastore.id | N | Datastore ID, required for datastore price type
crossCloudApply | N | Apply price across clouds, optional true, false flag for datastore price type
restartUsage | N | Apply changes to usage


## Deactivate a Price

```shell
curl -XDELETE "$MORPHEUS_API_URL/api/prices/1/deactivate" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will deactivate a price

### HTTP Request

`PUT https://api.gomorpheus.com/api/prices/:id/deactivate`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the price

# Reports

Provides API interfaces for viewing report results and executing new reports.

## Get All Report Types

```shell
curl "$MORPHEUS_API_URL/api/report-types" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "reportTypes": [
    {
      "id": 21,
      "code": "appCost",
      "name": "Application Cost",
      "category": "cost",
      "dateCreated": "2018-05-02T07:44:46+0000",
      "optionTypes": [
        {
          "id": 1073,
          "name": "endDate",
          "code": "reportType.endDate",
          "description": null,
          "fieldName": "endDate",
          "fieldLabel": "End Date",
          "fieldContext": "report",
          "fieldGroup": null,
          "fieldClass": null,
          "fieldAddOn": null,
          "fieldComponent": null,
          "placeHolder": null,
          "helpBlock": "",
          "defaultValue": null,
          "optionSource": null,
          "type": "text",
          "advanced": false,
          "required": true,
          "editable": true,
          "creatable": null,
          "config": {
          },
          "displayOrder": 2,
          "wrapperClass": null,
          "enabled": true,
          "noBlank": false,
          "dependsOnCode": null,
          "contextualDefault": false
        }
      ]
    },
    {
      "id": 26,
      "code": "workloadSummary",
      "name": "Workload Summary",
      "category": "provisioningInventory",
      "dateCreated": "2018-09-10T08:18:04+0000",
      "optionTypes": [

      ]
    }
  ],
  "meta": {
    "size": 18,
    "total": 18,
    "offset": 0,
    "max": 25
  }
}
```

This endpoint retrieves all available report types. A report type has `optionTypes` that define the parameters available when executing a report of that type. The sample response has been abbreviated.

### HTTP Request

`GET https://api.gomorpheus.com/api/report-types`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase |  | If specified will return a partial match on name
name |  | If specified will return an exact match on name
code |  | If specified will return an exact match on code
category |  | If specified will return an exact match on category


## Get All Reports

```shell
curl "$MORPHEUS_API_URL/api/reports" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "reportResults": [
    {
      "id": 2,
      "type": {
        "id": 21,
        "code": "appCost",
        "name": "Application Cost"
      },
      "reportTitle": "Application Cost Jun 04, 2019 19:28:02",
      "filterTitle": "Jun 04, 2019",
      "status": "ready",
      "dateCreated": "2019-06-04T23:28:02+0000",
      "lastUpdated": "2019-06-04T23:28:02+0000",
      "startDate": null,
      "endDate": null,
      "config": {
        "type": "appCost"
      },
      "createdBy": {
        "id": 1,
        "username": "root"
      }
    {
      "id": 1,
      "type": {
        "id": 6,
        "code": "groupInventory",
        "name": "Group Inventory Summary"
      },
      "reportTitle": "Group Inventory Summary Jul 12, 2019 16:30:04",
      "filterTitle": "Jul 12, 2019 | All Clouds | foo:bar",
      "status": "ready",
      "dateCreated": "2019-07-12T20:30:04+0000",
      "lastUpdated": "2019-07-12T20:30:04+0000",
      "startDate": null,
      "endDate": null,
      "config": {
        "reportType": "groupInventory",
        "cloudId": "",
        "environment": "",
        "tagName": "foo",
        "tagValue": "bar"
      },
      "createdBy": {
        "id": 1,
        "username": "root"
      }
    }
  ],
  "meta": {
    "size": 2,
    "total": 2,
    "offset": 0,
    "max": 25
  }
}
```

This endpoint returns all reports. This is results of reports that have been executed in the past.

### HTTP Request

`GET https://api.gomorpheus.com/api/reports`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order, default is `dateCreated` with direction `desc`
direction | asc | Sort direction, use 'desc' to reverse sort
phrase |  | If specified will return a partial match on name
name |  | If specified will return an exact match on name
reportType |  | If specified will return an exact match on report type code, accepts multiple values
category |  | If specified will return an exact match on report type category, accepts multiple values

## Get a Specific Report

```shell
curl "$MORPHEUS_API_URL/api/reports/2" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "reportResult": {
    "id": 2,
    "type": {
      "id": 21,
      "code": "appCost",
      "name": "Application Cost"
    },
    "reportTitle": "Application Cost Jun 04, 2019 19:28:02",
    "filterTitle": "Jun 04, 2019",
    "status": "ready",
    "dateCreated": "2019-06-04T23:28:02+0000",
    "lastUpdated": "2019-06-04T23:28:02+0000",
    "startDate": null,
    "endDate": null,
    "config": {
      "type": "appCost"
    },
    "createdBy": {
      "id": 1,
      "username": "root"
    },
    "rows": [
      {
        "id": 536,
        "section": "header",
        "data": "{\"code\":\"totalCount\",\"name\":\"Apps\",\"value\":2",
        "displayOrder": 0
      },
      {
        "id": 535,
        "section": "header",
        "data": "{\"code\":\"totalCost\",\"name\":\"Total Cost\",\"value\":99.99,\"currency\":\"USD\"}",
        "displayOrder": 0
      },
      {
        "id": 534,
        "section": "main",
        "data": "{\"name\":\"testapp1\",\"cost\":0,\"price\":0,\"currency\":\"USD\"}",
        "displayOrder": 0
      },
      {
        "id": 533,
        "section": "main",
        "data": "{\"name\":\"testapp2\",\"cost\":99.99,\"price\":0,\"currency\":\"USD\"}",
        "displayOrder": 1
      }
    ]
  }
}
```

This endpoint retrieves a specific report result. The response includes the result data as `rows` which can be used to render the report.

### HTTP Request

`GET https://api.gomorpheus.com/api/reports/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the report result

## Download a Specific Report

```shell
curl "$MORPHEUS_API_URL/api/reports/download/2" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns `Content-Type: "application/octet-stream"` and `Content-disposition: attachment;filename=reportTitle.json`.

This endpoint downloads a specific report result as a file attachment. The default file format is `json`.

### HTTP Request

`GET https://api.gomorpheus.com/api/reports/download/:id(.:format)`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the report result
format | Format of the rendered report file, `json` or `csv`. The default is `.json`.


## Run a Report

```shell
curl -XPOST "$MORPHEUS_API_URL/api/reports" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "report": {
    "type": "appCost",
    "startDate": "2019-01-01",
    "endDate": "2020-01-01"
  }}'
```

> The above command returns JSON structured like getting a single report:

This endpoint execute the specified report type and create a new report result.

### HTTP Request

`POST https://api.gomorpheus.com/api/reports`

### JSON Report Parameters

Parameter | Default | Description
--------- | ------- | -----------
type     |  | The [Report Type](#report-types) code to be executed.

The available parameters vary by report type. Refer to the defined `optionTypes` for each report.

### JSON Common Report Parameters

Parameter | Default | Description
--------- | ------- | -----------
startDate     |  | The start date for the report
endDate     |  | The end date for the report
groupId     |  | The Group ID filter for the report
cloudId     |  | The Cloud ID filter for the report

## Delete a Report

```shell
curl -XDELETE "$MORPHEUS_API_URL/api/reports/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

This endpoint will delete a report result.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/reports/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the report result.

# Log Settings

Provides API interfaces for managing log settings within Morpheus

## Get Log Settings

```shell
curl "$MORPHEUS_API_URL/api/log-settings" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "logSettings": {
    "enabled": true,
    "retentionDays": "1",
    "syslogRules": [
      {
        "id": 1,
        "name": "local",
        "rule": "*.* @@localhost:1234"
      }
    ],
    "integrations": [
      {
        "name": "splunk",
        "enabled": true,
        "host": "foo.com",
        "port": "80"
      },
      {
        "name": "logrhythm",
        "enabled": false
      }
    ]
  }
}
```

This endpoint retrieves log settings.

### HTTP Request

`GET https://api.gomorpheus.com/api/log-settings`


## Update Log Settings

```shell
curl -XPUT "$MORPHEUS_API_URL/api/log-settings" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"logSettings": {
        "enabled": true,
        "retentionDays": 7,
        "syslogRules": [
          {
            "name": "local",
            "rule": "*.* @@localhost:4567"
          }
        ],
        "integrations": [
          {
            "name": "splunk",
            "enabled": true,
            "host": "foo.com",
            "port": 8080
          }
        ]
      }}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/log-settings`

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
enabled | N | Use this to enable / disable logs
retentionDays | N | Availability time frame in days
syslogRules | N | Key for syslog rules list, see [Syslog Rules](#syslog-rules)
integrations | N | Key for integrations rules list, see [Integrations](#integrations)

#### Syslog Rules

The `syslogRules` parameter is a list used for adding syslog forwarding rules to log settings.

Parameter | Required | Description
--------- | -------- | -----------
name | Y | Syslog name
rule | Y | Syslog rule, example: `*.* @@server:port`

#### Integrations

The `integrations` parameter is a list used for enabling / disabling integrations to log settings.

Parameter | Required | Description
--------- | -------- | -----------
name | Y | Integration name
enabled | N | Use this to enable / disable the integration. Host and port required when enabling.
host | - | Host of the integration, required when enabled is true  
port | - | Port of the integration, required when enabled is true


## Add Syslog Rule

```shell
curl -XPOST "$MORPHEUS_API_URL/api/log-settings/syslog-rules" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"syslogRule": {"name": "foo", "rule": "*.* @@bar.com:8080"}}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

<aside class="info">
This command will update existing syslog rule by specified name if already exists
</aside>

### HTTP Request

`POST https://api.gomorpheus.com/api/log-settings/syslog-rules`

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
syslogRule.name | Y | Syslog name
syslogRule.rule | Y | Syslog rule, example: `*.* @@server:port`


## Delete Syslog Rules

```shell
curl -XDELETE "$MORPHEUS_API_URL/api/log-settings/syslog-rules/1" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete the syslog rule matching the specified name.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/log-settings/syslog-rules/:id`

### URL Parameters

Parameter | Description
--------- | -----------
:id | ID of the syslog rule

# Backup Settings

Provides API interfaces for managing backup settings within Morpheus

## Get Backup Settings

```shell
curl "$MORPHEUS_API_URL/api/backup-settings" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "backupSettings": {
    "backupsEnabled": true,
    "createBackups": true,
    "backupAppliance": true,
    "defaultStorageBucket": {
      "id": 42,
      "name": "backups"
    },
    "defaultSchedule": {
      "id": 1,
      "code": "dailyAtMidnight",
      "name": "Daily at Midnight"
    },
    "retentionCount": 12
  }
}
```

This endpoint retrieves backup settings.

### HTTP Request

`GET https://api.gomorpheus.com/api/backup-settings`


## Update Backup Settings

```shell
curl -XPUT "$MORPHEUS_API_URL/api/backup-settings" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"backupSettings": {
         "backupsEnabled": false,
         "createBackups": false,
         "backupAppliance": true,
         "retentionCount": 7,
         "updateExisting": false,
         "defaultSchedule": {
           "id": 2
         },
         "defaultStorageBucket": {
           "id": 44,
         }
      }}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/backup-settings`

### JSON Parameters

Parameter | Required | Description
--------- | -------- | -----------
backupsEnabled | N | Use this to enable / disable scheduled backups
retentionCount | N | Maximum number of successful backups to retain
createBackups | N | Use this to enable / disable create backups
backupAppliance | N | When enabled, a Backup will be created to backup the Morpheus appliance database
updateExisting | N | Use this to update existing backups with new settings
defaultSchedule.id | N | ID of default backup schedule type
clearDefaultSchedule | N | Use this to clear existing default backup schedule
defaultStorageBucket.id | N | ID of default storage bucket
clearDefaultStorageBucket | N | Use this to clear default store bucket

# Approvals

Provides API interfaces for managing approvals within Morpheus

## Get All Approvals

```shell
curl "$MORPHEUS_API_URL/api/approvals" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "approvals": [
    {
      "id": 3,
      "name": "APPROVAL-0000003",
      "internalId": null,
      "externalId": null,
      "externalName": null,
      "requestType": "Instance Approval",
      "account": {
        "id": 1,
        "name": "Stubby Toes Inc."
      },
      "approver": {
        "id": 1,
        "name": "Stubby Toes Inc."
      },
      "accountIntegration": null,
      "status": "1 approved",
      "errorMessage": null,
      "dateCreated": "2019-11-07T02:35:15+0000",
      "lastUpdated": "2019-11-07T02:35:15+0000",
      "requestBy": "Stubby Toes"
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

This endpoint retrieves all approvals.

### HTTP Request

`GET https://api.gomorpheus.com/api/approvals`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase |  | Name, externalName and requestBy filter, restricts query to only load approvals which contain the phrase specified
name |  | Name filter, restricts query to only load approval matching name specified


## Get a Specific Approval

```shell
curl "$MORPHEUS_API_URL/api/approvals/3" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "approval": {
    "id": 3,
    "name": "APPROVAL-0000003",
    "internalId": null,
    "externalId": null,
    "externalName": null,
    "requestType": "Instance Approval",
    "account": {
      "id": 1,
      "name": "Stubby Toes Inc."
    },
    "approver": {
      "id": 1,
      "name": "Stubby Toes Inc."
    },
    "accountIntegration": null,
    "status": "1 cancelled",
    "errorMessage": null,
    "dateCreated": "2019-11-07T02:35:15+0000",
    "lastUpdated": "2019-11-07T02:35:15+0000",
    "requestBy": "Stubby Toes",
    "approvalItems": [
      {
        "id": 3,
        "name": null,
        "externalId": null,
        "externalName": null,
        "internalId": null,
        "approvedBy": "Stubby Toes",
        "deniedBy": "Stubby Toes",
        "status": "cancelled",
        "errorMessage": null,
        "dateCreated": "2019-11-07T02:35:15+0000",
        "lastUpdated": "2019-11-18T21:00:25+0000",
        "dateApproved": "2019-11-18T19:56:30+0000",
        "dateDenied": null,
        "approval": {
          "id": 3
        },
        "reference": {
          "id": 3,
          "type": "instance",
          "name": "dans-ubuntu-3",
          "displayName": "dans-ubuntu-3"
        }
      }
    ]
  }
}
```

This endpoint retrieves a specific approval.

### HTTP Request

`GET https://api.gomorpheus.com/api/approvals/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the approval


## Get a Specific Approval Item

```shell
curl "$MORPHEUS_API_URL/api/approval-items/3" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "approvalItem": {
    "id": 3,
    "name": null,
    "externalId": null,
    "externalName": null,
    "internalId": null,
    "approvedBy": "Stubby Toes",
    "deniedBy": "Stubby Toes",
    "status": "cancelled",
    "errorMessage": null,
    "dateCreated": "2019-11-07T02:35:15+0000",
    "lastUpdated": "2019-11-18T21:00:25+0000",
    "dateApproved": "2019-11-18T19:56:30+0000",
    "dateDenied": null,
    "approval": {
      "id": 3
    },
    "reference": {
      "id": 3,
      "type": "instance",
      "name": "dans-ubuntu-3",
      "displayName": "dans-ubuntu-3"
    }
  }
}
```

This endpoint retrieves a specific approval item

### HTTP Request

`GET https://api.gomorpheus.com/api/approval-items/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | ID of the approval item


## Update an Approval Item

```shell
curl -XPUT "$MORPHEUS_API_URL/api/approval-items/3/approve" \
  -H "Authorization: BEARER $MORPHEUS_API_TOKEN"
```

> The above command returns JSON structured like this:

```json
{
  "success": true
}
```

This endpoint updates a specific approval item based upon specified action

### HTTP Request

`PUT https://api.gomorpheus.com/api/approval-items/:id/:action`

### URL Parameters

Parameter | Required | Description
--------- | -------- | -----------
id | Y | ID of the approval item
action | Y | Approval item action [approve, deny, cancel]
