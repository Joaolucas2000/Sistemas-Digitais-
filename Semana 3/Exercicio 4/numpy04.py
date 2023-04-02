#Array vs list

import numpy as np

l = [1,2,3]
a=np.array([1,2,3])

l = l * 2
print(l)
a = a * 2
a= a + np.array([4])
print (a) 
