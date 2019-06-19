# Security Group Rules

A Security Group Rule specifies that a certain CIDR is able to access a particular port (or port range) for a particular protocol.  Or, that a particular CIDR is able to access all instances of a particular type (like MySql, Redis, etc).  A Security Group Rule belongs to a Security Group and a Security Group is applied to either a Cloud, App, or Instance.

## Get All Security Group Rules for a Security Group

```shell
curl "https://api.gomorpheus.com/api/security-groups/19/rules"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "rules": [
    {
      "id": 29,
      "name": "my-sg port 5555",
      "ruleType": "customRule",
      "customRule": true,
      "instanceTypeId": null
      "direction": "ingress",
      "policy": "accept",
      "sourceType": "group",
      "source": null,
      "sourceGroup": {
        "id": 2239,
        "name": "my-sg"
      },
      "sourceTier": null,
      "portRange": "5555",
      "protocol": "tcp",
      "destinationType": "instance",
      "destination": null,
      "destinationGroup": null,
      "destinationTier": null,
      "externalId": null,
      "enabled": null,
      "syncSource": "external"
    },
    {
      "id": 30,
      "name": "my app ports",
      "ruleType": "customRule",
      "customRule": true,
      "instanceTypeId": null
      "direction": "ingress",
      "policy": "accept",
      "sourceType": "cidr",
      "source": "0.0.0.0/0",
      "sourceGroup": null,
      "sourceTier": null,
      "portRange": "5565-5570",
      "protocol": "tcp",
      "destinationType": "instance",
      "destination": null,
      "destinationGroup": null,
      "destinationTier": null,
      "externalId": null,
      "enabled": null,
    }
  ]
}
```

This endpoint retrieves all security group rules for a Security Gorup.

### HTTP Request

`GET https://api.gomorpheus.com/api/security-groups/:id/rules`

## Get a Specific Security Group Rule

```shell
curl "https://api.gomorpheus.com/api/security-groups/19/rules/30" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "success": true,
  "rule": {
      "id": 30,
      "name": "my app ports",
      "ruleType": "customRule",
      "customRule": true,
      "instanceTypeId": null
      "direction": "ingress",
      "policy": "accept",
      "sourceType": "cidr",
      "source": "0.0.0.0/0",
      "sourceGroup": null,
      "sourceTier": null,
      "portRange": "5565-5570",
      "protocol": "tcp",
      "destinationType": "instance",
      "destination": null,
      "destinationGroup": null,
      "destinationTier": null,
      "externalId": null,
      "enabled": null,
    }
}
```

This endpoint retrieves a specific security group rule.

### HTTP Request

`GET https://api.gomorpheus.com/api/security-groups/:id/rules/:id`

## Create a Security Group Rule

```shell
curl -XPOST "https://api.gomorpheus.com/api/security-groups/19/rules" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "rule": {
    "name": "port 55",
    "sourceType": "cidr",
    "source": "50.22.10.10/32",
    "portRange": "55",
    "protocol": "tcp",
    "destinationType": "instance",
    "customRule": true,
    "instanceTypeId": null
    }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single security group rule 

Will create a security group rule and update all clouds, apps, and instances which are currently using the security group in which this rule belongs.

### HTTP Request

`POST https://api.gomorpheus.com/api/security-groups/:id/rules`

### JSON Security Group Rule Parameters

Parameter | Default | Description
--------- | ------- | -----------
name      | null | A name for the rule
direction      | ingress | Either ingress or egress.
source      | null | CIDR representing the source IP(s) which should receive 
sourceType      | cidr | Either cidr, group, tier, all.
source      | null | CIDR representing the source IP(s) which should receive access. Required for sourceType=cidr.
sourceGroup.id      | null | The source Security Group ID. Required for sourceType=group. 
sourceTier.id      | null | The source Tier ID. Required for soureType=tier. 
portRange | null | Either a single value (i.e. 55) or a port range (i.e. 1-65535) for which to open access to the source.  Required if customRule is true, otherwise, ignored.
protocol | null | Either tcp, udp, icmp. Required if customRule is true, otherwise, ignored.
destinationType      | cidr | Either cidr, group, tier, instance.
destination      | null | CIDR representing the destination IP(s) which should receive access. Required for destinationType=cidr. 
destinationGroup.id      | null | The destination Security Group ID. Required for destinationType=group. 
destinationTier.id      | null | The destination Tier ID. Required for destinationType=tier. 
ruleType      | customRule | Either customRule or an instance type code.
policy      | accept | Either accept or deny.
instanceTypeId | null | The id of an Instance Type.  If specified, the source CIDR will have access to all ports exposed by the particular instance in the cloud, app, or instance.  Required if customRule is false, otherwise ignored. 

## Updating a Security Group Rule

```shell
curl -XPUT "https://api.gomorpheus.com/api/security-groups/19/rules/30" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{ "rule": {
    "portRange": "55-56"
    }}'
```

> The above command returns a similar JSON structure when submitting a GET request for a single security group rule

Will update a security group rule and update all clouds, apps, and instances which are currently using the security group in which this rule belongs.

### HTTP Request

`PUT https://api.gomorpheus.com/api/security-groups/:id/rules/:id`

### JSON Security Group Rule Parameters

Same parameters as specified in the creation of a Security Group Rule

## Delete a Security Group Rule

```shell
curl -XDELETE "https://api.gomorpheus.com/api/security-groups/19/rules/30" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structure like this:

```json
{
  "success": true
}
```

Will delete a security group rule and update all clouds, apps, and instances which are currently using the security group in which this rule belongs.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/security-groups/:id/rules/:id`