# Contacts

These entities define contacts to be notified of incidents.

## Get All Contacts

```shell
curl "https://api.gomorpheus.com/api/monitoring/contacts"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "contacts": [
    {
      "id": 1,
      "emailAddress": "admin@yourapp.com",
      "name": "Admin",
      "smsAddress": "555-555-5555",
      "slackHook": null
    }
  ],
  "meta": {
    "offset": 0,
    "max": "1",
    "size": 1,
    "total": 8
  }
}
```

This endpoint retrieves all contacts.

### HTTP Request

`GET https://api.gomorpheus.com/api/monitoring/contacts`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
name |  | If specified will return an exact match on name
phrase |  | If specified will return a partial match on name or email or sms

## Get a Specific Contact

```shell
curl "https://api.gomorpheus.com/api/monitoring/contacts/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "contact": {
    "id": 1,
    "emailAddress": "admin@yourapp.com",
    "name": "Admin",
    "smsAddress": "555-555-5555",
    "slackHook": null
  }
}
```

This endpoint retrieves a specific contact.

### HTTP Request

`GET https://api.gomorpheus.com/api/monitoring/contacts/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | ID of the contact

## Create a Contact

```shell
curl -XPOST "https://api.gomorpheus.com/api/monitoring/contacts" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"contact":{
    "name": "IT Admin",
    "emailAddress": "admin@yourapp.com",
    "smsAddress": "555-555-6789"
  }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single contact

### HTTP Request

`POST https://api.gomorpheus.com/api/monitoring/contacts`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | Unique name scoped to your account for the contact
emailAddress      |  | Email notification address
smsAddress      |  | SMS notification address
slackHook      |  | Slack Hook

## Updating a Contact

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/contacts/3" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"contact":{
    "name": "Jane Doe"
  }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single contact 

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/contacts/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | ID of the contact

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      |  | Unique name scoped to your account for the contact
emailAddress      |  | Email notification address
smsAddress      |  | SMS notification address
slackHook      |  | Slack Hook

## Delete a Contact

```shell
curl -XDELETE "https://api.gomorpheus.com/api/monitoring/contacts/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

### HTTP Request

`DELETE https://api.gomorpheus.com/api/monitoring/contacts/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | ID of the contact
