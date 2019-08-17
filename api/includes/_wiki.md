# Wiki

Morpheus provides a way to create and edit documentation in the form of wiki pages. Wiki pages use the **markdown** format and can be categorized to group them with other pages. Instances, apps, servers, clouds and groups can have their own wiki page associated to them.

## Get All Wiki Pages

```shell
curl "https://api.gomorpheus.com/api/wiki/pages"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "pages": [
    {
      "id": 1,
      "name": "Home",
      "urlName": "home",
      "category": null,
      "refId": null,
      "refType": null,
      "format": "markdown",
      "content": "Welcome to the home page for this morpheus appliance wiki.",
      "createdBy": {
        "id": 1,
        "username": "admin"
      },
      "updatedBy": {
        "id": 1,
        "username": "admin"
      },
      "dateCreated": "2019-06-27T16:55:59+0000",
      "lastUpdated": "2019-06-27T16:55:59+0000"
    },
    {
      "id": 2,
      "name": "README",
      "urlName": "info/readme",
      "category": "info",
      "refId": null,
      "refType": null,
      "format": "markdown",
      "content": "A readme file for this local dev appliance.\nNeat.",
      "createdBy": {
        "id": 1,
        "username": "admin"
      },
      "updatedBy": {
        "id": 1,
        "username": "admin"
      },
      "dateCreated": "2019-06-27T14:44:22+0000",
      "lastUpdated": "2019-06-27T14:44:22+0000"
    },
    {
      "id": 3,
      "name": "My Group",
      "urlName": "my-group",
      "category": "groups",
      "refId": 1,
      "refType": "ComputeSite",
      "format": "markdown",
      "content": "#My Group\nThis is a test group",
      "createdBy": {
        "id": 1,
        "username": "admin"
      },
      "updatedBy": {
        "id": 1,
        "username": "admin"
      },
      "dateCreated": "2019-06-28T01:41:45+0000",
      "lastUpdated": "2019-06-28T01:41:45+0000"
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

This endpoint retrieves wiki pages associated with the account.

### HTTP Request

`GET https://api.gomorpheus.com/api/wiki/pages`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name | null | If specified will return an exact match on name or urlName
phrase |  | If specified will return a partial match on name

## Get All Wiki Categories

```shell
curl "https://api.gomorpheus.com/api/wiki/categories"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "categories": [
    {
      "name": "apps",
      "pageCount": 1
    },
    {
      "name": "clouds",
      "pageCount": 1
    },
    {
      "name": "groups",
      "pageCount": 1
    },
    {
      "name": "info",
      "pageCount": 1
    },
    {
      "name": "instances",
      "pageCount": 2
    },
    {
      "name": "servers",
      "pageCount": 2
    }
  ]
}
```

This endpoint retrieves all categories associated with the account. The results are not paginated. The categories returned are those of the found pages.

### HTTP Request

`GET https://api.gomorpheus.com/api/wiki/categories`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
phrase |  | If specified will return a partial match on category name
pagePhrase |  | If specified will return a partial match on page name

## Get a Specific Wiki Page

```shell
curl "https://api.gomorpheus.com/api/wiki/pages/2" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json

{
  "page": {
      "id": 1,
      "name": "Home",
      "urlName": "home",
      "category": null,
      "refId": null,
      "refType": null,
      "format": "markdown",
      "content": "The home page for this wiki.",
      "createdBy": {
        "id": 1,
        "username": "admin"
      },
      "updatedBy": {
        "id": 1,
        "username": "admin"
      },
      "dateCreated": "2019-06-27T16:55:59+0000",
      "lastUpdated": "2019-06-27T16:55:59+0000"
    }
}
```

This endpoint retrieves a specific wiki page.


### HTTP Request

`GET https://api.gomorpheus.com/api/wiki/pages/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Wiki Page

## Create a Wiki Page

```shell
curl -XPOST "https://api.gomorpheus.com/api/wiki/pages" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"page":{
    "name": "Sample Doc",
    "category": "info",
    "content": "#Sample Doc\nA sample document in **markdown**."
  }}'
```

> The above command returns JSON structured like getting a single wiki page: 

### HTTP Request

`POST https://api.gomorpheus.com/api/wiki/pages`

### JSON Page Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to your account for the wiki page.
category | null | Optional category for grouping with other pages.
content | null | The content of the page (markdown).


## Update a Wiki Page

```shell
curl -XPUT "https://api.gomorpheus.com/api/wiki/pages/4" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"page":{
    "content": "#Sample Doc\nAn updated sample document in **markdown**.\nCheers!"
  }}'
```

> The above command returns JSON structured like getting a single wiki page

### HTTP Request

`PUT https://api.gomorpheus.com/api/wiki/pages/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Wiki Page

### JSON Page Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to your account for the wiki page.
category | null | Optional category for grouping with other pages.
content | null | The content of the page (markdown).

## Delete a Wiki Page

```shell
curl -XDELETE "https://api.gomorpheus.com/api/wiki/pages/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like getting a single wiki page

