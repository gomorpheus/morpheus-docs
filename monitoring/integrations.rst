Monitoring Integrations
=======================

While |morpheus| provides a fantastic means for determining uptime and availability of both services and VMs, sometimes more is needed. A good example of this is performance application monitoring. To solve this an external monitoring integration with ServiceNow is provided out of the box.

Service Now
-----------

To add a service now integration, simply visit the 'Monitoring Settings' section in |AdmSetMon|. This allows users to map incident severity levels to equivalent severities in ServiceNow.

To enable service now simply expand the section labelled "ServiceNow" in |AdmSetMon|. Toggle the enabled flag and enter the `Host`, `User`, and `Password` information required to connect to ServiceNow. The other options below include behaviors upon new incidents being opened and old incidents closing. It also includes a table for mapping |morpheus| incident severity levels to their ServiceNow counterparts.
