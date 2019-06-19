# Archives

Archives provides a way to store your files and make them available for download by your Scripts and Users.

Archives are organized by buckets. Each bucket has a unique name that is used to identify it in URLs and Scripts.

## Get All Archive Buckets

```shell
curl "https://api.gomorpheus.com/api/archives/buckets" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "archiveBuckets": [
   
    {
      "id": 1,
      "name": "testbucket",
      "description": "a test archive with local storage",
      "storageProvider": {
        "id": 2,
        "name": "testdrive2"
      },
      "owner": {
        "id": 1,
        "name": "root"
      },
      "createdBy": null,
      "isPublic": true,
      "visibility": "private",
      "code": "454ed1af504f",
      "filePath": "morpheus-archives/454ed1af504f/",
      "rawSize": 65154,
      "fileCount": 16,
      "accounts": [

      ],
      "dateCreated": "2017-06-14T14:09:01Z",
      "lastUpdated": "2017-06-14T14:09:01Z"
    },
    {
      "id": 2,
      "name": "s3bucket",
      "description": "an test archive using s3",
      "storageProvider": {
        "id": 3,
        "name": "morph-test-bucket"
      },
      "owner": {
        "id": 1,
        "name": "root"
      },
      "createdBy": null,
      "isPublic": false,
      "visibility": "private",
      "code": "4fdcad04901b",
      "filePath": "morpheus-archives/4fdcad04901b/",
      "rawSize": 70389,
      "fileCount": 18,
      "accounts": [

      ],
      "dateCreated": "2017-06-14T16:31:19Z",
      "lastUpdated": "2017-06-14T16:31:19Z"
    }
  ],
  "meta": {
    "size": 2,
    "total": 2,
    "offset": 0,
    "max": 50
  }
}
```

This endpoint retrieves all archive buckets associated with the account.

### HTTP Request

`GET https://api.gomorpheus.com/api/archives/buckets`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name |  | If specified will return an exact match on name
phrase |  | If specified will return a partial match on name

## Get a Specific Archive Bucket


```shell
curl "https://api.gomorpheus.com/api/archives/buckets/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "archiveBucket": {
    "id": 1,
    "name": "mybucket",
    "description": "a test bucket with local storage",
    "storageProvider": {
      "id": 10,
      "name": "testdrive3"
    },
    "owner": {
      "id": 1,
      "name": "root"
    },
    "createdBy": null,
    "isPublic": false,
    "visibility": "private",
    "code": "9dab5b3f4ada",
    "filePath": "morpheus-archives/9dab5b3f4ada/",
    "rawSize": 73909,
    "fileCount": 15,
    "accounts": [

    ],
    "dateCreated": "2018-07-20T04:07:09Z",
    "lastUpdated": "2018-07-26T19:38:17Z",
    "isOwner": true
  }
}
```

This endpoint retrieves a specific archive bucket.

### HTTP Request

`GET https://api.gomorpheus.com/api/archives/buckets/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the archive bucket to retrieve

## Create an Archive Bucket

```shell
curl -XPOST "https://api.gomorpheus.com/api/archives/buckets" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "archiveBucket": {
    "name": "mybucket",
    "description": "my archive bucket",
    "storageProvider": {
      "id": 2
    },
    "visibility": "private",
    "isPublic": false
  }
}'
```

> The above command returns JSON structured like getting a single archive bucket: 

### HTTP Request

`POST https://api.gomorpheus.com/api/archives/buckets`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | A name for the archive bucket.  Must be globally unique.
description      |  | A description for the archive bucket
storageProvider      |  | Storage Provider
isPublic      | false | Public URL - Set to true to allow anonymous access
visibility      | private | Visibility - Set to public to allow all tenants 
accounts      |  | Tenants - Grant read only access to certain tenants

## Update an Archive Bucket

```shell
curl -XPUT "https://api.gomorpheus.com/api/archives/buckets/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "archiveBucket": {
    "description": "our secure file store",
    "isPublic": false
  }
}'
```

> The above command returns JSON structured like getting a single archive bucket.


### HTTP Request

`PUT https://api.gomorpheus.com/api/archives/buckets/1`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the archive bucket

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | A name for the archive bucket.  Must be globally unique
description      |  | A description for the archive bucket
isPublic      | false | Public URL - Set to true to allow anonymous access
visibility      | private | Visibility - Set to public to allow all tenants access.
accounts      |  | Tenants - Grant read only access to certain tenants

## Delete an Archive Bucket

