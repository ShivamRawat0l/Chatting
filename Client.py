import socket
import sys
import time

s=socket.socket()
host = input("Enter the name of the host to connect ")
port = 12345
s.connect((host,port))
while True:
    message=s.recv(1024)
    print(message.decode())
    a=input()
    s.send(a.encode())
