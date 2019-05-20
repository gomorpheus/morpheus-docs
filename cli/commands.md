## MORPHEUS COMMANDS

    We divide morpheus into commands.  
    Every morpheus command may have 0-N sub-commands that it supports.
    Commands generally map to the functionality provided in the Morpheus UI.

    You can get help for any morpheus command by using the -h option.

    The available commands and their options are also documented below.


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
	roles
	security-group-rules
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

For more information, see https://github.com/gomorpheus/morpheus-cli/wiki
```


### morpheus access-token

```
Usage: morpheus access-token [command] [options]
Commands:
	details
	get
	refresh
```

#### morpheus access-token details

```
Usage: morpheus access-token details
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print your current authentication credentials.
This contains tokens that should be kept secret, be careful.
```

#### morpheus access-token get

```
Usage: morpheus access-token get
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print your current access token.
This token should be kept secret. Be careful.
```

#### morpheus access-token refresh

```
Usage: morpheus access-token refresh
    -y, --yes                        Auto Confirm
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -j, --json                       JSON Output
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Use your refresh token.
This will replace your current access and refresh tokens with a new values.
Your current access token will be invalidated
All other users or applications with access to your token will need to update to the new token.
```


### morpheus alias

```
Usage: morpheus alias [command] [options]
Commands:
	add
	export
	list
	remove
```

#### morpheus alias add

```
Usage: morpheus alias add [name]='[command]'
    -e, --export                     Export this alias to your .morpheus_profile for future use
    -h, --help                       Print this help

Define a new alias.
[name] is required. This is the alias name. It should be one word.
[command] is required. This is the full command wrapped in quotes.
Aliases can be exported for future use with the -e option.
The `alias add` command can be invoked with `alias [name]=[command]`

Examples:
    alias cloud=clouds
    alias ij='instances get -j'
    alias new-hosts='hosts list -S id -D'
For more information, see https://github.com/gomorpheus/morpheus-cli/wiki/Alias
```

#### morpheus alias export

```
Usage: morpheus alias export [alias] [alias2] [alias3]
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Export an alias, saving it to your .morpheus_profile for future use
```

#### morpheus alias list

```
Usage: morpheus alias list
    -f, --format FORMAT              The format for the output: export, json, list, table (default).
    -e, --export                     Include the '-e' switch after each alias in the output. This implies --format export.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print list of defined aliases.    
Use the --format option to vary output.
The `alias list` command can be abbreviated as just `alias`.
For more information, see https://github.com/gomorpheus/morpheus-cli/wiki/Alias
```

#### morpheus alias remove

```
Usage: morpheus alias remove [alias1] [alias2]
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This is how you remove alias definitions from your .morpheus_profile
```


### morpheus apps

```
Usage: morpheus apps [command] [options]
Commands:
	add
	add-instance
	apply-security-groups
	count
	firewall-disable
	firewall-enable
	get
	history
	list
	logs
	remove
	remove-instance
	restart
	security-groups
	start
	stop
	update
```

#### morpheus apps add

```
Usage: morpheus apps add [name] [options]
    -b, --blueprint BLUEPRINT        Blueprint Name or ID. The default value is 'existing' which means no blueprint, for creating a blank app and adding existing instances.
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Default Cloud Name or ID.
        --name VALUE                 Name
        --description VALUE          Description
    -e, --environment VALUE          Environment Name
        --validate                   Validate Only. Validates the configuration and skips creating it.
        --refresh [SECONDS]          Refresh until status is running,failed. Default interval is 5 seconds.
    -O, --option OPTION              Option in the format -O field="value"
    -P, --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
        --yaml                       YAML Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new app.
[name] is required. This is the name of the new app. It may also be passed as --name or inside your config.
```

#### morpheus apps add-instance

```
Usage: morpheus apps add-instance [app] [instance] [tier]
    -O, --option OPTION              Option in the format -O field="value"
    -P, --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Add an existing instance to an app.
[app] is required. This is the name or id of an app.
[instance] is required. This is the name or id of an instance.
[tier] is required. This is the name of the tier.
```

#### morpheus apps apply-security-groups

```
Usage: morpheus apps apply-security-groups [app] [--clear] [-s]
    -c, --clear                      Clear all security groups
    -s, --secgroups SECGROUPS        Apply the specified comma separated security group ids
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus apps count

```
Usage: morpheus apps count [options]
        --created-by USER            Created By User Username or ID
    -s, --search PHRASE              Search Phrase
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get the number of apps.
```

#### morpheus apps firewall-disable

```
Usage: morpheus apps firewall-disable [app]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus apps firewall-enable

```
Usage: morpheus apps firewall-enable [app]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus apps get

```
Usage: morpheus apps get [app]
        --refresh [SECONDS]          Refresh until status is running,failed. Default interval is 5 seconds.
        --refresh-until STATUS       Refresh until a specified status is reached.
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
        --out FILE                   Write standard output to a file instead of the terminal.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about an app.
[app] is required. This is the name or id of an app. Supports 1-N [app] arguments.
```

#### morpheus apps history

```
Usage: morpheus apps history [app]
        --events                     Display sub processes (events).
        --output                     Display process output.
        --details                    Display more details. Shows everything, untruncated.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List historical processes for a specific app.
[app] is required. This is the name or id of an app.
```

#### morpheus apps list

```
Usage: morpheus apps list
        --created-by USER            Created By User Username or ID
        --details                    Display more details: memory and storage usage used / max values.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List apps.
```

#### morpheus apps logs

```
Usage: morpheus apps logs [app]
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List logs for an app.
[app] is required. This is the name or id of an app.
```

#### morpheus apps remove

```
Usage: morpheus apps remove [app]
        --remove-instances [on|off]  Remove instances. Default is off.
        --preserve-volumes [on|off]  Preserve Volumes. Default is off. Applies to certain types only.
        --keep-backups               Preserve copy of backups
        --releaseEIPs [on|off]       Release EIPs. Default is on. Applies to Amazon only.
    -f, --force                      Force Delete
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -y, --yes                        Auto Confirm
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete an app.
[app] is required. This is the name or id of an app.
```

#### morpheus apps remove-instance

```
Usage: morpheus apps remove-instance [app] [instance]
    -O, --option OPTION              Option in the format -O field="value"
    -P, --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Remove an instance from an app.
[app] is required. This is the name or id of an app.
[instance] is required. This is the name or id of an instance.
```

#### morpheus apps restart

```
Usage: morpheus apps restart [app]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Restart an app.
[app] is required. This is the name or id of an app. Supports 1-N [app] arguments.
```

#### morpheus apps security-groups

```
Usage: morpheus apps security-groups [app]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus apps start

```
Usage: morpheus apps start [app]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Start an app.
[app] is required. This is the name or id of an app. Supports 1-N [app] arguments.
```

#### morpheus apps stop

```
Usage: morpheus apps stop [app]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Stop an app.
[app] is required. This is the name or id of an app. Supports 1-N [app] arguments.
```

#### morpheus apps update

```
Usage: morpheus apps update [app] [options]
    -g, --group GROUP                Group Name or ID
        --name VALUE                 Name
        --description VALUE          Description
        --environment VALUE          Environment
    -O, --option OPTION              Option in the format -O field="value"
    -P, --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update an app.
[app] is required. This is the name or id of an app.
```


### morpheus archives

```
Usage: morpheus archives [command] [options]
Commands:
	add
	add-file-link
	download
	download-bucket
	download-link
	file
	file-history
	file-links
	get
	list
	list-files
	ls
	read
	remove
	remove-file
	remove-file-link
	rm
	update
	upload
```

#### morpheus archives add

```
Usage: morpheus archives add [options]
        --name VALUE                 Name
        --description VALUE          Description
        --storageProvider VALUE      Storage Provider ID
        --visibility [private|public]
                                     Visibility determines if read access is restricted to the specified Tenants (Private) or all tenants (Public).
        --accounts LIST              Tenant Accounts (comma separated ids)
        --isPublic [on|off]          Enabling Public URL allows files to be downloaded without any authentication.
    -O, --option OPTION              Option in the format -O field="value"
    -P, --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new archive bucket.
```

#### morpheus archives add-file-link

```
Usage: morpheus archives add-file-link [bucket:/path]
    -e, --expire SECONDS             The time to live for this link. The default is 1200 (20 minutes). A value less than 1 means never expire.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a public link to a file.
[bucket:/path] is required. This is the name of the bucket and /path the file or folder to be fetched.
```

#### morpheus archives download

```
Usage: morpheus archives download [bucket:/path] [local-file]
    -f, --force                      Overwrite existing [local-file] if it exists.
        --mkdir                      Create missing directories for [local-file] if they do not exist.
    -p, --public                     Use Public Download URL instead of Private. The file must be in a public archives.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Download an archive file or directory.
[bucket:/path] is required. This is the name of the bucket and /path the file or folder to be downloaded.
[local-file] is required. This is the full local filepath for the downloaded file.
Directories will be downloaded as a .zip file, so you'll want to specify a [local-file] with a .zip extension.
```

#### morpheus archives download-bucket

```
Usage: morpheus archives download-bucket [bucket] [local-file]
    -f, --force                      Overwrite existing [local-file] if it exists.
    -p, --mkdir                      Create missing directories for [local-file] if they do not exist.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Download an entire archive bucket as a .zip file.
[bucket] is required. This is the name of the bucket.
[local-file] is required. This is the full local filepath for the downloaded file.
Buckets are be downloaded as a .zip file, so you'll want to specify a [local-file] with a .zip extension.
```

#### morpheus archives download-link

```
Usage: morpheus archives download-link [link-key] [local-file]
    -f, --force                      Overwrite existing [local-file] if it exists.
    -p, --mkdir                      Create missing directories for [local-file] if they do not exist.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Download an archive file link.
[link-key] is required. This is the secret access key for the archive file link.
[local-file] is required. This is the full local filepath for the downloaded file.
```

#### morpheus archives file

```
Usage: morpheus archives file [bucket:/path]
    -L, --all-links                  Display all links instead of only 10.
    -H, --all-history                Display all history instead of only 10.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about an archive file.
[bucket:/path] is required. This is the name of the bucket and /path the file or folder to be fetched.
[id] can be passed instead of [bucket:/path]. This is the numeric File ID.
```

#### morpheus archives file-history

```
Usage: morpheus archives file-history [bucket:/path]
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List history log events for an archive file.
```

#### morpheus archives file-links

```
Usage: morpheus archives file-links [bucket:/path]
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List links for an archive file.
```

#### morpheus archives get

```
Usage: morpheus archives get [bucket:/path]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Display archive bucket details and files.
The [bucket] component of the argument is the name or id of an archive bucket.
The [:/path] component is optional and can be used to display files under a sub-directory.
```

#### morpheus archives list

```
Usage: morpheus archives list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List archive buckets.
```

#### morpheus archives list-files

```
Usage: morpheus archives list-files [bucket:/path]
    -a, --all                        Show all files, including subdirectories under the /path.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List files in an archive bucket.
Include [/path] to show files under a directory.
```

#### morpheus archives ls

```
Usage: morpheus archives ls [bucket/path]
    -a, --all                        Show all files, including subdirectories under the /path.
    -l, --long                       Lists files in the long format, which contains lots of useful information, e.g. the exact size of the file, the file type, and when it was last modified.
    -H, --human                      Humanized file sizes. The default is just the number of bytes.
    -1, --oneline                    One file per line. The default delimiter is a single space.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print filenames for a given archive location.
Pass archive location in the format bucket/path.
```

#### morpheus archives read

```
Usage: morpheus archives read [bucket:/path]
    -y, --yes                        Auto Confirm
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print the contents of an archive file.
[bucket:/path] is required. This is the name of the bucket and /path the file or folder to be downloaded.
Confirmation is needed if the specified file is more than 1KB.
This confirmation can be skipped with the -y option.
```

#### morpheus archives remove

```
Usage: morpheus archives remove [bucket]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus archives remove-file

```
Usage: morpheus archives remove-file [bucket:/path]
    -R, --recursive                  Delete a directory and all of its files. This must be passed if specifying a directory.
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete an archive file or directory.
```

#### morpheus archives remove-file-link

```
Usage: morpheus archives remove-file-link [bucket:/path] [token]
    -y, --yes                        Auto Confirm
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a public link to a file.
[bucket:/path] is required. This is the name of the bucket and /path the file or folder to be fetched.[token] is required. This is the secret access key that identifies the link.
```

#### morpheus archives rm

```
Usage: morpheus archives remove-file [bucket:/path]
    -R, --recursive                  Delete a directory and all of its files. This must be passed if specifying a directory.
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete an archive file or directory.
```

#### morpheus archives update

```
Usage: morpheus archives update [bucket] [options]
        --name VALUE                 Name
        --description VALUE          Description
        --payload-file FILE          JSON Payload from a local file
        --visibility [private|public]
                                     Visibility determines if read access is restricted to the specified Tenants (Private) or all tenants (Public).
        --accounts LIST              Tenant Accounts (comma separated ids)
        --isPublic [on|off]          Enabling Public URL allows files to be downloaded without any authentication.
    -O, --option OPTION              Option in the format -O field="value"
    -P, --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update an existing archive bucket.
```

#### morpheus archives upload

```
Usage: morpheus archives upload [local-file] [bucket:/path]
    -R, --recursive                  Upload a directory and all of its files. This must be passed if [local-file] is a directory.
        --ignore-files PATTERN       Pattern of files to be ignored when uploading a directory.
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Upload a local file or folder to an archive bucket.
The first argument [local-file] should be the path of a local file or directory.
The second argument [bucket:/path] should contain the bucket name.
The [:/path] component is optional and can be used to specify the destination of the uploaded file or folder.
The default destination is the same name as the [local-file], under the root bucket directory '/'.
This will overwrite any existing remote files that match the destination /path.
```


### morpheus benchmark

```
Usage: morpheus benchmark [command] [options]
Commands:
	exec
	off
	off?
	on
	on?
	start
	status
	stop
```

#### morpheus benchmark exec

```
Usage: morpheus benchmark exec [command...]
    -n, --iterations NUMBER          Number of iterations to run. The default is 1.
        --name NAME                  Name for the benchmark. Default is the command itself.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Benchmark a specified command.
[command] is required. This is the command to execute
```

#### morpheus benchmark off

```
Usage: morpheus benchmark off
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Disable global benchmarking.
The default state for this setting is off.
```

#### morpheus benchmark off?

```
Usage: morpheus benchmark off?
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print the value of the global benchmark setting.
Exit 0 if off.
```

#### morpheus benchmark on

```
Usage: morpheus benchmark on
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Enable global benchmarking.
This behaves the same as if you were to add the -B switch to every command.
```

#### morpheus benchmark on?

```
Usage: morpheus benchmark on?
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print the value of the global benchmark setting.
Exit 0 if on.
```

#### morpheus benchmark start

```
Usage: morpheus benchmark start [name]
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Start recording a benchmark.
[name] is required. This is just a name for the routine.
This allows you to record how long it takes to run a series of commands.
Just run `benchmark stop` when you are finished.
```

#### morpheus benchmark status

```
Usage: morpheus benchmark status [name]
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print status of benchmark.
[name] is optional. This is the name of the benchmark to inspect.
The last benchmark is used by default.
```

#### morpheus benchmark stop

