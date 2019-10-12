# Changelog

This is a list of changes in the most recent versions of the CLI.

Backwards compatibility with older appliances should be preserved in most cases.

## 4.1.0

### Enhancements
* New command `clusters`
* New command `networks list-subnets|get-subnet|etc` for managing network subnets.
* New option `user-settings --user-id` for managing other users tokens,etc.
* Updated `roles add` and `roles update` to support the `--payload` option.
* New command `networks list-subnets|get-subnet|etc` for managing network subnets.
* New subcommand `containers logs`

### Fixes
* Fix issue with `library-option-lists update`  not allowing arbitrary `-O` options.
* Fix error seen with `library-node-type remove`.

## 4.0.0.1

### Fixes
* Fix issue with `instances history-event` breaking when an event had an error to display.

## 4.0.0

### Enhancements
* New command `wiki`
* New subcommands `network-pools list-ips|get-ip|etc` for managing network pool IPs
* New subcommands `network-domains list-records|get-record|etc` for managing network network domain records.
* Changed `--refresh` default interval to 30 seconds, instead of 5.

## 3.6.38

### Fixes
* Fix issue with `virtual-images add` to send imageType 'vmdk' instead of 'vmware'.
* Fix issue with `monitor-apps get` and `monitor-groups get` displaying Open Incidents as json

## 3.6.37

### Fixes
* Fix issue with `instances suspend` passing `server=true`

## 3.6.36

### Fixes
* Fix issue with `instances start-service`

## 3.6.35

### Fixes
* Fix issue with download/export commands that use arrays as query parameter values

## 3.6.34

### Fixes
* Hide new `wiki` command until 4.0

## 3.6.33

### Fixes
* Fixed issue with `instances add -O instanceContext` option not being included in payload
* Fixed issue with `access refresh-token`

## 3.6.32

### Enhancements
* New command `reports`
* New command `instances view`
* New option `instances add --environment`
* New option `networks list -c [cloud]`
* Improved `instances clone` prompting
* New command `environments`
* New command `wiki`

### Fixes
* Fixed issue with `instances scaling`
* Fixed issue with `recent-activity` data parameters
* Fix issue with `library-node-types update` specifying atleast one option error with -O
* Fixed issue with `remote list` name column not being wide enough.
* Fixed `tenants` commands missing support for `--dry-run`, etc
* Fixed issue with `library-container-types add` needing `-O containerType.config={}`

### Deprecations
* Deprecated `instances firewall-enable and firewall-disable` which have been recently deprecated in the api.

## 3.6.31

### Fixes
* Fixed error seen with `instances resize` again

## 3.6.30

### Fixes
* Fixed error seen with `instances resize`

## 3.6.29

### Enhancements
* New command `resource-pools`
* New command `resource-folders`
* Updates to command `security-groups` for rule and location management.

### Fixes
* Fixed issue with `instances add`  requiring Resource Pool when there are none available.

### Deprecations
* Deprecated `security-group-rules`, replaced by `security-groups get|add-rule|remove-rule`


## 3.6.28

### Enhancements
* Updated `networks add` to have options for Network Domain and Proxy settings.

## 3.6.27

### Fixes
* Fixed issue with `library-node-types add` error generating 'Sorry, no options were found for provision type' for some types.

## 3.6.26

### Fixes
* Fixed issue with `apps add --blueprint` prompting for values that are already set in the config.
* Fixed issue with `apps add --blueprint -N` erroring with message about 'rootVolume.storageType' being required.
* Fixed issue with `apps add -N` erroring with message about 'Version' being required.

## 3.6.24

### Fixes
* Fixed issue with `curl --insecure` option having the typo 'inescure'.
* Fixed issue with `--curl` option output, copy + paste + enter not working, due to trailing ansi reset character.

## 3.6.23

### Fixes
* Fixed issue with `instances add` for Nutanix clouds not prompting for Datastore for volumes.
* Fixed issue with `instances add --layout` causing HTTP 500 error

## 3.6.22

### Enhancements
* Updated `alias` to allow [command] to be an expression.
* New option `morpheus -e` to execute an expression. This works just like `morpheus shell -e`.
* New option `benchmark exec -n` to run many iterations and print the average duration.

### Fixes
* Fixed issue with some commands exiting 0 when an error occurs.
* Fixed issue with `apps add` where JSON errors were not rendered nicely.
* Fixed issue with `hosts get ID` making a redundant api request.

