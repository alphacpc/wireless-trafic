from scapy.all import ARP, Ether, srp
 
target_ip = "192.168.62.232/24"

arp = ARP(pdst=target_ip)

ether = Ether(dst="ff:ff:ff:ff:ff:ff")


# stack them
packet = ether/arp
 
result = srp(packet, timeout=3, verbose=0)[0]
 

clients = []
 
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})
 
 
print("IP" + " "*18 + "MAC")
print(len(clients))
for client in clients:
    print("{}    {}".format(client['ip'], client['mac']))