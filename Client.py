import socket
import sys
import time

s=socket.socket()
host = input("Enter the name of the host to connect ")
port = 8080
s.connect((host,port))