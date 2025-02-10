Checks
======

The Monitoring system is composed of individual checks. A check is created for every container or vm that is provisioned through |morpheus| . One interesting thing about these checks is they are type aware. There are several different built in check types that are selected based on the service or instance type that is being provisioned. These range from database type checks to web checks and message checks. They are highly configurable and also feature fallback check types for those more generic use cases.

Checks can be customized to run custom queries, check queue sizes, or even adjust severity levels and check intervals. All of these things can be controlled from the Checks sub tab within Monitoring.

Health
------

A Check can have four health states. They are Happy, Sad, Warning, and Unknown. Checks can also be muted in which case they are effectively disabled and are not actively run to gather an updated health state. The default view shows Checks in all health states but this view can be filtered to show just one health state. When a Check test fails the system automatically reattempts the check after 30 seconds to eliminate false positives. This will convert the check into a Sad state and raise the appropriate severity incident depending on the grouping of the check. When a check recovers, it automatically goes into a Warning state. The warning state will remain until 10 successful Check runs have completed.

Options
-------

All check types have several core options and some of these default options can be configured in `Admin > Monitoring`. This includes the default check interval time. By default a check is run every 5 minutes. This can however be changed to run as frequently as once every minute.

* *Max Severity*: The maximum severity level impact for a created incident that can occur if the check fails (defaults to Critical).
* *Check Interval*: The frequency with which a check is run (default 5 minutes).
* *Affects Availability*: Whether or not this check impacts overall system availability calculations.


SSH Tunneling
-------------

In many cases when it comes to monitoring databases, and services they may not be fronted on the public ip's for external monitoring. To reach these safely, and securely |morpheus| provides an SSH Tunneling mechanism for its check servers. This allows the check to be confirmed via an ssh port tunnel securely using a keypair.

Check Servers
-------------

On a base installation of |morpheus| a single `check server` is installed on the appliance. This is used for running any custom user checks. This service connects to the provided rabbitmq services and can be moved off or even scaled horizontally onto sets of check servers. All other checks that are related to provisioned containers or VMs are executed by the installed agent on the guest OS or Docker host.

Check types
-----------

Web Check
^^^^^^^^^^

A web check is useful to identify if a url is reachable and the text to match check criteria confirms if the website is loading with the expected values. The text to match character should be within the first few lines of the page source.

  Use case:
    Adding a check to make sure morpheus demo environment is functioning. The below check will login to the morpheus UI and look for a text Morpheus on the dashboard page.
      Values to be added in Check:
        * Name: "<enter name>"
        * Type: Web Check
        * Interval: 5 mins (Select an interval)
        * Max severity: Critical
        * Check the box for affects availability
        * Web Url: https://demo.morpheusdata.com/operations/dashboard (Note: this page will load only if my login is successful. Enter the login details in Username and password fields)
        * Request Method: GET
        * Basic Authentication:
          * User: <username>
          * Password: <password>
        * Text to Match: "Morpheus" (Login to the url and on the page of dashboard, right click and select view page source. In the forst few lines, look for a text that you want this check to verify)
        * Save Changes

Push API Check
^^^^^^^^^^^^^^^

This check can be used to send an API call to morpheus from a platform to check if the push api is working.
A push Check is not polled regularly by the standard monitoring system. Instead it is expected that an external API push updates as to the status of the check timed closely with the configured check interval setting. This is used to throttle the push from performing too many status updates.

.. NOTE:: If a check is not heard from within the check intervals, It's status will be updated to error and an incident will be raised as if it failed.

Use Case:
  Send an API call from an app to make sure the API is not cluttered and can send checks in a 2 mins interval.
    Values to be added to the check:
      * Name: "<enter name>"
      * Type: "Push API Check"
      * Interval: 5 mins (Select an interval)
      * Max severity: Critical
      * Check the box for affects availability
      * Copy the curl command are schedule to send this via your API. For testing we used postman to send the api call at an interval of 4 mins.
      * Save Changes

MySQL Check
^^^^^^^^^^^^

This check is used to run a query on a host running mysql.

  Use Case:
    Query localhost running mysql to query a table to check if there is any status as requested. If the status has a count of 1 then the check would pass else mark it as critical.
      Values to be added to the check:
        * Name: "<enter name>"
        * Type: "MySQL Check"
        * Interval: 5 mins (Select an interval)
        * Check the box for affects availability
        * Host: 127.0.0.1
        * Port: 3306
        * DB Name: morpheus
        * User: <db user name>
        * Password: <password>
        * Query: "select count(*) as count from request_reference where status = 'requested';"
        * Operator: Equal
        * Check results: 1
        * Save Changes
