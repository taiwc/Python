# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:54:03 2017

@author: ASUS
"""

from ch12_344 import NeuralNetMLP
from ch12_363 import MLPGradientCheck
import os
import struct
import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt1

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

#nn=NeuralNetMLP(n_output=10,n_features=X_train.shape[1],n_hidden=50,l2=0.1
#    ,l1=0.0,epochs=1000,eta=0.001,decrease_const=0.00001
#    ,shuffle=True,minibatches=50,random_state=1)
#nn.fit(X_train,y_train,print_progress=True)

nn_check=MLPGradientCheck(n_output=10,n_features=X_train.shape[1],n_hidden=10,l2=0.0
    ,l1=0.0,epochs=10,eta=0.001,decrease_const=0.0
    ,shuffle=True,minibatches=1,random_state=1)
nn_check.fit(X_train[:5],y_train[:5],print_progress=False)