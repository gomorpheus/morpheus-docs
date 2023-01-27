RabbitMQ Installation and Configuration
```````````````````````````````````````

#. Install erlang and rabbitmq-server repositories using Cloudsmith.io, as recommended by RabbitMQ's documentation:

   - `RabbitMQ Documentation <https://www.rabbitmq.com/install-rpm.html#cloudsmith>`_
   - `Cloudsmith.io erlang Documentation <https://cloudsmith.io/~rabbitmq/repos/rabbitmq-erlang/setup/#formats-rpm>`_
   - `Cloudsmith.io rabbitmq-server Documentation <https://cloudsmith.io/~rabbitmq/repos/rabbitmq-server/setup/#formats-rpm>`_

   .. code-block:: bash

      curl -1sLf 'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/setup.rpm.sh' | sudo -E bash
      curl -1sLf 'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-server/setup.rpm.sh' | sudo -E bash

#. The below commands will locate all versions available for erlang and rabbitmq-server but only install the OTP and RabbitMQ version that is listed as supported above in the **RabbitMQ/Erlang Compatibility Table**

   .. code-block:: bash

      dnf --showduplicates list erlang
      dnf --showduplicates list rabbitmq-server

   .. important:: In this example, we'll install 24.3.4.7-1.el8 OTP/erlang and rabbitmq-server-3.9.27-1.el8.noarch RabbitMQ. At the time of this writing, 24.x OTP and 3.9 RabbitMQ are the maximum supported versions

#. Install the pacakges using the versions selected above:

   .. code-block:: bash

      dnf install erlang-24.3.4.7-1.el8.x86_64 -y
      dnf install rabbitmq-server-3.9.27-1.el8.noarch -y

   .. important:: Format is [package-name]-[version].[architecture]

#. Pin the packages to ensure they are not accidentally upgraded:

   .. code-block:: bash

      dnf versionlock erlang-24.3.4.7-1.el8.x86_64
      dnf versionlock rabbitmq-server-3.9.27-1.el8.noarch

   .. note:: Instructions to enable versionlock is listed in the **Requirements** section