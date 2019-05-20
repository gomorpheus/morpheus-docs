# App Templates

Provides a list of all available app templates that can be used for creating an application as well as an ability to define custom app templates.


## Get All App Templates

```shell
curl "https://api.gomorpheus.com/api/app-types"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
{
  "appTypes": [
    {
      "id": 3,
      "name": "Tomcat - Mysql",
      "code": "tomcatmysql",
      "instanceTypes": []
    },
    appTypeCount: 1
  ]
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/app-types`

## Get Specific App Template

```shell
curl "https://api.gomorpheus.com/api/app-types/1"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
{
  "success": true,
  "appType": {
    "id": 1,
    "name": "Tomcat - Mysql",
    "code": "tomcatmysql",
    "instanceTypes": []
  }
}
```
### HTTP Request

`GET https://api.gomorpheus.com/api/app-types/:id`

