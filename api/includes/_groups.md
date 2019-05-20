# Server Groups

Server Groups are used to organize provisioned servers in your infrastructure. When a user on the system provisions an instance like MySQL, they can select which group to provision the instance into. This can be used to scope servers by environment or by region.

## Get All Groups

```shell
curl "https://api.gomorpheus.com/api/groups"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "groups": [
    {
      "id": 1,
      "accountId": 1,
      "name": "Amazon East",
      "code": "amazon",
      "active": true,
      "location": null,
      "visibility": "public",
      "zones": [
        {
          "id": 1,
          "accountId": 1,
          "groupId": 1,
          "name": "VPC 1a",
          "description": "1a VPC Subnet",
          "location": null,
          "visibility": "public",
          "zoneTypeId": 1
        }
      ]
    }
  ]
}
```

This endpoint retrieves all groups and a list of zones associated with the group by id.

### HTTP Request

`GET https://api.gomorpheus.com/api/groups`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
lastUpdated | null | A date filter, restricts query to only load groups updated more recent or equal to the date specified
name | null | If specified will return an exact match group


<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>

## Get a Specific Group


```shell
curl "https://api.gomorpheus.com/api/groups/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "success": true,
  "group": {
    "id": 1,
    "accountId": 1,
    "name": "Vagrant",
    "code": null,
    "active": true,
    "location": null,
    "visibility": "public",
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
}
```

This endpoint retrieves a specific group.


### HTTP Request

`GET https://api.gomorpheus.com/api/groups/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the group to retrieve

## Create a Group

```shell
curl -XPOST "https://api.gomorpheus.com/api/groups" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"group":{
    "name": "My Group",
    "description": "My description",
    "location": "US EAST"
  }}'
```

> The above command returns JSON structured like getting a single group:

### HTTP Request

`POST https://api.gomorpheus.com/api/groups`

### JSON Check Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to your account for the group
code      | null | Optional code for use with policies
location  | null | Optional location argument for your group

<aside class="warning">Creating a Server group requires the `System Admin` role.</aside>

## Updating a Group

```shell
curl -XPUT "https://api.gomorpheus.com/api/groups/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"group":{
    "name": "My Group",
    "location": "US EAST"
  }}'
```

> The above command returns JSON structured like getting a single group:

### HTTP Request

`PUT https://api.gomorpheus.com/api/groups/:id`

### JSON Check Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to your account for the group
code      | null | Optional code for use with policies
location  | null | Optional location for your group

<aside class="warning">Updating a Server group requires the `System Admin` role.</aside>

## Updating Group Zones

```shell
curl -XPUT "https://api.gomorpheus.com/api/groups/1/update-zones" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"group":{
    "zones": [
      {"id": 1}, {"id": 2}, {"id": 5}
    ]
  }}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

This will update the zones that are assigned to the group.
Any zones that are not passed in the `zones` parameter will be removed from the group.

### HTTP Request

`PUT https://api.gomorpheus.com/api/groups/:id/update-zones`

### JSON Check Parameters

Parameter | Default | Description
--------- | ------- | -----------
zones      | null | An array of all the zones assigned to this group.

<aside class="warning">Assigning Zones to a Server group requires the `System Admin` role.</aside>


## Delete a Group

```shell
curl -XDELETE "https://api.gomorpheus.com/api/groups/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

If a group has zones or servers still tied to it, a delete action will fail

### HTTP Request

`DELETE https://api.gomorpheus.com/api/groups/:id`
