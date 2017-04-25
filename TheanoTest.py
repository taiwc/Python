# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:49:37 2017

@author: ASUS
"""

from theano import function, config, shared, sandbox
import theano.tensor as T
import numpy
import time

t1=time.time()
vlen=10*30*768 #10 x #cores x # threads per core
iters=10000

#config.floatX='float32'

rng=numpy.random.RandomState(2)
kk=rng.rand(vlen)
kk1=rng.rand(vlen)
yy=numpy.asarray(kk,config.floatX)
yy1=numpy.asarray(kk1,config.floatX)
x=shared(yy1)
x_count=T.exp(x)
f=function(inputs=[],outputs=x_count,givens={x: yy1})

print (f.maker.fgraph.toposort())
#t0=time.time()

for i in range(iters):
    r=f()
    
t0=time.time()

print ('Loop %d times took %f seconds' % (iters, t1-t0))
print ('Input is kk=', kk )
print ('Input is yy=', yy )
print ('Input is yy1=', yy1 )
print ('Input is x=', x.get_value() )
print ('Result is r=', r)
if numpy.any([isinstance(x.op,T.Elemwise) for x in f.maker.fgraph.toposort()]):
    print ('Used the cpu')
else:
    print ('used the gpu')
    
print(time.time()-t1)
