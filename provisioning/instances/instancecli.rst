morpheus instances
~~~~~~~~~~~~~~~~~~

::

    Usage: morpheus instances [command] [options]
    Commands:
        action
        actions
        add
        apply-security-groups
        backup
        backups
        cancel-removal
        clone
        console
        containers
        count
        delenv
        eject
        envs
        exec
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
        update-wiki
        view
        wiki

morpheus instances action
^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances action [id list] -a CODE
        -a, --action CODE                Instance Action CODE to execute
        -y, --yes                        Auto Confirm
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -q, --quiet                      No Output, do not print to stdout
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Execute an action for one or many instances.

morpheus instances actions
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances actions [id or name list]
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    List the actions available to specified instance(s).

morpheus instances add
^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances add [name] -c CLOUD -t TYPE
        -g, --group GROUP                Group Name or ID
        -c, --cloud CLOUD                Cloud Name or ID
        -t, --type CODE                  Instance Type
            --name NAME                  Instance Name
            --description [TEXT]         Description
            --environment ENV            Environment code
            --metadata LIST              Metadata tags in the format 'name:value, name:value'
            --labels LIST                Labels (keywords) in the format 'foo, bar'
            --copies NUMBER              Number of copies to provision
            --layout-size NUMBER         Apply a multiply factor of containers/vms within the instance
        -l, --layout LAYOUT              Layout ID
        -p, --plan PLAN                  Service plan ID
            --resource-pool ID           Resource pool ID
            --workflow ID                Automation: Workflow ID
            --ports ARRAY                Exposed Ports, JSON formatted list of objects containing name and port
            --create-user on|off         User Config: Create Your User. Default is on
            --user-group USERGROUP       User Config: User Group
            --shutdown-days DAYS         Automation: Shutdown Days
            --expire-days DAYS           Automation: Expiration Days
            --create-backup [on|off]     Automation: Create Backups.
            --security-groups LIST       Security Groups, comma sepearated list of security group IDs
            --refresh [SECONDS]          Refresh until status is running,failed. Default interval is 30 seconds.
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
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -q, --quiet                      No Output, do not print to stdout
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Create a new instance.
    [name] is required. This is the new instance name.
    The available options vary by --type.

morpheus instances apply-security-groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances apply-security-groups [instance] [-S] [-c]
        -S, --secgroups SECGROUPS        Apply the specified comma separated security group ids
        -c, --clear                      Clear all security groups
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -q, --quiet                      No Output, do not print to stdout
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances backup
^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances backup [instance]
        -y, --yes                        Auto Confirm
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances backups
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances backups [instance]
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances cancel-removal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances cancel-removal [instance]
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -q, --quiet                      No Output, do not print to stdout
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances clone
^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances clone [instance] -g GROUP
            --name VALUE                 Name
        -g, --group GROUP                Group Name or ID for the new instance
        -c, --cloud CLOUD                Cloud Name or ID for the new instance
            --create-user on|off         User Config: Create Your User. Default is on
        -O, --option OPTION              Option in the format -O field="value"
            --prompt                     Always prompts. Use passed options as the default value.
        -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
            --payload FILE               Payload from a local JSON or YAML file, skip all prompting
            --payload-dir DIRECTORY      Payload from a local directory containing 1-N JSON or YAML files, skip all prompting
            --payload-json JSON          Payload JSON, skip all prompting
            --payload-yaml YAML          Payload YAML, skip all prompting
        -y, --yes                        Auto Confirm
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances console
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances console [instance]
        -n, --node NODE_ID               Scope console to specific Container or VM
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances containers [instance]
        -j, --json                       JSON Output
            --yaml                       YAML Output
            --csv                        CSV Output
            --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
            --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
            --csv-quotes                 Wrap CSV values with ". Default: false
            --csv-no-header              Exclude header for CSV Output.
        -f, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields for json,csv,yaml.
            --all-fields                 Show all fields present in the data.
            --wrap                       Wrap table columns instead hiding them when terminal is not wide enough.
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances count
^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances count [options]
        -g, --group GROUP                Group Name or ID
        -c, --cloud CLOUD                Cloud Name or ID
            --host HOST                  Host Name or ID
            --owner USER                 Owner Username or ID
        -s, --search PHRASE              Search Phrase
        -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
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
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Get the number of instances.

