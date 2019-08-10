#!/usr/bin/python3

from kamene.all import *

target = input("Informe um alvo: ")

destport = input("Porta de destino: ")

port = int(destport)

ans,unans=sr(IP(dst=target, ttl=(1,30))/TCP(dport=port,flags="S"))
ans.summary(lambda s,r: r.sprintf("%IP.src%\t{ICMP:%ICMP.type%}\t{TCP:%TCP.flags%}"))
