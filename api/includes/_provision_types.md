# Provision Types

Morpheus supports a diverse set of cloud APIS for provisioning compute and services. In order to facilitate some of these capabilities and preserve some of the diverse sets of feature sets across these plaforms it is necessary to provide a means to dynamicaly specifying provisioning options depending on what is being provisioned. Morpheus calls these `provision-types`. Each `InstanceTypeLayout` that can be provisioned has a correlating `ProvisionType` and each `CloudType` (aka `ZoneType`) has a list of supported provision types it is capable of provisioning. This record contains optionTypes (see section on `optionTypes` for specifics on how to parse this data) as well as information for building out network parameters and storage parameters by listing different storage type information.

## Get All Provision Types

```shell
curl "https://api.gomorpheus.com/api/provision-types"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
{
    "provisionTypes": [
        {
            "id": 9,
            "name": "Amazon",
            "description": null,
            "code": "amazon",
            "aclEnabled": false,
            "multiTenant": false,
            "managed": true,
            "hostNetwork": true,
            "customSupported": false,
            "mapPorts": false,
            "exportServer": null,
            "viewSet": "amazonCustom",
            "serverType": "ami",
            "hostType": "vm",
            "addVolumes": true,
            "hasDatastore": false,
            "hasNetworks": null,
            "maxNetworks": null,
            "customizeVolume": true,
            "rootDiskCustomizable": true,
            "lvmSupported": true,
            "hostDiskMode": "lvm",
            "minDisk": 0,
            "maxDisk": null,
            "resizeCopiesVolumes": true,
            "optionTypes": [
                {
                    "name": "subnet",
                    "description": null,
                    "fieldName": "subnetId",
                    "fieldLabel": "Subnet",
                    "fieldContext": "config",
                    "fieldAddOn": null,
                    "placeHolder": null,
                    "helpBlock": "",
                    "defaultValue": null,
                    "optionSource": "amazonSubnet",
                    "type": "select",
                    "advanced": false,
                    "required": true,
                    "editable": false,
                    "config": [],
                    "displayOrder": 100
                },
                {
                    "name": "security group",
                    "description": null,
                    "fieldName": "securityId",
                    "fieldLabel": "Security Group",
                    "fieldContext": "config",
                    "fieldAddOn": null,
                    "placeHolder": null,
                    "helpBlock": "",
                    "defaultValue": null,
                    "optionSource": "amazonSecurityGroup",
                    "type": "select",
                    "advanced": false,
                    "required": true,
                    "editable": false,
                    "config": [],
                    "displayOrder": 101
                },
                {
                    "name": "public key",
                    "description": null,
                    "fieldName": "publicKeyId",
                    "fieldLabel": "Public Key",
                    "fieldContext": "config",
                    "fieldAddOn": null,
                    "placeHolder": null,
                    "helpBlock": "",
                    "defaultValue": null,
                    "optionSource": "keyPairs",
                    "type": "select",
                    "advanced": false,
                    "required": false,
                    "editable": false,
                    "config": [],
                    "displayOrder": 9
                }
            ],
            "customOptionTypes": [],
            "networkTypes": [],
            "storageTypes": [
                {
                    "id": 7,
                    "code": "amazon-sc1",
                    "name": "sc1",
                    "displayOrder": 4,
                    "defaultType": false,
                    "customLabel": true,
                    "customSize": true,
                    "customSizeOptions": null
                },
                {
                    "id": 4,
                    "code": "amazon-io1",
                    "name": "io1",
                    "displayOrder": 2,
                    "defaultType": false,
                    "customLabel": true,
                    "customSize": true,
                    "customSizeOptions": null
                },
                {
                    "id": 5,
                    "code": "amazon-gp2",
                    "name": "gp2",
                    "displayOrder": 1,
                    "defaultType": true,
                    "customLabel": true,
                    "customSize": true,
                    "customSizeOptions": null
                },
                {
                    "id": 6,
                    "code": "amazon-st1",
                    "name": "st1",
                    "displayOrder": 3,
                    "defaultType": false,
                    "customLabel": true,
                    "customSize": true,
                    "customSizeOptions": null
                }
            ],
            "rootStorageTypes": [
                {
                    "id": 7,
                    "code": "amazon-sc1",
                    "name": "sc1",
                    "displayOrder": 4,
                    "defaultType": false,
                    "customLabel": true,
                    "customSize": true,
                    "customSizeOptions": null
                },
                {
                    "id": 4,
                    "code": "amazon-io1",
                    "name": "io1",
                    "displayOrder": 2,
                    "defaultType": false,
                    "customLabel": true,
                    "customSize": true,
                    "customSizeOptions": null
                },
                {
                    "id": 5,
                    "code": "amazon-gp2",
                    "name": "gp2",
                    "displayOrder": 1,
                    "defaultType": true,
                    "customLabel": true,
                    "customSize": true,
                    "customSizeOptions": null
                },
                {
                    "id": 6,
                    "code": "amazon-st1",
                    "name": "st1",
                    "displayOrder": 3,
                    "defaultType": false,
                    "customLabel": true,
                    "customSize": true,
                    "customSizeOptions": null
                }
            ],
            "controllerTypes": []
        }
    ]
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/provision-types`

