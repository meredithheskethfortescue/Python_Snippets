#!/usr/bin/env python3
"""Get the central value in an array (aka centerpoint)
This solution assumes that the array has an odd length and i.e. a single central index exists.
"""

import numpy as np

arr = np.array([[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]])

assert arr.size % 2  # odd length only

# put a value to the center 
np.put(arr, arr.size // 2, 999)
print(arr)

# take a value from the center
center = np.take(arr, arr.size // 2)
print(center)
