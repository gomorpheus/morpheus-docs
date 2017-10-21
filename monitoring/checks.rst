Checks
======

The Monitoring system is composed of individual checks. A check is created for every container or vm that is provisioned through |morpheus| . One interesting thing about these checks is they are type aware. There are several different built in check types that are selected based on the service or instance type that is being provisioned. These range from database type checks to web checks and message checks. They are highly configurable and also feature fallback check types for those more generic use cases.

Checks can be customized to run custom queries, check queue sizes, or even adjust severity levels and check intervals. All of these things can be controlled from the Checks sub tab within Monitoring.

Health
------

A check can have 3 health states. They are Failed, Warning (Recovering), and Healthy. When a check test fails the system automatically reattempts the check after 30 seconds to eliminate false positives. This will convert the check into a `Failed` state and raise the appropriate severity incident depending on the grouping of the check. When a check recovers it automatically goes into a Warning state. This will remain in the warning state until 10 successful check runs have completed.

Options
-------

All check types have several core options and some of these default options can be configured in `Admin -> Monitoring`. This includes the default check interval time. By default a check is run every 5 minutes. This can however be changed to run as frequently as once every minute.

* *Max Severity*: The maximum severity level impact for a created incident that can occur if the check fails (defaults to Critical).
* *Check Interval*: The frequency with which a check is run (default 5 minutes).
* *Affects Availability*: Whether or not this check impacts overall system availability calculations.


SSH Tunneling
-------------

In many cases when it comes to monitoring databases, and services they may not be fronted on the public ips for external monitoring. To reach these safely, and securely |morpheus| provides an SSH Tunneling mechanism for its check servers. This allows the check to be confirmed via an ssh port tunnel securely using a keypair.

Check Servers
-------------

On a base installation of |morpheus| a single `check server` is installed on the appliance. This is used for running any custom user checks. This services connects to the provided rabbitmq services and can be moved off or even scaled horizontally onto sets of check servers. All other checks that are related to provisioned containers or vms are executed by the installed agent on the guest OS or Docker host.
