# Provisioning

Provisioning options will depend heavily on the cloud you are provisioning to.  This section is broken out into options based on the instance-type that is being created.

## Provision an Instance

```shell
curl -X POST "https://api.gomorpheus.com/api/instances" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "zoneId": 6,
  "instance": {
    "name": "api-testing2",
    "site": {
      "id": 3
    },
    "instanceType": {
      "code": "Ubuntu"
    },
    "layout": {
      "id": 105
    },
    "plan": {
      "id": 75
    }
  },
  "volumes": [
    {
      "id": -1,
      "rootVolume": true,
      "name": "root",
      "size": 10,
      "sizeId": null,
      "storageType": 1,
      "datastoreId": "autoCluster"
    },
    {
      "id": -1,
      "rootVolume": false,
      "name": "data",
      "size": 5,
      "sizeId": null,
      "storageType": 1,
      "datastoreId": "auto"
    }
  ],
  "networkInterfaces": [
    {
      "network": {
        "id": 5
      },
      "networkInterfaceTypeId": 4
    }
  ],
  "config": {
    "publicKeyId": 14,
    "vmwareResourcePoolId": "resgroup-56",
    "hostId": null,
    "vmwareUsr": "morpheus-api",
    "vmwarePwd": "password",
    "vmwareDomainName": null,
    "vmwareCustomSpec": null
  },
  "evars": [
    {"name": "MY_APP_VAR1", "value": "VALUE1"},
    {"name": "MY_APP_VAR2", "value": "VALUE2"}
  ],
}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single check 

### HTTP Request

`POST https://api.gomorpheus.com/api/instances`

### JSON Parameters

Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
instance  | Y | n/a | Key for name, site, instanceType layout, and plan
instance.name | Y | null | Name of the instance to be created
instance.site.id | Y | null | The Group ID to provision the instance into
instance.instanceType.code | Y | null | The type of instance by code we want to fetch
instance.layout.id |  Y | null | The layout id for the instance type that you want to provision. i.e. single process or cluster
instance.plan.id | Y | null | The id for the memory and storage option pre-configured within Morpheus. See [Available Service Plans](##get-available-service-plans-for-an-instance)
zoneId | Y | null | The Cloud ID to provision the instance onto
evars | N | [] | Environment Variables, an array of objects that have name and value.
copies | N | 1 | Number of copies to provision
layoutSize | N | 1 | Apply a multiply factor of containers/vms within the instance
servicePlanOptions | N | null | Map of custom options depending on selected service plan . An example would be `maxMemory`, or `maxCores`.
securityGroups | N | null | Key for security group configuration. It should be passed as an array of objects containing the id of the security group to assign the instance to
volumes | N | null | Key for volume configuration, see [Volumes](#volumes)
networkInterfaces | N | null | Key for network configuration, see [Network Interfaces](#network-interfaces)
config | Y | null | Key for specific type configuration, see [Config](#config)
metadata | N | null | Array of name-value pairs for AWS metadata tags [Metadata](#metadata)
taskSetId | N | null | The Workflow ID to execute.
taskSetName | N | null | The Workflow Name to execute.

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

##### JSON Config Parameters for VMware
Parameter | Required | Default | Description
--------- | -------- | ------- | -----------
publicKeyId | N | null | ID of a public key to add to the instance
vmwareResourcePoolId | Y | null | ID of the resource group to use for instance
hostId | N | null | Specific host to deploy to if so desired
vmwareUsr | N | null | Additional user to provision to instance
vmwarePwd | N | null | Password for additional user
vmwareDomainName | N | null | Domain name to be given to instance
vmwareCustomSpec | N | null | Customization spec ID

#### Metadata
This is specific to AWS Metadata tags.  Name-Values pairs can be anything you like and are added to the instance JSON as an array of n-v pairs per the example to the right:

```shell
-d '{
  "zoneId": 6,
  "instance": {
    ...
  }
  ...
  "metadata": [
    {
      "id": null,
      "name": "SampleName",
      "value": "SampleValue"
    }
    {
      "id": null,
      "name": "BusinessUnit",
      "value": "QualityAssurance"
    }
  ]
  ...
}
```


**Documentation on ALL of the provision types to come...**



There can be additional properties to apply to the instance. For example mysql provisioning requires a set of initial credentials. You can get a list of what these input options are by fetching the instance-types list via the `instance-types` api and getting available layouts as well as the provision type option types associated with the layout. Currently these input options are available from the option-types map. These however, can be overridden in the event a config options map exists on the layout object within. **NOTE**: See the API Document on OptionTypes for figuring out how to build property maps from them.