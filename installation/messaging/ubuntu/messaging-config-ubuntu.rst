RabbitMQ Installation and Configuration
```````````````````````````````````````

#. Install erlang and rabbitmq-server repositories using Cloudsmith.io, as recommended by RabbitMQ's documentation:

   - `RabbitMQ Documentation <https://www.rabbitmq.com/install-debian.html#apt-cloudsmith>`_
   - `Cloudsmith.io erlang Documentation <https://cloudsmith.io/~rabbitmq/repos/rabbitmq-erlang/setup/#formats-deb>`_
   - `Cloudsmith.io rabbitmq-server Documentation <https://cloudsmith.io/~rabbitmq/repos/rabbitmq-server/setup/#formats-deb>`_

   .. code-block:: bash

      curl -1sLf 'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/setup.deb.sh' | sudo -E bash
      curl -1sLf 'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-server/setup.deb.sh' | sudo -E bash

#. The below commands will locate all versions available for erlang and rabbitmq-server but only install the OTP and RabbitMQ version that is listed as supported above in the **RabbitMQ/Erlang Compatibility Table**

   .. code-block:: bash

      apt-cache policy erlang
      apt-cache policy rabbitmq-server

   .. important:: In this example, we'll install 24.3.4.8-1 OTP/erlang and 3.9.27-1 rabbitmq-server. At the time of this writing, 24.x OTP and 3.9.x RabbitMQ are the maximum supported versions

#. Install the pacakges using the versions selected above:

   .. important:: Newer versions of Ubuntu come with erlang-base already installed, which installs erlang.  Because of this, a new version may already be installed, even beyond what is supported.  **This document will assume that there is no erlang installed** but if you attempt to install erlang following this process, you may see an error for dependency conflicts

   .. code-block:: bash

      apt-get install erlang=1:24.3.4.8-1 -y
      apt-get install rabbitmq-server=3.9.27-1 -y

   .. important:: Format is [package-name]=[version]

#. Hold the packages to ensure they are not accidentally upgraded:

   .. code-block:: bash

      apt-mark hold erlang
      apt-mark hold rabbitmq-server

   .. note:: Instructions to enable versionlock is listed in the **Requirements** section