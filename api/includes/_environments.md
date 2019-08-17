# Environments

Provides API interfaces for managing the creation and modification of provisioning environments.

## Get All Environments

```shell
curl "https://api.gomorpheus.com/api/environments"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "environments": [
    {
      "id": 1,
      "account": null,
      "code": "dev",
      "name": "Dev",
      "description": "Development",
      "visibility": null,
      "active": true,
      "sortOrder": 1,
      "dateCreated": "2016-08-27T19:26:09+0000",
      "lastUpdated": "2016-08-27T19:26:09+0000"
    },
    {
      "id": 2,
      "account": null,
      "code": "qa",
      "name": "Test",
      "description": "QA Test",
      "visibility": null,
      "active": true,
      "sortOrder": 2,
      "dateCreated": "2016-08-27T19:26:09+0000",
      "lastUpdated": "2016-08-27T19:26:09+0000"
    },
    {
      "id": 3,
      "account": null,
      "code": "staging",
      "name": "Staging",
      "description": "Staging",
      "visibility": null,
      "active": true,
      "sortOrder": 3,
      "dateCreated": "2016-08-27T19:26:09+0000",
      "lastUpdated": "2018-03-14T09:34:10+0000"
    },
    {
      "id": 4,
      "account": null,
      "code": "production",
      "name": "Production",
      "description": "Production",
      "visibility": null,
      "active": false,
      "sortOrder": 4,
      "dateCreated": "2016-08-27T19:26:09+0000",
      "lastUpdated": "2019-06-26T16:47:01+0000"
    }
  ],
  "meta": {
    "size": 4,
    "total": 5,
    "max": 25,
    "offset": 0
  }
}
```

This endpoint retrieves all environments.

### HTTP Request

`GET https://api.gomorpheus.com/api/environments`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase | null | Filter by matching name or code
name | null | Filter by name
code | null | Filter by code

## Get a Specific Environment

```shell
curl "https://api.gomorpheus.com/api/environments/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "environment": {
    "id": 1,
    "account": null,
    "code": "dev",
    "name": "Dev",
    "description": "Development",
    "visibility": null,
    "active": true,
    "sortOrder": 1,
    "dateCreated": "2016-08-27T19:26:09+0000",
    "lastUpdated": "2016-08-27T19:26:09+0000"
  }
}
```

This endpoint will retrieve a specific environment by id

### HTTP Request

`GET https://api.gomorpheus.com/api/environments/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the environment

## Create an Environment

```shell
curl -XPOST "https://api.gomorpheus.com/api/environments" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "environment": {
    "name": "Dev B",
    "code": "devb",
    "description": "Our other dev team",
    "sortOrder": 4,
    "visibility": "private"
  }
}'
```

> The above command returns JSON structured like getting a single environment:

### HTTP Request

`POST https://api.gomorpheus.com/api/environments`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | A unique name for the environment
code      |  | A unique code for the environment
description      |  | A description of the environment
visibility | "private" | private or public
sortOrder | 0 | Sort order


## Updating an Environment

```shell
curl -XPUT "https://api.gomorpheus.com/api/environments/5" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "environment": {
    "description": "The Dev B environment",
  }
}'
```

> The above command returns JSON structured like getting a single environment:

### HTTP Request

`PUT https://api.gomorpheus.com/api/environments/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the environment

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | A unique name for the environment
description      |  | A description of the environment
visibility |  | private or public
sortOrder |  | Sort order
active |  | Set to false to deactvate the environment

Only user created environments may be updated.

## Toggle an Environment

```shell
curl -XPUT "https://api.gomorpheus.com/api/environments/5/toggle-active" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like getting a single environment:

### HTTP Request

`PUT https://api.gomorpheus.com/api/environments/:id/toggle-active`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the environment

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
active      | (toggle) | Pass true or false explicitly. Default is to toggle the current value.

Setting active to false will remove it from the list of available environments, making it unavailable during provisioning.
This endpoint allows global environments to be updated by the master account.

## Delete an Environment

```shell
curl -XDELETE "https://api.gomorpheus.com/api/environments/5" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/environments/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the environment

Only user created environments may be deleted.
