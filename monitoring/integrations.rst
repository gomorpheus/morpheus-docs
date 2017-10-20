Monitoring Integrations
=======================

While |morpheus| provides a fantastic means for determining uptime and availability of both services and vms sometimes more is needed. A good example of this is performance application monitoring. To solve this several external integrations are provided out of the box. Even some external integrations with regards to incident management are provided.

AppDynamics
-----------

AppDynamics is a very powerful performance and application monitoring tool. It features advanced correlation features and profiling capabilities for a very wide range of application platforms including native Docker support. Due to the level of capabilities of AppDyanmics there are more required settings to integrate it with |morpheus| . To get started expand the section in `Admin -> Monitoring` related to AppDynamics and toggle it to Enabled. There are several fields here that need filled out. Once completed hit save and all hosts will automatically be configured to install the AppDynamics agent.

AppDynamics is capable of bein run as a paid SaaS based service as well as an on premise installation and |morpheus| supports both configurations. Most input fields related to connecting to AppDynamics provide helpful tips as to what information exactly needs provided and where to acquire it.

NewRelic
--------

New Relic is a very popular service based performance monitoring tool. It supports a wide variety of application platforms and is a breeze to configure with |morpheus| . Another great feature of new relic is its ability to monitor the server applications run on and provide additional stats. To do this an agent needs to be installed and configured on each server. Fortunately, this is performed automatically for every vm and docker host provisioned within |morpheus| . To turn on the integration simply go to `Admin -> Monitoring` and expand the section titled "New Relic". There it is simply a matter of toggling the Enabled setting to on and entering the New Relic account API Key.

Service Now
-----------

Service now integration is provided out of the box with |morpheus| . To add a service now integration simply visit the 'Monitoring Settings' section in `Admin -> Monitoring`. This allows one to map incident severity levels to equivalent severities in ServiceNow.

To enable service now simply expand the section labelled "ServiceNow" in `Admin -> Monitoring`. Toggle the enabled flag and enter the `Host`, `User`, and `Password` information required to connect to ServiceNow. The other options below include behaviors upon new incidents being opened and old incidents closing. It also includes a table for mapping |morpheus| incident serverity levels to their ServiceNow counterparts.

There are several other useful service now integrations planned for future releases and will be discussed as those features come out.
