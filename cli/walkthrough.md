# Walkthrough

The CLI provides a ton of features provided with it that can make it very convenient for working with morpheus. There are several base commands with subcommands within for example.

### morpheus

Lets look at what happens when we simply type `morpheus` on the command line:

```
Usage: morpheus [command] [options]

Commands:
	access-token
	alias
	apps
	archives
	benchmark
	blueprints
	clouds
	containers
	cypher
	datastores
	deploy
	deployments
	edit-profile
	edit-rc
	environments
	execute-schedules
	execution-request
	file-copy-request
	groups
	hosts
	image-builder
	instance-types
	instances
	key-pairs
	library-file-templates
	library-instance-types
	library-layouts
	library-node-types
	library-option-lists
	library-option-types
	library-scripts
	library-upgrades
	license
	load-balancers
	login
	logout
	monitor-apps
	monitor-checks
	monitor-contacts
	monitor-groups
	monitor-incidents
	network-domains
	network-groups
	network-pool-servers
	network-pools
	network-proxies
	network-services
	networks
	passwd
	policies
	power-schedules
	process
	recent-activity
	remote
	reports
	resource-folders
	resource-pools
	roles
	security-groups
	shell
	storage-buckets
	tasks
	tenants
	user-groups
	user-settings
	user-sources
	users
	version
	virtual-images
	whoami
	workflows
Options:
    -e, --exec EXPRESSION            Execute the command(s) expression. This is an alternative to passing [command] [options]
        --noprofile                  Do not read and execute the personal initialization script .morpheus_profile
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -v, --version                    Print the version.
    -h, --help                       Print this help

```

As you can see the cli is split into sections. Each of. these sections has subcommands available for performing certain actions. For example lets look at `morpheus instances`

```
morpheus instances

Usage: morpheus instances [list,add,remove,stop,start,restart,backup,run-workflow,stop-service,start-service,restart-service,resize,upgrade,clone,envs,setenv,delenv] [name]

```

These commands typically make it easier to figure out what command subsets are available and the CLI documentation can provide helpful information in more depth on each command option.


### whoami

To confirm that we are hooked into the appliance properly lets check our authentication information:

```
$ morpheus whoami

Current User
==================

ID: 1
Account: Labs (Master Account)
First Name: Demo
Last Name: Environment
Username: david
Email: #################
Role: System Admin

Remote Appliance
==================

Name: demo
Url: https://demo.morpheusdata.com
Build Version: |version|
```

If this command fails please be sure to verify the appliance url entered previously is correct, and also verify the provided credentials are correctly entered.

## Provisioning

To get started provisioning instances from the CLI a few prerequisite commands must be setup in the CLI. First we must decide what `Group` we want to provision into.  We can first get a list of available groups to use by running `morpheus groups list`

```
morpheus> groups list

Morpheus Groups
==================


=  Automation - denver
=> Demo - Multi
=  Morpheus AWS - US-West
=  Morpheus Azure - US West
=  Morpheus Google - Auto
=  morpheus-approvals -
=  NIck-Demo - Chicago
=  San Mateo Hyper-V - San Mateo, CA
=  San Mateo Nutanix - San Mateo, CA
=  San Mateo Openstack - San Mateo, CA
=  San Mateo Servers - San Mateo, CA
=  San Mateo UCS - San Mateo, CA
=  San Mateo Vmware - San Mateo, CA
=  San Mateo Xen - San Mateo, CA
=  snow-approvals -
=  SoftLayer - Dallas-9
```

In the above example the currently active group is `Demo` as can be seen by the `=>` symbol to the left of the group name. To switch groups simply run:

```
morpheus groups use "San Mateo Xen"
```

This now becomes the active group we would like to provision into. Another thing to know before provisioning is we do have to also specify the cloud we want to provision into . This does require the cloud be in the group that is currently active. To see a list of clouds in the relevant group simpyl run:


```
morpheus clouds list -g [groupName]
```

This will scope the clouds command to list only clouds in the group specified.

Morpheus makes it very easy to get started provisioning via the CLI. It provides a list of instance-types that can be provisioned via the `instance-types list` command. Lets get started by provisioning an ubuntu virtual machine.

```
morpheus> instances add

Usage: morpheus instances add TYPE NAME
    -g, --group GROUP                Group
    -c, --cloud CLOUD                Cloud
    -O, --option OPTION              Option
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print json without making the actual request.
    -r, --remote REMOTE              Remote Appliance
    -U, --url REMOTE                 API Url
    -u, --username USERNAME          Username
    -p, --password PASSWORD          Password
    -T, --token ACCESS_TOKEN         Access Token
    -C, --nocolor                    ANSI
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Prints this help

```

