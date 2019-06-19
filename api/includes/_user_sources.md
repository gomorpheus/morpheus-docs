# User Sources

User Sources can be configured for each Tenant.
Supported types include LDAP, JumpCloud, Active Directory, and others.

<aside class="notice">
This API is only available to the master account.
</aside>

## Get All User Sources

```shell
curl "https://api.gomorpheus.com/api/user-sources"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "userSources": [
    {
      "id": 17,
      "name": "jump cloud",
      "description": "our jump cloud users",
      "code": "KsUGxwhTU",
      "type": "jumpCloud",
      "active": true,
      "deleted": false,
      "autoSyncOnLogin": true,
      "account": {
        "id": 59,
        "name": "acme"
      },
      "defaultAccountRole": {
        "id": 19,
        "authority": "Basic User"
      },
      "roleMappings": [

      ],
      "subdomain": "acme",
      "dateCreated": "2018-03-22T01:57:12+0000",
      "lastUpdated": "2018-03-22T01:57:12+0000"
    }
  ],
  "meta": {
    "size": 1,
    "total": 1,
    "max": 25,
    "offset": 0
  }
}
```

This endpoint retrieves all user sources.

### HTTP Request

`GET https://api.gomorpheus.com/api/user-sources`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
phrase | null | Filter on wildcard match of name or description
name | null | Filter on exact match of name
type | null | Filter on exact match of type code

## Get a Specific User Source

```shell
curl "https://api.gomorpheus.com/api/user-sources/2" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "userSource": {
    "id": 17,
    "name": "jump cloud",
    "description": "our jump cloud users",
    "code": "KsUGxwhTU",
    "type": "jumpCloud",
    "active": true,
    "deleted": false,
    "autoSyncOnLogin": true,
    "account": {
      "id": 59,
      "name": "acme"
    },
    "defaultAccountRole": {
      "id": 19,
      "authority": "Basic User"
    },
    "config": {
      "organizationId": "34a927g43e21be3786b2343b",
      "bindingPassword": "************",
      "bindingUsername": "jumpadmin",
      "requiredRole": "MorpheusTag"
    },
    "roleMappings": [

    ],
    "subdomain": "acme",
    "loginURL": "https://app.gomorpheusdata.com/login/account/acme",
    "dateCreated": "2018-03-22T01:57:12+0000",
    "lastUpdated": "2018-03-22T01:57:12+0000"
  }
}
```

This endpoint retrieves a specific user source.


### HTTP Request

`GET https://api.gomorpheus.com/api/user-sources/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the user source

## Create a User Source

```shell
curl -XPOST "https://api.gomorpheus.com/api/accounts/60/user-sources" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"userSource": {
    "type": "activeDirectory",
    "name": "Ninja AD",
    "config": {
      "url": "10.30.10.155",
      "domain": "ad.morpheusdata.ninja",
      "useSSL": "on",
      "bindingUsername": "adadmin",
      "bindingPassword": "goodadpassword",
      "requiredGroup": "MorpheusUsers",
      "searchMemberGroups": "off"
    },
    "defaultAccountRole": {
      "id": 19
    }
  }
}'
```

> The above command returns JSON structured like getting a single user source: 

### HTTP Request

`POST https://api.gomorpheus.com/api/accounts/:accountId/user-sources`

### URL Parameters

Parameter | Description
--------- | -----------
accountId | The ID of the subtenant account to associate the user source with

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | Name
type      | null | Type code (ldap, jumpCloud, activeDirectory, okta, oneLogin, saml, customExternal, customApi)
description | null | Description (optional)
defaultAccountRole.id | null | Default Role ID
roleMappings | {} | Map of Morpheus Role ID : Fully Qualified Role Name
roleMappingNames | {} | Map of Morpheus Role ID : Role Name
config | {} | Map of configuration options which vary by type.

### JSON Parameters for LDAP

Parameter | Default | Description
--------- | ------- | -----------
config.url      | null | URL
config.bindingUsername      | null | Binding Username
config.bindingPassword      | null | Binding Password
config.requiredGroup      | null | Required group name (a.k.a. tag)

### JSON Parameters for jumpCloud

