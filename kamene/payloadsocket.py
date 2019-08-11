#!/usr/bin/python3

import socket
import os

target_host = "www.thecrackertechnology.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

payload = "GET / HTTP/1.1\t\nHOST: www.thecrackertechnology.com\r\nConnection: keep-alive\n\r\n"

client.send(payload.encode(encoding='utf-8'))

response = client.recv(4096)

print(response.decode('utf-8'))
