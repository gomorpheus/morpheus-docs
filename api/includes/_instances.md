# Instances

Instances are sets of containers or vms (morpheus API represents a vm as a container attached to a server) of various types that can be provisioned across the Morpheus stack and offer a wide range of services. MySQL, Redis, ElasticSearch, PostgreSQL, Tomcat, nginx, Confluence, Jenkins, and more. There are a few important concept differentiators between what morpheus calls an instance and what amazon calls an instance. In morpheus an isntance can represent many vms or containers that are of a set. For example. If you wanted to spin up a Mongo sharded replicaset, that requires 7 virtual machines or 7 docker containers. Morpheus represents this as a singular instance with a specified layout and then represents all the associated services running within that instance as containers. If, a container record is a docker container then the `serverId` it belongs to is representative of the Docker Host it was provisioned onto. If the container is a virtual machine then the serverId represents the compute resource it was provisioned onto, (i.e. the virtual machine).

## Get All Instances

```shell
curl "https://api.gomorpheus.com/api/instances?max=3"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "instances": [
    {
      "id": 1530,
      "accountId": 1,
      "instanceType": {
        "id": 35,
        "code": "ubuntu",
        "category": "os",
        "name": "Ubuntu"
      },
      "group": {
        "id": 3,
        "name": "Demo"
      },
      "cloud": {
        "id": 6,
        "name": "San Mateo VMware"
      },
      "containers": [
        1798
      ],
      "servers": [
        2
      ],
      "connectionInfo": [
        {
          "ip": "192.168.162.59",
          "port": 22
        }
      ],
      "layout": {
        "id": 105
      },
      "plan": {
        "id": 12,
        "code": "vm-2048"
      },
      "name": "ah-San Mateo VMware-ubuntu",
      "description": null,
      "instanceVersion": null,
      "dateCreated": "2017-01-31T21:30:49+0000",
      "lastUpdated": "2017-02-07T22:58:26+0000",
      "hostName": "ah-San-Mateo-VMware-ubuntu",
      "domainName": null,
      "environmentPrefix": null,
      "firewallEnabled": true,
      "networkLevel": "container",
      "autoScale": false,
      "instanceContext": "production",
      "currentDeployId": null,
      "status": "running",
      "statusMessage": null,
      "errorMessage": null,
      "statusDate": "2017-01-31T21:34:07+0000",
      "statusPercent": null,
      "statusEta": null,
      "userStatus": null,
      "createdBy": {
        "id": 38
      }
    },
    {
      "id": 1653,
      "accountId": 1,
      "instanceType": {
        "id": 35,
        "code": "ubuntu",
        "category": "os",
        "name": "Ubuntu"
      },
      "group": {
        "id": 3,
        "name": "Demo"
      },
      "cloud": {
        "id": 6,
        "name": "San Mateo VMware"
      },
      "containers": [
        1945
      ],
      "servers": [
        2
      ],
      "connectionInfo": [
        {
          "ip": "192.168.163.55",
          "port": 22
        }
      ],
      "layout": {
        "id": 105
      },
      "plan": {
        "id": 11,
        "code": "vm-1024"
      },
      "name": "ah-San Mateo VMware-ubuntu-PDNStest",
      "description": null,
      "instanceVersion": null,
      "dateCreated": "2017-02-10T14:27:42+0000",
      "lastUpdated": "2017-02-10T14:31:19+0000",
      "hostName": "ah-san-mateo-vmware-ubuntu-pdnstest",
      "domainName": null,
      "environmentPrefix": null,
      "firewallEnabled": true,
      "networkLevel": "container",
      "autoScale": false,
      "instanceContext": "dev",
      "currentDeployId": null,
      "status": "running",
      "statusMessage": null,
      "errorMessage": null,
      "statusDate": "2017-02-10T14:30:43+0000",
      "statusPercent": null,
      "statusEta": null,
      "userStatus": null,
      "createdBy": {
        "id": 38
      }
    },
    {
      "id": 1624,
      "accountId": 1,
      "instanceType": {
        "id": 21,
        "code": "apache",
        "category": "web",
        "name": "Apache"
      },
      "group": {
        "id": 163,
        "name": "snow-approvals"
      },
      "cloud": {
        "id": 6,
        "name": "San Mateo VMware"
      },
      "containers": [
        1912
      ],
      "servers": [
        3
      ],
      "connectionInfo": [
        {
          "ip": "192.168.163.28",
          "port": 10009
        }
      ],
      "layout": {
        "id": 48
      },
      "plan": {
        "id": 3,
        "code": "container-256"
      },
      "name": "approval-snow-test",
      "description": null,
      "instanceVersion": null,
      "dateCreated": "2017-02-09T06:45:30+0000",
      "lastUpdated": "2017-02-09T06:53:20+0000",
      "hostName": "approval-snow-test",
      "domainName": null,
      "environmentPrefix": null,
      "firewallEnabled": true,
      "networkLevel": "container",
      "autoScale": false,
      "instanceContext": null,
      "currentDeployId": null,
      "status": "running",
      "statusMessage": null,
      "errorMessage": null,
      "statusDate": "2017-02-09T06:53:20+0000",
      "statusPercent": null,
      "statusEta": null,
      "userStatus": null,
      "createdBy": {
        "id": 25
      }
    }
  ],
  "stats": {
    "1530": {
      "usedStorage": 6776664064,
      "maxStorage": 21067075584,
      "usedMemory": 1909739520,
      "maxMemory": 2098315264,
      "usedCpu": 1.0926682792
    },
    "1653": {
      "usedStorage": 2662801408,
      "maxStorage": 10499452928,
      "usedMemory": 935444480,
      "maxMemory": 1041350656,
      "usedCpu": 0.1501000667
    },
    "1624": {
      "usedStorage": 4829184,
      "maxStorage": 3103539200,
      "usedMemory": 9113600,
      "maxMemory": 268435456,
      "usedCpu": 0
    }
  },
  "loadBalancers": [],
  "meta": {
    "offset": 0,
    "max": "3",
    "size": 3,
    "total": 21
  }
}

```

