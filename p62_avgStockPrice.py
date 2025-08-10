import numpy as np

# daily stock prices
# [morning, midday, evening]
solar_x = np.array(
    [[1, 2, 3], # today
     [2, 2, 5]]) # yesterday

# midday - weighted_average
print(np.average(solar_x, axis=0))
# [1.5 2. 4. ]

'''
each method usually always has unique parameters in contrast to other methods,
so it's important to read the documentation on each function so I know what the parameters do.
in this example average() has the a parameter called axis=, which sets the result on axis=n
'''





    
