import numpy as np

x = np.array([[1, 0, 0],
              [0, 2, 2],
              [3, 0, 0]])

print(np.nonzero(x))
#nonzero() reads columns by rows, then rows by rows, to identify nonzero elements.