This endpoint retrieves all instances and their JSON encoded configuration attributes based on check type. Server data is encrypted in the database.

### HTTP Request

`GET https://api.gomorpheus.com/api/instances`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
name | null | Filter by name
phrase | null | Filter by wildcard search of name and description
instanceType | null | Filter by instance type code
lastUpdated | null | Date filter, restricts query to only load instances updated  timestamp is more recent or equal to the date specified
createdBy | null | Filter by Created By (User) ID. Accepts multiple values.

## Get a Specific Instance


```shell
curl "https://api.gomorpheus.com/api/instances/1216" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "success": true,
  "instance": {
    "id": 1698,
    "accountId": 1,
    "instanceType": {
      "id": 44,
      "code": "redis",
      "category": "cache",
      "name": "Redis"
    },
    "group": {
      "id": 3,
      "name": "Demo"
    },
    "cloud": {
      "id": 6,
      "name": "San Mateo VMware"
    },
    "containers": [
      19
    ],
    "servers": [
      2
    ],
    "connectionInfo": [
      {
        "ip": "10.211.55.11",
        "port": 10000
      }
    ],
    "layout": {
      "id": 221
    },
    "plan": {
      "id": 69,
      "code": "container-512"
    },
    "name": "redistest",
    "description": null,
    "instanceVersion": null,
    "tags": [

    ],
    "maxMemory": 536870912,
    "maxStorage": 5368709120,
    "maxCores": 0,
    "maxCpu": null,
    "dateCreated": "2016-10-25T15:12:06+0000",
    "lastUpdated": "2017-02-13T19:22:00+0000",
    "hostName": "redistest",
    "domainName": null,
    "environmentPrefix": null,
    "firewallEnabled": true,
    "networkLevel": "container",
    "autoScale": false,
    "instanceContext": null,
    "currentDeployId": null,
    "status": "running",
    "statusMessage": null,
    "errorMessage": null,
    "statusDate": "2016-10-25T15:12:41+0000",
    "statusPercent": null,
    "statusEta": null,
    "userStatus": null,
    "createdBy": {
      "id": 1
    }
  },
  "stats": {
    "usedStorage": 2951,
    "maxStorage": 1073741824,
    "usedMemory": 266240,
    "maxMemory": 268435456,
    "usedCpu": 0.0418375032
  }
}
```

