---
title: Morpheus Developer APIs

language_tabs:
  - shell

includes:
  - apps
  - blueprints
  - instances
  - instancetypes
  - provisioning
  - provision_types
  - option_types
  - deploys
  - checks
  - monitor_incidents
  - check_types
  - groups
  - zones
  - zonetypes
  - zone_datastores
  - storage_buckets
  - servers
  - server_types
  - virtual_images
  - certificates
  - keypairs
  - accounts
  - account_groups
  - user_sources
  - users
  - roles
  - policies
  - power_schedules
  - execute_schedules
  - errors
  - security_groups
  - security_group_rules
  - tasks
  - task_types
  - workflows
  - billing
  - cypher
  - archives
  - image_builds
  - boot_scripts
  - preseed_scripts
  - setup
  - whoami
  - user_settings
  - execution_request
  - processes

search: true
---

# Introduction

Welcome to the Morpheus API Documentation. Morpheus is a powerful provisioning service complete with monitoring, logging, backups, and application deployment strategies.

We currently provide an OAUTH 2.0 based authentication model and are working on language specific libraries for ruby and a few others.

<aside class="notice">
Replace the <code>morpheus-appliance-url</code> in the examples with your custom Morpheus appliance URL.
</aside>

The current version is **3.6.2**

# Authentication

The Morpheus API follows the OAuth 2.0 Specification and acts as an OAUTH 2.0 provider. To authorize your account you will need to use the same credentials you normally use to login to morpheus which will provide you with an `accessToken` as well as a `refreshToken`.

> To authorize, use this code:

```shell
# With shell, you can just pass the correct header with each request
curl -X POST --data "username=meow&password=meow" "https://morpheus-appliance-url/oauth/token?grant_type=password&scope=write&client_id=morph-customer"

#Returns:
{
  "access_token": "d0cc2cc4-f7f5-4713-a874-34491e7707de",
  "expires_in": 31535996,
  "refresh_token": "cda88865-f88d-4ed9-a621-424d9361beb2",
  "scope": "write",
  "token_type": "bearer"
}
```

> Make sure to replace `morpheus-appliance-url` with your appliance url and `meow` with your username and password.

Morpheus expects all api requests to use the resultant `access_token` from the request made during authentication. This can be passed via the `Authorization` header. Be sure to replace the `access_token` with the actual token received from the OAuth request.

`Authorization: BEARER access_token`

<aside class="notice">
You must replace <code>access_token</code> with your generated Access Token.
</aside>
