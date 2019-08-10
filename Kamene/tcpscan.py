#!/usr/bin/python3

from kamene.all import *

target = input("Informe um host: ")
flag = input("Informe uma flag: ")

res, unans = sr(IP(dst=target)/TCP(flags=flag, dport=(1, 1024)))

res.show(lfilter=lambda s,r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)))
