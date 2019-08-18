from scapy.all import *

counter = 0

for packet in PcapReader('HTTPS_traffic.pcap'):
    counter = counter + 1
    if counter > 999 and counter < 1006:
        hex_dump = ':'.join(x.encode('hex') for x in str(packet))
        print "# Packet : "+str(counter)
        print hex_dump
        print "\n"
    if counter == 1006:
        break
