# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 09:22:15 2017

@author: ASUS
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from OLSGD import LinearRegressionGD
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RANSACRegressor

def lin_regplot(X,y,model):
    plt.scatter(X,y,c='blue')
    plt.plot(X,model.predict(X),color='red')
    return None

df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',header=None,sep='\s+')
df.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
df.head()

sns.set(style='whitegrid',context='notebook')
cols=['LSTAT','INDUS','NOX','RM','MEDV']
sns.pairplot(df[cols],size=2.5);
plt.show()

print(df[:5])

cm=np.corrcoef(df[cols].values.T)
sns.set(font_scale=1.5)
hm=sns.heatmap(cm,cbar=True,annot=True,square=True,fmt='.2f',annot_kws={'size':15},yticklabels=cols,xticklabels=cols)
plt.show()

X=df[['RM']].values
y=df['MEDV'].values
sc_x=StandardScaler()
sc_y=StandardScaler()
X_std=sc_x.fit_transform(X)
y_std=sc_y.fit_transform(y)
lr=LinearRegressionGD()
lr.fit(X_std,y_std)
plt.plot(range(1,lr.n_iter+1),lr.cost_)
plt.ylabel('SSE')
plt.xlabel('Epoch')
plt.show()

lin_regplot(X_std,y_std,lr)
plt.xlabel('Average number of rooms [RM] (standardized)')
plt.ylabel('Price in $1000\'s [MEDV] (standarized)')
plt.show()

num_room_std=sc_x.transform([5.0])
price_std=lr.predict(num_room_std)
print("Price in $1000's: %.3f" % sc_y.inverse_transform(price_std))
print('Slope: %.3f' % lr.w_[1])
print('Intercept: %.3f' % lr.w_[0])

slr=LinearRegression()
slr.fit(X,y)
print('Slop:%.3f'%slr.coef_[0])
print('Intercept:%.3f'%slr.intercept_)
lin_regplot(X,y,slr)
plt.xlabel('Average number of rooms [RM] (standardized)')
plt.ylabel('Price in $1000\'s [MEDV] (standarized)')
plt.show()

ransac=RANSACRegressor(LinearRegression(),max_trials=100,min_samples=50,residual_metric=lambda x: np.sum(np.abs(x),axis=1),residual_threshold=5.0,random_state=0)
ransac.fit(X,y)
inlier_mask=ransac.inlier_mask_
outlier_mask=np.logical_not(inlier_mask)
line_X=np.arange(3,10,1)
line_y_ransac=ransac.predict(line_X[:,np.newaxis])
plt.scatter(X[inlier_mask],y[inlier_mask],c='blue',marker='o',label='Inliers')
plt.scatter(X[outlier_mask],y[outlier_mask],c='lightgreen',marker='s',label='Outliers')
plt.plot(line_X,line_y_ransac,color='red')
plt.xlabel('Average number of rooms [RM] (standardized)')
plt.ylabel('Price in $1000\'s [MEDV] (standarized)')
plt.legend(loc='upper left')
plt.show()
print('Slop:%.3f'%ransac.estimator_.coef_[0])
print('Intercept:%.3f'%ransac.estimator_.intercept_)