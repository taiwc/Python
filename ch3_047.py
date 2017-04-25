# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:59:46 2017

@author: wtai
"""

from sklearn import datasets
import numpy as np
iris=datasets.load_iris()
X=iris.data[:,[2,3]]
y=iris.target
