
#Concatenacion

import numpy as np
a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5, 6]])
print(b)
c = np.concatenate((a, b), axis=None)
print(c)

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.hstack((a,b))
print(c)
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
c = np.hstack((a,b))
print(c)
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.vstack((a,b))
print(c)
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
c = np.vstack((a,b))
print(c) 
