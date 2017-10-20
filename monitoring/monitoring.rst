**********
Monitoring
**********

|morpheus| provides great monitoring features out of the box. Anything
provisioned within |morpheus| automatically gets a check created in the
monitoring service. These checks are organized heirarchically in
"Groups" and "Apps". This makes it easy to gain a perspective as to what
a customer or full stack facing impact is in the event of a particularly
instance failure. This also takes into account redundancy layers when it
comes to calculating the applications overall uptime percentage.

There are also several integrations built into the monitoring subsystem
of |morpheus| including App Dynamics , New Relic, and even Service Now
integration.

.. include:: checks.rst
.. include:: hierarchy.rst
.. include:: incidents.rst
.. include:: alerts.rst
.. include:: integrations.rst
