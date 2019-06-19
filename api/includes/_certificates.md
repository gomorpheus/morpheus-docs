# SSL Certificates

Morpheus provides a database for keeping track of SSL Certificates in the system. These can be applied to various load balancers within the system and instances that use them.

## Get All SSL Certificates

```shell
curl "https://api.gomorpheus.com/api/certificates"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "certificateCount": 1,
  "certificates": [
    {
      "accountId": 1,
      "certFile": "certFileContent",
      "domainName": "test.local",
      "generated": false,
      "id": 1,
      "keyFile": "keyFileContent",
      "name": "Test Cert",
      "wildcard": true
    }
  ]
}
```

This endpoint retrieves all key pairs associated with the account.

### HTTP Request

`GET https://api.gomorpheus.com/api/certificates`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
lastUpdated | null | A date filter, restricts query to only load certificates updated more recent or equal to the date specified
name | null | If specified will return an exact match certificate


<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>

## Get a Specific Certificate


```shell
curl "https://api.gomorpheus.com/api/certificates/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "certificate": {
    "accountId": 1,
    "certFile": "certFileContent",
    "domainName": "test.local",
    "generated": false,
    "id": 1,
    "keyFile": "keyFileContent",
    "name": "Test Cert",
    "wildcard": true
  },
  "succcess": true
}
```

This endpoint retrieves a specific key.


### HTTP Request

`GET https://api.gomorpheus.com/api/certificates/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the key pair to retrieve

## Create a Certificate

```shell
curl -XPOST "https://api.gomorpheus.com/api/certificates" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"certificate":{
    "name": "My Cert",
    "certFile": "my cert file contents",
    "keyFile": "My keyfile",
    "domainName": "Domain name of cert",
    "wildcard": false
  }}'
```

> The above command returns JSON structured like getting a single certificate: 

### HTTP Request

`POST https://api.gomorpheus.com/api/certificates`

### JSON Check Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to your account for the key
certFile | null | The contents of the certificate file
keyFile | null | The contents of the key file
wildcard | false | Wether or not this certificate is a wildcard cert
domainName | null | The domain name this certificate is tied to

## Updating a Certificate

```shell
curl -XPUT "https://api.gomorpheus.com/api/certificates/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"certificate":{
    "name": "My Cert",
    "certFile": "my cert file contents",
    "keyFile": "My keyfile",
    "domainName": "Domain name of cert",
    "wildcard": false
  }}'
```

> The above command returns JSON structured like getting a single certificate: 

### HTTP Request

`PUT https://api.gomorpheus.com/api/certificates/:id`

### JSON Check Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to your account for the key
certFile | null | The contents of the certificate file
keyFile | null | The contents of the key file
wildcard | false | Wether or not this certificate is a wildcard cert
domainName | null | The domain name this certificate is tied to

## Delete a Certificate

```shell
curl -XDELETE "https://api.gomorpheus.com/api/certificates/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

Will delete a certificate from the system and make it no longer usable.

<aside class="warning">
If a certificate is actively in use, a delete will fail.
</aside>

### HTTP Request

`DELETE https://api.gomorpheus.com/api/certificates/:id`


