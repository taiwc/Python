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

filename="/home/pi/Python/imageTest.jpg"
filename1="/home/pi/Python/imageChess.jpg"
filenameCal="/home/pi/Python/imageCal.jpg"
           
with picamera.PiCamera() as camera:
    #camera.resolution=(640,480)
    camera.start_preview()
    print("Press Key to Save")
    #time.sleep(20)
    k=cv2.waitKey(0) & 0xff
    camera.stop_preview()

with picamera.PiCamera() as camera:
    camera.start_preview()
    try:      
      camera.capture(filename)
      print(filename)
    finally:
        camera.stop_preview()

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
row=9
col=6
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((col*row,3), np.float32)
objp[:,:2] = np.mgrid[0:row,0:col].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, (row,col),None)

# If found, add object points, image points (after refining them)
while True:
    objpoints.append(objp)
    corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
    imgpoints.append(corners2)
    # Draw and display the corners
    img = cv2.drawChessboardCorners(img, (row,col), corners2,ret)
    cv2.imwrite(filename1,img)
    print(filename1)
    cv2.imshow('img',img)
    k=cv2.waitKey(33)
    #Camera Calibration
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints,imgpoints,gray.shape[::-1],None,None)
    ##find the rotation and translation vector
    #rvecs, tvecs, inliers = cv2.solvePnPRansac(objpoints,imgpoints,mtx,dist)
    print("R=",rvecs)
    print("T=",tvecs)
    print("M=",mtx)
    print("D=",dist)
    # undistort
    h,w=img.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
    print("M1=",newcameramtx)
    print("ROI=",roi)
    dst=cv2.undistort(img,mtx,dist,None,newcameramtx)
    #x,y,w,h=roi
    #dst=dst[y:y+h,x:x+w]
    cv2.imwrite(filenameCal,dst)
else:
  print("No Chess board found!")
  
cv2.destroyAllWindows()
