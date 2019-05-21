# Cypher

Cypher at its core is a secure Key/Value store. But what makes cypher useful is the ability to securely store or generate credentials to connect to your instances. Not only are these credentials encrypted but by using a cypher you don't have to burn in connection credentials between instances into your apps.

Cypher keys can be revoked, either through lease timeouts or manually. So even if somebody were to gain access to your keys you could revoke access to the keys and generate new ones for your applications.

## Get All Cyphers

```shell
curl "https://api.gomorpheus.com/api/cypher"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "cyphers": [
    {
      "id": 4,
      "itemKey": "key/mykey",
      "leaseTimeout": 2764800000,
      "expireDate": "2018-10-20T15:35:05+0000",
      "dateCreated": "2018-09-18T15:35:05+0000",
      "lastUpdated": "2018-09-18T15:35:05+0000",
      "lastAccessed": "2018-09-18T15:35:05+0000"
    },
    {
      "id": 2,
      "itemKey": "secret/myClientId",
      "leaseTimeout": 2764800000,
      "expireDate": "2018-10-20T18:38:21+0000",
      "dateCreated": "2018-09-18T18:38:21+0000",
      "lastUpdated": "2018-09-18T18:38:21+0000",
      "lastAccessed": "2018-09-18T18:38:21+0000"
    },
    {
      "id": 3,
      "itemKey": "uuid/myid",
      "leaseTimeout": 2764800000,
      "expireDate": "2018-10-20T15:34:50+0000",
      "dateCreated": "2018-09-18T15:34:50+0000",
      "lastUpdated": "2018-09-18T15:34:50+0000",
      "lastAccessed": "2018-09-18T15:34:50+0000"
    }
  ],
  "meta": {
    "size": 3,
    "total": 3,
    "max": 25,
    "offset": 0
  }
}
```

This endpoint retrieves all cypher keys associated with the account, or user.

### HTTP Request

`GET https://api.gomorpheus.com/api/cypher`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name | null | If specified will return an exact match of key
phrase | null | If specified will match any part of key

## Get a Specific Cypher


```shell
curl "https://api.gomorpheus.com/api/cypher/2" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "cypher": {
    "id": 2,
    "itemKey": "secret/myClientId",
    "leaseTimeout": 2764800000,
    "expireDate": "2018-10-20T18:38:21+0000",
    "dateCreated": "2018-09-18T18:38:21+0000",
    "lastUpdated": "2018-09-18T18:38:21+0000",
    "lastAccessed": "2018-09-18T18:38:21+0000"
  }
}
```

This endpoint retrieves a specific cypher key.


### HTTP Request

`GET https://api.gomorpheus.com/api/cypher/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the cypher key

## Decrypt a Cypher


```shell
curl "https://api.gomorpheus.com/api/cypher/2/decrypt" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "cypher": {
    "id": 2,
    "itemKey": "secret/myClientId",
    "itemValue": "a secret value"
  },
  "success": true
}
```

This endpoint returns the decrypted value of the cypher key.  The last accessed timestamp is updated.

### HTTP Request

`GET https://api.gomorpheus.com/api/cypher/:id/decrypt`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the cypher

## Decrypt a Cypher with Lease


```shell
curl "https://api.gomorpheus.com/api/cypher/2/decrypt/lease/6f4d3563-22ef-404f-8b81-c13d093cd55a"
```

> The above command returns JSON structured like this:

```json
{
  "cypher": {
    "id": 2,
    "itemKey": "secret/myClientId",
    "itemValue": "a secret value"
  },
  "success": true
}
```

This endpoint returns the decrypted value of the cypher key.  The last accessed timestamp is updated.

This endpoint authenticates via the passed lease token instead of the normal authentication header.

### HTTP Request

`POST https://api.gomorpheus.com/api/cypher/:id/decrypt/lease/:lease`

### URL Parameters

Parameter | Description
--------- | -----------
id | The ID of the cypher
lease | Your execution lease token

## Create a Cypher

```shell
curl -XPOST "https://api.gomorpheus.com/api/cypher" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"cypher":{
    "itemKey": "secret/mysecret",
    "itemValue": "My Secret Value"
  }}'
```

> The above command returns JSON structured like getting a single cypher: 

### HTTP Request

`POST https://api.gomorpheus.com/api/cypher`

### JSON Parameters

The following parameters are available under the context **cypher**.

Parameter | Default | Description
--------- | ------- | -----------
itemKey      | null | A unique key in the format mount/key
itemValue | null | The value to be stored securely. Some types will generate their own value.
leaseTimeout | null | The Lease time in MS (default is 32 days)


#### Item Key

The *itemKey* contains two parts: the *mount* and the *key*, separated by a */*.

##### Available Mountpoints

Keys can have different behaviors depending on the specified mountpoint.

Mount | Description | Example
--------- | ------- | ---------
password | Generates a secure password of specified character length in the key pattern (or 15) with symbols, numbers, upper case, and lower case letters (i.e. password/15/mypass generates a 15 character password). | password/15/mypass
tfvars | This is a module to store a tfvars file for terraform. | tfvars/mytfvar
secret | This is the standard secret module that stores a key/value in encrypted form. | secret/mysecret
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
curl -XDELETE "https://api.gomorpheus.com/api/cypher/1" \
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

`DELETE https://api.gomorpheus.com/api/cypher/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the cypher key
