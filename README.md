# Simple ELK stack for testing logging with python-logstash

Very simple stack for development/testing which plugs together the OSS
Docker images provided by elastic (single node, no authentication).

## Quickstart

    # Bring up the containers
    $ docker-compose up -d

    # Test Elasticsearch and Logstash connectivity
    $ curl localhost:9200
    $ nc -v -z localhost 5959
    
    # Send some logs to Logstah using python-logstash
    $ python3 -m venv venv
    $ . ./venv/bin/activate
    $ pip install python-logstash
    $ python example.py
    
    # Visit http://localhost:5601, create a `logstash-*` index pattern, browse the logs
    
## Exposed services on host system

- localhost:9200 - Elasticsearch
- localhost:5959 - Logstash, TCP input plugin, format json_lines
- localhost:5601 - Kibana UI
