**********
Monitoring
**********

Overview
========

|morpheus| provides great monitoring features out of the box. Anything provisioned within |morpheus| automatically gets a check created in the monitoring service. These checks are organized hierarchically in "Groups" and "Apps". This makes it easy to gain a perspective as to what a customer or full stack facing impact is in the event of a particularly instance failure. This also takes into account redundancy layers when it comes to calculating the applications overall uptime percentage.

|morpheus| also includes a monitoring integration with ServiceNow. 

.. toctree::
  :maxdepth: 2

  logs.rst
  apps.rst
  checks.rst
  groups.rst
  incidents.rst
  contacts.rst
  alerts.rst

..
  status.rst
  integrations.rst
  hierarchy.rst