## Get Specific Provision Type

```shell
curl "https://api.gomorpheus.com/api/provision-types/9"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
{
  "success": true,
  "provisionType": {
        "id": 9,
        "name": "Amazon",
        "description": null,
        "code": "amazon",
        "aclEnabled": false,
        "multiTenant": false,
        "managed": true,
        "hostNetwork": true,
        "customSupported": false,
        "mapPorts": false,
        "exportServer": null,
        "viewSet": "amazonCustom",
        "serverType": "ami",
        "hostType": "vm",
        "addVolumes": true,
        "hasDatastore": false,
        "hasNetworks": null,
        "maxNetworks": null,
        "customizeVolume": true,
        "rootDiskCustomizable": true,
        "lvmSupported": true,
        "hostDiskMode": "lvm",
        "minDisk": 0,
        "maxDisk": null,
        "resizeCopiesVolumes": true,
        "optionTypes": [
            {
                "name": "subnet",
                "description": null,
                "fieldName": "subnetId",
                "fieldLabel": "Subnet",
                "fieldContext": "config",
                "fieldAddOn": null,
                "placeHolder": null,
                "helpBlock": "",
                "defaultValue": null,
                "optionSource": "amazonSubnet",
                "type": "select",
                "advanced": false,
                "required": true,
                "editable": false,
                "config": [],
                "displayOrder": 100
            },
            {
                "name": "security group",
                "description": null,
                "fieldName": "securityId",
                "fieldLabel": "Security Group",
                "fieldContext": "config",
                "fieldAddOn": null,
                "placeHolder": null,
                "helpBlock": "",
                "defaultValue": null,
                "optionSource": "amazonSecurityGroup",
                "type": "select",
                "advanced": false,
                "required": true,
                "editable": false,
                "config": [],
                "displayOrder": 101
            },
            {
                "name": "public key",
                "description": null,
                "fieldName": "publicKeyId",
                "fieldLabel": "Public Key",
                "fieldContext": "config",
                "fieldAddOn": null,
                "placeHolder": null,
                "helpBlock": "",
                "defaultValue": null,
                "optionSource": "keyPairs",
                "type": "select",
                "advanced": false,
                "required": false,
                "editable": false,
                "config": [],
                "displayOrder": 9
            }
        ],
        "customOptionTypes": [],
        "networkTypes": [],
        "storageTypes": [
            {
                "id": 7,
                "code": "amazon-sc1",
                "name": "sc1",
                "displayOrder": 4,
                "defaultType": false,
                "customLabel": true,
                "customSize": true,
                "customSizeOptions": null
            },
            {
                "id": 4,
                "code": "amazon-io1",
                "name": "io1",
                "displayOrder": 2,
                "defaultType": false,
                "customLabel": true,
                "customSize": true,
                "customSizeOptions": null
            },
            {
                "id": 5,
                "code": "amazon-gp2",
                "name": "gp2",
                "displayOrder": 1,
                "defaultType": true,
                "customLabel": true,
                "customSize": true,
                "customSizeOptions": null
            },
            {
                "id": 6,
                "code": "amazon-st1",
                "name": "st1",
                "displayOrder": 3,
                "defaultType": false,
                "customLabel": true,
                "customSize": true,
                "customSizeOptions": null
            }
        ],
        "rootStorageTypes": [
            {
                "id": 7,
                "code": "amazon-sc1",
                "name": "sc1",
                "displayOrder": 4,
                "defaultType": false,
                "customLabel": true,
                "customSize": true,
                "customSizeOptions": null
            },
            {
                "id": 4,
                "code": "amazon-io1",
                "name": "io1",
                "displayOrder": 2,
                "defaultType": false,
                "customLabel": true,
                "customSize": true,
                "customSizeOptions": null
            },
            {
                "id": 5,
                "code": "amazon-gp2",
                "name": "gp2",
                "displayOrder": 1,
                "defaultType": true,
                "customLabel": true,
                "customSize": true,
                "customSizeOptions": null
            },
            {
                "id": 6,
                "code": "amazon-st1",
                "name": "st1",
                "displayOrder": 3,
                "defaultType": false,
                "customLabel": true,
                "customSize": true,
                "customSizeOptions": null
            }
        ],
        "controllerTypes": []
    }
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/provision-types/:id`
