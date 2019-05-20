# Zone Types

Provides a means to find out which zone types are available for zone provisioning and in the  future what config properties are required. 

**NOTE:** A Zone Type in the API Is equivalent to a Cloud Type within the morpheus UI.

## Get All Zone Types

```shell
curl "https://api.gomorpheus.com/api/zone-types"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
{
  "zoneTypes": [
    {
      "id": 3,
      "name": "Amazon",
      "code": "amazon",
      "description": "amazon zone"
      serverTypes: [],
      optionTypes: []
    },
    {
      "id": 2,
      "name": "Openstack",
      "code": "openstack",
      "description": "openstac zone",
      serverTypes: [],
      optionTypes: []
    },
    {
      "id": 1,
      "name": "Standard",
      "code": "standard",
      "description": "Standard zone - manually managed servers or virtual machines"
      serverTypes: [],
      optionTypes: []
    }
  ]
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/zone-types`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | null | Max number of results to return. Default is all (no limit).
offset | 0 | Offset of records you want to load
sort | displayOrder | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
name | null | Filter by name or code
code | null | Filter by code
phrase | null | Filter by wildcard search of name, code and description
provisionType | null | Filter by [Provision Type](#provision-types) code

## Get Specific Zone Type

```shell
curl "https://api.gomorpheus.com/api/zone-types/1"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
{
  "success": true,
  "zoneType": {
    "id": 1,
    "name": "Standard",
    "code": "standard",
    "description": "Standard zone - manually managed servers or virtual machines"
    serverTypes: [],
    optionTypes: []
  }
}
```
### HTTP Request

`GET https://api.gomorpheus.com/api/zone-types/:id`

