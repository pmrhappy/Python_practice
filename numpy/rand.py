# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:46:15 2016

@author: A30294
"""

import numpy as np

result = np.array([])
base_low = -5
diff = 2
factor = 1

profile_num = 4

np.random.seed(profile_num)
for i in range(1, 11):
    if (base_low + diff) >= 5:
        high_value = 5
    else:
        high_value = base_low + diff
    new_arr = np.random.randint(low=base_low, high=high_value+1, size=(10))
    result = np.append(result, new_arr)
    if i%2 == 0:
        base_low += 1
    diff += 1

result = result[::-1]
for r in range(len(result)):
    print(r+1, " ", result[r])