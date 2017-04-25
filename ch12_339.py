# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:16:57 2017

@author: ASUS
"""

import os
import struct
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1

def load_mnist(path,kind='train'):
    """load MNIST data from 'path'"""
    labels_path=os.path.join(path,'%s-labels.idx1-ubyte' % kind)
    images_path=os.path.join(path,'%s-images.idx3-ubyte' % kind)
    with open(labels_path,'rb') as lbpath:
        magic, n = struct.unpack('>II',lbpath.read(8))
        labels = np.fromfile(lbpath,dtype=np.uint8)
        
    with open(images_path,'rb') as imgpath:
        magic, num, rows, cols = struct.unpack(">IIII",imgpath.read(16))
        images=np.fromfile(imgpath,dtype=np.uint8).reshape(len(labels),784)
    
    return images,labels
    
X_train, y_train=load_mnist('mnist',kind='train')
print('Row:%d, columns:%d' % (X_train.shape[0],X_train.shape[1]))

X_test, y_test=load_mnist('mnist',kind='t10k')
print('Rows:%d, columns:%d' % (X_test.shape[0],X_test.shape[1]))

fig, ax = plt.subplots(nrows=2,ncols=5,sharex=True,sharey=True)
ax=ax.flatten()
for i in range(10):
    img=X_train[y_train==i][0].reshape(28,28)
    ax[i].imshow(img,cmap='Greys',interpolation='nearest')
ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()

fig1, ax1 = plt1.subplots(nrows=5,ncols=5,sharex=True,sharey=True)
ax1=ax1.flatten()
for j in range(25):
    img1=X_train[y_train==7][j].reshape(28,28)
    ax1[j].imshow(img1,cmap='Greys',interpolation='nearest')
    
ax1[0].set_xticks([])
ax1[0].set_yticks([])
plt1.tight_layout()
plt1.show()

