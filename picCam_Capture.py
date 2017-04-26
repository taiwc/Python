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
import socket
import struct
#import pyplot as plt

#def wait():
#    m.getch()

def wait():
  try:
    #no=sys.stdin.fileno()
    #print "fileno ", no
    c = sys.stdin.read(1)
    #print "Got character", c #repr(c)
  except IOError: pass
  return ord(c)

def socket_wait_init():
  # Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
  # all interfaces)
  server_socket = socket.socket()
  server_socket.bind(('0.0.0.0', 8000))   
  return server_socket

    
def socket_wait_id(server_socket):
  server_socket.listen(10)
  server_connections,addr = server_socket.accept()
  connection=server_connections.makefile('rb')
  print('connected IP:%s' % addr[0])
  ID=0
  try:
    rd=connection.read(struct.calcsize('<L'))
    ID = struct.unpack('<L',rd)[0] 
  finally:
    connection.close()
  return ID

def socket_wait_str(server_socket):
  server_socket.listen(10)
  server_connections,addr = server_socket.accept()
  print('connected IP:%s' % addr[0])
  data = server_connections.recv(1024)
  print(data)
  server_connections.close()
  return data

def socket_send_id(ip,ID):
  client_socket = socket.socket()
  client_socket.connect((ip, 8000))
  connection = client_socket.makefile('wb')
  try:
    connection.write(struct.pack('<L', ID))
  finally:
    connection.close()
    client_socket.close()

def imgshow(fname,img):
  cv2.imshow(fname,img)
  kk=cv2.waitKey(1000)
  cv2.destroyAllWindows()
  #plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
  #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
  #plt.show()
    
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
          imgshow(filename,img)
          i=i+1
        elif k==ord('s'):
          print("stop_preview")
          camera.stop_preview()
        elif k==ord('v'):
          print("start_preview")
          camera.start_preview()
        elif k==ord('7'):
          print("1024x768")
          camera.resolution=(1024,768) 
        elif k==ord('6'):
          print("640x480")
          camera.resolution=(640,480)
        elif k==ord('3'):
          print("320x240")
          camera.resolution=(320,240)
        elif k==ord('9'):
          print("1920x1080")
          camera.resolution=(1920,1080) 
        else:
          ret=1
        return ret,i
    
#cv2.startWindowThread()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8000))   
    
with picamera.PiCamera() as camera:
    camera.resolution=(320,240)
    camera.start_preview()
    print("Press Key g to Save")
    #time.sleep(20)
    i=0
    while True:
        #k=cv2.waitKey(500) & 0xff
        #k=m.getch()
        #k=wait()
        k=socket_wait_id(server_socket)
        print(k)
        ret,i=proc_cam(camera,k,i)
        if(ret==00):
          break
        else:
          continue        
    camera.stop_preview()
    
server_socket.close()

