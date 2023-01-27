Requirements
````````````

Elasticsearch requires the following TCP ports for the cluster nodes. Please create the appropriate firewall rules on your
Percona nodes.

  - 9200
  - 9300

  .. code-block:: bash

    [root]# firewall-cmd --zone=public --add-port={9200/tcp,9300/tcp} --permanent
    [root]# firewall-cmd --reload



#. Three Existing CentOS 7+ nodes accessible to the Morpheus Appliance

#. Install Java on each node

   You can install the latest OpenJDK with the command:

   .. code-block:: bash

    sudo yum install java-1.8.0-openjdk.x86_64

   To verify your JRE is installed and can be used, run the command:

   .. code-block:: bash

    java -version

   The result should look like this:

   .. code-block:: bash

      Output of java -version
      openjdk version "1.8.0_65"
      OpenJDK Runtime Environment (build 1.8.0_65-b17)
      OpenJDK 64-Bit Server VM (build 25.65-b01, mixed mode)