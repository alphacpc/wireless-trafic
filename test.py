import pyshark
import time
import geocoder

from kafka3 import KafkaProducer

# Define Interface
networkInterface = "wlp0s20f3"

# Define Capture
capture = pyshark.LiveCapture(interface=networkInterface)

# Define Producer
# producer = KafkaProducer(bootstrap_servers="localhost:9092", api_version=(0,10,0,1))


for packet in capture:

    document = {}

    try:
        localtime = time.asctime(time.localtime(time.time()))
     
        document["protocol"] = packet.transport_layer
        document["src_addr"] = packet.ip.src
        document["src_port"] = packet[packet.transport_layer].srcport
        document["dst_addr"] = packet.ip.dst
        document["dst_port"] = packet[packet.transport_layer].dstport


        # ip = geocoder.ip(dst_addr)
        # country_name = ip.country
        # city_name = ip.city
        # state_name = ip.state
        # location = ip.latlng

        domaine_name = packet.dns.qry_name if ("DNS" in packet and not packet.dns.flags_response.int_value) else None

        document["informations"] = domaine_name
        

        # print ("%s --- IP %s:%s --- %s:%s --- (%s) --- (%s) --- (%s) --- %s --- %s" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol, country_name, city_name, state_name, location))
        # print ("%s --- IP %s:%s --- %s:%s --- (%s) --- " % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
        print(document)

        # producer.send('touch', b'some_message_bytes')


    except AttributeError as e:
        # IGNORE PACKETs !=  TCP, UDP and IPv4
        pass