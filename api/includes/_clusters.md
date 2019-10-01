# Clusters

Clusters is for creating and managing Kubernetes Clusters, Morpheus manager Docker Clusters, KVM Clusters, or Cloud specific Kubernetes services such as EKS. The `Triforce` Cluster is a combination Kubernetes, KVM and Functions* Cluster, with all nodes supporting all three provision types. 

## Get All Clusters

```shell
curl "https://api.gomorpheus.com/api/clusters"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
    "clusters": [
        {
            "id": 1,
            "name": "cluster-1",
            "code": null,
            "category": null,
            "visibility": "public",
            "description": null,
            "location": null,
            "enabled": false,
            "serviceUrl": null,
            "serviceHost": null,
            "servicePath": null,
            "serviceHostname": null,
            "servicePort": 22,
            "serviceUsername": null,
            "servicePassword": null,
            "serviceToken": null,
            "serviceAccess": null,
            "serviceCert": null,
            "serviceConfig": null,
            "serviceVersion": null,
            "searchDomains": null,
            "enableInternalDns": false,
            "internalId": null,
            "externalId": null,
            "datacenterId": null,
            "status": "provisioning",
            "statusDate": "2019-08-14T04:42:22+0000",
            "statusMessage": null,
            "inventoryLevel": "full",
            "lastSync": "2019-08-09T23:32:04+0000",
            "nextRunDate": "2019-08-14T04:47:22+0000",
            "lastSyncDuration": 138,
            "dateCreated": "2019-07-29T20:34:27+0000",
            "lastUpdated": "2019-08-14T04:42:22+0000",
            "serviceEntry": null,
            "createdBy": {
                "id": 1,
                "username": "root"
            },
            "userGroup": null,
            "layout": {
                "id": 3,
                "name": "Amazon Docker Host",
                "provisionTypeCode": "amazon"
            },
            "owner": {
                "id": 1,
                "name": "Stubby Toes Inc."
            },
            "servers": [
                {
                    "id": 1,
                    "name": "cluster-1",
                    "typeSet": {
                        "id": 5,
                        "code": "kubernetes-amazon-ubuntu-16.04-set",
                        "name": "kubernetes master"
                    },
                    "computeServerType": {
                        "id": 99,
                        "code": "amazonLinux",
                        "nodeType": "morpheus-node"
                    }
                }
            ],
            "accounts": [

            ],
            "integrations": [

            ],
            "site": {
                "id": 2,
                "name": "stubby toes aws group"
            },
            "type": {
                "id": 2,
                "name": "Docker Cluster"
            },
            "zone": {
                "id": 3,
                "name": "stubby toes aws cloud",
                "zoneType": {
                    "id": 12
                }
            },
            "config": null,
            "workers": [
                {
                    "id": 7,
                    "name": "cluster-1",
                    "status": "provisioning",
                    "powerState": "on"
                }
            ],
            "workerCount": 1,
            "workerStats": {
                "usedStorage": 0,
                "maxStorage": 21474836480,
                "usedMemory": 0,
                "maxMemory": 536870912,
                "usedCpu": 0.0,
                "cpuUsage": 0.0,
                "cpuUsagePeak": 0.0,
                "cpuUsageAvg": 0.0
            }
        }
    ],
    "meta": {
        "size": 5,
        "total": 5,
        "max": 25,
        "offset": 0
    }
}
```

This endpoint retrieves all clusters and a list of clusters associated with the zone by id.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase | null | Name or serviceUrl filter, restricts query to only load clusters which contain the phrase specified
name | null | Name filter, restricts query to only load clusters matching the name specified
zoneId | null | Zone filter, restricts query to only load clusters of a specified zone
typeId | null | Type filter, restricts query to only load clusters of a specified cluster type

<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>


## Get a Specific Cluster

