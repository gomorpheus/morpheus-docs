.. uml::

   !include <tupadr3/common>
   !include <tupadr3/devicons/mysql>
   !include <tupadr3/devicons/nginx>
   !include <tupadr3/devicons/php>
   !include <tupadr3/devicons/redis>
   !include <tupadr3/font-awesome-5/typo3>
   !include <cloudinsight/elasticsearch>
   !include <cloudinsight/haproxy>

   skinparam defaultTextAlignment center

   rectangle "<$elasticsearch>\nElastic\nSearch" as elastic
   rectangle "<$haproxy>\nHAProxy" as haproxy

   DEV_MYSQL(mysql,Mysql,database)
   DEV_NGINX(nginx,Nginx,rectangle)
   DEV_NGINX(nginx2,Nginx,rectangle)
   DEV_PHP(php,PHP + TYPO3,rectangle)
   DEV_PHP(php2,PHP + TYPO3,rectangle)
   DEV_REDIS(redis,Redis,database)

   FA5_TYPO3(typo3,TYPO3\nShared,rectangle,#f49700)

   haproxy <--> nginx
   haproxy <--> nginx2
   nginx <--> php
   nginx2 <--> php2
   php <--> typo3
   php <--> redis
   php <--> mysql
   php <--> elastic
   php2 <--> typo3
   php2 <--> redis
   php2 <--> mysql
   php2 <--> elastic