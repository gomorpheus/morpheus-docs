.. _automation:

Automation
==========

``Provisioning -> Automation``

The Automation section is composed of Tasks and Workflows. Tasks can be scripts added directly, scripts and blueprints from the Library section, recipes, playbooks, salt states, puppet agent installs, or http (api) calls. These Tasks are are combined into workflows, which can be selected to run at provision time or executed on existing instances via ``Actions -> Run Workflow``.

.. include:: tasks.rst
.. include:: workflows.rst
.. include:: executions.rst
.. include:: scale_thresholds.rst
.. include:: integrations.rst
.. include:: power_scheduling.rst
.. include:: execute_scheduling.rst
.. include:: /troubleshooting/Variables_Examples.rst
