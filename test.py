import pyshark
import time
import geocoder

# Define Interface
networkInterface = "wlp0s20f3"

# Define Capture
capture = pyshark.LiveCapture(interface=networkInterface)

for packet in capture.sniff_continuously(packet_count=200):
    try:
        localtime = time.asctime(time.localtime(time.time()))
     
        protocol = packet.transport_layer
        src_addr = packet.ip.src
        src_port = packet[protocol].srcport
        dst_addr = packet.ip.dst
        dst_port = packet[protocol].dstport

        ip = geocoder.ip(dst_addr)
        country_name = ip.country
        city_name = ip.city
        state_name = ip.state
        location = ip.latlng

        domaine_name = packet.dns.qry_name if ("DNS" in packet and not packet.dns.flags_response.int_value) else None

        print ("%s --- IP %s:%s --- %s:%s --- (%s) --- (%s) --- (%s) --- %s --- %s" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol, country_name, city_name, state_name, location))

    except AttributeError as e:
        # IGNORE PACKETs !=  TCP, UDP and IPv4
        pass