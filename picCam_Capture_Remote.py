# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 08:34:58 2017

@author: ASUS
"""
import numpy as np
import sys
import io
import struct
import socket
#import msvcrt as m

#def wait():
#    m.getch()

def wait():
  try:
    #no=sys.stdin.fileno()
    #print "fileno ", no
    c = sys.stdin.read(1)
    print ("Got character", c) #repr(c)
  except IOError: pass
  return ord(c)

def socket_wait_id():
  # Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
  # all interfaces)
  server_socket = socket.socket()
  server_socket.bind(('0.0.0.0', 8000)) 
  server_socket.listen(0)
  server_connections = server_socket.accept()
  connection=server_connections[0].makefile('rb')
  ID=0
  try:
    rd=connection.read(struct.calcsize('<L'))
    ID = struct.unpack('<L',rd)[0] 
  finally:
    connection.close()
    server_socket.close()
  return ID

def socket_send_id(ip,ID):
  client_socket = socket.socket()
  client_socket.connect((ip, 8000))
  connection = client_socket.makefile('wb')
  try:
    connection.write(struct.pack('<L', ID))
    print('Socket send ID',ID)
  finally:
    connection.close()
    client_socket.close()
    
def socket_send_str(ip,msg):
  client_socket = socket.socket()
  client_socket.connect((ip, 8000))
  connection = client_socket.makefile('wb')
  try:
    #client_socket.sendall(msg)
    connection.write(struct.pack('<L',msg))
  finally:
    connection.close()
    client_socket.close()

while True:
  print('Wait key press!')
  k=wait()
  ip='10.0.1.11'
  try:
    socket_send_id(ip,k)
  finally:
    if(k=='q'):
      break
   



#cv2.destroyAllWindows()
