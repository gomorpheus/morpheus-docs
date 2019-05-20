# Cypher

Cypher at its core is a secure Key/Value store. But what makes cypher useful is the ability to securely store or generate credentials to connect to your instances. Not only are these credentials encrypted but by using a cypher you don't have to burn in connection credentials between instances into your apps.

Cypher keys can be revoked, either through lease timeouts or manually. So even if somebody were to gain access to your keys you could revoke access to the keys and generate new ones for your applications.

## Cypher Authentication

The cypher api endpoints allow for authentication via an special headers or the standard *Authentication: bear access_token*. Instead of an access token, an execution lease token can be used to authenticate.
An execution lease will be issued by Morpheus for certain tasks, such as Ansible, which can then use the token to read cypher keys.

Cypher has the following headers and url parameters available for authentication:

Name | Type | Description
--------- | ----------- | -----------
X-Cypher-Token | HTTP Header | An access token or an execution lease token.
X-Vault-Token | HTTP Header | An access token or an execution lease token.
X-Morpheus-Lease | HTTP Header | An execution lease token.
leaseToken | URL Parameter | An execution lease token.



## List Cypher Keys

```shell
curl "https://api.gomorpheus.com/api/cypher/v1?list=true"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "auth": null,
  "data": {
    "keys": [
      "password/15/mypassword",
      "secret/foo"
    ]
  },
  "lease_duration": null,
  "lease_id": "",
  "renewable": false,
  "cypherItems": [
    {
      "itemKey": "password/15/mypassword",
      "leaseTimeout": 2764800000,
      "expireDate": "2019-03-23T10:17:52Z",
      "dateCreated": "2019-02-19T10:17:52Z",
      "lastUpdated": "2019-02-19T10:17:52Z",
      "lastAccessed": "2019-02-19T10:17:52Z"
    },
    {
      "itemKey": "secret/foo",
      "leaseTimeout": 2764800000,
      "expireDate": "2019-03-25T17:14:33Z",
      "dateCreated": "2019-02-21T17:14:33Z",
      "lastUpdated": "2019-02-21T17:14:33Z",
      "lastAccessed": "2019-02-21T17:14:33Z"
    }
  ],
  "meta": {
    "size": 2,
    "total": 2,
    "max": 25,
    "offset": 0
  }
}
```

This endpoint retrieves all cypher keys associated with the account, or user.

### HTTP Request

`GET https://api.gomorpheus.com/api/cypher/v1/:key?list=true`

### URL Parameters

Parameter | Description
--------- | -----------
key | If specified will match the start of the key.

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
list | Set to `true` for list behavior with HTTP `GET`.
phrase |  | If specified will match any part of key
key |  | If specified will return an exact match of key
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
sort | key | Sort order
direction | asc | Sort direction, use 'desc' to reverse sort

## Read a Cypher Key


```shell
curl "https://api.gomorpheus.com/api/cypher/v1/secret/foo" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "success": true,
  "auth": null,
  "data": {
    "foo":"bar",
    "briefing":"top secret info"
  },
  "lease_duration": 2764800000,
  "lease_id": "",
  "renewable": false,
  "cypher": {
    "itemKey": "secret/foo",
    "leaseTimeout": 2764800000,
    "expireDate": "2019-03-18T20:15:51Z",
    "dateCreated": "2019-02-14T20:15:51Z",
    "lastUpdated": "2019-02-14T20:15:51Z",
    "lastAccessed": "2019-02-14T20:15:51Z"
  }
}
```

This endpoint retrieves a specific cypher key.
The value of the key is decrypted and returned as `data`.
It may be a String or an object with many `{"key":"value"}` pairs.
The type depends on the cypher engine's capabilities and what type of data was written to the key.  For example the `secret/` engine allows either a string or an object, while the `password/` engine will always store and return a string.

The `leaseTimeout` and `ttl` parameters are only relevant if the cypher engine will be creating a key that does not exist. eg. `password/`

### HTTP Request

`GET https://api.gomorpheus.com/api/cypher/v1/:key`

### URL Parameters

