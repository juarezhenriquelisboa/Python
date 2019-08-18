from scapy.all import *

counter = 0

for packet in PcapReader('HTTPS_traffic.pcap'):
    if packet.haslayer(DNSRR):
        if isinstance(packet.an, DNSRR):
            counter = counter + 1
            print str(counter)+". "+packet.an.rrname
            if counter == 10:
                break
