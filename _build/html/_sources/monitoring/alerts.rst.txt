Alerts
======

There are several ways to configure alerts and notifications within |morpheus| . Users can be notified via Email or SMS as well as several other direct integrations. These integrations include PagerDuty, Alert Ops, Victor Ops, and even Slack chat Channel notifications (or optionally via the ServiceNow integration).

Contacts
--------

To configure user notifications a contact must first be created in `Monitoring -> Contacts`. These contacts can be one of a few types:

* *Contact*: Used for either Email or SMS
* *Web Hook*: Used for posting a notification to a web endpoint or Alert Ops.
* *Slack Hook*: Used for posting notifications to a https://slack.com/[Slack] channel.
* *VictorOps*: Provides a web post format consistent with the required notification format for Victor Ops.

Most of these options provide convenient examples and information when configuring the contact. Once they are configured contacts can freely be used to build `Alert Rules`.

Alert Rules
-----------

Alert Rules provide a powerful means to configure who gets notified in various scenarios. These scenarios include targetting specific checks, groups, or apps , and adding the appropriate recipients to be notified during a situation in which those filters are impacted.

* *Min Duration*: This setting delays notification to the recipients by the entered number of minutes required for the incident to be opened.
* *Min Severity*: Some executives might want to be notified of an outage but only if the severity impact goes above a certain level. This is very useful for scoping escalations.

To add recipients to a rule just start typing their name in the Recipients section towards the button of the edit form. An auto-complete list will start populating with contact names. Once one is selected a delivery method can be selected as well as whether or not they should be notified of any escalation changes and/or closed incidents.

.. TIP:: A recipient can be in multiple alert rules and can even be configured to be notified via different methods depending on the rule. A useful example might be to alert someone via email for lower severity incidents but SMS for critical severity levels.

Notifications
-------------

Configuring Notification Services

By default |morpheus| provides email notification services using the `morpheusdata.com` email address. It may be advisable to customize these services to use another mail delivery service.

.. T ODO We need to make this stick
