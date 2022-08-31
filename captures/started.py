from numpy import broadcast
import scapy.all as scapy

req = scapy.ARP()
req.pdst = "192.168.62.232/24"

broadcast = scapy.Ether()
broadcast.hwdst = "ff:ff:ff:ff:ff"

packet = req/broadcast

client = scapy.srp(packet, timeout=3, verbose=0)

print(req.summary())
print(req.show())