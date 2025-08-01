import numpy as np

a = np.array([[0,1,2,3],
              [4,5,6,7],
              [8,9,10,11],
              [12,13,14,15]])

print(a[:, 2])
#Third col: [2 6 10 14]

print(a[1, :])
# Second row: [4 5 6 7]

print(a[:, :-1])
# of a print all rows and columns
#exept the last column in all rows

print(a[:-2])
#of variable a, make a list and put all rows but excluding the last two
#(all columns is default)