Parameter | Description
--------- | -----------
key | The full cypher key including the mount prefix.

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
leaseTimeout | | The lease duration in milliseconds.
ttl | 32 days | Time to Live. The lease duration in seconds, or a human readable format eg. '15m', 8h, '7d'. This can be used instead of leaseTimeout.

## Read a Cypher with Lease


```shell
curl "https://api.gomorpheus.com/api/cypher/v1/password/15/mypassword"
  -H "X-Lease-Token: 6f4d3563-22ef-404f-8b81-c13d093cd55a"
```

> The above command returns JSON structured like reading a key with normal authentication:

```
{
  "auth": null,
  "data": "B[,t;ng[5[lg&th",
  "lease_duration": 432000000,
  "lease_id": "",
  "renewable": false,
  "cypher": {
    "itemKey": "password/15/mypassword",
    "leaseTimeout": 432000000,
    "expireDate": "2019-02-26T21:35:20Z",
    "dateCreated": "2019-02-21T21:35:20Z",
    "lastUpdated": "2019-02-21T21:35:20Z",
    "lastAccessed": "2019-02-21T21:35:20Z"
  }
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/cypher/v1/:key`

### HTTP Headers

See [Cypher Authentication](#cypher-authentication) for details on specifying a lease token.

### URL Parameters

Parameter | Default | Description
--------- | ------- | -----------
key | | The cypher key including the mount prefix.

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
leaseTimeout | | The lease duration in milliseconds.
ttl | 32 days | Time to Live. The lease duration in seconds, or a human readable format eg. '15m', 8h, '7d'. This can be used instead of leaseTimeout.

## Write a Cypher

```shell
curl -XPOST "https://api.gomorpheus.com/api/cypher/v1/secret/mymsg" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"msg":"hello world"}'
```

> The above command returns JSON structured like readding a cypher key:.

### HTTP Request

`POST https://api.gomorpheus.com/api/cypher/v1/:key`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
leaseTimeout | | The lease duration in milliseconds.
ttl | 32 days | Time to Live. The lease duration in seconds, or a human readable format eg. '15m', 8h, '7d'. This can be used instead of leaseTimeout.
value |  | The secret value to be stored. Only required for certain mountpoints.

### JSON Parameters

The following parameters are available under the root context of the JSON body.

Parameter | Default | Description
--------- | ------- | -----------
ttl      | 32 days | Time to Live in seconds, or a human readable format eg. '15m', 8h, '7d'

The `secret` engine is capable of storing the entire JSON object as key=value pairs, or just a single string. To pass a string, use the `value` query parameter instead of JSON.

The `ttl` payload key is a special key that if present will be parsed and used as the `ttl` parameter (lease duration in seconds).

#### Key

The *key* includes a *mount* prefix separated by a */*. For example, the key `secret/foo` uses the `secret` mount.

##### Available Mountpoints

Keys can have different behaviors depending on the specified mountpoint.

Mount | Description | Example
--------- | ------- | ---------
password | Generates a secure password of specified character length in the key pattern (or 15) with symbols, numbers, upper case, and lower case letters (i.e. password/15/mypass generates a 15 character password). | password/15/mypass
tfvars | This is a module to store a tfvars file for terraform. | tfvars/mytfvar
secret | This is the standard secret module that stores a key/value in encrypted form. Capable of storing entire JSON object or a String. | secret/mysecret
uuid | Returns a new UUID by key name when requested and stores the generated UUID by key name for a given lease timeout period. | uuid/autoMac1
key | Generates a Base 64 encoded AES Key of specified bit length in the key pattern (i.e. key/128/mykey generates a 128-bit key) | key/128/mykey

#### Lease Time

Quick MS Time Reference:

Time | MS
--------- | -------
Day      | 86400000
Week      | 604800000
Month (30 days)      |  2592000000
Year      | 31536000000

## Delete a Cypher

```shell
curl -XDELETE "https://api.gomorpheus.com/api/cypher/v1/secret/foo" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

Will delete a cypher from the system and make it no longer usable.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/cypher/v1/:key`

### URL Parameters

Parameter | Description
--------- | -----------
key | The full cypher key including the mount prefix.
