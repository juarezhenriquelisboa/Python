from scapy.all import *

packets = rdpcap('WiFi_traffic.pcap')

pkt = packets[0]

# printando detalhes do primeiro pacote
print(repr(pkt))

# printando o layout/formato do RadioTap header
print(repr(ls(RadioTap)))

# printando layout/formato do Dot11 header
print(repr(ls(Dot11)))

# printando layout/formato do Dot11Beacon header
print(repr(ls(Dot11Beacon)))

# printando layout/formato do Dot11 Information Element header
print(repr(ls(Dot11Elt)))

# printando apenas a camada wifi
print(repr(pkt.payload))

# printando apenas a camada Wifi Beacon
print(repr(pkt.payload.payload))

# printando apenas a camada de primeira informacao do elemento ELt
print(repr(pkt.payload.payload.payload))

# printando o SSID
print(repr(pkt.payload.payload.info))

# printando a camado Beacon usando a funcao getlayer()

beacon_layer = pkt.getlayer(Dot11Beacon)

print(repr(beacon_layer))

# Checando se o Beacon esta presente no pacote

print(repr(pkt.haslayer(Dot11Beacon)))




