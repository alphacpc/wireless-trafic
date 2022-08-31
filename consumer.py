import json
from kafka3 import KafkaConsumer

print("mafe1")

consumer = KafkaConsumer("touch", bootstrap_servers='localhost:9092')

print("mafe2")


print(consumer)

for m in consumer:
    print(m)
