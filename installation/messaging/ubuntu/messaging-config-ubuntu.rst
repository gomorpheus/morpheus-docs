RabbitMQ Installation and Configuration
```````````````````````````````````````

#. Install erlang and rabbitmq-server repositories using Cloudsmith.io, as recommended by RabbitMQ's documentation:

   - `RabbitMQ Documentation <https://www.rabbitmq.com/docs/install-debian>`_

   .. code-block:: bash

      #!/bin/sh

      sudo apt-get install curl gnupg apt-transport-https -y

      ## Team RabbitMQ's main signing key
      curl -1sLf "https://keys.openpgp.org/vks/v1/by-fingerprint/0A9AF2115F4687BD29803A206B73A36E6026DFCA" | sudo gpg --dearmor | sudo tee /usr/share/keyrings/com.rabbitmq.team.gpg > /dev/null
      ## Community mirror of Cloudsmith: modern Erlang repository
      curl -1sLf https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg > /dev/null
      ## Community mirror of Cloudsmith: RabbitMQ repository
      curl -1sLf https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/rabbitmq.9F4587F226208342.gpg > /dev/null

      ## Add apt repositories maintained by Team RabbitMQ
      sudo tee /etc/apt/sources.list.d/rabbitmq.list <<EOF
      ## Provides modern Erlang/OTP releases
      ##
      deb [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main
      deb-src [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main

      # another mirror for redundancy
      deb [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main
      deb-src [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main

      ## Provides RabbitMQ
      ##
      deb [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
      deb-src [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main

      # another mirror for redundancy
      deb [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
      deb-src [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
      EOF

      ## Update package indices
      sudo apt-get update -y

#. The below commands will locate all versions available for erlang and rabbitmq-server but only install the OTP and RabbitMQ version that is listed as supported above in the **RabbitMQ/Erlang Compatibility Table**

   .. code-block:: bash

      apt-get update
      apt-cache policy erlang
      apt-cache policy rabbitmq-server

   .. important:: In this example, we'll install 1:26.2.5.4-1 erlang and 3.12.13-1 rabbitmq-server. You can find what version of rabbit you need by going to https://docs.morpheusdata.com/en/latest/release_notes/compatibility.html#services

#. Install the pacakges using the versions selected above:

   .. NOTE:: Newer versions of Ubuntu may come with erlang-base already installed, which installs erlang. Because of this, a new version may already be installed, even beyond what is supported. **This document will assume that there is no erlang installed** but if you attempt to install erlang following this process, you may see an error for dependency conflicts. You can check what is curently is installed by running dpkg -l | grep erlang 

   .. important:: Make sure to install the correct erlang version for the rabbitmq-server version you want to install.

   .. code-block:: bash

      # Install Erlang packages
      ERLANG_VERSION=1:26.2.5.4-1

      sudo apt-get install -y erlang-base=$ERLANG_VERSION \
                              erlang-asn1=$ERLANG_VERSION erlang-crypto=$ERLANG_VERSION \
                              erlang-eldap=$ERLANG_VERSION erlang-ftp=$ERLANG_VERSION \
                              erlang-inets=$ERLANG_VERSION erlang-mnesia=$ERLANG_VERSION \
                              erlang-os-mon=$ERLANG_VERSION erlang-parsetools=$ERLANG_VERSION \
                              erlang-public-key=$ERLANG_VERSION erlang-runtime-tools=$ERLANG_VERSION \
                              erlang-snmp=$ERLANG_VERSION erlang-ssl=$ERLANG_VERSION \
                              erlang-syntax-tools=$ERLANG_VERSION erlang-tftp=$ERLANG_VERSION \
                              erlang-tools=$ERLANG_VERSION erlang-xmerl=$ERLANG_VERSION


      # Install rabbitmq-server and its dependencies
      sudo apt-get install rabbitmq-server=3.12.13-1 -y --fix-missing

   .. NOTE:: Format is [package-name]=[version]

#. Hold the packages to ensure they are not accidentally upgraded:

   .. code-block:: bash

      apt-mark hold erlang
      apt-mark hold rabbitmq-server