```
Usage: morpheus benchmark stop [name]
        --exit CODE                  Exit code to end benchmark with. Default is 0 to indicate success.
        --error ERROR                Error message to include with a benchmark that failed.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Stop recording a benchmark.
[name] is optional. This is the name of the benchmark to stop.
The last benchmark is used by default.
```


### morpheus blueprints

```
Usage: morpheus blueprints [command] [options]
Commands:
	add
	add-instance
	add-instance-config
	add-tier
	available-tiers
	connect-tiers
	disconnect-tiers
	duplicate
	get
	list
	remove
	remove-instance
	remove-instance-config
	remove-tier
	types
	update
	update-permissions
	update-tier
	upload-image
```

#### morpheus blueprints add

```
Usage: morpheus blueprints add [name] [options]
        --name VALUE                 Name - Enter a name for this app
        --description VALUE          Description (optional)
        --category VALUE             Category (optional)
    -t, --type TYPE                  Blueprint Type. Default is morpheus.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new blueprint.
[name] is required. This is the name of the new blueprint.
```

#### morpheus blueprints add-instance

```
Usage: morpheus blueprints add-instance [id] [tier] [instance-type]
        --name VALUE                 Instance Name
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a blueprint, adding an instance.
[id] is required. This is the name or id of a blueprint.
[tier] is required and will be prompted for. This is the name of the tier.
[instance-type] is required and will be prompted for. This is the type of instance.
```

#### morpheus blueprints add-instance-config

```
Usage: morpheus blueprints add-instance-config [id] [tier] [instance]
    -g, --group GROUP                Group
    -c, --cloud CLOUD                Cloud
    -e, --env ENVIRONMENT            Environment
        --name VALUE                 Instance Name
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a blueprint, adding an instance config.
[id] is required. This is the name or id of a blueprint.
[tier] is required. This is the name of the tier.
[instance] is required. This is the type of instance.
```

#### morpheus blueprints add-tier

```
Usage: morpheus blueprints add-tier [id] [tier]
        --name VALUE                 Tier Name
        --bootOrder NUMBER           Boot Order
        --linkedTiers x,y,z          Connected Tiers.
        --tierIndex NUMBER           Tier Index. Used for Display Order
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus blueprints available-tiers

```
Usage: morpheus blueprints available-tiers
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus blueprints connect-tiers

```
Usage: morpheus blueprints connect-tiers [id] [Tier1] [Tier2]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus blueprints disconnect-tiers

```
Usage: morpheus blueprints disconnect-tiers [id] [Tier1] [Tier2]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus blueprints duplicate

```
Usage: morpheus blueprints duplicate [id] [new name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Duplicate a blueprint.
[id] is required. This is the name or id of a blueprint.
[new name] is required. This is the name for the clone.
```

#### morpheus blueprints get

```
Usage: morpheus blueprints get [id]
    -c, --config                     Display raw config only. Default is YAML. Combine with -j for JSON instead.
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
        --out FILE                   Write standard output to a file instead of the terminal.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a blueprint.
[id] is required. This is the name or id of a blueprint.
```

#### morpheus blueprints list

```
Usage: morpheus blueprints list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List blueprints.
```

#### morpheus blueprints remove

```
Usage: morpheus blueprints remove [id]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a blueprint.
[id] is required. This is the name or id of a blueprint.
```

#### morpheus blueprints remove-instance

```
Usage: morpheus blueprints remove-instance [id] [tier] [instance]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus blueprints remove-instance-config

```
Usage: morpheus blueprints remove-instance-config [id] [tier] [instance] -g GROUP -c CLOUD
    -g, --group GROUP                Group
    -c, --cloud CLOUD                Cloud
    -e, --env ENV                    Environment
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a blueprint, removing a specified instance config.
[id] is required. This is the name or id of a blueprint.
[tier] is required. This is the name of the tier.
[instance] is required. This is the type of instance.
The config scope is specified with the -g GROUP, -c CLOUD and -e ENV. The -g and -c options are required.
```

#### morpheus blueprints remove-tier

```
Usage: morpheus blueprints remove-tier [id] [tier]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus blueprints types

```
Usage: morpheus blueprints types
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List blueprint types.
```

#### morpheus blueprints update

```
Usage: morpheus blueprints update [id] [options]
        --name VALUE                 Name (optional) - Enter a name for this app
        --category VALUE             Category (optional)
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a blueprint.
[id] is required. This is the name or id of a blueprint.
[options] Available options include --name and --description. This will update only the specified values.
[--config] or [--config-file] can be used to replace the entire blueprint.
```

#### morpheus blueprints update-permissions

```
Usage: morpheus blueprints update-permissions [id] [options]
        --group-access-all [on|off]  Toggle Access for all groups.
        --group-access LIST          Group Access, comma separated list of group IDs.
        --visibility [private|public]
                                     Visibility
        --name VALUE                 Name (optional) - Enter a name for this app
        --category VALUE             Category (optional)
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a blueprint permissions.
[id] is required. This is the name or id of a blueprint.
```

#### morpheus blueprints update-tier

```
Usage: morpheus blueprints update-tier [id] [tier]
        --name VALUE                 Tier Name
        --bootOrder NUMBER           Boot Order
        --linkedTiers x,y,z          Connected Tiers
        --tierIndex NUMBER           Tier Index. Used for Display Order
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus blueprints upload-image

```
Usage: morpheus blueprints upload-image [id] [file]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Upload an image file to be used as the icon for a blueprint.
[id] is required. This is the name or id of a blueprint.
[file] is required. This is the local path of a file to upload [png|jpg|svg].
```


### morpheus clouds

```
Usage: morpheus clouds [command] [options]
Commands:
	add
	apply-security-groups
	count
	firewall-disable
	firewall-enable
	get
	list
	remove
	security-groups
	types
	update
```

#### morpheus clouds add

```
Usage: morpheus clouds add [name] --group GROUP --type TYPE
    -g, --group GROUP                Group Name
    -t, --type TYPE                  Cloud Type
        --description DESCRIPTION    Description (optional)
        --certificate-provider CODE  Certificate Provider. Default is 'internal'
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus clouds apply-security-groups

