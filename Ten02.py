# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:32:54 2017

@author: ASUS
"""
#import json
from sklearn import metrics, cross_validation
import tensorflow as tf
from tensorflow.contrib import learn

#def bad_filename(filename):
#    return repr(filename)[1:-1]
    
#json.loads('"\\ud83d\\ude02"')
#def main(unused_argv):
iris=learn.datasets.load_dataset('iris')
#x_train, x_test, y_train, y_test=cross_validation.train_test_split(iris.data,iris.target,test_size=0.2,random_state=42)
#classifier=learn.DNNClassifier(hidden_units=[10,20,10],n_classes=3)
#classifier.fit(x_train,y_train,steps=200)
#score=metrics.accuracy_score(y_test,classifier.predict(x_test))
#print('Accuracy:{0:f}'.format(score).encode("utf-8", "surrogateescape"))
#print('Accuracy:{0:f}'.format(score))