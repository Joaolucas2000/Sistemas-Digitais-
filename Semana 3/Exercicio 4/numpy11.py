#Broadcasting

import numpy as np

x = np.array([[1,2,3], [4,5,6], [1,2,3], [4,5,6]])
a = np.array([1, 0, 1])
y = x + a  # Add v to each row of x using broadcasting
print(y)  
