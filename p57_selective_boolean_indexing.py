import numpy as np

#sets the base array
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

#makes the filter we will use to choose elements from the base array and make the new array
indices = np.array([[False, False, True],
                    [False, False, False],
                    [True, True, False]])

#print the result of the filter
print(a[indices])





