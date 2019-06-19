# Whoami

Provides API to retrieve information about yourself, including your roles and permissions.

```shell
curl "https://api.gomorpheus.com/api/whoami" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "user": {
    "id": 1,
    "accountId": 1,
    "username": "admin",
    "displayName": "Admin",
    "email": "admin@morpheustestdata.com",
    "firstName": "Admin",
    "lastName": "",
    "dateCreated": "2016-08-28T03:28:09+0000",
    "lastUpdated": "2018-11-20T05:11:50+0000",
    "enabled": true,
    "accountExpired": false,
    "accountLocked": false,
    "passwordExpired": false,
    "roles": [
      {
        "id": 1,
        "authority": "System Admin",
        "description": "Super User"
      }
    ],
    "account": {
      "id": 1,
      "name": "root"
    }
  },
  "isMasterAccount": true,
  "permissions": {
    "ComputeSite": "full",
    "ComputeZone": "full",
    "InstanceType": "full",
    "account-usage": "full",
    "admin-accounts-users": "full",
    "admin-accounts": "full",
    "admin-appliance": "full",
    "admin-backupSettings": "full",
    "admin-certificates": "full",
    "admin-cm": "full",
    "admin-containers": "full",
    "admin-environments": "full",
    "admin-global-policies": "full",
    "admin-groups": "full",
    "admin-identity-sources": "full",
    "admin-keypairs": "full",
    "admin-licenses": "full",
    "admin-logSettings": "full",
    "admin-monitorSettings": "full",
    "admin-policies": "full",
    "admin-provisioningSettings": "full",
    "admin-roles": "full",
    "admin-servers": "full",
    "admin-servicePlans": "full",
    "admin-users": "full",
    "admin-utilities": "full",
    "admin-whitelabel": "full",
    "admin-zones": "full",
    "app-templates": "full",
    "apps": "full",
    "arm-template": "full",
    "automation-services": "full",
    "backup-services": "full",
    "backups": "full",
    "billing": "full",
    "cloudFormation-template": "full",
    "dashboard": "read",
    "deployment-services": "full",
    "deployments": "full",
    "guidance": "full",
    "infrastructure-boot": "full",
    "infrastructure-loadbalancer": "full",
    "infrastructure-networks": "full",
    "infrastructure-securityGroups": "full",
    "infrastructure-state": "full",
    "infrastructure-storage-browser": "full",
    "infrastructure-storage": "full",
    "logs": "full",
    "migrations": "full",
    "monitoring": "full",
    "operations-approvals": "full",
    "operations-health": "read",
    "provisioning-admin": "full",
    "provisioning-force-delete": "full",
    "provisioning": "full",
    "reports-analytics": "full",
    "reports": "full",
    "scheduling-execute": "full",
    "scheduling-power": "full",
    "services-archives": "full",
    "services-cypher": "full",
    "services-image-builder": "full",
    "services-kubernetes": "full",
    "services-network-registry": "full",
    "support-menu": "read",
    "task-scripts": "full",
    "tasks": "full",
    "terminal-access": "yes",
    "terminal": "full",
    "terraform-template": "full",
    "thresholds": "full",
    "trust-services": "full",
    "virtual-images": "full"
  },
  "appliance": {
    "buildVersion": "3.5.3"
  }
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/whoami`

This endpoint retrieves your user information, roles and permissions.  The appliance build version is also returned.
