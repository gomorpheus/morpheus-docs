RabbitMQ Cluster
----------------



Prerequisites

The basic requirement for RabbitMQ Cluster setup is to have minimum 2 nodes with CentOS 7 that we will using in this articles. Setup their FQDN and basic network settings and make sure that you are connected to the Internet.

In this article we will be using two Linux CentOS 7 servers with following host names.

RabbitMQ Master Server:

[root@linux ~]# hostname
linux
RabbitMQ Slave Server:

[root@node2 ~]# hostname
node2
Make sure that your both servers are date with latest updates and patches by running the following command with root or sudo user privileges.

``yum -y update``

Installing ERLANG

After basic system setup, we are going to start installation of RabbitMQ’s main dependencies such Erlang. To install Erlang on our system, we will be using the latest EPEL repository. Let’s run the following command to install the latest EPEl release.

``yum install epel-release``

epeal release

Once the EPEL release has been installed on your system, then you can install Erlang on CentOS 7 by issuing the following command.

``yum install erlang``

Erlang Installation

after resolving the dependencies, you will be asked to proceed or not. Press ‘y’ key and hit enter to continue. This will install Erlang and its all required dependencies on your system as shown.

erlang and dependencies

Installing RabbitMQ

After completing the installation of Erlang, now we are going to install RabbitMQ using its latest RPM package available on RabbitMQ Resource Page.

RabbitMQ RPM

Let’s copy the download source address and run the following ‘wget’ command to download the RPM package on your system.

``wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.1/rabbitmq-server-3.6.1-1.noarch.rpm``

Then run the command below to install the RabbitMQ RPM package on your system.

 rpm -i rabbitmq-server-3.6.1-1.noarch.rpm
Installing rabbitmq

Now we have installed RabbitMQ server on both of our nodes. start is service and check the status using below commands.

 rabbitmqctl status
You might the below error , run the below command and check the status again.

 /etc/init.d/rabbitmq-server restart
rabbitmq status

 rabbitmqctl status
Once you have restarted RabbitMQ services you should see the following output on both nodes.

rq_status

RabbitMQ Cluster Setup:

In order to create a RabbitMQ cluster, first choose your fisrt node which is going to be the Master.
In our case we will using our ‘linux’ node. There’s a cookie file which resides on each one of the nodes, but in order to join all nodes into a cluster, this cookie file needs to be identical on all machines in the cluster, use the cookie file from the Master node and copy it to the rest of the nodes.

You can find this under below path.

 [root@linux ~]# cat /var/lib/rabbitmq/.erlang.cookie
Sample output:

 SVTRZKAOOADLOJQAOBJQ
Now copy this key o all of your current node that you want to join with the cluster and change its permissions using the follow commands.

 chown rabbitmq:rabbitmq /var/lib/rabbitmq/*
  chmod 400 /var/lib/rabbitmq/.erlang.cookie
Now we will run the commands to join each node to the cluster using below command

 rabbitmqctl stop_app
 rabbitmqctl join_cluster --ram rabbit@node_name
 rabbitmqctl start_app
In order to check the status of your cluster run the below command.

 rabbitmqctl cluster_status
OR

 /usr/sbin/rabbitmqctl cluster_status
Here is the sample output:

 Cluster status of node rabbit@node2 ...
[{nodes,[{disc,[rabbit@node2]}]},
{running_nodes,[rabbit@node2]},
{cluster_name,&lt;&gt;},
{partitions,[]},
{alarms,[{rabbit@linux,[]}]}]
Enable RabbitMQ Management Plugin

Our RabbitMQ Cluster has been installed and setup using two CentOS 7 nodes, let’s run the following commands to enable RabbitMQ management plugin.

 rabbitmq-plugins enable rabbitmq_management
 chown -R rabbitmq:rabbitmq /var/lib/rabbitmq/
Plugin management

You can do the same by going to the directory where the RabbitMQ is installed.

 cd /usr/lib/rabbitmq/lib/rabbitmq_server-3.6.1
 sbin/rabbitmq-plugins enable rabbitmq_management
The rabbitmq_management plugin is a combination of the following plugins. All of the following plugins will be enabled when you execute the above command:

mochiweb
webmachine
rabbitmq_web_dispatch
amqp_client
rabbitmq_management_agent
rabbitmq_management
After enabling the rabbitmq_management plugin you should restart the RabbitMQ server as shown below.

 sbin/rabbitmqctl stop 
 sbin/rabbitmq-server -detached
Restart RabbitMQ

RabbitMQ Web Management:

Now you access your RabbitMQ server from any of your web browser with mentioned below port.

http://your_servers_ip:15672/

The default user name and passowrd of RabbitMQ Management console sn ‘guest’, ‘guest’ . But you can also create new admin user using below commands.

 rabbitmqctl add_user mqadmin mqadmin
 rabbitmqctl set_user_tags mqadmin administrator
 rabbitmqctl set_permissions -p / mqadmin ".*" ".*" ".*"
Login to RabbitMQ

After providing the right credentials you be directed towards the RabbitMQ Dashboard where you can configure and utilize it awesome features.

RabbitMQ Dashboard

Conclusion

That’s it. We have successfully installed and configured RabbitMQ cluster along with its Web management console. RabbitMQ runs with its standard configuration by default, so you don’t need to be panic about its configurations. Now let’s start using it and explore its multiple features.