```shell
curl "https://api.gomorpheus.com/api/clusters/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
    "cluster": {
        "id": 3,
        "name": "kubernetes-cluster",
        "code": null,
        "category": null,
        "visibility": "public",
        "description": null,
        "location": null,
        "enabled": false,
        "serviceUrl": null,
        "serviceHost": null,
        "servicePath": null,
        "serviceHostname": null,
        "servicePort": 22,
        "serviceUsername": null,
        "servicePassword": null,
        "serviceToken": null,
        "serviceAccess": null,
        "serviceCert": null,
        "serviceConfig": null,
        "serviceVersion": null,
        "searchDomains": null,
        "enableInternalDns": false,
        "apiKey": "2006d897-664b-427a-a4eb-f0b23285a54a",
        "internalId": null,
        "externalId": null,
        "datacenterId": null,
        "status": "provisioning",
        "statusDate": "2019-07-29T23:44:34+0000",
        "statusMessage": null,
        "inventoryLevel": "full",
        "lastSync": null,
        "nextRunDate": "2019-08-14T04:47:22+0000",
        "lastSyncDuration": null,
        "dateCreated": "2019-07-29T23:40:56+0000",
        "lastUpdated": "2019-08-14T04:43:54+0000",
        "serviceEntry": null,
        "createdBy": {
            "id": 1,
            "username": "root"
        },
        "userGroup": null,
        "layout": {
            "id": 4,
            "name": "Kubernetes 1.14 Cluster on Ubuntu 16.04, Weave, OpenEBS",
            "provisionTypeCode": "amazon"
        },
        "owner": {
            "id": 1,
            "name": "Stubby Toes Inc."
        },
        "servers": [
            {
                "id": 14,
                "name": "kube1-worker-2",
                "computeServerType": {
                    "id": 192,
                    "code": "amazonKubeWorker",
                    "nodeType": "kube-worker"
                }
            },
            {
                "id": 12,
                "name": "kube1-master",
                "computeServerType": {
                    "id": 191,
                    "code": "amazonKubeMaster",
                    "nodeType": "kube-master"
                }
            },
            {
                "id": 13,
                "name": "kube1-worker-1",
                "computeServerType": {
                    "id": 192,
                    "code": "amazonKubeWorker",
                    "nodeType": "kube-worker"
                }
            },
            {
                "id": 15,
                "name": "kube1-worker-3",
                "computeServerType": {
                    "id": 192,
                    "code": "amazonKubeWorker",
                    "nodeType": "kube-worker"
                }
            }
        ],
        "accounts": [

        ],
        "integrations": [

        ],
        "site": {
            "id": 2,
            "name": "aws group"
        },
        "type": {
            "id": 1,
            "name": "Kubernetes Cluster"
        },
        "zone": {
            "id": 3,
            "name": "aws cloud",
            "zoneType": {
                "id": 12
            }
        },
        "config": "{\"initConfig\":\"\"}",
        "workerStats": {
            "usedStorage": 0,
            "maxStorage": 53687091200,
            "usedMemory": 0,
            "maxMemory": 2147483648,
            "usedCpu": 0.0,
            "cpuUsage": 0.0,
            "cpuUsagePeak": 0.0,
            "cpuUsageAvg": 0.0
        },
        "containersCount": 35,
        "servicesCount": 1,
        "deploymentsCount": 1,
        "podsCount": 33,
        "jobsCount": 1,
        "volumesCount": 2,
        "namespacesCount": 1,
        "workersCount": 4,
        "permissions": {
            "resourcePool": {
                "id": 12,
                "visibility": "public"
            },
            "resourcePermissions": {
                "allGroups": true,
                "defaultStore": false,
                "allPlans": false,
                "defaultTarget": false,
                "morpheusResourceType": "ComputeZonePool",
                "morpheusResourceId": 12,
                "canManage": false,
                "all": true,
                "account": {
                    "id": 1
                },
                "sites": [
                    {
                        "id": 2,
                        "name": "dans aws group",
                        "default": true
                    }
                ],
                "plans": [
                    {
                        "id": 88,
                        "name": "128MB Memory, 1GB Storage",
                        "default": false
                    }
                ]
            }
        }
    }
}
```

This endpoint retrieves a specific cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/cluster/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | ID of the cluster

## Create a Cluster

