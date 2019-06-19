# Monitor Checks

 These entities define what and when a check is executed within the Morpheus system. Morpheus supports a vast array of different check types (not solely web checks). The API provides a means to list all of an account's checks in addition to create, modify, mute, and or delete them.

## Get All Checks

```shell
curl "https://api.gomorpheus.com/api/monitoring/checks"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "checks": [
    {
      "id": 798,
      "account": {
        "id": 1
      },
      "active": true,
      "availability": 99.9804109,
      "checkAgent": null,
      "checkIntegrations": [
        
      ],
      "checkInterval": 300,
      "checkSpec": null,
      "checkType": {
        "id": 1
      },
      "config": {  "webMethod": "GET",  "webUrl": "http://google.com"},
      "createIncident": true,
      "dateCreated": "2015-05-16T12:05:23Z",
      "deleted": false,
      "description": null,
      "health": 10,
      "history": "{\"checkDates\":[1433339580607,1433339595119,1433339613169,1433339625412,1433339641010,1433339655209,1433339670178,1433339687802,1433339700471,1433339715171,1433339730710,1433339745351,1433339764299,1433339775508,1433339790377,1433339805373,1433339820944,1433339835996,1433339850317,1433339865833,1433339880884,1433339895489,1433339910554,1433339925660,1433339940875,1433339956143,1433339970551,1433339985179,1433340000961,1433340015765],\"successList\":[true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true],\"healthList\":[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],\"timerList\":[347,410,338,337,365,361,373,374,358,337,350,505,342,338,358,359,381,354,353,377,342,344,349,363,329,352,350,348,356,345]}",
      "inUptime": true,
      "lastBoxStats": null,
      "lastCheckStatus": "success",
      "lastError": "http error: Read timed out",
      "lastErrorDate": "2015-05-18T09:25:15Z",
      "lastMessage": "http 200",
      "lastMetric": "200",
      "lastRunDate": "2015-06-03T14:00:16Z",
      "lastStats": null,
      "lastSuccessDate": "2015-06-03T14:00:16Z",
      "lastTimer": 345,
      "lastUpdated": "2015-06-03T14:00:16Z",
      "lastWarningDate": null,
      "name": "Purity Plus",
      "nextRunDate": "2015-06-03T14:00:16Z",
      "severity": "critical",
      "startDate": null
    }
  ]
}
```

This endpoint retrieves all checks and their JSON encoded configuration attributes based on check type. Check data is encrypted in the database.

### HTTP Request

`GET https://api.gomorpheus.com/api/monitoring/checks`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
max | 25 | Max number of results to return
offset | 0 | Offset of records you want to load
lastUpdated | null | Date filter, restricts query to only load checks updated  timestamp is more recent or equal to the date specified
deleted | undefined | Used to specify you can load previously deleted checks. Useful for synchronizing deleted records in your client side store.


<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>

## Get a Specific Check


```shell
curl "https://api.gomorpheus.com/api/monitoring/checks/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "success": true,
  "check:" {
    "id": 798,
    "account": {
      "id": 1
    },
    "active": true,
    "availability": 99.9804109,
    "checkAgent": null,
    "checkIntegrations": [
      
    ],
    "checkInterval": 300,
    "checkSpec": null,
    "checkType": {
      "id": 1
    },
    "config": {"webMethod": "GET", "webUrl": "http://google.com"},
    "createIncident": true,
    "dateCreated": "2015-05-16T12:05:23Z",
    "deleted": false,
    "description": null,
    "health": 10,
    "history": "{\"checkDates\":[1433339580607,1433339595119,1433339613169,1433339625412,1433339641010,1433339655209,1433339670178,1433339687802,1433339700471,1433339715171,1433339730710,1433339745351,1433339764299,1433339775508,1433339790377,1433339805373,1433339820944,1433339835996,1433339850317,1433339865833,1433339880884,1433339895489,1433339910554,1433339925660,1433339940875,1433339956143,1433339970551,1433339985179,1433340000961,1433340015765],\"successList\":[true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true],\"healthList\":[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],\"timerList\":[347,410,338,337,365,361,373,374,358,337,350,505,342,338,358,359,381,354,353,377,342,344,349,363,329,352,350,348,356,345]}",
    "inUptime": true,
    "lastBoxStats": null,
    "lastCheckStatus": "success",
    "lastError": "http error: Read timed out",
    "lastErrorDate": "2015-05-18T09:25:15Z",
    "lastMessage": "http 200",
    "lastMetric": "200",
    "lastRunDate": "2015-06-03T14:00:16Z",
    "lastStats": null,
    "lastSuccessDate": "2015-06-03T14:00:16Z",
    "lastTimer": 345,
    "lastUpdated": "2015-06-03T14:00:16Z",
    "lastWarningDate": null,
    "name": "Purity Plus",
    "nextRunDate": "2015-06-03T14:00:16Z",
    "severity": "critical",
  }
}
```

