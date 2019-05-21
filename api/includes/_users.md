# Users

Managing users via the API is always scoped to a specific account. Most of the API's regarding user management require that the account Id of the user also be known

## Get All Users for an Account

```shell
curl "https://api.gomorpheus.com/api/accounts/1/users"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "users": [
    {
      "id": 1,
      "accountId": 1,
      "username": "davydotcom",
      "displayName": "David Estes",
      "email": "destes@bcap.com",
      "firstName": "David",
      "lastName": "Estes",
      "dateCreated": "2015-11-10T18:58:55+0000",
      "lastUpdated": "2015-11-10T18:58:55+0000",
      "enabled": true,
      "accountExpired": false,
      "accountLocked": false,
      "passwordExpired": false,
      "role": {
        "id": 1,
        "authority": "System Admin",
        "description": "Super User"
      },
      "account": {
        "id": 1,
        "name": "Root Account"
      },
      "instanceLimits": null
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

`GET https://api.gomorpheus.com/api/accounts/:accountId/users`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | name | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort order
phrase | null | Filter by matching firstName, lastName, username, or email
username | null | Filter by username
lastUpdated | null | Date filter, restricts query to only load users updated  timestamp is more recent or equal to the date specified


## Get a Specific User

```shell
curl "https://api.gomorpheus.com/api/accounts/1/users/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "user": {
    "id": 1,
    "accountId": 1,
    "username": "davydotcom",
    "displayName": "David Estes",
    "email": "destes@bcap.com",
    "firstName": "David",
    "lastName": "Estes",
    "dateCreated": "2015-11-10T18:58:55+0000",
    "lastUpdated": "2015-11-10T18:58:55+0000",
    "enabled": true,
    "accountExpired": false,
    "accountLocked": false,
    "passwordExpired": false,
    "role": {
      "id": 1,
      "authority": "System Admin",
      "description": "Super User"
    },
    "account": {
      "id": 1,
      "name": "Root Account"
    },
    "instanceLimits": null
  }
}
```

This endpoint will retrieve a specific user by id if the user has permission to access the user.

### HTTP Request

`GET https://api.gomorpheus.com/api/accounts/:accountId/users/:id`

## Create a User

```shell
curl -XPOST "https://api.gomorpheus.com/api/accounts/1/users" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"user":{
    "username": "testuser",
    "email": "testuser@yourcompany.com",
    "firstName": "Test",
    "lastName": "User",
    "password": "aStrongpassword123!",
    "role": {"id": 1}
  }}'
```

> The above command returns JSON structured like getting a single user:

### HTTP Request

`POST https://api.gomorpheus.com/api/accounts/:accountId/users`

### JSON User Parameters

Parameter | Default | Description
--------- | ------- | -----------
username  | null | A unique username
email     | null | The user's email
firstName | null | The user's first name (optional)
lastName  | null | The user's last name (optional)
password  | null | The password to apply to the user
role      | null | A nested id of the role to assign to the user
instanceLimits | null | Optional JSON Map of maxCpu, maxMemory (bytes) and maxStorage (bytes) restrictions (0 means unlimited). The parameters maxMemoryMiB, maxMemoryGiB, maxStorageMiB and maxStorageGiB can be used to pass values in larger units.


## Updating a User

```shell
curl -XPUT "https://api.gomorpheus.com/api/accounts/1/users/2" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"user":{
    "username": "testUser",
    "firstName": "Jane",
    "lastName": "Doe",
    "password": "abc123",
    "role": {"id": 1},
    "instanceLimits": {
      "maxCpu": 0,
      "maxMemory": 0,
      "maxStorage": 0
    }
  }}'
```

> The above command returns JSON structured like getting a single user:

### HTTP Request

`PUT https://api.gomorpheus.com/api/accounts/:accountId/users/:id`

### JSON User Parameters

Parameter | Default | Description
--------- | ------- | -----------
username  | null | A unique username
email     | null | The user's email
firstName | null | The user's first name (optional)
lastName  | null | The user's last name (optional)
password  | null | The password to apply to the user
role      | null | A nested id of the role to assign to the user
instanceLimits | null | Optional JSON Map of maxCpu, maxMemory (bytes) and maxStorage (bytes) restrictions (0 means unlimited). The parameters maxMemoryMiB, maxMemoryGiB, maxStorageMiB and maxStorageGiB can be used to pass values in larger units.

## Delete a User

```shell
curl -XDELETE "https://api.gomorpheus.com/api/accounts/1/users/2" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

This will disassociate the user from any instances they have previously provisioned.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/accounts/:accountId/users/:id`
