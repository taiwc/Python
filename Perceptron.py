# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 10:09:56 2017

@author: ASUS
"""

import numpy as np

class Perceptron(object):
    """Perceptron classifier.
    Prameters 
    eta: float (learning rate 0.0 to 1.0)
    n_iter: int (passes over training data)
    Attributes
    w_:1d-array (weighting after fitting)
    errors_:list (Number of misclassifications in every epoch)    
    """
    def __init__(self,eta=0.01,n_iter=10):
        self.eta=eta
        self.n_iter=n_iter
        
    def fit(self,X,Y):
        """Fit training data.
        Parmeters
        X:{array-like}, shape = [n_samples,n_features
        Y:array-like,shape=[n_sample]]
        Returns
        self:object
        """
        self.w_=np.zeros(1+X.shape[1])
        self.errors_=[]
        
        for _ in range(self.n_iter):
            errors=0
            for xi, target in zip(X,Y):
                update=self.eta*(target-self.predict(xi))
                self.w_[1:]+=update*xi
                self.w_[0]+=update
                errors+=int(update!=0.0)
            self.errors_.append(errors)
        return self
        
    def net_input(self,X):
        """Calculate net input"""
        return np.dot(X,self.w_[1:])+self.w_[0]
        
    def predict(self,X):
        """Return class label after unit step"""
        return np.where(self.net_input(X)>=0.0,1,-1)
    