# Image Builds

Image Builds are used to generate [Virtual Images](#virtual-images) for  your Morpheus Library.

## Get All Image Builds

```shell
curl "https://api.gomorpheus.com/api/image-builds" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "imageBuilds": [
    {
      "id": 1,
      "account": {
        "id": 1,
        "name": "root"
      },
      "type": {
        "id": 1,
        "code": "vmware",
        "name": "VMware"
      },
      "site": {
        "id": 1,
        "name": "my-group"
      },
      "zone": {
        "id": 1,
        "name": "my-vmware"
      },
      "name": "testbuild",
      "description": "a test build",
      "bootScript": {
        "id": 2,
        "fileName": "debian standard"
      },
      "bootCommand": null,
      "preseedScript": {
        "id": 2,
        "fileName": "debian 8"
      },
      "scripts": [
        {
          "id": 114,
          "name": "blah.txt",
          "type": "bash",
          "phase": "postProvision"
        }
      ],
      "sshUsername": "builderbot",
      "sshPassword": "************",
      "storageProvider": null,
      "buildOutputName": "mytestbuild",
      "conversionFormats": null,
      "isCloudInit": false,
      "vmToolsInstalled": true,
      "keepResults": 2,
      "config": {
      },
      "lastResult": {
        "id": 70,
        "imageBuild": {
          "id": 21,
          "name": "testbuild"
        },
        "buildNumber": 6,
        "startDate": "2017-09-28T05:48:03Z",
        "endDate": null,
        "statusMessage": "Initializing",
        "statusPercent": 0.0,
        "statusEta": null,
        "status": "running",
        "errorMessage": null,
        "createdBy": {
          "username": "admin"
        },
        "tempInstance": null,
        "virtualImages": [

        ]
      },
      "executionCount": 2
    }
  ],
  "meta": {
    "size": 1,
    "total": 1,
    "offset": 0,
    "max": 25
  }
}
```

This endpoint retrieves all image builds associated with the account.

### HTTP Request

`GET https://api.gomorpheus.com/api/image-builds`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name |  | If specified will return an exact match on name
phrase |  | If specified will return a partial match on name

## Get a Specific Image Build


```shell
curl "https://api.gomorpheus.com/api/image-builds/4" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this *(config omited)* :

```json
{
  "imageBuild": {
    "id": 1,
    "account": {
      "id": 1,
      "name": "root"
    },
    "type": {
      "id": 1,
      "code": "vmware",
      "name": "VMware"
    },
    "site": {
      "id": 1,
      "name": "my-group"
    },
    "zone": {
      "id": 1,
      "name": "my-vmware"
    },
    "name": "testbuild",
    "description": "a test build",
    "bootScript": {
      "id": 2,
      "fileName": "debian standard"
    },
    "bootCommand": null,
    "preseedScript": {
      "id": 2,
      "fileName": "debian 8"
    },
    "scripts": [
      {
        "id": 114,
        "name": "cleanup.sh",
        "type": "bash",
        "phase": "postProvision"
      }
    ],
    "sshUsername": "builderbot",
    "sshPassword": "************",
    "storageProvider": null,
    "buildOutputName": null,
    "conversionFormats": null,
    "isCloudInit": false,
    "vmToolsInstalled": true,
    "keepResults": 2,
    "config": {
      "instance": {
        "layout": {
          "code": "vmware-1.0-single",
          "id": 142
        },
        "type": "vmware",
        "userGroup": {
          "id": ""
        }
      },
      "networkInterfaces": [
        {
          "primaryInterface": true,
          "network": {
            "id": "network-147"
          }
        }
      ],
      "volumes": [
        {
          "vId": 1752,
          "size": 10,
          "maxIOPS": null,
          "name": "root",
          "rootVolume": true,
          "storageType": 1,
          "datastoreId": "auto"
        }
      ],
      "storageControllers": [

      ],
      "zoneId": 1,
      "config": {
        "template": 1752,
        "vmwareResourcePoolId": "resgroup-123",
        "expose": 8080
      },
      "plan": {
        "code": "vm-512",
        "id": 75
      }
    },
    "lastResult": {
      "id": 70,
      "imageBuild": {
        "id": 21,
        "name": "testbuild"
      },
      "buildNumber": 6,
      "startDate": "2017-09-28T05:48:03Z",
      "endDate": null,
      "statusMessage": "Booting",
      "statusPercent": 20.0,
      "statusEta": null,
      "status": "running",
      "errorMessage": null,
      "createdBy": {
        "username": "admin"
      },
      "tempInstance": null,
      "virtualImages": [

      ]
    },
    "executionCount": 4
  },
  "imageBuildExecutions": [
    {
      "id": 70,
      "imageBuild": {
        "id": 21,
        "name": "testbuild"
      },
      "buildNumber": 6,
      "startDate": "2017-09-28T05:48:03Z",
      "endDate": null,
      "statusMessage": "Booting",
      "statusPercent": 20.0,
      "statusEta": null,
      "status": "running",
      "errorMessage": null,
      "createdBy": {
        "username": "admin"
      },
      "tempInstance": null,
      "virtualImages": [
        
      ]
    },
    {
      "id": 57,
      "imageBuild": {
        "id": 21,
        "name": "testbuild"
      },
      "buildNumber": 3,
      "startDate": "2017-09-27T02:41:26Z",
      "endDate": "2017-09-27T03:08:30Z",
      "statusMessage": null,
      "statusPercent": 100.0,
      "statusEta": null,
      "status": "success",
      "errorMessage": null,
      "createdBy": {
        "username": "admin"
      },
      "tempInstance": null,
      "virtualImages": [
        {
          "id": 1812,
          "name": "testbuild-1-156-1506480866464"
        }
      ]
    }
  ]
}
```

This endpoint retrieves a specific image build.


### HTTP Request

`GET https://api.gomorpheus.com/api/image-builds/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the image build to retrieve


## Create an Image Build

```shell
curl -XPOST "https://api.gomorpheus.com/api/image-builds" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "imageBuild": {
    "type": "vmware",
    "name": "builder test",
    "description": null,
    "site": {
      "id": 1
    },
    "zone": {
      "id": 1
    },
    "config": {
      "zoneId": 1,
      "instance": {
        "name": "builder test",
        "site": {
          "id": 1
        },
        "type": "vmware",
        "instanceType": {
          "code": "vmware"
        },
        "layout": {
          "id": 142
        },
        "plan": {
          "id": 76
        },
        "networkDomain": {
        }
      },
      "config": {
        "resourcePoolId": "resgroup-123",
        "template": 1232,
        "nestedVirtualization": "off",
        "expose": "8080"
      },
      "volumes": [
        {
          "id": -1,
          "rootVolume": true,
          "name": "root",
          "size": 10,
          "storageType": 1,
          "datastoreId": "autoCluster"
        }
      ],
      "networkInterfaces": [
        {
          "network": {
            "id": "network-147"
          },
          "networkInterfaceTypeId": 4
        }
      ]
    },
    "bootScript": {
      "id": 2
    },
    "preseedScript": {
      "id": 2
    },
    "scripts": [

    ],
    "sshUsername": "builderbot",
    "sshPassword": "password",
    "storageProvider": null,
    "isCloudInit": "off",
    "buildOutputName": null,
    "conversionFormats": null,
    "keepResults": 0
  }
}'
```

> The above command returns JSON structured like getting a single image build.

### HTTP Request

`POST https://api.gomorpheus.com/api/image-builds`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | A name for the image build
description      |  | A description for the image build
type      |  | The image builder type.  [vmware]
site      |  | Group
zone      |  | Cloud
config      |  | A map of config values. This is the instance config that is used for provisioning. See [Provisioning Types](#provisioning).
bootScript      |  | Boot Script
preseedScript      |  | Preseed Script
sshUsername      |  | SSH Username
sshPassword      |  | SSH Password
storageProvider      |  | Storage Provider
isCloudInit      |  | Cloud Init
buildOutputName      |  | Build Output Name
conversionFormats      |  | Conversion Formats - ie. ovf, qcow2, vhd
keepResults      |  0 | Keep Results - Keep only the most recent builds. Older executions will be deleted along with their associated Virtual Images. The value 0 disables this functionality.

## Update an Image Build

```shell
curl -XPUT "https://api.gomorpheus.com/api/image-builds/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "imageBuild": {
    "description": "a good build",
    "keepResults": 5,
  }
}'
```

> The above command returns JSON structured like getting a single image build.

### HTTP Request

`PUT https://api.gomorpheus.com/api/image-builds/1`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the image build

### JSON Parameters

See [Create](#create-an-image-build).

## Delete an Image Build

```shell
curl -XDELETE "https://api.gomorpheus.com/api/image-builds/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

Will delete an image build from the system and make it no longer usable.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/image-builds/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the image build

## Run an Image Build

```shell
curl -XPOST "https://api.gomorpheus.com/api/image-builds/1/run" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "success": true
}
```

Running an image build is done asynchronously.  This api will kick off the new execution and update the image build status.

### HTTP Request

`POST https://api.gomorpheus.com/api/image-builds/1/run`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the image build

## List Image Build Executions

```shell
curl "https://api.gomorpheus.com/api/image-builds/1/list-executions" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "imageBuildExecutions": [
    {
      "id": 82,
      "imageBuild": {
        "id": 20,
        "name": "my-testbuild"
      },
      "buildNumber": 2,
      "startDate": "2017-09-29T15:30:07Z",
      "endDate": null,
      "statusMessage": "Installing",
      "statusPercent": 25.0,
      "statusEta": null,
      "status": "running",
      "errorMessage": null,
      "createdBy": {
        "username": "admin"
      },
      "tempInstance": null,
      "virtualImages": [

      ]
    },
    {
      "id": 81,
      "imageBuild": {
        "id": 20,
        "name": "my-testbuild"
      },
      "buildNumber": 1,
      "startDate": "2017-09-29T14:57:33Z",
      "endDate": "2017-09-29T15:26:41Z",
      "statusMessage": null,
      "statusPercent": 100.0,
      "statusEta": null,
      "status": "success",
      "errorMessage": null,
      "createdBy": {
        "username": "admin"
      },
      "tempInstance": null,
      "virtualImages": [
        {
          "id": 1850,
          "name": "my-testbuild-4-176-1506697891084"
        }
      ]
    }
  ],
  "imageBuildExecutionCount": 2,
  "meta": {
    "offset": 0,
    "max": 25,
    "size": 2,
    "total": 2
  }
}
```

List all executions for an image build.  This same info is also returned by the image build [GET](#get-a-specific-image-build) api, which returns the 100 most recent executions.

### HTTP Request

`GET https://api.gomorpheus.com/api/image-builds/1/list-executions`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the image build

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
buildNumber |  | If specified will return an exact match on buildNumber
status |  | Filter by status  [running, success, failed]