## 3.6.21

### Enhancements
* New command `apps count`
* Added options to `instances count` and `hosts count`
* New command `hosts types` to list all server types via API.  *Required appliance version 3.6.2*

### Deprecations
* Removed command `hosts server-types [cloud]`. This has been replaced with `hosts types -c [cloud]`.

### Fixes
* Fixed issue with `apps list` having an extra newline in the output.

## 3.6.20

### Fixes
* Fixed issue with `apps add --validate` not displaying some errors, such as 'name: must be unique'.

## 3.6.19

### Enhancements
* Updated `instances list` to display a `CREATED BY` column.

## 3.6.18

### Fixes
* Fixed `history` command some more.

## 3.6.17

### Fixes
* Fixed `history` command behavior.

## 3.6.16

### Fixes
* Fixed `monitor-incidents list` `--status` and `--severity` options.
* Fixed `monitor-checks mute` Unexpected Error

## 3.6.15

### Fixes
* Fixed `groups use` causing unexpected error. This error was NOT seen when inside a morpheus shell, and likely impacted other commands too.

## 3.6.14

### Enhancments
* New options `instances list --details` to Display more details: memory and storage usage used / max values. `apps` and `hosts` have this option too.
* New option `tenants update --active [on|off]`

### Fixes
* Fixed `tenants update -O` not working.

## 3.6.13

### Enhancments
* Improved table display by preventing table wrapping. Only the columns that fit the terminal width will be displayed. This is enabled by default. If you want to see columns that are hidden because of terminal width, you can use `--all-fields` or `--fields x,y,z` option.
* Removed the *table_print* gem as a dependency.
* Changed usage of `tenants groups list -a [account]` to `tenants groups list [tenant]`.
* Improved `history` command. All prior commands are viewable now, instead of only the last 1000. History recording is now supported on Windows.

### Fixes
* Fixed `history` on Windows only displaying commands from current shell session.
* Fixed `clouds types` error.

## 3.6.12

### Enhancments
* Improved `history` command to support standard search `-s` and sort `-S` options.
* Changed `debug` command to work the same as `debug on`. The same goes for `coloring`.

### Fixes
* Removed extraneous debugging output with `cypher put`.
* Changed `cypher put` to put `ttl` in the query params and not the JSON payload.

## 3.6.11

* Improved `process list`, `process get`, `instances history` and `apps history` by truncating output by default. The new option `--details` can be used to see everything.
* New option `process list --app` for filtering by app(s).

### Fixes
* Fixed `cypher put` so that it skips the 'overwrite' confirmation prompt if the key does not exist already. It makes a list request beforehand to check if the key exists.
* Fix `apps security-groups-apply` causing Unexpected Error
* Fixed issue `history` command itself being logged consecutive times in the command history list.
* Fixed `man -gq` not being quiet
* Fixed a few help docs.


### Enhancements
* Fixed versioning to match current morpheus appliance version: `3.6.1`. Hopefully this avoid some confusion.

## 3.6.10

### Enhancements
* Finished adding support for `--curl`, `--timeout` and `--header` to all commands that should have it.
* Removed default 30 second timeout for `POST` and `PUT` api requests. Only `GET` requests will use the default 30 second timeout.  The new option `--timeout`  gives users a workaround as well.

### Fixes
* Fixed `whoami --dry-run` causing error.

### Deprecations
* Removed command `app-templates`. This has been deprecated and hidden since it was replaced with `blueprints`.

## 3.6.9

### Enhancements

**This release has so much!**

