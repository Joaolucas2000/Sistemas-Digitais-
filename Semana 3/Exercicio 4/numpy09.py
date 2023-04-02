#Reshape
import numpy as np
a = np.arange(1, 7)
print(a)
b = a.reshape((2, 3))
print(b)
b2 = a.reshape((3, 2))
print(b2)
print(a.shape)
b3 = a[np.newaxis, :]
print(b3)
print(b3.shape)
b4 = a[:, np.newaxis]
print(b4)
print(b4.shape) 
