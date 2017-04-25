# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 07:55:58 2017

@author: ASUS
"""

import numpy as np
import cv2
import glob

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
