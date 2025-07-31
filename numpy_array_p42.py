import numpy as np

#Creating a 1D array from a list
a = np.array([1,2,3])
print(a)
"""
[1 2 3]
"""

# Creating a 2D array from a list of lists
b = np.array([[1, 2],
              [3, 4]])

print(b)
"""
[[1 2]
 [3 4]]
"""

#Creating a 3D array from a list of lists of lists
c = np.array([[[1,2], [3,4]],
              [[5,6], [7,8]]])
print(c)
"""
[[[1 2]
    [3 4]
[[5 6]
  [7 8]]]
"""

