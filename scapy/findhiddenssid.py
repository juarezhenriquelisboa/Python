from scapy.all import *

hidden_ssid_aps = set()

def FindHinddenSSID(pkt) :

    if pkt.haslayer(Dot11Beacon) :
        if not pkt.info :
            if pkt.addr3 not in hidden_ssid_aps :
                hidden_ssid_aps.add(pkt.addr3)
                print "HIDDEN SSID Network Found! BSSID: ", pkt.addr3
    elif pkt.haslayer(Dot11ProbeResp) and  ( pkt.addr3 in hidden_ssid_aps ) :
        print "HIDDEN SSID Uncovered! ", pkt.info, pkt.addr3 

packets = rdpcap('Hidden_Network.pcap')

for pkt in packets:
    FindHinddenSSID(pkt)
