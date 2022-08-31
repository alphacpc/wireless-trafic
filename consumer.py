import json
from kafka3 import KafkaConsumer

consumer = KafkaConsumer("tester", bootstrap_servers='localhost:9092')

for m in consumer:
    print(m)
