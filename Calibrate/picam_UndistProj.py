# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 07:55:58 2017

@author: ASUS
"""

import numpy as np
import cv2
import glob

row=9
col=6
gsize=20 #mm
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((col*row,3), np.float32)
objp[:,:2] = np.mgrid[0:row,0:col].T.reshape(-1,2)
objp[:,:2] = objp[:,:2]*gsize

rvecs=np.loadtxt("rvecs.txt")
tvecs=np.loadtxt("tvecs.txt")
mtx=np.loadtxt("mtx.txt")
dist=np.loadtxt("dist.txt")
newcameramtx=np.loadtxt("newcameramtx.txt")
roi=np.loadtxt("roi.txt")

print("R=",rvecs)
print("T=",tvecs)
print("M=",mtx)
print("D=",dist)
print("M1=",newcameramtx)
print("ROI=",roi)

images = glob.glob('*.jpg')

for fname in images:
    print(fname)
    img = cv2.imread(fname)
    dst=cv2.undistort(img,mtx,dist,None,newcameramtx)
    fname1="UndistJPG"+"/"+fname
    cv2.imwrite(fname1,dst)
    img = cv2.imread(fname1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('img',img)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (row,col),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        print(fname," Chess Ok")
        #objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        #imgpoints.append(corners2)
