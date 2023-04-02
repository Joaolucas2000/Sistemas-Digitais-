# Array indexing/Slicing/Boolean
import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
b = a[0,1]
print(b)
row0 = a[0,:]
print(row0)
col0 = a[:, 0]
print(col0)
slice_a = a[0:2,1:3]
print(slice_a)
last = a[-1,-1]
print(last)
a = np.array([[1,2], [3, 4], [5, 6]])
print(a)

bool_idx = a > 2
print(bool_idx)
print(a[bool_idx])
print(a[a > 2])
b = np.where(a>2, a, -1)
print(b)

a = np.array([10,19,30,41,50,61])
print(a)
b = a[[1,3,5]]
print(b)
even = np.argwhere(a%2==0).flatten()
print(even)
a_even = a[even]
print(a_even) 