This endpoint retrieves a specific instance.

### HTTP Request

`GET https://api.gomorpheus.com/api/instances/:id`

## Get Env Variables

```shell
curl "https://api.gomorpheus.com/api/instances/1216/envs" \
  -H "Authorization: BEARER access_token"
```
> The above command returns JSON structured like this:

```json
{
  "envs": [
    {
      "export": false,
      "masked": false,
      "name": "DATABASE_NAME",
      "value": "spud_marketing"
    }
  ],
  "readOnlyEnvs": {
    "TOMCAT_HOST": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_HOST",
      "value": "container1414"
    },
    "TOMCAT_HOST_2": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_HOST_2",
      "value": "container1759"
    },
    "TOMCAT_IP": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_IP",
      "value": "192.168.163.232"
    },
    "TOMCAT_IP_2": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_IP_2",
      "value": "192.168.163.233"
    },
    "TOMCAT_PORT": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_PORT",
      "value": 10017
    },
    "TOMCAT_PORT_2": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_PORT_2",
      "value": 10017
    },
    "TOMCAT_PORT_8080_TCP": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_PORT_8080_TCP",
      "value": "tcp://192.168.163.232:10017"
    },
    "TOMCAT_PORT_8080_TCP_2": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_PORT_8080_TCP_2",
      "value": "tcp://192.168.163.233:10017"
    },
    "TOMCAT_PORT_8080_TCP_ADDR": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_PORT_8080_TCP_ADDR",
      "value": "192.168.163.232"
    },
    "TOMCAT_PORT_8080_TCP_ADDR_2": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_PORT_8080_TCP_ADDR_2",
      "value": "192.168.163.233"
    },
    "TOMCAT_PORT_8080_TCP_PORT": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_PORT_8080_TCP_PORT",
      "value": 10017
    },
    "TOMCAT_PORT_8080_TCP_PORT_2": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_PORT_8080_TCP_PORT_2",
      "value": 10017
    },
    "TOMCAT_PORT_8080_TCP_PROTO": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_PORT_8080_TCP_PROTO",
      "value": "tcp"
    },
    "TOMCAT_PORT_8080_TCP_PROTO_2": {
      "export": true,
      "masked": false,
      "name": "TOMCAT_PORT_8080_TCP_PROTO_2",
      "value": "tcp"
    }
  },
  "importedEnvs": {
    "MYSQL_HOST": {
      "export": true,
      "masked": false,
      "name": "MYSQL_HOST",
      "value": "container1413"
    },
    "MYSQL_HOST_2": {
      "export": true,
      "masked": false,
      "name": "MYSQL_HOST_2",
      "value": "container1756"
    },
    "MYSQL_IP": {
      "export": true,
      "masked": false,
      "name": "MYSQL_IP",
      "value": "192.168.163.232"
    },
    "MYSQL_IP_2": {
      "export": true,
      "masked": false,
      "name": "MYSQL_IP_2",
      "value": "192.168.163.233"
    },
    "MYSQL_MASTER": {
      "export": true,
      "masked": false,
      "name": "MYSQL_HOST",
      "value": "container1413"
    },
    "MYSQL_PASSWORD": {
      "export": true,
      "masked": true,
      "name": "MYSQL_PASSWORD",
      "value": "morpheus"
    },
    "MYSQL_PASSWORD_2": {
      "export": true,
      "masked": true,
      "name": "MYSQL_PASSWORD",
      "value": "morpheus"
    },
    "MYSQL_PORT": {
      "export": true,
      "masked": false,
      "name": "MYSQL_PORT",
      "value": 10016
    },
    "MYSQL_PORT_2": {
      "export": true,
      "masked": false,
      "name": "MYSQL_PORT_2",
      "value": 10016
    },
    "MYSQL_PORT_3306_TCP": {
      "export": true,
      "masked": false,
      "name": "MYSQL_PORT_3306_TCP",
      "value": "tcp://192.168.163.232:10016"
    },
    "MYSQL_PORT_3306_TCP_2": {
      "export": true,
      "masked": false,
      "name": "MYSQL_PORT_3306_TCP_2",
      "value": "tcp://192.168.163.233:10016"
    },
    "MYSQL_PORT_3306_TCP_ADDR": {
      "export": true,
      "masked": false,
      "name": "MYSQL_PORT_3306_TCP_ADDR",
      "value": "192.168.163.232"
    },
    "MYSQL_PORT_3306_TCP_ADDR_2": {
      "export": true,
      "masked": false,
      "name": "MYSQL_PORT_3306_TCP_ADDR_2",
      "value": "192.168.163.233"
    },
    "MYSQL_PORT_3306_TCP_PORT": {
      "export": true,
      "masked": false,
      "name": "MYSQL_PORT_3306_TCP_PORT",
      "value": 10016
    },
    "MYSQL_PORT_3306_TCP_PORT_2": {
      "export": true,
      "masked": false,
      "name": "MYSQL_PORT_3306_TCP_PORT_2",
      "value": 10016
    },
    "MYSQL_PORT_3306_TCP_PROTO": {
      "export": true,
      "masked": false,
      "name": "MYSQL_PORT_3306_TCP_PROTO",
      "value": "tcp"
    },
    "MYSQL_PORT_3306_TCP_PROTO_2": {
      "export": true,
      "masked": false,
      "name": "MYSQL_PORT_3306_TCP_PROTO_2",
      "value": "tcp"
    },
    "MYSQL_USERNAME": "morpheus",
    "MYSQL_USERNAME_2": "morpheus"
  }
}
```