* Updated `cypher` command for simplified cypher key management. (requires appliance 3.6.0-2) The previous command that consumes the old cypher API is still available as the hidden command `old-cypher`. Please update your usage accordingly.
* Improved `login`. Refresh tokens are now stored with credentials to support refreshing.
* New command `access-token` that behaves like `whoami -t`
* New command `access-token refresh`.
* Updated `whoami` to
* New command `login --test` for testing credentials without updating the your session.
* New command `passwd` for changing passwords.
* New command `benchmark` to run adhoc benchmark tests for a command or series of commands. Also provides [on|off] commands to control the global benchmarking flag while in a shell.
* New option `-B` or `--benchmark` to print output about how long it took to run a command and the exit status.
* New option `--remote-url` for transient login with any command.
* New option `-U` or `--username` for transient login with any command.
* New option `-P` or `--password` for transient login with any command.
* Removed the short option `-B` from the `--keep-backups` option.
* New option `--curl` for doing a dry run that outputs a curl command that can be copy and pasted.
* New option `--header` to add extra headers to api requests.
* New option `--timeout` to use a custom timeout to api requests.
* note: `--header`, `--curl` and `--timeout` support is limited at the moment. It supported by a few several common commands eg. instances and apps. All will support it soon.
* Renamed `accounts` to `tenants`. The old command still exists, though it will be deprecated in the future.  Please update your scripts to use `tenants`.
* Updated `alias` command to improve help output and usability.
* Updated `--dry-run` output format to improve readability and usability. It  prints DRY RUN right away, before prompting, etc.
* Updated command `roles get` output to remove deprecated 'Role Instance Limits' settings. Also, moved global settings to details section to improve readability.
* Updated command `users get` output to remove deprecated 'Instance Limits' settings.
* New option `--thin` for less bulky headers and tables. At the moment,  support for this is...thin. A few popular commands fully support it eg. `instances`.
* Changed time format to no longer display the timezone ISO code. This was taking up extra space on some already too-wide tables.  We can add a timezone setting to the cli soon.

### Fixes
* Fix `groups list` missing support for `--dry-run`

## 3.6.8

### Fixes
* Fix issue with custom shell prompts not showing username after logging in.

## 3.6.7

### Fixes
* Fix issue with `apps` status displaying empty instead of PROVISIONING.

## 3.6.6

### Fixes
* Fix issue with `instances start` support of `-y` option.

## 3.6.5

### Enhancements
* Updated `instances stop|start|restart|etc` to accept multiple instance arguments.
* Updated `hosts stop|start` to accept multiple host arguments.
* Added confirmation to `instances start`, and support of Auto Confirm `-y` option.
* Added confirmation to `hosts start`, and support of Auto Confirm `-y` option.

## 3.6.4

### Enhancements
* Updated `apps add` to merge blueprints into payload and prompt for instance configuration.
* New option `apps add --validate` to only validate without creating.
* Replaced `apps add --config` options with standard `--payload` options.
* Replaced `blueprints add --config` options with standard `--payload` options.
* Updated `blueprints add` to prompt for type.
* New commands `apps stop|start|restart`
* New option `--payload-dir` for all commands supporting `--payload`.
* New option `--prompt` for all commands supporting `--options`.

### Fixes
* Fix issue with `apps add` not showing useful error messages.

## 3.6.3

### Fixes
* Fix issue with `apps add` not including `-O` options

## 3.6.2

### Fixes
* Fix issue with `run-workflow` requiring parameters

## 3.6.1

### Fixes
* Fix issue with archives upload timing out for large files

## 3.6.0

### Enhancements
* New commands `monitor-checks mute-all`

### Fixes
* Fix issue with `roles update-cloud-access` when group has to be specified
* Fix issue with `roles update --multitenant off`

## 3.5.3

### Enhancements
* New command `blueprints` to replace `app-templates`. The old command still exists, though it will be deprecated in the future.
* New command `instances history`
* New command `instances exec`
* New command `user-settings`
* New command `process`
* New command `execution-request`
* Change `instances add --workflow` to support Name or ID
* New filter option `tasks list --types`
* New filter option `servers list --account`. Servers finds records for all tenants by default for master tenant users.
* New command `roles update-global-blueprint-access` and `roles update-blueprint-access`
* New command `hosts update`

### Fixes
* Fix cloud status display not showing DISABLED.
* Fix issue with `--refresh-until [status]` never stopping.
* Fix issue with `--nocolor` not resetting between shell commands
* Fix issue with `remote add` always asking for login credentials twice.

### Deprecations

## 3.5.2

### Enhancements
* Updates to `instances list` and `instances get` to consume new api format for stats and load balancer data (no longer need to stitch together)
* New options for `instances update` to update metadata, power schedule, and group
* Renamed `storage-providers` to `storage-buckets` to correspond with API changes.
* The `--remove-volumes` option has been replaced with `--preserve-volumes` to correspond with API changes.
* `login` now prints 'Logged in to %remote as %username' on success
* New option `--refresh-until [status]` for `instances get`, `apps get` and `servers get`.

## 3.5.1.3

### Fixes
* Fix error output for `whoami -T [token] -j`

