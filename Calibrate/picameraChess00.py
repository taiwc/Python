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
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((col*row,3), np.float32)
objp[:,:2] = np.mgrid[0:row,0:col].T.reshape(-1,2)
objp[:,:2] = objp[:,:2]*gsize

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


images = glob.glob('*.jpg')

for fname in images:
    print(fname)
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('img',img)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (row,col),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        print(fname," Chess Ok")
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        
        # Draw and display the corners
        #img = cv2.drawChessboardCorners(img, (row,col), corners2,ret)
        #cv2.imshow('imgchess',img)
        #cv2.waitKey(500)

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
cv2.imwrite("undist.jpg",dst)
np.savetxt("rvecs.txt",rvecs)
np.savetxt("tvecs.txt",tvecs)
np.savetxt("mtx.txt",mtx)
np.savetxt("dist.txt",dist)
np.savetxt("newcameramtx.txt",newcameramtx)
np.savetxt("roi.txt",roi)
np.savez("objpoints",objpoints)
np.savez("imgpoints",imgpoints)

mean_error=0
tot_error=0
for i in range(len(objpoints)):
    imgpoints2, _=cv2.projectPoints(objpoints[i],rvecs[i],tvecs[i],mtx,dist)
    error=cv2.norm(imgpoints[i],imgpoints2,cv2.NORM_L2)/len(imgpoints2)
    tot_error+=error

print("total error:",meanerror/len(objpoints))
      

cv2.destroyAllWindows()
