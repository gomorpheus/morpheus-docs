# Security Groups

A Security Group is a grouping of rules.  Each rule is a whitelist entry for a particular IP address to either a port range or a particular Morpheus instance type.  A Security Group may be applied to multiple Clouds, Apps, and Instances.

## Get All Security Groups

```shell
curl "https://api.gomorpheus.com/api/security-groups"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "success": true,
  "securityGroups": [
    {
      "id": 19,
      "accountId": 1,
      "name": "All Access to Tomcat",
      "description": ""
    },
    {
      "id": 18,
      "accountId": 1,
      "name": "Colorado office",
      "description": "All the Colorado office to access anywhere"
    }
  ],
  "securityGroupCount": 2
}
```

This endpoint retrieves all security groups and their JSON encoded configuration attributes.

### HTTP Request

`GET https://api.gomorpheus.com/api/security-groups`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
phrase | null | Name or description filter, restricts query to only load security groups which contain the phrase specified

## Get a Specific Security Group


```shell
curl "https://api.gomorpheus.com/api/security-groups/18" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "success": true,
  "securityGroup": {
    "id": 18,
    "accountId": 1,
    "name": "Colorado office",
    "description": "All the Colorado office to access anywhere"
  }
}
```

This endpoint retrieves a specific security group.

### HTTP Request

`GET https://api.gomorpheus.com/api/security-groups/:id`

## Create a Security Group

```shell
curl -XPOST "https://api.gomorpheus.com/api/security-groups" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "securityGroup": {
  "name": "My New Security Group",
  "description": "My Description"
  }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single security group 

### HTTP Request

`POST https://api.gomorpheus.com/api/security-groups`

### JSON Security Group Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | Name for your security group
description | null | Optional description field

## Updating a Security Group

```shell
curl -XPUT "https://api.gomorpheus.com/api/security-groups/18" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "securityGroup": {
  "name": "My New Security Group",
  "description": "My Description"
  }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single security group 

### HTTP Request

`PUT https://api.gomorpheus.com/api/security-groups/:id`

### JSON Security Group Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | Name for your security group
description | null | Optional description field

## Delete a Security Group

```shell
curl -XDELETE "https://api.gomorpheus.com/api/security-groups/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete a security group and update all clouds, apps, and instances which are currently using the security group.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/security-groups/:id`