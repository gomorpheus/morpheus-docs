Install Elasticsearch 7.x
`````````````````````````

#. On each ES node run the following to install Elasticsearch.

   .. code-block:: bash

      wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
      apt-get install apt-transport-https
      echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
      apt-get update && apt-get install elasticsearch