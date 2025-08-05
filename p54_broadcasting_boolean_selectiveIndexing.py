
##Dependencies
import numpy as np

## Data: air quality index AQI data (row = city)
X = np.array(
    [[ 42, 40, 41, 43, 44, 43 ], # Hong Kong
     [ 30, 31, 29, 29, 29, 30 ], #New York
     [8, 13, 31, 11, 11, 9 ], # Berlin
     [11, 11, 12, 13, 1, 12]]) # Montreal

cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

## One-liner
polluted = set(cities[np.nonzero(X > np.average(X))[0]])
"""
since > is boolean, it will return 0 or 1 for False or True, so then np.nonzero()
can check if it is a nonzero True of False, set() converts a list or array
into a set, an unordered collection of unique elements to ensure no duplicate elements.
"""

## Result
print(polluted)

"""
let's print the insides that happen before the main result that is reported above.
"""
print(X > np.average(X))
"""
this returns True or False
"""

print(np.nonzero(X > np.average(X)))
"""
since True is 1, nonzero() will report this as true or 1, nonzero() counts by row element-wise during row or column
element-wise counts. Since bool (True False) is also 0 or 1, it is under dtype=int64
"""

print(cities[np.nonzero(X > np.average(X))[0]])
"""
advanced indexing, [0] extracts the string name for each element in the array,
notice at this point there are duplicates, so use set() to remove duplicates.
"""




