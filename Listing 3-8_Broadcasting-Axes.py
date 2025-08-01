import numpy as np

a = np.array([1,2,3,4])
print(a.ndim)
#a.ndim counts how many dimensions, dimensions are how deep nested lists go.

b = np.array([[2, 1, 2], [3, 2, 3,], [4, 3, 4]])
print(b.ndim)
#This nested list is only two arrays deep.

c = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
              [[1, 2, 4], [2, 3, 5], [3, 4, 6]]])
print(c.ndim)
#how deep is the deepest array? 3. So the dimension is 3.









