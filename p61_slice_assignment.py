import numpy as np

a = np.array([4] * 16)

a[1:8:2] = 16
print(a)
#start:stop:skip every other from index 1 to 8 with 16

a = np.array([1, 2, 3, 4, 5, 6])
print(a.reshape((2,3)))
'''
reshape a int n rows and columns as given by reshape(a,b)
'''

a = np.array([1, 2, 3, 4, 5, 6])
print(a.reshape((2, -1)))
'''
-1 tells reshape() to choose the suitable dimension for reshape(2, b).
'''





