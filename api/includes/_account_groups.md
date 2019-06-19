# Subtenant Groups

Groups belonging to a subtenant can be managed by the master account.

## Get All Groups for Subtenant

```shell
curl "https://api.gomorpheus.com/api/accounts/20/groups"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "groups": [
    {
      "id": 365,
      "name": "testgroup",
      "code": "testgroup",
      "location": "West",
      "accountId": 20,
      "visibility": "public",
      "active": true,
      "dateCreated": "2018-03-20T20:34:22+0000",
      "lastUpdated": "2018-03-31T18:32:56+0000",
      "zones": [
        {
          "id": 32,
          "name": "test-google"
        },
        {
          "id": 33,
          "name": "test-vmware"
        }
      ]
    }
  ],
  "meta": {
    "offset": 0,
    "max": 25,
    "size": 1,
    "total": 1
  }
}
```

This endpoint retrieves all groups and a list of zones associated with the group by id.

### HTTP Request

`GET https://api.gomorpheus.com/api/accounts/:accountId/groups`

### URL Parameters

Parameter | Description
--------- | -----------
accountId | The ID of the subtenant account

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
phrase | null | Filter on partial match of name or location
name | null | Filter on exact match of name
lastUpdated | null | A date filter, restricts query to only load groups updated more recent or equal to the date specified

## Get a Specific Group for Subtenant

```shell
curl "https://api.gomorpheus.com/api/accounts/20/groups/365" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "group": {
      "id": 365,
      "name": "testgroup",
      "code": "testgroup",
      "location": "West",
      "accountId": 20,
      "visibility": "public",
      "active": true,
      "dateCreated": "2018-03-20T20:34:22+0000",
      "lastUpdated": "2018-03-31T18:32:56+0000",
      "zones": [
        {
          "id": 32,
          "name": "test-google"
        },
        {
          "id": 33,
          "name": "test-vmware"
        }
      ]
    }
}
```

This endpoint retrieves a specific group.


### HTTP Request

`GET https://api.gomorpheus.com/api/accounts/:accountId/groups/:id`

### URL Parameters

Parameter | Description
--------- | -----------
accountId | The ID of the subtenant account
id | The ID of the group to retrieve

## Create a Group for Subtenant

```shell
curl -XPOST "https://api.gomorpheus.com/api/accounts/20/groups" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"group":{
    "name": "My Group",
    "description": "My description",
    "location": "West"
  }}'
```

> The above command returns JSON structured like getting a single group:

### HTTP Request

`POST https://api.gomorpheus.com/api/accounts/:accountId/groups`

### URL Parameters

Parameter | Description
--------- | -----------
accountId | The ID of the subtenant account

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to the subtenant for the group
description | null | Optional description field if you want to put more info there
code      | null | Optional code for use with policies
location  | null | Optional location argument for the group

## Updating a Group for Subtenant

```shell
curl -XPUT "https://api.gomorpheus.com/api/accounts/20/groups/365" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"group":{
    "name": "My Group",
    "description": "My description",
    "location": "West"
  }}'
```

> The above command returns JSON structured like getting a single group:

### HTTP Request

`PUT https://api.gomorpheus.com/api/accounts/:accountId/groups/:id`

### URL Parameters

Parameter | Description
--------- | -----------
accountId | The ID of the subtenant account
id | The ID of the group

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to the subtenant for the group
description | null | Optional description field if you want to put more info there
code      | null | Optional code for use with policies
location  | null | Optional location for the group

## Updating Group Zones for Subtenant

```shell
curl -XPUT "https://api.gomorpheus.com/api/accounts/20/groups/365/update-zones" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"group":{
    "zones": [
      {"id": 32}, {"id": 33}, {"id": 34}
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

`PUT https://api.gomorpheus.com/api/accounts/:id/groups/:groupId/update-zones`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
zones      | null | An array of all the zones assigned to this group.


## Delete a Group for Subtenant

```shell
curl -XDELETE "https://api.gomorpheus.com/api/accounts/20/groups/365" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/accounts/:id/groups/:groupId`

If a group has zones or servers still tied to it, a delete action will fail
