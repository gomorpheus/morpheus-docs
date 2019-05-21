# Setup New Appliance

The Morpheus CLI can be used to setup a freshly installed Morpheus Appliance.

First, add your remote appliance with `remote add`

```bash
morpheus remote add myappliance https://myappliance.mysite.com --use
```
*Note that the `--use` option is not necessary if this is the first and only appliance in your CLI config*

Now, use the `remote setup` command to walk you through setting up your appliance.

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