## 3.5.1.2

### Enhancements
* Renamed power-scheduling to `power-schedules` and mapped to new api endpoint
* Added new command `execute-schedules`
* Added new option `curl --pretty`
* Updated `curl [url]` to allow an absolute URL to allow easier copy and pasting

### Fixes
* Fixed issue with `shell` log-level being saved for subsequent commands when using `--debug` while in a shell
* Fixed some errors seen with power schedules

## 3.5.1.1

### Fixes
* Fixed issue with `storage-providers add -t rackspace`

## 3.5.1

### Enhancements
* New command `cypher` for managing cypher keys
* Updated `library-option-lists` to support the Source Headers settings
* Updated `storage-providers` file browser commands
* Updated `clouds` to display the Enabled setting
* Updated `set-prompt` to no longer reset to terminal default colors for input. Append `%reset` to your prompt string to keep that behavior.

## 3.4.1.10

### Fixes
* `instances update` should allow any option with `-O`

## 3.4.1.9

### Fixes
* Allow removing tasks still in use with `tasks remove --force`

## 3.4.1.8

### Fixes
* Fixes for `virtual-images add`

### New Dependencies
* Ruby version >= 2.3 is now required. This is for the http gem.

### Enhancements
* Improve performance of `virtual-images add`
* Improve performance of `virtual-images add`

### Fixes
* Allow task phase to specified for `workflows add --tasks`
* Fix error seen with `whoami -j`

## 3.4.1.4

### Enhancements
* New option `login -T` to login with an existing access token instead of a username and password

## 3.4.1.3

### Fixes
* Fix issue with `--fields` resulting in 'null' for values that should be 'false'.

## 3.4.1.2

### Fixes
* Fix issue with `--fields` resulting in 'null' for values that should be 'false'.

## 3.4.1.1

### Fixes
* Fix error with `policies` command.

## 3.4.1

### Enhancements
* New command `datastores` for managing cloud datastores
* New command `accounts groups` for managing subtenant groups

### Fixes
* Fix `--fields` option for lots of `list` and `get` commands

## 3.3.2.6

### Enhancements
* Enhanced expression parsing for `morpheus shell`. Parenthesis can be used in conjuction with operators. eg. `(whoami || login) && (instances list -m 5; hosts list -m 5)`

## 3.3.2.5

### Enhancements
* Updated `clouds list` supports more standard options
* Updated `clouds get` supports multiple arguments
* Updated `clouds add` and `clouds update` to support the `--payload` option.

### Fixes
* Fix issue with `clouds add` not including the default `config.certificateProvider` value, which the 3.3.2 api (incorrectly) requires.

## 3.3.2.4

### Enhancements
* `instances add` has new options `--name`, `--create-user` and `--user-group`
* `instances add` uses `--create-user=on` by default
* `instances add` will combine options on top of `--payload`

## 3.3.2.3

### Enhancements
* Improved commands `workflows` and `tasks`
* New commands `edit-profile` and `edit-rc`
* Removed `--json-raw` from help output.

## 3.3.2.2

### Fixes
* Fix issue with `library-file-template add --file`.

## 3.3.2.1

### Enhancements
* `morpheus` now parses pipe `|` input as command arguments. eg. `cat my_host_ids.txt | morpheus instances get`

## 3.3.2

### Enhancements
* New commands `library-*` to replace old `library` command
* New command `user-sources`
* Improved option `-F --fields`. You can now use field `as Label` eg. `--fields "id,name,plan.id as planId"`
* New option `-Q --query` for several `list` commands. This allows filtering with arbitrary query params.
* `shell` now supports simple use of `||` and `&&` operators
* New option `shell -e` for executing shell scripts
* New option `shell -Z` for Incognito mode
* New utility commands `edit-profile` and `edit-rc` and `sleep`

## 3.2.0

### Enhancements
* New commands `monitor-groups`, `monitor-groups`
* Renamed command `checks` to `monitor-checks`
* Renamed `incidents` to `monitor-incidents`
* New command `user-groups`
* New command `users passwd`
* Updated `users` commands to support `--payload` options

## 3.1.2

### Enhancements
* New command `storage-providers`
* New command `networks`, `network-groups`, `network-pools`, and others
* New option `--payload FILE` and `--payload-json JSON` for `instances add`

### Fixes
* Fix issue with `instances add` showing details after provisioning.

