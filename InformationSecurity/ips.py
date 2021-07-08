import ipaddress

ip = '192.168.15.30'
ip1 = '192.168.15.0/24'

address = ipaddress.ip_address(ip)
network = ipaddress.ip_network(ip1, strict = False)

print(address + 250)
print(network)
for ip2 in network:
    print(ip2)
