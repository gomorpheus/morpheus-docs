# Installation and Setup

The morpheus cli is a ruby based cli that can execute nearly every task that can be performed in the morpheus UI as well as additional capabilities not found in the ui. It is also a great way to get started in exploring the morpheus API and understanding some of the data model aspects.

The morpheus cli is capable of running on many platforms due to its ruby runtime. This includes linux and windows based platforms. The morpheus CLI is also available as a container in docker hub at https://hub.docker.com/r/morpheusdata/morpheus-cli

## Installation

### Linux

A Prerequisite to running the CLI is to have ruby 2.0.0+ installed (2.5 or greater recommended). Once the ruby runtime is installed simply use rubygems to install the cli `gem install morpheus-cli`. Once the gem is installed all cli commands can be run on the shell via `morpheus`.

Add this line to your application's Gemfile:

    gem 'morpheus-cli'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install morpheus-cli

To install a specific version of Morpheus CLI, pass in a -v option as shown in the example below:

    $ gem install morpheus-cli -v 3.6.38

### Windows

To get started, we must first ensure ruby is running on the windows machine in question. To do this please visit [http://rubyinstaller.org/downloads](http://rubyinstaller.org/downloads) and download at least Ruby version 2.0.0 (2.3.3 recommended).

**NOTE:** When installing ruby on windows, make sure the options are selected for adding the ruby binaries to your `PATH`.

Now that ruby is installed, simply open a `PowerShell` window and run

```
gem install morpheus-cli --no-ri --no-rdoc
```

A list of installed dependencies should start sliding by the screen. Once this has completed the CLI setup is complete. Now all that must be done is configuring the cli to point to an appliance for use.

```
morpheus remote add myapp https://applianceUrl
morpheus remote use myapp
morpheus login
```

Credentials are used to acquire an access token which is then stored in the users home directory in a folder called `.morpheus`. Now all commands provided by the CLI are available for use just as if running in a *nix based environment*.

### Docker

The morpheus cli is available as a container at https://hub.docker.com/r/morpheusdata/morpheus-cli

Docker Pull Command

```
docker pull morpheusdata/morpheus-cli
```

*Note use tags for specific versions as latest tag may not be the most recent release*

The CLI looks for a user directory to store remote appliance credentials which may need mounted into the container for persistence between runs. Within the container the cli will look for ~/.morpheus

To get started using the interactive morpheus cli shell simply run:

```
docker run -ti morpheus-cli shell
```

All available commands can be run.

## Configuration

Morpheus reads and writes several configuration files within the $MORPHEUS_CLI_HOME directory.

**Note:** These files are maintained by the program. It is not recommended for you to manipulate them.

### appliances file

The `appliances` YAML file contains a list of known appliances, keyed by name.

Example:
```yaml
:qa:
  :host: https://qa.mycoolsite.com
  :active: true
:production:
  :host: https://morpheus.mycoolsite.com
  :active: false
```

### credentials file

The `.morpheus/credentials` YAML file contains access tokens for each known appliance.

### groups file

The `.morpheus/groups` YAML file contains the active group information for each known appliance.


## Startup scripts

When Morpheus starts, it executes the commands in a couple of dot files.

These scripts are written in morpheus commands, not bash, so they can only execute morpheus commands and aliases.

### .morpheus_profile file

It looks for `$MORPHEUS_CLI_HOME/.morpheus_profile`, and reads and executes it (if it exists).

This may be inhibited by using the `--noprofile` option.

### .morpheusrc file

When started as an interactive shell with the `morpheus shell` command,
Morpheus reads and executes `$MORPHEUS_CLI_HOME/.morpheusrc` (if it exists). This may be inhibited by using the `--norc` option.

An example startup script might look like this:

```
# .morpheusrc

# aliases
alias our-instances='instances list -c "Our Cloud"'

# switch to our appliance that we created with `remote add morphapp1`
remote use morphapp1

# greeting
echo "Welcome back human,  have fun!"

# print current user information
whoami

# print the list of instances in our cloud
our-instances

```

### Environment Variables

Morpheus has only one environment variable that it uses, **MORPHEUS_CLI_HOME**

The **MORPHEUS_CLI_HOME** variable is where morpheus CLI stores its configuration files.
This can be set to allow a single system user to maintain many different configurations
If the directory does not exist, morpheus will attempt to create it.

The default home directory is **$HOME/.morpheus**

To see how this works, run the following:

```shell
MORPHEUS_CLI_HOME=~/.morpheus_test morpheus shell
```

Now, in your new morpheus shell, you can see that it is a fresh environment.
There are no remote appliances configured.

```shell
morpheus> remote list

Morpheus Appliances
===================

You have no appliances configured. See the `remote add` command.

```

You can use this to create isolated environments (sandboxes), within which to execute your morpheus commands.

```shell
export MORPHEUS_CLI_HOME=~/morpheus_test
morpheus remote add myremote https://testmorpheusappliance.mycompany.com --insecure
morpheus instances list
```

Morpheus saves the remote appliance information, including api access tokens,
to the $MORPHEUS_HOME_DIRECTORY. These files are saved with file permissions **6000**.
So, only one system user should be allowed to execute morpheus with that home directory.
See [Configuration](#Configuration) for more information on the files morpheus reads and writes.


## Setup Appliance

The first thing that needs to be done after installing the cli is pointing the cli to the appliance. The CLI can be pointed at many appliances and uses the RESTful OAUTH public developer apis to perform tasks. To set this up simply add a remote appliance with the `morpheus remote add` command

```
morpheus remote add myappliance https://applianceUrl
morpheus remote use myappliance
morpheus login
```

*Note that the `--use` option is not necessary if this is the first and only appliance in your CLI config*

There are several commands available when dealing with configuration of remote appliances. To see what commands are available just type `morpheus remote`.

### remote setup

The `remote setup` command walks you through setting up your appliance.

```bash
morpheus remote setup
```

This will prompt you for all the settings required to initialize the appliance, and then log you as the new master System Admin user.

```bash
Morpheus Appliance Setup
==================

It looks like you're the first one here.
Let's initialize your remote appliance at https://myappliance.mysite.com

Create Master account
==================

Master Account Name: root

Create Master User
==================

First Name (optional):
Last Name (optional):
Username: james
Email: james@morpheusdata.com
Password:
Confirm Password:

Initial Setup
==================

Appliance Name: myappliance
Appliance URL [http://10.0.2.2:8080/]: https://myappliance.mysite.com
Enable Backups (yes/no) [no]:
Enable Monitoring (yes/no) [yes]:
Enable Logs (yes/no) [yes]:
Initializing the appliance...

You have successfully setup the appliance.
You are now logged in as the System Admin james.

Would you like to apply your License Key now? (yes/no) [yes]:    
License Key: <your key>

Do you want to create the first group now? (yes/no) [yes]:
Name: g1
Code (optional):
Location (optional):
Added group g1

Morpheus Groups
==================

   | ID | NAME | LOCATION | CLOUDS | HOSTS
---|----|------|----------|--------|------
=> | 1  | g1   |          | 0      | 0    

Viewing 1-1 of 1

# => Currently using g1

Do you want to create the first cloud now? (yes/no) [yes]:
Cloud Type ['?' for options]: Morpheus
Name: c1
Code (optional):
Location (optional):
Visibility (optional) [private] ['?' for options]:


Cloud Details
==================

ID: 1
Name: c1
Type: Morpheus
Code: standard
Location:
Visibility: Private
Groups: g1
Status: OK

Cloud Servers (0)
==================

 Container Hosts: 0    Hypervisors: 0      Bare Metal: 0    Virtual Machines: 0     Unmanaged: 0    

```

That's it, your appliance is ready for use now, and you've already created your first Group and Cloud.

This command can only be done once.

```bash
morpheus remote setup
Appliance has already been setup
```
