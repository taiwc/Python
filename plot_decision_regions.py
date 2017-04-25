# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 10:13:10 2017

@author: ASUS
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_decision_regions(X,y,classifier,resolution=0.02):
    #setup
    markers=('s','x','o','^','v')
    colors=('red','blue','lightgreen','gray','cyan')
    uny=np.unique(y)
    cmap=ListedColormap(colors[:len(uny)])
    #plot
    x1_min,x1_max=X[:,0].min()-1,X[:,0].max()+1
    x2_min,x2_max=X[:,1].min()-1,X[:,1].max()+1
    xx1,xx2=np.meshgrid(np.arange(x1_min,x1_max,resolution),np.arange(x2_min,x2_max,resolution))
    Z=classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    Z=Z.reshape(xx1.shape)
    plt.contourf(xx1,xx2,Z,alpha=0.4,cmap=cmap)
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())
    #plot class samples
    #print("X=",X,"\n")
    #print("y=",y,"\n")
    #print("uny=",uny,"\n")
    for idx, c1 in enumerate(uny):
        k=(y==c1)
        #print("idx=",idx,"k=",k,"c1=",c1,"\n")
        sx=X[k,0]
        sy=X[k,1]
        #print("sx=",sx,"sy=",sy,"\n")
        plt.scatter(sx,sy,alpha=0.8,c=cmap(idx),marker=markers[idx],label=c1)
        
    