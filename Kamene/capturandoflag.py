#!/usr/bin/python3

from kamene.all import *

dest = input("\nDestino: ")
destport = input("\nPorta de destino: ")
flag = input("Flags: ")

port = int(destport)

ip = IP(dst=dest)
tcp = TCP(dport=port, flags=flag)

pkt = ip/tcp

srloop(pkt, count=1)
