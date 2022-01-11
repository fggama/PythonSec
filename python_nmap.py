import nmap
import socket


def print_result(lista, nivel=1):
    if type(lista) is list:
        for elemento in lista:
            if type(elemento) is dict:
                print_result_dict(elemento,nivel+1)
            elif type(elemento) is list:
                print_result(elemento, nivel+1)
            else:
                print(".\t"*nivel , "{",str(elemento))
    else:
        print_result_dict(lista, nivel)


def print_result_dict(lista, nivel):
    for key, value in lista.items():
        if type(value) is dict:
            print("\t"*nivel, str(key), "[")
            print_result_dict(value, nivel+1)
        elif type(value) is list:
            print_result(value, nivel+1)
        else:
            if (len(str(value)) > 0):
                print("\t"*nivel , str(key) , ":" , str(value).replace("\n",""))


scanner = nmap.PortScanner()
ip_addr = '213.169.3.195'
ip_mask = "213.169.0.0/22"

print("\n",socket.gethostname()," (" , ip_addr , " : " , ip_mask , ")")
print(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
response = input("""Seleccione una opción
                1. SYN ACK Scan
                2. UDP Scan
                3. Comprehensive Scan (-v -sS -sV -sC -A -O)
                4. Regular Scan
                5. OS Detection
                6. Multiple IP inputs
                7. Ping Scan\n""")

print("[+] Nmap Version: ", scanner.nmap_version())

if response == '1':
    print("[+] SYN ACK Scan:",ip_addr)
    scanner.scan(ip_addr,'1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("[+] Ip Status: ", scanner[ip_addr].state())
    print("[+] Protocolos:",scanner[ip_addr].all_protocols())
    print("[+] Puertos abiertos: ")
    print_result(scanner[ip_addr]['tcp'])
 
     
elif response == '2':
    print("[+] UDP Scan:",ip_addr)
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("[+] Ip Status: ", scanner[ip_addr].state())
    print("[+] Protocolos:",scanner[ip_addr].all_protocols())
    print("[+] Puertos abiertos: ")
    print_result(scanner[ip_addr]['udp'])
  
     
elif response == '3':
    print("[+] Comprehensive Scan:",ip_addr)
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("[+] Ip Status: ", scanner[ip_addr].state())
    print("[+] Protocolos:",scanner[ip_addr].all_protocols())
    print("[+] Puertos abiertos: ")
    print_result(scanner[ip_addr]['tcp'])

elif response == '4':
    print("[+] Regular Scan:",ip_addr)
    scanner.scan(ip_addr)
    print(scanner.scaninfo())
    print("[+] Ip Status: ", scanner[ip_addr].state())
    print("[+] Protocolos:",scanner[ip_addr].all_protocols())
    print("[+] Puertos abiertos: ")
    print_result(scanner[ip_addr]['tcp'])

elif response == '5':
    print("[+] OS Detection:",ip_addr)
    scanner.scan(ip_addr, arguments="-O")
    print_result(scanner[ip_addr]['osmatch'])
 
elif response == '6':
    print("[+] Multiple IP:",ip_addr)
    scanner.scan(ip_addr,'1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("[+] Ip Status: ", scanner[ip_addr].state())
    print("[+] Protocolos:",scanner[ip_addr].all_protocols())
    print("[+] Puertos abiertos: ")
    print_result(scanner[ip_addr]['tcp'])
     
elif response == '7': 
    print("[+] Ping Scan:",ip_mask)
    scanner.scan(hosts=ip_mask, arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    for host, status in hosts_list:
        print('\t{0}:{1}'.format(host, status))
     
else:
    print("Seleccione una opcion")