This gets all the environment variables associated with the instance.


### HTTP Request

`GET https://api.gomorpheus.com/api/instances/:id/envs`

## Get Instance History

```shell
curl "https://api.gomorpheus.com/api/238/history" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "processes": [
    {
      "id": 250,
      "accountId": 1,
      "uniqueId": "cebc47ec-cb2f-417a-886e-dd60cf81db26",
      "processType": {
        "code": "provision",
        "name": "provision"
      },
      "description": null,
      "subType": null,
      "subId": null,
      "zoneId": 34,
      "integrationId": null,
      "instanceId": 238,
      "containerId": 240,
      "serverId": 601,
      "containerName": "apachetest",
      "displayName": "apachetest",
      "timerCategory": "vmware",
      "timerSubCategory": "28",
      "status": "failed",
      "reason": null,
      "percent": 100.0,
      "statusEta": 348246,
      "message": null,
      "output": null,
      "error": null,
      "startDate": "2018-09-28T19:10:56+0000",
      "endDate": "2018-09-28T20:21:49+0000",
      "duration": 4253127,
      "dateCreated": "2018-09-28T19:10:56+0000",
      "lastUpdated": "2018-09-28T20:21:49+0000",
      "createdBy": {
        "username": "admin",
        "displayName": "Admin"
      },
      "updatedBy": {
        "username": "admin",
        "displayName": "Admin"
      },
      "events": [

      ]
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

This endpoint retrieves the process history for a specific instance. 

Alternatively, the [Process History](#get-all-processes) endpoint can be used to get the same information.

### HTTP Request

`GET https://api.gomorpheus.com/api/instances/:id/history`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
phrase |  | If specified will return a partial match on displayName, message or output
containerId |  | Filter by container id(s)
serverId |  | Filter by server id(s)
zoneId |  | Filter by zone id(s)

## Get Container Details

```shell
curl "https://api.gomorpheus.com/api/instances/1216/containers" \
  -H "Authorization: BEARER access_token"
```
> The above command returns JSON structured like this:

