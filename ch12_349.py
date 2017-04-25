# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:41:33 2017

@author: ASUS
"""
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import numpy as np

plt.plot(range(len(nn.cost_)),nn.cost_)
plt.ylim([0,2000])
plt.ylabel('Cost')
plt.xlabel('Epochs*50')
plt.tight_layout()
plt.show()

batches=np.array_split(range(len(nn.cost_)),1000)
cost_ary=np.array(nn.cost_)
cost_avgs=[np.mean(cost_ary[i]) for i in batches]
plt.plot(range(len(cost_avgs)),cost_avgs,color='red')
plt.ylim([0,2000])
plt.ylabel('Cost')
plt.xlabel('Epochs')
plt.tight_layout()
plt.show()

y_train_pred=nn.predict(X_train)
acc=np.sum(y_train==y_train_pred,axis=0)/X_train.shape[0]
print('Training accurcay for train set:%.2f%%' % (acc*100))

y_test_pred=nn.predict(X_test)
acc=np.sum(y_test==y_test_pred,axis=0)/X_test.shape[0]
print('Training accuracy for test set: %.2f%%' % (acc*100))

miscl_img=X_test[y_test!=y_test_pred][:25]
correct_lab=y_test[y_test!=y_test_pred][:25]
miscl_lab=y_test_pred[y_test!=y_test_pred][:25]

fig,ax=plt1.subplots(nrows=5,ncols=5,sharex=True,sharey=True)
ax=ax.flatten()
for i in range(25):
    img=miscl_img[i].reshape(28,28)
    ax[i].imshow(img,cmap='Greys',interpolation='nearest')
    ax[i].set_title('%d) t:%d p:%d' % (i+1, correct_lab[i],miscl_lab[i]))
    
ax[0].set_xticks([])
ax[0].set_yticks([])
plt1.tight_layout()
plt1.show()