#Dependencies
import numpy as np

##Data: popular Instagram accounts (millions followers)
inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriasecret"],
                 [120, "@cristiano"],
                 [76, "@nike"]])

## One-liner, mask index array 
superstars = inst[inst[:,0].astype(float) > 100, 1]

## Results
print(superstars)





