# Boot Scripts

Boot Scripts are used in the Image Builder service. See [Image Builds](#image-builds)

## Get All Boot Scripts

```shell
curl "https://api.gomorpheus.com/api/boot-scripts"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "bootScripts": [
    {
      "id": 1,
      "account": {
        "id": 1,
        "name": "root"
      },
      "fileName": "debian standard",
      "description": null,
      "content": "...",
      "createdBy": {
        "username": "admin"
      },
      "visibility": "private"
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

This endpoint retrieves all boot scripts associated with the account.

### HTTP Request

`GET https://api.gomorpheus.com/api/boot-scripts`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name |  | If specified will return an exact match on fileName
phrase |  | If specified will return a partial match on fileName

## Get a Specific Boot Script


```shell
curl "https://api.gomorpheus.com/api/boot-scripts/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "bootScript": {
    "id": 1,
    "account": {
      "id": 1,
      "name": "root"
    },
    "fileName": "debian standard",
    "description": null,
    "content": "...",
    "createdBy": {
      "username": "admin"
    },
    "visibility": "private"
  }
}
```

This endpoint retrieves a specific boot script.


### HTTP Request

`GET https://api.gomorpheus.com/api/boot-scripts/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the boot script to retrieve


## Create a Boot Script

```shell
curl -XPOST "https://api.gomorpheus.com/api/boot-scripts" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "bootScript": {
    "fileName": "debian standard",
    "content": "<esc><wait>install <wait> preseed/url=<%=preseedUrl%> <wait>debian-installer=en_US.UTF-8 <wait>auto <wait>locale=en_US.UTF-8 <wait>kbd-chooser/method=us <wait>keyboard-configuration/xkb-keymap=us <wait>netcfg/get_hostname=<%=container.hostname%> <wait>netcfg/get_domain=morpheusdata.com <wait>fb=false <wait>debconf/frontend=noninteractive <wait>console-setup/ask_detect=false <wait>console-keymaps-at/keymap=us <wait>grub-installer/bootdev=/dev/sda <wait><enter><wait>"
  }
}'
```

> The above command returns JSON structured like getting a single boot script: 

### HTTP Request

`POST https://api.gomorpheus.com/api/boot-scripts`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
fileName      |  | A name for the boot script
content      |  | The script content

## Update a Boot Script

```shell
curl -XPUT "https://api.gomorpheus.com/api/boot-scripts/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "bootScript": {
    "fileName": "debian default"
  }
}'
```

> The above command returns JSON structured like getting a single boot script: 

### HTTP Request

`PUT https://api.gomorpheus.com/api/boot-scripts/1`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the boot script

### JSON Parameters

Same as [Create](#create-a-boot-script).

## Delete a Boot Script

```shell
curl -XDELETE "https://api.gomorpheus.com/api/boot-scripts/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

Will delete a boot script from the system and make it no longer usable.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/boot-scripts/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the boot script

