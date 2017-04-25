import io
import socket
import struct
import time


client_socket = socket.socket()
client_socket.connect(('10.0.1.11', 8000))
connection = client_socket.makefile('wb')

try:
    ID=1
    count=0
    start=time.time()
    while count<10:
      connection.write(struct.pack('<L', ID))
      ID=ID+1
      count=count+1
    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()
    finish = time.time()
print('Sent %d in %d seconds at %.2ffps' % (
    count, finish-start, count / (finish-start)))