```shell
curl -XPOST "https://api.gomorpheus.com/api/clusters" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"cluster": {
        "type": "docker-cluster",
        "name": "stubby toes docker cluster",
        "description": null,
        "group": {"id": 2},
        "cloud": {"id": 3},
        "layout": "docker-amazon-ubuntu-16.04-single",
        "server": {
            "config": {
                "resourcePool": "vpc-d673ebb3",
                "publicIpType": "subnet",
                "createUser": false
            },
            "name": "tippytoes",
            "plan": {
                "code": "amazon-t2.nano",
                "options": {
                    "maxMemory": 536870912,
                    "cpuCount": 1,
                    "coreCount": 1,
                    "coresPerSocket": 1
                }
            },
            "volumes": [
                {
                    "id": -1,
                    "rootVolume": true,
                    "name": "root",
                    "size": 10,
                    "sizeId": null,
                    "storageType": 10,
                    "datastoreId": null
                }
            ],
            "networkInterfaces": [
                {
                    "network": {
                        "id": "network-20"
                    }
                }
            ],
            "securityGroups": [
                "sg-052d3dacc2b663fdd"
            ],
            "visibility": "private",
            "userGroup": {
                "id": 1
            },
            "networkDomain": null,
            "hostname": null
        }
    }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single check 

### HTTP Request

`POST https://api.gomorpheus.com/api/clusters`

