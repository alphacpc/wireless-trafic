from kafka3 import KafkaConsumer
from elasticsearch6 import Elasticsearch

consumer = KafkaConsumer("tester", bootstrap_servers='localhost:9092')

elastic = Elasticsearch()

# elastic.indices.create(index = "captures")

for msg in consumer:

    response = msg.value.decode("utf-8").split("-")

    doc = {
        "localtime": response[0].strip(),
        "protocol": response[1].strip(),
        "src_addr": response[2].strip(),
        "src_port": response[3].strip(),
        "dst_addr": response[4].strip(),
        "dst_port": response[5].strip(),
        "information": response[6].strip(),
    }
    
    elastic.index(index="captures", body=doc, doc_type="_doc")


    print(doc)
