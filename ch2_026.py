import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Perceptron import Perceptron
from plot_decision_regions import plot_decision_regions
from Adaline import AdalineGD

df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None,engine='python')
df.tail()
y=df.iloc[0:100,4].values
y=np.where(y=='Iris-setosa',-1,1)
x=df.iloc[0:100,[0,2]].values
plt.scatter(x[:50,0],x[:50,1],color='red',marker='o',label='setosa')
plt.scatter(x[50:100,0],x[50:100,1],color='blue',marker='x',label='versicolor')
plt.xlabel('petal length')
plt.ylabel('setpal length')
plt.legend(loc='upper left')
plt.show()
ppn=Perceptron(eta=0.1,n_iter=10)
ppn.fit(x,y)
plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassification')
plt.show()
print("w=",ppn.w_,"\n")
plot_decision_regions(x,y,classifier=ppn)
plt.xlabel('sepal length[cm]')
plt.ylabel('petal length[cm]')
plt.legend(loc='upper left')
plt.show()
fig, ax=plt.subplots(nrows=1,ncols=2,figsize=(8,4))
ada1=AdalineGD(n_iter=10,eta=0.01).fit(x,y)
print("w=",ada1.w_,"\n")
ax[0].plot(range(1,len(ada1.cost_)+1),np.log10(ada1.cost_),marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Sum-squred-erroe)')
ax[0].set_title('Adaline-Learning rate 0.01')
ada2=AdalineGD(n_iter=10,eta=0.0001).fit(x,y)
print("w=",ada2.w_,"\n")
ax[1].plot(range(1,len(ada2.cost_)+1),ada2.cost_,marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('Sum-squred-erroe')
ax[1].set_title('Adaline-Learning rate 0.0001')
plt.show()
#print(x)
#print(y)
X_std=np.copy(x)
X_std[:,0]=(x[:,0]-x[:,0].mean())/x[:,0].std()
X_std[:,1]=(x[:,1]-x[:,1].mean())/x[:,1].std()
ada=AdalineGD(n_iter=15,eta=0.01)
ada.fit(X_std,y)
print("w=",ada.w_,"\n")
plot_decision_regions(X_std,y,classifier=ada)
plt.title('Adaline-Gradient')
plt.xlabel('sepal length[standardized]')
plt.ylabel('petal length[standardized]')
plt.legend(loc='upper left')
plt.show()
plt.plot(range(1,len(ada.cost_)+1),ada.cost_,marker='o')
plt.xlabel('Epochs')
plt.ylabel('Sum-squred-erroe')
plt.title('Adaline-Gradient')
plt.show()