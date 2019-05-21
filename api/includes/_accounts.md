# Accounts

Provides API interfaces for managing the creation and modification of accounts within Morpheus (Typically only accessible by the Master Account)

## Get All Accounts

```shell
curl "https://api.gomorpheus.com/api/accounts"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "accounts": [
    {
      "id": 1,
      "name": "Root Account",
      "description": "The master account",
      "currency": "USD",
      "instanceLimits": null,
      "lastUpdated": "2015-11-10T18:58:55+0000",
      "dateCreated": "2015-11-10T18:58:55+0000",
      "role": {
        "id": 1,
        "authority": "System Admin",
        "description": "Super User"
      },
      "active": true
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

This endpoint retrieves all accounts.

### HTTP Request

`GET https://api.gomorpheus.com/api/accounts`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort
phrase | null | Filter by matching name or description
name | null | Filter by name
lastUpdated | null | Date filter, restricts query to only load accounts updated  timestamp is more recent or equal to the date specified


## Get a Specific Account

```shell
curl "https://api.gomorpheus.com/api/accounts/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "account": {
    "id": 1,
    "name": "Root Account",
    "description": "The master account",
    "currency": "USD",
    "instanceLimits": null,
    "externalId": null,
    "lastUpdated": "2015-11-10T18:58:55+0000",
    "dateCreated": "2015-11-10T18:58:55+0000",
    "role": {
      "id": 1,
      "authority": "System Admin",
      "description": "Super User"
    },
    "active": true
  }
}
```

This endpoint will retrieve a specific account by id if the user has permission to access it.

### HTTP Request

`GET https://api.gomorpheus.com/api/accounts/:id`

## Create an Account

```shell
curl -XPOST "https://api.gomorpheus.com/api/accounts" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"account":{
    "name": "My New Account",
    "description": "My description",
    "instanceLimits": {
      "maxCpu": 0,
      "maxMemory": 0,
      "maxStorage": 0
    },
    role: {
      id: 2
    }
  }}'
```

> The above command returns JSON structured like getting a single account:

### HTTP Request

`POST https://api.gomorpheus.com/api/accounts`

### JSON Account Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name for the account
description | null | Optional description field if you want to put more info there
role      | Account Admin | A nested id of the default role for the account
instanceLimits | null | Optional JSON Map of maxCpu, maxMemory (bytes) and maxStorage (bytes) restrictions (0 means unlimited). The parameters maxMemoryMiB, maxMemoryGiB, maxStorageMiB and maxStorageGiB can be used to pass values in larger units.


## Updating an Account

```shell
curl -XPUT "https://api.gomorpheus.com/api/accounts/2" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"account":{
    "name": "My New Account",
    "description": "My new description",
    "instanceLimits": {
      "maxCpu": 0,
      "maxMemory": 0,
      "maxStorage": 0
    },
    "role": {
      id: 3
    }
  }}'
```

> The above command returns JSON structured like getting a single account:

### HTTP Request

`PUT https://api.gomorpheus.com/api/accounts/:id`

### JSON Account Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name for the account
description | null | Optional description field if you want to put more info there
role      | null | A nested id of the default role for the account
active | null | Set to false to deactvate the account

## Delete an Account

```shell
curl -XDELETE "https://api.gomorpheus.com/api/accounts/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

If an account still has users or instances tied to it, The delete will fail.

<aside class="info">This restriction should be lifted in a forthcoming API release</aside>

### HTTP Request

`DELETE https://api.gomorpheus.com/api/accounts/:id`