Will delete a Wiki Page from the system.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/wiki/pages/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Wiki Page

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

## Get a Wiki Page For Instance

```shell
curl "https://api.gomorpheus.com/api/instances/1/wiki" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like getting a single wiki page.

This endpoint retrieves the wiki page for an instance.
If its page does not yet exist, the response is still 200 OK with a body like *"page":null*.

### HTTP Request

`GET https://api.gomorpheus.com/api/instances/:id/wiki`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Instance

## Update a Wiki Page For Instance

```shell
curl -XPUT "https://api.gomorpheus.com/instances/1/wiki" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"page":{
    "content": "Lots of good information about this instance."
  }}'
```

> The above command returns JSON structured like getting a single wiki page: 

This endpoint updates the wiki page for an instance. 
The page will be created if it does not yet exist.

### HTTP Request

`PUT https://api.gomorpheus.com/api/instances/:id/wiki`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Instance

### JSON Page Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | (instance name) | A unique name scoped to your account for the wiki page.
content | null | The content of the page (markdown).



## Get a Wiki Page For App

```shell
curl "https://api.gomorpheus.com/api/apps/1/wiki" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like getting a single wiki page.

This endpoint retrieves the wiki page for an app.
If its page does not yet exist, the response is still 200 OK with a body like *"page":null*.

### HTTP Request

`GET https://api.gomorpheus.com/api/apps/:id/wiki`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the App

## Update a Wiki Page For App

```shell
curl -XPUT "https://api.gomorpheus.com/apps/1/wiki" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"page":{
    "content": "Lots of good information about this app."
  }}'
```

> The above command returns JSON structured like getting a single wiki page: 

This endpoint updates the wiki page for an app. 
The page will be created if it does not yet exist.

### HTTP Request

`PUT https://api.gomorpheus.com/api/apps/:id/wiki`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the App

### JSON Page Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | (app name) | A unique name scoped to your account for the wiki page.
content | null | The content of the page (markdown).



## Get a Wiki Page For Server

```shell
curl "https://api.gomorpheus.com/api/servers/1/wiki" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like getting a single wiki page.

This endpoint retrieves the wiki page for a server.
If its page does not yet exist, the response is still 200 OK with a body like *"page":null*.

### HTTP Request

`GET https://api.gomorpheus.com/api/servers/:id/wiki`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Server

## Update a Wiki Page For Server

```shell
curl -XPUT "https://api.gomorpheus.com/servers/1/wiki" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"page":{
    "content": "Lots of good information about this server."
  }}'
```

> The above command returns JSON structured like getting a single wiki page: 

This endpoint updates the wiki page for a server. 
The page will be created if it does not yet exist.

### HTTP Request

`PUT https://api.gomorpheus.com/api/servers/:id/wiki`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Server

### JSON Page Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | (server name) | A unique name scoped to your account for the wiki page.
content | null | The content of the page (markdown).



## Get a Wiki Page For Cloud

```shell
curl "https://api.gomorpheus.com/api/zones/1/wiki" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like getting a single wiki page.

This endpoint retrieves the wiki page for a cloud.
If its page does not yet exist, the response is still 200 OK with a body like *"page":null*.

### HTTP Request

`GET https://api.gomorpheus.com/api/zones/:id/wiki`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Cloud

## Update a Wiki Page For Cloud

```shell
curl -XPUT "https://api.gomorpheus.com/zones/1/wiki" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"page":{
    "content": "Lots of good information about this cloud."
  }}'
```

> The above command returns JSON structured like getting a single wiki page: 

This endpoint updates wiki page for a cloud. 
The page will be created if it does not yet exist.

### HTTP Request

`PUT https://api.gomorpheus.com/api/zones/:id/wiki`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Cloud

### JSON Page Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | (cloud name) | A unique name scoped to your account for the wiki page.
content | null | The content of the page (markdown).


## Get a Wiki Page For Group

```shell
curl "https://api.gomorpheus.com/api/groups/1/wiki" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like getting a single wiki page.

This endpoint retrieves the wiki page for a group.
If its page does not yet exist, the response is still 200 OK with a body like *"page":null*.

### HTTP Request

`GET https://api.gomorpheus.com/api/groups/:id/wiki`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Group

## Update a Wiki Page For Group

```shell
curl -XPUT "https://api.gomorpheus.com/groups/1/wiki" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"page":{
    "content": "Lots of good information about this group."
  }}'
```

> The above command returns JSON structured like getting a single wiki page: 

This endpoint updates the wiki page for a group. 
The page will be created if it does not yet exist.

### HTTP Request

`PUT https://api.gomorpheus.com/api/groups/:id/wiki`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the Group

### JSON Page Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | (group name) | A unique name scoped to your account for the wiki page.
content | null | The content of the page (markdown).
