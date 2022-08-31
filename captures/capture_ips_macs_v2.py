import scapy.all as scapy


req = scapy.ARP()

print("Test : ",req.summary())

print(req.show())


req.pdst = '192.168.62.232/24'
broadcast = scapy.Ether() 
  
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / req 

clients = scapy.srp(request_broadcast, timeout = 1)[0] 


for element in clients: 
    print(element[1].psrc + " --------- " + element[1].hwsrc) 