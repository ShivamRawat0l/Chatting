import socket
import time
import sys

s=socket.socket()
host=socket.gethostname()
print(host + 'is the name of the host ')
port=8080
s.bind((host,port))
print("Listening    ")
s.listen(1)
conn,addr=s.accept()
