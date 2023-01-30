Install Elasticsearch 7.x
`````````````````````````

#. On each ES node run the following to install Elasticsearch.

   `Elasticsearch Install Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/rpm.html>`_

   .. code-block:: bash

      rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

   .. code-block:: bash

      vi /etc/yum.repos.d/elasticsearch.repo
         # Paste in the below:
         [elasticsearch]
         name=Elasticsearch repository for 7.x packages
         baseurl=https://artifacts.elastic.co/packages/7.x/yum
         gpgcheck=1
         gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
         enabled=0
         autorefresh=1
         type=rpm-md

   .. code-block:: bash

      dnf install --enablerepo=elasticsearch elasticsearch -y