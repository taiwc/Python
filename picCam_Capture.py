# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 08:34:58 2017

@author: ASUS
"""
import numpy as np
import time
import sys
import io
import picamera
import cv2
#import msvcrt as m

#def wait():
#    m.getch()

def wait():
  try:
    #no=sys.stdin.fileno()
    #print "fileno ", no
    c = sys.stdin.read(1)
    #print "Got character", c #repr(c)
  except IOError: pass
  return c

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
  finally:
    connection.close()
    client_socket.close()
    
def proc_cam(camera,k,ii):
        ret=1
        i=ii
        if k==ord('q'): #q key to stop
          print("quit")
          ret=0
        elif k==-1:
          ret=-1
        elif k==ord('g'):
          filename="/home/pi/Python/image%02d.jpg" % i
          camera.capture(filename)
          print(filename)
          img=cv2.imread(filename)
          cv2.imshow(filename,img)
          i=i+1
        elif k==ord('s'):
          print("stop_preview")
          camera.stop_preview()
        elif k==ord('v'):
          print("start_preview")
          camera.start_preview()
        elif k==ord('6'):
          print("640x480")
          camera.resolution=(640,480)
        elif k==ord('3'):
          print("320x240")
          camera.resolution=(320,240) 
        else:
          ret=1
        return ret,i
    
with picamera.PiCamera() as camera:
    camera.resolution=(320,240)
    camera.start_preview()
    print("Press Key g to Save")
    #time.sleep(20)
    i=0
    while True:
        #k=cv2.waitKey(500) & 0xff
        #k=m.getch()
        k=wait()
        print(k)
        ret,i=proc_cam(camera,ord(k),i)
        if(ret==00):
          break
        else:
          continue
        
    camera.stop_preview()

cv2.destroyAllWindows()
