import numpy as np

arr=np.array(range(100000))
np.set_printoptions(threshold=np.inf) # or threshold=np.nan
print(arr)