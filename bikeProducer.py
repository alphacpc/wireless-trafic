import json
import time
import requests
from kafka3 import KafkaProducer


url = "https://api.jcdecaux.com/vls/v1/stations?apiKey=2ad8eced5129d4ce52775999119427cfc6af1e2e"

producer = KafkaProducer(bootstrap_servers="localhost:2181", api_version=(0,10,0,1), value_serializer=lambda x: json.dumps(x).encode('utf-8'))

while True:
    response = requests.get(url)
    stations = response.json()
    # print(json.dumps(stations[4]).encode())

    producer.send('foobar', b'some_message_bytes')

    # producer.send(topic="touch", key=bytes("someString", encoding='utf8'),value=bytes("test", encoding='utf8'))


    for station in stations:
        # print(json.dumps(stations[4]).encode())
        pass

        
        # producer.send("test-stations", json.dumps(station))
    print("{} Produced {} station records".format(time.time(), len(stations)))
    # print("{} Produced {} station records".format(time.time(), len(stations)))
    time.sleep(4)