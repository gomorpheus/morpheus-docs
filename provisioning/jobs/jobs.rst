Jobs
====

Jobs are for scheduled execution of Automation Tasks and Workflows. Jobs can be set to execute on a schedule, at one specific point in time, and/or execute manually (on demand). Jobs are linked to existing Tasks or Workflows, and allow for custom config options. Jobs can be associated with Instances, Servers, or have no association, such as a job for an ssh task.

Jobs allow for scheduled execution of essentially anything, as Tasks Types include bash, powershell, http/api, ansible, chef, puppet, groovy, python, jRuby, javascript, and library scripts and templates, which can be configured for resource, remote or local execution targets. If you need something to execute on a schedule, |morpheus| Jobs can deliver.

Jobs are configured in the ``JOBS`` tab, and the ``JOB EXECUTIONS`` tab contains Job execution history with result output.

.. include:: jobs_tab.rst
.. include:: job_executions.rst
