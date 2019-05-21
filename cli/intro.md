## Installation

The morpheus cli is a ruby based cli that provides a lot of functionality out of the box and is rapidly growing in coverage to be able to perform every task that can be performed in the morpheus UI. It is also a great way to get started in exploring the morpheus API and understanding some of the data model aspects.

### Linux

A Prerequisite to running the CLI is to have ruby 2.0.0+ installed (2.5 or greater recommended). Once the ruby runtime is installed simply use rubygems to install the cli `gem install morpheus-cli`. Once the gem is installed all cli commands can be run on the shell via `morpheus`.

Add this line to your application's Gemfile:

    gem 'morpheus-cli'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install morpheus-cli

### Windows

The morpheus cli is capable of running on many platforms due to its ruby runtime. This includes windows based platforms. To get started, we must first ensure ruby is running on the windows machine in question. To do this please visit [http://rubyinstaller.org/downloads](http://rubyinstaller.org/downloads) and download at least Ruby version 2.0.0 (2.3.3 recommended).

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

## Contributing

1. Fork it ( https://github.com/[my-github-username]/morpheus-cli/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