morpheus instances delenv
^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances delenv [instance] VAR
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances eject
^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances eject [instance]
        -y, --yes                        Auto Confirm
        -q, --quiet                      No Output, do not print to stdout
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Eject an instance.
    [instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.

morpheus instances envs
^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances envs [instance]
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances exec
^^^^^^^^^^^^^^^^^^^^^^^

::

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
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Execute an arbitrary script or command on an instance.
    [id] is required. This is the id or name of an instance.
    [script] is required. This is the script that is to be executed.

morpheus instances get
^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances get [instance]
        -a, --all                        Display all details: containers|vms, and scaling.
            --containers                 Display Instance Containers
            --nodes                      Alias for --containers
            --vms                        Alias for --containers
            --scaling                    Display Instance Scaling Settings
            --refresh [SECONDS]          Refresh until status is running,failed. Default interval is 30 seconds.
            --refresh-until STATUS       Refresh until a specified status is reached.
        -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        -j, --json                       JSON Output
            --yaml                       YAML Output
            --csv                        CSV Output
            --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
            --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
            --csv-quotes                 Wrap CSV values with ". Default: false
            --csv-no-header              Exclude header for CSV Output.
        -f, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields for json,csv,yaml.
            --all-fields                 Show all fields present in the data.
            --wrap                       Wrap table columns instead hiding them when terminal is not wide enough.
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Get details about an instance.
    [instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.

morpheus instances history
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances history [instance]
            --events                     Display sub processes (events).
            --output                     Display process output.
            --details                    Display more details: memory and storage usage used / max values.
            --process-id ID              Display details about a specfic process only.
            --event-id ID                Display details about a specfic process event only.
        -m, --max MAX                    Max Results
        -o, --offset OFFSET              Offset Results
        -s, --search PHRASE              Search Phrase
        -S, --sort ORDER                 Sort Order. DIRECTION may be included as "ORDER [asc|desc]".
        -D, --desc                       Reverse Sort Order
        -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        -j, --json                       JSON Output
            --yaml                       YAML Output
            --csv                        CSV Output
            --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
            --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
            --csv-quotes                 Wrap CSV values with ". Default: false
            --csv-no-header              Exclude header for CSV Output.
        -f, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields for json,csv,yaml.
            --all-fields                 Show all fields present in the data.
            --wrap                       Wrap table columns instead hiding them when terminal is not wide enough.
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    List historical processes for a specific instance.
    [instance] is required. This is the name or id of an instance.

morpheus instances history-details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances history-details [instance] [process-id]
        -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        -j, --json                       JSON Output
            --yaml                       YAML Output
            --csv                        CSV Output
            --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
            --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
            --csv-quotes                 Wrap CSV values with ". Default: false
            --csv-no-header              Exclude header for CSV Output.
        -f, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields for json,csv,yaml.
            --all-fields                 Show all fields present in the data.
            --wrap                       Wrap table columns instead hiding them when terminal is not wide enough.
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Display history details for a specific process.
    [instance] is required. This is the name or id of an instance.
    [process-id] is required. This is the id of the process.

morpheus instances history-event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances history-event [instance] [event-id]
        -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        -j, --json                       JSON Output
            --yaml                       YAML Output
            --csv                        CSV Output
            --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
            --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
            --csv-quotes                 Wrap CSV values with ". Default: false
            --csv-no-header              Exclude header for CSV Output.
        -f, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields for json,csv,yaml.
            --all-fields                 Show all fields present in the data.
            --wrap                       Wrap table columns instead hiding them when terminal is not wide enough.
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Display history details for a specific process event.
    [instance] is required. This is the name or id of an instance.
    [event-id] is required. This is the id of the process event.

morpheus instances import-snapshot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances import-snapshot [instance]
            --storage-provider ID        Optional storage provider
        -y, --yes                        Auto Confirm
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances list
^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances list
        -g, --group GROUP                Group Name or ID
        -c, --cloud CLOUD                Cloud Name or ID
            --host HOST                  Host Name or ID
            --owner USER                 Owner Username or ID
            --details                    Display more details: memory and storage usage used / max values.
            --status STATUS              Filter by status i.e. provisioning,running,starting,stopping
            --pending-removal            Include instances pending removal.
            --pending-removal-only       Only instances pending removal.
        -m, --max MAX                    Max Results
        -o, --offset OFFSET              Offset Results
        -s, --search PHRASE              Search Phrase
        -S, --sort ORDER                 Sort Order. DIRECTION may be included as "ORDER [asc|desc]".
        -D, --desc                       Reverse Sort Order
        -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        -j, --json                       JSON Output
            --yaml                       YAML Output
            --csv                        CSV Output
            --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
            --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
            --csv-quotes                 Wrap CSV values with ". Default: false
            --csv-no-header              Exclude header for CSV Output.
        -f, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields for json,csv,yaml.
            --all-fields                 Show all fields present in the data.
            --wrap                       Wrap table columns instead hiding them when terminal is not wide enough.
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    List instances.

morpheus instances logs
^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances logs [instance]
        -n, --node NODE_ID               Scope logs to specific Container or VM
            --start TIMESTAMP            Start timestamp. Default is 30 days ago.
            --end TIMESTAMP              End timestamp. Default is now.
            --level VALUE                Log Level. DEBUG,INFO,WARN,ERROR
            --table                      Format ouput as a table.
        -a, --all                        Display all details: entire message.
        -m, --max MAX                    Max Results
        -o, --offset OFFSET              Offset Results
        -s, --search PHRASE              Search Phrase
        -S, --sort ORDER                 Sort Order. DIRECTION may be included as "ORDER [asc|desc]".
        -D, --desc                       Reverse Sort Order
        -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        -j, --json                       JSON Output
            --yaml                       YAML Output
            --csv                        CSV Output
            --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
            --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
            --csv-quotes                 Wrap CSV values with ". Default: false
            --csv-no-header              Exclude header for CSV Output.
        -f, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields for json,csv,yaml.
            --all-fields                 Show all fields present in the data.
            --wrap                       Wrap table columns instead hiding them when terminal is not wide enough.
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances remove
^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances remove [instance]
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
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances resize
^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances resize [instance]
        -O, --option OPTION              Option in the format -O field="value"
            --prompt                     Always prompts. Use passed options as the default value.
        -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances restart
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances restart [instance]
            --mute-monitoring [on|off]   Mute monitoring. Default is on.
        -y, --yes                        Auto Confirm
        -q, --quiet                      No Output, do not print to stdout
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Restart an instance.
    [instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.

morpheus instances restart-service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances restart-service [instance]
            --mute-monitoring [on|off]   Mute monitoring. Default is on.
        -y, --yes                        Auto Confirm
        -q, --quiet                      No Output, do not print to stdout
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Restart service on an instance.
    [instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.

morpheus instances run-workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances run-workflow [instance] [workflow] [options]
        -O, --option OPTION              Option in the format -O field="value"
            --prompt                     Always prompts. Use passed options as the default value.
        -N, --no-prompt                  Skip prompts. Use default values for all optional fields.
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances scaling
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances scaling [instance]
        -Q, --query PARAMS               Query parameters. PARAMS format is 'phrase=foobar&category=web'
        -j, --json                       JSON Output
            --yaml                       YAML Output
            --csv                        CSV Output
            --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
            --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
            --csv-quotes                 Wrap CSV values with ". Default: false
            --csv-no-header              Exclude header for CSV Output.
        -f, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields for json,csv,yaml.
            --all-fields                 Show all fields present in the data.
            --wrap                       Wrap table columns instead hiding them when terminal is not wide enough.
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Show scaling threshold information for an instance.

morpheus instances scaling-update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances scaling-update [instance]
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
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Update scaling threshold information for an instance.

morpheus instances security-groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances security-groups [instance]
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances setenv
^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances setenv [instance] VAR VALUE [-e]
        -e                               Exportable
        -M                               Masked
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -q, --quiet                      No Output, do not print to stdout
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances start
^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances start [instance]
        -y, --yes                        Auto Confirm
        -q, --quiet                      No Output, do not print to stdout
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Start an instance.
    [instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.

morpheus instances start-service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances start-service [instance]
        -y, --yes                        Auto Confirm
        -q, --quiet                      No Output, do not print to stdout
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Start service on an instance.
    [instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.

morpheus instances stats
^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances stats [instance]
        -j, --json                       JSON Output
            --yaml                       YAML Output
            --csv                        CSV Output
            --csv-delim CHAR             Delimiter for CSV Output values. Default: ','
            --csv-newline [CHAR]         Delimiter for CSV Output rows. Default: '\n'
            --csv-quotes                 Wrap CSV values with ". Default: false
            --csv-no-header              Exclude header for CSV Output.
        -f, --fields x,y,z               Filter Output to a limited set of fields. Default is all fields for json,csv,yaml.
            --all-fields                 Show all fields present in the data.
            --wrap                       Wrap table columns instead hiding them when terminal is not wide enough.
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances status-check
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances status-check [instance]
        -q, --quiet                      No Output, do not print to stdout
        -j, --json                       JSON Output
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances stop
^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances stop [instance]
            --mute-monitoring [on|off]   Mute monitoring. Default is off.
        -y, --yes                        Auto Confirm
        -q, --quiet                      No Output, do not print to stdout
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Stop an instance.
    [instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.

morpheus instances stop-service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances stop-service [instance]
            --mute-monitoring [on|off]   Mute monitoring. Default is off.
        -y, --yes                        Auto Confirm
        -q, --quiet                      No Output, do not print to stdout
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Stop service on an instance.
    [instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.

morpheus instances suspend
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances suspend [instance]
            --mute-monitoring [on|off]   Mute monitoring. Default is on.
            --server [on|off]            Suspend instance server. Default is off.
        -y, --yes                        Auto Confirm
        -q, --quiet                      No Output, do not print to stdout
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    Suspend an instance.
    [instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.

morpheus instances update
^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances update [instance]
            --name VALUE                 Name
            --description VALUE          Description
            --environment VALUE          Environment
            --group GROUP                Group Name or ID
            --metadata LIST              Metadata tags in the format 'name:value, name:value'
            --labels LIST                Labels (keywords) in the format 'foo, bar'
            --power-schedule-type ID     Power Schedule Type ID
            --owner USER                 Owner Username or ID
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
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances update-wiki
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances update-wiki [instance] [options]
            --name VALUE                 Name (optional) - The name of the wiki page for this instance. Default is the instance name.
            --content VALUE              Content (optional) - The content (markdown) of the wiki page.
            --file FILE                  File containing the wiki content. This can be used instead of --content
            --clear                      Clear current page content
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
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

morpheus instances view
^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances view [instance]
        -w, --wiki                       Open the wiki tab for this instance
            --tab VALUE                  Open a specific tab
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    View an instance in a web browser
    [instance] is required. This is the name or id of an instance. Supports 1-N [instance] arguments.

morpheus instances wiki
^^^^^^^^^^^^^^^^^^^^^^^

::

    Usage: morpheus instances wiki [instance]
            --view                       View wiki page in web browser.
        -j, --json                       JSON Output
        -d, --dry-run                    Dry Run, print the API request instead of executing it
            --curl                       Dry Run to output API request as a curl command.
            --scrub                      Mask secrets in output, such as the Authorization header. For use with --curl and --dry-run.
        -r, --remote REMOTE              Remote name. The current remote is used by default.
            --remote-url URL             Remote url. This allows adhoc requests instead of using a configured remote.
        -T, --token TOKEN                Access token for authentication with --remote. Saved credentials are used by default.
        -U, --username USERNAME          Username for authentication.
        -P, --password PASSWORD          Password for authentication.
        -I, --insecure                   Allow insecure HTTPS communication.  i.e. bad SSL certificate.
        -H, --header HEADER              Additional HTTP header to include with requests.
            --timeout SECONDS            Timeout for api requests. Default is typically 30 seconds.
        -C, --nocolor                    Disable ANSI coloring
        -B, --benchmark                  Print benchmark time and exit/error after the command is finished.
        -V, --debug                      Print extra output for debugging.
        -h, --help                       Print this help

    View wiki page details for an instance.
    [instance] is required. This is the name or id of an instance.