### JSON Parameters

Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
type  | Y | n/a | Type of cluster to be created
name | Y | n/a | Name of the cluster to be created
description | N | null | Description of the cluster to be created
group.id | Y | n/a | The Group ID to provision the cluster into
cloud.id | Y | n/a | The Cloud ID to provision the instance into 
layout.id | Y | n/a | The Layout ID for the instance type(s) that will be provisioned for the cluster 
server | Y | n/a | Key for server configuration, see [Server](#server)
        
#### Server

The `server` parameter is for server instance configuration that are specific to each Provision Type.
The Provision Types api can be used to see which options are available.

Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
config | Y | null | Key for specific instance type configuration, see [Config](#config)
name | Y | n/a | Name to be used for instance(s) created in the cluster
plan.id | Y | null | The id for the memory and storage option pre-configured within Morpheus. See [Available Service Plans](##get-available-service-plans-for-an-instance)
plan.options | N | null | Map of custom options depending on selected service plan . An example would be `maxMemory`, or `maxCores`.
volumes | N | null | Key for volume configuration, see [Volumes](#volumes)  
networkInterfaces | N | null | Key for network configuration, see [Network Interfaces](#network-interfaces)
securityGroups | N | null | Key for security group configuration. It should be passed as an array of objects containing the id of the security group to assign the instance to
visibility | N | private | Visibility for server instance
userGroup.id | N | null | User Group ID for server instance
hostname | N | null | Hostname for server instance

#### Volumes

The (optional) `volumes` parameter is for LV configuration, can create additional LVs at provision
It should be passed as an array of Objects with the following attributes:

Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
id | N | -1 | The id for the LV configuration being created
rootVolume | N | true | If set to false then a non-root LV will be created
name | Y | root | Name/type of the LV being created
size | N | [from service plan] | Size of the LV to be created in GBs
sizeId | N | null | Can be used to select pre-existing LV choices from Morpheus
storageType | N | null | Identifier for LV type
datastoreId | Y | null | The ID of the specific datastore. Auto selection can be specified as `auto` or `autoCluster` (for clusters).

#### Network Interfaces

The `networkInterfaces` parameter is for network configuration.

The Options API `/api/options/zoneNetworkOptions?zoneId=5&provisionTypeId=10` can be used to see which options are available.

It should be passed as an array of Objects with the following attributes:

Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
network.id | Y | n/a | id of the network to be used. A network group can be specified instead by prefixing its ID  with `networkGroup-`.
networkInterfaceTypeId | Y | n/a | The id of type of the network interface.
ipAddress | Y | n/a | The ip address. Not applicable when using DHCP or IP Pools.

#### Config

The `config` parameter is for configuration options that are specific to each Provision Type.
The Provision Types api can be used to see which options are available.


## Update Cluster

```shell
curl -XPUT "https://api.gomorpheus.com/api/clusters/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"cluster": {
       "name": "Cluster Name",
       "description": "Cluster Description",
       "enabled": true,
       "serviceUrl": "https://api-endpoint.com",
       "refresh": true
      }}' 
```

> The above command returns a similar JSON structure when submitting a GET request for a single cluster 

### HTTP Request

`PUT https://api.gomorpheus.com/api/clusters/:id`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cluster

### JSON Cluster Parameters

Parameter | Default | Description
--------- | ------- | -----------
name | null | Cluster name
description | null | Cluster description
enabled | null | Cluster enabled
serviceUrl | null | Cluster API Url
refresh | null | Queue cluster refresh

## Update Cluster Permissions

```shell
curl -XPUT "https://api.gomorpheus.com/api/clusters/1/permissions" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"permissions": {
       "resourcePermissions": {
         "all": true,
         "sites": [{"id": 1, "default": true}],
         "allPlans": true,
         "plans": [{"id": 1, "default": false}]
       }
      }}' 
```

> The above command returns a similar JSON structure when submitting a GET request for a single cluster 

### HTTP Request

`PUT https://api.gomorpheus.com/api/clusters/:id/permissions`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cluster

### JSON Cluster Parameters

Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
permissions | Y | n/a | Key for server configuration, see [Permissions](#permissions)

#### Permissions

The `permissions` parameter is for permissions for clusters and namespaces.

Parameter | Default | Description
--------- | ------- | -----------
resourcePool.visibility | null | Applicable to clusters only
resourcePermissions.all  | null | Pass true to allow access all groups
resourcePermissions.sites  | null | Array of groups that are allowed access
resourcePermissions.allPlans | null | Pass true to allow access all plans
resourcePermissions.plans | null | Array of plans that are allowed access
tenantPermissions.accounts  | null | Array of tenant account ids that are allowed access


## Delete a Cluster

```shell
curl -XDELETE "https://api.gomorpheus.com/api/clusters/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete a cluster and associated resources, instances, volumes asynchronously 

### HTTP Request

`DELETE https://api.gomorpheus.com/api/clusters/:id`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
removeResources | on | Remove Infrastructure.
removeInstances | off | Remove Associated Instances
preserveVolumes | off | Preserve Volumes
releaseEIPs | on | Release EIPs
force | off | Force Delete


## Get API Config

```shell
curl "https://api.gomorpheus.com/api/clusters/1/api-config" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" 
```

> The above comand returns JSON structure like this:

```json
{
  "serviceUrl": null,
  "serviceHost": null,
  "servicePath": null,
  "serviceHostname": null,
  "servicePort": 22,
  "serviceUsername": null,
  "servicePassword": null,
  "serviceToken": null,
  "serviceAccess": null,
  "serviceCert": null,
  "serviceConfig": null,
  "serviceVersion": null
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/api-config`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cluster


## Get API Token 

```shell
curl "https://api.gomorpheus.com/api/clusters/1/api-token" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" 
```

> The above comand returns JSON structure like this:

```json
{
  "serviceUrl": null,
  "serviceHost": null,
  "servicePath": null,
  "serviceHostname": null,
  "servicePort": 22,
  "serviceUsername": null,
  "servicePassword": null,
  "serviceToken": null,
  "serviceAccess": null,
  "serviceCert": null,
  "serviceConfig": null,
  "serviceVersion": null
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/api-token`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cluster


## List Namespaces (Kubernetes)

```shell
curl "https://api.gomorpheus.com/api/clusters/:cluster_id/namespaces"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "namespaces": [
    {
      "id": 1,
      "name": "Namespace",
      "description": "Some details about namespace",
      "regionCode": null,
      "externalId": null,
      "status": "available"
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

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:clusterId/namespaces`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster


## Get Namespace (Kubernetes)

```shell
curl "https://api.gomorpheus.com/api/clusters/:clusterId/namespaces/:id"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "namespace": {
    "id": 13,
    "visibility": "public",
    "name": "My Namespace",
    "status": "available",
    "description": "new description",
    "permissions": {
      "resourcePermissions": {
        "allGroups": true,
        "defaultStore": false,
        "allPlans": true,
        "defaultTarget": false,
        "morpheusResourceType": "ComputeZonePool",
        "morpheusResourceId": 13,
        "canManage": false,
        "all": true,
        "account": {
          "id": 1
        },
        "sites": [
          {
            "id": 2,
            "name": "aws group",
            "default": false
          }
        ],
        "plans": [
          {
            "id": 88,
            "name": "128MB Memory, 1GB Storage",
            "default": true
          }
        ]
      }
    }
  }
}
```

This endpoint retrieves a specific namespace of a cluster

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:clusterId/namespaces/:id`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the namespace


## Add Namespace (Kubernetes)

```shell
curl -XPOST "https://api.gomorpheus.com/api/clusters/1/namespaces" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"namespace": {
       "name": "Namespace Name",
       "description": "Description",
       "active": true,
       "resourcePermissions": {
         "all": true,
         "allPlans": true,
         "sites": [{"id": 2,"default": true}],
         "plans": [{"id": 88,"default": false}]
       }
      }}'
```         

> The above command returns JSON structure like this:

```json
{
  "success": true,
  "namespace": {
    "id": 1,
    "name": "Namespace Name",
    "description": "Description",
    "regionCode": null,
    "externalId": null,
    "status": "available"
  }
}
```

### HTTP Request

`POST https://api.gomorpheus.com/api/clusters/:id/namespaces`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cluster

### JSON Cluster Parameters

Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
name | Y | null | Namespace name
description | N | null | Namespace description
active | N | false | Namespace active
resourcePermissions | N | null | Key for resource permission configuration, see [Resource Permissions](#resource-permissions)  

#### Resource Permissions

The `resourcePermissions` parameter is map for namespace group and service plan permissions.

Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
all | N | null | Pass true to allow access all groups
sites | N | null | Array of groups that are allowed access
allPlans | N | null | Pass true to allow access all service plans
plans | N | n/a | Array of service plans that are allowed access


## Update Namespace (Kubernetes)

```shell
curl -XPUT "https://api.gomorpheus.com/api/clusters/1/namespaces" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"namespace": {
       "description": "Description",
       "active": true,
       "permissions": {
         "resourcePermissions": {
           "all": true,
           "sites": [{"id": 1, "default": true}],
           "allPlans": true,
           "plans": [{"id": 1, "default": false}]
         }
       }  
      }}'
```         

> The above command returns same JSON structure as [Add Namespace](#add-namespace-kubernetes)

### HTTP Request

`PUT https://api.gomorpheus.com/api/clusters/:id/namespaces`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cluster

### JSON Cluster Parameters

Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
description | N | null | Namespace description
active | N | false | Namespace active
permissions | N | null | Key for resource permission configuration, see [Permissions](#permissions)  


## Delete a Namespace

```shell
curl -XDELETE "https://api.gomorpheus.com/api/clusters/:clusterId/namespaces/:id" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete a namespace of the from the specified cluster

### HTTP Request

`DELETE https://api.gomorpheus.com/api/clusters/:clusterId/namespaces/:id`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the namespace to delete

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
force | off | Force Delete


## Add Worker

```shell
curl -XPOST "https://api.gomorpheus.com/api/clusters/:id/servers" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"server": {
        "config": {
            "resourcePool": "vpc-d673ebb3",
            "publicIpType": "subnet",
            "createUser": false
        },
        "name": "tippytoes",
        "plan": {
            "code": "amazon-t2.nano",
            "options": {
                "maxMemory": 536870912,
                "cpuCount": 1,
                "coreCount": 1,
                "coresPerSocket": 1
            }
        },
        "volumes": [
            {
                "id": -1,
                "rootVolume": true,
                "name": "root",
                "size": 10,
                "sizeId": null,
                "storageType": 10,
                "datastoreId": null
            }
        ],
        "networkInterfaces": [
            {
                "network": {
                    "id": "network-20"
                }
            }
        ],
        "securityGroups": [
            "sg-052d3dacc2b663fdd"
        ],
        "visibility": "private",
        "userGroup": {
            "id": 1
        },
        "networkDomain": null,
        "hostname": null,
        "taskSet": {
          "id": 2
        }       
    }}'
```

> The above command returns a similar JSON structure when submitting a GET request for workers 

### HTTP Request

`POST https://api.gomorpheus.com/api/clusters/:id/servers`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cluster

### JSON Parameters

Parameter | Description
--------- | -----------
server | Key for server configuration, see [Server](#server)


## Get Workers

```shell
curl "https://api.gomorpheus.com/api/clusters/:id/workers"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "workers": [
    {
      "id": 11,
      "externalId": "i-03a65f2d1d34f4d76",
      "internalId": null,
      "accountId": 1,
      "account": {
        "name": "Stubby Toes Inc."
      },
      "name": "kube-worker-1",
      "visibility": "public",
      "description": null,
      "zoneId": 3,
      "siteId": 2,
      "sshHost": null,
      "sshPort": 22,
      "externalIp": null,
      "internalIp": "172.31.7.195",
      "volumeId": null,
      "platform": null,
      "platformVersion": null,
      "sshUsername": "root",
      "sshPassword": "****",
      "osDevice": "/dev/sda",
      "dataDevice": "/dev/sdb",
      "lvmEnabled": false,
      "apiKey": "9f91db5c-25fc-4869-9881-f65b76c4c58a",
      "softwareRaid": false,
      "dateCreated": "2019-07-29T23:41:19+0000",
      "lastUpdated": "2019-08-09T21:25:44+0000",
      "stats": {
        "usedStorage": null,
        "reservedStorage": 0,
        "maxStorage": 10737418240,
        "usedMemory": 0,
        "reservedMemory": 0,
        "maxMemory": 536870912
      },
      "status": "failed",
      "statusMessage": null,
      "errorMessage": null,
      "statusDate": null,
      "statusPercent": null,
      "statusEta": null,
      "powerState": "unknown",
      "computeServerType": {
        "id": 192,
        "code": "amazonKubeWorker",
        "name": "Amazon Kubernetes Worker",
        "managed": true,
        "externalDelete": true
      },
      "agentInstalled": false,
      "lastAgentUpdate": null,
      "agentVersion": null,
      "maxCores": 1,
      "maxMemory": 536870912,
      "maxStorage": 10737418240,
      "maxCpu": null,
      "serverOs": null,
      "enabled": true,
      "zone": {
        "id": 3,
        "name": "stubby toes aws cloud"
      },
      "plan": {
        "id": 1,
        "code": "amazon-t2.nano",
        "name": "Amazon T2 Nano - 1 Core, 0.5GB Memory"
      },
      "containers": [

      ]
    }
  ]  
}
```

This endpoint retrieves workers of a specified cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/workers`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cluster

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
phrase | null | Name filter, restricts query to only load workers matching the name or display name

## Get Masters (Kubernetes)

```shell
curl "https://api.gomorpheus.com/api/clusters/:id/masters"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured similar to [Get Workers](#get-workers)

This endpoint retrieves masters of a specified kubernetes cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/masters`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cluster

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
phrase | null | Name filter, restricts query to only load workers matching the name or display name


## Get Volumes

```shell
curl "https://api.gomorpheus.com/api/clusters/:id/volumes"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "volumes": [
    {
      "id": 123,
      "displayOrder": 0,
      "active": true,
      "usedStorage": 0,
      "resizeable": true,
      "online": true,
      "deviceDisplayName": "xvda",
      "name": "root",
      "externalId": "vol-076adc80392a1217a",
      "volumeType": "disk",
      "deviceName": "/dev/sda1",
      "removable": false,
      "readOnly": false,
      "zoneId": 3,
      "rootVolume": true,
      "category": "kubernetes.persistentVolumeClaim.cluster.3",
      "status": "provisioned",
      "maxStorage": 21474836480,
      "account": {
        "id": 1
      },
      "type": {
        "id": 10
      }
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

This endpoint retrieves volumes of a specified cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/volumes`

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
phrase | null | Name or internalId filter, restricts query to only load volumes which contain the phrase specified


## Delete a Volume

```shell
curl -XDELETE "https://api.gomorpheus.com/api/clusters/:clusterId/namespaces/:id" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete a namespace of the from the specified cluster

### HTTP Request

`DELETE https://api.gomorpheus.com/api/clusters/:clusterId/namespaces/:id`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the namespace to delete

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
force | off | Force Delete

 
## Get Containers

```shell
curl "https://api.gomorpheus.com/api/clusters/:id/containers"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "containers": [
    {
      "id": 14,
      "uuid": "",
      "accountId": 1,
      "instance": null,
      "containerType": {
        "id": 50,
        "code": "ubuntu-14.04.03",
        "category": null,
        "name": "Ubuntu 14.04"
      },
      "containerTypeSet": {
        "id": null,
        "code": null,
        "category": null
      },
      "server": {
        "id": 20,
        "name": "cluster 2"
      },
      "cloud": {
        "id": 3,
        "name": "aws cloud"
      },
      "name": "ubuntu_14",
      "ip": "172.31.0.197",
      "internalIp": "172.31.0.197",
      "internalHostname": "container14",
      "externalHostname": "container14",
      "externalDomain": "localdomain",
      "externalFqdn": "container14.localdomain",
      "ports": [

      ],
      "plan": {
        "id": null,
        "code": null,
        "name": null
      },
      "dateCreated": null,
      "lastUpdated": "2019-10-01T13:55:23+0000",
      "statsEnabled": false,
      "status": "unknown",
      "userStatus": "stopped",
      "environmentPrefix": null,
      "stats": {
      },
      "runtimeInfo": {
      },
      "containerVersion": null,
      "repositoryImage": null,
      "planCategory": null,
      "hostname": null,
      "domainName": null,
      "volumeCreated": false,
      "containerCreated": false,
      "maxStorage": null,
      "maxMemory": null,
      "maxCores": null,
      "maxCpu": null,
      "availableActions": [

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

This endpoint retrieves containers of a specified cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/containers`

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
phrase | null | Name or internalId filter, restricts query to only load volumes which contain the phrase specified
resourceLevel | null | Resource level filter


## Get Deployments

```shell
curl "https://api.gomorpheus.com/api/clusters/:id/deployments"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "deployments": [
    {
      "id": 4,
      "code": "test_pod_code",
      "lastUpdated": "2019-10-01T02:09:53+0000",
      "managed": false,
      "resourceType": "deployment",
      "category": "kubernetes.deployment.cluster.3",
      "status": "starting",
      "name": "test deployment display name",
      "owner": {
        "id": 1
      },
      "totalCpuUsage": 0,
      "stats": {
      }
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

This endpoint retrieves deployments of a specified cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/deployments`

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
phrase | null | Name or internalId filter, restricts query to only load volumes which contain the phrase specified
resourceLevel | null | Resource level filter


## Get Jobs

```shell
curl "https://api.gomorpheus.com/api/clusters/:id/jobs"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "jobs": [
    {
      "id": 5,
      "name": "Job 1",
      "type": "morpheus.task",
      "status": null,
      "namespace": null,
      "category": "kubernetes.job.cluster.3",
      "description": null,
      "enabled": true,
      "dateCreated": "2019-09-29T19:51:37+0000",
      "lastUpdated": "2019-09-29T20:00:58+0000",
      "lastRun": null,
      "createdBy": {
        "id": 1,
        "username": "root"
      }
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

This endpoint retrieves jobs of a specified cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/jobs`

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
phrase | null | Name or internalId filter, restricts query to only load volumes which contain the phrase specified


## Get Pods

```shell
curl "https://api.gomorpheus.com/api/clusters/:id/pods"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "pods": [
    {
      "id": 2,
      "code": "test_pod_code",
      "lastUpdated": "2019-10-01T02:23:19+0000",
      "managed": false,
      "resourceType": "pod",
      "category": "kubernetes.pod.cluster.3",
      "status": "starting",
      "name": "test pod display name",
      "owner": {
        "id": 1
      },
      "totalCpuUsage": 0,
      "stats": {
      }
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

This endpoint retrieves pods of a specified cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/deployments`

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
phrase | null | Name or internalId filter, restricts query to only load volumes which contain the phrase specified
resourceLevel | null | Resource level filter


## Get Services

```shell
curl "https://api.gomorpheus.com/api/clusters/:id/services"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "services": [
    {
      "id": 5,
      "name": "test service",
      "type": null,
      "code": null,
      "externalIp": null,
      "internalIp": null,
      "externalPort": null,
      "internalPort": null,
      "status": null,
      "dateCreated": null,
      "lastUpdated": null
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

This endpoint retrieves services of a specified cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/services`

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
phrase | null | Name or internalId filter, restricts query to only load volumes which contain the phrase specified


## Get Stateful Sets

```shell
curl "https://api.gomorpheus.com/api/clusters/:id/statefulsets"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "statefulsets": [
    {
      "id": 3,
      "code": "test_pod_code",
      "lastUpdated": "2019-10-01T02:10:32+0000",
      "managed": false,
      "resourceType": "statefulset",
      "category": "kubernetes.statefulset.cluster.3",
      "status": "starting",
      "name": "test statefulset display name",
      "owner": {
        "id": 1
      },
      "totalCpuUsage": 0,
      "stats": {
      }
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

This endpoint retrieves stateful sets of a specified cluster.

### HTTP Request

`GET https://api.gomorpheus.com/api/clusters/:id/statefulsets`

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
phrase | null | Name or internalId filter, restricts query to only load volumes which contain the phrase specified
resourceLevel | null | Resource level filter


## Delete Container

```shell
curl -XDELETE "https://api.gomorpheus.com/api/clusters/:clusterId/containers/:id" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete a container from the specified cluster

### HTTP Request

`DELETE https://api.gomorpheus.com/api/clusters/:clusterId/containers/:id`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the container to delete

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
force | off | Force Delete


## Delete a Deployment

```shell
curl -XDELETE "https://api.gomorpheus.com/api/clusters/:clusterId/deployments/:id" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete a deployment from the specified cluster

### HTTP Request

`DELETE https://api.gomorpheus.com/api/clusters/:clusterId/deployments/:id`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the deployment to delete

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
force | off | Force Delete


## Delete a Job

```shell
curl -XDELETE "https://api.gomorpheus.com/api/clusters/:clusterId/jobs/:id" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete a job from the specified cluster

### HTTP Request

`DELETE https://api.gomorpheus.com/api/clusters/:clusterId/jobs/:id`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the job to delete

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
force | off | Force Delete


## Delete a Service

```shell
curl -XDELETE "https://api.gomorpheus.com/api/clusters/:clusterId/services/:id" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete a service from the specified cluster

### HTTP Request

`DELETE https://api.gomorpheus.com/api/clusters/:clusterId/services/:id`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the service to delete

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
force | off | Force Delete


## Delete a Stateful Set

```shell
curl -XDELETE "https://api.gomorpheus.com/api/clusters/:clusterId/statefulset/:id" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete a stateful set from the specified cluster

### HTTP Request

`DELETE https://api.gomorpheus.com/api/clusters/:clusterId/statefulset/:id`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the stateful set to delete

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
force | off | Force Delete


## Restart a Container

```shell
curl -XPUT "https://api.gomorpheus.com/api/clusters/:clusterId/containers/:id/restart" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will restart a container in the specified cluster

### HTTP Request

`PUT https://api.gomorpheus.com/api/clusters/:clusterId/containers/:id/restart`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the container to restart


## Restart a Deployment

```shell
curl -XPUT "https://api.gomorpheus.com/api/clusters/:clusterId/deployments/:id/restart" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will restart a deployment in the specified cluster

### HTTP Request

`PUT https://api.gomorpheus.com/api/clusters/:clusterId/deployments/:id/restart`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the deployment to restart


## Restart a Pod

```shell
curl -XPUT "https://api.gomorpheus.com/api/clusters/:clusterId/pods/:id/restart" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will restart a pod in the specified cluster

### HTTP Request

`PUT https://api.gomorpheus.com/api/clusters/:clusterId/pods/:id/restart`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the pod to restart


## Restart a Stateful Set

```shell
curl -XPUT "https://api.gomorpheus.com/api/clusters/:clusterId/statefulsets/:id/restart" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will restart a stateful set in the specified cluster

### HTTP Request

`PUT https://api.gomorpheus.com/api/clusters/:clusterId/statefulsets/:id/restart`

### URL Parameters

Parameter | Description
--------- | -----------
clusterId | The ID of the cluster
id | The ID of the stateful set to restart

