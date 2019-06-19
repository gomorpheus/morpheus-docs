# Blueprints

Blueprints are templates for creating apps. They are a set of instance configurations, organized by tier, and scoped by group, cloud and environment.

## Get All Blueprints

```shell
curl "https://api.gomorpheus.com/api/blueprints"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "blueprints": [
    {
      "id": 135,
      "name": "test",
      "type": "morpheus",
      "description": null,
      "category": null,
      "config": {
        "image": "/assets/apps/template.png",
        "tiers": {
          "Web": {
            "linkedTiers": [

            ],
            "tierIndex": 1,
            "instances": [
              {
                "instance": {
                  "type": "nginx"
                },
                "groups": {
                  "My Group": {
                    "clouds": {
                      "My Cloud": {
                        "instance": {
                          "layout": {
                            "code": "nginx-vmware-1.9-single",
                            "id": 179
                          },
                          "name": "test-nginx-${sequence}",
                          "allowExisting": false,
                          "createUser": "on",
                          "type": "nginx",
                          "userGroup": {
                            "id": ""
                          }
                        },
                        "networkInterfaces": [
                          {
                            "ipMode": "",
                            "primaryInterface": true,
                            "network": {
                              "id": "",
                              "hasPool": false
                            },
                            "networkInterfaceTypeId": 4,
                            "networkInterfaceTypeIdName": "VMXNET 3"
                          }
                        ],
                        "volumes": [
                          {
                            "vId": 255,
                            "controllerMountPoint": "46:0:4:0",
                            "size": 10,
                            "maxIOPS": null,
                            "name": "root",
                            "rootVolume": true,
                            "storageType": 1,
                            "datastoreId": "autoCluster",
                            "maxStorage": 0
                          }
                        ],
                        "config": {
                          "resourcePoolId": "resgroup-123",
                          "createUser": true
                        },
                        "plan": {
                          "code": "vm-1024",
                          "id": 76
                        }
                      }
                    }
                  }
                }
              }
            ]
          }
        },
        "name": "test",
        "templateImage": "",
        "type": "morpheus",
        "config": {
          "isVpcSelectable": true,
          "isEC2": false
        }
      },
      "visibility": "private",
      "resourcePermission": {
        "all": true,
        "sites": [

        ]
      }
    }
  ],
  "meta": {
    "offset": 0,
    "max": "1",
    "size": 1,
    "total": 1
  }
}

```

This endpoint retrieves all blueprints.

### HTTP Request

`GET https://api.gomorpheus.com/api/blueprints`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
name | null | Filter by name
phrase | null | Filter by wildcard search of name and description

## Get a Specific Blueprint


```shell
curl "https://api.gomorpheus.com/api/blueprints/4" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "blueprint": {
    "id": 135,
    "name": "test",
    "type": "morpheus",
    "description": null,
    "category": null,
    "config": {
      "image": "/assets/apps/template.png",
      "tiers": {
        "Web": {
          "linkedTiers": [

          ],
          "tierIndex": 1,
          "instances": [
            {
              "instance": {
                "type": "nginx"
              },
              "groups": {
                "My Group": {
                  "clouds": {
                    "My Cloud": {
                      "instance": {
                        "layout": {
                          "code": "nginx-vmware-1.9-single",
                          "id": 179
                        },
                        "name": "test-nginx-${sequence}",
                        "allowExisting": false,
                        "createUser": "on",
                        "type": "nginx",
                        "userGroup": {
                          "id": ""
                        }
                      },
                      "networkInterfaces": [
                        {
                          "ipMode": "",
                          "primaryInterface": true,
                          "network": {
                            "id": "",
                            "hasPool": false
                          },
                          "networkInterfaceTypeId": 4,
                          "networkInterfaceTypeIdName": "VMXNET 3"
                        }
                      ],
                      "volumes": [
                        {
                          "vId": 255,
                          "controllerMountPoint": "46:0:4:0",
                          "size": 10,
                          "maxIOPS": null,
                          "name": "root",
                          "rootVolume": true,
                          "storageType": 1,
                          "datastoreId": "autoCluster",
                          "maxStorage": 0
                        }
                      ],
                      "config": {
                        "resourcePoolId": "resgroup-123",
                        "createUser": true
                      },
                      "plan": {
                        "code": "vm-1024",
                        "id": 76
                      }
                    }
                  }
                }
              }
            }
          ]
        }
      },
      "name": "test",
      "templateImage": "",
      "type": "morpheus",
      "config": {
        "isVpcSelectable": true,
        "isEC2": false
      }
    },
    "visibility": "private",
    "resourcePermission": {
      "all": true,
      "sites": [

      ]
    }
  }
}
```

This endpoint retrieves a specific blueprint.

### HTTP Request

`GET https://api.gomorpheus.com/api/blueprints/:id`


## Create a Blueprint