## 3.1.0

### Enhancements
* Changed format of command `instances add`. The old format of `instance add [type] [name]` is deprecated. The new format is `instances add [name] -t TYPE`
* Updated command `instances add` for 3.0
* Updated command `app-templates` for 3.0
* Updated command `apps` for 3.0
* New command `image-builder`
* New command `archives`

## 2.11.3.4

### Enhancements
* `virtual-images` command uploads without multipart.

### Fixes
* `roles update-feature-access` should allow any access value eg. 'user' or 'view'

## 2.11.3.3

### Fixes
* Fix issue with `remote setup --insecure`

## 2.11.3.2

### Fixes
* IP Address (optional) when using networks with IP Pools or DHCP.

## 2.11.3.1

### Fixes
* Fix issues with `remote add --insecure` and `shell --insecure`

## 2.11.2

### Enhancements
* New options for `instances add`. Automation inputs such as workflow, shutdown days, create backups, metadata.
* New command `recent-activity`

### Fixes

## 2.11.1

### Enhancements
* New command `containers action|actions|get|reject|restart|start|stop|suspend`
* New command `instances containers` and `instances get --containers`
* New command `instances scaling` and  `instances --scaling`
* New command `instances scaling-update`
* New command `instances action|actions`

### Fixes
* Fix `load-balancers add`
* Fix issue with Virtual Image prompt being optional when provisioning a private image.
* Fix issue with whoami --remote

## 2.11.0

### Enhancements
* Improved `remote` commands. Added `remote get`, `remote check`. Remote appliance status and session activity can now be seen.
* New command `incidents` for managing monitoring incidents.
* New command `checks` for managing monitoring checks.
* New options `--csv` and `--fields`.  Only available for `hosts` and `instances` at the moment.
* New commands `library option-types` and `library option-lists`
* New command `whoami -t` to print your access token only.
* New command `curl` for adhoc api testing.
* New command `man` for viewing the [CLI-Manual](CLI-Manual).
* Formatting changes for Details output, aligned and right justified labels.
* Formatting changes for `--help` output.

### Fixes
* Fixed missing command `instances logs`
* Errors are now written to STDERR.

## 2.10.3

### Enhancements
* Network Domain selection during instance and server provisioning

### Fixes
* Fix error seen when $HOME/.morpheus directory does not exist yet.
* Fix bug with `alias` not being available right away within a shell
* Fix some behavior with the shell's `history`, `!`  `!!` commands

## 2.10.2

### Enhancements

* Proper `.morpheusrc` file support for the shell.  You can put any morpheus command in here now.
* Support for `.morpheus_profile` and disabling it with the `--noprofile` option.
* Aliases need to be exported with `-e` or `alias export`, which stores them in the .morpheus_profile file.
* new script commands: source, echo, ssl-verification, coloring, log-level
* The `--debug` option now prints every API request that morpheus makes, and http response code. You can also turn this on all the time automatically in your .morpheus_profile with `log-level debug`
* Added `hosts make-managed`

### Fixes
* Fix a bug seen with Azure provisioning.
* Fix `shell --insecure` not working
* Fix `hosts upgrade-agent`
* Fix `instances clone`

## 2.10.1

### Enhancements

* Renamed the subcommand `details` to `get` for all commands. Use `hosts get "myhost"` instead of `hosts details "myhost"`
* Prettier usage stats for `instances get`, `hosts get` and `apps get`
* Display more information about `groups` and `clouds`  e.g. Clouds assigned to group, # of Hosts
* Added `groups add-cloud` and `groups remove-cloud` for managing which clouds are assigned to a group
* Added new `instances` commands `suspend`, `eject`, `console` and `status-check`
* Environment Variable configuration for `instances add`
* New options `--copies` and `--layout-size` for `instances add`
* Description, Environment, Tags options for `instances add`
* Added `remote setup` to [Setup New Appliance](Setup-New-Appliance)
* Support for the `-r` `--remote` option on just about every command
* Added `virtual-images` command for Virtual Image management
* Better [Morpheus Shell](Shell) performance and functionality
* Added [Morpheus Alias](Alias)
* Improved option parsing for all commands.  e.g.  [name] argument may appear before or after option switches
* Improved help documentation for all commands
* Make `list` the default subcommand for many commands. Now `hosts` can be used in place of `hosts list`.  This is experimental, and may be removed in 2.10.2
