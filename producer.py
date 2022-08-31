import json
import time
import requests
from kafka3 import KafkaProducer


url = "https://api.jcdecaux.com/vls/v1/stations?apiKey=2ad8eced5129d4ce52775999119427cfc6af1e2e"

print("mafe1")


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

print("mafe2")


producer = KafkaProducer(bootstrap_servers="localhost:9092", api_version=(0,10,0,1))

print("mafe3")


while True:
    response = requests.get(url)
    stations = response.json()
    print("mafe4")
    producer.send('touch', b'some_message_bytes')

    print("mafe5")



    for station in stations:
        pass
        # producer.send("test-stations", json.dumps(station))
    
    print("{} Produced {} station records".format(time.time(), len(stations)))
    
    time.sleep(4)