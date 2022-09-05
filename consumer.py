from kafka3 import KafkaConsumer
from elasticsearch6 import Elasticsearch
from datetime import datetime

from pprint import pprint

consumer = KafkaConsumer("trafic", bootstrap_servers='localhost:9092')

elastic = Elasticsearch()

# elastic.indices.create(index = "captures")

tabs = []

print("Consumer tourne...")
for msg in consumer:

    response = msg.value.decode("utf-8").split("-")

    print(response, "\n")

    if len(response) == 9:

        # doc = {
        #     "localtime": response[0].strip(),
        #     "today": response[1].strip(),
        #     "src_addr": response[2].strip(),
        #     "src_port": response[5].strip(),
        #     "dst_addr": response[4].strip(),
        #     "dst_port": response[3].strip(),
        #     "protocol": response[6].strip(),
        #     "information": response[7].strip(),
        #     "isDNS": response[8].strip(),
        # }
        
        elastic.index(
            index="captures", 
            body = {
                "localtime": response[0].strip(),
                "today": response[1].strip(),
                "src_addr": response[2].strip(),
                "src_port": response[5].strip(),
                "dst_addr": response[4].strip(),
                "dst_port": response[3].strip(),
                "protocol": response[6].strip(),
                "information": response[7].strip(),
                "isDNS": response[8].strip(),
            }, 
            doc_type = "_doc"
        )




print("Consumer finish !!!")