from scapy.all import *

response_counter = 0

for packet in PcapReader('HTTPS_traffic.pcap'):
    if packet.haslayer(DNSRR):
        response_counter = response_counter + 1

print "Total DNS response: "+str(response_counter)
