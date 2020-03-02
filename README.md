# STA9760 Analysis of Citibike Docks with Kibana and ElasticSearch

Kibana docker compose example. **[Dataset used](https://feeds.citibikenyc.com/stations/stations.jso)**

![scrnshot](https://raw.githubusercontent.com/mottaquikarim/STA9760_Kibana/master/Screen%20Shot%202020-03-02%20at%2012.26.53%20AM.png)

## [Tutorial](https://www.youtube.com/watch?v=9Mkf6kHroG8&feature=youtu.be)

## How to Run

Start:

```
docker-compose up -d
```

This will start ElasticSearch and Kibana.

**ElasticSearch**: http://localhost:9200
**Kibana**: http://localhost:5601

Both should load...something but will be empty as python has not yet run. If nothing shows up, give it a minute as it takes a bit of time for these services to load.

Running python:

```
docker-compose run pyth python citibike.py
```

This will load citibike dock data into Elasticsearch at a cadence of once / 30s.

Shutting off:

```
docker-compose down
```
