#Shell

The CLI provides a command called **shell** that allows you enter an interactive shell.

This is a convenient way to test things out quickly, and to avoid prefixing your commands with `morpheus `

## Open a shell

```bash
morpheus shell
```

Now you may run all the available commands like so:

```bash
morpheus> remote use qa
morpheus> login
morpheus> clouds list
```

To see the list of all available commands, use `help`

```bash
morpheus> help
```

**TAB** can be used to auto-complete the name of a command or any aliases you've defined.

**CTRL + R** can be used to search for available commands and previously executed commands.

The **↑** and **↓** arrow keys can be used to navigate through the shell history.

To see a list of all the commands you've executed in a shell, use `history`

```bash
morpheus> history
Last 4 commands
  1  flush-history
  2  groups list
  3  clouds list
  4  instances list
```

Historical commands can be executed by prefixing the command number with `!`
```bash
morpheus> !2
```

And again, just like bash, you can re-execute the last command with `!!`
```bash
morpheus> !!
```

The `flush-history` command can be used to delete the shell history.


It is possible to execute multiple commands sequentially inside a shell, like this:

```bash
morpheus> instances stats 7; instances stats 8; instances stats 9
```

You may define an [Alias](Alias) within a shell, which will persist through subsequent shells.

```bash
morpheus shell
morpheus> alias restart-711='instances restart "My Test Instance"'
morpheus> restart-711
morpheus> exit
morpheus shell
morpheus> restart-711
```

To exit a shell, use `exit`
```bash
morpheus> exit
```
