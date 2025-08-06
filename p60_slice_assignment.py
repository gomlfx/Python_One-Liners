import numpy as np

a = np.array([4] * 16)
print(a)
# creates an array with the value 4 sixteen times

a[1::] = [42] * 15
print(a)
# a[start:stop:step]