```json
{
  "containers": [
    {
      "id": 292,
      "accountId": 1,
      "instance": {
        "id": 294,
        "name": "nginxtest"
      },
      "containerType": {
        "id": 187,
        "code": "nginx-vmware-1.9",
        "category": "nginx",
        "name": "NGINX 1.9"
      },
      "containerTypeSet": {
        "id": 193,
        "code": "nginx-vmware-1.9-set",
        "category": "nginx"
      },
      "server": {
        "id": 653,
        "name": "nginxtest"
      },
      "cloud": {
        "id": 34,
        "name": "myvmware"
      },
      "name": "nginxtest_292",
      "ip": "10.30.20.50",
      "internalIp": "10.30.20.50",
      "internalHostname": "container292",
      "externalHostname": "nginxtest",
      "externalDomain": "localdomain",
      "externalFqdn": "nginxtest.localdomain",
      "ports": [
        {
          "index": 0,
          "external": 80,
          "internal": 80,
          "primaryPort": true,
          "displayName": "Http",
          "export": true,
          "visible": true,
          "loadBalance": true,
          "link": true,
          "exportName": "HTTP",
          "protocol": "http",
          "code": "nginx.80"
        },
        {
          "index": 1,
          "external": 443,
          "internal": 443,
          "primaryPort": false,
          "displayName": "Https",
          "export": true,
          "visible": true,
          "loadBalance": true,
          "link": true,
          "exportName": "HTTPS",
          "protocol": "https",
          "code": "nginx.443"
        }
      ],
      "plan": {
        "id": 76,
        "code": "vm-1024",
        "name": "1 CPU, 1GB Memory"
      },
      "dateCreated": "2019-02-20T18:29:05+0000",
      "lastUpdated": "2019-02-27T21:07:35+0000",
      "statsEnabled": true,
      "status": "running",
      "userStatus": "running",
      "environmentPrefix": null,
      "stats": {
        "ts": "2019-02-27T21:07:31+0000",
        "running": true,
        "userCpuUsage": 0.1504010695,
        "systemCpuUsage": 0.1838235294,
        "usedMemory": 317256000,
        "maxMemory": 1017032000,
        "cacheMemory": 404236000,
        "maxStorage": 10499452928,
        "usedStorage": 3700285440,
        "readIOPS": 0,
        "writeIOPS": 0.35,
        "totalIOPS": 0.35,
        "iops": {
        },
        "netTxUsage": 114,
        "netRxUsage": 2198
      },
      "runtimeInfo": {
      },
      "containerVersion": null,
      "repositoryImage": null,
      "planCategory": null,
      "hostname": "nginxtest",
      "domainName": null,
      "volumeCreated": true,
      "containerCreated": false,
      "maxStorage": 10737418240,
      "maxMemory": 1073741824,
      "maxCores": 1,
      "maxCpu": 1,
      "availableActions": [
        {
          "code": "nginx-1.9-remove-node",
          "name": "Remove Nginx Node"
        }
      ]
    }
  ]
}
```

This can be valuable for evaluating the details of the compute server(s) running on an instance

### HTTP Request

`GET https://api.gomorpheus.com/api/instances/:id/containers`

## Get Available Service Plans for an Instance

