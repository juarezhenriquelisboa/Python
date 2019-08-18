from scapy.all import *

packets = rdpcap('HTTPS_traffic.pcap')

count = 0

for packet in packets:
    count = counter + 1
    if counter > 999 and counter < 1006:
        hex_dump = ':'.join(x.encode('hex') for x in str(packete))
        print "# Packet : "+str(counter)
        print hex_dump
        print "\n"
    if counter == 1006:
        break