```
morpheus> instances add ubuntu MyInstanceName -c "San Mateo Vmware"

morpheus> instances add ubuntu -c "San Mateo Vmware" dre-test
Layout ['?' for options]: ?
  * Layout [-O layout=] - Select which configuration of the instance type to be provisioned.

Options
===============
 * Docker Ubuntu Container [104]
 * VMware VM [105]
 * Existing Ubuntu [497]


Layout ['?' for options]: VMware VM
Plan ['?' for options]: ?
  * Plan [-O servicePlan=] - Choose the appropriately sized plan for this instance

Options
===============
 * Memory: 512MB Storage: 10GB [10]
 * Memory: 1GB Storage: 10GB [11]
 * Memory: 2GB Storage: 20GB [12]
 * Memory: 4GB Storage: 40GB [13]
 * Memory: 8GB Storage: 80GB [14]
 * Memory: 16GB Storage: 160GB [15]
 * Memory: 24GB Storage: 240GB [16]
 * Memory: 32GB Storage: 320GB [17]


Plan ['?' for options]: 10
Root Volume Label [root]:
Root Volume Size (GB) [10]:
Root Datastore ['?' for options]: ?
  * Root Datastore [-O rootVolume.datastoreId=] - Choose a datastore.

Options
===============
 * Auto - Cluster [autoCluster]
 * Auto - Datastore [auto]
 * cluster: labs-ds-cluster - 2.9TB Free [19]
 * store: ds-130-root - 178.5GB Free [5]
 * store: ds-130-vm - 699.0GB Free [6]
 * store: ds-131-root - 191.3GB Free [1]
 * store: ds-131-vm - 798.9GB Free [9]
 * store: ds-132-root - 191.2GB Free [4]
 * store: ds-132-vm - 799.4GB Free [10]
 * store: ds-177-root - 399.4GB Free [3]
 * store: labs-vm - 2.9TB Free [18]
 * store: VeeamBackup_WIN-0JNJSO32KI4 - 5.1GB Free [8]
 * store: VeeamBackup_WIN-QGARB6FA1GQ - 2.7GB Free [17]


Root Datastore ['?' for options]: Auto - Cluster
Add data volume? (yes/no): no
Network ['?' for options]: VM Network
Network Interface Type ['?' for options]: E1000
IP Address: Using DHCP
Add another network interface? (yes/no): no
Public Key (optional) ['?' for options]:
Resource Pool ['?' for options]: ?
  * Resource Pool [-O config.vmwareResourcePoolId=] -

Options
===============
 * Resources [resgroup-56]
 * Resources / Brian [resgroup-2301]
 * Resources / Brian / Macbook [resgroup-2302]
 * Resources / David [resgroup-2158]
 * Resources / David / Macbook [resgroup-2160]

Resource Pool ['?' for options]: resgroup-2160
```

As can be seen in the example above, the CLI nicely prompts the user for input on required options for provisioning this particular instance type within this particular cloud. It provides capabilities of adding multiple disks and multiple networks in this scenario. It is also posslbe to skip these prompts and provision everything via one command line syntax by using the `-O optionName=value` syntax:

```
morpheus> instances add ubuntu MyInstanceName -c "San Mateo Vmware"  -O layout=105 -O servicePlan=10 -O rootVolume.datastoreId=autoCluster
```

This will cause morpheus cli to skip prompting for input on these prompts. All inputs have an equivalent `-O` option that can be passed. To see what that option argument is simply enter `?` on the input prompt to get specifics.

Now your VM should be provisioning and status can be checked by simply typing `morpheus instances list`.

## List Arguments

Most of the `list` command types can be queried or paged via the cli. To do this simply look at the help information for the relevant list command

```
morpheus> instances list -h
Usage: morpheus [options]
    -g, --group GROUP                Group Name
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -r, --remote REMOTE              Remote Appliance
    -U, --url REMOTE                 API Url
    -u, --username USERNAME          Username
    -p, --password PASSWORD          Password
    -T, --token ACCESS_TOKEN         Access Token
    -C, --nocolor                    ANSI
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Prints this help
```




## Managing Instances

The CLI provides several convenience commands for managing your instances.

### Listing Instances

```bash
morpheus instances list

Morpheus Instances
==================

ID | NAME        | GROUP    | CLOUD           | TYPE  | ENVIRONMENT | NODES | CONNECTION                     | STATUS           
---|-------------|----------|-----------------|-------|-------------|-------|--------------------------------|------------------
73 | mysql500    | thegroup | bertramlabs-aws | MySQL |             | 1     | mysql500.cpkvktms2l92.us-ea... | RUNNING
```

Simply calling the list command will output a list of instances your account has access to. You can see it not only displays the name of the instance but also the instance type as well as running state (aka status).

### Working with a specific Instance

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
