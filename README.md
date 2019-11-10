# Simple ELK stack for testing logging with python-logstash

Very simple stack for development/testing plugging together the OSS
images provided by elastic (single node, no authentication).

## Quickstart

    $ docker-compose up

    $ curl localhost:9200
    $ python3 -m venv venv; . ./venv/bin/activate
    $ pip install python-logstash
    $ python example.py  # Logs to console and logstash at localhost:5959

## Exposed ports on host

- 9200 - Elasticsearch
- 5959 - Logstash TCP input plugin, json_lines format
- 5601 - Kibana UI
