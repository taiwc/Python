import io
import socket
import struct
import time


client_socket = socket.socket()
client_socket.connect(('10.0.1.11', 8000))
client_connection = client_socket.makefile('wb')

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

server_connections = server_socket.accept()
server_connection=server_connections[0].makefile('rb')

ID = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]


    connection.write(struct.pack('<L', 0))

    connection.close()
    client_socket.close()
    finish = time.time()
print('Sent %d images in %d seconds at %.2ffps' % (
    count, finish-start, count / (finish-start)))
