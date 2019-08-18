from scapy.all import *

counter = 0

for packet in PcapReader('HTTPS_traffic.pcap'):
    counter = counter + 1
    print "# Packet : "+str(counter)
    print packet.summary()
    print "\n"
    if counter == 6:
        break
