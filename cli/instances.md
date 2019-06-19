# Managing Instances

The CLI provides several convenience commands for managing your instances. This subsection of the CLI is still being built out but some useful ones are already up and ready to go.


## Listing Instances

```bash
morpheus instances list

Morpheus Instances
==================

ID | NAME        | GROUP    | CLOUD           | TYPE  | ENVIRONMENT | NODES | CONNECTION                     | STATUS           
---|-------------|----------|-----------------|-------|-------------|-------|--------------------------------|------------------
73 | mysql500    | thegroup | bertramlabs-aws | MySQL |             | 1     | mysql500.cpkvktms2l92.us-ea... | RUNNING
```

Simply calling the list command will output a list of instances your account has access to. You can see it not only displays the name of the instance but also the instance type as well as running state (aka status).

## Working with a specific Instance

There are several commands pertaining to specific instances. For example it is very easy to stop,start, and restart a running instance. To do so you can execute one of the following commands:

```bash
morpheus instances stop "mysql500"
morpheus instances start "mysql500"
morpheus instances restart "mysql500"
```

You may pass the instance ID in place of NAME

```bash
morpheus instances restart 73
```

You may view the current usage statistics for an instance

```bash
morpheus instances stats 23

Instance Stats: testredis1 (Redis)
==================

Status: RUNNING

Memory:   [||                                                ]  2.42%       6.20 MiB / 256.00 MiB     
Storage:  [|||||||                                           ] 12.41%     254.08 MiB / 2.00 GiB       
CPU:      [|                                                 ]  0.12%
```


To get the output as JSON instead, use `--json`

```bash
morpheus instances stats "V1 - Redis" --json
```

This command outputs the following:

```json
{
  "instance": {
    "id": 23
  },
  "stats": {
    "usedStorage": 266423216,
    "maxStorage": 2147483648,
    "usedMemory": 6500352,
    "maxMemory": 268435456,
    "usedCpu": 0.1171646237
  }
}
```

### Environment Variables

The CLI provides several useful commands for managing the environment variables applied to the running instance. To list the known environment variables simply execute:

```bash
morpheus instances envs "Spud Marketing"
```

You can assign environment variables as well with the `setenv` command

```bash
morpheus instances setenv INSTANCE NAME VALUE [-e]
```

The `-e` argument allows you to mark an environment variable as exportable. Exportable means that if this instance were to be added to an App, all other instances in that app would automatic get this environment variable.

To delete an environment variable simply use the `delenv` command:

```bash
morpheus instances delenv INSTANCE NAME
```

**NOTE**: Containers must be restarted for new environment variables to be applied. Be sure to run a restart of the instance after you are done manipulating the environment.

## Creating Instances

The CLI makes it very easy to add new instances into the environment. There are still features being added here for container specific configuration but most of this is operational. The first step is to ensure an active Server group is selected within your cli. To do so simply execute

```bash
morpheus groups list
```

then select a group using:

```bash
morpheus groups use "My group name"
```

Now we are ready to create an instance. There are several different instance types available to choose from. We add a shorthand code to make it easy to  provision these without having to type the full formal name of the instance type. You can get a list of instance types from the catalog by executing:

```bash
morpheus instance-types list
```

This will list all items in the catalog as well as their known configuration options. The shorthand name will be in parenthesis.

Lets start by creating a node.js instance.

```bash
morpheus instances add "My Test Instance" node

Configurations:
  1) Single Node (node-4.0.0-single)
Selection: 1

Select a Plan:
  1) Memory: 128MB Storage: 1GB
  2) Memory: 256MB Storage: 3GB
  3) Memory: 512MB Storage: 5GB
  4) Memory: 1GB Storage: 10GB
  5) Memory: 2GB Storage: 20GB
  6) Memory: 4GB Storage: 40GB
  7) Memory: 8GB Storage: 80GB
  8) Memory: 16GB Storage: 160GB
Selection: 1

```

Thats it now we have created a new node js app. If you did mysql you would get prompted for some additional configuration information. We are actively working to make these selections all from the main command line as well and some of them are already.

You may also have the CLI prompt you for all the available options.

```bash
morpheus instances add
Cloud ['?' for options]: vcenter
Type ['?' for options]: Node
Instance Name: My Test Instance
Description (optional):

```

## Removing Instances

Removing morpheus instances is also fairly simple.

```bash
morpheus instances remove "My Test Instance"
```

**NOTE**: As of appliance version 2.1.9 a delete issue has been discovered with the CLI and API. We should have this resolved in the next release cycle `2.2.x`
