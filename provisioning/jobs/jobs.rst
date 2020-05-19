Jobs
====

Jobs are for scheduled execution of Automation Tasks and Workflows. Jobs can be set to execute on a schedule, at one specific point in time, and/or execute manually (on-demand). Jobs are linked to existing Tasks or Workflows, and allow for custom configuration options. Jobs can be associated with Instances, Servers, or have no association, such as a job for an SSH task.

Jobs allow for scheduled execution of nearly anything as Tasks Types include Bash, Powershell, HTTP/API, Ansible, Chef, Puppet, Groovy, Python, jRuby, Javascript, and library scripts and templates, which can be configured for resource, remote, or local execution targets. If you need something to execute on a schedule, |morpheus| Jobs can deliver.

Jobs are configured in the ``JOBS`` tab, and the ``JOB EXECUTIONS`` tab contains Job execution history with result output.

.. include:: jobs_tab.rst
.. include:: job_executions.rst