This endpoint retrieves a specific check.


### HTTP Request

`GET https://api.gomorpheus.com/api/monitoring/checks/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | ID of the check to retrieve

## Create a Check

```shell
curl -XPOST "https://api.gomorpheus.com/api/monitoring/checks" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"check":{
    "name": "My Check",
    "checkType": {"code": "webGetCheck"},
    "inUptime": true,
    "severity": "critical",
    "description": null,
    "checkInterval": 300,
    "checkAgent": null,
    "active": true,
    "config": {
      "webMethod": "GET",
      "webUrl": "http://google.com"
    }
  }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single check 

### HTTP Request

`POST https://api.gomorpheus.com/api/monitoring/checks`

### JSON Check Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | Unique name scoped to your account for the check
description | null | Optional description field
checkType | null | Check type you want to create, use code and a valid check type: `{"code": "webGetCheck"}`
checkInterval | 300 | Number of seconds you want between check executions (minimum value is 60, depending on your subscription plan)
inUptime  | true | Used to determine if check should affect account wide availability calculations
active    | true | Used to determine if check should be scheduled to execute
severity  | critical | Severity level of incidents that are created when this check fails. They can be `info`, `warning`, or `critical`
checkAgent | null | Specifies agent you want to run the check with i.e. `{"id": 1}` See Agents for more information
config | null | JSON encoded list of parameters that varies by check type. See below for more information

