# Storage Buckets

Provides API interfaces for managing Storage Buckets (Object Stores and File Shares).

## Get All Storage Buckets

```shell
curl "https://api.gomorpheus.com/api/storage/buckets"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "storageBuckets": [
    {
      "id": 1,
      "name": "s3 test",
      "accountId": 1,
      "providerType": "s3",
      "config": {
        "accessKey": "G429AED2C4L5YZB7Q",
        "secretKey": "************",
        "endpoint": ""
      },
      "bucketName": "morpheus-s3-test",
      "readOnly": false,
      "defaultBackupTarget": false,
      "defaultDeploymentTarget": false,
      "defaultVirtualImageTarget": false,
      "copyToStore": true
    },
    {
      "id": 2,
      "name": "testdrive",
      "accountId": 1,
      "providerType": "local",
      "config": {
        "basePath": "/tmp/testdrive"
      },
      "bucketName": ".",
      "readOnly": false,
      "defaultBackupTarget": false,
      "defaultDeploymentTarget": false,
      "defaultVirtualImageTarget": false,
      "copyToStore": false
    }
  ],
  "meta": {
    "offset": 0,
    "max": 25,
    "size": 2,
    "total": 2
  }
}
```

This endpoint retrieves all storage buckets associated with the account.

### HTTP Request

`GET https://api.gomorpheus.com/api/storage/buckets`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name | null | If specified will return an exact match on name
phrase | null | If specified will return a partial match on name

## Get a Specific Storage Bucket


```shell
curl "https://api.gomorpheus.com/api/storage/buckets/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "storageBucket": {
    "id": 1,
    "name": "s3 test",
    "accountId": 1,
    "providerType": "s3",
    "config": {
      "accessKey": "G429AED2C4L5YZB7Q",
      "secretKey": "************",
      "endpoint": ""
    },
    "bucketName": "morpheus-s3-test",
    "readOnly": false,
    "defaultBackupTarget": false,
    "defaultDeploymentTarget": false,
    "defaultVirtualImageTarget": false,
    "copyToStore": true,
    "retentionPolicyType": null,
    "retentionPolicyDays": null,
    "retentionProvider": null
  }
}
```

This endpoint retrieves a specific storage bucket.


### HTTP Request

`GET https://api.gomorpheus.com/api/storage/buckets/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the storage bucket to retrieve

## Create a Storage Bucket

```shell
curl -XPOST "https://api.gomorpheus.com/api/storage/buckets" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "storageBucket": {
    "name": "test-storage",
    "providerType": "local",
    "config": {
      "basePath": "/tmp/test-storage"
    },
    "defaultBackupTarget": false,
    "copyToStore": true,
    "defaultDeploymentTarget": false,
    "defaultVirtualImageTarget": false,
    "retentionPolicyType": null,
    "retentionPolicyDays": null,
    "retentionProvider": null
  }
}'
```

> The above command returns JSON structured like getting a single storage bucket: 

### HTTP Request

`POST https://api.gomorpheus.com/api/storage/buckets`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A unique name scoped to your account for the storage bucket
providerType      | null | The type of storage bucket. [s3, azure, cifs, local, nfs, openstack, rackspace]
config      | null | A map of config values. The expected values vary by providerType.
bucketName      | null | The name of the bucket. Only applies to certain types eg. s3
createBucket | false | Create the bucket if it does not exist. Only applies to certain types eg. s3
defaultBackupTarget      | null | Default Backup Target
copyToStore      | null | Archive Snapshots
defaultDeploymentTarget      | null | Default Deployment Target
defaultVirtualImageTarget      | null | Default Virtual Image Store
retentionPolicyType      | null | Cleanup mode. backup - Move old files to a backup provider. delete - Delete old files. none (default) - Keep all files.
retentionPolicyDays      | null | The number of days old a file must be before it is deleted.
retentionProvider      | null | The backup Storage Bucket where old files are moved to.

### Amazon S3 (s3)

Parameter | Default | Description
--------- | ------- | -----------
config.accessKey | null | Access Key
config.secretKey | null | Secret Key
bucketName | null | Bucket Name
createBucket | false | Create the bucket if it does not exist
config.region | null | Optional Amazon region if creating a new bucket
config.endpoint | null | Optional endpoint URL if pointing to an object store other than amazon that mimics the Amazon S3 APIs.

### Azure (azure) Parameters

Parameter | Default | Description
--------- | ------- | -----------
config.storageAccount | null | Storage Account
config.storageKey | null | Storage Key
bucketName | null | Bucket Name
createBucket | false | Create the bucket if it does not exist

### CIFS (cifs) Parameters

Parameter | Default | Description
--------- | ------- | -----------
config.host | null | Host
config.username | null | Username
config.password | null | Password
bucketName | null | Bucket Name

### Local Storage (local) Parameters

Parameter | Default | Description
--------- | ------- | -----------
config.basePath | null | Storage Path

### NFSv3 (nfs) Parameters

Parameter | Default | Description
--------- | ------- | -----------
config.host | null | Host
config.exportFolder | null | Export Folder
bucketName | null | Bucket Name

### Openstack Swift (openstack) Parameters

Parameter | Default | Description
--------- | ------- | -----------
config.username | null | Username
config.apiKey | null | API Key
config.region | null | Region
bucketName | null | Bucket Name
createBucket | false | Create the bucket if it does not exist
config.identityUrl | null | Identity URL

### Rackspace CDN (rackspace) Parameters

Parameter | Default | Description
--------- | ------- | -----------
config.username | null | Username
config.apiKey | null | API Key
config.region | null | Region
bucketName | null | Bucket Name
createBucket | false | Create the bucket if it does not exist


## Update a Storage Bucket

```shell
curl -XPUT "https://api.gomorpheus.com/api/storage/buckets/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "storageBucket": {
    "name": "my-storage",
    "copyToStore": true
  }
}'
```

> The above command returns JSON structured like getting a single storage bucket: 

### HTTP Request

`PUT https://api.gomorpheus.com/api/storage/buckets/1`

### JSON Parameters

See [Create](#create-a-storage-bucket).

## Delete a Storage Bucket

```shell
curl -XDELETE "https://api.gomorpheus.com/api/storage/buckets/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

Will delete a storage bucket from the system and make it no longer usable.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/storage/buckets/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the storage bucket