```shell
curl -XDELETE "https://api.gomorpheus.com/api/archives/buckets/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

Will delete an archive bucket from the system and make it no longer usable.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/archives/buckets/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the archive bucket



## Get All Archive Files

```shell
curl "https://api.gomorpheus.com/api/archives/buckets/mybucket/files/"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "parentDirectory": null,
  "archiveFiles": [
    {
      "id": 951,
      "name": "myapp",
      "filePath": "myapp",
      "archiveBucket": {
        "id": 38,
        "name": "mybucket",
        "isPublic": false
      },
      "createdBy": {
        "username": "admin"
      },
      "isDirectory": true,
      "status": "Active",
      "rawSize": 26719,
      "contentType": null,
      "dateCreated": "2018-07-26T19:38:17Z",
      "lastUpdated": "2018-07-26T19:38:17Z"
    },
    {
      "id": 933,
      "name": "readme.txt",
      "filePath": "readme.txt",
      "archiveBucket": {
        "id": 38,
        "name": "mybucket",
        "isPublic": false
      },
      "createdBy": {
        "username": "admin"
      },
      "isDirectory": false,
      "status": "Active",
      "rawSize": 47104,
      "contentType": "text/plain",
      "dateCreated": "2018-07-20T04:07:33Z",
      "lastUpdated": "2018-07-20T04:07:33Z"
    }
  ],
  "archiveBucket": {
    "id": 38,
    "name": "mybucket",
    "description": "a test bucket with local storage",
    "storageProvider": {
      "id": 10,
      "name": "testdrive3"
    },
    "owner": {
      "id": 1,
      "name": "root"
    },
    "createdBy": null,
    "isPublic": false,
    "visibility": "private",
    "code": "9dab5b3f4ada",
    "filePath": "morpheus-archives/9dab5b3f4ada/",
    "rawSize": 73823,
    "fileCount": 3,
    "accounts": [

    ],
    "dateCreated": "2018-07-20T04:07:09Z",
    "lastUpdated": "2018-07-26T19:38:17Z"
  },
  "isOwner": true,
  "meta": {
    "size": 2,
    "total": 2,
    "offset": 0,
    "max": 50
  }
}
```

This endpoint retrieves all files in an archive bucket under the specified `filePath`. 

### HTTP Request

`GET https://api.gomorpheus.com/api/archives/buckets/:bucket/files/:filePath`

### URL Parameters

Parameter | Description
--------- | -----------
bucket | The Name or ID of the archive bucket
filePath | The directory to search under. The root directory **/** is the default.

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name |  | If specified will return an exact match on name
phrase |  | If specified will return a partial match on filePath
fullTree | false | Include files under sub directories too. This is always true when searching with phrase.



```shell
curl "https://api.gomorpheus.com/api/archives/files/954"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "archiveFile": {
    "id": 954,
    "name": "articles_controller.rb",
    "filePath": "future/app/controllers/agents_controller.rb",
    "archiveBucket": {
      "id": 38,
      "name": "b10",
      "isPublic": false
    },
    "createdBy": {
      "username": "tom"
    },
    "isDirectory": false,
    "status": "Active",
    "rawSize": 8534,
    "contentType": "application/octet-stream",
    "downloadCount": 0,
    "dateCreated": "2017-07-26T19:38:17Z",
    "lastUpdated": "2017-07-27T02:03:49Z"
  },
  "isOwner": true
}
```

Get details about a specific archive file.

### HTTP Request

`GET https://api.gomorpheus.com/api/archives/files/:fileId`

### URL Parameters

Parameter | Description
--------- | -----------
fileId | The ID of the archive file

## Upload Archive File

```shell
curl -XPOST "https://api.gomorpheus.com/api/archives/buckets/mybucket/files/myapp/config/?filename=application.rb" \
  -H "Authorization: BEARER access_token" \
  --data-binary '@/path/to/file'
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Upload a file to the specified archive bucket and file path.

<aside class="notice">This will overwrite the file if it already exists.</aside>

### HTTP Request

`POST https://api.gomorpheus.com/api/archives/buckets/:bucket/files/:filePath`

### URL Parameters

Parameter | Description
--------- | -----------
bucket | The Name or ID of the archive bucket
filePath | The directory for the file being uploaded. The root directory **/** is the default.

### Query Parameters

Parameter | Description
--------- | -----------
filename | Specify a filename for archive file. The base filename of the uploaded file is the default.

## Download an Archive File

```shell
curl -XGET "https://api.gomorpheus.com/api/archives/download/mybucket/myapp/config/application.rb" \
  -H "Authorization: BEARER access_token"
```

> The above command returns the contents of the specified file as an attachment with Content-Type dicated by the file

Download the file as an authorized user with access to the bucket.