```shell
curl -XPOST "https://api.gomorpheus.com/api/blueprints" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "sample",
    "description": "A sample blueprint",
    "type": "morpheus",
    "tiers": {
      "Web": {
        "linkedTiers": [

        ],
        "tierIndex": 1,
        "instances": [
          {
            "instance": {
              "type": "nginx"
            },
            "groups": {
              "My Group": {
                "clouds": {
                  "My Cloud": {
                    "instance": {
                      "layout": {
                        "code": "nginx-vmware-1.9-single",
                        "id": 179
                      },
                      "name": "test-nginx-${sequence}",
                      "allowExisting": false,
                      "createUser": "on",
                      "type": "nginx",
                      "userGroup": {
                        "id": ""
                      }
                    },
                    "networkInterfaces": [
                      {
                        "ipMode": "",
                        "primaryInterface": true,
                        "network": {
                          "id": "",
                          "hasPool": false
                        },
                        "networkInterfaceTypeId": 4,
                        "networkInterfaceTypeIdName": "VMXNET 3"
                      }
                    ],
                    "volumes": [
                      {
                        "vId": 255,
                        "controllerMountPoint": "46:0:4:0",
                        "size": 10,
                        "maxIOPS": null,
                        "name": "root",
                        "rootVolume": true,
                        "storageType": 1,
                        "datastoreId": "autoCluster",
                        "maxStorage": 0
                      }
                    ],
                    "config": {
                      "resourcePoolId": "resgroup-123",
                      "createUser": true
                    },
                    "plan": {
                      "code": "vm-1024",
                      "id": 76
                    }
                  }
                }
              }
            }
          }
        ]
      }
    }
  }'
```

> The above command returns JSON structured like getting a single blueprint.

### HTTP Request

`POST https://api.gomorpheus.com/api/blueprints`

### JSON Blueprint Parameters

Parameter | Default | Description
--------- | ------- | -----------
name  | null | A name for the blueprint
description     | null | Optional description field
category     | morpheus | Optional category field
type     | morpheus | Blueprint Type. The default is 'morpheus'.
tiers | null | A Map containing a key for each tier and all their instances.

### Blueprint Tiers Configuration

The blueprint `tiers` can be structured so that instance configurations are scoped to a specific environment, group and/or cloud. The `environments` key is the environment name.  The `groups` key is the group name. The `clouds` key is the cloud name. The order of scoping must always be done in the order: environments, groups, and then clouds.

Example:
```json
 {
  "name": "sample blueprint",
  "type": "morpheus",
  "tiers": {
    "App": {
      "tierIndex": 1
      "linkedTiers": [],
      "instances": [
        {
          "instance": {
            "type": "activemq"
          },
          "environments": {
            "Dev": {
              "groups": {
                "My Group": {
                  "clouds": {
                    "My Cloud": {
                      "instance": {
                        "layout": {
                          "code": "nginx-vmware-1.9-single",
                          "id": 179
                        },
                        "name": "test-nginx-${sequence}"
                      },
                      "plan": {
                        "code": "vm-1024",
                        "id": 76
                      }
                    }
                  }
                }
              }
            }
          }
        }
      ],
    }
  }
}
```

## Updating a Blueprint

```shell
curl -XPUT "https://api.gomorpheus.com/api/blueprints/2" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "sample",
    "description": "A sample nginx blueprint",
    "type": "morpheus",
    "tiers": {
      "Web": {
        "linkedTiers": [

        ],
        "tierIndex": 1,
        "instances": [
          {
            "instance": {
              "type": "nginx"
            },
            "groups": {
              "My Group": {
                "clouds": {
                  "My Cloud": {
                    "instance": {
                      "layout": {
                        "code": "nginx-vmware-1.9-single",
                        "id": 179
                      },
                      "name": "test-nginx-${sequence}",
                      "allowExisting": false,
                      "createUser": "on",
                      "type": "nginx",
                      "userGroup": {
                        "id": ""
                      }
                    },
                    "networkInterfaces": [
                      {
                        "ipMode": "",
                        "primaryInterface": true,
                        "network": {
                          "id": "",
                          "hasPool": false
                        },
                        "networkInterfaceTypeId": 4,
                        "networkInterfaceTypeIdName": "VMXNET 3"
                      }
                    ],
                    "volumes": [
                      {
                        "vId": 255,
                        "controllerMountPoint": "46:0:4:0",
                        "size": 10,
                        "maxIOPS": null,
                        "name": "root",
                        "rootVolume": true,
                        "storageType": 1,
                        "datastoreId": "autoCluster",
                        "maxStorage": 0
                      }
                    ],
                    "config": {
                      "resourcePoolId": "resgroup-123",
                      "createUser": true
                    },
                    "plan": {
                      "code": "vm-1024",
                      "id": 76
                    }
                  }
                }
              }
            }
          }
        ]
      }
    }
  }'
```

> The above command returns JSON structured like getting a single blueprint.

### HTTP Request

`PUT https://api.gomorpheus.com/api/blueprints/:id`

### JSON Blueprint Parameters

Same as [Create](#create-a-blueprint).

This overwrites the entire config, so the entire blueprint config should be passed.

## Update Blueprint Permissions

```shell
curl -XPOST "https://api.gomorpheus.com/api/blueprints/1/update-permissions" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "resourcePermission": {
    "all":false,
    "sites": [
      {"id": 1}
    ]
  }}'
```

> The above command returns JSON structured like getting a single blueprint.

### HTTP Request

`POST https://api.gomorpheus.com/api/blueprints/:id/update-permissions`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
resourcePermission.all  | null | Enable access for all groups
resourcePermission.sites  | null | Enable access for specific groups only


## Update Blueprint Image

```shell
curl -XPOST "https://api.gomorpheus.com/api/blueprints/1/image" \
  -H "Authorization: BEARER access_token"
  -F 'templateImage=@filename'
```

> The above command returns JSON structured like getting a single blueprint.

### HTTP Request

`POST https://api.gomorpheus.com/api/blueprints/:id/image`

### Parameters

Parameter | Default | Description
--------- | ------- | -----------
templateImage  | null | Image File png,jpg,svg

Upload a new logo image.  Expects multipart form data as the request format, not JSON.


## Delete a Blueprint

```shell
curl -XDELETE "https://api.gomorpheus.com/api/blueprints/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/blueprints/:id`
