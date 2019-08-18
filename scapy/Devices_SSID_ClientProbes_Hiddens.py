import sys
from scapy.all import *

packets = rdpcap('WiFi_traffic3.pcap')

devices = set()
ssids = set()
clientprobes = set()
hidden_ssid_aps = set()

def FindHinddenSSID(pkt) :

    if pkt.haslayer(Dot11Beacon) :
        if not pkt.info :
            if pkt.addr3 not in hidden_ssid_aps :
                hidden_ssid_aps.add(pkt.addr3)
                print "HIDDEN SSID Network Found! BSSID: ", pkt.addr3
    elif pkt.haslayer(Dot11ProbeResp) and  ( pkt.addr3 in hidden_ssid_aps ) :
        print "HIDDEN SSID Uncovered! ", pkt.info, pkt.addr3 
def GetClientProbes(pkt) :

    if pkt.haslayer(Dot11ProbeReq) :

        if len(pkt.info) > 0 : 
            testcase = pkt.addr2 + '---' + pkt.info 
            if testcase not in clientprobes :
                clientprobes.add(testcase) 
                print "New Probe Found:  " + pkt.addr2 + ' ' + pkt.info 

                print "\n------------Client Probes Table ---------------\n"
                counter = 1
                for probe in clientprobes :
                    [client, ssid] = probe.split('---')
                    print counter, client, ssid
                    counter = counter + 1 
                print "\n-----------------------------------------------\n"

def GetSSID(pkt) :

    if pkt.haslayer(Dot11Beacon) : 
        temp = pkt 

        while temp:
            temp = temp.getlayer(Dot11Elt) 
            if temp and temp.ID == 0 and (temp.info not in ssids) :	
                ssids.add(temp.info)
                print len(ssids), pkt.addr3, temp.info
                break 

            temp = temp.payload 

def GetDevices(pkt) :
    if pkt.haslayer(Dot11) :
        if pkt.addr2 and ( pkt.addr2 not in devices ) :
            devices.add(pkt.addr2)
            print len(devices) 
            print repr(pkt.addr2)


for pkt in packets:
    GetDevices(pkt)
    GetSSID(pkt)
    GetClientProbes(pkt)
    FindHinddenSSID(pkt)
