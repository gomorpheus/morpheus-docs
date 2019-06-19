# User Settings

Provides API for managing your own user settings and api access tokens.

## Get User Settings

```shell
curl "https://api.gomorpheus.com/api/user-settings" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "user": {
    "id": 1,
    "username": "admin",
    "firstName": "Admin",
    "lastName": "",
    "email": "admin@morpheustestdata.com",
    "linuxUsername": "morphadmin",
    "linuxPassword": "************",
    "linuxKeyPairId": null,
    "windowsUsername": null,
    "windowsPassword": null,
    "avatar": null,
    "receiveNotifications": true
  },
  "accessTokens": [
    {
      "clientId": "morph-cli",
      "username": "admin",
      "expiration": "2019-11-20T02:19:18Z",
      "tokenType": "bearer"
    }
  ]
}
```

This endpoint retrieves your user settings and API access token information.

### HTTP Request

`GET https://api.gomorpheus.com/api/user-settings`

## Update User Settings

```shell
curl -XPUT "https://api.gomorpheus.com/api/user-settings" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "user": {
    "receiveNoticiations": true
  }
}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/user-settings`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
username      |  | Username
email      |  | Email
firstName      |  | First Name
lastName      |  | Last Name
password      |  | Change your password
linuxUsername      |  | Linux Username
linuxPassword      |  | Linux Password
linuxKeyPairId      |  | Linux Key Pair ID
windowsUsername      |  | Windows Username
windowsPassword      |  | Windows Password
receiveNotifications      |  | Receive Notifications (true or false)

## Update Avatar Image

```shell
curl -XPOST "https://api.gomorpheus.com/api/user-settings/avatar" \
  -H "Authorization: BEARER access_token" \
  -F 'user.avatar=@filename'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`POST https://api.gomorpheus.com/api/user-settings/avatar`

### Parameters

Parameter | Default | Description
--------- | ------- | -----------
user.avatar      |  | Image File png,jpg,svg

Upload a new avatar image.  Expects multipart form data as the request format, not JSON.

## Delete Avatar Image

```shell
curl -XDELETE "https://api.gomorpheus.com/api/user-settings/avatar" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/user-settings/avatar`

Delete your avatar image.  Expects multipart form data as the request format, not JSON.


## Regenerate API Access Token

```shell
curl -XPUT "https://api.gomorpheus.com/api/user-settings/regenerate-access-token?clientId=morph-api" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/user-settings/regenerate-access-token?clientId=:clientId`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
clientId      |  | Client ID

> The above command returns JSON structured like this:

```json
{
  "success": true,
  "token": "a936c304-374d-42c3-8634-8f825756d240"
}
```

This endpoint regenerates your API access token for the specified client. If a current token exists, it is revoked and a new token is returned.

## Revoke API Access Token

```shell
curl -XPUT "https://api.gomorpheus.com/api/user-settings/clear-access-token?clientId=morph-api" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/user-settings/clear-access-token?clientId=:clientId`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
clientId      |  | Client ID

This endpoint revokes your API access token for the specified client.

## Get Available API Clients

```shell
curl "https://api.gomorpheus.com/api/user-settings/api-clients" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
    "clients": [
    {
      "clientId": "morph-ios"
    },
    {
      "clientId": "morph-marketing"
    },
    {
      "clientId": "morph-customer"
    },
    {
      "clientId": "morph-cli"
    },
    {
      "clientId": "morph-api"
    }
  ]
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/user-settings/api-clients`

This endpoint retrieves a list of available API clients.
