# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 15:26:29 2017

@author: ASUS
"""
import theano
from theano import tensor as T

import numpy as np
import matplotlib.pyplot as plt

def train_linreg(X_train,y_train,eta,epochs):
    costs=[]
    #Initialize arrays
    eta0=T.fscalar('eta0')
    y=T.fvector(name='y')
    X=T.fmatrix(name='X')
    w=theano.shared(np.zeros(shape=(X_train.shape[1]+1),dtype=theano.config.floatX),name='w')
    #calculate cost
    net_input=T.dot(X,w[1:])+w[0]
    errors=y-net_input
    cost=T.sum(T.pow(errors,2))
    #perform gradient update
    gradient=T.grad(cost,wrt=w)
    update=[(w,w-eta0*gradient)]
    #compile model
    train=theano.function(inputs=[eta0],outputs=cost,updates=update,givens={X:X_train,y:y_train,})
    for _ in range(epochs):
        costs.append(train(eta))
        
    return costs,w
 
def predict_linreg(X,w):
    Xt=T.matrix(name='X')
    net_input=T.dot(Xt,w[1:])+w[0]
    predict=theano.function(inputs=[Xt],givens={w:w},outputs=net_input)
    return predict(X)
   
theano.config.floatX='float32'
X_train=np.asarray([[0.0],[1.0],
                        [2.0],[3.0],
                        [4.0],[5.0],
                        [6.0],[7.0],
                        [8.0],[9.0]],dtype=theano.config.floatX)
y_train=np.asarray([1.0,1.3,
                        3.1,2.0,
                        5.0,6.3,
                        6.6,7.4,
                        8.0,9.0],dtype=theano.config.floatX)
                        
costs,w =train_linreg(X_train=X_train,y_train=y_train,eta=0.001,epochs=10)
plt.plot(range(1,len(costs)+1),costs)
plt.tight_layout()
plt.xlabel('Epoch')
plt.ylabel('Cost')
plt.show()

print(w.get_value())
plt.scatter(X_train,y_train,marker='s',s=50)
net_data=predict_linreg(X_train,w)
plt.plot(range(X_train.shape[0]),net_data,color='gray',marker='o',markersize=4,linewidth=3)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


print(costs)
print(X_train)
print(y_train)


    