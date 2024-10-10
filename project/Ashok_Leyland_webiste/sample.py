import numpy as np

a = np.random.rand(4,3)
y = np.sum(a,axis = 0,keepdims = True)
print(y.shape)