## Updating a Check

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/checks/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"check":{
    "name": "My Check",
    "checkType": {"code": "webGetCheck"},
    "inUptime": true,
    "severity": "critical",
    "description": null,
    "checkInterval": 300,
    "checkAgent": null,
    "active": true,
    "config": {
      "webMethod": "GET",
      "webUrl": "http://google.com"
    }
  }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single check 

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/checks/:id`

### JSON Check Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | Unique name scoped to your account for the check
description | null | Optional description field
checkType | null | Check type you want to create, use code and a valid check type: `{"code": "webGetCheck"}`
checkInterval | 300 | Number of seconds you want between check executions (minimum value is 60, depending on your subscription plan)
inUptime  | true | Used to determine if check should affect account wide availability calculations
active    | true | Used to determine if check should be scheduled to execute
severity  | critical | Severity level of incidents that are created when this check fails. They can be `info`, `warning`, or `critical`
checkAgent | null | Specifies agent you want to run the check with i.e. `{"id": 1}` See Agents for more information
config | null | JSON encoded list of parameters that varies by check type. See below for more information

## Check Types and Options

We support a wide variety of check types. Each check type varies in its configuration payload when determining how the check should be run.


> Creates a Web type Check

### Web Get Check

```json
{
  "check": {
    "name": "My Web Check",
    "checkType": {"code": "webGetCheck"},
    "config": {"webMethod":"GET","webUrl": "http://google.com", "checkUser":"basicUser","checkPassword":"basicPassword", "webTextMatch": "Login", "textCheckOn": "on"}
  }
}
```

Code: `webGetCheck`

Web check type allows you to perform a standard web request and validate the response came back successfully. Additionally, you can check for matching text within the result. There are several `config` parameters available for use with this type of check

Parameter | Requirement | Description
--------- | ----------- | -----------
webMethod | Yes         | HTTP method to use for testing (GET or POST)
webUrl    | Yes         | Web URL you wish to use to run a check on
checkUser | No          | If you want to use HTTP Basic Authentication, populate this field with the username
checkPassword | No      | If you want to use HTTP basic Authentication, populate this field with the password
textCheckOn   | No      | Set value to "on" if you want to turn on text matching
webTextMatch  | No      | Set the string you want to look for in the page source

### MySQL Check

```json
{
  "check": {
    "name": "MySql Check",
    "checkType": {"code": "mysqlCheck"},
    "config": {"dbHost":"db.example.org","dbPort": "3306", "dbUser":"basicUser","dbPassword":"basicPassword", "dbName": "mydb", "dbQuery": "select 1", "checkOperator": "lt", "checkResult": 2}
  }
}
```

Code: `mysqlCheck`

MySQL check allows you to execute a query so that you may validate the value returned in addition to verifying the database is responding. This can be useful for doing a slow query check or just making sure something isn't growing out of control.

Parameter | Requirement | Description
--------- | ----------- | -----------
dbHost    | Yes         | Hostname or IP address of the MySQL database
dbPort    | Yes         | MySQL Port (defaults to 3306)
dbUser    | Yes         | Database username
dbPassword | Yes        | Database password, (all check data is encrypted inside the Morpheus database)
dbName    | Yes         | Database name you would like to connect to
checkOperator  | No     | Can be set to `lt` (less than), `gt` (greater than), `equal` (Equal to) for comparison
checkResult | No        | Numerical value to compare the check result against

<aside class="notice">Direct access over the Internet to your database is not required.  SSH tunneling is available to protect the communication, which is configured using additional JSON parameters (see SSH checks). Also, you can run our agent, with the correct subscription plan, where the check is executed from a host behind your firewall.</aside>

### SQL Server Check

```json
{
  "check": {
    "name": "SQL Server Check",
    "checkType": {"code": "sqlCheck"},
    "config": {"dbHost":"db.example.org","dbPort": "3306", "dbUser":"basicUser","dbPassword":"basicPassword", "dbName": "mydb", "dbQuery": "select 1", "checkOperator": "lt", "checkResult": 2}
  }
}
```

Code: `sqlCheck`

SQL Server check allows to execute a query so that you may validate the value returned in addition to verifying the database is responding. This can be useful for doing a slow query check or just making sure something isn't growing out of control.

Parameter | Requirement | Description
--------- | ----------- | -----------
dbHost    | Yes         | Hostname or IP address of the SQL database
dbPort    | Yes         | SQL Port (defaults to 1433)
dbUser    | Yes         | Database username
dbPassword | Yes        | Database password, (all check data is encrypted inside the Morpheus database)
dbName    | Yes         | Database name you would like to connect to
checkOperator  | No     | Can be set to `lt` (less than), `gt` (greater than), `equal` (Equal to) for comparison
checkResult | No        | Numerical value to compare the check result against

<aside class="notice">Direct access over the Internet to your database is not required.  SSH tunneling is available to protect the communication, which is configured using additional JSON parameters (see SSH checks). Also, you can run our agent, with the correct subscription plan, where the check is executed from a host behind your firewall.</aside>

### PostgreSQL Check

```json
{
  "check": {
    "name": "PostgerSQL Check",
    "checkType": {"code": "postgresCheck"},
    "config": {"dbHost":"db.example.org","dbPort": "3306", "dbUser":"basicUser","dbPassword":"basicPassword", "dbName": "mydb", "dbQuery": "select 1", "checkOperator": "lt", "checkResult": 2}
  }
}
```

Code: `postgresCheck`

PostgreSQL check allows to execute a query so that you may validate the value returned in addition to verifying the database is responding. This can be useful for doing a slow query check or just making sure something isn't growing out of control.

Parameter | Requirement | Description
--------- | ----------- | -----------
dbHost    | Yes         | Hostname or IP address of the PostgreSQL database
dbPort    | Yes         | SQL Port (defaults to 5432)
dbUser    | Yes         | Database username
dbPassword | Yes        | Database password, (all check data is encrypted inside the Morpheus database)
dbName    | Yes         | Database name you would like to connect to
checkOperator  | No     | Can be set to `lt` (less than), `gt` (greater than), `equal` (Equal to) for comparison
checkResult | No        | Numerical value to compare the check result against

<aside class="notice">Direct access over the Internet to your database is not required.  SSH tunneling is available to protect the communication, which is configured using additional JSON parameters (see SSH checks). Also, you can run our agent, with the correct subscription plan, where the check is executed from a host behind your firewall.</aside>


### Socket Check

```json
{
  "check": {
    "name": "Socket Check",
    "checkType": {"code": "socketCheck"},
    "config": {"host":"test.example.org","port": "3306", "send":"blah","responseMatch":"OK"}
  }
}
```

Code: `socketCheck`

Socket check confirms a certain TCP port is up and responding in your environment. It can be configured do an initial send upon connect and compare and expected response of the service.

Parameter | Requirement | Description
--------- | ----------- | -----------
host      | Yes         | Hostname or IP address of the socket server
port      | Yes         | TCP port
send      | No          | Connection string you might want to send to the service
responseMatch | No      | Response from the service to match against

### Elastic Search Check

```json
{
  "check": {
    "name": "Socket Check",
    "checkType": {"code": "elasticSearchCheck"},
    "config": {"esHost":"test.example.org","esPort": "9200"}
  }
}
```

Code: `elasticSearchCheck`

Elasticsearch check is capable of connecting to your Elasticsearch, cluster or node, verifying its health. In addition, Morpheus will also pull statistical information such as: document size, capacity, and cpu usage.

Parameter | Requirement | Description
--------- | ----------- | -----------
esHost      | Yes         | Hostname or IP address of the Elasticsearch server
esPort      | Yes         | Port to connect to the HTTP service 

<aside class="notice">Direct access over the Internet to Elasticsearch is not required.  SSH tunneling is available to protect the communication, which is configured using additional JSON parameters (see SSH checks). Also, you can run our agent, with the correct subscription plan, where the check is executed from a host behind your firewall.</aside>

### Push Check

```json
{
  "check": {
    "name": "Push Check",
    "checkType": {"code": "pushCheck"}
  }
}
```

Code: `pushCheck`

A Push check is a check that is updated by a web hook. An external source is responsible for periodically submitting a check status. Please see the section on Push Checks API for details.

## SSH Tunneling

SSH tunneling options allow the different check types to tunnel to a host via a proxy, and execute checks relative to the proxy. A SSH tunnel can use your account generated public and private key-pairs or SSH password (we **strongly** recommend using a key-pair).

To enable SSH tunneling for a check, add the following parameters to any check type config as seen earlier in the Check Types section.

```json
{
  "check": {
    "name": "Socket Check",
    "checkType": {"code": "elasticSearchCheck"},
    "config": {"esHost":"test.example.org","esPort": "9200", "tunnelOn": "on", "sshHost": "example.org", "sshPort": 22, "sshUser": "happyapps"}
  }
}
```

Parameter | Requirement | Description
--------- | ----------- | -----------
tunnelOn  | Yes         | Set to `on` to turn on tunneling
sshHost   | Yes         | Hostname or IP address of the proxy host
sshPort   | No          | Port for SSH on the proxy host, defaults to 22
sshUser   | Yes         | SSH user on the proxy host to login as
sshPassword | No        | Password for user, if not using key based authentication

<aside class="notice">**Note on Security** All check data including key-pairs are encrypted in Morpheus using a RSA 2048 bit key. In the event you believe your private key is compromised or uncomfortable with the auto-generated key-pair, you can always re-create a new key-pair in account settings. An alternative to using tunneling is an agent, which provides behind-the-firewall access to your services.</aside>

## Mute a Check

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/checks/1/mute" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"enabled":true}'
```

> The above command returns JSON structure like this:

```json
{
  "muteState": "QUARANTINED",
  "success": true
}
```

This endpoint can be used to toggle the mute state of a check on and off.

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/checks/:id/mute`

### JSON Parameters

Parameter | Default | Description
--------- | ----------- | -----------
enabled | true | Set to false to unmute


## Mute All Checks

```shell
curl -XPUT "https://api.gomorpheus.com/api/monitoring/checks/mute-all" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{"enabled":true}'
```

> The above command returns JSON structure like this:

```json
{
  "muteState": "QUARANTINED",
  "updated": 20,
  "success": true
}
```

This endpoint can be used to toggle the mute state on and off for all checks.

### HTTP Request

`PUT https://api.gomorpheus.com/api/monitoring/checks/mute-all`

### JSON Parameters

Parameter | Default | Description
--------- | ----------- | -----------
enabled | true | Set to false to unmute

## Delete a Check

```shell
curl -XDELETE "https://api.gomorpheus.com/api/monitoring/checks/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

A deleted check can be fetched from the API using the GET method to synchronize client side views, but can not be executed or updated.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/monitoring/checks/:id`

