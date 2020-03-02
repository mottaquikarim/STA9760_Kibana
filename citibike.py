from datetime import datetime
from elasticsearch import Elasticsearch
from requests import get
from time import sleep


def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass

    es.indices.put_mapping(
        index=index_name,
        doc_type=doc_type,
        body={
            doc_type: {
                "properties": {"location": {"type": "geo_point"}, }
            }
        }
    )

    return es


def get_bike_data():
    url = "https://feeds.citibikenyc.com/stations/stations.json"
    r = get(url)
    r.raise_for_status()
    resp = r.json()
    stations = resp["stationBeanList"]

    return stations


if __name__ == "__main__":

    # Step 1: create an elastic search "index" to store data
    es = create_and_update_index('citibike-index', 'bike')

    i = 0
    while True:
        i += 1

        # Step 2: fetch bike data from the internets
        docks = get_bike_data()

        # Step 3: Push data into the elastic search
        for dock in docks:
            dock['location'] = {
                'lat': dock['latitude'],
                'lon': dock['longitude'],
            }
            dock['lastCommunicationTime'] = datetime.strptime(
                dock['lastCommunicationTime'],
                '%Y-%m-%d %I:%M:%S %p',
            )
            res = es.index(index='citibike-index', doc_type='bike', body=dock,)
            print(res['result'])

        print(f"DONE LOADING {i}, SLEEPING...")
        sleep(30)
