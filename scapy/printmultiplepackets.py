from scapy.all import *

packets = rdpcap('HTTP_Traffic_mini.pcap')

for packet in packets[0:5]:
    print packet 
    print "\n"


#printando como hexa
for packet in packets[0:5]:
    hex_dump = ':'.join(x.encode('hex') for x in str(packet))
    print hex_dump
    print "\n"