```shell
curl -XGET "https://api.gomorpheus.com/api/instances/service-plans?zoneId=1&layoutId=75" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "plans": [
    {
      "id": 75,
      "name": "1 CPU, 512MB Memory",
      "value": 75,
      "code": "vm-512",
      "maxStorage": 10737418240,
      "maxMemory": 536870912,
      "maxCpu": 1,
      "maxCores": 1,
      "customCpu": false,
      "customMaxMemory": false,
      "customMaxStorage": true,
      "customMaxDataStorage": true,
      "customCoresPerSocket": false,
      "coresPerSocket": 1,
      "storageTypes": [
        {
          "id": 1,
          "editable": false,
          "optionTypes": [

          ],
          "displayOrder": 1,
          "code": "standard",
          "volumeType": "disk",
          "minStorage": null,
          "deletable": false,
          "defaultType": true,
          "createDatastore": null,
          "resizable": false,
          "storageType": null,
          "allowSearch": true,
          "volumeOptionSource": null,
          "displayName": "Disk",
          "minIOPS": null,
          "maxIOPS": null,
          "hasDatastore": true,
          "customSize": true,
          "autoDelete": true,
          "name": "Standard",
          "configurableIOPS": false,
          "customLabel": true,
          "enabled": true,
          "description": "Standard",
          "volumeCategory": "disk",
          "externalId": null,
          "maxStorage": null
        }
      ],
      "rootStorageTypes": [
        {
          "id": 1,
          "editable": false,
          "optionTypes": [

          ],
          "displayOrder": 1,
          "code": "standard",
          "volumeType": "disk",
          "minStorage": null,
          "deletable": false,
          "defaultType": true,
          "createDatastore": null,
          "resizable": false,
          "storageType": null,
          "allowSearch": true,
          "volumeOptionSource": null,
          "displayName": "Disk",
          "minIOPS": null,
          "maxIOPS": null,
          "hasDatastore": true,
          "customSize": true,
          "autoDelete": true,
          "name": "Standard",
          "configurableIOPS": false,
          "customLabel": true,
          "enabled": true,
          "description": "Standard",
          "volumeCategory": "disk",
          "externalId": null,
          "maxStorage": null
        }
      ],
      "addVolumes": true,
      "customizeVolume": true,
      "rootDiskCustomizable": true,
      "noDisks": false,
      "hasDatastore": true,
      "minDisk": 0,
      "maxDisk": null,
      "lvmSupported": true,
      "datastores": {
        "cluster": [
          {
            "id": 54,
            "name": "demo-qnap - 4.3TB Free"
          }
        ],
        "store": [
          {
            "id": 50,
            "name": "datastore1 - 463.4GB Free"
          }
        ]
      },
      "supportsAutoDatastore": true,
      "autoOptions": [
        {
          "id": "autoCluster",
          "name": "Auto - Cluster"
        },
        {
          "id": "auto",
          "name": "Auto - Datastore"
        }
      ],
      "cpuOptions": [

      ],
      "coreOptions": [

      ],
      "memoryOptions": [

      ],
      "rootCustomSizeOptions": {
      },
      "customSizeOptions": {
      },
      "customCores": false,
      "maxDisks": null,
      "memorySizeType": "MB"
    }
  ]
}
```

This returns a list of all of the service plans available for an instance type. The response includes details about the plans and their configuration options. The parameters *zoneId* and *layoutId* are required.

This endpoint can  be used to get the list of plans available for creating a new instance or resizing an existing instance.

### HTTP Request

`GET https://api.gomorpheus.com/api/instances/service-plans`

### Query Parameters