<aside class="info">Downloading a directory will return a .zip file containing all files under it.</aside>

### HTTP Request

`GET https://api.gomorpheus.com/api/archives/download/:bucket/:filePath`

### URL Parameters

Parameter | Description
--------- | -----------
bucket | The Name or ID of the archive bucket
filePath | The full path of the file being downloaded

## Download a Public Archive File

```shell
curl -XGET "https://api.gomorpheus.com/public-archives/download/mybucket/pubdemo/GREETINGS.md"
```

> The above command returns the contents of the file as an attachment with Content-Type dicated by the file

Files in an archive bucket that has **Public URL** enabled can be downloaded via this endpoint without any authentication, anonymously.

### HTTP Request

`GET https://api.gomorpheus.com/public-archives/download/:bucket/:filePath`

### URL Parameters

Parameter | Description
--------- | -----------
bucket | The Name or ID of the archive bucket
filePath | The full path of the file being downloaded


## Delete Archive File

```shell
curl -XDELETE "https://api.gomorpheus.com/api/archives/files/99" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Permanently delete a file or directory. 

<aside class="warning">Deleting a directory will also delete all the files under it.</aside>

### HTTP Request

`DELETE https://api.gomorpheus.com/api/archives/files/:fileId`

### URL Parameters

Parameter | Description
--------- | -----------
fileId | The ID of the archive file



## Get Archive File Links

### HTTP Request

```shell
curl "https://api.gomorpheus.com/api/archives/files/1/links"
  -H "Authorization: BEARER access_token"
```

```json
{
  "archiveFileLinks": [
    {
      "id": 2,
      "secretAccessKey": "6e37727235041746",
      "archiveFile": {
        "id": 1,
        "name": "config.ini",
        "filePath": "config.ini"
      },
      "createdBy": {
        "username": "admin"
      },
      "dateCreated": "2018-09-20T21:15:38Z",
      "lastUpdated": "2018-09-20T21:15:38Z",
      "lastAccessDate": null,
      "expirationDate": null,
      "downloadCount": 0
    },
    {
      "id": 1,
      "secretAccessKey": "6562129e9e546b9",
      "archiveFile": {
        "id": 1,
        "name": "config.ini",
        "filePath": "config.ini"
      },
      "createdBy": {
        "username": "admin"
      },
      "dateCreated": "2018-09-20T21:06:04Z",
      "lastUpdated": "2018-09-20T21:09:26Z",
      "lastAccessDate": null,
      "expirationDate": "2018-09-20T21:26:04Z",
      "downloadCount": 1
    }
  ],
  "meta": {
    "size": 2,
    "total": 2,
    "offset": 0,
    "max": 50
  }
}
```

This endpoint retrieves the links that have been created for the specified file.

### HTTP Request

`GET https://api.gomorpheus.com/api/archives/files/:fileId/links`

### URL Parameters

Parameter | Description
--------- | -----------
fileId | The ID of the archive file

## Create an Archive File Link

```shell
curl -XPOST "https://api.gomorpheus.com/api/archives/files/:fileId/links" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
```

> The above command returns JSON structured like this: 

```json
{
  "success": true,
  "secretAccessKey": "45a214fce9a546b9"
}
```

This returns a secret token that can be used to download the file via a public url, without any other authentication or authorization.  File links can be set to expire after a certain amount of time.

See [Download an Archive File Link](#download-an-archive-file-link)

### HTTP Request

`POST https://api.gomorpheus.com/api/archives/files/:fileId/links`

### URL Parameters

Parameter | Description
--------- | -----------
fileId | The ID of the archive file

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
expireSeconds      | 0 | Time to live in seconds. 0 means do not expire.


## Delete an Archive File Link

```shell
curl -XDELETE "https://api.gomorpheus.com/api/archives/files/1/links/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
```

> The above command returns JSON structured like this: 

```json
{
  "success": true
}
```

This will delete the link from the system, so it can no longer be used.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/archives/files/:fileId/links/:linkId`

### URL Parameters

Parameter | Description
--------- | -----------
fileId | The ID of the archive file
linkId | The ID of the archive file link


## Download an Archive File Link

```shell
curl -XGET "https://api.gomorpheus.com/public-archives/link?s=45a214fce9a546b9"
```

> The above command returns the contents of the file as an attachment with Content-Type dicated by the file

Download an archive file lin

### HTTP Request

`POST https://api.gomorpheus.com/public-archives/link?s=:secretAccessToken`

### URL Parameters

Parameter | Description
--------- | -----------
s | The secret access token for the archive file being downloaded. See [Create An Archive File Link](#create-an-archive-file-link)
