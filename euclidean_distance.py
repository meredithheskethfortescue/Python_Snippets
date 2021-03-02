#!/usr/bin/env python3
"""Calculate the euclidean distance between two points"""

import numpy as np

a, b = np.array([1, 1]), np.array([2, 2])
distance = np.linalg.norm(a - b)

print(distance)
