import scapy.all as scapy
  
request = scapy.ARP()
  
request.pdst = '213.169.3.0/24'
broadcast = scapy.Ether()
  
broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout = 1)[0]
for element in clients:
    print(element[1].psrc + "      " + element[1].hwsrc)