from scapy.all import *

counter = 0

for packet in PcapReader('HTTPS_traffic.pcap'):
    print " # Packet : "+ str(counter)
    print packet.show()
    break
