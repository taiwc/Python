import io
import socket
import struct
import time

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)
server_connections = server_socket.accept()
connection=server_connections[0].makefile('rb')
ID=1
try:
    start=time.time()
    count=0
    while True:
        ID = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not ID:
            break
        count=count+1
        print("ID=%d" % ID)
finally:
    connection.close()
    server_socket.close()
    finish = time.time()
print('Sent %d ID in %d seconds at %.2ffps' % (
    count, finish-start, count / (finish-start)))
