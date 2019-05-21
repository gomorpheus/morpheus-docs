# Data Stores

Data Stores can be managed for each Compute Zone (Cloud) in your infrastructure.

## Get All Data Stores for Cloud

```shell
curl "https://api.gomorpheus.com/api/zones/5/data-stores"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "datastores": [
    {
      "id": 50,
      "name": "datastore1",
      "zone": {
        "id": 34,
        "name": "test-vmware"
      },
      "type": "generic",
      "freeSpace": 421317836800,
      "online": false,
      "active": false,
      "visibility": "private",
      "tenants": [
        {
          "id": 1,
          "name": "root"
        }
      ]
    }
  ],
  "meta": {
    "size": 7,
    "total": 7,
    "max": 25,
    "offset": 0
  }
}
```

This endpoint retrieves all data stores under a cloud.

### HTTP Request

`GET https://api.gomorpheus.com/api/zones/:zoneId/data-stores`

### URL Parameters

Parameter | Description
--------- | -----------
zoneId | The ID of the cloud

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
phrase | null | Filter on partial match of name
name | null | Filter on exact match of name

## Get a Specific Data Store

```shell
curl "https://api.gomorpheus.com/api/zones/5/data-stores/50" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "datastore": {
    "id": 50,
    "name": "datastore1",
    "zone": {
      "id": 34,
      "name": "test-vmware"
    },
    "type": "generic",
    "freeSpace": 421317836800,
    "online": true,
    "active": true,
    "visibility": "private",
    "tenants": [
      {
        "id": 1,
        "name": "root"
      }
    ],
    "resourcePermission": {
      "all": false,
      "sites": [
        {
          "id": 1,
          "name": "group1"
        },
        {
          "id": 2,
          "name": "group2"
        },
      ]
    }
  }
}
```

This endpoint retrieves a specific data store.


### HTTP Request

`GET https://api.gomorpheus.com/api/zones/:zoneId/data-stores/:id`

### URL Parameters

Parameter | Description
--------- | -----------
zoneId | The ID of the cloud
id | The ID of the data store to retrieve

## Updating a Data Store

```shell
curl -XPUT "https://api.gomorpheus.com/api/zones/5/data-stores/50" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"datastore":{
    "active": true,
    "visibility": "private",
    "tenantPermissions": {
      "accounts": [1,2,3,4,5]
    },
    "resourcePermissions": {
      "all": false,
      "sites": [
        {"id": 1}, {"id": 2}, {"id": 3}
      ]
    }
  }}'
```

> The above command returns JSON structured like getting a single data store:

This endpoint allows updating settings for a data store.

### HTTP Request

`PUT https://api.gomorpheus.com/api/zones/:zoneId/data-stores/:id`

### URL Parameters

Parameter | Description
--------- | -----------
zoneId | The ID of the cloud
id | The ID of the data store

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
active      | null | Activate (true) or disable (false) the datastore
visibility      | private | private or public
tenantPermissions.accounts  | null | Array of tenant account ids that are allowed access
resourcePermissions.all  | null | Pass true to allow access all groups
resourcePermissions.sites  | null | Array of groups that are allowed access