Parameter | Default | Description
--------- | ------- | -----------
config.organizationId      | false | Organization ID
config.bindingUsername      | null | Binding Username
config.bindingPassword      | null | Binding Password
config.requiredRole      | null | Required group name (a.k.a. tag)

### JSON Parameters for activeDirectory

Parameter | Default | Description
--------- | ------- | -----------
config.url      | null | AD Server
config.domain      | null | Domain
config.useSSL      | false | Use SSL
config.bindingUsername      | null | Binding Username
config.bindingPassword      | null | Binding Password
config.requiredGroup      | null | Required Group
config.searchMemberGroups      | null | Include Member Groups

### JSON Parameters for okta

Parameter | Default | Description
--------- | ------- | -----------
config.url      | null | OKTA URL
config.administratorAPIToken      | null | Adminstrator API Token
config.requiredGroup      | null | Required Group

### JSON Parameters for oneLogin

Parameter | Default | Description
--------- | ------- | -----------
config.subdomain      | null | OneLogin Subdomain
config.region      | null | OneLogin Region
config.clientSecret      | null | API Client Secret
config.clientId      | null | API Client ID
config.requiredRole      | null | Required Role

### JSON Parameters for saml

Parameter | Default | Description
--------- | ------- | -----------
config.url      | null | Login Redirect URL
config.doNotIncludeSAMLRequest      | false | Exclude SAMLRequest Parameter
config.logoutUrl      | null | Logout Post URL
config.publicKey      | null | Signing Public Key

### JSON Parameters for customExternal

Parameter | Default | Description
--------- | ------- | -----------
config.loginUrl      | null | External Login URL
config.doNotIncludeSAMLRequest      | false | Do not include SAMLRequest
config.logout      | null | External Logout URL
config.encryptionAlgo      | null | Encryption Algorithm ('NONE','AES','DES','DESede','HmacSHA1', 'HmacSHA256')
config.encryptionKey      | null | Encryption Key

### JSON Parameters for customApi

Parameter | Default | Description
--------- | ------- | -----------
config.endpoint      | null | API Endpoint
config.apiStyle      | null | API Style ('Form URL Encoded [GET]','Form URL Encoded [POST]','JSON [POST]','XML [POST]','HTTP Basic [GET]')
config.encryptionAlgo      | null | Encryption Algorithm ('NONE','AES','DES','DESede','HmacSHA1', 'HmacSHA256')
config.encryptionKey      | null | Encryption Key

## Updating a User Source

```shell
curl -XPUT "https://api.gomorpheus.com/api/user-sources/3" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"userSource": {
    "type": "activeDirectory",
    "name": "Ninja AD",
    "config": {
      "url": "10.30.10.155",
      "domain": "ad.morpheusdata.ninja",
      "useSSL": "on",
      "bindingUsername": "adadmin",
      "bindingPassword": "goodadpassword",
      "requiredGroup": "MorpheusUsers",
      "searchMemberGroups": "off"
    },
    "defaultAccountRole": {
      "id": 19
    }
  }
}'
```

> The above command returns JSON structured like getting a single user source: 

### HTTP Request

`PUT https://api.gomorpheus.com/api/user-sources/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the user source

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | Name
description | null | Description (optional)
active      | null | Activate (true) or disable (false) the user source
defaultAccountRole.id | null | Default Role ID
roleMappings | {} | Map of Morpheus Role ID : Fully Qualified Role Name
roleMappingNames | {} | Map of Morpheus Role ID : Role Name
config | {} | Map of configuration options which vary by type.

## Updating Subdomain for a User Source

```shell
curl -XPUT "https://api.gomorpheus.com/api/user-sources/3/subdomain" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"subdomain": "ninjas"}'
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`PUT https://api.gomorpheus.com/api/user-sources/:id/subdomain`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the user source

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
subdomain      | null | New Subdomain for account

This endpoint updates the subdomain for the account associated with the user source.

## Delete a User Source

```shell
curl -XDELETE "https://api.gomorpheus.com/api/user-sources/3" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/user-sources/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the user source

Will delete a user source from the system and make it no longer usable.

<aside class="warning">
If a user source is tied to existing users, a delete will fail.
</aside>
