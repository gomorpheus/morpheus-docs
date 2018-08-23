you can add this to /etc/rsyslog.d/morpheus.conf
```input(type="imfile" File="/var/log/morpheus/morpheus-ui/current" Tag="morpheus-ui" ReadMode="2" Severity="info" StateFile="morpheus-ui")
input(type="imfile" File="/var/log/morpheus/check-server/current" Tag="check-server" ReadMode="2" Severity="info" StateFile="morpheus-check-server")
input(type="imfile" File="/var/log/morpheus/elasticsearch/current" Tag="elasticsearch" ReadMode="2" Severity="info" StateFile="morpheus-elasticsearch")
input(type="imfile" File="/var/log/morpheus/mysql/current" Tag="mysql" ReadMode="2" Severity="info" StateFile="morpheus-mysql")
input(type="imfile" File="/var/log/morpheus/nginx/current" Tag="nginx" ReadMode="2" Severity="info" StateFile="morpheus-nginx")
input(type="imfile" File="/var/log/morpheus/rabbitmq/current" Tag="rabbitmq" ReadMode="2" Severity="info" StateFile="morpheus-rabbitmq")
input(type="imfile" File="/var/log/morpheus/redis/current" Tag="redis" ReadMode="2" Severity="info" StateFile="morpheus-redis")
```
input(type="imfile" File="/var/log/morpheus/guacd/current" Tag="guacd" ReadMode="2" Severity="info" StateFile="morpheus-guacd")


assuming they forward rsyslog to whatever they use. (edited)
