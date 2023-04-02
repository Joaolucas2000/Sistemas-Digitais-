#generate arrays

import numpy as np
a = np.zeros((2,3))
b = np.ones((2,3))
print(a)
print(b)
a = 5 * np.ones((3,3))
print(a)
a = np.full((3,3),5.0)
print(a)
a = np.eye(3)
print(a)
a = np.arange(10)
print(a)
a = np.linspace(0, 10, 5)
print(a) 
