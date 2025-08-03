import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
"""
[1, 2, 3, 4]
"""
print(a.shape)
# (4,) -this means the dimension shape of the array is by default 1 row, with 4 elements in the 1st row.

b = np.array([[2, 1, 2], [3, 2, 3], [4, 3, 4]])
print(b)
"""
[[2 1 2]
 [3 2 3]
 [4 3 4]]
"""

print(b.shape)
# since this array has rows and columns it will be (3,3)

c = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
               [[1, 2, 4], [2, 3, 5], [3, 4, 6]]])
print(c)
"""
[[[ 1 2 3]
  [2 3 4]
  [3 4 5]

[[1 2 4]
 [2 3 5]
 [3 4 6]
"""

print(c.shape)
#there are a max 3 sets of arrays (nested multi dimensional), so the print will give (2, 3, 3)
#this concludes 1D,2D,3D numpy arrays / matrices.             
             