Parameter | Description
--------- | -----------
zoneId | The ID of the [Cloud](#compute-zones)
layoutId | The ID of the instance layout

## Create an Instance

See [Provisioning](#provisioning) for details.

### HTTP Request

`POST https://api.gomorpheus.com/api/instances`

## Updating an Instance

```shell
curl -X PUT "https://api.gomorpheus.com/api/instances/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "instance": {
  "description": "my new redis"
  }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single check

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id`

### JSON Instance Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | Unique name scoped to your account for the instance
description |  | Optional description field
tags |  | Tags
instanceContext |  | Environment
metadata |  | Array of metadata objects
powerScheduleType |  | Power Schedule ID
site.id |  | Group ID

## Stop an Instance

```shell
curl -X PUT "https://api.gomorpheus.com/api/instances/1/stop" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

This will stop all containers running within an instance.

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id/stop`

## Start an Instance

```shell
curl -X PUT "https://api.gomorpheus.com/api/instances/1/start" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

This will start all containers running within an instance.

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id/start`

## Restart an Instance

```shell
curl -X PUT "https://api.gomorpheus.com/api/instances/1/restart" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

This will restart all containers running within an instance. This includes rebuilding the environment variables and applying settings to the docker containers.

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id/restart`

## Suspend an Instance

```shell
curl -X PUT "https://api.gomorpheus.com/api/instances/1/suspend" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

This will suspend all containers in the instance.

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id/eject`

## Eject an Instance

```shell
curl -X PUT "https://api.gomorpheus.com/api/instances/1/eject" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

This will eject any ISO media on all containers in the instance.

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id/eject`

## Resize an Instance

```shell
curl -X PUT "https://api.gomorpheus.com/api/instances/1/resize" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "instance": {
    "id": 1,
    "plan": {
      "id": 15
    }
  },
  "volumes": [
    {
      "id": "-1",
      "rootVolume": true,
      "name": "root",
      "size": 20,
      "sizeId": null,
      "storageType": null,
      "datastoreId": null
    }
  ],
  "deleteOriginalVolumes": true
}'
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

It is possible to resize containers within an instance by increasing their memory plan or storage limit. This is done by assigning a new service plan to the container.

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id/resize`

### JSON Parameters

Parameter   | Required | Default | Description
---------   | -------- | ------- | -----------
instance.plan.id | no | null    | The map containing the id of the service plan you wish to apply to the containers in this instance
volumes | no | defaults to plan config | Can be used to grow just the logical volume of the instance instead of choosing a plan
deleteOriginalVolumes | no | false | Delete the original volumes after resizing. (Amazon only)

## Clone an Instance

```shell
curl -X PUT "https://api.gomorpheus.com/api/instances/1/clone" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "name": "New Name",
    "group": {
      "id": 1
  }}'
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

One can easily clone an instance and all containers within that instance. The containers are backed up via the backup services and used as a snapshot to produce a clone of the instance. It is possible to clone this app instance into an entirely different availability zone.

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id/clone`

### JSON Parameters

Parameter   | Default | Description
---------   | ------- | -----------
group       | null    | the map containing the id of the server group you would like to clone into.
name        | null    | A name for the new cloned instance. If none is specified the existing name will be duplicated with the 'clone' suffix added.

## Backup an Instance

```shell
curl -X PUT "https://api.gomorpheus.com/api/instances/1773/backup" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure that looks like this:

```json
{
    "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id/backup`

## Get list of backups for an Instance

```shell
curl "https://api.gomorpheus.com/api/instances/1773/backups" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure that looks like this:

```json
{
    "instance": {
      "id": 1773
    },
    "backups": [
    ]
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/instances/:id/backups`

## Import Snapshot of an Instance

```shell
curl -X PUT "https://api.gomorpheus.com/api/instances/1/import-snapshot" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "storageProviderId": 1
  }'
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

It is possible to import a snapshot of an instance. This creates a Virtual Image of the instance as it currently exists.

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id/import-snapshot`

### JSON Parameters

Parameter   | Default | Description
---------   | ------- | -----------
storageProviderId       | null    | Optional storage provider to use.

## Get Security Groups

```shell
curl -XGET "https://api.gomorpheus.com/api/instances/1/security-groups" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true,
  "firewallEnabled": true,
  "securityGroups": [
    {
      "id": 19,
      "accountId": 1,
      "name": "All Tomcat Access",
      "description": "Allow everyone to access Tomcat"
    }
  ]
}
```

This returns a list of all of the security groups applied to an instance and whether the firewall is enabled.

### HTTP Request

`GET https://api.gomorpheus.com/api/instances/:id/security-groups`


## Set Security Groups

```shell
curl -X POST "https://api.gomorpheus.com/api/instances/1/security-groups" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "securityGroupIds": [19, 2] }'
```

> The above command returns JSON structure similar to the 'get' of security groups.

### HTTP Request

`POST https://api.gomorpheus.com/api/instances/:id/security-groups`

### JSON Parameters

Parameter   | Default | Description
---------   | ------- | -----------
securityGroupIds | null | List of all security groups ids which should be applied.  If no security groups should apply, pass '[]'

This defines the list of all the security groups applied to an instance.

## Delete an Instance

```shell
curl -XDELETE "https://api.gomorpheus.com/api/instances/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete an instance and all associated monitors and backups.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/instances/:id`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
preserveVolumes | off | Preserve Volumes
keepBackups | off | Preserve copy of backups
releaseEIPs | on | Release EIPs
force | off | Force Delete
