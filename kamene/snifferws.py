#!/usr/bin/python3

from kamene.all import *

print("Realizando o sniffer de 30 pacotes..")

pkts = sniff(count=30, iface="wlx0cb6d2f2ca28")

print("Finalizado")

wrpcap("tmp.pcap", pkts)