```
Usage: morpheus clouds apply-security-groups [name] [-s] [--clear]
    -c, --clear                      Clear all security groups
    -s, --secgroups SECGROUPS        Apply the specified comma separated security group ids
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus clouds count

```
Usage: morpheus clouds count [options]
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get the number of clouds.
```

#### morpheus clouds firewall-disable

```
Usage: morpheus clouds firewall-disable [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus clouds firewall-enable

```
Usage: morpheus clouds firewall-enable [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus clouds get

```
Usage: morpheus clouds get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a cloud.
[name] is required. This is the name or id of a cloud.
```

#### morpheus clouds list

```
Usage: morpheus clouds list
    -g, --group GROUP                Group Name
    -t, --type TYPE                  Cloud Type
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List clouds.
```

#### morpheus clouds remove

```
Usage: morpheus clouds remove [name]
    -f, --force                      Force Remove
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus clouds security-groups

```
Usage: morpheus clouds security-groups [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus clouds types

```
Usage: morpheus clouds types
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus clouds update

```
Usage: morpheus clouds update [name] [options]
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus containers

```
Usage: morpheus containers [command] [options]
Commands:
	action
	actions
	eject
	exec
	get
	restart
	start
	stop
	suspend
```

#### morpheus containers action

```
Usage: morpheus containers action [id list] -a CODE
    -a, --action CODE                Container Action CODE to execute
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Execute an action for a container or containers
```

#### morpheus containers actions

```
Usage: morpheus containers actions [id list]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This outputs the list of the actions available to specified container(s).
```

#### morpheus containers eject

```
Usage: morpheus containers eject [id list]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus containers exec

```
Usage: morpheus containers exec [id] [options]
        --script SCRIPT              Script to be executed
        --file FILE                  File containing the script. This can be used instead of --script
        --no-refresh                 Do not refresh until finished
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Execute an arbitrary command or script on a container.
[id] is required. This is the id a container.
[script] is required. This is the script that is to be executed.
```

#### morpheus containers get

```
Usage: morpheus containers get [name]
        --actions                    Display Available Actions
        --refresh [SECONDS]          Refresh until status is running,failed. Default interval is 5 seconds.
        --refresh-until STATUS       Refresh until a specified status is reached.
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus containers restart

```
Usage: morpheus containers restart [id list]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus containers start

```
Usage: morpheus containers start [id list]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus containers stop

```
Usage: morpheus containers stop [id list]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus containers suspend

```
Usage: morpheus containers suspend [id list]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus cypher

```
Usage: morpheus cypher [command] [options]
Commands:
	get
	list
	put
	remove
```

#### morpheus cypher get

```
Usage: morpheus cypher get [key]
    -v, --value                      Print only the decrypted value.
    -t, --ttl SECONDS                Time to live, the lease duration before this key expires. Use if creating new key.
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Read a cypher item and display the decrypted value.
[key] is required. This is the cypher key to read.
Use --ttl to specify a ttl if expecting cypher engine to automatically create the key.
```

#### morpheus cypher list

```
Usage: morpheus cypher list [key]
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List cypher keys.
[key] is optional. This is the cypher key or path to search for.
```

#### morpheus cypher put

```
Usage: morpheus cypher put [key] [value]
    -v, --value VALUE                Secret value
    -t, --ttl SECONDS                Time to live, the lease duration before this key expires.
    -y, --yes                        Auto Confirm
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create or update a cypher key.
[key] is required. This is the key of the cypher being created or updated.
[value] is required. This is the new value or value pairs being stored. Supports format foo=bar, 1-N arguments.
The --payload option can be used instead of passing [value] argument.
```

#### morpheus cypher remove

```
Usage: morpheus cypher remove [key]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a cypher.
[key] is required. This is the key of a cypher.
```


### morpheus datastores

```
Usage: morpheus datastores [command] [options]
Commands:
	get
	list
	update
```

#### morpheus datastores get

```
Usage: morpheus datastores get [datastore]
    -c, --cloud CLOUD                Cloud Name or ID
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a datastore.
[datastore] is required. This is the name or id of a datastore.
-c [cloud] is required. This is the name or id of the cloud.
```

#### morpheus datastores list

```
Usage: morpheus datastores list -c [cloud]
    -c, --cloud CLOUD                Cloud Name or ID
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List datastores for a cloud.
-c [cloud] is required. This is the name or id of the cloud.
```

#### morpheus datastores update

```
Usage: morpheus datastores update [datastore] -c [cloud] [options]
    -c, --cloud CLOUD                Cloud Name or ID
        --group-access-all [on|off]  Toggle Access for all groups.
        --group-access LIST          Group Access, comma separated list of group IDs.
        --tenants LIST               Tenant Access, comma separated list of account IDs
        --visibility [private|public]
                                     Visibility
        --active [on|off]            Can be used to disable a datastore
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a datastore.
[datastore] is required. This is the id of a datstore.
```


### morpheus deploy

```
Usage: morpheus deploy [environment]
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Deploy to an environment using the morpheus.yml file, located in the working directory.
```


### morpheus deployments

```
Usage: morpheus deployments [command] [options]
Commands:
	add
	list
	remove
	update
	versions
```

#### morpheus deployments add

```
Usage: morpheus deployments add [name]
        --description DESCRIPTION    Description
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus deployments list

```
Usage: morpheus deployments list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus deployments remove

```
Usage: morpheus deployments remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus deployments update

```
Usage: morpheus deployments update [name] [options]
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus deployments versions

```
Usage: morpheus deployments versions [name] versions
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus edit-profile

```
Usage: morpheus edit-profile
    -e, --editor PROGRAM             Editor program to use. The default is $EDITOR.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Edit your interactive shell script at /Users/jwheeler/.morpheus/.morpheus_profile
```


### morpheus edit-rc

```
Usage: morpheus edit-rc
    -e, --editor PROGRAM             Editor program to use. The default is $EDITOR.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Edit your morpheus initialization script at /Users/jwheeler/.morpheus/.morpheusrc
```


### morpheus execute-schedules

```
Usage: morpheus execute-schedules [command] [options]
Commands:
	add
	add-hosts
	add-instances
	get
	list
	remove
	remove-hosts
	remove-instances
	update
```

#### morpheus execute-schedules add

```
Usage: morpheus execute-schedules add [name]
        --name VALUE                 Name
        --description VALUE          Description
        --type [execute]             Type of Schedule. Default is 'execute'
        --timezone CODE              The timezone. Default is UTC.
        --cron EXPRESSION            Cron Expression. Default is daily at midnight '0 0 * * *'
        --enabled [on|off]           Can be used to disable it
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new execute schedule.
[name] is required and can be passed as --name instead.
```

#### morpheus execute-schedules add-hosts

```
Usage: morpheus execute-schedules add-hosts [name] [host]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Assign hosts to a execute schedule.
[name] is required. This is the name or id of a execute schedule.
[host] is required. This is the name or id of a host. More than one can be passed.
```

#### morpheus execute-schedules add-instances

```
Usage: morpheus execute-schedules add-instances [name] [instance]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Assign instances to a execute schedule.
[name] is required. This is the name or id of a execute schedule.
[instance] is required. This is the name or id of an instance. More than one can be passed.
```

#### morpheus execute-schedules get

```
Usage: morpheus execute-schedules get [name]
        --max-instances VALUE        Display a limited number of instances in schedule. Default is 25
        --max-hosts VALUE            Display a limited number of hosts in schedule. Default is 25
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus execute-schedules list

```
Usage: morpheus execute-schedules list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus execute-schedules remove

```
Usage: morpheus execute-schedules remove [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -y, --yes                        Auto Confirm
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus execute-schedules remove-hosts

```
Usage: morpheus execute-schedules remove-hosts [name] [host]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Remove hosts from a execute schedule.
[name] is required. This is the name or id of a execute schedule.
[host] is required. This is the name or id of a host. More than one can be passed.
```

#### morpheus execute-schedules remove-instances

```
Usage: morpheus execute-schedules remove-instances [name] [instance]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Remove instances from a execute schedule.
[name] is required. This is the name or id of a execute schedule.
[instance] is required. This is the name or id of an instance. More than one can be passed.
```

#### morpheus execute-schedules update

```
Usage: morpheus execute-schedules update [name]
        --name VALUE                 Name
        --description VALUE          Description
        --type [execute]             Type of Schedule. Default is 'execute'
        --timezone CODE              The timezone. Default is UTC.
        --cron EXPRESSION            Cron Expression
        --enabled [on|off]           Can be used to disable it
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a execute schedule.
[name] is required. This is the name or id of a execute schedule.
```


### morpheus execution-request

```
Usage: morpheus execution-request [command] [options]
Commands:
	execute
	get
```

#### morpheus execution-request execute

```
Usage: morpheus execution-request execute [options]
        --server ID                  Server ID
        --instance ID                Instance ID
        --container ID               Container ID
        --request ID                 Execution Request ID
        --script SCRIPT              Script to be executed
        --file FILE                  File containing the script. This can be used instead of --script
        --no-refresh                 Do not refresh until finished
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Execute an arbitrary script.
[server] or [instance] or [container] is required. This is the id of a server, instance or container.
[script] is required. This is the script that is to be executed.
```

#### morpheus execution-request get

```
Usage: morpheus execution-request get [uid]
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
        --refresh [SECONDS]          Refresh until execution is finished. Default interval is 5 seconds.

Get details about an execution request.
[uid] is required. This is the unique id of an execution request.
```


### morpheus file-copy-request

```
Usage: morpheus file-copy-request [command] [options]
Commands:
	download
	execute
	get
```

#### morpheus file-copy-request download

```
Usage: morpheus file-copy-request download [uid] [file]
        --file FILE                  Local file destination for the downloaded file.
    -f, --force                      Overwrite existing [file] if it exists.
    -p, --mkdir                      Create missing directories for [file] if they do not exist.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Download a file associated with a file copy request.
[uid] is required. This is the unique id of a file copy request.
[file] is required. This is the full local filepath for the downloaded file.
```

#### morpheus file-copy-request execute

```
Usage: morpheus file-copy-request execute [options]
        --server ID                  Server ID
        --instance ID                Instance ID
        --container ID               Container ID
        --request ID                 File Copy Request ID
        --file FILE                  Local file to be copied.
        --target-path PATH           Target path for file on destination host.
        --no-refresh                 Do not refresh until finished
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Copy a file to a remote host(s).
[server] or [instance] or [container] is required. This is the id of a server, instance or container.
[file] is required. This is the local filename that is to be copied.
[target-path] is required. This is the target path for the file on the destination host.
```

#### morpheus file-copy-request get

```
Usage: morpheus file-copy-request get [uid]
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
        --refresh [SECONDS]          Refresh until execution is finished. Default interval is 5 seconds.

Get details about a file copy request.
[uid] is required. This is the unique id of a file copy request.
```


### morpheus groups

```
Usage: morpheus groups [command] [options]
Commands:
	add
	add-cloud
	current
	get
	list
	remove
	remove-cloud
	unuse
	update
	use
```

#### morpheus groups add

```
Usage: morpheus groups add [name]
        --name VALUE                 Name
        --code VALUE                 Code (optional)
        --location VALUE             Location (optional)
        --use                        Make this the current active group
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new group.
```

#### morpheus groups add-cloud

```
Usage: morpheus groups add-cloud [name] CLOUD
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Add a cloud to a group.
```

#### morpheus groups current

```
Usage: morpheus groups current
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print the name of the current active group
```

#### morpheus groups get

```
Usage: morpheus groups get [name]
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a group.
[name] is required. This is the name or id of a group. Supports 1-N arguments.
```

#### morpheus groups list

```
Usage: morpheus groups list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List groups (sites).
```

#### morpheus groups remove

```
Usage: morpheus groups remove [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -y, --yes                        Auto Confirm
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a group.
```

#### morpheus groups remove-cloud

```
Usage: morpheus groups remove-cloud [name] CLOUD
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Remove a cloud from a group.
```

#### morpheus groups unuse

```
Usage: morpheus groups unuse
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This will clear the current active group.
You will be prompted for a Group during provisioning.
```

#### morpheus groups update

```
Usage: morpheus groups update [name] [options]
        --name VALUE                 Name (optional)
        --code VALUE                 Code (optional)
        --location VALUE             Location (optional)
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update an existing group.
```

#### morpheus groups use

```
Usage: morpheus groups use [name]
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This sets the active group.
The active group will be auto-selected for use during provisioning.
You can still use the --group option to override this.
```


### morpheus hosts

```
Usage: morpheus hosts [command] [options]
Commands:
	add
	count
	exec
	get
	list
	logs
	make-managed
	remove
	resize
	run-workflow
	start
	stats
	stop
	types
	update
	upgrade-agent
```

#### morpheus hosts add

```
Usage: morpheus hosts add [cloud] [name]
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Cloud Name or ID
    -t, --type TYPE                  Server Type Code
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus hosts count

```
Usage: morpheus hosts count [options]
    -a, --account ACCOUNT            Account Name or ID
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Cloud Name or ID
    -M, --managed                    Show only Managed Servers
        --unmanaged                  Show only Unmanaged Servers
    -t, --type TYPE                  Show only Certain Server Types
    -p, --power STATE                Filter by Power Status
    -i, --ip IPADDRESS               Filter by IP Address
        --vm
                                     Show only virtual machines
        --hypervisor
                                     Show only VM Hypervisors
        --container
                                     Show only Container Hypervisors
        --baremetal
                                     Show only Baremetal Servers
        --status STATUS
                                     Filter by Status
        --agent
                                     Show only Servers with the agent installed
        --noagent
                                     Show only Servers with No agent
        --created-by USER            Created By User Username or ID
        --details                    Display more details: memory and storage usage used / max values.
    -s, --search PHRASE              Search Phrase
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get the number of hosts.
```

#### morpheus hosts exec

```
Usage: morpheus hosts exec [id] [options]
        --script SCRIPT              Script to be executed
        --file FILE                  File containing the script. This can be used instead of --script
        --no-refresh                 Do not refresh until finished
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Execute an arbitrary command or script on a host.
[id] is required. This is the id a host.
[script] is required. This is the script that is to be executed.
```

#### morpheus hosts get

```
Usage: morpheus hosts get [name]
        --refresh [SECONDS]          Refresh until status is running,failed. Default interval is 5 seconds.
        --refresh-until STATUS       Refresh until a specified status is reached.
    -j, --json                       JSON Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
        --yaml                       YAML Output
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus hosts list

```
Usage: morpheus hosts list
    -a, --account ACCOUNT            Account Name or ID
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Cloud Name or ID
    -M, --managed                    Show only Managed Servers
        --unmanaged                  Show only Unmanaged Servers
    -t, --type TYPE                  Show only Certain Server Types
    -p, --power STATE                Filter by Power Status
    -i, --ip IPADDRESS               Filter by IP Address
        --vm
                                     Show only virtual machines
        --hypervisor
                                     Show only VM Hypervisors
        --container
                                     Show only Container Hypervisors
        --baremetal
                                     Show only Baremetal Servers
        --status STATUS
                                     Filter by Status
        --agent
                                     Show only Servers with the agent installed
        --noagent
                                     Show only Servers with No agent
        --created-by USER            Created By User Username or ID
        --details                    Display more details: memory and storage usage used / max values.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List hosts.
```

#### morpheus hosts logs

```
Usage: morpheus hosts logs [name]
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus hosts make-managed

```
Usage: morpheus hosts make-managed [name]
        --sshUsername VALUE          SSH Username
        --sshPassword VALUE          SSH Password (optional)
        --serverOs VALUE             OS Type (optional)
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus hosts remove

```
Usage: morpheus hosts remove [name]
        --remove-resources [on|off]  Remove Infrastructure. Default is on if server is managed.
        --preserve-volumes [on|off]  Preserve Volumes. Default is off.
        --remove-instances [on|off]  Remove Associated Instances. Default is off.
        --release-eips [on|off]      Release EIPs, default is on. Amazon only.
    -f, --force                      Force Delete
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus hosts resize

```
Usage: morpheus hosts resize [name]
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus hosts run-workflow

```
Usage: morpheus hosts run-workflow [name] [workflow] [options]
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus hosts start

```
Usage: morpheus hosts start [name]
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Start a host.
[name] is required. This is the name or id of a host. Supports 1-N [name] arguments.
```

#### morpheus hosts stats

```
Usage: morpheus hosts stats [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus hosts stop

```
Usage: morpheus hosts stop [name]
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Stop a host.
[name] is required. This is the name or id of a host. Supports 1-N [name] arguments.
```

#### morpheus hosts types

```
Usage: morpheus hosts types
    -c, --cloud CLOUD                Cloud Name or ID
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List host types.
```

#### morpheus hosts update

```
Usage: morpheus hosts update [name]
        --name VALUE                 Name
        --description VALUE          Description
        --ssh-username VALUE         SSH Username
        --ssh-password VALUE         SSH Password
        --power-schedule-type ID     Power Schedule Type ID
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus hosts upgrade-agent

```
Usage: morpheus hosts upgrade-agent [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus image-builder

```
Usage: morpheus image-builder [command] [options]
Commands:
	add
	boot-scripts
	get
	list
	list-runs
	preseed-scripts
	remove
	run
	update
```

#### morpheus image-builder add

```
Usage: morpheus image-builder add [options]
    -t, --type TYPE                  Image Build Type
        --name VALUE                 Name
        --description VALUE          Description
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Cloud Name or ID
        --config JSON                Instance Config JSON
        --config-yaml YAML           Instance Config YAML
        --config-file FILE           Instance Config from a local JSON or YAML file
        --bootScript VALUE           Boot Script ID
        --bootCommand VALUE          Boot Command. This can be used in place of a bootScript
        --preseedScript VALUE        Preseed Script ID
        --scripts LIST               Additional Scripts (comma separated names or ids)
        --sshUsername VALUE          SSH Username
        --sshPassword VALUE          SSH Password
        --storageProvider VALUE      Storage Provider ID
        --isCloudInit [on|off]       Cloud Init?
        --buildOutputName VALUE      Build Output Name
        --conversionFormats VALUE    Conversion Formats ie. ovf, qcow2, vhd
        --keepResults VALUE          Keep only the most recent builds. Older executions will be deleted along with their associated Virtual Images. The value 0 disables this functionality.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus image-builder boot-scripts

```
Usage: morpheus image-builder boot-scripts [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus image-builder get

```
Usage: morpheus image-builder get [image-build]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus image-builder list

```
Usage: morpheus image-builder list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus image-builder list-runs

```
Usage: morpheus image-builder list-runs [image-build]
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Display a list of executions for an image build.
```

#### morpheus image-builder preseed-scripts

```
Usage: morpheus image-builder preseed-scripts [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus image-builder remove

```
Usage: morpheus image-builder remove [image-build]
    -K, --keep-virtual-images        Preserve associated virtual images
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus image-builder run

```
Usage: morpheus image-builder run [image-build]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus image-builder update

```
Usage: morpheus image-builder update [image-build] [options]
    -t, --type TYPE                  Image Build Type
        --name VALUE                 New Name
        --description VALUE          Description
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Cloud Name or ID
        --config JSON                Instance Config JSON
        --config-yaml YAML           Instance Config YAML
        --config-file FILE           Instance Config from a local JSON or YAML file
        --bootScript VALUE           Boot Script ID
        --bootCommand VALUE          Boot Command. This can be used in place of a bootScript
        --preseedScript VALUE        Preseed Script ID
        --scripts LIST               Additional Scripts (comma separated names or ids)
        --sshUsername VALUE          SSH Username
        --sshPassword VALUE          SSH Password
        --storageProvider VALUE      Storage Provider ID
        --isCloudInit [on|off]       Cloud Init?
        --buildOutputName VALUE      Build Output Name
        --conversionFormats VALUE    Conversion Formats ie. ovf, qcow2, vhd
        --keepResults VALUE          Keep only the most recent builds. Older executions will be deleted along with their associated Virtual Images. The value 0 disables this functionality.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus instance-types

```
Usage: morpheus instance-types [command] [options]
Commands:
	get
	list
```

#### morpheus instance-types get

```
Usage: morpheus instance-types get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get instance type details.
[name] is required. This is the name or id of an instance type.
```

#### morpheus instance-types list

```
Usage: morpheus instance-types list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
        --category VALUE             Filter by category
        --code VALUE                 Filter by code
        --technology VALUE           Filter by technology

List instance types.
```


### morpheus instances

```
Usage: morpheus instances [command] [options]
Commands:
	action
	actions
	add
	apply-security-groups
	backup
	backups
	clone
	console
	containers
	count
	delenv
	eject
	envs
	exec
	firewall-disable
	firewall-enable
	get
	history
	history-details
	history-event
	import-snapshot
	list
	logs
	remove
	resize
	restart
	restart-service
	run-workflow
	scaling
	scaling-update
	security-groups
	setenv
	start
	start-service
	stats
	status-check
	stop
	stop-service
	suspend
	update
	update-notes
```

#### morpheus instances action

```
Usage: morpheus instances action [id list] -a CODE
    -a, --action CODE                Instance Action CODE to execute
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Execute an action for one or many instances.
```

#### morpheus instances actions

```
Usage: morpheus instances actions [id or name list]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This outputs the list of the actions available to specified instance(s).
```

#### morpheus instances add

```
Usage: morpheus instances add [name] -c CLOUD -t TYPE
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Cloud Name or ID
    -t, --type CODE                  Instance Type
        --name NAME                  Instance Name
        --description [TEXT]         Description
        --copies NUMBER              Number of copies to provision
        --layout-size NUMBER         Apply a multiply factor of containers/vms within the instance
        --workflow ID                Automation: Workflow ID
        --create-user on|off         User Config: Create Your User. Default is on
        --user-group USERGROUP       User Config: User Group
        --shutdown-days NUMBER       Automation: Shutdown Days
        --expire-days NUMBER         Automation: Expiration Days
        --create-backup [on|off]     Automation: Create Backups.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new instance.
[name] is required. This is the new instance name.
The available options vary by --type.
```

#### morpheus instances apply-security-groups

```
Usage: morpheus instances apply-security-groups [name] [-S] [-c]
    -S, --secgroups SECGROUPS        Apply the specified comma separated security group ids
    -c, --clear                      Clear all security groups
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances backup

```
Usage: morpheus instances backup [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances backups

```
Usage: morpheus instances backups [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances clone

```
Usage: morpheus instances clone [name] -g GROUP
        --name VALUE                 Name - Enter a name for the new instance
    -g, --group GROUP                Group Name or ID for the new instance
    -c, --cloud CLOUD                Cloud Name or ID for the new instance
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances console

```
Usage: morpheus instances console [name]
    -n, --node NODE_ID               Scope console to specific Container or VM
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances containers

```
Usage: morpheus instances containers [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances count

```
Usage: morpheus instances count [options]
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Cloud Name or ID
        --host HOST                  Host Name or ID
        --created-by USER            Created By User Username or ID
    -s, --search PHRASE              Search Phrase
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get the number of instances.
```

#### morpheus instances delenv

```
Usage: morpheus instances delenv [name] VAR
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances eject

```
Usage: morpheus instances eject [name]
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Eject an instance.
[name] is required. This is the name or id of an instance. Supports 1-N [name] arguments.
```

#### morpheus instances envs

```
Usage: morpheus instances envs [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances exec

```
Usage: morpheus instances exec [id] [options]
        --script SCRIPT              Script to be executed
        --file FILE                  File containing the script. This can be used instead of --script
        --no-refresh                 Do not refresh until finished
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Execute an arbitrary script or command on an instance.
[id] is required. This is the id or name of an instance.
[script] is required. This is the script that is to be executed.
```

#### morpheus instances firewall-disable

```
Usage: morpheus instances firewall-disable [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances firewall-enable

```
Usage: morpheus instances firewall-enable [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances get

```
Usage: morpheus instances get [instance]
        --containers                 Display Instance Containers
        --nodes                      Alias for --containers
        --vms                        Alias for --containers
        --scaling                    Display Instance Scaling Settings
        --refresh [SECONDS]          Refresh until status is running,failed. Default interval is 5 seconds.
        --refresh-until STATUS       Refresh until a specified status is reached.
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about an instance.
[instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.
```

#### morpheus instances history

```
Usage: morpheus instances history [instance]
        --events                     Display sub processes (events).
        --output                     Display process output.
        --details                    Display more details: memory and storage usage used / max values.
        --process-id ID              Display details about a specfic process only.
        --event-id ID                Display details about a specfic process event only.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List historical processes for a specific instance.
[instance] is required. This is the name or id of an instance.
```

#### morpheus instances history-details

```
Usage: morpheus instances history-details [instance] [process-id]
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Display history details for a specific process.
[instance] is required. This is the name or id of an instance.
[process-id] is required. This is the id of the process.
```

#### morpheus instances history-event

```
Usage: morpheus instances history-event [instance] [event-id]
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Display history details for a specific process event.
[instance] is required. This is the name or id of an instance.
[event-id] is required. This is the id of the process event.
```

#### morpheus instances import-snapshot

```
Usage: morpheus instances import-snapshot [name]
        --storage-provider ID        Optional storage provider
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances list

```
Usage: morpheus instances list
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Cloud Name or ID
        --host HOST                  Host Name or ID
        --created-by USER            Created By User Username or ID
        --details                    Display more details: memory and storage usage used / max values.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List instances.
```

#### morpheus instances logs

```
Usage: morpheus instances logs [name]
    -n, --node NODE_ID               Scope logs to specific Container or VM
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances remove

```
Usage: morpheus instances remove [name]
        --keep-backups               Preserve copy of backups
        --preserve-volumes [on|off]  Preserve Volumes. Default is off. Applies to certain types only.
        --releaseEIPs [on|off]       Release EIPs. Default is on. Applies to Amazon only.
    -f, --force                      Force Delete
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances resize

```
Usage: morpheus instances resize [name]
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances restart

```
Usage: morpheus instances restart [name]
        --mute-monitoring [on|off]   Mute monitoring. Default is on.
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Restart an instance.
[name] is required. This is the name or id of an instance. Supports 1-N [name] arguments.
```

#### morpheus instances restart-service

```
Usage: morpheus instances restart-service [name]
        --mute-monitoring [on|off]   Mute monitoring. Default is on.
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Restart service on an instance.
[name] is required. This is the name or id of an instance. Supports 1-N [name] arguments.
```

#### morpheus instances run-workflow

```
Usage: morpheus instances run-workflow [name] [workflow] [options]
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances scaling

```
Usage: morpheus instances scaling [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Show scaling threshold information for an instance.
```

#### morpheus instances scaling-update

```
Usage: morpheus instances scaling-update [name]
        --autoUp on|off              Auto Upscale - Enable auto upscaling
        --autoDown on|off            Auto Downscale - Enable auto downscaling
        --zoneId ID                  Cloud (optional) - Choose a cloud to scale into.
        --minCount NUMBER            Min Count (optional) - Minimum number of nodes
        --maxCount NUMBER            Max Count (optional) - Maximum number of nodes
        --memoryEnabled on|off       Enable Memory Threshold - Scale when memory thresholds are met.
        --minMemory PERCENT          Min Memory (optional) - Minimum memory percent (0-100)
        --maxMemory PERCENT          Max Memory (optional) - Maximum memory percent (0-100)
        --diskEnabled on|off         Enable Disk Threshold - Scale when disk thresholds are met.
        --minDisk PERCENT            Min Disk (optional) - Minimum storage percent (0-100)
        --maxDisk PERCENT            Max Disk (optional) - Maximum storage percent (0-100)
        --cpuEnabled on|off          Enable CPU Threshold - Scale when cpu thresholds are met.
        --minCpu PERCENT             Min CPU (optional) - Minimum CPU percent (0-100)
        --maxCpu PERCENT             Max CPU (optional) - Maximum CPU percent (0-100)
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update scaling threshold information for an instance.
```

#### morpheus instances security-groups

```
Usage: morpheus instances security-groups [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances setenv

```
Usage: morpheus instances setenv [name] VAR VALUE [-e]
    -e                               Exportable
    -M                               Masked
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances start

```
Usage: morpheus instances start [name]
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Start an instance.
[name] is required. This is the name or id of an instance. Supports 1-N [name] arguments.
```

#### morpheus instances start-service

```
Usage: morpheus instances start-service [name]
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Start service on an instance.
[name] is required. This is the name or id of an instance. Supports 1-N [name] arguments.
```

#### morpheus instances stats

```
Usage: morpheus instances stats [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances status-check

```
Usage: morpheus instances status-check [name]
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances stop

```
Usage: morpheus instances stop [name]
        --mute-monitoring [on|off]   Mute monitoring. Default is off.
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Stop an instance.
[instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.
```

#### morpheus instances stop-service

```
Usage: morpheus instances stop-service [name]
        --mute-monitoring [on|off]   Mute monitoring. Default is off.
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Stop service on an instance.
[name] is required. This is the name or id of an instance. Supports 1-N [name] arguments.
```

#### morpheus instances suspend

```
Usage: morpheus instances suspend [name]
        --muteMonitoring [on|off]    Mute monitoring. Default is off.
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Suspend an instance.
[name] is required. This is the name or id of an instance. Supports 1-N [name] arguments.
```

#### morpheus instances update

```
Usage: morpheus instances update [name]
        --name VALUE                 Name
        --description VALUE          Description
        --environment VALUE          Environment
        --group GROUP                Group Name or ID
        --metadata LIST              Metadata in the format 'name:value, name:value'
        --tags LIST                  Tags
        --power-schedule-type ID     Power Schedule Type ID
        --created-by ID              Created By User ID
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus instances update-notes

```
Usage: morpheus instances update-notes [name]
        --notes VALUE                Notes content (Markdown)
        --file FILE                  File containing the notes content. This can be used instead of --notes
        --clear                      Clear current notes
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus key-pairs

```
Usage: morpheus key-pairs [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus key-pairs add

```
Usage: morpheus key-pairs add [name] [options]
        --public-key-file FILENAME
                                     Public Key File
        --public-key TEXT
                                     Public Key Text
        --private-key-file FILENAME
                                     Private Key File
        --private-key TEXT
                                     Private Key Text
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus key-pairs get

```
Usage: morpheus key-pairs get [name]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus key-pairs list

```
Usage: morpheus key-pairs list
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus key-pairs remove

```
Usage: morpheus key-pairs remove [name]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus key-pairs update

```
Usage: morpheus key-pairs update [name] [options]
        --name VALUE                 Name
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus library-file-templates

```
Usage: morpheus library-file-templates [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus library-file-templates add

```
Usage: morpheus library-file-templates add [name]
        --name VALUE                 Name
        --fileName VALUE             File Name
        --filePath VALUE             File Path
        --phase [start|stop|postProvision]
                                     Template Phase. Default is 'provision'
        --category VALUE             Category
        --template TEXT              Contents of the template.
        --file FILE                  File containing the template. This can be used instead of --template
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new file template.
[name] is required and can be passed as --name instead.
```

#### morpheus library-file-templates get

```
Usage: morpheus library-file-templates get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-file-templates list

```
Usage: morpheus library-file-templates list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-file-templates remove

```
Usage: morpheus library-file-templates remove [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -y, --yes                        Auto Confirm
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-file-templates update

```
Usage: morpheus library-file-templates update [name]
        --name VALUE                 Name
        --fileName VALUE             File Name
        --filePath VALUE             File Path
        --phase [start|stop]         Template Phase
        --template TEXT              Contents of the template.
        --file FILE                  File containing the template. This can be used instead of --template
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a file template.
[name] is required. This is the name or id of a file template.
```


### morpheus library-instance-types

```
Usage: morpheus library-instance-types [command] [options]
Commands:
	add
	get
	list
	remove
	update
	update-logo
```

#### morpheus library-instance-types add

```
Usage: morpheus library-instance-types add
        --name VALUE                 Name
        --code VALUE                 Code - Useful shortcode for provisioning naming schemes and export reference.
        --description VALUE          Description (optional)
        --category VALUE             Category
        --logo VALUE                 Icon File (optional)
        --visibility VALUE           Visibility (optional) Default: private
        --environmentPrefix VALUE    Environment Prefix (optional) - Used for exportable environment variables when tying instance types together in app contexts. If not specified a name will be generated.
        --hasSettings on|off         Enable Settings (optional)
        --hasAutoScale on|off        Enable Scaling (Horizontal) (optional)
        --hasDeployment on|off       Supports Deployments (optional) - Requires a data volume be configured on each version. Files will be copied into this location.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new instance type.
```

#### morpheus library-instance-types get

```
Usage: morpheus library-instance-types get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-instance-types list

```
Usage: morpheus library-instance-types list
        --category VALUE             Filter by category
        --code VALUE                 Filter by code
        --technology VALUE           Filter by technology
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List instance types.
```

#### morpheus library-instance-types remove

```
Usage: morpheus library-instance-types remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete an instance type.
```

#### morpheus library-instance-types update

```
Usage: morpheus library-instance-types update [name] [options]
        --name VALUE                 Name
        --code VALUE                 Code - Useful shortcode for provisioning naming schemes and export reference.
        --description VALUE          Description (optional)
        --category VALUE             Category
        --visibility VALUE           Visibility (optional) Default: private
        --environmentPrefix VALUE    Environment Prefix (optional) - Used for exportable environment variables when tying instance types together in app contexts. If not specified a name will be generated.
        --hasSettings on|off         Enable Settings (optional)
        --hasAutoScale on|off        Enable Scaling (Horizontal) (optional)
        --hasDeployment on|off       Supports Deployments (optional) - Requires a data volume be configured on each version. Files will be copied into this location.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update an instance type.
[name] is required. This is the name or id of a instance type.
```

#### morpheus library-instance-types update-logo

```
Usage: morpheus library-instance-types update-logo [name] [file]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update the logo for an instance type.
[name] is required. This is the name or id of a instance type.
[file] is required. This is the path of the logo file
```


### morpheus library-layouts

```
Usage: morpheus library-layouts [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus library-layouts add

```
Usage: morpheus library-layouts add [instance-type]
        --instance-type ID           Instance Type
        --name VALUE                 Name for this layout
        --version VALUE              Version
        --description VALUE          Description
        --technology CODE            Technology
        --min-memory VALUE           Minimum Memory (MB)
        --workflow ID                Workflow
        --option-types x,y,z         List of Option Type IDs
        --node-types x,y,z           List of Node Type IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new layout.
[instance-type] is required and can be passed as --instance-type instead.
```

#### morpheus library-layouts get

```
Usage: morpheus library-layouts get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-layouts list

```
Usage: morpheus library-layouts list
        --instance-type ID           Filter by Instance Type
        --category VALUE             Filter by category
        --code VALUE                 Filter by code
        --technology VALUE           Filter by technology
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List layouts.
```

#### morpheus library-layouts remove

```
Usage: morpheus library-layouts remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a layout.
```

#### morpheus library-layouts update

```
Usage: morpheus library-layouts update [name] [options]
        --name VALUE                 Name for this layout
        --version VALUE              Version
        --description VALUE          Description
        --min-memory VALUE           Minimum Memory (MB)
        --workflow ID                Workflow
        --option-types x,y,z         List of Option Type IDs
        --node-types x,y,z           List of Node Type IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a layout.
```


### morpheus library-node-types

```
Usage: morpheus library-node-types [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus library-node-types add

```
Usage: morpheus library-node-types add
        --name VALUE                 Name for this node type
        --shortName VALUE            Short Name
        --version VALUE              Version
        --technology CODE            Technology. This is the provision type code.
        --scripts x,y,z              List of Script IDs
        --file-templates x,y,z       List of File Template IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a node type.
[name] is required and can be passed as --name instead.
```

#### morpheus library-node-types get

```
Usage: morpheus library-node-types get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Display node type details.
[name] is required. This is the name or id of a node type.
```

#### morpheus library-node-types list

```
Usage: morpheus library-node-types list
        --layout ID                  Filter by Layout
        --technology VALUE           Filter by technology
        --category VALUE             Filter by category
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List node types.
```

#### morpheus library-node-types remove

```
Usage: morpheus library-node-types remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a node type.
```

#### morpheus library-node-types update

```
Usage: morpheus library-node-types update [name] [options]
        --name VALUE                 Name for this layout
        --shortName VALUE            Short Name
        --version VALUE              Version
        --scripts x,y,z              List of Script IDs
        --file-templates x,y,z       List of File Template IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a node type.
```


### morpheus library-option-lists

```
Usage: morpheus library-option-lists [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus library-option-lists add

```
Usage: morpheus library-option-lists add [type] [options]
    -t, --type TYPE                  Option List Type. (rest, manual)
        --name VALUE                 Name
        --description VALUE          Description (optional)
        --sourceUrl VALUE            Source Url - A REST URL can be used to fetch list data and is cached in the appliance database.
        --ignoreSSLErrors on|off     Ignore SSL Errors (optional) Default: off
        --realTime on|off            Real Time (optional) Default: off
        --sourceMethod VALUE         Source Method Default: GET
        --initialDataset VALUE       Initial Dataset (optional) - Create an initial json dataset to be used as the collection for this option list. It should be a list containing objects with properties 'name', and 'value'. However, if there is a translation script, that will also be passed through.
        --translationScript VALUE    Translation Script (optional) - Create a js script to translate the result data object into an Array containing objects with properties name, and value. The input data is provided as data and the result should be put on the global variable results.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-option-lists get

```
Usage: morpheus library-option-lists get [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This outputs details about a particular Option List.
```

#### morpheus library-option-lists list

```
Usage: morpheus library-option-lists list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -j, --json                       JSON Output
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This outputs a list of custom Option List records.
```

#### morpheus library-option-lists remove

```
Usage: morpheus library-option-lists remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-option-lists update

```
Usage: morpheus library-option-lists update [name] [options]
        --name VALUE                 Name (optional)
        --description VALUE          Description (optional)
        --sourceUrl VALUE            Source Url (optional) - A REST URL can be used to fetch list data and is cached in the appliance database.
        --ignoreSSLErrors on|off     Ignore SSL Errors (optional)
        --realTime on|off            Real Time (optional)
        --sourceMethod VALUE         Source Method (optional)
        --initialDataset VALUE       Initial Dataset (optional) - Create an initial json dataset to be used as the collection for this option list. It should be a list containing objects with properties 'name', and 'value'. However, if there is a translation script, that will also be passed through.
        --translationScript VALUE    Translation Script (optional) - Create a js script to translate the result data object into an Array containing objects with properties name, and value. The input data is provided as data and the result should be put on the global variable results.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus library-option-types

```
Usage: morpheus library-option-types [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus library-option-types add

```
Usage: morpheus library-option-types add [options]
        --name VALUE                 Name
        --description VALUE          Description (optional)
        --fieldName VALUE            Field Name - This is the input fieldName property that the value gets assigned to.
        --type VALUE                 Type Default: text
        --fieldLabel VALUE           Field Label - This is the input label that shows typically to the left of a custom option.
        --placeHolder VALUE          Placeholder (optional)
        --defaultValue VALUE         Default Value (optional)
        --required on|off            Required (optional) Default: off
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-option-types get

```
Usage: morpheus library-option-types get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-option-types list

```
Usage: morpheus library-option-types list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -j, --json                       JSON Output
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List option types.
```

#### morpheus library-option-types remove

```
Usage: morpheus library-option-types remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-option-types update

```
Usage: morpheus library-option-types update [name] [options]
        --name VALUE                 Name (optional)
        --description VALUE          Description (optional)
        --fieldName VALUE            Field Name (optional) - This is the input fieldName property that the value gets assigned to.
        --type VALUE                 Type (optional)
        --fieldLabel VALUE           Field Label (optional) - This is the input label that shows typically to the left of a custom option.
        --placeHolder VALUE          Placeholder (optional)
        --defaultValue VALUE         Default Value (optional)
        --required on|off            Required (optional)
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus library-scripts

```
Usage: morpheus library-scripts [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus library-scripts add

```
Usage: morpheus library-scripts add [name]
        --name VALUE                 Name
        --type [bash|powershell]     Script Type. Default is 'bash'
        --phase [provision|start|stop]
                                     Script Phase. Default is 'provision'
        --category VALUE             Category
        --script TEXT                Contents of the script.
        --file FILE                  File containing the script. This can be used instead of --script
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new container script.
[name] is required and can be passed as --name instead.
```

#### morpheus library-scripts get

```
Usage: morpheus library-scripts get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-scripts list

```
Usage: morpheus library-scripts list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List container scripts.
```

#### morpheus library-scripts remove

```
Usage: morpheus library-scripts remove [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -y, --yes                        Auto Confirm
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus library-scripts update

```
Usage: morpheus library-scripts update [name]
        --name VALUE                 Name
        --type [bash|powershell]     Script Type
        --phase [start|stop]         Script Phase
        --category VALUE             Category
        --script TEXT                Contents of the script.
        --file FILE                  File containing the script. This can be used instead of --script
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a container script.
[name] is required. This is the name or id of a container script.
```


### morpheus library-upgrades

```
Usage: morpheus library-upgrades [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus library-upgrades add

```
Usage: morpheus library-upgrades add [instance-type] [name]
        --instance-type ID           Instance Type this upgrade belongs to
        --name VALUE                 Name for this upgrade
        --code CODE                  Code
        --description VALUE          Description
        --source-layout ID           Source Layout ID to upgrade from
        --target-layout ID           Target Layout ID to upgrade to
        --upgradeCommand TEXT        Upgrade Command
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new upgrade.
[instance-type] is required.
```

#### morpheus library-upgrades get

```
Usage: morpheus library-upgrades get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about an upgrade.
[instance-type] is required.
[name] is required. This is the name or id of an upgrade.
```

#### morpheus library-upgrades list

```
Usage: morpheus library-upgrades list [instance-type]
        --code VALUE                 Filter by code
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List upgrades.
[instance-type] is required.
```

#### morpheus library-upgrades remove

```
Usage: morpheus library-upgrades remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a upgrade.
```

#### morpheus library-upgrades update

```
Usage: morpheus library-upgrades update [name] [options]
        --name VALUE                 Name for this upgrade
        --version VALUE              Version
        --description VALUE          Description
        --min-memory VALUE           Minimum Memory (MB)
        --workflow ID                Workflow
        --option-types x,y,z         List of Option Type IDs
        --node-types x,y,z           List of Node Type IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a upgrade.
```


### morpheus license

```
Usage: morpheus license [command] [options]
Commands:
	apply
	decode
	get
```

#### morpheus license apply

```
Usage: morpheus license apply [key]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus license decode

```
Usage: morpheus license decode [key]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Decode a license key.
```

#### morpheus license get

```
Usage: morpheus license get
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus load-balancers

```
Usage: morpheus load-balancers [command] [options]
Commands:
	add
	get
	list
	remove
	types
	update
```

#### morpheus load-balancers add

```
Usage: morpheus load-balancers add [name] -t LB_TYPE
    -t, --type LB_TYPE               Load Balancer Type
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus load-balancers get

```
Usage: morpheus load-balancers get [name]
    -j, --json                       JSON Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
        --yaml                       YAML Output
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus load-balancers list

```
Usage: morpheus load-balancers list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
        --yaml                       YAML Output
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus load-balancers remove

```
Usage: morpheus load-balancers remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus load-balancers types

```
Usage: morpheus load-balancers types
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus load-balancers update

```
Usage: morpheus load-balancers update [name] [options]
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus login

```
Usage: morpheus login [username] [password]
    -u, --username USERNAME          Username
    -p, --password PASSWORD          Password
    -t, --test                       Test credentials only, does not update stored credentials for the appliance.
    -T, --token ACCESS_TOKEN         Use an existing access token to login instead of authenticating with a username and password.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Login to a remote appliance with a username and password or an access token.
[username] is required .
[password] is required.
Logging in with username and password will make an authentication api request to obtain an access token.
The --token option can be used to login with an existing token instead of username and password.
Using --token makes a whoami api request to validate the token.
If successful, the access token will be saved with the active session for the remote appliance.
This command will first logout any active session before attempting to login.
The --test option can be used for testing credentials without updating your active session.
```


### morpheus logout

```
Usage: morpheus logout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus monitor-apps

```
Usage: morpheus monitor-apps [command] [options]
Commands:
	add
	get
	list
	mute
	mute-all
	remove
	unmute
	unmute-all
	update
```

#### morpheus monitor-apps add

```
Usage: morpheus monitor-apps add [name]
        --name VALUE                 Name
        --description VALUE          Description
        --minHappy VALUE             Min Checks. This specifies the minimum number of checks within the app that must be happy to keep the app from becoming unhealthy.
        --severity VALUE             Max Severity. Determines the maximum severity level this app can incur on an incident when failing. Default is critical
        --inUptime [on|off]          Affects Availability. Default is on.
        --checks LIST                Checks to include in this app, comma separated list of IDs
        --checkGroups LIST           Check Groups to include in this app, comma separated list of IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new app of monitoring checks.
[name] is required and can be passed as --name instead.
```

#### morpheus monitor-apps get

```
Usage: morpheus monitor-apps get [id list]
        --history                    Display Monitoring App History
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-apps list

```
Usage: morpheus monitor-apps list
        --status LIST                Filter by status. error,healthy,warning,muted
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        --last-updated TIME          Filter by Last Updated (gte)
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-apps mute

```
Usage: morpheus monitor-apps mute [name]
        --disable                    Unmute instead, the same as the unmute command
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Mute a monitoring app. This prevents it from creating new incidents.
[name] is required. This is the name or id of a monitoring app.
```

#### morpheus monitor-apps mute-all

```
Usage: morpheus monitor-apps mute-all
        --disable                    Unmute instead, the same as the unmute-all command
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Mute all monitoring apps. This prevents the creation of new incidents.
```

#### morpheus monitor-apps remove

```
Usage: morpheus monitor-apps remove [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-apps unmute

```
Usage: morpheus monitor-apps unmute [name]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Unmute a monitoring app.
[name] is required. This is the name or id of a monitoring app.
```

#### morpheus monitor-apps unmute-all

```
Usage: morpheus monitor-apps unmute-all
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Unmute all monitoring apps.
```

#### morpheus monitor-apps update

```
Usage: morpheus monitor-apps update [name]
        --name VALUE                 Name
        --description VALUE          Description
        --minHappy VALUE             Min Checks. This specifies the minimum number of checks within the app that must be happy to keep the app from becoming unhealthy.
        --severity VALUE             Max Severity. Determines the maximum severity level this app can incur on an incident when failing. Default is critical
        --inUptime [on|off]          Affects Availability. Default is on.
        --checks LIST                Checks to include in this app, comma separated list of IDs
        --checkGroups LIST           Check Groups to include in this app, comma separated list of IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a monitoring app.
[name] is required. This is the name or id of a monitoring app.
```


### morpheus monitor-checks

```
Usage: morpheus monitor-checks [command] [options]
Commands:
	add
	get
	history
	list
	list-types
	mute
	mute-all
	remove
	unmute
	unmute-all
	update
```

#### morpheus monitor-checks add

```
Usage: morpheus monitor-checks add [name] -t CODE
    -t, --type CODE                  Check Type Code or ID
        --name VALUE                 Name
        --description VALUE          Description
        --checkInterval MILLIS       Check Interval. Value is in milliseconds. Default varies by type.
        --severity VALUE             Max Severity. Determines the maximum severity level this check can incur on an incident when failing. Default is critical
        --inUptime [on|off]          Affects Availability. Default is on.
    -c, --config JSON                Config settings as JSON
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List monitoring checks.
```

#### morpheus monitor-checks get

```
Usage: morpheus monitor-checks get [id list]
        --history                    Display Check History
    -j, --json                       JSON Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-checks history

```
Usage: morpheus monitor-checks history [name] [options]
        --severity LIST              Filter by severity. critical, warning, info
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --last-updated TIME          Filter by Last Updated (gte)
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-checks list

```
Usage: morpheus monitor-checks list
        --status VALUE               Filter by status. error,healthy,warning,muted
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        --last-updated TIME          Filter by Last Updated (gte)
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-checks list-types

```
Usage: morpheus monitor-checks list-types
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List monitoring check types.
```

#### morpheus monitor-checks mute

```
Usage: morpheus monitor-checks mute [name]
        --disable                    Disable mute state instead, the same as unmute
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Mute a check. This prevents it from creating new incidents.
[name] is required. This is the name or id of a check.
```

#### morpheus monitor-checks mute-all

```
Usage: morpheus monitor-checks mute-all
        --disable                    Disable mute state instead, the same as unmute-all
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Mute all checks. This prevents the creation new incidents.
```

#### morpheus monitor-checks remove

```
Usage: morpheus monitor-checks remove [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-checks unmute

```
Usage: morpheus monitor-checks unmute [name]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Unmute a check.
[name] is required. This is the name or id of a check.
```

#### morpheus monitor-checks unmute-all

```
Usage: morpheus monitor-checks unmute-all
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Unmute all checks.
```

#### morpheus monitor-checks update

```
Usage: morpheus monitor-checks update [name]
        --name VALUE                 Name
        --description VALUE          Description
        --checkInterval VALUE        Check Interval. Value is in milliseconds.
        --severity VALUE             Max Severity. Determines the maximum severity level this check can incur on an incident when failing. Default is critical
        --inUptime [on|off]          Affects Availability. Default is on.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a monitoring check.
[name] is required. This is the name or id of a check.
The available options vary by type.
```


### morpheus monitor-contacts

```
Usage: morpheus monitor-contacts [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus monitor-contacts add

```
Usage: morpheus monitor-contacts add [id]
        --name STRING                Contact name
        --email STRING               Contact email address
        --mobile STRING              Contact sms addresss
        --slackHook STRING           Contact slack hook
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-contacts get

```
Usage: morpheus monitor-contacts get [id list]
        --history                    Display History
        --notifications              Display Notifications
    -j, --json                       JSON Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-contacts list

```
Usage: morpheus monitor-contacts list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
        --yaml                       YAML Output
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-contacts remove

```
Usage: morpheus monitor-contacts remove [id list]
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-contacts update

```
Usage: morpheus monitor-contacts update [id]
        --name STRING                Contact name
        --email STRING               Contact email address
        --mobile STRING              Contact sms addresss
        --slackHook STRING           Contact slack hook
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus monitor-groups

```
Usage: morpheus monitor-groups [command] [options]
Commands:
	add
	get
	history
	list
	mute
	mute-all
	remove
	unmute
	unmute-all
	update
```

#### morpheus monitor-groups add

```
Usage: morpheus monitor-groups add [name]
        --name VALUE                 Name
        --description VALUE          Description
        --minHappy VALUE             Min Checks. This specifies the minimum number of checks within the group that must be happy to keep the group from becoming unhealthy.
        --severity VALUE             Max Severity. Determines the maximum severity level this group can incur on an incident when failing. Default is critical
        --inUptime [on|off]          Affects Availability. Default is on.
        --checks LIST                Checks to include in this group, comma separated list of IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new group of monitoring checks.
[name] is required and can be passed as --name instead.
```

#### morpheus monitor-groups get

```
Usage: morpheus monitor-groups get [id list]
        --history                    Display Check Group History
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-groups history

```
Usage: morpheus monitor-groups history [name] [options]
        --severity LIST              Filter by severity. critical, warning, info
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --last-updated TIME          Filter by Last Updated (gte)
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-groups list

```
Usage: morpheus monitor-groups list
        --status VALUE               Filter by status. error,healthy,warning,muted
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        --last-updated TIME          Filter by Last Updated (gte)
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-groups mute

```
Usage: morpheus monitor-groups mute [name]
        --disable                    Disable mute, the same as unmute
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Mute a check group. This prevents it from creating new incidents.
[name] is required. This is the name or id of a check group.
```

#### morpheus monitor-groups mute-all

```
Usage: morpheus monitor-groups mute-all
        --disable                    Disable mute, the same as unmute-all
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Mute all check groups. This prevents the creation of new incidents.
```

#### morpheus monitor-groups remove

```
Usage: morpheus monitor-groups remove [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-groups unmute

```
Usage: morpheus monitor-groups unmute [name]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Unmute a check group.
[name] is required. This is the name or id of a check.
```

#### morpheus monitor-groups unmute-all

```
Usage: morpheus monitor-groups unmute-all
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Unmute all check groups.
```

#### morpheus monitor-groups update

```
Usage: morpheus monitor-groups update [name]
        --name VALUE                 Name for this check group
        --description VALUE          Description
        --minHappy VALUE             Min Checks. This specifies the minimum number of checks within the group that must be happy to keep the group from becoming unhealthy.
        --severity VALUE             Max Severity. Determines the maximum severity level this group can incur on an incident when failing. Default is critical
        --inUptime [on|off]          Affects Availability. Default is on.
        --checks LIST                Checks to include in this group, comma separated list of IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a check group.
[name] is required. This is the name or id of a check group.
```


### morpheus monitor-incidents

```
Usage: morpheus monitor-incidents [command] [options]
Commands:
	close
	get
	history
	list
	mute
	mute-all
	notifications
	reopen
	stats
	unmute
	unmute-all
	update
```

#### morpheus monitor-incidents close

```
Usage: morpheus monitor-incidents close [id list]
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-incidents get

```
Usage: morpheus monitor-incidents get [id list]
        --history                    Display Incident History
        --notifications              Display Incident Notifications
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-incidents history

```
Usage: morpheus monitor-incidents history [id] [options]
        --severity LIST              Filter by severity. critical, warning, info
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --last-updated TIME          Filter by Last Updated (gte)
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
        --yaml                       YAML Output
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-incidents list

```
Usage: morpheus monitor-incidents list
        --status LIST                Filter by status. open, closed
        --severity LIST              Filter by severity. critical, warning, info
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        --last-updated TIME          Filter by Last Updated (gte)
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-incidents mute

```
Usage: morpheus monitor-incidents mute [id]
        --disable                    Disable mute state instead, the same as unmute
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Mute an incident.
[id] is required. This is the id of an incident.
```

#### morpheus monitor-incidents mute-all

```
Usage: morpheus monitor-incidents mute-all
        --disable                    Disable mute state instead, the same as unmute-all
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Mute all open incidents.
```

#### morpheus monitor-incidents notifications

```
Usage: morpheus monitor-incidents notifications [id] [options]
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
        --yaml                       YAML Output
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-incidents reopen

```
Usage: morpheus monitor-incidents reopen [id list]
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-incidents stats

```
Usage: morpheus monitor-incidents stats
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus monitor-incidents unmute

```
Usage: morpheus monitor-incidents unmute [id]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Unmute an incident.
[id] is required. This is the id of an incident.
```

#### morpheus monitor-incidents unmute-all

```
Usage: morpheus monitor-incidents unmute-all
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Unmute all open incidents.
```

#### morpheus monitor-incidents update

```
Usage: morpheus monitor-incidents update [id]
    -c, --comment STRING             Comment on this incident
        --resolution STRING          Description of the resolution to this incident
        --status STATUS              Set status (open or closed)
        --severity STATUS            Set severity (critical, warning or info)
        --name STRING                Set display name (subject)
        --startDate TIME             Set start time
        --endDate TIME               Set end time
        --inUptime BOOL              Set 'In Availability'
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus network-domains

```
Usage: morpheus network-domains [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus network-domains add

```
Usage: morpheus network-domains add
        --name VALUE                 Name for this network domain
        --description VALUE          Description for this network domain
        --public-zone [on|off]       Public Zone
        --domain-controller [on|off] Join Domain Controller
        --domain-username VALUE      Domain Username
        --domain-password VALUE      Domain Password
        --dc-server VALUE            DC Server
        --ou-path VALUE              OU Path
        --visibility [private|public]
                                     Visibility
        --tenant ID                  Tenant Account ID
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new network domain.
[name] is required and can be passed as --name instead.
```

#### morpheus network-domains get

```
Usage: morpheus network-domains get [network-domain]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a network domain.
[network-domain] is required. This is the name or id of a network domain.
```

#### morpheus network-domains list

```
Usage: morpheus network-domains list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List network domains.
```

#### morpheus network-domains remove

```
Usage: morpheus network-domains remove [network-domain]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a network domain.
[network-domain] is required. This is the name or id of a network domain.
```

#### morpheus network-domains update

```
Usage: morpheus network-domains update [network-domain] [options]
        --name VALUE                 Name for this network domain
        --type VALUE                 Type of network domain
        --ip-ranges LIST             IP Ranges, comma separated list IP ranges in the format start-end.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a network domain.
[network-domain] is required. This is the id of a network domain.
```


### morpheus network-groups

```
Usage: morpheus network-groups [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus network-groups add

```
Usage: morpheus network-groups add --networks [id,id,id]
        --name VALUE                 Name for this network group
        --description VALUE          Description of network group
        --networks LIST              Networks in the group, comma separated list of network IDs
        --group-access-all [on|off]  Toggle Access for all groups.
        --group-access LIST          Group Access, comma separated list of group IDs.
        --group-defaults LIST        Group Default Selection, comma separated list of group IDs
        --tenants LIST               Tenant Access, comma separated list of account IDs
        --accounts LIST              alias for --tenants
        --visibility [private|public]
                                     Visibility
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new network group.
[name] is required and can be passed as --name instead.
```

#### morpheus network-groups get

```
Usage: morpheus network-groups get [network-group]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a network group.
[network-group] is required. This is the name or id of a network group.
```

#### morpheus network-groups list

```
Usage: morpheus network-groups list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List network groups.
```

#### morpheus network-groups remove

```
Usage: morpheus network-groups remove [network-group]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a network group.
[network-group] is required. This is the name or id of a network group.
```

#### morpheus network-groups update

```
Usage: morpheus network-groups update [network-group] [options]
        --name VALUE                 Name for this network group
        --description VALUE          Description of network group
        --networks LIST              Networks in the group, comma separated list of network IDs
        --group-access-all [on|off]  Toggle Access for all groups.
        --group-access LIST          Group Access, comma separated list of group IDs.
        --group-defaults LIST        Group Default Selection, comma separated list of group IDs
        --tenants LIST               Tenant Access, comma separated list of account IDs
        --accounts LIST              alias for --tenants
        --visibility [private|public]
                                     Visibility
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a network group.
[network-group] is required. This is the id of a network group.
```


### morpheus network-pool-servers

```
Usage: morpheus network-pool-servers [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus network-pool-servers add

```
Usage: morpheus network-pool-servers add
        --name VALUE                 Name for this network pool server
        --type VALUE                 Type of network pool server
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new network pool server.
[name] is required and can be passed as --name instead.
```

#### morpheus network-pool-servers get

```
Usage: morpheus network-pool-servers get [network-pool-server]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a network pool server.
[network-pool-server] is required. This is the name or id of a network pool server.
```

#### morpheus network-pool-servers list

```
Usage: morpheus network-pool-servers list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List network pool servers.
```

#### morpheus network-pool-servers remove

```
Usage: morpheus network-pool-servers remove [network-pool-server]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a network pool server.
[network-pool-server] is required. This is the name or id of a network pool server.
```

#### morpheus network-pool-servers update

```
Usage: morpheus network-pool-servers update [network-pool-server] [options]
        --name VALUE                 Name for this network pool server
        --type VALUE                 Type of network pool server
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a network pool server.
[network-pool-server] is required. This is the id of a network pool server.
```


### morpheus network-pools

```
Usage: morpheus network-pools [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus network-pools add

```
Usage: morpheus network-pools add
        --name VALUE                 Name for this network pool
        --type VALUE                 Type of network pool
        --ip-ranges LIST             IP Ranges, comma separated list IP ranges in the format start-end.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new network pool.
[name] is required and can be passed as --name instead.
```

#### morpheus network-pools get

```
Usage: morpheus network-pools get [network-pool]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a network pool.
[network-pool] is required. This is the name or id of a network pool.
```

#### morpheus network-pools list

```
Usage: morpheus network-pools list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List network pools.
```

#### morpheus network-pools remove

```
Usage: morpheus network-pools remove [network-pool]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a network pool.
[network-pool] is required. This is the name or id of a network pool.
```

#### morpheus network-pools update

```
Usage: morpheus network-pools update [network-pool] [options]
        --name VALUE                 Name for this network pool
        --type VALUE                 Type of network pool
        --ip-ranges LIST             IP Ranges, comma separated list IP ranges in the format start-end.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a network pool.
[network-pool] is required. This is the id of a network pool.
```


### morpheus network-proxies

```
Usage: morpheus network-proxies [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus network-proxies add

```
Usage: morpheus network-proxies add
        --name VALUE                 Name for this network proxy
        --proxy-host VALUE           Proxy Host
        --proxy-port VALUE           Proxy Port
        --proxy-user VALUE           Proxy User
        --proxy-password VALUE       Proxy Password
        --proxy-domain VALUE         Proxy Domain
        --proxy-workstation VALUE    Proxy Workstation
        --visibility [private|public]
                                     Visibility
        --tenant ID                  Tenant Account ID
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new network proxy.
[name] is required and can be passed as --name instead.
```

#### morpheus network-proxies get

```
Usage: morpheus network-proxies get [network-proxy]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a network proxy.
[network-proxy] is required. This is the name or id of a network proxy.
```

#### morpheus network-proxies list

```
Usage: morpheus network-proxies list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List network proxies.
```

#### morpheus network-proxies remove

```
Usage: morpheus network-proxies remove [network-proxy]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a network proxy.
[network-proxy] is required. This is the name or id of a network proxy.
```

#### morpheus network-proxies update

```
Usage: morpheus network-proxies update [network-proxy] [options]
        --name VALUE                 Name for this network proxy
        --proxy-host VALUE           Proxy Host
        --proxy-port VALUE           Proxy Port
        --proxy-user VALUE           Proxy User
        --proxy-password VALUE       Proxy Password
        --proxy-domain VALUE         Proxy Domain
        --proxy-workstation VALUE    Proxy Workstation
        --visibility [private|public]
                                     Visibility
        --tenant ID                  Tenant Account ID
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a network proxy.
[network-proxy] is required. This is the id of a network proxy.
```


### morpheus network-services

```
Usage: morpheus network-services [command] [options]
Commands:
	list
```

#### morpheus network-services list

```
Usage: morpheus network-services list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List network services.
```


### morpheus networks

```
Usage: morpheus networks [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus networks add

```
Usage: morpheus networks add -t TYPE
    -c, --cloud CLOUD                Cloud Name or ID
    -t, --type ID                    Network Type Name or ID
        --name VALUE                 Name for this network
        --description VALUE          Description of network
        --gateway VALUE              Gateway
        --dns-primary VALUE          DNS Primary
        --dns-secondary VALUE        DNS Secondary
        --cidr VALUE                 CIDR
        --vlan-id VALUE              VLAN ID
        --pool ID                    Network Pool
        --dhcp-server [on|off]       DHCP Server
        --allow-ip-override [on|off] Allow IP Override
        --domain VALUE               Network Domain ID
        --scan [on|off]              Scan Network
        --proxy-bypass [on|off]      Bypass Proxy for Appliance URL
        --no-proxy LIST              No Proxy Addresses
        --group-access-all [on|off]  Toggle Access for all groups.
        --group-access LIST          Group Access, comma separated list of group IDs.
        --group-defaults LIST        Group Default Selection, comma separated list of group IDs
        --tenants LIST               Tenant Access, comma separated list of account IDs
        --accounts LIST              alias for --tenants
        --visibility [private|public]
                                     Visibility
        --active [on|off]            Can be used to disable a network
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new network.
[name] is required and can be passed as --name instead.
```

#### morpheus networks get

```
Usage: morpheus networks get [network]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a network.
[network] is required. This is the name or id of a network.
```

#### morpheus networks list

```
Usage: morpheus networks list
        --cidr VALUE                 Filter by cidr, matches beginning of value.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List networks.
```

#### morpheus networks remove

```
Usage: morpheus networks remove [network]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a network.
[network] is required. This is the name or id of a network.
```

#### morpheus networks update

```
Usage: morpheus networks update [network] [options]
        --name VALUE                 Name for this network
        --description VALUE          Description of network
        --gateway VALUE              Gateway
        --dns-primary VALUE          DNS Primary
        --dns-secondary VALUE        DNS Secondary
        --cidr VALUE                 CIDR
        --vlan-id VALUE              VLAN ID
        --pool ID                    Network Pool
        --dhcp-server [on|off]       DHCP Server
        --allow-ip-override [on|off] Allow IP Override
        --domain VALUE               Network Domain ID
        --scan [on|off]              Scan Network
        --proxy-bypass [on|off]      Bypass Proxy for Appliance URL
        --no-proxy LIST              No Proxy Addresses
        --group-access-all [on|off]  Toggle Access for all groups.
        --group-access LIST          Group Access, comma separated list of group IDs.
        --group-defaults LIST        Group Default Selection, comma separated list of group IDs
        --tenants LIST               Tenant Access, comma separated list of account IDs
        --accounts LIST              alias for --tenants
        --visibility [private|public]
                                     Visibility
        --active [on|off]            Can be used to disable a network
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a network.
[network] is required. This is the id of a network.
```


### morpheus passwd

```
Usage: morpheus passwd [username] [options]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -y, --yes                        Auto Confirm
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Change your password or the password of another user.
[username] is optional. This is the username of the user to update. Default is your own.
Be careful with this command, the default behavior is to update your own password.
```


### morpheus policies

```
Usage: morpheus policies [command] [options]
Commands:
	add
	get
	get-type
	list
	list-types
	remove
	update
```

#### morpheus policies add

```
Usage: morpheus policies add -t TYPE
    -g, --group GROUP                Group Name or ID, for scoping the policy to a group.
    -c, --cloud CLOUD                Cloud Name or ID, for scoping the policy to a cloud
    -u, --user USER                  Username or ID, for scoping the policy to a user
    -t, --type ID                    Policy Type Name or ID
        --name VALUE                 Name for this policy
        --description VALUE          Description of policy
        --accounts LIST              Tenant accounts, comma separated list of account IDs
        --enabled [on|off]           Can be used to disable a policy
        --config JSON                Policy Config JSON
        --config-yaml YAML           Policy Config YAML
        --config-file FILE           Policy Config from a local JSON or YAML file
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new policy.
[name] is optional and can be passed as --name instead.
```

#### morpheus policies get

```
Usage: morpheus policies get [policy]
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Cloud Name or ID
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a policy.
[policy] is required. This is the id of a policy.
```

#### morpheus policies get-type

```
Usage: morpheus policies get-type [policy-type]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a policy type.
[policy-type] is required. This is ID of a policy type.
```

#### morpheus policies list

```
Usage: morpheus policies list
    -g, --group GROUP                Group Name or ID
    -c, --cloud CLOUD                Cloud Name or ID
    -u, --user USER                  Username or ID
    -G, --global                     Global policies only
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List policies.
```

#### morpheus policies list-types

```
Usage: morpheus policies list-types
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List policy types.
```

#### morpheus policies remove

```
Usage: morpheus policies remove [policy]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a policy.
[policy] is required. This is the id of a policy.
```

#### morpheus policies update

```
Usage: morpheus policies update [policy] [options]
        --name VALUE                 Name for this policy
        --description VALUE          Description of policy
        --accounts LIST              Tenant accounts, comma separated list of account IDs
        --enabled [on|off]           Can be used to disable a policy
        --config JSON                Policy Config JSON
        --config-yaml YAML           Policy Config YAML
        --config-file FILE           Policy Config from a local JSON or YAML file
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a policy.
[policy] is required. This is the id of a policy.
```


### morpheus power-schedules

```
Usage: morpheus power-schedules [command] [options]
Commands:
	add
	add-hosts
	add-instances
	get
	list
	remove
	remove-hosts
	remove-instances
	update
```

#### morpheus power-schedules add

```
Usage: morpheus power-schedules add [name]
        --name VALUE                 Name
        --description VALUE          Description
        --type [power|power off]     Type of Schedule. Default is 'power'
        --timezone CODE              The timezone. Default is UTC.
        --sundayOn [0-24]            Sunday start hour. Default is 0.
        --sundayOff [0-24]           Sunday end hour. Default is 24.
        --mondayOn [0-24]            Monday start hour. Default is 0.
        --mondayOff [0-24]           Monday end hour. Default is 24.
        --tuesdayOn [0-24]           Tuesday start hour. Default is 0.
        --tuesdayOff [0-24]          Tuesday end hour. Default is 24.
        --wednesdayOn [0-24]         Wednesday start hour. Default is 0.
        --wednesdayOff [0-24]        Wednesday end hour. Default is 24.
        --thursdayOn [0-24]          Thursday start hour. Default is 0.
        --thursdayOff [0-24]         Thursday end hour. Default is 24.
        --fridayOn [0-24]            Friday start hour. Default is 0.
        --fridayOff [0-24]           Friday end hour. Default is 24.
        --saturdayOn [0-24]          Saturday start hour. Default is 0.
        --saturdayOff [0-24]         Saturday end hour. Default is 24.
        --enabled [on|off]           Can be used to disable it
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new power schedule.
[name] is required and can be passed as --name instead.
```

#### morpheus power-schedules add-hosts

```
Usage: morpheus power-schedules add-hosts [name] [host]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Assign hosts to a power schedule.
[name] is required. This is the name or id of a power schedule.
[host] is required. This is the name or id of a host. More than one can be passed.
```

#### morpheus power-schedules add-instances

```
Usage: morpheus power-schedules add-instances [name] [instance]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Assign instances to a power schedule.
[name] is required. This is the name or id of a power schedule.
[instance] is required. This is the name or id of an instance. More than one can be passed.
```

#### morpheus power-schedules get

```
Usage: morpheus power-schedules get [name]
        --max-instances VALUE        Display a limited number of instances in schedule. Default is 25
        --max-hosts VALUE            Display a limited number of hosts in schedule. Default is 25
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus power-schedules list

```
Usage: morpheus power-schedules list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus power-schedules remove

```
Usage: morpheus power-schedules remove [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -y, --yes                        Auto Confirm
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus power-schedules remove-hosts

```
Usage: morpheus power-schedules remove-hosts [name] [host]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Remove hosts from a power schedule.
[name] is required. This is the name or id of a power schedule.
[host] is required. This is the name or id of a host. More than one can be passed.
```

#### morpheus power-schedules remove-instances

```
Usage: morpheus power-schedules remove-instances [name] [instance]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Remove instances from a power schedule.
[name] is required. This is the name or id of a power schedule.
[instance] is required. This is the name or id of an instance. More than one can be passed.
```

#### morpheus power-schedules update

```
Usage: morpheus power-schedules update [name]
        --name VALUE                 Name
        --description VALUE          Description
        --type [power|power off]     Type of Schedule. Default is 'power'
        --timezone CODE              The timezone. Default is UTC.
        --sundayOn [0-24]            Sunday on hour. Default is 0.
        --sundayOff [0-24]           Sunday off hour. Default is 24.
        --mondayOn [0-24]            Monday on hour. Default is 0.
        --mondayOff [0-24]           Monday off hour. Default is 24.
        --tuesdayOn [0-24]           Tuesday on hour. Default is 0.
        --tuesdayOff [0-24]          Tuesday off hour. Default is 24.
        --wednesdayOn [0-24]         Wednesday on hour. Default is 0.
        --wednesdayOff [0-24]        Wednesday off hour. Default is 24.
        --thursdayOn [0-24]          Thursday on hour. Default is 0.
        --thursdayOff [0-24]         Thursday off hour. Default is 24.
        --fridayOn [0-24]            Friday on hour. Default is 0.
        --fridayOff [0-24]           Friday off hour. Default is 24.
        --saturdayOn [0-24]          Saturday on hour. Default is 0.
        --saturdayOff [0-24]         Saturday off hour. Default is 24.
        --enabled [on|off]           Can be used to disable it
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a power schedule.
[name] is required. This is the name or id of a power schedule.
```


### morpheus process

```
Usage: morpheus process [command] [options]
Commands:
	get
	get-event
	list
```

#### morpheus process get

```
Usage: morpheus process get [id]
        --details                    Display more details. Shows everything, untruncated.
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Display details for a specific process.
```

#### morpheus process get-event

```
Usage: morpheus process get-event [event-id]
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Display details for a specific process event.
[event-id] is required. This is the id of the process event.
```

#### morpheus process list

```
Usage: morpheus process list
        --events                     Display sub processes (events).
        --output                     Display process output.
        --details                    Display all details. Includes sub processes, output and error data is not truncated.
        --app ID                     Limit results to specific app(s).
        --instance ID                Limit results to specific instance(s).
        --container ID               Limit results to specific container(s).
        --host ID                    Limit results to specific host(s).
        --cloud ID                   Limit results to specific cloud(s).
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List historical processes.
```


### morpheus recent-activity

```
Usage: morpheus recent-activity
        --start TIMESTAMP            Start timestamp. Default is 30 days ago.
        --end TIMESTAMP              End timestamp. Default is now.
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus remote

```
Usage: morpheus remote [command] [options]
Commands:
	add
	check
	current
	get
	list
	remove
	setup
	unuse
	update
	use
```

#### morpheus remote add

```
Usage: morpheus remote add [name] [url]
    [name]                           The name for your appliance. eg. mymorph
    [url]                            The url of your appliance eg. https://morpheus.mycompany.com
        --use                        Make this the current appliance
    -d, --default                    Does the same thing as --use
        --secure                     Prevent insecure HTTPS communication.  This is enabled by default.
        --insecure                   Allow insecure HTTPS communication.  i.e. Ignore SSL errors.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This will add a new remote appliance to your morpheus client configuration.
If the new remote is your one and only, --use is automatically applied and
it will be made the current remote appliance.
This command will prompt you to login and/or setup a fresh appliance.
Prompting can be skipped with use of the --quiet option.
```

#### morpheus remote check

```
Usage: morpheus remote check [name]
    [name] is required. This is the name of the remote. Use 'current' to check the active appliance."
    -a, --all                        Refresh all appliances
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This can be used to refresh a remote appliance.
It makes an api request to the configured appliance url to check the status and version.
[name] is required. This is the name of the remote. Use 'current' to check the active appliance."
```

#### morpheus remote current

```
Usage: morpheus remote current
    -n, --name                       Print only the name.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print details about the current remote appliance.The default behavior is the same as 'remote get current'.
```

#### morpheus remote get

```
Usage: morpheus remote get [name]
    -j, --json                       JSON Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus remote list

```
Usage: morpheus remote list
    -a, --all                        Show all the appliance activity details
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This outputs a list of the configured remote appliances. It also indicates
the current appliance. The current appliance is where morpheus will send
its commands by default. That is, in absence of the '--remote' option.
```

#### morpheus remote remove

```
Usage: morpheus remote remove [name]
    -y, --yes                        Auto Confirm
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This will delete an appliance from your list.
```

#### morpheus remote setup

```
Usage: morpheus remote setup
    -O, --option OPTION              Option in the format -O field="value"
    -P, --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.

This can be used to initialize a new appliance.
You will be prompted to create the master account.
This is only available on a new, freshly installed, remote appliance.
```

#### morpheus remote unuse

```
Usage: morpheus remote unuse
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This clears the current remote appliance.
You will need to use an appliance, or pass the --remote option to your commands.
```

#### morpheus remote update

```
Usage: morpheus remote update [name]
        --url URL                    Update the url of your remote appliance
        --secure                     Prevent insecure HTTPS communication.  This is enabled by default
        --insecure                   Allow insecure HTTPS communication.  i.e. Ignore SSL errors.
        --use                        Make this the current appliance
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

This can be used to update remote appliance settings.
```

#### morpheus remote use

```
Usage: morpheus remote use [name]
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Make an appliance the current remote appliance.
This allows you to switch between your different appliances.
You may override this with the --remote option in your commands.
```


### morpheus roles

```
Usage: morpheus roles [command] [options]
Commands:
	add
	get
	list
	remove
	update
	update-blueprint-access
	update-cloud-access
	update-feature-access
	update-global-blueprint-access
	update-global-cloud-access
	update-global-group-access
	update-global-instance-type-access
	update-group-access
	update-instance-type-access
```

#### morpheus roles add

```
Usage: morpheus roles add [options]
        --authority VALUE            Name
        --description VALUE          Description (optional)
        --roleType VALUE             Role Type (optional) Default: user
        --baseRole VALUE             Copy From Role (optional)
        --multitenant on|off         Multitenant (optional) Default: off - A Multitenant role is automatically copied into all existing subaccounts as well as placed into a subaccount when created. Useful for providing a set of predefined roles a Customer can use
        --instanceLimits.maxStorage VALUE
                                     Max Storage (bytes) (optional)
        --instanceLimits.maxMemory VALUE
                                     Max Memory (bytes) (optional)
        --instanceLimits.maxCpu VALUE
                                     CPU Count (optional)
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus roles get

```
Usage: morpheus roles get [name]
    -f, --feature-access             Display Feature Access
    -g, --group-access               Display Group Access
    -c, --cloud-access               Display Cloud Access
    -i, --instance-type-access       Display Instance Type Access
    -b, --blueprint-access           Display Blueprint Access
    -a, --all-access                 Display All Access Lists
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a role.
[name] is required. This is the name or id of a role.
```

#### morpheus roles list

```
Usage: morpheus roles list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List roles.
```

#### morpheus roles remove

```
Usage: morpheus roles remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus roles update

```
Usage: morpheus roles update [name] [options]
        --authority VALUE            Name
        --description VALUE          Description (optional)
        --multitenant on|off         Multitenant (optional) Default: off - A Multitenant role is automatically copied into all existing subaccounts as well as placed into a subaccount when created. Useful for providing a set of predefined roles a Customer can use
        --instanceLimits.maxStorage VALUE
                                     Max Storage (bytes) (optional)
        --instanceLimits.maxMemory VALUE
                                     Max Memory (bytes) (optional)
        --instanceLimits.maxCpu VALUE
                                     CPU Count (optional)
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus roles update-blueprint-access

```
Usage: morpheus roles update-blueprint-access [name]
        --blueprint ID               Blueprint ID or Name
        --all                        Update all blueprints at once.
        --access VALUE               Access value [full|read|none]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update role access for an blueprint or all blueprints.
[name] is required. This is the name or id of a role.
--blueprint or --all is required. This is the name or id of a blueprint.
--access is required. This is the new access value.
```

#### morpheus roles update-cloud-access

```
Usage: morpheus roles update-cloud-access [name]
    -c, --cloud CLOUD                Cloud name or id
        --all                        Update all clouds at once.
        --access VALUE               Access value [full|read|none]
    -g, --group GROUP                Group to find cloud in
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update role access for a cloud or all clouds.
[name] is required. This is the name or id of a role.
--cloud or --all is required. This is the name or id of a cloud.
--access is required. This is the new access value.
```

#### morpheus roles update-feature-access

```
Usage: morpheus roles update-feature-access [name] [code] [full|read|user|yes|no|none]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus roles update-global-blueprint-access

```
Usage: morpheus roles update-global-blueprint-access [name] [full|custom|none]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus roles update-global-cloud-access

```
Usage: morpheus roles update-global-cloud-access [name] [full|custom|none]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus roles update-global-group-access

```
Usage: morpheus roles update-global-group-access [name] [code] [full|read|custom|none]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus roles update-global-instance-type-access

```
Usage: morpheus roles update-global-instance-type-access [name] [full|custom|none]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus roles update-group-access

```
Usage: morpheus roles update-group-access [name]
    -g, --group GROUP                Group name or id
        --all                        Update all groups at once.
        --access VALUE               Access value [full|read|none]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update role access for a group or all groups.
[name] is required. This is the name or id of a role.
--group or --all is required. This is the name or id of a group.
--access is required. This is the new access value.
```

#### morpheus roles update-instance-type-access

```
Usage: morpheus roles update-instance-type-access [name]
        --instance-type INSTANCE_TYPE
                                     Instance Type name
        --all                        Update all instance types at once.
        --access VALUE               Access value [full|read|none]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update role access for an instance type or all instance types.
[name] is required. This is the name or id of a role.
--instance-type or --all is required. This is the name of an instance type.
--access is required. This is the new access value.
```


### morpheus security-group-rules

```
Usage: morpheus security-group-rules [command] [options]
Commands:
	add-custom-rule
	add-instance-rule
	list
	remove
```

#### morpheus security-group-rules add-custom-rule

```
Usage: morpheus security-group-rules add-custom-rule SOURCE_CIDR PORT_RANGE PROTOCOL [options]
	SOURCE_CIDR: CIDR to white-list
	PORT_RANGE: Port value (i.e. 123) or port range (i.e. 1-65535)
	PROTOCOL: tcp, udp, icmp
    -s, --secgroup SECGROUP          Security Group ID (Use will use security as set with 'security-groups use id'
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus security-group-rules add-instance-rule

```
Usage: morpheus security-group-rules add_instance_rule SOURCE_CIDR INSTANCE_TYPE_ID [options]
	SOURCE_CIDR: CIDR to white-list
	INSTANCE_TYPE_ID: ID of the Instance Type to access
    -s, --secgroup secgroup          Security Group ID (Use will use security as set with 'security-groups use id'
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus security-group-rules list

```
Usage: morpheus security-group-rules list [id]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus security-group-rules remove

```
Usage: morpheus security-group-rules remove [id] [options]
    -s, --secgroup secgroup          Security Group ID (Use will use security as set with 'security-groups use id'
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus security-groups

```
Usage: morpheus security-groups [command] [options]
Commands:
	add
	get
	list
	remove
	unuse
	use
```

#### morpheus security-groups add

```
Usage: morpheus security-groups add [name] [options]
        --description Description    Description of the security group
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus security-groups get

```
Usage: morpheus security-groups get [id]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus security-groups list

```
Usage: morpheus security-groups list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus security-groups remove

```
Usage: morpheus security-groups remove [id]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus security-groups unuse

```
Usage: morpheus security-groups use [id] [--none]
        --none                       Do not use an active group.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus security-groups use

```
Usage: morpheus security-groups use [id] [--none]
        --none                       Do not use an active group.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus shell

```
Usage: morpheus shell
    -e, --exec EXPRESSION            Execute the command(s) expression and exit.
        --norc                       Do not read and execute the personal initialization script .morpheusrc
    -I, --insecure                   Allow for insecure HTTPS communication i.e. bad SSL certificate
    -Z, --incognito                  Incognito mode. Use a temporary shell. Remotes are loaded without without saved credentials or history logging.
    -C, --nocolor                    Disable ANSI coloring
    -V, --debug                      Print extra output for debugging.
    -B, --benchmark                  Print benchmark time after each command is finished, including shell itself.
    -h, --help                       Print this help
```


### morpheus storage-buckets

```
Usage: morpheus storage-buckets [command] [options]
Commands:
	add
	download
	get
	list
	list-files
	ls
	read
	remove
	remove-file
	rm
	update
	upload
```

#### morpheus storage-buckets add

```
Usage: morpheus storage-buckets add
        --name VALUE                 Name for this storage bucket
        --type code                  Storage Bucket Type Code
        --bucket-name VALUE          Bucket Name
        --default-backup-target [on|off]
                                     Default Backup Target
        --default-deployment-target [on|off]
                                     Default Deployment Target
        --default-virtual-image-target [on|off]
                                     Default Virtual Image Store
        --copy-to-store [on|off]     Archive Snapshots
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new storage bucket.
[name] is required and can be passed as --name instead.
```

#### morpheus storage-buckets download

```
Usage: morpheus storage-buckets download [provider:/path] [local-file]
    -f, --force                      Overwrite existing [local-file] if it exists.
    -p, --mkdir                      Create missing directories for [local-file] if they do not exist.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Download a file or directory.
[provider:/path] is required. This is the name or id of the provider and /path the file or folder to be downloaded.
[local-file] is required. This is the full local filepath for the downloaded file.
Directories will be downloaded as a .zip file, so you'll want to specify a [local-file] with a .zip extension.
```

#### morpheus storage-buckets get

```
Usage: morpheus storage-buckets get [storage-bucket]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a storage bucket.
[storage-bucket] is required. This is the name or id of a storage bucket.
```

#### morpheus storage-buckets list

```
Usage: morpheus storage-buckets list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List storage buckets.
```

#### morpheus storage-buckets list-files

```
Usage: morpheus storage-buckets list-files [provider:/path]
    -a, --all                        Show all files, including subdirectories under the /path.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List files in a storage bucket.
Include [/path] to show files under a directory.
```

#### morpheus storage-buckets ls

```
Usage: morpheus storage-buckets ls [bucket/path]
    -a, --all                        Show all files, including subdirectories under the /path.
    -l, --long                       Lists files in the long format, which contains lots of useful information, e.g. the exact size of the file, the file type, and when it was last modified.
    -H, --human                      Humanized file sizes. The default is just the number of bytes.
    -1, --oneline                    One file per line. The default delimiter is a single space.
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print filenames for a given location.
Pass storage location in the format bucket/path.
```

#### morpheus storage-buckets read

```
Usage: morpheus storage-buckets read [provider:/path]
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Print the contents of a storage file.
[provider:/path] is required. This is the name or id of the provider and /path the file or folder to be downloaded.
This confirmation can be skipped with the -y option.
```

#### morpheus storage-buckets remove

```
Usage: morpheus storage-buckets remove [storage-bucket]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a storage bucket.
[storage-bucket] is required. This is the name or id of a storage bucket.
```

#### morpheus storage-buckets remove-file

```
Usage: morpheus storage-buckets remove-file [provider:/path]
    -R, --recursive                  Delete a directory and all of its files. This must be passed if specifying a directory.
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a storage file or directory.
```

#### morpheus storage-buckets rm

```
Usage: morpheus storage-buckets remove-file [provider:/path]
    -R, --recursive                  Delete a directory and all of its files. This must be passed if specifying a directory.
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a storage file or directory.
```

#### morpheus storage-buckets update

```
Usage: morpheus storage-buckets update [storage-bucket] [options]
        --name VALUE                 Name for this storage bucket
        --type code                  Storage Bucket Type Code
        --bucket-name VALUE          Bucket Name
        --default-backup-target [on|off]
                                     Default Backup Target
        --default-deployment-target [on|off]
                                     Default Deployment Target
        --default-virtual-image-target [on|off]
                                     Default Virtual Image Store
        --copy-to-store [on|off]     Archive Snapshots
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a storage bucket.
[storage-bucket] is required. This is the id of a storage bucket.
```

#### morpheus storage-buckets upload

```
Usage: morpheus storage-buckets upload [local-file] [provider:/path]
    -R, --recursive                  Upload a directory and all of its files. This must be passed if [local-file] is a directory.
        --ignore-files PATTERN       Pattern of files to be ignored when uploading a directory.
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Upload a local file or folder to a storage bucket.
The first argument [local-file] should be the path of a local file or directory.
The second argument [provider:/path] should contain the name or id of the provider.
The [:/path] component is optional and can be used to specify the destination of the uploaded file or folder.
The default destination is the same name as the [local-file], under the root directory '/'.
This will overwrite any existing remote files that match the destination /path.
```


### morpheus tasks

```
Usage: morpheus tasks [command] [options]
Commands:
	add
	get
	list
	remove
	types
	update
```

#### morpheus tasks add

```
Usage: morpheus tasks add [name] -t TASK_TYPE
    -t, --type TASK_TYPE             Task Type
        --name NAME                  Task Name
        --file FILE                  File containing the script. This can be used instead of --O taskOptions.script
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus tasks get

```
Usage: morpheus tasks get [workflow]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus tasks list

```
Usage: morpheus tasks list
        --types x,y,z                Filter by task type code(s)
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus tasks remove

```
Usage: morpheus tasks remove [task]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
    -f, --force                      Force Delete
```

#### morpheus tasks types

```
Usage: morpheus tasks types
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus tasks update

```
Usage: morpheus tasks update [task] [options]
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus tenants

```
Usage: morpheus tenants [command] [options]
Commands:
	add
	count
	get
	groups
	list
	remove
	update
```

#### morpheus tenants add

```
Usage: morpheus tenants add [options]
        --name VALUE                 Name
        --description VALUE          Description (optional)
        --role VALUE                 Base Role (optional)
        --currency VALUE             Currency (optional)
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus tenants count

```
Usage: morpheus tenants count [options]
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get the number of tenants.
```

#### morpheus tenants get

```
Usage: morpheus tenants get [name]
    -j, --json                       JSON Output
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus tenants groups

```
Usage: morpheus tenants groups [command] [options]
Commands:
	add
	add-cloud
	get
	list
	remove
	remove-cloud
	update
```

#### morpheus tenants list

```
Usage: morpheus tenants list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List tenants (accounts).
```

#### morpheus tenants remove

```
Usage: morpheus tenants remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus tenants update

```
Usage: morpheus tenants update [name] [options]
        --active [on|off]            Can be used to disable a network
        --name VALUE                 Name
        --description VALUE          Description (optional)
        --role VALUE                 Base Role (optional)
        --currency VALUE             Currency (optional)
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus user-groups

```
Usage: morpheus user-groups [command] [options]
Commands:
	add
	add-user
	get
	list
	remove
	remove-user
	update
```

#### morpheus user-groups add

```
Usage: morpheus user-groups add [name]
        --name VALUE                 Name
        --description VALUE          Description
        --sudoUser [on|off]          Sudo Access
        --serverGroup VALUE          Server Group
        --users LIST                 Users to include in this group, comma separated list of IDs or usernames
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new user group.
[name] is required and can be passed as --name instead.
```

#### morpheus user-groups add-user

```
Usage: morpheus user-groups add-user [name] [user]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Add a user to a user group.
[name] is required. This is the name or id of a user group.
[user] is required. This is the username or id of a user. More than one can be passed.
```

#### morpheus user-groups get

```
Usage: morpheus user-groups get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus user-groups list

```
Usage: morpheus user-groups list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus user-groups remove

```
Usage: morpheus user-groups remove [name]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -y, --yes                        Auto Confirm
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus user-groups remove-user

```
Usage: morpheus user-groups remove-user [name] [user]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Remove a user from a user group.
[name] is required. This is the name or id of a user group.
[user] is required. This is the username or id of a user. More than one can be passed.
```

#### morpheus user-groups update

```
Usage: morpheus user-groups update [name]
        --name VALUE                 Name for this user group
        --description VALUE          Description
        --sudoUser [on|off]          Sudo Access. Default is off.
        --users LIST                 Users to include in this group, comma separated list of IDs or usernames
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a user group.
[name] is required. This is the name or id of a user group.
```


### morpheus user-settings

```
Usage: morpheus user-settings [command] [options]
Commands:
	clear-access-token
	get
	list-clients
	regenerate-access-token
	update
	update-avatar
	view-avatar
```

#### morpheus user-settings clear-access-token

```
Usage: morpheus user-settings clear-access-token [client-id]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Clear API access token for a specific client.
[client-id] is required. This is the id of an api client.
```

#### morpheus user-settings get

```
Usage: morpheus user-settings get
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get your user settings.
```

#### morpheus user-settings list-clients

```
Usage: morpheus user-settings list-clients
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List available api clients.
```

#### morpheus user-settings regenerate-access-token

```
Usage: morpheus user-settings regenerate-access-token [client-id]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Regenerate API access token for a specific client.
[client-id] is required. This is the id of an api client.
```

#### morpheus user-settings update

```
Usage: morpheus user-settings update [options]
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update your user settings.
```

#### morpheus user-settings update-avatar

```
Usage: morpheus user-settings update-avatar [file]
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update your avatar profile image.
[file] is required. This is the local path of a file to upload [png|jpg|svg].
```

#### morpheus user-settings view-avatar

```
Usage: morpheus user-settings view-avatar
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

View your avatar profile image.
This opens the avatar image url with a web browser.
```


### morpheus user-sources

```
Usage: morpheus user-sources [command] [options]
Commands:
	activate
	add
	deactivate
	get
	get-type
	list
	list-types
	remove
	update
	update-subdomain
```

#### morpheus user-sources activate

```
Usage: morpheus user-sources activate [name]
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Activate a user source.
[name] is required. This is the name or id of a user source.
```

#### morpheus user-sources add

```
Usage: morpheus user-sources add [account] [name]
        --account ID                 Account this user source belongs to
        --type CODE                  User Source Type
        --name VALUE                 Name for this user source
        --description VALUE          Description
        --role-mappings MAPPINGS     Role Mappings FQN in the format id1:FQN1,id2:FQN2
        --role-mapping-names MAPPINGS
                                     Role Mapping Names in the format id1:Name1,id2:Name2
        --default-role ID            Default Role ID
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a new user source.
[account] is required. This is the name or id of an account.
```

#### morpheus user-sources deactivate

```
Usage: morpheus user-sources deactivate [name]
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Deactivate a user source.
[name] is required. This is the name or id of a user source.
```

#### morpheus user-sources get

```
Usage: morpheus user-sources get [name]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about an user source.
[name] is required. This is the name or id of an user source.
```

#### morpheus user-sources get-type

```
Usage: morpheus user-sources get-type [type]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a user source type.
[type] is required. This is the type identifier.
```

#### morpheus user-sources list

```
Usage: morpheus user-sources list
        --account ID                 Filter by Tenant
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List user sources.
```

#### morpheus user-sources list-types

```
Usage: morpheus user-sources list-types
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List user source types.
```

#### morpheus user-sources remove

```
Usage: morpheus user-sources remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Delete a user_source.
```

#### morpheus user-sources update

```
Usage: morpheus user-sources update [name] [options]
        --name VALUE                 Name for this user source
        --description VALUE          Description
        --role-mappings MAPPINGS     Role Mappings in the format id1:FQN,id2:FQN2
        --role-mapping-names MAPPINGS
                                     Role Mapping Names in the format id1:Name1,id2:Name2
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a user source.
[name] is required. This is the name or id of a user source.
```

#### morpheus user-sources update-subdomain

```
Usage: morpheus user-sources update-subdomain [name]
        --subdomain VALUE            New subdomain for this user source
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update subdomain for a user source.
[name] is required. This is the name or id of a user source.
```


### morpheus users

```
Usage: morpheus users [command] [options]
Commands:
	add
	count
	get
	list
	passwd
	remove
	update
```

#### morpheus users add

```
Usage: morpheus users add [options]
        --firstName VALUE            First Name (optional)
        --lastName VALUE             Last Name (optional)
        --username VALUE             Username
        --email VALUE                Email
        --password VALUE             Password
        --passwordConfirmation VALUE Confirm Password
        --instanceLimits.maxStorage VALUE
                                     Max Storage (bytes) (optional)
        --instanceLimits.maxMemory VALUE
                                     Max Memory (bytes) (optional)
        --instanceLimits.maxCpu VALUE
                                     CPU Count (optional)
        --role VALUE                 Role (optional) - Role names (comma separated)
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -O, --option OPTION              Option in the format -O field="value"
    -P, --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus users count

```
Usage: morpheus users count [options]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get the number of users.
```

#### morpheus users get

```
Usage: morpheus users get [username]
    -f, --feature-access             Display Feature Access
        --all-access                 Display All Access Lists
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a user.
[username] is required. This is the username or id of a user.
```

#### morpheus users list

```
Usage: morpheus users list
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List users.
```

#### morpheus users passwd

```
Usage: morpheus users passwd [username] [options]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus users remove

```
Usage: morpheus users remove [username]
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus users update

```
Usage: morpheus users update [username] [options]
        --firstName VALUE            First Name (optional)
        --lastName VALUE             Last Name (optional)
        --username VALUE             Username (optional)
        --email VALUE                Email (optional)
        --password VALUE             Password (optional)
        --passwordConfirmation VALUE Confirm Password (optional)
        --instanceLimits.maxStorage VALUE
                                     Max Storage (bytes) (optional)
        --instanceLimits.maxMemory VALUE
                                     Max Memory (bytes) (optional)
        --instanceLimits.maxCpu VALUE
                                     CPU Count (optional)
        --role VALUE                 Role (optional) - Role names (comma separated)
    -a, --account ACCOUNT            Account Name
    -A, --account-id ID              Account ID
    -O, --option OPTION              Option in the format -O field="value"
    -P, --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus version

```
morpheus version
    -v, --short                      Print only the client version number
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus virtual-images

```
Usage: morpheus virtual-images [command] [options]
Commands:
	add
	add-file
	get
	list
	remove
	remove-file
	types
	update
```

#### morpheus virtual-images add

```
Usage: morpheus virtual-images add [name] -t TYPE
    -t, --type TYPE                  Virtual Image Type
        --filename NAME              Image File Name. Specify a name for the uploaded file.
        --url URL                    Image File URL. This can be used instead of uploading local files.
        --tenants LIST               Tenant Access, comma separated list of account IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Create a virtual image.
```

#### morpheus virtual-images add-file

```
Usage: morpheus virtual-images add-file [name] [filepath]
        --filename FILENAME          Filename for uploaded file. Derived from [filepath] by default.
        --url URL                    Image File URL. This can be used instead of [filepath]
        --gzip                       Compress uploaded file
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Upload a virtual image file.
[name] is required. This is the name or id of a virtual image.
[filepath] or --url is required. This is location of the virtual image file.
```

#### morpheus virtual-images get

```
Usage: morpheus virtual-images get [name]
        --details                    Show more details.
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Get details about a virtual image.
[name] is required. This is the name or id of a virtual image.
```

#### morpheus virtual-images list

```
Usage: morpheus virtual-images list
    -t, --type IMAGE_TYPE            Image Type
        --all                        All Images
        --user                       User Images
        --system                     System Images
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

List virtual images.
```

#### morpheus virtual-images remove

```
Usage: morpheus virtual-images remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus virtual-images remove-file

```
Usage: morpheus virtual-images remove-file [name] [filename]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus virtual-images types

```
Usage: morpheus virtual-images types
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus virtual-images update

```
Usage: morpheus virtual-images update [name] [options]
        --tenants LIST               Tenant Access, comma separated list of account IDs
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help

Update a virtual image.
[name] is required. This is the name or id of a virtual image.
```


### morpheus whoami

```
Usage: morpheus whoami [options]
    -n, --name                       Print only your username.
    -f, --feature-access             Display Feature Access
    -t, --token-only                 Print your access token only
    -j, --json                       JSON Output
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


### morpheus workflows

```
Usage: morpheus workflows [command] [options]
Commands:
	add
	get
	list
	remove
	update
```

#### morpheus workflows add

```
Usage: morpheus workflows add [name] --tasks taskId:phase,taskId2:phase,taskId3:phase
        --name NAME                  Name for workflow
        --tasks x,y,z                List of tasks to run in order, in the format <Task ID>:<Task Phase> Task Phase is optional, the default is 'provision'.
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus workflows get

```
Usage: morpheus workflows get [workflow]
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus workflows list

```
Usage: morpheus workflows list
    -m, --max MAX                    Max Results
    -o, --offset OFFSET              Offset Results
    -s, --search PHRASE              Search Phrase
    -S, --sort ORDER                 Sort Order
    -D, --desc                       Reverse Sort Order
    -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
    -j, --json                       JSON Output
        --yaml                       YAML Output
        --csv                        CSV Output
        --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
        --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
        --csv-quotes                 Wrap CSV values with ". Default: false
        --csv-no-header              Exclude header for CSV Output.
    -F, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields.
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus workflows remove

```
Usage: morpheus workflows remove [name]
    -y, --yes                        Auto Confirm
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```

#### morpheus workflows update

```
Usage: morpheus workflows update [name] --tasks taskId:phase,taskId2:phase,taskId3:phase
        --tasks x,y,z                New list of tasks to run in the format <Task ID>:<Phase>. Phase is optional, the default is 'provision'.
        --name NAME                  New name for workflow
    -O, --option OPTION              Option in the format -O field="value"
        --prompt                     Always prompts. Use passed options as the default value.
    -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        --payload FILE               Payload from a local JSON or YAML file, skip all prompting
        --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
        --payload-json JSON          Payload JSON, skip all prompting
        --payload-yaml YAML          Payload YAML, skip all prompting
    -j, --json                       JSON Output
    -d, --dry-run                    Dry Run, print the API request instead of executing it
        --curl                       Dry Run to output API request as a curl command.
        --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
    -q, --quiet                      No Output, do not print to stdout
    -r, --remote REMOTE              Remote name. The current remote is used by default.
        --remote-url URL             Remote url. The current remote url is used by default.
    -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
    -U, --username USERNAME          Username for authentication.
    -P, --password PASSWORD          Password for authentication.
    -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
    -H, --header HEADER              Additional HTTP header to include with requests.
        --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
    -C, --nocolor                    Disable ANSI coloring
    -B, --benchmark                  Print benchmark time after the command is finished.
    -V, --debug                      Print extra output for debugging.
    -h, --help                       Print this help
```


## ENVIRONMENT VARIABLES

Morpheus has only one environment variable that it uses.

### MORPHEUS_CLI_HOME

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
==================

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

## CONFIGURATION

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
