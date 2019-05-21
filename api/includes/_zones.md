# Compute Zones

Zones are a means of zoning various servers based on provisioning type or subnets. Typically a Zone belongs to a zone and a zone can have many zones. There are several supported zone types that can be used for hardware/vm procurement such as the OpenStack zone type. The zone holds the credentials necessary to provision virtual machines on the open stack api. Amazon is another openstack zone type currently in the works. Of course, we also have the Standard zone type which allows for manual vm procurement.

## Get All Zones

```shell
curl "https://api.gomorpheus.com/api/zones"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "zones": [
    {
      "id": 1,
      "accountId": 1,
      "groupId": 1,
      "name": "Davids Laptop",
      "description": "My Laptop Vagrant",
      "location": null,
      "visibility": "public",
      "zoneTypeId": 1
    }
  ]
}
```

This endpoint retrieves all zones and a list of zones associated with the zone by id.

### HTTP Request

`GET https://api.gomorpheus.com/api/zones`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
lastUpdated | null | A date filter, restricts query to only load zones updated more recent or equal to the date specified
name | null | If specified will return an exact match zone
type | null | If specified will return all zones by type code (`standard`,`openstack`,`amazon`)
groupId | null | If specified will return all zones assigned to a server group by id.


<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>

## Get a Specific Zone


```shell
curl "https://api.gomorpheus.com/api/zones/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "success": true,
  "zone": {
    "id": 1,
    "accountId": 1,
    "groupId": 1,
    "name": "Davids Laptop",
    "description": "My Laptop Vagrant",
    "location": null,
    "visibility": "public",
    "zoneTypeId": 1
  }
}
```

This endpoint retrieves a specific zone.


### HTTP Request

`GET https://api.gomorpheus.com/api/zones/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the zone to retrieve

## Create a Zone

```shell
curl -XPOST "https://api.gomorpheus.com/api/zones" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"zone":{
    "name": "My Zone",
    "code": "myzone",
    "description": "My description",
    "location": "US EAST",
    "zoneType": {"code": "standard"},
    "groupId": 1
  }}'
```

> The above command returns JSON structured like getting a single zone:

### HTTP Request

`POST https://api.gomorpheus.com/api/zones`

### JSON Check Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to your account for the zone
description | null | Optional description field if you want to put more info there
code      | null | Optional code for use with policies
location  | null | Optional location for your zone
visibility      | private | private or public
zoneType  | "standard" | Map containing code or id of the zone type
groupId  | null | Specifies which Server group this zone should be assigned to
accountId | null | Specifies which Tenant this zone should be assigned to

Additional properties are dynamic for the most part depending on teh zone/cloud type. To determine what these are please look at the `optionTypes` list on the `ZoneType` record.

<aside class="warning">Creating a Server zone requires the `System Admin` role.</aside>

## Updating a Zone

```shell
curl -XPUT "https://api.gomorpheus.com/api/zones/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"zone":{
    "name": "My Zone",
    "description": "My description",
    "location": "US EAST",
    "zoneType": {"code": "standard"},
    "groupId": 1,
    "config": null
  }}'
```

> The above command returns JSON structured like getting a single zone:

### HTTP Request

`PUT https://api.gomorpheus.com/api/zones/:id`

### JSON Check Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to your account for the zone
description | null | Optional description field if you want to put more info there
code      | null | Optional code for use with policies
location  | null | Optional location for your zone
visibility      | private | private or public
accountId | null | Specifies which Tenant this zone should be assigned to
config | null | For non standard zone types, this is a json encoded string with config properties for openstack and Amazon. See the section on specific zone types for details.

Additional properties are dynamic for the most part depending on the zone/cloud type. To determine what these are please look at the `optionTypes` list on the `ZoneType` record.

<aside class="warning">Updating a Server zone requires the `System Admin` role.</aside>

## Delete a Zone

```shell
curl -XDELETE "https://api.gomorpheus.com/api/zones/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

If a zone has zones or servers still tied to it, a delete action will fail

### HTTP Request

`DELETE https://api.gomorpheus.com/api/zones/:id`

## Get Security Groups

```shell
curl -XGET "https://api.gomorpheus.com/api/zones/1/security-groups" \
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

This returns a list of all of the security groups applied to a zone and whether the firewall is enabled.

### HTTP Request

`GET https://api.gomorpheus.com/api/zones/:id/security-groups`


## Set Security Groups

```shell
curl -XPOST "https://api.gomorpheus.com/api/zones/1/security-groups" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "securityGroupIds": [19, 2] }'
```

> The above command returns JSON structure similar to the 'get' of security groups.

### HTTP Request

`POST https://api.gomorpheus.com/api/zones/:id/security-groups`

### JSON Parameters

Parameter   | Default | Description
---------   | ------- | -----------
securityGroupIds | null | List of all security groups ids which should be applied.  If no security groups should apply, pass '[]'

