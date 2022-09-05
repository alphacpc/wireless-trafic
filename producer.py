import pyshark
import time
from datetime import datetime
from kafka3 import KafkaProducer


# Define Interface
networkInterface = "wlp0s20f3"

# Define Producer
producer = KafkaProducer(bootstrap_servers="localhost:9092", api_version=(0,10,0,1))


# Define Capture
capture = pyshark.LiveCapture(interface=networkInterface)

print("Programme tourne...")
for packet in capture:
    try:
        localtime = time.asctime(time.localtime(time.time()))
        today = datetime.today().strftime('%Y/%m/%d')
        protocol = packet.transport_layer
        src_addr = packet.ip.src
        src_port = packet[protocol].srcport
        dst_addr = packet.ip.dst
        dst_port = packet[protocol].dstport
        domaine_name = packet.dns.qry_name if ("DNS" in packet and not packet.dns.flags_response.int_value) else packet.length
        domaine_existe = True if ("DNS" in packet and not packet.dns.flags_response.int_value) else False


        producer.send('trafic', bytes("%s - %s - %s - %s - %s - %s - %s -%s - %s" % (localtime, today, src_addr, src_port, dst_addr, dst_port, protocol, domaine_name, domaine_existe), 'utf-8'))
 

    except AttributeError as e:
        # IGNORE PACKETs !=  TCP, UDP and IPv4
        pass

print("Fin du programme !")
