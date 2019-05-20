# Instance Types

Provides a means to find out which instance types are available to your user account. These can vary in range from database containers, to web containers, to custom containers.
.
## Get All Instance Types

```shell
curl "https://api.gomorpheus.com/api/instance-types"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
{
  "instanceTypes": [
    {
      "id": 12,
      "name": "ActiveMQ",
      "code": "activemq",
      "category": "messaging",
      "active": true,
      "versions": [
        "5.11"
      ],
      "instanceTypeLayouts": [
        {
          "id": 14,
          "code": "activemq-5.11",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/}
        }
      ]
    },
    {
      "id": 13,
      "name": "Cassandra",
      "code": "cassandra",
      "category": "nosql",
      "active": true,
      "versions": [
        "2.1"
      ],
      "instanceTypeLayouts": [
        {
          "id": 15,
          "code": "cassandra-2.1-single",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 10,
      "name": "Confluence",
      "code": "confluence",
      "category": "utils",
      "active": true,
      "versions": [
        "5.7"
      ],
      "instanceTypeLayouts": [
        {
          "id": 12,
          "code": "confluence-5.7",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 5,
      "name": "Elastic Search",
      "code": "elasticsearch",
      "category": "nosql",
      "active": true,
      "versions": [
        "1.5"
      ],
      "instanceTypeLayouts": [
        {
          "id": 3,
          "code": "elasticsearch-1.5-single",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        },
        {
          "id": 4,
          "code": "elasticsearch-1.5-cluster",
          "name": "Cluster",
          "description": "This will provision two nodes, in multi master cluster",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 7,
      "name": "Jenkins",
      "code": "jenkins",
      "category": "utils",
      "active": true,
      "versions": [
        "1.596"
      ],
      "instanceTypeLayouts": [
        {
          "id": 8,
          "code": "jenkins-1.596",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 2,
      "name": "Memcached",
      "code": "memcached",
      "category": "cache",
      "active": true,
      "versions": [
        "1.4"
      ],
      "instanceTypeLayouts": [
        {
          "id": 11,
          "code": "memcached-1.4-single",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 4,
      "name": "Mongo",
      "code": "mongo",
      "category": "nosql",
      "active": true,
      "versions": [
        "3.0"
      ],
      "instanceTypeLayouts": [
        {
          "id": 16,
          "code": "mongo-3.0-rs",
          "name": "ReplicaSet",
          "description": "This will provision a 3 node replicaSet",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        },
        {
          "id": 6,
          "code": "mongo-3.0-single",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 3,
      "name": "MySQL",
      "code": "mysql",
      "category": "sql",
      "active": true,
      "versions": [
        "5.6"
      ],
      "instanceTypeLayouts": [
        {
          "id": 5,
          "code": "mysql-5.6-single",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 8,
      "name": "Nexus",
      "code": "nexus",
      "category": "utils",
      "active": true,
      "versions": [
        "2.11"
      ],
      "instanceTypeLayouts": [
        {
          "id": 9,
          "code": "nexus-2.11",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 14,
      "name": "Nginx",
      "code": "nginx",
      "category": "web",
      "active": true,
      "versions": [
        "1.9"
      ],
      "instanceTypeLayouts": [
        
      ]
    },
    {
      "id": 11,
      "name": "Postgres",
      "code": "postgres",
      "category": "sql",
      "active": true,
      "versions": [
        "9.4"
      ],
      "instanceTypeLayouts": [
        {
          "id": 13,
          "code": "postgres-9.4-single",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 9,
      "name": "RabbitMQ",
      "code": "rabbitmq",
      "category": "utils",
      "active": true,
      "versions": [
        "3.5"
      ],
      "instanceTypeLayouts": [
        {
          "id": 10,
          "code": "rabbitmq-3.5",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 1,
      "name": "Redis",
      "code": "redis",
      "category": "cache",
      "active": true,
      "versions": [
        "3.0"
      ],
      "instanceTypeLayouts": [
        {
          "id": 1,
          "code": "redis-3.0-single",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        },
        {
          "id": 2,
          "code": "redis-3.0-master-slave",
          "name": "Master\/Slave",
          "description": "This will provision 2 containers, one master and 1 slave.",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    },
    {
      "id": 6,
      "name": "Tomcat",
      "code": "tomcat",
      "category": "web",
      "active": true,
      "versions": [
        "7.0.62"
      ],
      "instanceTypeLayouts": [
        {
          "id": 7,
          "code": "tomcat-7.0.62-single",
          "name": "Single Process",
          "description": "This will provision a single process with no redundancy",
          "provisionType": { /* see provision types */ },
          "optionTypes": { /** see option types **/ }
        }
      ]
    }
  ]
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/instance-types`

## Get Specific Instance Type

```shell
curl "https://api.gomorpheus.com/api/instance-types/12"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
{
  "success": true,
  "instanceType": {
    "id": 12,
    "name": "ActiveMQ",
    "code": "activemq",
    "category": "messaging",
    "active": true,
    "versions": [
      "5.11"
    ],
    "instanceTypeLayouts": [
      {
        "id": 14,
        "code": "activemq-5.11",
        "name": "Single Process",
        "description": "This will provision a single process with no redundancy",
        "provisionType": { /* see provision types */ },
        "optionTypes": { /** see option types **/ }
      }
    ]
  }
}
```

### HTTP Request

`GET https://api.gomorpheus.com/api/instance-types/:id`
