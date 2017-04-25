# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:25:59 2017

@author: wtai
"""
import numpy as np

class LinearRegressionGD(object):
    """Adaptive Linear NEuron classifier.
    Parameters:
    eta: float (Learning rate 0.0 ~ 1.0)
    n_iter: int (Passes over the training data)
    Attributes:
    w_:1d-array (weights after fitting)
    error_:list (number of misclassifications in every epoch)    
    """
    def __init__(self,eta=0.001,n_iter=20):
        self.eta=eta
        self.n_iter=n_iter
        
    def fit(self,X,y):
        """
        Fit training data.
        Parameters:
        X:{array-like},shape=[n_sample,n_features]
        y:array-like, shape=[n_samples]
        Returns:
        self:object
        """
        self.w_=np.zeros(1+X.shape[1])
        self.cost_=[]

        for i in range(self.n_iter):
            output=self.net_input(X)
            errors=(y-output)
            self.w_[1:]+=self.eta*X.T.dot(errors)
            self.w_[0]+=self.eta*errors.sum()
            cost=(errors**2).sum()/2.0
            self.cost_.append(cost)
        return self
        
    def net_input(self,X):
        """Calculate net input"""
        return np.dot(X,self.w_[1:])+self.w_[0]
                      
    #def activation(self,X):
    #    """Compute linear activation"""
    #    return self.net_input(X)
        
    def predict(self,X):
        """Return class label without unit step"""
        return self.net_input(X)
        
