
#Multidimensional arrays

import numpy as np
a = np.array([[1,2], [3,4]])
print(a)
print(a.shape)

print(a[0])
print(a[0][0])
print(a[0,0])
print(a[:,0]) 
print(a[0,:]) 
print(a.T)
b = np.array([[3, 4], [5,6]])
c = a.dot(b)
print(c)
d = a * b
print(d)
b = np.array([[1,2,3], [4,5,6]])
c = np.linalg.det(a)
print(c)
c = np.linalg.inv(a)
print(c)
c = np.diag(a)
print(c)
c = np.diag([1,4])
print(c) 
